/**
 * \file    TestInferRnFunctions.cpp
 * \brief   Test extra functions for inferring rns
 * \author  Sarah Keating
 * 
 * <!--------------------------------------------------------------------------
 * This file is part of libSBML.  Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 *
 * Copyright (C) 2020 jointly by the following organizations:
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. University of Heidelberg, Heidelberg, Germany
 *     3. University College London, London, UK
 *
 * Copyright (C) 2019 jointly by the following organizations:
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. University of Heidelberg, Heidelberg, Germany
 *
 * Copyright (C) 2013-2018 jointly by the following organizations:
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK
 *     3. University of Heidelberg, Heidelberg, Germany
 *
 * Copyright (C) 2009-2013 jointly by the following organizations: 
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK
 *  
 * Copyright (C) 2006-2008 by the California Institute of Technology,
 *     Pasadena, CA, USA 
 *  
 * Copyright (C) 2002-2005 jointly by the following organizations: 
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. Japan Science and Technology Agency, Japan
 * 
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation.  A copy of the license agreement is provided
 * in the file named "LICENSE.txt" included with this software distribution
 * and also available online as http://sbml.org/software/libsbml/license.html
 * ---------------------------------------------------------------------- -->*/

#include <limits>
#include <iostream>
#include <cstdio>
#include <cstring>

#include <check.h>

#include <sbml/math/FormulaParser.h>
#include <sbml/math/FormulaFormatter.h>
#include <sbml/math/ASTNode.h>
#include <sbml/math/MathML.h>

#include <sbml/xml/XMLToken.h>
#include <sbml/xml/XMLNode.h>

/** @cond doxygenIgnored */

using namespace std;
LIBSBML_CPP_NAMESPACE_USE

/** @endcond */

CK_CPPSTART


START_TEST (test_eqivalent)
{
  const ASTNode *n = readMathMLFromString(
     "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
     "  <apply>"
     "    <plus/>"
    "    <ci> s </ci>"
    "    <cn> 4.1 </cn>"
     "  </apply>"
     "</math>"
    );

  fail_unless( n != NULL );
  char* formula = "s+4.1";
  ASTNode *node = SBML_parseFormula(formula);

  fail_unless(node->exactlyEqual(*n) == true);

  char* formula1 = "4.1+s";
  ASTNode *node1 = SBML_parseFormula(formula1);

  fail_unless(node1->exactlyEqual(*n) == false);
  delete n;
  delete node;
  delete node1;
}
END_TEST


START_TEST(test_refactor_numbers)
{
  const ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <plus/>"
    "    <cn> 4 </cn>"
    "    <ci> s </ci>"
    "  </apply>"
    "</math>"
  );
  // n treats 4 as real
  fail_unless(n != NULL);
  char* formula = "4+s";
  ASTNode *node = SBML_parseFormula(formula);
  // nodetreats 4 as integer

  fail_unless(node->exactlyEqual(*n) == false);

  node->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST


START_TEST(test_encompass_uminus1)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <minus/>"
    "    <cn> 4.1 </cn>"
    "  </apply>"
    "</math>"
  );
 
  fail_unless(n != NULL);
  char* formula = "-(4.1)";
  ASTNode *node = SBML_parseFormula(formula);

  fail_unless(node->exactlyEqual(*n) == false);

  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST


START_TEST(test_encompass_uminus2)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <minus/>"
    "  <apply>"
    "    <times/>"
    "    <cn> 4.1 </cn>"
    "    <ci> s </ci>"
    "  </apply>"
    "  </apply>"
    "</math>"
  );

  fail_unless(n != NULL);
  char* formula = "-4.1*s";
  ASTNode *node = SBML_parseFormula(formula);

  fail_unless(node->exactlyEqual(*n) == false);

  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

START_TEST(test_encompass_uminus3)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <minus/>"
    "  <apply>"
    "    <divide/>"
    "    <ci> a </ci>"
    "    <ci> s </ci>"
    "  </apply>"
    "  </apply>"
    "</math>"
  );

  fail_unless(n != NULL);
  char* formula = "(-1.0*a)/s";
  ASTNode *node = SBML_parseFormula(formula);

  fail_unless(node->exactlyEqual(*n) == false);

  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

START_TEST(test_encompass_uminus4)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <minus/>"
    "  <apply>"
    "    <plus/>"
    "    <ci> a </ci>"
    "    <ci> s </ci>"
    "  </apply>"
    "  </apply>"
    "</math>"
  );

  fail_unless(n != NULL);
  char* formula = "-1.0*(a+s)";
  ASTNode *node = SBML_parseFormula(formula);

  fail_unless(node->exactlyEqual(*n) == false);

  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

START_TEST(test_nonbinary)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <plus/>"
    "  <apply>"
    "    <plus/>"
    "    <ci> a </ci>"
    "    <ci> b </ci>"
    "  </apply>"
    "  <apply>"
    "    <plus/>"
    "    <ci> c </ci>"
    "    <ci> s </ci>"
    "  </apply>"
    "  </apply>"
    "</math>"
  );
  ASTNode * node = new ASTNode(AST_PLUS);
  ASTNode * a = new ASTNode(AST_NAME);
  a->setName("a");
  ASTNode * b = new ASTNode(AST_NAME);
  b->setName("b");
  ASTNode * c = new ASTNode(AST_NAME);
  c->setName("c");
  ASTNode * s = new ASTNode(AST_NAME);
  s->setName("s");

  node->addChild(a);
  node->addChild(b);
  node->addChild(c);
  node->addChild(s);

  fail_unless(n != NULL);

  fail_unless(node->exactlyEqual(*n) == false);

  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

START_TEST(test_reorder_args1)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <plus/>"
    "    <ci> b </ci>"
    "    <cn> 2.1 </cn>"
    "  </apply>"
    "</math>"
  );
  ASTNode * node = new ASTNode(AST_PLUS);
  ASTNode * a = new ASTNode(AST_REAL);
  a->setValue(2.1);
  ASTNode * b = new ASTNode(AST_NAME);
  b->setName("b");
  //ASTNode * c = new ASTNode(AST_NAME);
  //c->setName("c");
  //ASTNode * s = new ASTNode(AST_NAME);
  //s->setName("s");

  node->addChild(a);
  node->addChild(b);
  //node->addChild(c);
  //node->addChild(s);

  fail_unless(n != NULL);

  fail_unless(node->exactlyEqual(*n) == false);

  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

START_TEST(test_reorder_args1_combine_numbers1)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <plus/>"
    "    <cn> 3.1 </cn>"
    "    <ci> b </ci>"
    "    <cn> 2.1 </cn>"
    "  </apply>"
    "</math>"
  );
  ASTNode * node = new ASTNode(AST_PLUS);
  ASTNode * a = new ASTNode(AST_REAL);
  a->setValue(5.2);
  ASTNode * b = new ASTNode(AST_NAME);
  b->setName("b");

  node->addChild(a);
  node->addChild(b);

  fail_unless(n != NULL);

  fail_unless(node->exactlyEqual(*n) == false);
  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

START_TEST(test_reorder_args1_combine_numbers2)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <plus/>"
    "    <cn> 3.1 </cn>"
    "    <cn> 2.1 </cn>"
    "  </apply>"
    "</math>"
  );
  ASTNode * node = new ASTNode(AST_REAL);
  node->setValue(5.2);
  ASTNode * b = new ASTNode(AST_NAME);
  b->setName("b");

  fail_unless(n != NULL);

  fail_unless(node->exactlyEqual(*n) == false);
  
  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

START_TEST(test_reorder_args1_combine_numbers3)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <plus/>"
    "  <apply>"
    "    <minus/>"
    "    <cn> 3.1 </cn>"
    "    <cn> 2.1 </cn>"
    "  </apply>"
    "    <cn> 3.1 </cn>"
    "    <cn> 2.1 </cn>"
    "  </apply>"
    "</math>"
  );
  ASTNode * node = new ASTNode(AST_REAL);
  node->setValue(6.2);

  fail_unless(n != NULL);

  fail_unless(node->exactlyEqual(*n) == false);

  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

START_TEST(test_reorder_args2)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <plus/>"
    "  <apply>"
    "    <sin/>"
    "    <cn> 3.1 </cn>"
    "  </apply>"
    "    <cn> 3.1 </cn>"
    "    <ci> b </ci>"
    "  </apply>"
    "</math>"
  );
  ASTNode * node = new ASTNode(AST_PLUS);
  ASTNode * a = new ASTNode(AST_REAL);
  a->setValue(3.1);
  ASTNode * b = new ASTNode(AST_NAME);
  b->setName("b");
  ASTNode * c = new ASTNode(AST_FUNCTION_SIN);
  ASTNode * d = new ASTNode(AST_REAL);
  d->setValue(3.1);
  c->addChild(d);

  node->addChild(a);
  node->addChild(b);
  node->addChild(c);

  fail_unless(n != NULL);

  fail_unless(node->exactlyEqual(*n) == false);

  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

START_TEST(test_reorder_args2_combine_numbers1)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <plus/>"
    "  <apply>"
    "    <sin/>"
    "  <apply>"
    "    <plus/>"
    "    <cn> 2.2 </cn>"
    "    <cn> 3.1 </cn>"
    "  </apply>"
    "  </apply>"
    "    <cn> 3.1 </cn>"
    "    <ci> b </ci>"
    "  </apply>"
    "</math>"
  );
  ASTNode * node = new ASTNode(AST_PLUS);
  ASTNode * a = new ASTNode(AST_REAL);
  a->setValue(3.1);
  ASTNode * b = new ASTNode(AST_NAME);
  b->setName("b");
  ASTNode * c = new ASTNode(AST_FUNCTION_SIN);
  ASTNode * d = new ASTNode(AST_REAL);
  d->setValue(5.3);
  c->addChild(d);

  node->addChild(a);
  node->addChild(b);
  node->addChild(c);

  fail_unless(n != NULL);

  fail_unless(node->exactlyEqual(*n) == false);

  n->refactor();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

START_TEST(test_reorder_args3)
{
  ASTNode *n = readMathMLFromString(
    "<math xmlns='http://www.w3.org/1998/Math/MathML'>"
    "  <apply>"
    "    <times/>"
    "  <apply>"
    "    <sin/>"
    "  <apply>"
    "    <plus/>"
    "    <cn> 2.2 </cn>"
    "    <cn> 3.1 </cn>"
    "  </apply>"
    "  </apply>"
    "  <apply>"
    "    <plus/>"
    "    <cn> 1.2 </cn>"
    "    <cn> 4.4 </cn>"
    "  </apply>"
    "    <ci> b </ci>"
    "  </apply>"
    "</math>"
  );
  ASTNode * node = new ASTNode(AST_TIMES);
  ASTNode * a = new ASTNode(AST_REAL);
  a->setValue(5.6);
  ASTNode * b = new ASTNode(AST_NAME);
  b->setName("b");
  ASTNode * c = new ASTNode(AST_FUNCTION_SIN);
  ASTNode * d = new ASTNode(AST_REAL);
  d->setValue(5.3);
  c->addChild(d);
  //c->setName("c");
  //ASTNode * s = new ASTNode(AST_NAME);
  //s->setName("s");

  node->addChild(a);
  node->addChild(b);
  node->addChild(c);
  //node->addChild(s);

  fail_unless(n != NULL);

  fail_unless(node->exactlyEqual(*n) == false);
  n->printMath();
  n->refactor();
  n->printMath();

  fail_unless(node->exactlyEqual(*n) == true);
  delete n;
  delete node;
}
END_TEST

Suite *
create_suite_TestInferRnFunctions()
{
  Suite *suite = suite_create("TestInferRnFunctions");
  TCase *tcase = tcase_create("TestInferRnFunctions");

  tcase_add_test( tcase, test_eqivalent);
  tcase_add_test(tcase, test_refactor_numbers);
  tcase_add_test(tcase, test_encompass_uminus1);
  tcase_add_test(tcase, test_encompass_uminus2);
  tcase_add_test(tcase, test_encompass_uminus3);
  tcase_add_test(tcase, test_encompass_uminus4);
  tcase_add_test(tcase, test_nonbinary);
  tcase_add_test(tcase, test_reorder_args1);
  tcase_add_test(tcase, test_reorder_args1_combine_numbers1);
  tcase_add_test(tcase, test_reorder_args1_combine_numbers2);
  //tcase_add_test(tcase, test_reorder_args1_combine_numbers3);
  tcase_add_test(tcase, test_reorder_args2);
  tcase_add_test(tcase, test_reorder_args2_combine_numbers1);
  tcase_add_test(tcase, test_reorder_args3);

  suite_add_tcase(suite, tcase);

  return suite;
}


CK_CPPEND

