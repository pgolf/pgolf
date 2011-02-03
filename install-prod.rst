
Plone installation notes
============================

Sum up
-------
 * :port zope: 25555
 * :port supervisor: 25553
 * :port zeo: 25554
 * :install path: /opt/minitage/zope/pgolf-prod
 * :user: fit4par
 * :apache bits: /opt/minitage/zope/pgolf-prod/etc/apache/200-pgolf.conf

Minitage
-----------
Pgolf is installed in a basic minitage installation.
Its prefix is in /opt/minitage.
The minitage goal is to have all the dependencies of pgolf installed alongside the project.

Use the zope user
-------------------------------
**!WARNING!**

The **id** command lets you verify the current user.

from root, you need to be fit4par::

	id
	uid=0(root) gid=0(root) groups=0(root),1(bin) ...
	su fit4par
	id
	uid=32009(fit4par) gid=100(users) groups=100(users)

Go inside the instance folder
---------------------------------
::

	cd /opt/minitage/zope/pgolf-prod

The instance environment
----------------------------

**YOU NEED TO DO THIS PRIORI TO USE ANY COMMAND ON YOUR INSTANCE**

If you do not have **(minitage-pgolf-prod)** in the shell prompt do this
::

	. /opt/minitage/zope/pgolf-prod/sys/share/minitage/minitage.env

Use supervisor to know the status
--------------------------------
::

	cd $INS
	./bin/supervisorctl status

Restart the whole server
-------------------------
With the global init script, you can restart the server with
As **root**
::

	service pgolf restart

Log rotation
-------------
That had be done to enable logrotatation on the zope server::

	ln -s /opt/minitage/zope/pgolf-prod/etc/logrotate.conf /etc/logrotate.d/pgolf-plone

Edit the websites configuration
------------------------------------

  - vhosts bits are in ``minitage/zope/pgolf-prod/etc/apache/200-pgolf.conf``.
  - Edit this file in coda via ssh as **root**: ``/home/fit4par/minitage/zope/pgolf-prod/etc/apache/200-pgolf.conf``.
  - To take changes in account, restart apache, as **root**::

		service httpd restart


Main apache Configuration
---------------------------
NOTE: We have put in the cpanel apache configuration editor an post hook to include /opt/minitage/zope/pgolf-prod/etc/apache/200-pgolf.conf.::

	Include /opt/minitage/zope/pgolf-prod/etc/apache/200-pgolf.conf in the textarea

To resume apache to work:

  - Edit on your server as *root* :  /etc/httpd/conf/httpd.conf via *SSH*
  - Remove from this file all <VirtualHost> nodes (from <VirtualHost> to </VirtualHost>) which relate to your domains
    eg remove ::

                        # DO NOT EDIT. AUTOMATICALLY GENERATED.  IF YOU NEED TO MAKE A CHANGE PLEASE USE THE INCLUDE FILES.

                        <VirtualHost 208.116.60.117:80>
                            ServerName fit4par.ch
                            ServerAlias www.fit4par.ch
                            DocumentRoot /home/fit4par/public_html
                            ServerAdmin webmaster@fit4par.ch
                            UseCanonicalName Off
                            CustomLog /usr/local/apache/domlogs/fit4par.ch combined
                            CustomLog /usr/local/apache/domlogs/fit4par.ch-bytes_log "%{%s}t %I .\n%{%s}t %O ."
                            ## User fit4par # Needed for Cpanel::ApacheConf
                            <IfModule mod_suphp.c>
                                suPHP_UserGroup fit4par fit4par
                            </IfModule>
                            <IfModule !mod_disable_suexec.c>
                                SuexecUserGroup fit4par fit4par
                            </IfModule>
                            ScriptAlias /cgi-bin/ /home/fit4par/public_html/cgi-bin/


                            # To customize this VirtualHost use an include file at the following location
                            # Include "/usr/local/apache/conf/userdata/std/2/fit4par/fit4par.ch/.conf"

                        </VirtualHost>

  - Remove the VirtualHost which has a documentroot set to /dev/null::

                        # WHM DOMAIN FORWARDING VHOST
                        <VirtualHost 208.116.60.118>
                            ServerName 208.116.60.118
                            ServerAdmin root@localhost
                            DocumentRoot /dev/null
                            ScriptAliasMatch .* /usr/local/cpanel/cgi-sys/domainredirect.cgi
                        </VirtualHost>

  - To take changes in account, restart apache on your server, as **root**::

        ssh root@208.116.60.117
		service httpd restart

 Alternativly without coda:

  - Open a terminal
  - Download the main apache configuration::
 
		scp -P 100 root@208.116.60.117:/etc/httpd/conf/httpd.conf http.conf

  - Do the edit
  - Reupload::

		scp -P 100 httpd.conf root@208.116.60.117:/etc/httpd/conf/httpd.conf



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


Add a plone site
------------------
    - Go to http://www.b:asio.ch/zmiroot/manage_main (admin/XXXXX)

            - create a plone site: select plone site in the select box
                
                 - put 'foo' as the plone site id
                 - go for creation
                 - enter this website (foo)
                 - go to the add one panel ( admin / konfiguration / Erweiterungen)
                 - install the pgolf.policy product

    - Edit  /home/fit4par/minitage/zope/pgolf-prod/etc/apache/200-pgolf.conf via ssh
    - Copy Paste a VirtualHost and adapt it to your needs:

            - Change the server name / alias::

                    ServerName foo.ch
                    
            - Change the logs pass::

                 /usr/local/apache/domlogs/golfchallenge.ch-bytes_log -> g /usr/local/apache/domlogs/foo.ch-bytes_log

            - Adapt the ProxyPass Rules to match your plone installation

                ProxyPass        /             http://127.0.0.1:25556/VirtualHostBase/http/www.foo.ch:80/foo/VirtualHostRoot/
                ProxyPassReverse /             http://127.0.0.1:25556/VirtualHostBase/http/www.foo.ch:80/foo/VirtualHostRoot/
                                                                                           DOMAIN              PLONEID








