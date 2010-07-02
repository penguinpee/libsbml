#
# @file    TestXMLToken.py
# @brief   XMLToken unit tests
#
# @author  Akiya Jouraku (Python conversion)
# @author  Michael Hucka <mhucka@caltech.edu> 
#
# $Id$
# $HeadURL$
#
# This test file was converted from src/sbml/test/TestXMLToken.c
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


class TestXMLToken(unittest.TestCase):


  def test_XMLToken_attribute_add_remove(self):
    triple = libsbml.XMLTriple("test","","")
    attr = libsbml.XMLAttributes()
    token = libsbml.XMLToken(triple,attr)
    xt1 = libsbml.XMLTriple("name1", "http://name1.org/", "p1")
    xt2 = libsbml.XMLTriple("name2", "http://name2.org/", "p2")
    xt3 = libsbml.XMLTriple("name3", "http://name3.org/", "p3")
    xt1a = libsbml.XMLTriple("name1", "http://name1a.org/", "p1a")
    xt2a = libsbml.XMLTriple("name2", "http://name2a.org/", "p2a")
    token.addAttr( "name1", "val1", "http://name1.org/", "p1")
    token.addAttr(xt2, "val2")
    self.assert_( token.getAttributesLength() == 2 )
    self.assert_( token.isAttributesEmpty() == False )
    self.assert_( (  "name1" != token.getAttrName(0) ) == False )
    self.assert_( (  "val1"  != token.getAttrValue(0) ) == False )
    self.assert_( (  "http://name1.org/" != token.getAttrURI(0) ) == False )
    self.assert_( (  "p1"    != token.getAttrPrefix(0) ) == False )
    self.assert_( (  "name2" != token.getAttrName(1) ) == False )
    self.assert_( (  "val2"  != token.getAttrValue(1) ) == False )
    self.assert_( (  "http://name2.org/" != token.getAttrURI(1) ) == False )
    self.assert_( (  "p2"    != token.getAttrPrefix(1) ) == False )
    self.assert_( token.getAttrValue( "name1") == "" )
    self.assert_( token.getAttrValue( "name2") == "" )
    self.assert_( (  "val1"  != token.getAttrValue( "name1", "http://name1.org/") ) == False )
    self.assert_( (  "val2"  != token.getAttrValue( "name2", "http://name2.org/") ) == False )
    self.assert_( (  "val1"  != token.getAttrValue(xt1) ) == False )
    self.assert_( (  "val2"  != token.getAttrValue(xt2) ) == False )
    self.assert_( token.hasAttr(-1) == False )
    self.assert_( token.hasAttr(2) == False )
    self.assert_( token.hasAttr(0) == True )
    self.assert_( token.hasAttr( "name1", "http://name1.org/") == True )
    self.assert_( token.hasAttr( "name2", "http://name2.org/") == True )
    self.assert_( token.hasAttr( "name3", "http://name3.org/") == False )
    self.assert_( token.hasAttr(xt1) == True )
    self.assert_( token.hasAttr(xt2) == True )
    self.assert_( token.hasAttr(xt3) == False )
    token.addAttr( "noprefix", "val3")
    self.assert_( token.getAttributesLength() == 3 )
    self.assert_( token.isAttributesEmpty() == False )
    self.assert_( (  "noprefix" != token.getAttrName(2) ) == False )
    self.assert_( (  "val3"     != token.getAttrValue(2) ) == False )
    self.assert_( token.getAttrURI(2) == "" )
    self.assert_( token.getAttrPrefix(2) == "" )
    self.assert_( (      "val3"  != token.getAttrValue( "noprefix") ) == False )
    self.assert_( (  "val3"  != token.getAttrValue( "noprefix", "") ) == False )
    self.assert_( token.hasAttr( "noprefix"    ) == True )
    self.assert_( token.hasAttr( "noprefix", "") == True )
    token.addAttr(xt1, "mval1")
    token.addAttr( "name2", "mval2", "http://name2.org/", "p2")
    self.assert_( token.getAttributesLength() == 3 )
    self.assert_( token.isAttributesEmpty() == False )
    self.assert_( (  "name1" != token.getAttrName(0) ) == False )
    self.assert_( (  "mval1" != token.getAttrValue(0) ) == False )
    self.assert_( (  "http://name1.org/" != token.getAttrURI(0) ) == False )
    self.assert_( (  "p1"    != token.getAttrPrefix(0) ) == False )
    self.assert_( (  "name2"    != token.getAttrName(1) ) == False )
    self.assert_( (  "mval2"    != token.getAttrValue(1) ) == False )
    self.assert_( (  "http://name2.org/" != token.getAttrURI(1) ) == False )
    self.assert_( (  "p2"       != token.getAttrPrefix(1) ) == False )
    self.assert_( token.hasAttr(xt1) == True )
    self.assert_( token.hasAttr( "name1", "http://name1.org/") == True )
    token.addAttr( "noprefix", "mval3")
    self.assert_( token.getAttributesLength() == 3 )
    self.assert_( token.isAttributesEmpty() == False )
    self.assert_( (  "noprefix" != token.getAttrName(2) ) == False )
    self.assert_( (  "mval3"    != token.getAttrValue(2) ) == False )
    self.assert_( token.getAttrURI(2) == "" )
    self.assert_( token.getAttrPrefix(2) == "" )
    self.assert_( token.hasAttr( "noprefix") == True )
    self.assert_( token.hasAttr( "noprefix", "") == True )
    token.addAttr(xt1a, "val1a")
    token.addAttr(xt2a, "val2a")
    self.assert_( token.getAttributesLength() == 5 )
    self.assert_( (  "name1" != token.getAttrName(3) ) == False )
    self.assert_( (  "val1a" != token.getAttrValue(3) ) == False )
    self.assert_( (  "http://name1a.org/" != token.getAttrURI(3) ) == False )
    self.assert_( (  "p1a" != token.getAttrPrefix(3) ) == False )
    self.assert_( (  "name2" != token.getAttrName(4) ) == False )
    self.assert_( (  "val2a" != token.getAttrValue(4) ) == False )
    self.assert_( (  "http://name2a.org/" != token.getAttrURI(4) ) == False )
    self.assert_( (  "p2a" != token.getAttrPrefix(4) ) == False )
    self.assert_( (  "val1a"  != token.getAttrValue( "name1", "http://name1a.org/") ) == False )
    self.assert_( (  "val2a"  != token.getAttrValue( "name2", "http://name2a.org/") ) == False )
    self.assert_( (  "val1a"  != token.getAttrValue(xt1a) ) == False )
    self.assert_( (  "val2a"  != token.getAttrValue(xt2a) ) == False )
    token.removeAttr(xt1a)
    token.removeAttr(xt2a)
    self.assert_( token.getAttributesLength() == 3 )
    token.removeAttr( "name1", "http://name1.org/")
    self.assert_( token.getAttributesLength() == 2 )
    self.assert_( token.isAttributesEmpty() == False )
    self.assert_( (  "name2" != token.getAttrName(0) ) == False )
    self.assert_( (  "mval2" != token.getAttrValue(0) ) == False )
    self.assert_( (  "http://name2.org/" != token.getAttrURI(0) ) == False )
    self.assert_( (  "p2" != token.getAttrPrefix(0) ) == False )
    self.assert_( (  "noprefix" != token.getAttrName(1) ) == False )
    self.assert_( (  "mval3" != token.getAttrValue(1) ) == False )
    self.assert_( token.getAttrURI(1) == "" )
    self.assert_( token.getAttrPrefix(1) == "" )
    self.assert_( token.hasAttr( "name1", "http://name1.org/") == False )
    token.removeAttr(xt2)
    self.assert_( token.getAttributesLength() == 1 )
    self.assert_( token.isAttributesEmpty() == False )
    self.assert_( (  "noprefix" != token.getAttrName(0) ) == False )
    self.assert_( (  "mval3" != token.getAttrValue(0) ) == False )
    self.assert_( token.getAttrURI(0) == "" )
    self.assert_( token.getAttrPrefix(0) == "" )
    self.assert_( token.hasAttr(xt2) == False )
    self.assert_( token.hasAttr( "name2", "http://name2.org/") == False )
    token.removeAttr( "noprefix")
    self.assert_( token.getAttributesLength() == 0 )
    self.assert_( token.isAttributesEmpty() == True )
    self.assert_( token.hasAttr( "noprefix"    ) == False )
    self.assert_( token.hasAttr( "noprefix", "") == False )
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ xt1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ xt2 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ xt3 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ xt1a ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ xt2a ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ attr ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_XMLToken_attribute_set_clear(self):
    triple = libsbml.XMLTriple("test","","")
    attr = libsbml.XMLAttributes()
    token = libsbml.XMLToken(triple,attr)
    nattr = libsbml.XMLAttributes()
    xt1 = libsbml.XMLTriple("name1", "http://name1.org/", "p1")
    xt2 = libsbml.XMLTriple("name2", "http://name2.org/", "p2")
    xt3 = libsbml.XMLTriple("name3", "http://name3.org/", "p3")
    xt4 = libsbml.XMLTriple("name4", "http://name4.org/", "p4")
    xt5 = libsbml.XMLTriple("name5", "http://name5.org/", "p5")
    nattr.add(xt1, "val1")
    nattr.add(xt2, "val2")
    nattr.add(xt3, "val3")
    nattr.add(xt4, "val4")
    nattr.add(xt5, "val5")
    token.setAttributes(nattr)
    self.assert_( token.getAttributesLength() == 5 )
    self.assert_( token.isAttributesEmpty() == False )
    self.assert_( (  "name1" != token.getAttrName(0) ) == False )
    self.assert_( (  "val1"  != token.getAttrValue(0) ) == False )
    self.assert_( (  "http://name1.org/" != token.getAttrURI(0) ) == False )
    self.assert_( (  "p1"    != token.getAttrPrefix(0) ) == False )
    self.assert_( (  "name2" != token.getAttrName(1) ) == False )
    self.assert_( (  "val2"  != token.getAttrValue(1) ) == False )
    self.assert_( (  "http://name2.org/" != token.getAttrURI(1) ) == False )
    self.assert_( (  "p2"    != token.getAttrPrefix(1) ) == False )
    self.assert_( (  "name3" != token.getAttrName(2) ) == False )
    self.assert_( (  "val3"  != token.getAttrValue(2) ) == False )
    self.assert_( (  "http://name3.org/" != token.getAttrURI(2) ) == False )
    self.assert_( (  "p3"    != token.getAttrPrefix(2) ) == False )
    self.assert_( (  "name4" != token.getAttrName(3) ) == False )
    self.assert_( (  "val4"  != token.getAttrValue(3) ) == False )
    self.assert_( (  "http://name4.org/" != token.getAttrURI(3) ) == False )
    self.assert_( (  "p4"    != token.getAttrPrefix(3) ) == False )
    self.assert_( (  "name5" != token.getAttrName(4) ) == False )
    self.assert_( (  "val5"  != token.getAttrValue(4) ) == False )
    self.assert_( (  "http://name5.org/" != token.getAttrURI(4) ) == False )
    self.assert_( (  "p5"    != token.getAttrPrefix(4) ) == False )
    ntriple = libsbml.XMLTriple("test2","http://test2.org/","p2")
    token.setTriple(ntriple)
    self.assert_( (    "test2" != token.getName() ) == False )
    self.assert_( (     "http://test2.org/" != token.getURI() ) == False )
    self.assert_( (  "p2" != token.getPrefix() ) == False )
    token.clearAttributes()
    self.assert_( token.getAttributesLength() == 0 )
    self.assert_( token.isAttributesEmpty() != False )
    _dummyList = [ nattr ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ ntriple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ attr ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ xt1 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ xt2 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ xt3 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ xt4 ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ xt5 ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_XMLToken_chars(self):
    token = libsbml.XMLToken("This is text")
    self.assert_( token.isElement() == False )
    self.assert_( token.isEnd() == False )
    self.assert_( token.isStart() == False )
    self.assert_( token.isText() == True )
    self.assert_( token.isEOF() == False )
    self.assert_( (  "This is text" != token.getCharacters() ) == False )
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_XMLToken_create(self):
    token = libsbml.XMLToken()
    self.assert_( token != None )
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    triple = libsbml.XMLTriple("attr", "uri", "prefix")
    token = libsbml.XMLToken(triple)
    self.assert_( token != None )
    self.assert_( (  "attr" != token.getName() ) == False )
    self.assert_( (  "prefix" != token.getPrefix() ) == False )
    self.assert_( (  "uri" != token.getURI() ) == False )
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    attr = libsbml.XMLAttributes()
    self.assert_( attr != None )
    attr.add( "attr2", "value")
    token = libsbml.XMLToken(triple,attr)
    self.assert_( token != None )
    returnattr = token.getAttributes()
    self.assert_( (  "attr2" != returnattr.getName(0) ) == False )
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ attr ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_XMLToken_fields(self):
    triple = libsbml.XMLTriple("attr", "uri", "prefix")
    token = libsbml.XMLToken(triple)
    self.assert_( token.isElement() == True )
    self.assert_( token.isEnd() == True )
    self.assert_( token.isStart() == False )
    self.assert_( token.isText() == False )
    self.assert_( token.isEOF() == False )
    self.assert_( (  "attr" != token.getName() ) == False )
    self.assert_( (  "uri" != token.getURI() ) == False )
    self.assert_( (  "prefix" != token.getPrefix() ) == False )
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ triple ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_XMLToken_namespace_add(self):
    triple = libsbml.XMLTriple("test","","")
    attr = libsbml.XMLAttributes()
    token = libsbml.XMLToken(triple,attr)
    self.assert_( token.getNamespacesLength() == 0 )
    self.assert_( token.isNamespacesEmpty() == True )
    token.addNamespace( "http://test1.org/", "test1")
    self.assert_( token.getNamespacesLength() == 1 )
    self.assert_( token.isNamespacesEmpty() == False )
    token.addNamespace( "http://test2.org/", "test2")
    self.assert_( token.getNamespacesLength() == 2 )
    self.assert_( token.isNamespacesEmpty() == False )
    token.addNamespace( "http://test1.org/", "test1a")
    self.assert_( token.getNamespacesLength() == 3 )
    self.assert_( token.isNamespacesEmpty() == False )
    token.addNamespace( "http://test1.org/", "test1a")
    self.assert_( token.getNamespacesLength() == 3 )
    self.assert_( token.isNamespacesEmpty() == False )
    self.assert_( (token.getNamespaceIndex( "http://test1.org/") == -1) == False )
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ attr ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_XMLToken_namespace_get(self):
    triple = libsbml.XMLTriple("test","","")
    attr = libsbml.XMLAttributes()
    token = libsbml.XMLToken(triple,attr)
    token.addNamespace( "http://test1.org/", "test1")
    token.addNamespace( "http://test2.org/", "test2")
    token.addNamespace( "http://test3.org/", "test3")
    token.addNamespace( "http://test4.org/", "test4")
    token.addNamespace( "http://test5.org/", "test5")
    token.addNamespace( "http://test6.org/", "test6")
    token.addNamespace( "http://test7.org/", "test7")
    token.addNamespace( "http://test8.org/", "test8")
    token.addNamespace( "http://test9.org/", "test9")
    self.assert_( token.getNamespacesLength() == 9 )
    self.assert_( token.getNamespaceIndex( "http://test1.org/") == 0 )
    self.assert_( (  "test2" != token.getNamespacePrefix(1) ) == False )
    self.assert_( ( 		      "test1" != token.getNamespacePrefix( "http://test1.org/") ) == False )
    self.assert_( (  "http://test2.org/" != token.getNamespaceURI(1) ) == False )
    self.assert_( ( 		      "http://test2.org/" != token.getNamespaceURI( "test2") ) == False )
    self.assert_( token.getNamespaceIndex( "http://test1.org/") == 0 )
    self.assert_( token.getNamespaceIndex( "http://test2.org/") == 1 )
    self.assert_( token.getNamespaceIndex( "http://test5.org/") == 4 )
    self.assert_( token.getNamespaceIndex( "http://test9.org/") == 8 )
    self.assert_( token.getNamespaceIndex( "http://testX.org/") == -1 )
    self.assert_( token.hasNamespaceURI( "http://test1.org/") != False )
    self.assert_( token.hasNamespaceURI( "http://test2.org/") != False )
    self.assert_( token.hasNamespaceURI( "http://test5.org/") != False )
    self.assert_( token.hasNamespaceURI( "http://test9.org/") != False )
    self.assert_( token.hasNamespaceURI( "http://testX.org/") == False )
    self.assert_( token.getNamespaceIndexByPrefix( "test1") == 0 )
    self.assert_( token.getNamespaceIndexByPrefix( "test5") == 4 )
    self.assert_( token.getNamespaceIndexByPrefix( "test9") == 8 )
    self.assert_( token.getNamespaceIndexByPrefix( "testX") == -1 )
    self.assert_( token.hasNamespacePrefix( "test1") != False )
    self.assert_( token.hasNamespacePrefix( "test5") != False )
    self.assert_( token.hasNamespacePrefix( "test9") != False )
    self.assert_( token.hasNamespacePrefix( "testX") == False )
    self.assert_( token.hasNamespaceNS( "http://test1.org/", "test1") != False )
    self.assert_( token.hasNamespaceNS( "http://test5.org/", "test5") != False )
    self.assert_( token.hasNamespaceNS( "http://test9.org/", "test9") != False )
    self.assert_( token.hasNamespaceNS( "http://testX.org/", "testX") == False )
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ attr ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_XMLToken_namespace_remove(self):
    triple = libsbml.XMLTriple("test","","")
    attr = libsbml.XMLAttributes()
    token = libsbml.XMLToken(triple,attr)
    token.addNamespace( "http://test1.org/", "test1")
    token.addNamespace( "http://test2.org/", "test2")
    token.addNamespace( "http://test3.org/", "test3")
    token.addNamespace( "http://test4.org/", "test4")
    token.addNamespace( "http://test5.org/", "test5")
    self.assert_( token.getNamespacesLength() == 5 )
    token.removeNamespace(4)
    self.assert_( token.getNamespacesLength() == 4 )
    token.removeNamespace(3)
    self.assert_( token.getNamespacesLength() == 3 )
    token.removeNamespace(2)
    self.assert_( token.getNamespacesLength() == 2 )
    token.removeNamespace(1)
    self.assert_( token.getNamespacesLength() == 1 )
    token.removeNamespace(0)
    self.assert_( token.getNamespacesLength() == 0 )
    token.addNamespace( "http://test1.org/", "test1")
    token.addNamespace( "http://test2.org/", "test2")
    token.addNamespace( "http://test3.org/", "test3")
    token.addNamespace( "http://test4.org/", "test4")
    token.addNamespace( "http://test5.org/", "test5")
    self.assert_( token.getNamespacesLength() == 5 )
    token.removeNamespace(0)
    self.assert_( token.getNamespacesLength() == 4 )
    token.removeNamespace(0)
    self.assert_( token.getNamespacesLength() == 3 )
    token.removeNamespace(0)
    self.assert_( token.getNamespacesLength() == 2 )
    token.removeNamespace(0)
    self.assert_( token.getNamespacesLength() == 1 )
    token.removeNamespace(0)
    self.assert_( token.getNamespacesLength() == 0 )
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ attr ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_XMLToken_namespace_remove_by_prefix(self):
    triple = libsbml.XMLTriple("test","","")
    attr = libsbml.XMLAttributes()
    token = libsbml.XMLToken(triple,attr)
    token.addNamespace( "http://test1.org/", "test1")
    token.addNamespace( "http://test2.org/", "test2")
    token.addNamespace( "http://test3.org/", "test3")
    token.addNamespace( "http://test4.org/", "test4")
    token.addNamespace( "http://test5.org/", "test5")
    self.assert_( token.getNamespacesLength() == 5 )
    token.removeNamespace( "test1")
    self.assert_( token.getNamespacesLength() == 4 )
    token.removeNamespace( "test2")
    self.assert_( token.getNamespacesLength() == 3 )
    token.removeNamespace( "test3")
    self.assert_( token.getNamespacesLength() == 2 )
    token.removeNamespace( "test4")
    self.assert_( token.getNamespacesLength() == 1 )
    token.removeNamespace( "test5")
    self.assert_( token.getNamespacesLength() == 0 )
    token.addNamespace( "http://test1.org/", "test1")
    token.addNamespace( "http://test2.org/", "test2")
    token.addNamespace( "http://test3.org/", "test3")
    token.addNamespace( "http://test4.org/", "test4")
    token.addNamespace( "http://test5.org/", "test5")
    self.assert_( token.getNamespacesLength() == 5 )
    token.removeNamespace( "test5")
    self.assert_( token.getNamespacesLength() == 4 )
    token.removeNamespace( "test4")
    self.assert_( token.getNamespacesLength() == 3 )
    token.removeNamespace( "test3")
    self.assert_( token.getNamespacesLength() == 2 )
    token.removeNamespace( "test2")
    self.assert_( token.getNamespacesLength() == 1 )
    token.removeNamespace( "test1")
    self.assert_( token.getNamespacesLength() == 0 )
    token.addNamespace( "http://test1.org/", "test1")
    token.addNamespace( "http://test2.org/", "test2")
    token.addNamespace( "http://test3.org/", "test3")
    token.addNamespace( "http://test4.org/", "test4")
    token.addNamespace( "http://test5.org/", "test5")
    self.assert_( token.getNamespacesLength() == 5 )
    token.removeNamespace( "test3")
    self.assert_( token.getNamespacesLength() == 4 )
    token.removeNamespace( "test1")
    self.assert_( token.getNamespacesLength() == 3 )
    token.removeNamespace( "test4")
    self.assert_( token.getNamespacesLength() == 2 )
    token.removeNamespace( "test5")
    self.assert_( token.getNamespacesLength() == 1 )
    token.removeNamespace( "test2")
    self.assert_( token.getNamespacesLength() == 0 )
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ attr ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_XMLToken_namespace_set_clear(self):
    triple = libsbml.XMLTriple("test","","")
    attr = libsbml.XMLAttributes()
    token = libsbml.XMLToken(triple,attr)
    ns = libsbml.XMLNamespaces()
    self.assert_( token.getNamespacesLength() == 0 )
    self.assert_( token.isNamespacesEmpty() == True )
    ns.add( "http://test1.org/", "test1")
    ns.add( "http://test2.org/", "test2")
    ns.add( "http://test3.org/", "test3")
    ns.add( "http://test4.org/", "test4")
    ns.add( "http://test5.org/", "test5")
    token.setNamespaces(ns)
    self.assert_( token.getNamespacesLength() == 5 )
    self.assert_( token.isNamespacesEmpty() == False )
    self.assert_( (  "test1" != token.getNamespacePrefix(0) ) == False )
    self.assert_( (  "test2" != token.getNamespacePrefix(1) ) == False )
    self.assert_( (  "test3" != token.getNamespacePrefix(2) ) == False )
    self.assert_( (  "test4" != token.getNamespacePrefix(3) ) == False )
    self.assert_( (  "test5" != token.getNamespacePrefix(4) ) == False )
    self.assert_( (  "http://test1.org/" != token.getNamespaceURI(0) ) == False )
    self.assert_( (  "http://test2.org/" != token.getNamespaceURI(1) ) == False )
    self.assert_( (  "http://test3.org/" != token.getNamespaceURI(2) ) == False )
    self.assert_( (  "http://test4.org/" != token.getNamespaceURI(3) ) == False )
    self.assert_( (  "http://test5.org/" != token.getNamespaceURI(4) ) == False )
    token.clearNamespaces()
    self.assert_( token.getNamespacesLength() == 0 )
    _dummyList = [ ns ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ token ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ triple ]; _dummyList[:] = []; del _dummyList
    _dummyList = [ attr ]; _dummyList[:] = []; del _dummyList
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestXMLToken))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)
