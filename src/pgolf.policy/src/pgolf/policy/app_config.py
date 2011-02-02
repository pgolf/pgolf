#-*- coding: utf-8 -*-
"""Specific project configuration."""
GLOBALS = globals()




################################################################################
# Products that have entries in quickinstaller,
# here are their 'id' (not the translated name)
################################################################################

PRODUCT_DEPENDENCIES = (\
)

EXTENSION_PROFILES = ('pgolf.policy:default',)

SKIN = 'pgolf.skin'
HIDDEN_PRODUCTS = [u'plone.app.openid', u'NuPlone',
#      u'Products.CMFPlacefulWorkflow',
#      u'Products.Ploneboard',
#      u'plone.app.blob',
#      u'Products.ContentWellPortlets',
#      u'Products.csvreplicata',
#      u'Products.TinyMCE',
#      u'collective.gallery',
#      u'Products.SimpleAttachment',
#      u'plone.app.z3cform',
#      u'Products.PloneFormGen',
    #with_ploneproduct_contentwellportlet

#    u'ContentWellPortlets',
    #with_ploneproduct_ploneboard

#    u'CMFPlacefulWorkflow',

#    u'Ploneboard',

#    u'SimpleAttachment',
    #with_ploneproduct_ploneformgen

#    u'PloneFormGen',
    #with_ploneproduct_csvreplica
         #'csvreplicata',
#        #with_ploneproduct_tinymce

#    u'TinyMCE',
#    u'pgolf.skin',
#    u'pgolf.tma',
#    u'pgolf.policy.migrations.v1_1',
#    u'pgolf.policy.migrations',
#    u'csvreplicata',
#    u'Products.csvreplicata',
]
HIDDEN_PROFILES = [u'plone.app.openid', u'NuPlone',
    u'pgolf.skin',
    u'pgolf.tma',
    u'pgolf.policy.migrations.v1_1',
    u'pgolf.policy.migrations',
      u'Products.CMFPlacefulWorkflow',
      u'Products.Ploneboard',
      u'plone.app.blob',
      u'Products.ContentWellPortlets',
      u'Products.csvreplicata',
      u'Products.TinyMCE',
      u'collective.gallery',
      u'Products.SimpleAttachment',
      u'plone.app.z3cform',
      u'Products.PloneFormGen',
#    u'csvreplicata',
#    u'Products.csvreplicata',

]

from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable as INonInstallableProducts
from Products.CMFPlone.interfaces import INonInstallable as INonInstallableProfiles

class HiddenProducts(object):
    implements(INonInstallableProducts)

    def getNonInstallableProducts(self):
        return HIDDEN_PRODUCTS

class HiddenProfiles(object):
    implements(INonInstallableProfiles)

    def getNonInstallableProfiles(self):
        return [ u'plone.app.openid', u'NuPlone', ]
