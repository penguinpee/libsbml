#
# @file    TestRequiredAttributes.py
# @brief   Test hasRequiredAttributes unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Ben Bornstein 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestRequiredAttributes.cpp
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


class TestRequiredAttributes(unittest.TestCase):


  def test_AlgebraicRule(self):
    ar = libsbml.AlgebraicRule(2,4)
    self.assertEqual( True, ar.hasRequiredAttributes() )
    ar = None
    pass  

  def test_AlgebraicRule_L1(self):
    ar = libsbml.AlgebraicRule(1,2)
    self.assertEqual( False, (ar.hasRequiredAttributes()) )
    ar.setFormula("ar")
    self.assertEqual( True, ar.hasRequiredAttributes() )
    ar = None
    pass  

  def test_AssignmentRule(self):
    r = libsbml.AssignmentRule(2,4)
    self.assertEqual( False, (r.hasRequiredAttributes()) )
    r.setVariable("r")
    self.assertEqual( True, r.hasRequiredAttributes() )
    r = None
    pass  

  def test_AssignmentRule_L1(self):
    r = libsbml.AssignmentRule(1,2)
    self.assertEqual( False, (r.hasRequiredAttributes()) )
    r.setVariable("r")
    self.assertEqual( False, (r.hasRequiredAttributes()) )
    r.setFormula("r")
    self.assertEqual( True, r.hasRequiredAttributes() )
    r = None
    pass  

  def test_Compartment(self):
    c = libsbml.Compartment(2,4)
    self.assertEqual( False, (c.hasRequiredAttributes()) )
    c.setId("c")
    self.assertEqual( True, c.hasRequiredAttributes() )
    c = None
    pass  

  def test_CompartmentType(self):
    ct = libsbml.CompartmentType(2,4)
    self.assertEqual( False, (ct.hasRequiredAttributes()) )
    ct.setId("c")
    self.assertEqual( True, ct.hasRequiredAttributes() )
    ct = None
    pass  

  def test_Constraint(self):
    c = libsbml.Constraint(2,4)
    self.assertEqual( True, c.hasRequiredAttributes() )
    c = None
    pass  

  def test_Delay(self):
    d = libsbml.Delay(2,4)
    self.assertEqual( True, d.hasRequiredAttributes() )
    d = None
    pass  

  def test_Event(self):
    e = libsbml.Event(2,4)
    self.assertEqual( True, e.hasRequiredAttributes() )
    e = None
    pass  

  def test_EventAssignment(self):
    ea = libsbml.EventAssignment(2,4)
    self.assertEqual( False, (ea.hasRequiredAttributes()) )
    ea.setVariable("ea")
    self.assertEqual( True, ea.hasRequiredAttributes() )
    ea = None
    pass  

  def test_FunctionDefinition(self):
    fd = libsbml.FunctionDefinition(2,4)
    self.assertEqual( False, (fd.hasRequiredAttributes()) )
    fd.setId("fd")
    self.assertEqual( True, fd.hasRequiredAttributes() )
    fd = None
    pass  

  def test_InitialAssignment(self):
    ia = libsbml.InitialAssignment(2,4)
    self.assertEqual( False, (ia.hasRequiredAttributes()) )
    ia.setSymbol("ia")
    self.assertEqual( True, ia.hasRequiredAttributes() )
    ia = None
    pass  

  def test_KineticLaw(self):
    kl = libsbml.KineticLaw(2,4)
    self.assertEqual( True, kl.hasRequiredAttributes() )
    kl = None
    pass  

  def test_KineticLaw_L1(self):
    kl = libsbml.KineticLaw(1,2)
    self.assertEqual( False, (kl.hasRequiredAttributes()) )
    kl.setFormula("kl")
    self.assertEqual( True, kl.hasRequiredAttributes() )
    kl = None
    pass  

  def test_Model(self):
    m = libsbml.Model(2,4)
    self.assertEqual( True, m.hasRequiredAttributes() )
    m = None
    pass  

  def test_ModifierSpeciesReference(self):
    msr = libsbml.ModifierSpeciesReference(2,4)
    self.assertEqual( False, (msr.hasRequiredAttributes()) )
    msr.setSpecies("msr")
    self.assertEqual( True, msr.hasRequiredAttributes() )
    msr = None
    pass  

  def test_Parameter(self):
    p = libsbml.Parameter(2,4)
    self.assertEqual( False, (p.hasRequiredAttributes()) )
    p.setId("p")
    self.assertEqual( True, p.hasRequiredAttributes() )
    p = None
    pass  

  def test_Parameter_L1V1(self):
    p = libsbml.Parameter(1,1)
    self.assertEqual( False, (p.hasRequiredAttributes()) )
    p.setId("p")
    self.assertEqual( False, (p.hasRequiredAttributes()) )
    p.setValue(12)
    self.assertEqual( True, p.hasRequiredAttributes() )
    p = None
    pass  

  def test_RateRule(self):
    r = libsbml.RateRule(2,4)
    self.assertEqual( False, (r.hasRequiredAttributes()) )
    r.setVariable("r")
    self.assertEqual( True, r.hasRequiredAttributes() )
    r = None
    pass  

  def test_RateRule_L1(self):
    r = libsbml.RateRule(1,2)
    self.assertEqual( False, (r.hasRequiredAttributes()) )
    r.setVariable("r")
    self.assertEqual( False, (r.hasRequiredAttributes()) )
    r.setFormula("r")
    self.assertEqual( True, r.hasRequiredAttributes() )
    r = None
    pass  

  def test_Reaction(self):
    r = libsbml.Reaction(2,4)
    self.assertEqual( False, (r.hasRequiredAttributes()) )
    r.setId("r")
    self.assertEqual( True, r.hasRequiredAttributes() )
    r = None
    pass  

  def test_Species(self):
    s = libsbml.Species(2,4)
    self.assertEqual( False, (s.hasRequiredAttributes()) )
    s.setId("s")
    self.assertEqual( False, (s.hasRequiredAttributes()) )
    s.setCompartment("c")
    self.assertEqual( True, s.hasRequiredAttributes() )
    s = None
    pass  

  def test_SpeciesReference(self):
    sr = libsbml.SpeciesReference(2,4)
    self.assertEqual( False, (sr.hasRequiredAttributes()) )
    sr.setSpecies("sr")
    self.assertEqual( True, sr.hasRequiredAttributes() )
    sr = None
    pass  

  def test_SpeciesType(self):
    st = libsbml.SpeciesType(2,4)
    self.assertEqual( False, (st.hasRequiredAttributes()) )
    st.setId("st")
    self.assertEqual( True, st.hasRequiredAttributes() )
    st = None
    pass  

  def test_Species_L1(self):
    s = libsbml.Species(1,2)
    self.assertEqual( False, (s.hasRequiredAttributes()) )
    s.setId("s")
    self.assertEqual( False, (s.hasRequiredAttributes()) )
    s.setCompartment("c")
    self.assertEqual( False, (s.hasRequiredAttributes()) )
    s.setInitialAmount(2)
    self.assertEqual( True, s.hasRequiredAttributes() )
    s = None
    pass  

  def test_StoichiometryMath(self):
    sm = libsbml.StoichiometryMath(2,4)
    self.assertEqual( True, sm.hasRequiredAttributes() )
    sm = None
    pass  

  def test_Trigger(self):
    t = libsbml.Trigger(2,4)
    self.assertEqual( True, t.hasRequiredAttributes() )
    t = None
    pass  

  def test_Unit(self):
    u = libsbml.Unit(2,4)
    self.assertEqual( False, (u.hasRequiredAttributes()) )
    u.setKind(libsbml.UNIT_KIND_MOLE)
    self.assertEqual( True, u.hasRequiredAttributes() )
    u = None
    pass  

  def test_UnitDefinition(self):
    ud = libsbml.UnitDefinition(2,4)
    self.assertEqual( False, (ud.hasRequiredAttributes()) )
    ud.setId("ud")
    self.assertEqual( True, ud.hasRequiredAttributes() )
    ud = None
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestRequiredAttributes))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
