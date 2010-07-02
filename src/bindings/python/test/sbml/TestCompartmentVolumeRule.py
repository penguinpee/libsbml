#
# @file    TestCompartmentVolumeRule.py
# @brief   CompartmentVolumeRule unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Ben Bornstein 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestCompartmentVolumeRule.c
# with the help of conversion sciprt (ctest_converter.pl).
#
#<!---------------------------------------------------------------------------
# This file is part of libSBML.  Please visit http://sbml.org for more
# information about SBML, and the latest version of libSBML.
#
# Copyright 2005-2010 California Institute of Technology.
# Copyright 2002-2005 California Institute of Technology and
#                     Japan Science and Technology Corporation.
# 
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation.  A copy of the license agreement is provided
# in the file named "LICENSE.txt" included with this software distribution
# and also available online as http://sbml.org/software/libsbml/license.html
#--------------------------------------------------------------------------->*/
import sys
import unittest
import libsbml


class TestCompartmentVolumeRule(unittest.TestCase):

  global CVR
  CVR = None

  def setUp(self):
    self.CVR = libsbml.AssignmentRule(1,2)
    self.CVR.setL1TypeCode(libsbml.SBML_COMPARTMENT_VOLUME_RULE)
    if (self.CVR == None):
      pass    
    pass  

  def tearDown(self):
    _dummyList = [ self.CVR ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_CompartmentVolumeRule_create(self):
    self.assert_( self.CVR.getTypeCode() == libsbml.SBML_ASSIGNMENT_RULE )
    self.assert_( self.CVR.getL1TypeCode() == libsbml.SBML_COMPARTMENT_VOLUME_RULE )
    self.assert_( self.CVR.getNotes() == None )
    self.assert_( self.CVR.getAnnotation() == None )
    self.assert_( self.CVR.getFormula() == "" )
    self.assert_( self.CVR.getType() == libsbml.RULE_TYPE_SCALAR )
    self.assert_( self.CVR.getVariable() == "" )
    self.assertEqual( False, self.CVR.isSetVariable() )
    pass  

  def test_CompartmentVolumeRule_free_NULL(self):
    _dummyList = [ None ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_CompartmentVolumeRule_setCompartment(self):
    compartment =  "cell";
    self.CVR.setVariable(compartment)
    self.assert_(( compartment == self.CVR.getVariable() ))
    self.assertEqual( True, self.CVR.isSetVariable() )
    if (self.CVR.getVariable() == compartment):
      pass    
    c = self.CVR.getVariable()
    self.CVR.setVariable(c)
    self.assert_(( compartment == self.CVR.getVariable() ))
    self.CVR.setVariable("")
    self.assertEqual( False, self.CVR.isSetVariable() )
    if (self.CVR.getVariable() != None):
      pass    
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestCompartmentVolumeRule))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
