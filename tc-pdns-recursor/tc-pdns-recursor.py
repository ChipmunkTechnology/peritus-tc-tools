#!/usr/bin/env python

"""

peritus-tc-tools/tc-pdns-recursor/tc-pdns-recursor.py - v 1.0.0
OpenTSDB tcollector wrapper for PowerDNS Recursor

2015-06-18 Stian Ovrevage <stian@peritusconsulting.no>

Collects statistics from PowerDNS using 'rec_control'.

No metric name matching or parsing is done in this script
and should therefore be fully future compatible.

"""

import subprocess
import os
import sys
import time
import socket

COLLECTION_INTERVAL = 10

''' host tag for metrics. Use system fqdn hostname by default '''
host = socket.getfqdn()

def collect_stats():
    ''' Collects stats from pdns command line '''

    command = ['rec_control get-all']

    try:
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, bufsize=0)
        line = p.stdout.readline()
        ts = int(time.time())
        while line:
            fields = line.split()
            
            ''' If there is a second field, and it is a number, assume it is statistics and send it '''
            if(fields[1].isdigit()):
                print('pdns.' + fields[0] + " " + str(ts) + " " + fields[1] + " host=" + host)
            
            ''' Read next line '''
            line = p.stdout.readline()
        
    except OSError, err:
        print >> sys.stderr, 'Got execption running command "%s": %s' % (command, err)

def main():
  while True:
    collect_stats()
    time.sleep(COLLECTION_INTERVAL)

if __name__ == "__main__":
  sys.exit(main())
