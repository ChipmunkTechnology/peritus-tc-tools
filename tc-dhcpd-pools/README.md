tc-dhcpd-pools
==============
OpenTSDB tcollector wrapper for dhcpd-pools.

![](https://raw.github.com/PeritusConsulting/peritus-tc-tools/master/tc-dhcpd-pools/tc-dhcpd-pools-graph-screenshot.png)

Requirements
------------
OpenTSDB tcollector - http://opentsdb.net/tcollector.html
  
dhcpd-pools - http://dhcpd-pools.sourceforge.net/

  aptitude install uthash-dev
  wget http://sourceforge.net/projects/dhcpd-pools/files/dhcpd-pools-2.24.tar.xz
  tar -xJvf dhcpd-pools-2.24.tar.xz
  cd dhcpd-pools-2.24
  ./configure
  make && make install

Installation
------------
Put ``tc-dhcpd-pools.py`` into ``tcollector/collectors/600/``
Change permissions of ``tc-dhcpd-pools.py`` to 755. 
tcollector will only execute scripts that are runnable.

If tcollector is running already it will automatically spawn tc-dhcpd-pools. 
If not start tcollector with:

    ./startstop start

Performance
-----------
~0.3 seconds on 30000 leases on dual core 800Mhz VM with 256MB ram.

Compatibility
-------------
Tested with Python 2.7 and dhcpd-pools 2.24.

Troubleshooting
---------------

Look at the tcollector log in ``/var/log/tcollector`` for errors etc
