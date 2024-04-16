/*
 * @file    TestCompartment.java
 * @brief   Compartment unit tests
 *
 * @author  Akiya Jouraku (Java conversion)
 * @author  Ben Bornstein 
 * 
 * ====== WARNING ===== WARNING ===== WARNING ===== WARNING ===== WARNING ======
 *
 * DO NOT EDIT THIS FILE.
 *
 * This file was generated automatically by converting the file located at
 * src/sbml/test/TestCompartment.c
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

public class TestCompartment {

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
  private Compartment C;

  protected void setUp() throws Exception
  {
    C = new  Compartment(2,4);
    if (C == null);
    {
    }
  }

  protected void tearDown() throws Exception
  {
    C = null;
  }

  public void test_Compartment_create()
  {
    assertTrue( C.getTypeCode() == libsbml.SBML_COMPARTMENT );
    assertTrue( C.getMetaId().equals("") == true );
    assertTrue( C.getNotes() == null );
    assertTrue( C.getAnnotation() == null );
    assertTrue( C.getId().equals("") == true );
    assertTrue( C.getName().equals("") == true );
    assertTrue( C.getUnits().equals("") == true );
    assertTrue( C.getOutside().equals("") == true );
    assertTrue( C.getSpatialDimensions() == 3 );
    assertTrue( C.getVolume() == 1.0 );
    assertTrue( C.getConstant() == true );
    assertEquals( false, C.isSetId() );
    assertEquals( false, C.isSetName() );
    assertEquals( false, C.isSetSize() );
    assertEquals( false, C.isSetVolume() );
    assertEquals( false, C.isSetUnits() );
    assertEquals( false, C.isSetOutside() );
  }

  public void test_Compartment_createWith()
  {
    Compartment c = new  Compartment(2,4);
    c.setId( "A");
    assertTrue( c.getTypeCode() == libsbml.SBML_COMPARTMENT );
    assertTrue( c.getMetaId().equals("") == true );
    assertTrue( c.getNotes() == null );
    assertTrue( c.getAnnotation() == null );
    assertTrue( c.getName().equals("") == true );
    assertTrue( c.getSpatialDimensions() == 3 );
    assertTrue(c.getId().equals( "A"     ));
    assertTrue( c.getConstant() == true );
    assertEquals( true, c.isSetId() );
    assertEquals( false, c.isSetName() );
    c = null;
  }

  public void test_Compartment_createWithNS()
  {
    XMLNamespaces xmlns = new  XMLNamespaces();
    xmlns.add( "http://www.sbml.org", "testsbml");
    SBMLNamespaces sbmlns = new  SBMLNamespaces(2,1);
    sbmlns.addNamespaces(xmlns);
    Compartment c = new  Compartment(sbmlns);
    assertTrue( c.getTypeCode() == libsbml.SBML_COMPARTMENT );
    assertTrue( c.getMetaId().equals("") == true );
    assertTrue( c.getNotes() == null );
    assertTrue( c.getAnnotation() == null );
    assertTrue( c.getLevel() == 2 );
    assertTrue( c.getVersion() == 1 );
    assertTrue( c.getNamespaces() != null );
    assertTrue( c.getNamespaces().getLength() == 2 );
    assertTrue( c.getName().equals("") == true );
    assertTrue( c.getSpatialDimensions() == 3 );
    assertTrue( c.getConstant() == true );
    c = null;
  }

  public void test_Compartment_free_NULL()
  {
  }

  public void test_Compartment_getSpatialDimensions()
  {
    C.setSpatialDimensions(1);
    assertTrue( C.getSpatialDimensions() == 1 );
  }

  public void test_Compartment_getsetConstant()
  {
    C.setConstant(true);
    assertTrue( C.getConstant() == true );
  }

  public void test_Compartment_getsetType()
  {
    C.setCompartmentType( "cell");
    assertTrue(C.getCompartmentType().equals( "cell" ));
    assertEquals( true, C.isSetCompartmentType() );
    C.unsetCompartmentType();
    assertEquals( false, C.isSetCompartmentType() );
  }

  public void test_Compartment_initDefaults()
  {
    Compartment c = new  Compartment(2,4);
    c.setId( "A");
    c.initDefaults();
    assertTrue(c.getId().equals( "A"));
    assertTrue( c.getName().equals("") == true );
    assertTrue( c.getUnits().equals("") == true );
    assertTrue( c.getOutside().equals("") == true );
    assertTrue( c.getSpatialDimensions() == 3 );
    assertTrue( c.getVolume() == 1.0 );
    assertTrue( c.getConstant() == true );
    assertEquals( true, c.isSetId() );
    assertEquals( false, c.isSetName() );
    assertEquals( false, c.isSetSize() );
    assertEquals( false, c.isSetVolume() );
    assertEquals( false, c.isSetUnits() );
    assertEquals( false, c.isSetOutside() );
    assertEquals( true, c.isSetSpatialDimensions() );
    assertEquals( true, c.isSetConstant() );
    c = null;
  }

  public void test_Compartment_setId()
  {
    String id =  "mitochondria";
    C.setId(id);
    assertTrue(C.getId().equals(id));
    assertEquals( true, C.isSetId() );
    if (C.getId() == id);
    {
    }
    C.setId(C.getId());
    assertTrue(C.getId().equals(id));
    C.setId("");
    assertEquals( false, C.isSetId() );
    if (C.getId() != null);
    {
    }
  }

  public void test_Compartment_setName()
  {
    String name =  "My_Favorite_Factory";
    C.setName(name);
    assertTrue(C.getName().equals(name));
    assertEquals( true, C.isSetName() );
    if (C.getName() == name);
    {
    }
    C.setName(C.getName());
    assertTrue(C.getName().equals(name));
    C.setName("");
    assertEquals( false, C.isSetName() );
    if (C.getName() != null);
    {
    }
  }

  public void test_Compartment_setOutside()
  {
    String outside =  "cell";
    C.setOutside(outside);
    assertTrue(C.getOutside().equals(outside));
    assertEquals( true, C.isSetOutside() );
    if (C.getOutside() == outside);
    {
    }
    C.setOutside(C.getOutside());
    assertTrue(C.getOutside().equals(outside));
    C.setOutside("");
    assertEquals( false, C.isSetOutside() );
    if (C.getOutside() != null);
    {
    }
  }

  public void test_Compartment_setUnits()
  {
    String units =  "volume";
    C.setUnits(units);
    assertTrue(C.getUnits().equals(units));
    assertEquals( true, C.isSetUnits() );
    if (C.getUnits() == units);
    {
    }
    C.setUnits(C.getUnits());
    assertTrue(C.getUnits().equals(units));
    C.setUnits("");
    assertEquals( false, C.isSetUnits() );
    if (C.getUnits() != null);
    {
    }
  }

  public void test_Compartment_unsetSize()
  {
    C.setSize(0.2);
    assertTrue( C.getSize() == 0.2 );
    assertEquals( true, C.isSetSize() );
    C.unsetSize();
    assertEquals( false, C.isSetSize() );
  }

  public void test_Compartment_unsetVolume()
  {
    C.setVolume(1.0);
    assertTrue( C.getVolume() == 1.0 );
    C.unsetVolume();
    assertEquals( false, C.isSetVolume() );
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