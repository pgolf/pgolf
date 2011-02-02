
Plone installation notes
============================

Sum up
-------
-:port zope: 25555
-:port zeo: 25554
-:install path: /opt/minitage/zope/pgolf-prod
-:user: zope



Minitage
-----------
- Basic minitage installation in /opt/minitage

cat /opt/minitage/minilays/pgolf/pgolf-prod
::

		[minibuild]
		dependencies=py-libxml2-2.7 py-libxslt-1.1 libxml2-2.7 libxslt-1.1 pil-1.1.7 libiconv-1.12 subversion-1.6 git-1.7 python-2.6
		install_method=buildout
		src_uri=http://hg.foo.net
		src_type=git
		category=zope
		homepage=http://www.makina-corpus.com
		description= a plone 4.0.3 buildout for pgolf (PRODUCTION MODE)
		buildout_config=minitage.buildout-prod.cfg






