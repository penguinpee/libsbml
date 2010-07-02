#
# @file    TestCompartmentType_newSetters.py
# @brief   CompartmentType unit tests for new set function API
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestCompartmentType_newSetters.c
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


class TestCompartmentType_newSetters(unittest.TestCase):

  global C
  C = None

  def setUp(self):
    self.C = libsbml.CompartmentType(2,2)
    if (self.C == None):
      pass    
    pass  

  def tearDown(self):
    _dummyList = [ self.C ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_CompartmentType_setId2(self):
    i = self.C.setId( "1cell")
    self.assert_( i == libsbml.LIBSBML_INVALID_ATTRIBUTE_VALUE )
    self.assertEqual( False, self.C.isSetId() )
    pass  

  def test_CompartmentType_setId3(self):
    i = self.C.setId( "cell")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.C.isSetId() )
    self.assert_((  "cell"  == self.C.getId() ))
    pass  

  def test_CompartmentType_setId4(self):
    i = self.C.setId("")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( False, self.C.isSetId() )
    pass  

  def test_CompartmentType_setName1(self):
    i = self.C.setName( "cell")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.C.isSetName() )
    i = self.C.unsetName()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( False, self.C.isSetName() )
    pass  

  def test_CompartmentType_setName2(self):
    i = self.C.setName( "1cell")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.C.isSetName() )
    i = self.C.unsetName()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( False, self.C.isSetName() )
    pass  

  def test_CompartmentType_setName3(self):
    i = self.C.setName("")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( False, self.C.isSetName() )
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestCompartmentType_newSetters))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
