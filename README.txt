==============================================================
MINITAGE.PLONE3 BUILDOUT FOR pgolf
==============================================================

WARNING ABOUT BUILOOUT BOOTSTRAP WARNING
--------------------------------------------

        !!!    Be sure to use zc.buildout >= 1.4.3, or you ll have errors or bugs.    !!!

If you are using the standalone (choose to answer inside_minitage=no), you must ensure to do the
$python bootstrap.py dance with a python compatible with the targeted zope installation (python 2.4/plone3 python 2.6/plone4)
eg: cd pgolf && python2.4 bootstrap.py && bin/buildout -vvvvvvc <CONFIG_FILE>


Minitage users, don't worry about that, all is setted for you in the two minibuilds created for you,
just issue minimerge -v <MINIBUILD_NAME> after installing the minilay in your MINITAGE/minilays directory.


ALWAYS USE THE MINITAGE ENVIRONMENT FILE INSIDE A MINITAGE
--------------------------------------------------------------

Before doing anything in your project just after being installed, just source the environment file in your current shell::

    source $MT/zope/pgolf/sys/share/minitage/minitage.env # env file is generated with $MT/bin/paster create -t minitage.instances.env pgolf


INSTALLING THIS PROJECT VITH MINITAGE
--------------------------------------
::

    export MT=/minitage
    virtualenv --no-site-packages --distribute $MT
    source /minitage/bin/activate
    easy_install -U minitage.core minitage.paste
    svn co http://hg.foo.net/minilays/pgolf $MT/minilays/pgolf
    minimerge -v pgolf
    #minimerge -v pgolf-prod
    $MT/bin/paster create -t minitage.instances.env pgolf #(-prod)
    source $MT/zope/pgolf/sys/share/minitage/minitage.env
    cd $INS #enjoy !


CREATE A FIRST PLONESITE OBJECT
---------------------------------
Run bin/buildout -c <CONFIG_FILE> install newplonesite


PLAYING WITH DATAFS & PROJECT DATABASES
-------------------------------------------
- Upload the latest datafs from production to staging server::

    bin/buildout -vNc <CONFIG>-prod.cfg install upload-datafs

- Get the latest datafs from production to staging server::

    bin/buildout -vNc <CONFIG> install get-datafs


DEVELOP MODE
---------------
To develop your application, run the ``(minitage.)buildout-dev.cfg`` buildout, it extends this one but:
  * it comes with development tools.
  * it configures the instance to be more verbose (debug mode & verbose security)
  * it has only one instance and not all the hassles from production.


PRODUCTION MODE
---------------
To make your application safe for production, run the ``(minitage.)buildout-prod.cfg`` buildout'.
It extends this one with additionnal crontabs and backup scripts and some additionnal instances creation.


BASE BUILDOUTS WHICH DO ONLY AGGREGATE PARTS FROM THERE & THERE
-------------------------------------------------------------------
Love to know that Minitage support includes xml libs, ldap, dbs; python, dependencies & common eggs cache for things like lxml or PIL), subversion & much more.
::

    |-- minitage.buildout-dev.cfg   -> buildout for development with minitage support
    |-- buildout-dev.cfg                     -> buildout for development
    |-- minitage.buildout-prod.cfg  -> buildout for production  with minitage support
    |-- buildout-prod.cfg                    -> buildout for production
    |-- etc/minitage/minitage.cfg -> some buildout tweaks to run in the best of the world with minitage
    |-- etc/base.cfg       -> The base buildout


PLONE OFFICIAL BUILDOUTS INTEGRATION
--------------------------------------
The original ``etc/plone/plone3.version.cfg`` is the original pinned version file for your plone3 release maintened by the official plone folks.
The parts in this buildout extends/overwrite this file, you can read it to get additionnal documentation.
You must enter specific project settings in the ``etc/pgolf.cfg`` file.
::

    etc/plone/
    `-- plone4.versions.cfg    -> official plone buildout kgs
    `-- zope2.versions.cfg    -> official zope2 buildout kgs
    `-- experimental.cfg       -> experimental plone code (not used by default just here for your convenients & personal manual use)


PROJECT SETTINGS
~~~~~~~~~~~~~~~~~~~~~~~~
- Think you have the most important sections of this buildout configuration in etc/pgolf.cfg
Set the project developement  specific settings there
::

    etc/project/
    |-- pgolf.cfg       -> your project needs (packages, sources, products)
    |-- sources.cfg          -> externals sources of your project:
    |                           - Sources not packaged as python eggs.
    |                           - Eggs Grabbed from svn, add here your develoment eggs.
    |                           - Links to find distributions.
    |-- patches.cfg          -> patches used on the project
    |-- cluster.cfg          -> define new zope instances here & also their FileSystemStorage if any.
    |-- newsletter.cfg       -> singing & dancing integration (new instance with clockserver, version pinning, fss if any)
    |-- pgolf-kgs.cfg   -> Generated KGS for your project (minitage's printer or buildout.dumppickledversion)
    `-- versions.cfg         -> minimal version pinning for installing your project


SYSTEM ADMINISTRATORS RELATED FILES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    etc/init.d/                 -> various init script (eg supervisor)
    etc/logrotate.d/            -> various logrotate configuration files
    etc/sys/
    |-- high-availability.cfg   -> Project production settings like supervision, loadbalancer and so on
    |-- maintenance.cfg         -> Project maintenance settings (crons, logs)
    `-- settings.cfg            -> various settings (crons hours, hosts, installation paths, ports, passwords)


CRONS
~~~~~~
::

    |-- etc/cron_scripts/fss_daily.sh   -> backup script for fss

DELIVERANCE SUPPORT
-----------------------

To setup correctly the reverse proxy front end:
*PLEASE READ THE REVERSE PROXY SECTION BELOW*


Layout
~~~~~~~~~
::

    |-- etc/deliverance
        |-- etc/deliverance/deliverance.cfg      -> buildout used for deliverance component installations
        |-- etc/deliverance/deliverance.ini      -> PasteDeploy configuration file (paster serve etc/deliverance/deliverance.ini)
        |-- etc/deliverance/deliverance-prod.ini -> PasteDeploy configuration file (paster serve etc/deliverance/deliverance.ini) (PRODUCTIO?)
        `-- etc/deliverance/deliverance.xml      -> Main Deliverance rules file
    |-- etc/templates
        |-- etc/templates/deliverance/deliverance.ini.in      -> PasteDeploy configuration file template (paster serve etc/deliverance/deliverance.ini)
        |-- etc/templates/deliverance/deliverance-prod.ini.in -> PasteDeploy configuration file template (paster serve etc/deliverance/deliverance.ini)
        `-- etc/templates/deliverance/deliverance.xml.in      -> Main Deliverance rules file template

notes
~~~~~~~~~~~~~~
- deliverance is launched and monitored with supervisord
- Deliverance do not use the proxy mode but *the WSGI middleware*, and use PasteDeploy to fire the server.
  The part triggering its contruction is ``deliverance_ini`` && ``deliverance_prod_ini``
- Settings can be as usual changed by editing ``etc/sys/settings.cfg``
  * hosts:deliverance / ports:deliverance / locations:deliverance-themes -> The deliverance server itself  & the default theme
  * hosts:deliverance-backend / ports:deliverance-backend  -> The proxied backend (eg: zope server):
In development mode, we switched the host and url of the deliveranced host to be the development instance instead of either haproxy or the first instance.


dev mode
~~~~~~~~
You can launch manually deliverance via::

    ./bin/deliverance-paster serve etc/deliverance/deliverance.ini

- Hit thz deliverance server vith a virtualhostmonster url, if not you won't have the links rewritten.::

     http://localhost:8078/VirtualHostBase/http/localhost:8078/pgolf/VirtualHostRoot/<REQUEST>

- You can copy/symlink the below apache deliverance vhost to your apache configuration to test in a full environment
- To complete your apache installation, you must add ::

    127.0.0.1 pgolf.localhost

- To access the deliverane log, append 'deliv_log'to the GET parmaters::

     http://localhost:8078/VirtualHostBase/http/localhost:8078/pgolf/VirtualHostRoot/<REQUEST>?deliv_log=1

And then hit http://pgolf.localhost to view your proxified deliverance server

REVERSE PROXY
--------------
We generate two virtualhosts for a cliassical apache setup, mostly ready but feel free to copy/adapt.
::
    etc/apache/
    |-- 100-pgolf.reverseproxy.conf                     -> a vhost for ruse with a standalone plone (even with haproxy in front of.)
    |-- 100-pgolf.reverseproxy.deliverance.conf         -> a vhost for use with a plone behind a deliverance server.
    `-- apache.cfg
    etc/templates/apache/
    |-- 100-pgolf.reverseproxy.conf.in                   -> Template for a vhost for ruse with a standalone plone (even with haproxy in front of.)
    `-- 100-pgolf.reverseproxy.deliverance.conf.in       -> Template for a vhost for use with a plone behind a deliverance server.

In settings.cfg you have now some settings for declaring which host is your reverse proxy backend & the vhost mounting:
    * hosts:zope-front / ports:zope-front                              -> zope front backend
    * reverseproxy:host / reverseproxy:port / reverseproxy:mount-point -> host / port / mountpoint on the reverse proxy)

CONFIGURATION TEMPLATES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    etc/templates/
    |-- balancer.conf.template      -> haproxy template.
    |                                  Copy or ln the generated file 'etc/loadbalancing/balancer.conf' to your haproxy installation if any.
    |-- fss_daily.sh.in             -> FSS daily backup script template
    `-- logrotate.conf.template     -> logrotate configuration file template for your Zope logs
    `-- supervisor.initd            -> template for supervisor init script


BACKENDS
~~~~~~~~~~~
::

    etc/backends/
    |-- etc/backends/fss.cfg                   -> Filestorage configuration if any
    |-- etc/backends/relstorage.cfg            -> relstorage configuration if any
    |-- etc/backends/solr.cfg                  -> Solr configuration if any
    |-- etc/backends/zeo.cfg                   -> zeoserver configuration if any
    `-- etc/backends/zodb.cfg                  -> zodb configuration if any


KGS FILE
----------
We provide a part to generate the etc/pgolf-kgs.cfg file.
This will allow you to freeze software versions known to work with your project and make reproducible environment.
This file will be generated the first time that you run buildout.
To un it, just run bin/buildout -vvvvvvc <CONFIG_FILE> install kgs
To unlock the versions, cmment out the according statement ``etc/project/pgolf-kgs}.cfg`` in the extends option of the pgolf.cfg gile.


NOTES ABOUT RELSTORAGE SUPPORT
------------~~~~~~~-------------
We use the ZODB as an egg which is patched during installation, please see ``etc/project/patches.cfg``


OS SPECIFIC SYSTEM INSTALLERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Thos popular tools around zope/plone dev (not supported, just here for your conveniance, READ BEFORE USING THEM)
And you'd  better have to learn how to bootstrap some minitage environment out there, funny and more secure & reproductible!
::

    |-- etc/os
        |-- debian.sh       -> debian specific
        |-- opensuse-dev.sh -> opensuse/dev specific
        |-- opensuse.sh     -> suse specific
        |-- osx.sh          -> osx specific
        `-- ubuntu.sh       -> ubuntu specific


CONTINEOUS INTEGRATION
~~~~~~~~~~~~~~~~~~~~~~~~~
Here ae the files needed for our hudson and/or buildbot integration.

For hudson we provide some shell helpers more or less generated to run 'a build':

    - an helper which set some variables in the current environement for others helpers
    - an helper which update the project
    - an helper which update the associated sources grabbed via mr.developer
    - an helper which run all the tests

This is described in details on the related configuration files you will find in the layout below.
::

    |-- minitage.buildout-buildbot.cfg     -> buildout for deploying a buildbot related to your project (requires to be inside a minitage)
    |-- etc/hudson/
    |   `-- pgolf
    |       |-- build
    |           |-- build.sh               -> the project build helper
    |           |-- test.sh                -> the project test executor helper (launch all tests needed)
    |           |-- update_mrdeveloper.sh  -> update sources grabbed via mrdeveloper
    |           `-- update_project.sh      -> update this layout
    |
    |-- etc/templates/hudson/
        `-- pgolf
            |-- build
            |   `-- activate_env.sh.in   -> buildout template to generate etc/hudson/pgolf/build/activate.env.sh
            `-- config.xml.in            -> buildout template to generate etc/hudson/pgolf/config.xml (hudson job/build file)

CYNIN integration if any
------------------------

     |-- etc/project/buildout-cynin.cfg -> cynin specific buildout


NOTES ABOUT WSGI SUPPORT
-------------------------
::

    etc/wsgi/
    |-- dev.ini      -> paster production configuration for running in wsgi mode
    `-- prod.ini     -> paster development configuration for running in wsgi mode

The egg is on your cache with a particular version, the classical ZODB3 egg wont be touched if you have one.
WHAT IS VERY IMPORTANT is that [zopepy] part must run BEFORE [instance] to get the version with appropriate patches pinned.
This WSGI support is nowodays deprecated (on the plone side), unmaintened and not supported, use it at our own risks.

As we support WSGI, there is an important thing to know:
  - ``zopelib`` is an egg from repoze where live the zope code, we totally do not NEED it.
        * It's useless and make things buggy.
        * We build zopelib as a fake egg, as we have already zope in our PYTHONPATH.
  - If you raelly want zopelib as an egg, (un)comment things in the buildout(develop, patch). But we are sure, you surely dont have to !
  - To run in WSGI with repoze.zope2, issue::

      bin/paster serve etc/wsgi/dev.ini
      or bin/paster serve etc/wsgi/prod.ini


A word about minitage.paste instances
--------------------------------------
You are maybe wondering why this big buildout do not have out of the box those fancy monitoring, load-balancing or speedy databases support.
#
For the author, System programs that are not well integrated via buildout and most of all not written in python don't really have to be deployed via that buildout.
And most of all, you ll surelly have head aches to make those init-scripts or rotation logs configurations right.
Because the recipe which do them don't support it or other problems more or less spiritual.
#
Keep in mind that in Unix, one thing must do one purpose, and do it well. And many sysadmins don't want to run a buildout
to generate a configuration file or build their loadbalancer, They want to edit in place, at most fetch the configuration file from somewhere and adapt,that's all.
#
Nevertheless, as usual, they are exceptions:
     - supervisord which is well integrated. So supervisor is deployed along in the production buildout if any.
     - We generate through buildout a haproxy configuration file or hudson related stuff
#
That's because we support that throught 'minitage.paste.instances'. Those are templates which create some instance of some program
inside a subdirectory which is:
   - sys/ inside a minitage project
   - ADirectoryOfYourChoice/ if your are not using minitage
#
This significate that you can install a lot of things along with your project with:
   - minitage/bin/easy_install -U minitage.paste(.extras) (or get it via buildout)
   - paster create -t <TEMPLATE_NAME> projectname_OR_subdirectoryName inside_minitage=y/n
     Where TEMPLATE_NAME can be (run paster create --list-templates|grep minitage.instances to get an up2date version):
#
     * minitage.instances.apache:          Template for creating an apache instance
     * minitage.instances.env:             Template for creating a file to source to get the needed environnment variables for playing in the shell or for other templates
     * minitage.instances.mysql:           Template for creating a postgresql instance
     * minitage.instances.nginx:           Template for creating a nginx instance
     * minitage.instances.paste-initd:     Template for creating init script for paster serve
     * minitage.instances.postgresql:      Template for creating a postgresql instance
     * minitage.instances.varnish:         Template for creating a varnish instance
     * minitage.instances.varnish2:        Template for creating a varnish2 instance
#
     The minitage.paste package as the following extras:
#
     * minitage.instances.openldap:      Template for creating an openldap instance
     * minitage.instances.tomcat:        Template for creating a tomcat instance
     * minitage.instances.cas:           Template for creating a Jisag CAS instance
     * minitage.instances.hudson:        Template for creating an hudson instance
#
Note that if you are using minitage, you ll have better to add dependencies inside your minibuild and run minimerge to build them prior to run the paster command
#
For example, to add a postgresql instance to your project, you will have to issue those steps:
    * $EDITOR minitage/minilays/pgolf_minilay/pgolf -> add postgresql-8.4 to the dependencies list
    * minimerge -v  pgolf install what was not, and surely at least postgresql-8.4
    * minitage/bin/paster create -t minitage.instance.postgresql pgolf
    * Then to start the postgres : zope/pgolf/sys/etc/init.d/pgolf_postgresql restart


# vim:set ft=rst:
