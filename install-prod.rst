
Plone installation notes
============================

Sum up
-------
-:port zope: 25555
-:port supervisor: 25553
-:port zeo: 25554
-:install path: /opt/minitage/zope/pgolf-prod
-:user: zope
-:apache bits: /opt/minitage/zope/pgolf-prod/etc/apache/200-pgolf.conf

Minitage
-----------
Pgolf is installed in a basic minitage installation.
Its prefix is in /opt/minitage.
The minitage goal is to have all the dependencies of pgolf installed alongside the project.

Use the plone instance
-------------------------------
!WARNING! ALWAYS Activate the environment::

	. /opt/minitage/zope/pgolf-prod/sys/share/minitage/minitage.env

	Use supervisor to know the status
	+++++++++++++++++++++++++++++++++++
	cd $INS
	./bin/supervisorctl st

Restart the whole server
-------------------------
With the global init script, you can restart the server with::

	service pgolf restart

Log rotation
-------------
That had be done to enable logrotatation on the zope server::

	ln -s /opt/minitage/zope/pgolf-prod/etc/logrotate.conf /etc/logrotate.d/pgolf-plone

Apache Configuration
---------------------
vhosts bits are in ``/opt/minitage/zope/pgolf-prod/etc/apache/200-pgolf.conf``.

Running buildout
---------------------
::

	cd /opt/minitage/zope/pgolf-prod
	. /opt/minitage/zope/pgolf-prod/sys/share/minitage/minitage.env
	bin/buildout -vvvvvvvvNc minitage.buildout-prod.cfg

Adding modules to plone
-------------------------------
- Edit etc/project/pgolf.cfg
- add whatever you want to eggs= alongside with the other eggs
- add whatever you want to zcml= alongside with the other eggs

Pinning versions
-----------------
Edit etc/project/versions.cfg, and add your pinning

Products installed at installation time:
--------------------------------------------
- medialog.subkins
- ploneforgen
- ploneboard
- contentwellportlets
- collective.gallery














