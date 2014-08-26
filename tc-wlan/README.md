tc-wlan
==============
OpenTSDB tcollector wrapper for iwlist.

Collects information on WLAN signal and quality levels. Can be run while
associated/connected to a SSID without any disruption.

Collects the following metrics for all SSIDs in range:
  * wlan.channel
  * wlan.bitrate
  * wlan.quality_level
  * wlan.signal_level

As well as the total number of SSIDs in range:
  * wlan.adjecent_networks

Example graph #1. Number of WLAN cells (1), quality and signal level per SSID.
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-wlan/tc-wlan-example.png)


Requirements
------------
OpenTSDB tcollector - http://opentsdb.net/tcollector.html


Installation
------------
Put ``tc-wlan.py`` into ``tcollector/collectors/0/``
Change permissions of ``tc-wlan.py`` to 755.
tcollector will only execute scripts that are runnable.

If tcollector is running already it will automatically spawn tc-ping.
If not start tcollector with:

    ./startstop start


Troubleshooting
---------------
Look at the tcollector log in ``/var/log/tcollector`` for errors etc
