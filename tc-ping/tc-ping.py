#!/usr/bin/env python

"""

peritus-tc-tools/tc-ping/tc-ping.py - v 1.1.1
OpenTSDB tcollector wrapper for fping3

2014-08-23 Stian Ovrevage <stian@peritusconsulting.no>

Pings hosts every 3 seconds, outputs statistic every 10 seconds
which are formatted into OpenTSDB tcollector compatible format.
Metrics gathered:
  icmp.latency.avg
  icmp.latency.max
  icmp.latency.lossrate

For more information on fping:
http://fping.org/fping.1.html

fping output format:
  up.com : xmt/rcv/%loss = 1/1/0%, min/avg/max = 0.98/0.98/0.98
  down.org : xmt/rcv/%loss = 1/0/100%

"""

import subprocess
import time
import sys
import os.path
import socket

''' Text file containing hostnames or IPs to be pinged, one per line '''
hostfile = "/opt/tcollector/collectors/etc/hosts.txt"

'''
Interval between pings to an individual host, in milliseconds
Recommended 3000. 3 seconds.
'''
pinginterval = "3000"

'''
Interval between printing statistics, and hence, sending to OpenTSDB
Recommended 10 seconds.
'''
statsinterval = "10"

'''
Number of pings to send in one session. tcollector will re-start 
this script when it finishes and it will then re-read the host-list
Recommended 1200 pings. Will run each session 
for approx 1 hour before respawning.
'''
pingcount = "1200"

'''
Type-of-service byte. Used for QoS marking of packets. Good reference
and mapping og TOS-to-DSCP here: http://www.tucny.com/Home/dscp-tos
Default should be 0. DSCP cs4 (32) is TOS 128. DSCP ef (46) is TOS 184.
'''
tos = "0"

'''
Interface. Usefull for pinging hosts via different interfaces, such as wired
and wireless. Have a different tc-ping.py for each interface-value.
Default is empty for auto. Example: interface = "wlan0"
'''
interface = ""

''' host tag for metrics. Use system fqdn hostname by default '''
host = socket.getfqdn()

''' create interface tag string, if interface is defined '''
if len(interface) > 0:
  interface_tag = "interface=" + interface
else:
  interface_tag = ""


command = ['fping -I "' + interface + '" -B 1 -C ' + pingcount + ' -D -r0 -O ' + tos + ' -Q '
           + statsinterval + ' -p ' + pinginterval + ' < ' + hostfile]

def main():
    if not os.path.isfile(hostfile):
        print >> sys.stderr, 'error: '+hostfile+' does not exist'
        return 1

    try:
        p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, bufsize=0)
        line = p.stderr.readline()
        while line:
            ts = int(time.time())

            line = line.replace(':','')
            line = line.replace('=','')
            line = line.replace(',','')
            line = line.replace('%','')
            line = line.replace('/',' ')
            
            fields = line.split()
            
            # Only process lines including a "xmt", this excludes time lines etc
            if 'xmt' in fields:
                print("icmp.lossrate " + str(ts) + " " + fields[6] +
                      " host=" + host + " dsthost=" + fields[0] + " tos=" + tos + " " + interface_tag)
                # RTT numbers only included if at least one packet received:
                if 'avg' in fields:
                    print("icmp.latency.avg " + str(ts) + " " + fields[11] +
                          " host=" + host + " dsthost=" + fields[0] + " tos=" + tos + " " + interface_tag)
                    print("icmp.latency.max " + str(ts) + " " + fields[12] +
                          " host=" + host + " dsthost=" + fields[0] + " tos=" + tos + " " + interface_tag)

            line = p.stderr.readline()
        
    except OSError, err:
        print >> sys.stderr, 'Got execption running command "%s": %s' % (command, err)

if __name__ == "__main__":
    main()
