/*
 * @file    TestSBMLConvert.java
 * @brief   SBMLConvert unit tests
 *
 * @author  Akiya Jouraku (Java conversion)
 * @author  Ben Bornstein 
 * 
 * ====== WARNING ===== WARNING ===== WARNING ===== WARNING ===== WARNING ======
 *
 * DO NOT EDIT THIS FILE.
 *
 * This file was generated automatically by converting the file located at
 * src/sbml/test/TestSBMLConvert.c
 * using the conversion program dev/utilities/translateTests/translateTests.pl.
 * Any changes made here will be lost the next time the file is regenerated.
 *
 * -----------------------------------------------------------------------------
 * This file is part of libSBML.  Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 *
 * Copyright (C) 2020 jointly by the following organizations:
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. University of Heidelberg, Heidelberg, Germany
 *     3. University College London, London, UK
 *
 * Copyright 2005-2010 California Institute of Technology.
 * Copyright 2002-2005 California Institute of Technology and
 *                     Japan Science and Technology Corporation.
 * 
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation.  A copy of the license agreement is provided
 * in the file named "LICENSE.txt" included with this software distribution
 * and also available online as http://sbml.org/software/libsbml/license.html
 * -----------------------------------------------------------------------------
 */

package org.sbml.libsbml.test.sbml;

import org.sbml.libsbml.*;

import java.io.File;
import java.lang.AssertionError;

public class TestSBMLConvert {

  static void assertTrue(boolean condition) throws AssertionError
  {
    if (condition == true)
    {
      return;
    }
    throw new AssertionError();
  }

  static void assertEquals(Object a, Object b) throws AssertionError
  {
    if ( (a == null) && (b == null) )
    {
      return;
    }
    else if ( (a == null) || (b == null) )
    {
      throw new AssertionError();
    }
    else if (a.equals(b))
    {
      return;
    }

    throw new AssertionError();
  }

  static void assertNotEquals(Object a, Object b) throws AssertionError
  {
    if ( (a == null) && (b == null) )
    {
      throw new AssertionError();
    }
    else if ( (a == null) || (b == null) )
    {
      return;
    }
    else if (a.equals(b))
    {
      throw new AssertionError();
    }
  }

  static void assertEquals(boolean a, boolean b) throws AssertionError
  {
    if ( a == b )
    {
      return;
    }
    throw new AssertionError();
  }

  static void assertNotEquals(boolean a, boolean b) throws AssertionError
  {
    if ( a != b )
    {
      return;
    }
    throw new AssertionError();
  }

  static void assertEquals(int a, int b) throws AssertionError
  {
    if ( a == b )
    {
      return;
    }
    throw new AssertionError();
  }

  static void assertNotEquals(int a, int b) throws AssertionError
  {
    if ( a != b )
    {
      return;
    }
    throw new AssertionError();
  }

  public void test_SBMLConvert_addModifiersToReaction()
  {
    SBMLDocument d = new  SBMLDocument(1,2);
    Model m = d.createModel();
    Reaction r = m.createReaction();
    KineticLaw kl = r.createKineticLaw();
    kl.setFormula( "k1*S1*S2*S3*S4*S5");
    SimpleSpeciesReference ssr1;
    SimpleSpeciesReference ssr2;
    Species s1 = m.createSpecies();
    s1.setId( "S1" );
    Species s2 = m.createSpecies();
    s2.setId( "S2");
    Species s3 = m.createSpecies();
    s3.setId( "S3");
    Species s4 = m.createSpecies();
    s4.setId( "S4");
    Species s5 = m.createSpecies();
    s5.setId( "S5");
    SpeciesReference sr1 = r.createReactant();
    SpeciesReference sr2 = r.createReactant();
    SpeciesReference sr3 = r.createProduct();
    sr1.setSpecies( "S1");
    sr2.setSpecies( "S2");
    sr3.setSpecies( "S5");
    assertTrue( r.getNumModifiers() == 0 );
    assertTrue( d.setLevelAndVersion(2,1,false) == true );
    assertTrue( d.getLevel() == 2 );
    assertTrue( d.getVersion() == 1 );
    assertTrue( m.getReaction(0).getNumModifiers() == 2 );
    ssr1 = m.getReaction(0).getModifier(0);
    ssr2 = m.getReaction(0).getModifier(1);
    assertTrue(ssr1.getSpecies().equals( "S3"));
    assertTrue(ssr2.getSpecies().equals( "S4"));
    d = null;
  }

  public void test_SBMLConvert_convertFromL3()
  {
    SBMLDocument d = new  SBMLDocument(3,1);
    Model m = d.createModel();
    String sid =  "C";
    Compartment c = m.createCompartment();
    c.setId(sid);
    c.setSize(1.2);
    c.setConstant(true);
    c.setSpatialDimensions(3.4);
    assertTrue( d.setLevelAndVersion(1,1,true) == false );
    assertTrue( d.setLevelAndVersion(1,2,true) == false );
    assertTrue( d.setLevelAndVersion(2,1,true) == false );
    assertTrue( d.setLevelAndVersion(2,2,true) == false );
    assertTrue( d.setLevelAndVersion(2,3,true) == false );
    assertTrue( d.setLevelAndVersion(2,4,true) == false );
    assertTrue( d.setLevelAndVersion(3,1,true) == true );
  }

  public void test_SBMLConvert_convertFromL3_conversionFactor()
  {
    SBMLDocument d = new  SBMLDocument(3,1);
    Model m = d.createModel();
    String sid =  "P";
    m.setConversionFactor(sid);
    Parameter c = m.createParameter();
    c.setId(sid);
    c.setConstant(true);
    assertTrue( d.setLevelAndVersion(1,1,true) == false );
    assertTrue( d.setLevelAndVersion(1,2,true) == false );
    assertTrue( d.setLevelAndVersion(2,1,true) == false );
    assertTrue( d.setLevelAndVersion(2,2,true) == false );
    assertTrue( d.setLevelAndVersion(2,3,true) == false );
    assertTrue( d.setLevelAndVersion(2,4,true) == false );
    assertTrue( d.setLevelAndVersion(3,1,true) == true );
  }

  public void test_SBMLConvert_convertFromL3_initialValue()
  {
    SBMLDocument d = new  SBMLDocument(3,1);
    Model m = d.createModel();
    Event e = m.createEvent();
    Trigger t = e.createTrigger();
    t.setInitialValue(false);
    assertTrue( d.setLevelAndVersion(1,1,false) == false );
    assertTrue( d.setLevelAndVersion(1,2,false) == true );
    assertTrue( d.setLevelAndVersion(2,1,false) == true );
    assertTrue( d.setLevelAndVersion(2,2,false) == true );
    assertTrue( d.setLevelAndVersion(2,3,false) == true );
    assertTrue( d.setLevelAndVersion(2,4,false) == true );
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
  }

  public void test_SBMLConvert_convertFromL3_modelUnits()
  {
    UnitDefinition ud;
    SBMLDocument d = new  SBMLDocument(3,1);
    Model m = d.createModel();
    m.setVolumeUnits( "litre");
    assertTrue( m.getNumUnitDefinitions() == 0 );
    assertTrue( d.setLevelAndVersion(2,4,false) == true );
    m = d.getModel();
    assertTrue( m.getNumUnitDefinitions() == 1 );
    ud = m.getUnitDefinition(0);
    assertTrue(ud.getId().equals( "volume"));
    assertTrue( ud.getNumUnits() == 1 );
    assertTrue( ud.getUnit(0).getKind() == libsbml.UNIT_KIND_LITRE );
  }

  public void test_SBMLConvert_convertFromL3_persistent()
  {
    SBMLDocument d = new  SBMLDocument(3,1);
    Model m = d.createModel();
    Event e = m.createEvent();
    Trigger t = e.createTrigger();
    t.setPersistent(false);
    assertTrue( d.setLevelAndVersion(1,1,false) == false );
    assertTrue( d.setLevelAndVersion(1,2,false) == true );
    assertTrue( d.setLevelAndVersion(2,1,false) == true );
    assertTrue( d.setLevelAndVersion(2,2,false) == true );
    assertTrue( d.setLevelAndVersion(2,3,false) == true );
    assertTrue( d.setLevelAndVersion(2,4,false) == true );
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
  }

  public void test_SBMLConvert_convertFromL3_priority()
  {
    SBMLDocument d = new  SBMLDocument(3,1);
    Model m = d.createModel();
    Event e = m.createEvent();
    Priority p = e.createPriority();
    assertTrue( d.setLevelAndVersion(1,1,false) == false );
    assertTrue( d.setLevelAndVersion(1,2,false) == true );
    assertTrue( d.setLevelAndVersion(2,1,false) == true );
    assertTrue( d.setLevelAndVersion(2,2,false) == true );
    assertTrue( d.setLevelAndVersion(2,3,false) == true );
    assertTrue( d.setLevelAndVersion(2,4,false) == true );
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
  }

  public void test_SBMLConvert_convertToL1_SBMLDocument()
  {
    SBMLDocument d = new  SBMLDocument(2,1);
    assertTrue( d.setLevelAndVersion(1,2,false) == true );
    assertTrue( d.getLevel() == 1 );
    assertTrue( d.getVersion() == 2 );
    d = null;
  }

  public void test_SBMLConvert_convertToL1_Species_Amount()
  {
    SBMLDocument d = new  SBMLDocument(2,1);
    Model m = d.createModel();
    String sid =  "C";
    Compartment c = new  Compartment(2,4);
    Species s = new  Species(2,4);
    c.setId(sid);
    m.addCompartment(c);
    s.setCompartment(sid);
    s.setInitialAmount(2.34);
    m.addSpecies(s);
    assertTrue( d.setLevelAndVersion(1,2,true) == true );
    assertTrue( s.getInitialAmount() == 2.34 );
    d = null;
  }

  public void test_SBMLConvert_convertToL1_Species_Concentration()
  {
    SBMLDocument d = new  SBMLDocument(2,1);
    Model m = d.createModel();
    String sid =  "C";
    Compartment c = new  Compartment(2,1);
    Species s = new  Species(2,1);
    c.setId(sid);
    c.setSize(1.2);
    m.addCompartment(c);
    s.setId( "s"  );
    s.setCompartment(sid);
    s.setInitialConcentration(2.34);
    m.addSpecies(s);
    assertTrue( d.setLevelAndVersion(1,2,true) == true );
    Species s1 = m.getSpecies(0);
    assertTrue( s1 != null );
    assertTrue(s1.getCompartment().equals( "C"));
    assertTrue( m.getCompartment( "C").getSize() == 1.2 );
    assertTrue( s1.getInitialConcentration() == 2.34 );
    assertTrue( s1.isSetInitialConcentration() == true );
    d = null;
  }

  public void test_SBMLConvert_convertToL2_SBMLDocument()
  {
    SBMLDocument d = new  SBMLDocument(1,2);
    assertTrue( d.setLevelAndVersion(2,1,false) == true );
    assertTrue( d.getLevel() == 2 );
    assertTrue( d.getVersion() == 1 );
    assertTrue( d.setLevelAndVersion(2,2,false) == true );
    assertTrue( d.getLevel() == 2 );
    assertTrue( d.getVersion() == 2 );
    assertTrue( d.setLevelAndVersion(2,3,false) == true );
    assertTrue( d.getLevel() == 2 );
    assertTrue( d.getVersion() == 3 );
    d = null;
  }

  public void test_SBMLConvert_convertToL2v4_DuplicateAnnotations_doc()
  {
    SBMLDocument d = new  SBMLDocument(2,1);
    d.createModel();
    String annotation =  "<rdf/>\n<rdf/>";
    int i = (d).setAnnotation(annotation);
    assertTrue( d.getLevel() == 2 );
    assertTrue( d.getVersion() == 1 );
    assertTrue( (d).getAnnotation().getNumChildren() == 2 );
    assertTrue( d.setLevelAndVersion(2,4,true) == true );
    assertTrue( d.getLevel() == 2 );
    assertTrue( d.getVersion() == 4 );
    assertTrue( (d).getAnnotation().getNumChildren() == 1 );
    d = null;
  }

  public void test_SBMLConvert_convertToL2v4_DuplicateAnnotations_model()
  {
    SBMLDocument d = new  SBMLDocument(2,1);
    Model m = d.createModel();
    String annotation =  "<rdf/>\n<rdf/>";
    int i = (m).setAnnotation(annotation);
    assertTrue( d.getLevel() == 2 );
    assertTrue( d.getVersion() == 1 );
    assertTrue( (m).getAnnotation().getNumChildren() == 2 );
    assertTrue( d.setLevelAndVersion(2,4,true) == true );
    assertTrue( d.getLevel() == 2 );
    assertTrue( d.getVersion() == 4 );
    m = d.getModel();
    assertTrue( (m).getAnnotation().getNumChildren() == 1 );
    d = null;
  }

  public void test_SBMLConvert_convertToL3_compartment()
  {
    SBMLDocument d = new  SBMLDocument(2,2);
    Model m = d.createModel();
    String sid =  "C";
    Compartment c = m.createCompartment();
    Compartment c1;
    c.setId(sid);
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    c1 = m.getCompartment(0);
    assertTrue( c1.hasRequiredAttributes() == true );
    d = null;
  }

  public void test_SBMLConvert_convertToL3_defaultUnits()
  {
    SBMLDocument d = new  SBMLDocument(1,2);
    Model m = d.createModel();
    String sid =  "C";
    Compartment c = m.createCompartment();
    c.setId(sid);
    c.setSize(1.2);
    c.setUnits( "volume");
    assertTrue( m.getNumUnitDefinitions() == 0 );
    assertTrue( d.setLevelAndVersion(3,1,true) == true );
    assertTrue( m.getNumUnitDefinitions() == 2 );
    UnitDefinition ud = m.getUnitDefinition(0);
    assertTrue( ud != null );
    assertTrue(ud.getId().equals( "volume"));
    assertTrue( ud.getNumUnits() == 1 );
    Unit u = ud.getUnit(0);
    assertTrue( u.getKind() == libsbml.UNIT_KIND_LITRE );
    assertTrue( u.getExponent() == 1 );
    assertTrue( u.getMultiplier() == 1 );
    assertTrue( u.getScale() == 0 );
    ud = m.getUnitDefinition(1);
    assertTrue( ud != null );
    assertTrue(ud.getId().equals( "area"));
    assertTrue( ud.getNumUnits() == 1 );
    u = ud.getUnit(0);
    assertTrue( u.getKind() == libsbml.UNIT_KIND_METRE );
    assertTrue( u.getExponent() == 2 );
    assertTrue( u.getMultiplier() == 1 );
    assertTrue( u.getScale() == 0 );
    assertTrue(m.isSetSubstanceUnits() == true);
    assertTrue(m.getTimeUnits().equals( "second"));
    d = null;
  }

  public void test_SBMLConvert_convertToL3_event()
  {
    SBMLDocument d = new  SBMLDocument(2,2);
    Model m = d.createModel();
    Event e = m.createEvent();
    Event e1;
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    e1 = m.getEvent(0);
    assertTrue( e1.hasRequiredAttributes() == true );
    d = null;
  }

  public void test_SBMLConvert_convertToL3_localParameters()
  {
    SBMLDocument d = new  SBMLDocument(1,2);
    Model m = d.createModel();
    Compartment c = m.createCompartment();
    c.setId( "c" );
    Species s = m.createSpecies();
    s.setId( "s");
    s.setCompartment( "c");
    Reaction r = m.createReaction();
    SpeciesReference sr = r.createReactant();
    sr.setSpecies( "s");
    KineticLaw kl = r.createKineticLaw();
    kl.setFormula( "s*k");
    Parameter p = kl.createParameter();
    p.setId( "k");
    assertTrue( kl.getNumLocalParameters() == 0 );
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    m = d.getModel();
    r = m.getReaction(0);
    kl = r.getKineticLaw();
    assertTrue( kl.getNumLocalParameters() == 1 );
    LocalParameter lp = kl.getLocalParameter(0);
    d = null;
  }

  public void test_SBMLConvert_convertToL3_parameter()
  {
    SBMLDocument d = new  SBMLDocument(2,2);
    Model m = d.createModel();
    String sid =  "C";
    Parameter p = m.createParameter();
    Parameter p1;
    p.setId(sid);
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    p1 = m.getParameter(0);
    assertTrue( p1.hasRequiredAttributes() == true );
    d = null;
  }

  public void test_SBMLConvert_convertToL3_product()
  {
    SBMLDocument d = new  SBMLDocument(2,2);
    Model m = d.createModel();
    Reaction r = m.createReaction();
    SpeciesReference sr = r.createProduct();
    SpeciesReference sr1;
    sr.setSpecies( "s" );
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    sr1 = m.getReaction(0).getProduct(0);
    assertTrue( sr1.hasRequiredAttributes() == true );
    d = null;
  }

  public void test_SBMLConvert_convertToL3_reactant()
  {
    SBMLDocument d = new  SBMLDocument(2,2);
    Model m = d.createModel();
    Reaction r = m.createReaction();
    SpeciesReference sr = r.createReactant();
    SpeciesReference sr1;
    sr.setSpecies( "s" );
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    sr1 = m.getReaction(0).getReactant(0);
    assertTrue( sr1.hasRequiredAttributes() == true );
    d = null;
  }

  public void test_SBMLConvert_convertToL3_reaction()
  {
    SBMLDocument d = new  SBMLDocument(2,2);
    Model m = d.createModel();
    String sid =  "C";
    Reaction r = m.createReaction();
    r.setId(sid);
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    Reaction r1 = m.getReaction(0);
    assertTrue( r1.hasRequiredAttributes() == true );
    d = null;
  }

  public void test_SBMLConvert_convertToL3_species()
  {
    SBMLDocument d = new  SBMLDocument(2,2);
    Model m = d.createModel();
    String sid =  "C";
    Species s = m.createSpecies();
    Species s1;
    s.setId(sid);
    s.setCompartment( "comp");
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    s1 = m.getSpecies(0);
    assertTrue( s1.hasRequiredAttributes() == true );
    d = null;
  }

  public void test_SBMLConvert_convertToL3_stoichiometryMath()
  {
    SBMLDocument d = new  SBMLDocument(2,1);
    Model m = d.createModel();
    Compartment c = m.createCompartment();
    c.setId( "c" );
    Species s = m.createSpecies();
    s.setId( "s");
    s.setCompartment( "c");
    Reaction r = m.createReaction();
    SpeciesReference sr = r.createReactant();
    sr.setSpecies( "s");
    StoichiometryMath sm = sr.createStoichiometryMath();
    ASTNode ast = libsbml.parseFormula("c*2");
    sm.setMath(ast);
    assertTrue( m.getNumRules() == 0 );
    assertTrue( sr.isSetId() == false );
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    m = d.getModel();
    r = m.getReaction(0);
    sr = r.getReactant(0);
    assertTrue( m.getNumRules() == 1 );
    assertTrue( sr.isSetId() == true );
    Rule rule = m.getRule(0);
    assertTrue( sr.getId().equals(rule.getVariable()) == true );
    d = null;
  }

  public void test_SBMLConvert_convertToL3_trigger()
  {
    SBMLDocument d = new  SBMLDocument(2,2);
    Model m = d.createModel();
    Event e = m.createEvent();
    Trigger t = e.createTrigger();
    Trigger t1;
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    t1 = m.getEvent(0).getTrigger();
    assertTrue( t1.hasRequiredAttributes() == true );
    d = null;
  }

  public void test_SBMLConvert_convertToL3_unit()
  {
    SBMLDocument d = new  SBMLDocument(2,2);
    Model m = d.createModel();
    String sid =  "C";
    UnitDefinition ud = m.createUnitDefinition();
    ud.setId(sid);
    Unit u = ud.createUnit();
    u.setKind(libsbml.UNIT_KIND_MOLE);
    assertTrue( d.setLevelAndVersion(3,1,false) == true );
    Unit u1 = m.getUnitDefinition(0).getUnit(0);
    assertTrue( u1.hasRequiredAttributes() == true );
    d = null;
  }

  public void test_SBMLConvert_invalidLevelVersion()
  {
    SBMLDocument d = new  SBMLDocument(2,1);
    Model m = d.createModel();
    String sid =  "C";
    Compartment c = m.createCompartment();
    c.setId(sid);
    c.setSize(1.2);
    c.setUnits( "volume");
    assertTrue( d.setLevelAndVersion(1,3,true) == false );
    assertTrue( d.setLevelAndVersion(2,7,true) == false );
    assertTrue( d.setLevelAndVersion(3,5,true) == false );
    assertTrue( d.setLevelAndVersion(4,1,true) == false );
  }

  /**
   * Loads the SWIG-generated libSBML Java module when this class is
   * loaded, or reports a sensible diagnostic message about why it failed.
   */
  static
  {
    String varname;
    String shlibname;

    if (System.getProperty("mrj.version") != null)
    {
      varname = "DYLD_LIBRARY_PATH";    // We're on a Mac.
      shlibname = "libsbmlj.jnilib and/or libsbml.dylib";
    }
    else
    {
      varname = "LD_LIBRARY_PATH";      // We're not on a Mac.
      shlibname = "libsbmlj.so and/or libsbml.so";
    }

    try
    {
      System.loadLibrary("sbmlj");
      // For extra safety, check that the jar file is in the classpath.
      Class.forName("org.sbml.libsbml.libsbml");
    }
    catch (SecurityException e)
    {
      e.printStackTrace();
      System.err.println("Could not load the libSBML library files due to a"+
                         " security exception.\n");
      System.exit(1);
    }
    catch (UnsatisfiedLinkError e)
    {
      e.printStackTrace();
      System.err.println("Error: could not link with the libSBML library files."+
                         " It is likely\nyour " + varname +
                         " environment variable does not include the directories\n"+
                         "containing the " + shlibname + " library files.\n");
      System.exit(1);
    }
    catch (ClassNotFoundException e)
    {
      e.printStackTrace();
      System.err.println("Error: unable to load the file libsbmlj.jar."+
                         " It is likely\nyour -classpath option and CLASSPATH" +
                         " environment variable\n"+
                         "do not include the path to libsbmlj.jar.\n");
      System.exit(1);
    }
  }
}