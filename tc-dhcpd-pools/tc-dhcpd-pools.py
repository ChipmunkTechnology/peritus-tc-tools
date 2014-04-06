#!/usr/bin/env python

"""

peritus-tc-tools/tc-dhcpd-pools/tc-dhcpd-pools.py
OpenTSDB tcollector wrapper for dhcpd-pools

2014-04-06 Stian Ovrevage <stian@peritusconsulting.no>

Runs dhcpd-pools and extracts data on dhcp pool usage and 
formats into OpenTSDB/tcollector compatible format.

Metrics gathered:
    dhcpd.pool.size - Total pool size, number of IPs
    dhcpd.pool.usage.absolute - Current pool usage, number of IPs (dhcpd-pools "current" field)
    dhcpd.pool.usage.percent - Current pool usage in percent (dhcpd-pools "percent" field)
    dhcpd.pool.inactive - Inactive, expired or abandoned leases (dhcpd-pools "touch" field)
    dhcpd.pool.backup - Failover backup allocatable addresses (dhcpd-pools "bu" field)

    For more information on the different fields, see dhcpd-pools documentation at:
        http://dhcpd-pools.sourceforge.net/man.html

dhcpd-pools output format:
  Shared network: 
    "name","max","cur","percent","touch","t+c","t+c perc","bu","bu perc"
    "prov-kvh018-RosRaadhus","234","16","6.838","23","39","16.667","0","0.000"

"""

import subprocess
import time
import sys
import os.path
import socket


''' dhcpd.conf file. Default is /etc/dhcpd.conf '''
config_file = '/etc/dhcpd.master'

''' dhcpd.leases file. Default is /var/db/dhcpd.leases '''
lease_file = '/var/db/dhcpd.leases'

''' host tag for metrics. Use system fqdn hostname by default '''
host = socket.getfqdn()


command = ['/usr/local/bin/dhcpd-pools --limit 02 --format c --config '
           + config_file + ' --leases ' + lease_file]


def main():
    if not os.path.isfile(config_file):
        print >> sys.stderr, 'error: config_file "'+config_file+'" does not exist'
        return 1
    if not os.path.isfile(lease_file):
        print >> sys.stderr, 'error: lease_file "'+lease_file+'" does not exist'
        return 1

    try:
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, bufsize=0)
        line = p.stdout.readline()
        ts = int(time.time())               # Timestamp used when sending data
        while line:

            if len(line) > 1:                   # Only process lines with content

                line = line.replace('"','')     # Remove quotes
                fields = line.split(',')        # Split fields

                print("dhcpd.pool.size " + str(ts) + " " + fields[1]
                      + " host=" + host + " dhcppoolname=" + fields[0])
                print("dhcpd.pool.usage.absolute " + str(ts) + " " + fields[2]
                      + " host=" + host + " dhcppoolname=" + fields[0])
                print("dhcpd.pool.usage.percent " + str(ts) + " " + fields[3]
                      + " host=" + host + " dhcppoolname=" + fields[0])
                print("dhcpd.pool.inactive " + str(ts) + " " + fields[4]
                      + " host=" + host + " dhcppoolname=" + fields[0])
                print("dhcpd.pool.backup " + str(ts) + " " + fields[7]
                      + " host=" + host + " dhcppoolname=" + fields[0])

            line = p.stdout.readline()

    except OSError, err:
        print >> sys.stderr, 'Got execption running command "%s": %s' % (command, err)

if __name__ == "__main__":
    main()
