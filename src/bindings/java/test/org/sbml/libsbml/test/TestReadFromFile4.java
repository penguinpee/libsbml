/*
 *
 * @file    TestReadFromFile4.java
 * @brief   Reads tests/l1v1-minimal.xml into memory and tests it.
 *
 * @author  Akiya Jouraku (Java conversion)
 * @author  Ben Bornstein 
 *
 * $Id:$
 * $HeadURL:$
 *
 * This test file was converted from src/sbml/test/TestReadFromFile4.c
 * with the help of conversion sciprt (ctest_converter.pl).
 *
 *<!---------------------------------------------------------------------------
 * This file is part of libSBML.  Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 *
 * Copyright 2005-2008 California Institute of Technology.
 * Copyright 2002-2005 California Institute of Technology and
 *                     Japan Science and Technology Corporation.
 * 
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation.  A copy of the license agreement is provided
 * in the file named "LICENSE.txt" included with this software distribution
 * and also available online as http://sbml.org/software/libsbml/license.html
 *--------------------------------------------------------------------------->*/


package org.sbml.libsbml.test;

import org.sbml.libsbml.*;

import java.io.File;
import java.lang.AssertionError;

public class TestReadFromFile4 {

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

  public void test_read_l1v1_minimal()
  {
    SBMLDocument d;
    Model m;
    Compartment c;
    Reaction r;
    Species s;
    SpeciesReference sr;
    String filename = "../../sbml/test/test-data/l1v1-minimal.xml";
    d = libsbml.readSBML(filename);
    if (d == null);
    {
    }
    assertTrue( d.getLevel() == 1 );
    assertTrue( d.getVersion() == 1 );
    m = d.getModel();
    assertTrue( m.getNumCompartments() == 1 );
    c = m.getCompartment(0);
    assertTrue(c.getName().equals( "x"));
    assertTrue( m.getNumSpecies() == 1 );
    s = m.getSpecies(0);
    assertTrue(s.getName().equals( "y" ));
    assertTrue(s.getCompartment().equals( "x" ));
    assertTrue( s.getInitialAmount() == 1 );
    assertTrue( s.getBoundaryCondition() == false );
    assertTrue( m.getNumReactions() == 1 );
    r = m.getReaction(0);
    assertTrue(r.getName().equals( "r"));
    assertTrue( r.getReversible() != false );
    assertTrue( r.getFast() == false );
    assertTrue( r.getNumReactants() == 1 );
    assertTrue( r.getNumProducts() == 1 );
    sr = r.getReactant(0);
    assertTrue(sr.getSpecies().equals( "y"));
    assertTrue( sr.getStoichiometry() == 1 );
    assertTrue( sr.getDenominator() == 1 );
    sr = r.getProduct(0);
    assertTrue(sr.getSpecies().equals( "y"));
    assertTrue( sr.getStoichiometry() == 1 );
    assertTrue( sr.getDenominator() == 1 );
    d = null;
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
