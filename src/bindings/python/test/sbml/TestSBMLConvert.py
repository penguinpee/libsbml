#
# @file    TestSBMLConvert.py
# @brief   SBMLConvert unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Ben Bornstein 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestSBMLConvert.c
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


class TestSBMLConvert(unittest.TestCase):


  def test_SBMLConvert_addModifiersToReaction(self):
    d = libsbml.SBMLDocument(1,2)
    m = d.createModel()
    r = m.createReaction()
    kl = r.createKineticLaw()
    kl.setFormula( "k1*S1*S2*S3*S4*S5")
    s1 = m.createSpecies()
    s1.setId( "S1" )
    s2 = m.createSpecies()
    s2.setId( "S2")
    s3 = m.createSpecies()
    s3.setId( "S3")
    s4 = m.createSpecies()
    s4.setId( "S4")
    s5 = m.createSpecies()
    s5.setId( "S5")
    sr1 = r.createReactant()
    sr2 = r.createReactant()
    sr3 = r.createProduct()
    sr1.setSpecies( "S1")
    sr2.setSpecies( "S2")
    sr3.setSpecies( "S5")
    self.assert_( r.getNumModifiers() == 0 )
    self.assert_( d.setLevelAndVersion(2,1,False) == True )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 1 )
    self.assert_( m.getReaction(0).getNumModifiers() == 2 )
    ssr1 = m.getReaction(0).getModifier(0)
    ssr2 = m.getReaction(0).getModifier(1)
    self.assert_((  "S3" == ssr1.getSpecies() ))
    self.assert_((  "S4" == ssr2.getSpecies() ))
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvert_convertFromL3(self):
    d = libsbml.SBMLDocument(3,1)
    m = d.createModel()
    sid =  "C";
    c = m.createCompartment()
    c.setId(sid)
    c.setSize(1.2)
    c.setUnits( "volume")
    self.assert_( d.setLevelAndVersion(1,1,False) == False )
    self.assert_( d.setLevelAndVersion(1,2,False) == False )
    self.assert_( d.setLevelAndVersion(2,1,False) == False )
    self.assert_( d.setLevelAndVersion(2,2,False) == False )
    self.assert_( d.setLevelAndVersion(2,3,False) == False )
    self.assert_( d.setLevelAndVersion(2,4,False) == False )
    self.assert_( d.setLevelAndVersion(3,1,False) == True )
    pass  

  def test_SBMLConvert_convertToL1_SBMLDocument(self):
    d = libsbml.SBMLDocument(2,1)
    self.assert_( d.setLevelAndVersion(1,2,False) == True )
    self.assert_( d.getLevel() == 1 )
    self.assert_( d.getVersion() == 2 )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvert_convertToL1_Species_Amount(self):
    d = libsbml.SBMLDocument(2,1)
    m = d.createModel()
    sid =  "C";
    c = libsbml.Compartment(2,4)
    s = libsbml.Species(2,4)
    c.setId(sid)
    m.addCompartment(c)
    s.setCompartment(sid)
    s.setInitialAmount(2.34)
    m.addSpecies(s)
    self.assert_( d.setLevelAndVersion(1,2,False) == True )
    self.assert_( s.getInitialAmount() == 2.34 )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvert_convertToL1_Species_Concentration(self):
    d = libsbml.SBMLDocument(2,1)
    m = d.createModel()
    sid =  "C";
    c = libsbml.Compartment(2,1)
    s = libsbml.Species(2,1)
    c.setId(sid)
    c.setSize(1.2)
    m.addCompartment(c)
    s.setId( "s"  )
    s.setCompartment(sid)
    s.setInitialConcentration(2.34)
    m.addSpecies(s)
    self.assert_( d.setLevelAndVersion(1,2,False) == True )
    s1 = m.getSpecies(0)
    self.assert_( s1 != None )
    self.assert_((  "C" == s1.getCompartment() ))
    self.assert_( m.getCompartment( "C").getSize() == 1.2 )
    self.assert_( s1.getInitialConcentration() == 2.34 )
    self.assert_( s1.isSetInitialConcentration() == True )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvert_convertToL2_SBMLDocument(self):
    d = libsbml.SBMLDocument(1,2)
    self.assert_( d.setLevelAndVersion(2,1,False) == True )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 1 )
    self.assert_( d.setLevelAndVersion(2,2,False) == True )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 2 )
    self.assert_( d.setLevelAndVersion(2,3,False) == True )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 3 )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvert_convertToL2v4_DuplicateAnnotations_doc(self):
    d = libsbml.SBMLDocument(2,1)
    d.createModel()
    annotation =  "<rdf/>\n<rdf/>";
    i = (d).setAnnotation(annotation)
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 1 )
    self.assert_( (d).getAnnotation().getNumChildren() == 2 )
    self.assert_( d.setLevelAndVersion(2,4,False) == True )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 4 )
    self.assert_( (d).getAnnotation().getNumChildren() == 1 )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvert_convertToL2v4_DuplicateAnnotations_model(self):
    d = libsbml.SBMLDocument(2,1)
    m = d.createModel()
    annotation =  "<rdf/>\n<rdf/>";
    i = (m).setAnnotation(annotation)
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 1 )
    self.assert_( (m).getAnnotation().getNumChildren() == 2 )
    self.assert_( d.setLevelAndVersion(2,4,False) == True )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 4 )
    m = d.getModel()
    self.assert_( (m).getAnnotation().getNumChildren() == 1 )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvert_convertToL3_defaultUnits(self):
    d = libsbml.SBMLDocument(1,2)
    m = d.createModel()
    sid =  "C";
    c = m.createCompartment()
    c.setId(sid)
    c.setSize(1.2)
    c.setUnits( "volume")
    self.assert_( m.getNumUnitDefinitions() == 0 )
    self.assert_( d.setLevelAndVersion(3,1,False) == True )
    self.assert_( m.getNumUnitDefinitions() == 2 )
    ud = m.getUnitDefinition(0)
    self.assert_( ud != None )
    self.assert_((  "volume" == ud.getId() ))
    self.assert_( ud.getNumUnits() == 1 )
    u = ud.getUnit(0)
    self.assert_( u.getKind() == libsbml.UNIT_KIND_LITRE )
    self.assert_( u.getExponent() == 1 )
    self.assert_( u.getMultiplier() == 1 )
    self.assert_( u.getScale() == 0 )
    ud = m.getUnitDefinition(1)
    self.assert_( ud != None )
    self.assert_((  "time" == ud.getId() ))
    self.assert_( ud.getNumUnits() == 1 )
    u = ud.getUnit(0)
    self.assert_( u.getKind() == libsbml.UNIT_KIND_SECOND )
    self.assert_( u.getExponent() == 1 )
    self.assert_( u.getMultiplier() == 1 )
    self.assert_( u.getScale() == 0 )
    self.assert_((  "time" == m.getTimeUnits() ))
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvert_convertToL3_localParameters(self):
    d = libsbml.SBMLDocument(1,2)
    m = d.createModel()
    c = m.createCompartment()
    c.setId( "c" )
    s = m.createSpecies()
    s.setId( "s")
    s.setCompartment( "c")
    r = m.createReaction()
    sr = r.createReactant()
    sr.setSpecies( "s")
    kl = r.createKineticLaw()
    kl.setFormula( "s*k")
    p = kl.createParameter()
    p.setId( "k")
    self.assert_( kl.getNumLocalParameters() == 0 )
    self.assert_( d.setLevelAndVersion(3,1,False) == True )
    m = d.getModel()
    r = m.getReaction(0)
    kl = r.getKineticLaw()
    self.assert_( kl.getNumLocalParameters() == 1 )
    lp = kl.getLocalParameter(0)
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvert_convertToL3_stoichiometryMath(self):
    d = libsbml.SBMLDocument(2,1)
    m = d.createModel()
    c = m.createCompartment()
    c.setId( "c" )
    s = m.createSpecies()
    s.setId( "s")
    s.setCompartment( "c")
    r = m.createReaction()
    sr = r.createReactant()
    sr.setSpecies( "s")
    sm = sr.createStoichiometryMath()
    ast = libsbml.parseFormula("c*2")
    sm.setMath(ast)
    self.assert_( m.getNumRules() == 0 )
    self.assert_( sr.isSetId() == 0 )
    self.assert_( d.setLevelAndVersion(3,1,False) == True )
    m = d.getModel()
    r = m.getReaction(0)
    sr = r.getReactant(0)
    self.assert_( m.getNumRules() == 1 )
    self.assert_( sr.isSetId() == 1 )
    rule = m.getRule(0)
    self.assert_( sr.getId() == rule.getVariable() )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvert_invalidLevelVersion(self):
    d = libsbml.SBMLDocument(2,1)
    m = d.createModel()
    sid =  "C";
    c = m.createCompartment()
    c.setId(sid)
    c.setSize(1.2)
    c.setUnits( "volume")
    self.assert_( d.setLevelAndVersion(1,3,False) == False )
    self.assert_( d.setLevelAndVersion(2,5,False) == False )
    self.assert_( d.setLevelAndVersion(3,2,False) == False )
    self.assert_( d.setLevelAndVersion(4,1,False) == False )
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestSBMLConvert))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
