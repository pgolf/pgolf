"""

Launching all doctests in the tests directory using:

    - The test_suite helper from the testing product
    - the base FunctionalTestCase in base.py

"""

from pgolf.policy.tests.base import FunctionalTestCase, setup_site
from pgolf.testing.tests.test_doctests import test_doctests_suite

################################################################################
# GLOBALS avalaible in doctests
# IMPORT/DEFINE objects there or inside ./user_globals.py (better)
# globals from the testing product are also available.
################################################################################
# example:
# from for import bar
# and in your doctests, you can do:
# >>> bar.something
from pgolf.policy.tests.globals import *
################################################################################

def test_suite():
    """."""
    setup_site()
    return test_doctests_suite(
        __file__,
        globs=globals(),
        testklass=FunctionalTestCase
    )

# vim:set ft=python:
