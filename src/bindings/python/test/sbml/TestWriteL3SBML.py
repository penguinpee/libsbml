#
# @file    TestWriteL3SBML.py
# @brief   Write SBML unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestWriteL3SBML.cpp
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

def util_NaN():
  z = 1e300
  z = z * z

  return z - z

def util_PosInf():
  z = 1e300
  z = z * z

  return z

def util_NegInf():
  z = 1e300
  z = z * z

  return -z 

def wrapString(s):
  return s
  pass

def LV_L3v1():
  return "level=\"3\" version=\"1\">\n"
  pass

def NS_L3v1():
  return "xmlns=\"http://www.sbml.org/sbml/level3/version1/core\" "
  pass

def SBML_END():
  return "</sbml>\n"
  pass

def SBML_START():
  return "<sbml "
  pass

def XML_START():
  return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
  pass

def wrapSBML_L3v1(s):
  r = XML_START()
  r += SBML_START()
  r += NS_L3v1()
  r += LV_L3v1()
  r += s
  r += SBML_END()
  return r
  pass

def wrapXML(s):
  r = XML_START()
  r += s
  return r
  pass


class TestWriteL3SBML(unittest.TestCase):

  global S
  S = None
  global D
  D = None

  def equals(self, *x):
    if len(x) == 2:
      return x[0] == x[1]
    elif len(x) == 1:
      return x[0] == self.OSS.str()

  def setUp(self):
    self.D = libsbml.SBMLDocument()
    self.D.setLevelAndVersion(3,1,False)
    self.S = 0
    pass  

  def tearDown(self):
    self.D = None
    self.S = None
    pass  

  def test_SBMLWriter_L3_create(self):
    w = libsbml.SBMLWriter()
    self.assert_( w != None )
    _dummyList = [ w ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLWriter_L3_setProgramName(self):
    w = libsbml.SBMLWriter()
    self.assert_( w != None )
    i = w.setProgramName( "sss")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    i = w.setProgramName("")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    _dummyList = [ w ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLWriter_L3_setProgramVersion(self):
    w = libsbml.SBMLWriter()
    self.assert_( w != None )
    i = w.setProgramVersion( "sss")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    i = w.setProgramVersion("")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    _dummyList = [ w ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_WriteL3SBML_Compartment(self):
    expected =  "<compartment id=\"A\" constant=\"true\"/>";
    c = self.D.createModel().createCompartment()
    c.setId("A")
    c.setConstant(True)
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    pass  

  def test_WriteL3SBML_Compartment_spatialDimensions(self):
    expected = "<compartment id=\"A\" spatialDimensions=\"2.1\" " + "constant=\"false\"/>";
    expected1 =  "<compartment id=\"A\" constant=\"false\"/>";
    c = self.D.createModel().createCompartment()
    c.setId("A")
    c.setConstant(False)
    c.setSpatialDimensions(2.1)
    self.assertEqual( True, self.equals(expected,c.toSBML()) )
    c.unsetSpatialDimensions()
    self.assertEqual( True, self.equals(expected1,c.toSBML()) )
    pass  

  def test_WriteL3SBML_Event(self):
    expected =  "<event id=\"e\"/>";
    e = self.D.createModel().createEvent()
    e.setId("e")
    e.setUseValuesFromTriggerTime(True)
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteL3SBML_Event_useValues(self):
    expected = wrapString("<event id=\"e\" useValuesFromTriggerTime=\"false\">\n" + 
    "  <delay/>\n" + 
    "</event>")
    e = self.D.createModel().createEvent()
    e.setId("e")
    e.setUseValuesFromTriggerTime(False)
    e.createDelay()
    self.assertEqual( True, self.equals(expected,e.toSBML()) )
    pass  

  def test_WriteL3SBML_INF(self):
    expected = "<parameter id=\"p\" value=\"INF\"" + " constant=\"true\"/>";
    p = self.D.createModel().createParameter()
    p.setId("p")
    p.setValue(util_PosInf())
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteL3SBML_KineticLaw_ListOfParameters(self):
    expected = wrapString("<kineticLaw>\n" + 
    "  <listOfLocalParameters>\n" + 
    "    <localParameter id=\"n\" value=\"1.2\"/>\n" + 
    "  </listOfLocalParameters>\n" + 
    "</kineticLaw>")
    kl = self.D.createModel().createReaction().createKineticLaw()
    p = kl.createLocalParameter()
    p.setId("n")
    p.setValue(1.2)
    self.assertEqual( True, self.equals(expected,kl.toSBML()) )
    pass  

  def test_WriteL3SBML_Model(self):
    expected = wrapSBML_L3v1("  <model/>\n"  
    )
    m = self.D.createModel("")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteL3SBML_Model_conversionFactor(self):
    expected = wrapSBML_L3v1("  <model conversionFactor=\"p\"/>\n"  
    )
    m = self.D.createModel("")
    m.setConversionFactor("p")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteL3SBML_Model_otherUnits(self):
    expected = wrapSBML_L3v1("  <model volumeUnits=\"litre\" areaUnits=\"area\" lengthUnits=\"metre\"/>\n"  
    )
    m = self.D.createModel("")
    m.setVolumeUnits("litre")
    m.setAreaUnits("area")
    m.setLengthUnits("metre")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteL3SBML_Model_substanceUnits(self):
    expected = wrapSBML_L3v1("  <model substanceUnits=\"mole\"/>\n"  
    )
    m = self.D.createModel("")
    m.setSubstanceUnits("mole")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteL3SBML_Model_timeUnits(self):
    expected = wrapSBML_L3v1("  <model timeUnits=\"second\"/>\n"  
    )
    m = self.D.createModel("")
    m.setTimeUnits("second")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteL3SBML_NaN(self):
    expected = "<parameter id=\"p\" value=\"NaN\"" + " constant=\"true\"/>";
    p = self.D.createModel().createParameter()
    p.setId("p")
    p.setValue(util_NaN())
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteL3SBML_NegINF(self):
    expected = "<parameter id=\"p\" value=\"-INF\"" + " constant=\"true\"/>";
    p = self.D.createModel().createParameter()
    p.setId("p")
    p.setValue(util_NegInf())
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteL3SBML_Parameter(self):
    expected = "<parameter id=\"Km1\" value=\"2.3\"" + " units=\"second\" constant=\"true\"/>";
    p = self.D.createModel().createParameter()
    p.setId("Km1")
    p.setValue(2.3)
    p.setUnits("second")
    p.setConstant(True)
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteL3SBML_Reaction(self):
    expected = "<reaction id=\"r\" reversible=\"false\"" + " fast=\"true\"/>";
    r = self.D.createModel().createReaction()
    r.setId("r")
    r.setReversible(False)
    r.setFast(True)
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteL3SBML_Reaction_compartment(self):
    expected = "<reaction id=\"r\" reversible=\"false\"" + " fast=\"true\" compartment=\"c\"/>";
    expected1 = "<reaction id=\"r\" reversible=\"false\"" + " fast=\"true\"/>";
    r = self.D.createModel().createReaction()
    r.setId("r")
    r.setReversible(False)
    r.setFast(True)
    r.setCompartment("c")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    r.unsetCompartment()
    self.assertEqual( True, self.equals(expected1,r.toSBML()) )
    pass  

  def test_WriteL3SBML_Reaction_full(self):
    expected = wrapString("<reaction id=\"v1\" reversible=\"true\" fast=\"false\">\n" + 
    "  <listOfReactants>\n" + 
    "    <speciesReference species=\"x0\" constant=\"false\"/>\n" + 
    "  </listOfReactants>\n" + 
    "  <listOfProducts>\n" + 
    "    <speciesReference species=\"s1\" constant=\"false\"/>\n" + 
    "  </listOfProducts>\n" + 
    "  <listOfModifiers>\n" + 
    "    <modifierSpeciesReference species=\"m1\"/>\n" + 
    "  </listOfModifiers>\n" + 
    "  <kineticLaw>\n" + 
    "    <math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n" + 
    "      <apply>\n" + 
    "        <divide/>\n" + 
    "        <apply>\n" + 
    "          <times/>\n" + 
    "          <ci> vm </ci>\n" + 
    "          <ci> s1 </ci>\n" + 
    "        </apply>\n" + 
    "        <apply>\n" + 
    "          <plus/>\n" + 
    "          <ci> km </ci>\n" + 
    "          <ci> s1 </ci>\n" + 
    "        </apply>\n" + 
    "      </apply>\n" + 
    "    </math>\n" + 
    "  </kineticLaw>\n" + 
    "</reaction>")
    self.D.createModel()
    r = self.D.getModel().createReaction()
    r.setId("v1")
    r.setReversible(True)
    r.createReactant().setSpecies("x0")
    r.createProduct().setSpecies("s1")
    r.createModifier().setSpecies("m1")
    r.createKineticLaw().setFormula("(vm * s1)/(km + s1)")
    self.assertEqual( True, self.equals(expected,r.toSBML()) )
    pass  

  def test_WriteL3SBML_SBMLDocument_L3v1(self):
    expected = wrapXML("<sbml xmlns=\"http://www.sbml.org/sbml/level3/version1/core\" " + "level=\"3\" version=\"1\"/>\n")
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteL3SBML_Species(self):
    expected = wrapString("<species id=\"Ca2\" compartment=\"cell\" initialAmount=\"0.7\"" + 
    " substanceUnits=\"mole\" hasOnlySubstanceUnits=\"false\"" + 
    " boundaryCondition=\"true\" constant=\"true\"/>")
    s = self.D.createModel().createSpecies()
    s.setId("Ca2")
    s.setCompartment("cell")
    s.setInitialAmount(0.7)
    s.setUnits("mole")
    s.setBoundaryCondition(True)
    s.setHasOnlySubstanceUnits(False)
    s.setConstant(True)
    self.assertEqual( True, self.equals(expected,s.toSBML()) )
    pass  

  def test_WriteL3SBML_SpeciesReference(self):
    expected = "<speciesReference species=\"s\"" + " stoichiometry=\"3\" constant=\"true\"/>";
    sr = self.D.createModel().createReaction().createReactant()
    sr.setSpecies("s")
    sr.setStoichiometry(3)
    sr.setConstant(True)
    self.assertEqual( True, self.equals(expected,sr.toSBML()) )
    pass  

  def test_WriteL3SBML_Species_conversionFactor(self):
    expected = wrapString("<species id=\"Ca2\" compartment=\"cell\"" + 
    " hasOnlySubstanceUnits=\"false\"" + 
    " boundaryCondition=\"true\" constant=\"true\"" + 
    " conversionFactor=\"p\"/>")
    expected1 = wrapString("<species id=\"Ca2\" compartment=\"cell\"" + 
    " hasOnlySubstanceUnits=\"false\"" + 
    " boundaryCondition=\"true\" constant=\"true\"/>")
    s = self.D.createModel().createSpecies()
    s.setId("Ca2")
    s.setCompartment("cell")
    s.setBoundaryCondition(True)
    s.setHasOnlySubstanceUnits(False)
    s.setConstant(True)
    s.setConversionFactor("p")
    self.assertEqual( True, self.equals(expected,s.toSBML()) )
    s.unsetConversionFactor()
    self.assertEqual( True, self.equals(expected1,s.toSBML()) )
    pass  

  def test_WriteL3SBML_Unit(self):
    expected = "<unit kind=\"kilogram\" exponent=\"0.2\"" + " scale=\"-3\" multiplier=\"3.2\"/>";
    u = self.D.createModel().createUnitDefinition().createUnit()
    u.setKind(libsbml.UNIT_KIND_KILOGRAM)
    exp = 0.2
    u.setExponent(exp)
    u.setScale(-3)
    u.setMultiplier(3.2)
    self.assertEqual( True, self.equals(expected,u.toSBML()) )
    pass  

  def test_WriteL3SBML_UnitDefinition(self):
    expected = wrapString("<unitDefinition id=\"myUnit\">\n" + 
    "  <listOfUnits>\n" + 
    "    <unit kind=\"mole\" exponent=\"1\" scale=\"0\" multiplier=\"1.8\"/>\n" + 
    "  </listOfUnits>\n" + 
    "</unitDefinition>")
    ud = self.D.createModel().createUnitDefinition()
    ud.setId("myUnit")
    u1 = ud.createUnit()
    u1.setKind(libsbml.UnitKind_forName("mole"))
    u1.setMultiplier(1.8)
    u1.setScale(0)
    u1.setExponent(1)
    self.assertEqual( True, self.equals(expected,ud.toSBML()) )
    pass  

  def test_WriteL3SBML_Unit_noValues(self):
    expected = "<unit kind=\"(Invalid UnitKind)\" exponent=\"NaN\"" + " scale=\"2147483647\" multiplier=\"NaN\"/>";
    u = self.D.createModel().createUnitDefinition().createUnit()
    self.assertEqual( True, self.equals(expected,u.toSBML()) )
    pass  

  def test_WriteL3SBML_bzip2(self):
    file = []
    file.append("../../../examples/sample-models/from-spec/level-3/algebraicrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/assignmentrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/boundarycondition.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/delay.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/dimerization.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/enzymekinetics.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/events.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/functiondef.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/multicomp.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/overdetermined.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/twodimensional.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/units.xml")

    bz2file = "test.xml.bz2"
    for f in file:
      d = libsbml.readSBML(f)
      self.assert_( d != None )
      if not libsbml.SBMLWriter.hasBzip2():
        self.assert_( libsbml.writeSBML(d,bz2file) == 0 )
        d = None
        continue
      result = libsbml.writeSBML(d,bz2file)
      self.assertEqual( 1, result )
      dg = libsbml.readSBML(bz2file)
      self.assert_( dg != None )
      self.assert_( ( dg.toSBML() != d.toSBML() ) == False )
      d = None
      dg = None
    pass


  def test_WriteL3SBML_elements(self):
    expected = wrapSBML_L3v1("  <model>\n" + 
    "    <listOfFunctionDefinitions>\n" + 
    "      <functionDefinition/>\n" + 
    "    </listOfFunctionDefinitions>\n" + 
    "    <listOfUnitDefinitions>\n" + 
    "      <unitDefinition/>\n" + 
    "    </listOfUnitDefinitions>\n" + 
    "    <listOfCompartments>\n" + 
    "      <compartment constant=\"true\"/>\n" + 
    "    </listOfCompartments>\n" + 
    "    <listOfSpecies>\n" + 
    "      <species hasOnlySubstanceUnits=\"false\"" + 
    " boundaryCondition=\"false\" constant=\"false\"/>\n" + 
    "    </listOfSpecies>\n" + 
    "    <listOfParameters>\n" + 
    "      <parameter constant=\"true\"/>\n" + 
    "    </listOfParameters>\n" + 
    "    <listOfInitialAssignments>\n" + 
    "      <initialAssignment/>\n" + 
    "    </listOfInitialAssignments>\n" + 
    "    <listOfRules>\n" + 
    "      <algebraicRule/>\n" + 
    "    </listOfRules>\n" + 
    "    <listOfConstraints>\n" + 
    "      <constraint/>\n" + 
    "    </listOfConstraints>\n" + 
    "    <listOfReactions>\n" + 
    "      <reaction reversible=\"true\" fast=\"false\"/>\n" + 
    "    </listOfReactions>\n" + 
    "    <listOfEvents>\n" + 
    "      <event/>\n" + 
    "    </listOfEvents>\n" + 
    "  </model>\n")
    m = self.D.createModel()
    m.createUnitDefinition()
    m.createFunctionDefinition()
    m.createCompartment()
    m.createEvent()
    m.createParameter()
    m.createAlgebraicRule()
    m.createInitialAssignment()
    m.createConstraint()
    m.createReaction()
    m.createSpecies()
    self.S = libsbml.writeSBMLToString(self.D)
    self.assertEqual( True, self.equals(expected,self.S) )
    pass  

  def test_WriteL3SBML_error(self):
    d = libsbml.SBMLDocument()
    w = libsbml.SBMLWriter()
    self.assertEqual( False, w.writeSBML(d, "/tmp/impossible/path/should/fail") )
    self.assert_( d.getNumErrors() == 1 )
    self.assert_( d.getError(0).getErrorId() == libsbml.XMLFileUnwritable )
    d = None
    w = None
    pass  

  def test_WriteL3SBML_gzip(self):
    file = []
    file.append("../../../examples/sample-models/from-spec/level-3/algebraicrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/assignmentrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/boundarycondition.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/delay.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/dimerization.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/enzymekinetics.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/events.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/functiondef.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/multicomp.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/overdetermined.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/twodimensional.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/units.xml")

    gzfile = "test.xml.gz"
    for f in file:
      d = libsbml.readSBML(f)
      self.assert_( d != None )
      if not libsbml.SBMLWriter.hasZlib():
        self.assert_( libsbml.writeSBML(d,gzfile) == 0 )
        d = None
        continue
      result = libsbml.writeSBML(d,gzfile)
      self.assertEqual( 1, result )
      dg = libsbml.readSBML(gzfile)
      self.assert_( dg != None )
      self.assert_( ( dg.toSBML() != d.toSBML() ) == False )
      d = None
      dg = None
    pass


  def test_WriteL3SBML_locale(self):
    expected = "<parameter id=\"p\" value=\"3.31\"" + " constant=\"true\"/>";
    p = self.D.createModel().createParameter()
    p.setId("p")
    p.setValue(3.31)
    self.assertEqual( True, self.equals(expected,p.toSBML()) )
    pass  

  def test_WriteL3SBML_zip(self):
    file = []
    file.append("../../../examples/sample-models/from-spec/level-3/algebraicrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/assignmentrules.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/boundarycondition.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/delay.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/dimerization.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/enzymekinetics.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/events.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/functiondef.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/multicomp.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/overdetermined.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/twodimensional.xml")
    file.append("../../../examples/sample-models/from-spec/level-3/units.xml")

    zipfile = "test.xml.zip"
    for f in file:
      d = libsbml.readSBML(f)
      self.assert_( d != None )
      if not libsbml.SBMLWriter.hasZlib():
        self.assert_( libsbml.writeSBML(d,zipfile) == 0 )
        d = None
        continue
      result = libsbml.writeSBML(d,zipfile)
      self.assertEqual( 1, result )
      dg = libsbml.readSBML(zipfile)
      self.assert_( dg != None )
      self.assert_( ( dg.toSBML() != d.toSBML() ) == False )
      d = None
      dg = None
    pass


def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestWriteL3SBML))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
