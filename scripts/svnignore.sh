#!/usr/bin/env bash
PROJECT="pgolf"
up="up --ignore-externals "
ignore="bin
buildout-preprod.cfg.before.fixed_version.bak
cron_scripts
README.postgresql.cchb-preprod-cchb
develop-eggs
.directory
downloads
dumps
a
*.egg-info
eggs
*.env
*.bak
activate_env.sh
fake-eggs
README.postgresql.ccva-ccva
fake-eggs/*
.installed.cfg
.mr.developer.cfg
parts
100-ccva.reverseproxy.conf
.minitage
100-ccva.reverseproxy.con
instance.ini
instance1.ini
instance2.ini
instance3.ini
instance4.ini
settings-prod.cfg
*.pt.py
t
sys
tags.python
var
"
etc="$ignore
deliverance*.ini
cherrypy.ini
cherrypy-prod.ini
deliverance.xml
settings-prod.cfg
init.d
"
apache="$etc
100-$PROJECT.reverseproxy.conf
*.conf"
hudson="$ignore
${PROJECT}.xml
config.xml
"
developer="$ignore
$PROJECT
$PROJECT.tma
$PROJECT.policy
$PROJECT.testing
$PROJECT.sdkin
$PROJECT.skin.mo
"
var="$ignore
zeoserver.pid
fss_storage_global
fss_backup_global
fss_storage_$PROJECT
fss_storagenewsletter_${PROJECT}
pgsql_dumps
instance.pid
*.pid
instance.lock
*.lock
log
${PROJECT}.*-access_log
${PROJECT}.*_log 
${PROJECT}.localhost-access_log
${PROJECT}.localhost_log
fss_backupnewsletter_${PROJECT}
newsletter
instance-newsletter
fss_backup_${PROJECT}
fss_storagenewsletter_${PROJECT}
fss_backupnewsletter_${PROJECT}
newsletter
instance-newsletter
instance
zeocl.sock
instance*
filestorage
snapshotbackups
backups
zeo.zdsock
supervisord_*
log
*.log
*_log
*-log
"
hudson="$etc
config.xml
activate_env.sh
"
policy="$ignore"
skin="$ignore"
testing="$ignore"
products="
${PROJECT}.policy
${PROJECT}.skin
${PROJECT}.testing
${PROJECT}.tma
"
vapache="$ignore
${PROJECT}*.log
"

iproducts="$ignore
*.egg-info
$PROJECT.skin.mo
*.pyc
*.mo"
developer="$ignore
formrenderingtools
formwizard
revegetalisation
opencarto
ccva
olwidget
"
doproduct() {
    for p in $products;do
        svn $up $p
        svn propset  -R svn:ignore "$iproducts" src.mrdeveloper/$p
        svn $up $p
        svn ci -m "resetting svnignore"         src.mrdeveloper/$p
    done
}
cd $(dirname $0)/..
svn $up 
doproduct
svn propset -R  svn:ignore "$etc" etc
svn propset  svn:ignore "$var" var
svn propset  -R svn:ignore "$hudson" etc/hudson
svn propset  svn:ignore "$developer" src.mrdeveloper
svn propset  svn:ignore "$ignore" .
svn ci -m "resetting svnignore"
# vim:set et sts=4 ts=4 tw=80:
