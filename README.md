peritus-tc-tools
================

A few OpenTSDB tcollector tools and plugins

[tc-ping][1]
------------
High performance replacement for smokeping, collecting latency and loss data using [fping][6].

![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-ping/tc-ping-details-one-host.png)

Metrics:

* ```icmp.lossrate``` - percentage
* ```icmp.latency.avg``` - milliseconds
* ```icmp.latency.max``` - milliseconds

Tags:

* ```dsthost```
* ```host```
* ```tos```

[tc-dhcpd-pools][2]
-------------------
High performance collection of ISC dhcpd pool lease statistics using [dhcpd-pools][7].
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-dhcpd-pools/tc-dhcpd-pools-graph-screenshot.png)

Metrics:

* ```dhcpd.pool.size```
* ```dhcpd.pool.usage.absolute```
* ```dhcpd.pool.usage.percent```
* ```dhcpd.pool.inactive```
* ```dhcpd.pool.backup```

Tags:

* ```host```
* ```dhcppoolname```

[tc-isc-dhcpd-log-stats][3]
---------------------------
Simple log "parser" for ISC dhcpd collecting DHCP event statistics (DISCOVER, OFFER, ACK, REQUEST, etc)
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-isc-dhcpd-log-stats/tc-isc-dhcpd-log-stats-graph-request-ack.png)

Metrics:

* ```dhcp.events.discover```
* ```dhcp.events.offer```
* ```dhcp.events.request```
* ```dhcp.events.ack```
* ```dhcp.events.nak```
* ```dhcp.events.release```
* ```dhcp.events.inform```
* ```dhcp.events.addforwardmap```
* ```dhcp.events.removeforwardmap```
* ```dhcp.errors.noaddforwardmap```
* ```dhcp.errors.noaddreversemap```
* ```dhcp.errors.notsec```
* ```dhcp.errors.bindupdatexidmismatch```
* ```dhcp.errors.uidduplicate```
* ```dhcp.errors.bindupdaterejected```
* ```dhcp.errors.others```
* ```dhcp.total```
* ```tcollector.collectors.isc-dhcpd-log-stats.elapsedtime```

Tags:

* ```host```
* ```instance```


[tc-atmail][4]
--------------
Simple script counts [Atmail][8] mysql database rows.
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-atmail/tc-atmail-graph-screenshot.png)

Metrics:

* ```atmail.adminusers```
* ```atmail.domains```
* ```atmail.mailrelays```
* ```atmail.sharedfiles```
* ```atmail.users```
* ```atmail.usersessions```
* ```atmail.log.virus```
* ```atmail.log.spam```
* ```atmail.log.sentmail```
* ```atmail.log.recvmail```
* ```atmail.log.logins```
* ```atmail.log.errors```
* ```tcollector.collectors.atmail.elapsedtime```

Tags:

* ```host```

[tc-opensips][5]
----------------
Simple script counts [opensips][9] mysql database rows.
![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-opensips/tc-opensips-graph-locations-subscribers.png)

Metrics:

* ```opensips.subscribers```
* ```opensips.locations```
* ```tcollector.collectors.opensips.elapsedtime```

Tags:

* ```host```


  [1]: https://github.com/PeritusConsulting/peritus-tc-tools/tree/master/tc-ping
  [2]: https://github.com/PeritusConsulting/peritus-tc-tools/tree/master/tc-dhcpd-pools
  [3]: https://github.com/PeritusConsulting/peritus-tc-tools/tree/master/tc-isc-dhcpd-log-stats
  [4]: https://github.com/PeritusConsulting/peritus-tc-tools/tree/master/tc-atmail
  [5]: https://github.com/PeritusConsulting/peritus-tc-tools/tree/master/tc-opensips
  [6]: http://fping.org/
  [7]: http://dhcpd-pools.sourceforge.net/
  [8]: http://atmail.com/
  [9]: http://www.opensips.org/
