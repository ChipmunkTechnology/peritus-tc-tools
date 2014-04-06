tc-atmail.sh
==============
OpenTSDB tcollector script for counting Atmail mysql table sizes.

![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-atmail/tc-atmail-graph-screenshot.png.png)

Requirements
------------
OpenTSDB tcollector - http://opentsdb.net/tcollector.html

mysql command line client

Installation
------------
Put ``tc-atmail.sh`` into ``tcollector/collectors/300/``
Change permissions of ``tc-atmail.sh`` to 755.
tcollector will only execute scripts that are runnable.

Performance
-----------
~2 seconds for a single run.
Total table size about 15M rows on MySQL 5.1

Run-time in usec saved as metric ``tcollector.collectors.atmail.elapsedtime``

Troubleshooting
---------------

Look at the tcollector log in ``/var/log/tcollector`` for errors etc
