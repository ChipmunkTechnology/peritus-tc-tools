tc-ping
==============
OpenTSDB tcollector wrapper for fping.

Example graph #1. Details for a single host. Show packet loss in full detail. Show the 5 minute average as well as 5 minute max latency measurements.
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-ping/tc-ping-details-one-host.png)

Example graph #2. Comparison of packet loss for three different hosts. Usefull for verifying if packet loss is occuring at similar times and therefore possibly on a single saturated link.
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-ping/tc-ping-compare-hosts.png)
> NOTE: Due to an apparent bug in OpenTSDB the loss rate percentages are somehow inflated by 50%.

This collector is intended as a replacement to smokeping for collecting 
latency and loss statistics. Whereas smokeping is a complete suite for 
gathering statistics, saving aggregated statistics to .rrd files and 
displaying graphs, tc-ping is simply a wrapper of the same 
fping-plugin which smokeping uses and formats the output so it can 
be transmitted to OpenTSDB via the tcollector daemon.

Requirements
------------
OpenTSDB tcollector - http://opentsdb.net/tcollector.html

fping3 - http://fping.org/fping.1.html

Installation
------------
Put ``tc-ping.py`` into ``tcollector/collectors/0/``
Change permissions of ``tc-ping.py`` to 755. 
tcollector will only execute scripts that are runnable.

Put ``hosts.txt`` into ``/opt/tcollector/collectors/etc/``

If tcollector is running already it will automatically spawn tc-ping. 
If not start tcollector with:

    ./startstop start

Performance
-----------
Debian 7 with standard tcollector probes and tc-ping pinging 200 hosts
every 3 seconds consumes about 40Mhz of CPU compared to ~160Mhz on Smokeping. 
This is mainly due to the improved efficiency of fping3. Total virtual machine
memory footprint is reduced from 200MB to 40MB.

Troubleshooting
---------------
Look at the tcollector log in ``/var/log/tcollector`` for errors etc
