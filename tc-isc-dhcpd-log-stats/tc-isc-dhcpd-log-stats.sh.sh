#!/bin/sh
#
# peritus-tc-tools/tc-isc-dhcpd-log-stats.sh
# Count matching lines in ISC dhcpd log files
# and output it to OpenTSDB tcollector
#
# 2014-04-06 Stian Ovrevage <stian@peritusconsulting.no>
# 
# This script will simply grep words and sequences corresponding to
# dhcp-events from the ISC dhcpd log file.
#
# Instructions:
#   Put this file into a tcollector/collectors/XX/ folder where XX is how
#   often you want the script to run. 300 should be reasonable and gives
#   statistics every 5 minutes. Make sure the script is runnable.
#
# Requirements:
#   Be sure to enable logging in your dhcpd.conf:
#      log-facility local7
#   And log to a separate file in Xsyslog.conf:
#      local7.debug    /var/log/dhcpd.log
#   And to rotate the log file so that it will not fill your disks, or violate
#   customer privacy, /etc/logrotate.d/dhcpd:
#  
#      /var/log/dhcpd.log {
#          compress
#          dateext
#          maxage 365
#          daily
#          rotate 14
#          postrotate
#              /etc/init.d/rsyslog reload
#          endscript
#      }
# 

# instance tag sent with metrics, usefull if you have
# several instances, for example ipv4 and ipv6 
TAG_INSTANCE=ipv4

# dhcpd logfile location, default is /var/log/dhcpd.log
DHCPD_LOGFILE=/var/log/dhcpd.log

TAG_HOST=`hostname`


STARTTIME=$(date +%s%N)

echo dhcp.events.discover `date +%s` `grep DHCPDISCOVER $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.events.offer `date +%s` `grep DHCPOFFER $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.events.request `date +%s` `grep DHCPREQUEST $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.events.ack `date +%s` `grep DHCPACK $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.events.nak `date +%s` `grep DHCPNAK $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.events.release `date +%s` `grep DHCPRELEASE $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.events.inform `date +%s` `grep DHCPINFORM $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE

echo dhcp.events.addforwardmap `date +%s` `grep "Added new forward map from" $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.events.removeforwardmap `date +%s` `grep "Removed forward map from" $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE

echo dhcp.errors.noaddforwardmap `date +%s` `grep "Unable to add forward map from" $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.errors.noaddreversemap `date +%s` `grep "Unable to add reverse map from" $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.errors.notsec `date +%s` `grep "No tsec for use with key" $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.errors.bindupdatexidmismatch `date +%s` `grep "got ack from dhcp: xid mismatch" $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.errors.uidduplicate `date +%s` `grep "is duplicate on" $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE
echo dhcp.errors.bindupdaterejected `date +%s` `grep "incoming update is less critical than outgoing update" $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE

echo dhcp.errors.others `date +%s` `cat $DHCPD_LOGFILE | grep -v "DHCPDISCOVER" | grep -v "DHCPOFFER" | grep -v "DHCPREQUEST" | grep -v "DHCPACK" | grep -v "DHCPNAK" | grep -v "DHCPRELEASE" | grep -v "DHCPINFORM" | grep -v "Added new forward map from" | grep -v "Removed forward map from" | grep -v "Unable to add forward map from" | grep -v "Unable to add reverse map from" | grep -v "No tsec for use with key" | grep -v "got ack from dhcp: xid mismatch" | grep -v "is duplicate on" | grep -v "incoming update is less critical than outgoing update" | wc -l` host=$TAG_HOST instance=$TAG_INSTANCE

echo dhcp.total `date +%s` `cat $DHCPD_LOGFILE|wc -l` host=$TAG_HOST instance=$TAG_INSTANCE

ENDTIME=$(date +%s%N)

echo tcollector.collectors.isc-dhcpd-log-stats.elapsedtime `date +%s` "$((($ENDTIME - $STARTTIME) / 1000))" host=$TAG_HOST
