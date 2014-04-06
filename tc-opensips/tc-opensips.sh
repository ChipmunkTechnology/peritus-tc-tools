#!/bin/sh
# 
# peritus-tc-tools/tc-opensips/tc-opensips.sh
# Count some tables from opensips MySQL database
# and output it to OpenTSDB tcollector
#
# 2014-04-06 Stian Ovrevage <stian@peritusconsulting.no>
#
# This script will simply count the number of rows for some of the opensips
# tables and output the metrics in tcollector compatible format.
#
# It will also output a metric of its own running time in microseconds in
# order to evaluate performance over time as counting mysql-rows on huge
# databases might result in performance degradation.
#
# Instructions:
#   Put this file into a tcollector/collectors/XX/ folder where XX is how
#   often you want the script to run. 60 should be reasonable and gives
#   statistics every minute. Make sure the script is runnable.  
# 
#   You can run the script on the opensips server itself or another host.
#   Make sure you create a user with permissions to connect if using a 
#   remote host. And update the config below.
#
#   You can run the script itself on the command-line to verify that 
#   it is working properly.
# 

MYSQL_USER=
MYSQL_PASS=
MYSQL_HOST=localhost
MYSQL_DB=opensips

TAG_HOST=`hostname`

STARTTIME=$(date +%s%N)

echo opensips.subscribers `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM subscriber;" | mysql mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo opensips.locations `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM location;" | mysql mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST

ENDTIME=$(date +%s%N)

echo tcollector.collectors.opensips.elapsedtime `date +%s` "$((($ENDTIME - $STARTTIME) / 1000))" host=$TAG_HOST
