tc-isc-dhcpd-log-stats.sh
==============
OpenTSDB tcollector script for count DHCPD events from logfile.

Examples
--------
Example graph #1. Showing number of DHCPDISCOVERs to DHCPOFFERs across all servers. Difference between these might indicate problems with the DHCP server. Too few DHCPOFFERs compared to baseline might indicate problems with infrastructure. Too many DHCPOFFERs, as apparent by this example, might indicate problems with a DHCP client.
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-isc-dhcpd-log-stats/tc-isc-dhcpd-log-stats-graph-discover-offer.png)

Example graph #2. Showing number of DHCPREQUESTs to DHCPACKs. Divering lines might indicate problems with DHCP servers.
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-isc-dhcpd-log-stats/tc-isc-dhcpd-log-stats-graph-request-ack.png)

Example graph #3. Showing number of completed DHCP transactions per server by counting DHCPACKs. Clearly shows how load is balanced between servers as well as showing if a server stops serving (or just logging) leases.
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-isc-dhcpd-log-stats/tc-isc-dhcpd-log-stats-graph-two-server-acks.png)

Requirements
------------
OpenTSDB tcollector - http://opentsdb.net/tcollector.html

Installation
------------
Put ``tc-isc-dhcpd-log-stats.sh`` into ``tcollector/collectors/10/``
Change permissions of ``tc-isc-dhcpd-log-stats.sh`` to 755.
tcollector will only execute scripts that are runnable.

Performance
-----------
~0.3 seconds for a single run. 80.000 lines in logfile.

Run-time in usec saved as metric ``tcollector.collectors.isc-dhcpd-log-stats.elapsedtime``

Troubleshooting
---------------
Look at the tcollector log in ``/var/log/tcollector`` for errors etc
