tc-opensips.sh
==============
OpenTSDB tcollector script for counting opensips mysql table sizes.

Example graph #1: Number of total SIP subscribers and number of active SIP locations. A large difference might indicate many inactive SIP accounts. A decline in SIP locations might indicate problems with clients registering and timing out.
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-opensips/tc-opensips-graph-locations-subscribers.png)

Requirements
------------
OpenTSDB tcollector - http://opentsdb.net/tcollector.html

mysql command line client

Installation
------------
Put ``tc-opensips.sh`` into ``tcollector/collectors/60/``
Change permissions of ``tc-opensips.sh`` to 755.
tcollector will only execute scripts that are runnable.

Performance
-----------
~0.01 seconds for a single run. 1500 rows.

Run-time in usec saved as metric ``tcollector.collectors.opensips.elapsedtime``

Troubleshooting
---------------
Look at the tcollector log in ``/var/log/tcollector`` for errors etc
