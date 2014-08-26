#!/usr/bin/env python

"""

peritus-tc-tools/tc-wlan/tc-wlan.py - v 1.0.0
OpenTSDB tcollector wrapper for iwlist scan

2014-08-23 Stian Ovrevage <stian@peritusconsulting.no>

Metrics gathered:
  wlan.channel
  wlan.bitrate
  wlan.quality_level
  wlan.signal_level
  wlan.adjecent_networks

iwlist scan output format:
          Cell 01 - Address: 00:31:96:41:8C:8B
                    ESSID:"SomeSSIDName"
                    Protocol:IEEE 802.11bg
                    Mode:Master
                    Frequency:2.462 GHz (Channel 11)
                    Encryption key:on
                    Bit Rates:54 Mb/s
                    Extra:wpa_ie=dd160050f201010
                    IE: WPA Version 1
                        Group Cipher : TKIP
                        Pairwise Ciphers (1) : TKIP
                        Authentication Suites (1) : PSK
                    Quality=100/100  Signal level=85/100

Tested with:
D-link DWA-121 - Recommended. High update rate. Apparently high precision.
Edimax EW-7811Un - Only updates values every 2-3 minutes
Asus USB-N10 - Only updates values every 2-3 minutes

"""

import subprocess
import time
import sys
import os.path
import socket
import re

'''
How long between scans, in seconds. Note that an interval of 10 will not give a result
every 10 seconds since iwlist typically takes a second or two to send the scan
command to the NIC and receive an answer. Recommended: 10. Certain NICs can scan
very often and 3 second interval has been used successfully. But this could lead
to overheating over time, so use caution with very short intervals.
'''
scan_interval = 10


'''
Which interface to use.
'''
interface = "wlan0"

''' host tag for metrics. Use system fqdn hostname by default '''
host = socket.getfqdn()


command = ['iwlist ' + interface + ' scan']

def main():

    ssid = ""
    re_ssid = re.compile(r'\s*ESSID:\"([^\n\r"]+)\"\s*')
    channel = ""
    re_channel = re.compile(r'\s*Frequency:.*Channel ([0-9]+)\s*')
    bitrate = ""
    re_bitrate = re.compile(r'\s*Bit Rates:([0-9]+) Mb/s\s*')
    quality_level = ""
    signal_level = ""
    re_levels = re.compile(r'\s*Quality=([0-9]+)/100.*Signal level=([0-9]+)/100\s*')
    re_signal_level = re.compile(r'\s*Signal level=([0-9]+)/100\s*')

    re_cell = re.compile(r'\s*Cell ([0-9]+) - Address:.*')

    adjecent_networks = 0

    try:
        while(True):
            ts = int(time.time())

            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, bufsize=0)
            line = p.stdout.readline()
            while line:
                if re_cell.match(line):
                    adjecent_networks = adjecent_networks + 1
                    ssid, channel, bitrate, quality_level, signal_level = "", "", "", "", ""

                if re_ssid.match(line):
                    ssid = re_ssid.match(line).groups()[0]

                if re_channel.match(line):
                    channel = re_channel.match(line).groups()[0]
                    print("wlan.channel " + str(ts) + " " + channel + " host=" + host + " interface=" + interface + " ssid=" + ssid)

                if re_bitrate.match(line):
                    bitrate = re_bitrate.match(line).groups()[0]
                    print("wlan.bitrate " + str(ts) + " " + bitrate + " host=" + host + " interface=" + interface + " ssid=" + ssid)

                if re_levels.match(line):
                    quality_level = re_levels.match(line).groups()[0]
                    signal_level = re_levels.match(line).groups()[1]
                    print("wlan.quality_level " + str(ts) + " " +  quality_level  + " host=" + host + " interface=" + interface + " ssid=" + ssid)
                    print("wlan.signal_level " + str(ts) + " " +  signal_level + " host=" + host + " interface=" + interface + " ssid=" + ssid)

                if re_signal_level.match(line):
                    signal_level = re_signal_level.match(line).groups()[0]
                    print("wlan.signal_level " + str(ts) + " " + signal_level + " host=" + host + " interface=" + interface + " ssid=" + ssid)

                line = p.stdout.readline()

            ''' Output statistic on number of adjecent networks '''
            print("wlan.adjecent_networks " + str(ts) + " " +  str(adjecent_networks) + " host=" + host + " interface=" + interface + " ssid=" + ssid)
            adjecent_networks = 0

            time.sleep(scan_interval)

    except OSError, err:
        print >> sys.stderr, 'Got execption running command "%s": %s' % (command, err)

if __name__ == "__main__":
    main()
