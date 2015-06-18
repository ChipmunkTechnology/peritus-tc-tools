tc-pdns-recursor.py
==============
OpenTSDB tcollector script for collecting PowerDNS (pdns) recursor statistics

Requirements
------------
OpenTSDB tcollector - http://opentsdb.net/tcollector.html

pdns recursor

Installation
------------
Put ``tc-pdns-recursor.py`` into ``tcollector/collectors/0/``
Change permissions of ``tc-pdns-recursor.py`` to 755.
tcollector will only execute scripts that are runnable.

Change variable COLLECTION_INTERVAL in script if desired. Default is 10 seconds.

Troubleshooting
---------------
Look at the tcollector log in ``/var/log/tcollector`` for errors etc

Todo
----
Add timing information to ''tcollector.collectors.pdns-recursor.elapsedtime''
