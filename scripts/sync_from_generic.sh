#!/usr/bin/env bash
cd $(dirname $0)/..
PROJECT="pgolf"
IMPORT_URL="https://subversion.makina-corpus.net/scrumpy/$PROJECT"
cd $(dirname $0)/..
[[ ! -d t ]] && mkdir t
rm -rf t/*
tar xzvf $(ls -1t ~/cgwb/$PROJECT*z) -C t
files="
bootstrap.py
buildout-dev.cfg
buildout-prod.cfg
minitage.buildout-dev.cfg
minitage.buildout-prod.cfg
README.*
etc/
minilays/
"
for f in $files;do
    rsync -azv t/$f $f
done
policy="tests/base.py 
configure.zcml
profiles/default/metadata.xml"
for i in $policy;do
    rsync -azv t/src/$PROJECT.policy/src/$PROJECT/policy/$i src/$PROJECT.policy/src/$PROJECT/policy/$i
done
sed -re "s/.*:default/    ${PROJECT}.policy:default/g" -i  etc/project/$PROJECT.cfg
sed -re "s/(extends=.*)/\1 etc\/sys\/settings-prod.cfg/g" -i buildout-prod.cfg
sed -re "/\[buildout\]/ {
aallow-hosts = \${mirrors:allow-hosts}
}" -i etc/base.cfg
sed -re "/\[mirrors\]/ {
aminitage-globalenv=true
aallow-hosts =
a\     *localhost*
a\     *willowrise.org*
a\     *plone.org*
a\     *zope.org*
a\     *effbot.org*
a\     *python.org*
a\     *pybrary.net*
a\     *initd.org*
a\     *googlecode.com*
a\     *plope.com*
a\     *bitbucket.org*
a\     *repoze.org*
a\     *crummy.com*
a\     *minitage.org*
a\     *.selenic.com*
}" -i etc/sys/settings.cfg
sed -re "s/python-2.6/subversion-1.6 git-1.7 python-2.6/g" -i minilays/pgolf/pgolf* 


# vim:set et sts=4 ts=4 tw=80:
