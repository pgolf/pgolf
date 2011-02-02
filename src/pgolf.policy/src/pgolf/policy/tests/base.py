from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc
import transaction
from OFS.Folder import Folder

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup


################################################################################
"""


Lot of files generated by the collective.generic packages  will try to load user defined objects in user specific files.
The final goal is to regenerate easyly the test infrastructure on templates updates without impacting
user-specific test boilerplate.
We do not use paster local commands (insert/update) as it cannot determine witch is specific or not and we prefer to totally
separe generated stuff and what is user specific



If you need to edit something in this file, you must have better to do it in:


    - user_base.py


Objects that you can edit and get things overidden are:


    - user_base.py

        * method: setup_pgolf_policy()

            method to setup the plone site

        * class: pgolf_policy_TestCase

            Base plone test case like PloneTestCase

        * class: pgolf_policy_FunctionalTestCase:

            Functionnal TestBase barely based on the previous TestCase.



Think to put "FAILS_ON_UNTESTED_ELEMENT" to True in testing.cfg for production mode or to test very strictly your code!
This will issue errors for untested elements instead of just simple warnings !


"""
################################################################################


TESTED_PRODUCTS = (\
#with_ploneproduct_contentwellportlet
    'ContentWellPortlets',
#with_ploneproduct_ploneboard
    'CMFPlacefulWorkflow',
    'Ploneboard',
    'SimpleAttachment',
#with_ploneproduct_ploneformgen
    'PloneFormGen',
#with_ploneproduct_csvreplica
    #'csvreplicata',
#with_ploneproduct_tinymce
    'TinyMCE',
)
for product in TESTED_PRODUCTS:
    ztc.installProduct(product)

@onsetup
def setup_policyPloneSite():
    """Set up the additional products required for the pgolf) site policy.

    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """
    # ------------------------------------------------------------------------------------
    # Get five errors if any for making debug easy.
    # ------------------------------------------------------------------------------------
    fiveconfigure.debug_mode = True

    # ------------------------------------------------------------------------------------
    # Import all our python modules required by our packages
    # ------------------------------------------------------------------------------------
#with_ploneproduct_pz3cform
    import five.grok
    import plone.app.z3cform
    import plone.directives.form
    import plone.z3cform
#with_ploneproduct_ploneformgen
    import Products.PloneFormGen
#with_ploneproduct_ploneboard
    import Products.Ploneboard
    import Products.SimpleAttachment
#with_ploneproduct_contentwellportlet
    import Products.ContentWellPortlets
#with_ploneproduct_cgallery
    import collective.gallery
#with_ploneproduct_tinymce
    import Products.TinyMCE
#with_ploneproduct_ploneappblob
    import plone.app.blob
#with_ploneproduct_cpwkf
    import Products.CMFPlacefulWorkflow

    # ------------------------------------------------------------------------------------
    # - Load the python packages that are registered as Zope2 Products via Five
    #   which can't happen until we have loaded the package ZCML.
    # ------------------------------------------------------------------------------------

#with_ploneproduct_ploneappblob
    ztc.installPackage('plone.app.blob')


    ztc.installPackage('pgolf.policy')
    ztc.installPackage('pgolf.skin')
    ztc.installPackage('pgolf.tma') 

    # ------------------------------------------------------------------------------------
    # Load our own policy & dependency zcml
    # ------------------------------------------------------------------------------------
    import pgolf.policy
    zcml.load_config('configure.zcml', pgolf.policy)


    # ------------------------------------------------------------------------------------
    # Reset five debug mode as we do not use it anymore
    # ------------------------------------------------------------------------------------
    fiveconfigure.debug_mode = False

class TestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here.
    """
    class Session(dict):
        def set(self, key, value):
            self[key] = value

    def afterSetUp(self):
        # support for sessions without invalidreferences if using zeo temp storage
        self.app.REQUEST['SESSION'] = self.Session()
        if not hasattr(self.app, 'temp_folder'):
            tf = Folder('temp_folder')
            self.app._setObject('temp_folder', tf)
            transaction.commit()
        ztc.utils.setupCoreSessions(self.app)

class FunctionalTestCase(ptc.FunctionalTestCase, TestCase):
    """Functionnal base TestCase."""

# try to load user code
try: from pgolf.policy.tests.user_base import setup_policyPloneSite
except: pass

try:from pgolf.policy.tests.user_base import TestCase
except: pass

try:from pgolf.policy.tests.user_base import FunctionalTestCase
except: pass

# The order here is important: We first call the (deferred) function which
# installs the products we need for the pgolf package. Then, we let
# PloneTestCase set up this product on installation.
def setup_site():
    setup_policyPloneSite()
    ptc.setupPloneSite(products=[\
    # if we have csvreplicata, just say that a plone site can't live without it.
        'csvreplicata',
        'pgolf.policy']
    )
# vim:set ft=python:
