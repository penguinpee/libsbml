#
# @file    TestSBase_newSetters.py
# @brief   SBase unit tests for new set API
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestSBase_newSetters.cpp
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

def wrapString(s):
  return s
  pass

SBML_INT_MAX = 2147483647

class TestSBase_newSetters(unittest.TestCase):

  global S
  S = None

  def setUp(self):
    self.S = libsbml.Model(2,4)
    if (self.S == None):
      pass    
    pass  

  def tearDown(self):
    self.S = None
    pass  

  def test_SBase_addCVTerms(self):
    cv = libsbml.CVTerm(libsbml.BIOLOGICAL_QUALIFIER)
    cv.setBiologicalQualifierType(libsbml.BQB_ENCODES)
    cv.addResource( "foo")
    i = self.S.addCVTerm(cv)
    self.assert_( i == libsbml.LIBSBML_UNEXPECTED_ATTRIBUTE )
    self.assert_( self.S.getNumCVTerms() == 0 )
    self.S.setMetaId( "_id")
    i = self.S.addCVTerm(cv)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.getNumCVTerms() == 1 )
    self.assert_( self.S.getCVTerms() != None )
    i = self.S.addCVTerm(None)
    self.assert_( i == libsbml.LIBSBML_OPERATION_FAILED )
    self.assert_( self.S.getNumCVTerms() == 1 )
    self.assert_( self.S.getCVTerms() != None )
    cv2 = libsbml.CVTerm(libsbml.MODEL_QUALIFIER)
    i = self.S.addCVTerm(cv2)
    self.assert_( i == libsbml.LIBSBML_INVALID_OBJECT )
    self.assert_( self.S.getNumCVTerms() == 1 )
    self.assert_( self.S.getCVTerms() != None )
    _dummyList = [ cv ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ cv2 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_appendAnnotation(self):
    token = libsbml.XMLToken("This is a test note")
    node = libsbml.XMLNode(token)
    token1 = libsbml.XMLToken("This is additional")
    node1 = libsbml.XMLNode(token1)
    i = self.S.setAnnotation(node)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    i = self.S.appendAnnotation(node1)
    t1 = self.S.getAnnotation()
    self.assert_( t1.getNumChildren() == 2 )
    self.assert_((     "This is a test note" == t1.getChild(0).getCharacters() ))
    self.assert_((     "This is additional" == t1.getChild(1).getCharacters() ))
    pass  

  def test_SBase_appendAnnotationString(self):
    token = libsbml.XMLToken("This is a test note")
    node = libsbml.XMLNode(token)
    i = self.S.setAnnotation(node)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    i = self.S.appendAnnotation( "This is additional")
    t1 = self.S.getAnnotation()
    self.assert_( t1.getNumChildren() == 2 )
    self.assert_((     "This is a test note" == t1.getChild(0).getCharacters() ))
    c1 = t1.getChild(1)
    self.assert_( c1.getNumChildren() == 0 )
    self.assert_((  "This is additional" == c1.getCharacters() ))
    pass  

  def test_SBase_appendNotes(self):
    triple = libsbml.XMLTriple("p", "", "")
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    token4 = libsbml.XMLToken("This is my text")
    node4 = libsbml.XMLNode(token4)
    token5 = libsbml.XMLToken("This is additional text")
    node5 = libsbml.XMLNode(token5)
    token = libsbml.XMLToken(triple,att,ns)
    node = libsbml.XMLNode(token)
    node.addChild(node4)
    i = self.S.setNotes(node)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    token1 = libsbml.XMLToken(triple,att,ns)
    node1 = libsbml.XMLNode(token1)
    node1.addChild(node5)
    i = self.S.appendNotes(node1)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    node2 = self.S.getNotes()
    self.assert_( node2.getNumChildren() == 2 )
    self.assert_((  "p" == node2.getChild(0).getName() ))
    self.assert_( node2.getChild(0).getNumChildren() == 1 )
    self.assert_((  "p" == node2.getChild(1).getName() ))
    self.assert_( node2.getChild(1).getNumChildren() == 1 )
    chars1 = node2.getChild(0).getChild(0).getCharacters()
    chars2 = node2.getChild(1).getChild(0).getCharacters()
    self.assert_((  "This is my text" == chars1 ))
    self.assert_((  "This is additional text" == chars2 ))
    _dummyList = [ node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ node1 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_appendNotes1(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    html_triple = libsbml.XMLTriple("html", "", "")
    head_triple = libsbml.XMLTriple("head", "", "")
    title_triple = libsbml.XMLTriple("title", "", "")
    body_triple = libsbml.XMLTriple("body", "", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    html_token = libsbml.XMLToken(html_triple,att,ns)
    head_token = libsbml.XMLToken(head_triple,att)
    title_token = libsbml.XMLToken(title_triple,att)
    body_token = libsbml.XMLToken(body_triple,att)
    p_token = libsbml.XMLToken(p_triple,att)
    text_token = libsbml.XMLToken("This is my text")
    html_node = libsbml.XMLNode(html_token)
    head_node = libsbml.XMLNode(head_token)
    title_node = libsbml.XMLNode(title_token)
    body_node = libsbml.XMLNode(body_token)
    p_node = libsbml.XMLNode(p_token)
    text_node = libsbml.XMLNode(text_token)
    text_token1 = libsbml.XMLToken("This is more text")
    html_node1 = libsbml.XMLNode(html_token)
    head_node1 = libsbml.XMLNode(head_token)
    title_node1 = libsbml.XMLNode(title_token)
    body_node1 = libsbml.XMLNode(body_token)
    p_node1 = libsbml.XMLNode(p_token)
    text_node1 = libsbml.XMLNode(text_token1)
    p_node.addChild(text_node)
    body_node.addChild(p_node)
    head_node.addChild(title_node)
    html_node.addChild(head_node)
    html_node.addChild(body_node)
    p_node1.addChild(text_node1)
    body_node1.addChild(p_node1)
    head_node1.addChild(title_node1)
    html_node1.addChild(head_node1)
    html_node1.addChild(body_node1)
    i = self.S.setNotes(html_node)
    i = self.S.appendNotes(html_node1)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "html" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child = child.getChild(1)
    self.assert_((  "body" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child1 = child.getChild(0)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is my text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    child1 = child.getChild(1)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is more text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node1 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_appendNotes2(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    html_triple = libsbml.XMLTriple("html", "", "")
    head_triple = libsbml.XMLTriple("head", "", "")
    title_triple = libsbml.XMLTriple("title", "", "")
    body_triple = libsbml.XMLTriple("body", "", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    html_token = libsbml.XMLToken(html_triple,att,ns)
    head_token = libsbml.XMLToken(head_triple,att)
    title_token = libsbml.XMLToken(title_triple,att)
    body_token = libsbml.XMLToken(body_triple,att)
    p_token = libsbml.XMLToken(p_triple,att)
    text_token = libsbml.XMLToken("This is my text")
    html_node = libsbml.XMLNode(html_token)
    head_node = libsbml.XMLNode(head_token)
    title_node = libsbml.XMLNode(title_token)
    body_node = libsbml.XMLNode(body_token)
    p_node = libsbml.XMLNode(p_token)
    text_node = libsbml.XMLNode(text_token)
    body_token1 = libsbml.XMLToken(body_triple,att,ns)
    text_token1 = libsbml.XMLToken("This is more text")
    body_node1 = libsbml.XMLNode(body_token1)
    p_node1 = libsbml.XMLNode(p_token)
    text_node1 = libsbml.XMLNode(text_token1)
    p_node.addChild(text_node)
    body_node.addChild(p_node)
    head_node.addChild(title_node)
    html_node.addChild(head_node)
    html_node.addChild(body_node)
    p_node1.addChild(text_node1)
    body_node1.addChild(p_node1)
    i = self.S.setNotes(html_node)
    i = self.S.appendNotes(body_node1)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "html" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child = child.getChild(1)
    self.assert_((  "body" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child1 = child.getChild(0)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is my text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    child1 = child.getChild(1)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is more text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node1 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_appendNotes3(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    html_triple = libsbml.XMLTriple("html", "", "")
    head_triple = libsbml.XMLTriple("head", "", "")
    title_triple = libsbml.XMLTriple("title", "", "")
    body_triple = libsbml.XMLTriple("body", "", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    html_token = libsbml.XMLToken(html_triple,att,ns)
    head_token = libsbml.XMLToken(head_triple,att)
    title_token = libsbml.XMLToken(title_triple,att)
    body_token = libsbml.XMLToken(body_triple,att)
    p_token = libsbml.XMLToken(p_triple,att)
    text_token = libsbml.XMLToken("This is my text")
    html_node = libsbml.XMLNode(html_token)
    head_node = libsbml.XMLNode(head_token)
    title_node = libsbml.XMLNode(title_token)
    body_node = libsbml.XMLNode(body_token)
    p_node = libsbml.XMLNode(p_token)
    text_node = libsbml.XMLNode(text_token)
    p_token1 = libsbml.XMLToken(p_triple,att,ns)
    text_token1 = libsbml.XMLToken("This is more text")
    p_node1 = libsbml.XMLNode(p_token1)
    text_node1 = libsbml.XMLNode(text_token1)
    p_node.addChild(text_node)
    body_node.addChild(p_node)
    head_node.addChild(title_node)
    html_node.addChild(head_node)
    html_node.addChild(body_node)
    p_node1.addChild(text_node1)
    i = self.S.setNotes(html_node)
    i = self.S.appendNotes(p_node1)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "html" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child = child.getChild(1)
    self.assert_((  "body" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child1 = child.getChild(0)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is my text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    child1 = child.getChild(1)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is more text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node1 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_appendNotes4(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    html_triple = libsbml.XMLTriple("html", "", "")
    head_triple = libsbml.XMLTriple("head", "", "")
    title_triple = libsbml.XMLTriple("title", "", "")
    body_triple = libsbml.XMLTriple("body", "", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    html_token = libsbml.XMLToken(html_triple,att,ns)
    head_token = libsbml.XMLToken(head_triple,att)
    title_token = libsbml.XMLToken(title_triple,att)
    body_token = libsbml.XMLToken(body_triple,att)
    p_token = libsbml.XMLToken(p_triple,att)
    body_token1 = libsbml.XMLToken(body_triple,att,ns)
    text_token = libsbml.XMLToken("This is my text")
    body_node = libsbml.XMLNode(body_token1)
    p_node = libsbml.XMLNode(p_token)
    text_node = libsbml.XMLNode(text_token)
    text_token1 = libsbml.XMLToken("This is more text")
    html_node1 = libsbml.XMLNode(html_token)
    head_node1 = libsbml.XMLNode(head_token)
    title_node1 = libsbml.XMLNode(title_token)
    body_node1 = libsbml.XMLNode(body_token)
    p_node1 = libsbml.XMLNode(p_token)
    text_node1 = libsbml.XMLNode(text_token1)
    p_node.addChild(text_node)
    body_node.addChild(p_node)
    p_node1.addChild(text_node1)
    body_node1.addChild(p_node1)
    head_node1.addChild(title_node1)
    html_node1.addChild(head_node1)
    html_node1.addChild(body_node1)
    i = self.S.setNotes(body_node)
    i = self.S.appendNotes(html_node1)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "html" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child = child.getChild(1)
    self.assert_((  "body" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child1 = child.getChild(0)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is my text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    child1 = child.getChild(1)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is more text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node1 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_appendNotes5(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    html_triple = libsbml.XMLTriple("html", "", "")
    head_triple = libsbml.XMLTriple("head", "", "")
    title_triple = libsbml.XMLTriple("title", "", "")
    body_triple = libsbml.XMLTriple("body", "", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    html_token = libsbml.XMLToken(html_triple,att,ns)
    head_token = libsbml.XMLToken(head_triple,att)
    title_token = libsbml.XMLToken(title_triple,att)
    body_token = libsbml.XMLToken(body_triple,att)
    p_token = libsbml.XMLToken(p_triple,att)
    p_token1 = libsbml.XMLToken(p_triple,att,ns)
    text_token = libsbml.XMLToken("This is my text")
    p_node = libsbml.XMLNode(p_token1)
    text_node = libsbml.XMLNode(text_token)
    text_token1 = libsbml.XMLToken("This is more text")
    html_node1 = libsbml.XMLNode(html_token)
    head_node1 = libsbml.XMLNode(head_token)
    title_node1 = libsbml.XMLNode(title_token)
    body_node1 = libsbml.XMLNode(body_token)
    p_node1 = libsbml.XMLNode(p_token)
    text_node1 = libsbml.XMLNode(text_token1)
    p_node.addChild(text_node)
    p_node1.addChild(text_node1)
    body_node1.addChild(p_node1)
    head_node1.addChild(title_node1)
    html_node1.addChild(head_node1)
    html_node1.addChild(body_node1)
    i = self.S.setNotes(p_node)
    i = self.S.appendNotes(html_node1)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "html" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child = child.getChild(1)
    self.assert_((  "body" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child1 = child.getChild(0)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is my text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    child1 = child.getChild(1)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is more text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node1 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_appendNotes6(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    body_triple = libsbml.XMLTriple("body", "", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    body_token = libsbml.XMLToken(body_triple,att,ns)
    p_token = libsbml.XMLToken(p_triple,att)
    text_token = libsbml.XMLToken("This is my text")
    body_node = libsbml.XMLNode(body_token)
    p_node = libsbml.XMLNode(p_token)
    text_node = libsbml.XMLNode(text_token)
    text_token1 = libsbml.XMLToken("This is more text")
    body_node1 = libsbml.XMLNode(body_token)
    p_node1 = libsbml.XMLNode(p_token)
    text_node1 = libsbml.XMLNode(text_token1)
    p_node.addChild(text_node)
    body_node.addChild(p_node)
    p_node1.addChild(text_node1)
    body_node1.addChild(p_node1)
    i = self.S.setNotes(body_node)
    i = self.S.appendNotes(body_node1)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "body" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child1 = child.getChild(0)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is my text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    child1 = child.getChild(1)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is more text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node1 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_appendNotes7(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    body_triple = libsbml.XMLTriple("body", "", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    body_token = libsbml.XMLToken(body_triple,att,ns)
    p_token1 = libsbml.XMLToken(p_triple,att,ns)
    text_token = libsbml.XMLToken("This is my text")
    p_token = libsbml.XMLToken(p_triple,att)
    p_node = libsbml.XMLNode(p_token1)
    text_node = libsbml.XMLNode(text_token)
    text_token1 = libsbml.XMLToken("This is more text")
    body_node1 = libsbml.XMLNode(body_token)
    p_node1 = libsbml.XMLNode(p_token)
    text_node1 = libsbml.XMLNode(text_token1)
    p_node.addChild(text_node)
    p_node1.addChild(text_node1)
    body_node1.addChild(p_node1)
    i = self.S.setNotes(p_node)
    i = self.S.appendNotes(body_node1)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "body" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child1 = child.getChild(0)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is my text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    child1 = child.getChild(1)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is more text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node1 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_appendNotes8(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    body_triple = libsbml.XMLTriple("body", "", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    body_token = libsbml.XMLToken(body_triple,att,ns)
    p_token = libsbml.XMLToken(p_triple,att)
    text_token = libsbml.XMLToken("This is my text")
    body_node = libsbml.XMLNode(body_token)
    p_node = libsbml.XMLNode(p_token)
    text_node = libsbml.XMLNode(text_token)
    p_token1 = libsbml.XMLToken(p_triple,att,ns)
    text_token1 = libsbml.XMLToken("This is more text")
    p_node1 = libsbml.XMLNode(p_token1)
    text_node1 = libsbml.XMLNode(text_token1)
    p_node.addChild(text_node)
    body_node.addChild(p_node)
    p_node1.addChild(text_node1)
    i = self.S.setNotes(body_node)
    i = self.S.appendNotes(p_node1)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "body" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child1 = child.getChild(0)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is my text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    child1 = child.getChild(1)
    self.assert_((  "p" == child1.getName() ))
    self.assert_( child1.getNumChildren() == 1 )
    child1 = child1.getChild(0)
    self.assert_((  "This is more text" == child1.getCharacters() ))
    self.assert_( child1.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node1 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_appendNotesString(self):
    notes =  "<p xmlns=\"http://www.w3.org/1999/xhtml\">This is a test note </p>";
    taggednotes = wrapString("<notes>\n" + "  <p xmlns=\"http://www.w3.org/1999/xhtml\">This is a test note </p>\n" + "</notes>")
    taggednewnotes = wrapString("<notes>\n" + "  <p xmlns=\"http://www.w3.org/1999/xhtml\">This is a test note </p>\n" + 
    "  <p xmlns=\"http://www.w3.org/1999/xhtml\">This is more test notes </p>\n" + 
    "</notes>")
    badnotes =  "<notes>This is a test note</notes>";
    newnotes =  "<p xmlns=\"http://www.w3.org/1999/xhtml\">This is more test notes </p>";
    i = self.S.setNotes(notes)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    i = self.S.appendNotes(badnotes)
    notes1 = self.S.getNotesString()
    self.assert_( i == libsbml.LIBSBML_INVALID_OBJECT )
    self.assert_( self.S.isSetNotes() == True )
    self.assert_(( notes1 == taggednotes ))
    i = self.S.appendNotes(newnotes)
    notes1 = self.S.getNotesString()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    self.assert_(( notes1 == taggednewnotes ))
    pass  

  def test_SBase_appendNotesString1(self):
    notes = wrapString("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <head>\n" + 
    "    <title/>\n" + 
    "  </head>\n" + 
    "  <body>\n" + 
    "    <p>This is a test note </p>\n" + 
    "  </body>\n" + 
    "</html>")
    taggednewnotes = wrapString("<notes>\n" + 
    "  <html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + 
    "    <head>\n" + 
    "      <title/>\n" + 
    "    </head>\n" + 
    "    <body>\n" + 
    "      <p>This is a test note </p>\n" + 
    "      <p>This is more test notes </p>\n" + 
    "    </body>\n" + 
    "  </html>\n" + 
    "</notes>")
    addnotes = wrapString("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <head>\n" + 
    "    <title/>\n" + 
    "  </head>\n" + 
    "  <body>\n" + 
    "    <p>This is more test notes </p>\n" + 
    "  </body>\n" + 
    "</html>")
    i = self.S.setNotes(notes)
    i = self.S.appendNotes(addnotes)
    notes1 = self.S.getNotesString()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    self.assert_(( notes1 == taggednewnotes ))
    pass  

  def test_SBase_appendNotesString2(self):
    notes = wrapString("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <head>\n" + 
    "    <title/>\n" + 
    "  </head>\n" + 
    "  <body>\n" + 
    "    <p>This is a test note </p>\n" + 
    "  </body>\n" + 
    "</html>")
    taggednewnotes = wrapString("<notes>\n" + 
    "  <html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + 
    "    <head>\n" + 
    "      <title/>\n" + 
    "    </head>\n" + 
    "    <body>\n" + 
    "      <p>This is a test note </p>\n" + 
    "      <p>This is more test notes </p>\n" + 
    "    </body>\n" + 
    "  </html>\n" + 
    "</notes>")
    addnotes = wrapString("<body xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <p>This is more test notes </p>\n" + "</body>\n")
    i = self.S.setNotes(notes)
    i = self.S.appendNotes(addnotes)
    notes1 = self.S.getNotesString()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    self.assert_(( notes1 == taggednewnotes ))
    pass  

  def test_SBase_appendNotesString3(self):
    notes = wrapString("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <head>\n" + 
    "    <title/>\n" + 
    "  </head>\n" + 
    "  <body>\n" + 
    "    <p>This is a test note </p>\n" + 
    "  </body>\n" + 
    "</html>")
    taggednewnotes = wrapString("<notes>\n" + 
    "  <html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + 
    "    <head>\n" + 
    "      <title/>\n" + 
    "    </head>\n" + 
    "    <body>\n" + 
    "      <p>This is a test note </p>\n" + 
    "      <p xmlns=\"http://www.w3.org/1999/xhtml\">This is more test notes </p>\n" + 
    "    </body>\n" + 
    "  </html>\n" + 
    "</notes>")
    addnotes =  "<p xmlns=\"http://www.w3.org/1999/xhtml\">This is more test notes </p>";
    i = self.S.setNotes(notes)
    i = self.S.appendNotes(addnotes)
    notes1 = self.S.getNotesString()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    self.assert_(( notes1 == taggednewnotes ))
    pass  

  def test_SBase_appendNotesString4(self):
    notes = wrapString("<body xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <p>This is a test note </p>\n" + "</body>")
    taggednewnotes = wrapString("<notes>\n" + 
    "  <html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + 
    "    <head>\n" + 
    "      <title/>\n" + 
    "    </head>\n" + 
    "    <body>\n" + 
    "      <p>This is a test note </p>\n" + 
    "      <p>This is more test notes </p>\n" + 
    "    </body>\n" + 
    "  </html>\n" + 
    "</notes>")
    addnotes = wrapString("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <head>\n" + 
    "    <title/>\n" + 
    "  </head>\n" + 
    "  <body>\n" + 
    "    <p>This is more test notes </p>\n" + 
    "  </body>\n" + 
    "</html>")
    i = self.S.setNotes(notes)
    i = self.S.appendNotes(addnotes)
    notes1 = self.S.getNotesString()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    self.assert_(( notes1 == taggednewnotes ))
    pass  

  def test_SBase_appendNotesString5(self):
    notes =  "<p xmlns=\"http://www.w3.org/1999/xhtml\">This is a test note </p>";
    taggednewnotes = wrapString("<notes>\n" + 
    "  <html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + 
    "    <head>\n" + 
    "      <title/>\n" + 
    "    </head>\n" + 
    "    <body>\n" + 
    "      <p xmlns=\"http://www.w3.org/1999/xhtml\">This is a test note </p>\n" + 
    "      <p>This is more test notes </p>\n" + 
    "    </body>\n" + 
    "  </html>\n" + 
    "</notes>")
    addnotes = wrapString("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <head>\n" + 
    "    <title/>\n" + 
    "  </head>\n" + 
    "  <body>\n" + 
    "    <p>This is more test notes </p>\n" + 
    "  </body>\n" + 
    "</html>")
    i = self.S.setNotes(notes)
    i = self.S.appendNotes(addnotes)
    notes1 = self.S.getNotesString()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    self.assert_(( notes1 == taggednewnotes ))
    pass  

  def test_SBase_appendNotesString6(self):
    notes = wrapString("<body xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <p>This is a test note </p>\n" + "</body>")
    taggednewnotes = wrapString("<notes>\n" + 
    "  <body xmlns=\"http://www.w3.org/1999/xhtml\">\n" + 
    "    <p>This is a test note </p>\n" + 
    "    <p>This is more test notes </p>\n" + 
    "  </body>\n" + 
    "</notes>")
    addnotes = wrapString("<body xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <p>This is more test notes </p>\n" + "</body>")
    i = self.S.setNotes(notes)
    i = self.S.appendNotes(addnotes)
    notes1 = self.S.getNotesString()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    self.assert_(( notes1 == taggednewnotes ))
    pass  

  def test_SBase_appendNotesString7(self):
    notes =  "<p xmlns=\"http://www.w3.org/1999/xhtml\">This is a test note </p>";
    taggednewnotes = wrapString("<notes>\n" + 
    "  <body xmlns=\"http://www.w3.org/1999/xhtml\">\n" + 
    "    <p xmlns=\"http://www.w3.org/1999/xhtml\">This is a test note </p>\n" + 
    "    <p>This is more test notes </p>\n" + 
    "  </body>\n" + 
    "</notes>")
    addnotes = wrapString("<body xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <p>This is more test notes </p>\n" + "</body>")
    i = self.S.setNotes(notes)
    i = self.S.appendNotes(addnotes)
    notes1 = self.S.getNotesString()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    self.assert_(( notes1 == taggednewnotes ))
    pass  

  def test_SBase_appendNotesString8(self):
    notes = wrapString("<body xmlns=\"http://www.w3.org/1999/xhtml\">\n" + "  <p>This is a test note </p>\n" + "</body>")
    taggednewnotes = wrapString("<notes>\n" + 
    "  <body xmlns=\"http://www.w3.org/1999/xhtml\">\n" + 
    "    <p>This is a test note </p>\n" + 
    "    <p xmlns=\"http://www.w3.org/1999/xhtml\">This is more test notes </p>\n" + 
    "  </body>\n" + 
    "</notes>")
    addnotes =  "<p xmlns=\"http://www.w3.org/1999/xhtml\">This is more test notes </p>";
    i = self.S.setNotes(notes)
    i = self.S.appendNotes(addnotes)
    notes1 = self.S.getNotesString()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    self.assert_(( notes1 == taggednewnotes ))
    pass  

  def test_SBase_setAnnotation(self):
    token = libsbml.XMLToken("This is a test note")
    node = libsbml.XMLNode(token)
    i = self.S.setAnnotation(node)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetAnnotation() == True )
    i = self.S.unsetAnnotation()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.S.unsetAnnotation()
    self.assert_( self.S.isSetAnnotation() == False )
    i = self.S.setAnnotation(node)
    i = self.S.setAnnotation(None)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetAnnotation() == False )
    pass  

  def test_SBase_setAnnotationString(self):
    annotation =  "This is a test note";
    taggedannotation =  "<annotation>This is a test note</annotation>";
    i = self.S.setAnnotation(annotation)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetAnnotation() == True )
    i = self.S.setAnnotation( "")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetAnnotation() == False )
    i = self.S.setAnnotation(taggedannotation)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetAnnotation() == True )
    i = self.S.unsetAnnotation()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetAnnotation() == False )
    pass  

  def test_SBase_setMetaId1(self):
    c = libsbml.Compartment(1,2)
    i = c.setMetaId( "cell")
    self.assert_( i == libsbml.LIBSBML_UNEXPECTED_ATTRIBUTE )
    self.assertEqual( False, c.isSetMetaId() )
    c = None
    pass  

  def test_SBase_setMetaId2(self):
    i = self.S.setMetaId( "1cell")
    self.assert_( i == libsbml.LIBSBML_INVALID_ATTRIBUTE_VALUE )
    self.assertEqual( False, self.S.isSetMetaId() )
    i = self.S.unsetMetaId()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( False, self.S.isSetMetaId() )
    pass  

  def test_SBase_setMetaId3(self):
    i = self.S.setMetaId( "cell")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.S.isSetMetaId() )
    self.assert_((  "cell"  == self.S.getMetaId() ))
    i = self.S.unsetMetaId()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( False, self.S.isSetMetaId() )
    pass  

  def test_SBase_setMetaId4(self):
    i = self.S.setMetaId( "cell")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.S.isSetMetaId() )
    self.assert_((  "cell"  == self.S.getMetaId() ))
    i = self.S.setMetaId("")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( False, self.S.isSetMetaId() )
    pass  

  def test_SBase_setModelHistory(self):
    sb = libsbml.Species(2,4)
    mh = libsbml.ModelHistory()
    i = sb.setModelHistory(mh)
    self.assert_( i == libsbml.LIBSBML_UNEXPECTED_ATTRIBUTE )
    _dummyList = [ mh ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_setModelHistory_Model(self):
    history = libsbml.ModelHistory()
    mc = libsbml.ModelCreator()
    date = libsbml.Date(2005,12,30,12,15,45,1,2,0)
    mc.setFamilyName( "Keating")
    mc.setGivenName( "Sarah")
    mc.setEmail( "sbml-team@caltech.edu")
    mc.setOrganisation( "UH")
    history.addCreator(mc)
    history.setCreatedDate(date)
    history.setModifiedDate(date)
    i = self.S.setModelHistory(history)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    _dummyList = [ history ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_setNamespaces(self):
    ns = libsbml.XMLNamespaces()
    ns.add("url", "name")
    i = self.S.setNamespaces(ns)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( (self.S).getNamespaces().getLength() == 1 )
    i = self.S.setNamespaces(None)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( (self.S).getNamespaces() == None )
    pass  

  def test_SBase_setNotes(self):
    triple = libsbml.XMLTriple("p", "", "")
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    tt = libsbml.XMLToken("This is my text")
    n1 = libsbml.XMLNode(tt)
    token = libsbml.XMLToken(triple,att,ns)
    node = libsbml.XMLNode(token)
    node.addChild(n1)
    i = self.S.setNotes(node)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    i = self.S.unsetNotes()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( (self.S.isSetNotes() == True) == False )
    token = libsbml.XMLToken("This is a test note")
    node = libsbml.XMLNode(token)
    i = self.S.setNotes(node)
    self.assert_( i == libsbml.LIBSBML_INVALID_OBJECT )
    self.assert_( (self.S.isSetNotes() == True) == False )
    token = libsbml.XMLToken(triple,att,ns)
    node = libsbml.XMLNode(token)
    node.addChild(n1)
    i = self.S.setNotes(node)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    i = self.S.setNotes(None)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( (self.S.isSetNotes() == True) == False )
    _dummyList = [ node ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_setNotes1(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    html_triple = libsbml.XMLTriple("html", "", "")
    head_triple = libsbml.XMLTriple("head", "", "")
    title_triple = libsbml.XMLTriple("title", "", "")
    body_triple = libsbml.XMLTriple("body", "", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    html_token = libsbml.XMLToken(html_triple,att,ns)
    head_token = libsbml.XMLToken(head_triple,att)
    title_token = libsbml.XMLToken(title_triple,att)
    body_token = libsbml.XMLToken(body_triple,att)
    p_token = libsbml.XMLToken(p_triple,att)
    text_token = libsbml.XMLToken("This is my text")
    html_node = libsbml.XMLNode(html_token)
    head_node = libsbml.XMLNode(head_token)
    title_node = libsbml.XMLNode(title_token)
    body_node = libsbml.XMLNode(body_token)
    p_node = libsbml.XMLNode(p_token)
    text_node = libsbml.XMLNode(text_token)
    p_node.addChild(text_node)
    body_node.addChild(p_node)
    head_node.addChild(title_node)
    html_node.addChild(head_node)
    html_node.addChild(body_node)
    i = self.S.setNotes(html_node)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "html" == child.getName() ))
    self.assert_( child.getNumChildren() == 2 )
    child = child.getChild(1)
    self.assert_((  "body" == child.getName() ))
    self.assert_( child.getNumChildren() == 1 )
    child = child.getChild(0)
    self.assert_((  "p" == child.getName() ))
    self.assert_( child.getNumChildren() == 1 )
    child = child.getChild(0)
    self.assert_((  "This is my text" == child.getCharacters() ))
    self.assert_( child.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ html_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ head_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_setNotes2(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    body_triple = libsbml.XMLTriple("body", "", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    body_token = libsbml.XMLToken(body_triple,att,ns)
    p_token = libsbml.XMLToken(p_triple,att)
    text_token = libsbml.XMLToken("This is my text")
    body_node = libsbml.XMLNode(body_token)
    p_node = libsbml.XMLNode(p_token)
    text_node = libsbml.XMLNode(text_token)
    p_node.addChild(text_node)
    body_node.addChild(p_node)
    i = self.S.setNotes(body_node)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "body" == child.getName() ))
    self.assert_( child.getNumChildren() == 1 )
    child = child.getChild(0)
    self.assert_((  "p" == child.getName() ))
    self.assert_( child.getNumChildren() == 1 )
    child = child.getChild(0)
    self.assert_((  "This is my text" == child.getCharacters() ))
    self.assert_( child.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ body_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_setNotes3(self):
    att = libsbml.XMLAttributes()
    ns = libsbml.XMLNamespaces()
    ns.add( "http://www.w3.org/1999/xhtml", "")
    p_triple = libsbml.XMLTriple("p", "", "")
    p_token = libsbml.XMLToken(p_triple,att,ns)
    text_token = libsbml.XMLToken("This is my text")
    p_node = libsbml.XMLNode(p_token)
    text_node = libsbml.XMLNode(text_token)
    p_node.addChild(text_node)
    i = self.S.setNotes(p_node)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    notes = self.S.getNotes()
    self.assert_((  "notes" == notes.getName() ))
    self.assert_( notes.getNumChildren() == 1 )
    child = notes.getChild(0)
    self.assert_((  "p" == child.getName() ))
    self.assert_( child.getNumChildren() == 1 )
    child = child.getChild(0)
    self.assert_((  "This is my text" == child.getCharacters() ))
    self.assert_( child.getNumChildren() == 0 )
    _dummyList = [ att ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ p_node ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ text_node ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBase_setNotesString(self):
    notes =  "<p xmlns=\"http://www.w3.org/1999/xhtml\">This is a test note </p>";
    taggednotes =  "<notes><p xmlns=\"http://www.w3.org/1999/xhtml\">This is a test note </p></notes>";
    badnotes =  "<notes>This is a test note</notes>";
    i = self.S.setNotes(notes)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    i = self.S.unsetNotes()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( (self.S.isSetNotes() == True) == False )
    i = self.S.setNotes(taggednotes)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.isSetNotes() == True )
    i = self.S.setNotes(None)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( (self.S.isSetNotes() == True) == False )
    i = self.S.setNotes(badnotes)
    self.assert_( i == libsbml.LIBSBML_INVALID_OBJECT )
    self.assert_( (self.S.isSetNotes() == True) == False )
    pass  

  def test_SBase_setSBOTerm1(self):
    c = libsbml.Compartment(1,2)
    i = c.setSBOTerm(2)
    self.assert_( i == libsbml.LIBSBML_UNEXPECTED_ATTRIBUTE )
    self.assertEqual( False, c.isSetSBOTerm() )
    c = None
    pass  

  def test_SBase_setSBOTerm2(self):
    i = self.S.setSBOTerm(5)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.S.isSetSBOTerm() )
    self.assert_( self.S.getSBOTerm() == 5 )
    self.assert_( (  "SBO:0000005" != self.S.getSBOTermID() ) == False )
    i = self.S.unsetSBOTerm()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( False, self.S.isSetSBOTerm() )
    i = self.S.setSBOTerm(0)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.S.isSetSBOTerm() )
    self.assert_( self.S.getSBOTerm() == 0 )
    self.assert_( (  "SBO:0000000" != self.S.getSBOTermID() ) == False )
    i = self.S.setSBOTerm(9999999)
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.S.isSetSBOTerm() )
    self.assert_( self.S.getSBOTerm() == 9999999 )
    self.assert_( (  "SBO:9999999" != self.S.getSBOTermID() ) == False )
    i = self.S.setSBOTerm( "SBO:0000005")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.S.isSetSBOTerm() )
    self.assert_( self.S.getSBOTerm() == 5 )
    self.assert_( (  "SBO:0000005" != self.S.getSBOTermID() ) == False )
    i = self.S.unsetSBOTerm()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( False, self.S.isSetSBOTerm() )
    i = self.S.setSBOTerm( "SBO:0000000")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.S.isSetSBOTerm() )
    self.assert_( self.S.getSBOTerm() == 0 )
    self.assert_( (  "SBO:0000000" != self.S.getSBOTermID() ) == False )
    i = self.S.setSBOTerm( "SBO:9999999")
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assertEqual( True, self.S.isSetSBOTerm() )
    self.assert_( self.S.getSBOTerm() == 9999999 )
    self.assert_( (  "SBO:9999999" != self.S.getSBOTermID() ) == False )
    i = self.S.setSBOTerm(SBML_INT_MAX)
    self.assert_( i == libsbml.LIBSBML_INVALID_ATTRIBUTE_VALUE )
    self.assertEqual( False, self.S.isSetSBOTerm() )
    self.assert_( self.S.getSBOTermID() == "" )
    i = self.S.setSBOTerm(-1)
    self.assert_( i == libsbml.LIBSBML_INVALID_ATTRIBUTE_VALUE )
    self.assertEqual( False, self.S.isSetSBOTerm() )
    self.assert_( self.S.getSBOTermID() == "" )
    i = self.S.setSBOTerm(10000000)
    self.assert_( i == libsbml.LIBSBML_INVALID_ATTRIBUTE_VALUE )
    self.assertEqual( False, self.S.isSetSBOTerm() )
    self.assert_( self.S.getSBOTermID() == "" )
    pass  

  def test_SBase_unsetCVTerms(self):
    cv = libsbml.CVTerm(libsbml.BIOLOGICAL_QUALIFIER)
    cv.setBiologicalQualifierType(libsbml.BQB_ENCODES)
    cv.addResource( "foo")
    self.S.setMetaId( "_id")
    self.S.addCVTerm(cv)
    cv1 = libsbml.CVTerm(libsbml.BIOLOGICAL_QUALIFIER)
    cv1.setBiologicalQualifierType(libsbml.BQB_IS)
    cv1.addResource( "bar")
    self.S.addCVTerm(cv1)
    cv2 = libsbml.CVTerm(libsbml.BIOLOGICAL_QUALIFIER)
    cv2.setBiologicalQualifierType(libsbml.BQB_IS)
    cv2.addResource( "bar1")
    self.S.addCVTerm(cv2)
    cv4 = libsbml.CVTerm(libsbml.BIOLOGICAL_QUALIFIER)
    cv4.setBiologicalQualifierType(libsbml.BQB_IS)
    cv4.addResource( "bar1")
    self.S.addCVTerm(cv4)
    self.assert_( self.S.getNumCVTerms() == 2 )
    i = self.S.unsetCVTerms()
    self.assert_( i == libsbml.LIBSBML_OPERATION_SUCCESS )
    self.assert_( self.S.getNumCVTerms() == 0 )
    self.assert_( self.S.getCVTerms() == None )
    _dummyList = [ cv ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ cv2 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ cv1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ cv4 ]; _dummyList[:] = []; del _dummyList
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestSBase_newSetters))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
