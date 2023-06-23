#
# @file    TestAlgebraicRule.py
# @brief   AlgebraicRule unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Ben Bornstein 
# 
# ====== WARNING ===== WARNING ===== WARNING ===== WARNING ===== WARNING ======
#
# DO NOT EDIT THIS FILE.
#
# This file was generated automatically by converting the file located at
# src/sbml/test/TestAlgebraicRule.c
# using the conversion program dev/utilities/translateTests/translateTests.pl.
# Any changes made here will be lost the next time the file is regenerated.
#
# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------

import sys
import unittest
import libsbml


class TestAlgebraicRule(unittest.TestCase):

  global AR
  AR = None

  def setUp(self):
    self.AR = libsbml.AlgebraicRule(2,4)
    if (self.AR == None):
      pass    
    pass  

  def tearDown(self):
    _dummyList = [ self.AR ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_AlgebraicRule_create(self):
    self.assertTrue( self.AR.getTypeCode() == libsbml.SBML_ALGEBRAIC_RULE )
    self.assertTrue( self.AR.getMetaId() == "" )
    self.assertTrue( self.AR.getNotes() == None )
    self.assertTrue( self.AR.getAnnotation() == None )
    self.assertTrue( self.AR.getFormula() == "" )
    self.assertTrue( self.AR.getMath() == None )
    pass  

  def test_AlgebraicRule_createWithFormula(self):
    ar = libsbml.AlgebraicRule(2,4)
    ar.setFormula( "1 + 1")
    self.assertTrue( ar.getTypeCode() == libsbml.SBML_ALGEBRAIC_RULE )
    self.assertTrue( ar.getMetaId() == "" )
    math = ar.getMath()
    self.assertTrue( math != None )
    formula = libsbml.formulaToString(math)
    self.assertTrue( formula != None )
    self.assertTrue((  "1 + 1" == formula ))
    self.assertTrue(( formula == ar.getFormula() ))
    _dummyList = [ ar ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_AlgebraicRule_createWithMath(self):
    math = libsbml.parseFormula("1 + 1")
    ar = libsbml.AlgebraicRule(2,4)
    ar.setMath(math)
    self.assertTrue( ar.getTypeCode() == libsbml.SBML_ALGEBRAIC_RULE )
    self.assertTrue( ar.getMetaId() == "" )
    self.assertTrue((  "1 + 1" == ar.getFormula() ))
    self.assertTrue( ar.getMath() != math )
    _dummyList = [ ar ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_AlgebraicRule_createWithNS(self):
    xmlns = libsbml.XMLNamespaces()
    xmlns.add( "http://www.sbml.org", "testsbml")
    sbmlns = libsbml.SBMLNamespaces(2,3)
    sbmlns.addNamespaces(xmlns)
    r = libsbml.AlgebraicRule(sbmlns)
    self.assertTrue( r.getTypeCode() == libsbml.SBML_ALGEBRAIC_RULE )
    self.assertTrue( r.getMetaId() == "" )
    self.assertTrue( r.getNotes() == None )
    self.assertTrue( r.getAnnotation() == None )
    self.assertTrue( r.getLevel() == 2 )
    self.assertTrue( r.getVersion() == 3 )
    self.assertTrue( r.getNamespaces() != None )
    self.assertTrue( r.getNamespaces().getLength() == 2 )
    _dummyList = [ r ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_AlgebraicRule_free_NULL(self):
    _dummyList = [ None ]; _dummyList[:] = []; del _dummyList
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestAlgebraicRule))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)