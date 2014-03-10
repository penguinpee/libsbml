/**
 * @file:   FunctionTerm.h
 * @brief:  Implementation of the FunctionTerm class
 * @author: Generated by autocreate code
 *
 * <!--------------------------------------------------------------------------
 * This file is part of libSBML.  Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 *
 * Copyright (C) 2009-2013 jointly by the following organizations:
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. EMBL European Bioinformatics Institute (EBML-EBI), Hinxton, UK
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
 * ------------------------------------------------------------------------ -->
 *
 * @class FunctionTerm
 * @sbmlbrief{qual} The FunctionTerm class for the Qualitative Models
 * package.
 *
 * Each FunctionTerm is associated with a result and with a Boolean function
 * inside a Math element that can be used to set the conditions under which
 * this term is selected.
 */


#ifndef FunctionTerm_H__
#define FunctionTerm_H__


#include <sbml/common/extern.h>
#include <sbml/common/sbmlfwd.h>
#include <sbml/packages/qual/common/qualfwd.h>


#ifdef __cplusplus


#include <string>


#include <sbml/SBase.h>
#include <sbml/ListOf.h>
#include <sbml/packages/qual/extension/QualExtension.h>
#include <sbml/packages/qual/sbml/DefaultTerm.h>


LIBSBML_CPP_NAMESPACE_BEGIN


class LIBSBML_EXTERN FunctionTerm : public SBase
{

protected:

  int           mResultLevel;
  bool          mIsSetResultLevel;
  ASTNode*      mMath;


public:

  /**
   * Creates a new FunctionTerm with the given level, version, and package version.
   *
   * @param level an unsigned int, the SBML Level to assign to this FunctionTerm
   *
   * @param version an unsigned int, the SBML Version to assign to this FunctionTerm
   *
   * @param pkgVersion an unsigned int, the SBML Qual Version to assign to this FunctionTerm
   */
  FunctionTerm(unsigned int level      = QualExtension::getDefaultLevel(),
               unsigned int version    = QualExtension::getDefaultVersion(),
               unsigned int pkgVersion = QualExtension::getDefaultPackageVersion());


  /**
   * Creates a new FunctionTerm with the given QualPkgNamespaces object.
   *
   * @param qualns the QualPkgNamespaces object
   */
  FunctionTerm(QualPkgNamespaces* qualns);


  /**
   * Copy constructor for FunctionTerm.
   *
   * @param orig the FunctionTerm instance to copy.
   */
  FunctionTerm(const FunctionTerm& orig);


  /**
   * Assignment operator for FunctionTerm.
   *
   * @param rhs the object whose values are used as the basis
   * of the assignment
   */
  FunctionTerm& operator=(const FunctionTerm& rhs);


  /**
   * Creates and returns a deep copy of this FunctionTerm object.
   *
   * @return a (deep) copy of this FunctionTerm object.
   */
  virtual FunctionTerm* clone () const;


  /**
   * Destructor for FunctionTerm.
   */
  virtual ~FunctionTerm();


  /**
   * Returns the value of the "resultLevel" attribute of this FunctionTerm.
   *
   * @return the value of the "resultLevel" attribute of this FunctionTerm as a integer.
   */
  virtual const int getResultLevel() const;


  /**
   * Predicate returning @c true or @c false depending on whether this
   * FunctionTerm's "resultLevel" attribute has been set.
   *
   * @return @c true if this FunctionTerm's "resultLevel" attribute has been set,
   * otherwise @c false is returned.
   */
  virtual bool isSetResultLevel() const;


  /**
   * Sets the value of the "resultLevel" attribute of this FunctionTerm.
   *
   * @param resultLevel int value of the "resultLevel" attribute to be set
   *
   * @return integer value indicating success/failure of the
   * operation. The possible return values are:
   * @li @link OperationReturnValues_t#LIBSBML_OPERATION_SUCCESS LIBSBML_OPERATION_SUCCESS @endlink
   * @li @link OperationReturnValues_t#LIBSBML_INVALID_ATTRIBUTE_VALUE LIBSBML_INVALID_ATTRIBUTE_VALUE @endlink
   */
  virtual int setResultLevel(int resultLevel);


  /**
   * Unsets the value of the "resultLevel" attribute of this FunctionTerm.
   *
   * @return integer value indicating success/failure of the
   * operation. The possible return values are:
   * @li @link OperationReturnValues_t#LIBSBML_OPERATION_SUCCESS LIBSBML_OPERATION_SUCCESS @endlink
   * @li @link OperationReturnValues_t#LIBSBML_OPERATION_FAILED LIBSBML_OPERATION_FAILED @endlink
   */
  virtual int unsetResultLevel();


  /**
   * Returns the "math" element of this FunctionTerm.
   *
   * @return the "math" element of this FunctionTerm.
   */
  virtual const ASTNode* getMath() const;


  /**
   * Predicate returning @c true or @c false depending on whether this
   * FunctionTerm's "math" element has been set.
   *
   * @return @c true if this FunctionTerm's "math" element has been set,
   * otherwise @c false is returned.
   */
  virtual bool isSetMath() const;


  /**
   * Sets the "math" element of this FunctionTerm.
   *
   * @param math ASTNode * math of the "resultLevel" attribute to be set
   *
   * @return integer value indicating success/failure of the
   * operation. The possible return values are:
   * @li @link OperationReturnValues_t#LIBSBML_OPERATION_SUCCESS LIBSBML_OPERATION_SUCCESS @endlink
   * @li @link OperationReturnValues_t#LIBSBML_INVALID_ATTRIBUTE_VALUE LIBSBML_INVALID_ATTRIBUTE_VALUE @endlink
   */
  virtual int setMath(ASTNode* math);


  /**
   * Unsets the "math" element of this FunctionTerm.
   *
   * @return integer value indicating success/failure of the
   * operation. The possible return values are:
   * @li @link OperationReturnValues_t#LIBSBML_OPERATION_SUCCESS LIBSBML_OPERATION_SUCCESS @endlink
   * @li @link OperationReturnValues_t#LIBSBML_OPERATION_FAILED LIBSBML_OPERATION_FAILED @endlink
   */
  virtual int unsetMath();


  /**
   * Renames all the @c SIdRef attributes on this element, including any
   * found in MathML content (if such exists).
   *
   * This method works by looking at all attributes and (if appropriate)
   * mathematical formulas, comparing the identifiers to the value of @p
   * oldid.  If any matches are found, the matching identifiers are replaced
   * with @p newid.  The method does @em not descend into child elements.
   *
   * @param oldid the old identifier
   * @param newid the new identifier
   */
   virtual void renameSIdRefs(const std::string& oldid, const std::string& newid);


  /**
   * Returns the XML element name of this object, which for FunctionTerm, is
   * always @c "functionTerm".
   *
   * @return the name of this element, i.e. @c "functionTerm".
   */
  virtual const std::string& getElementName () const;


  /**
   * Returns the libSBML type code of this object instance.
   *
   * @copydetails doc_what_are_typecodes
   *
   * @return the SBML type code for this object:
   * @link SBMLQualTypeCode_t#SBML_QUAL_FUNCTION_TERM SBML_QUAL_FUNCTION_TERM@endlink
   *
   * @copydetails doc_warning_typecodes_not_unique
   *
   * @see getElementName()
   * @see getPackageName()
   */
  virtual int getTypeCode () const;


  /**
   * Predicate returning @c true if all the required attributes
   * for this FunctionTerm object have been set.
   *
   * @note The required attributes for a FunctionTerm object are:
   *
   * @return a boolean value indicating whether all the required
   * attributes for this object have been defined.
   */
  virtual bool hasRequiredAttributes() const;


  /**
   * Predicate returning @c true if all the required elements
   * for this FunctionTerm object have been set.
   *
   * @note The required elements for a FunctionTerm object are:
   * @li "math"
   *
   * @return a boolean value indicating whether all the required
   * elements for this object have been defined.
   */
  virtual bool hasRequiredElements() const;


  /** @cond doxygenLibsbmlInternal */

  /**
   * Subclasses should override this method to write out their contained
   * SBML objects as XML elements.  Be sure to call your parents
   * implementation of this method as well.
   */
  virtual void writeElements (XMLOutputStream& stream) const;


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

  /**
   * Accepts the given SBMLVisitor.
   */
  virtual bool accept (SBMLVisitor& v) const;


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

  /**
   * Sets the parent SBMLDocument.
   */
  virtual void setSBMLDocument (SBMLDocument* d);


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

  /**
   * Enables/Disables the given package with this element.
   */
  virtual void enablePackageInternal(const std::string& pkgURI,
               const std::string& pkgPrefix, bool flag);


  /** @endcond */


protected:

  /** @cond doxygenLibsbmlInternal */

  /**
   * Get the list of expected attributes for this element.
   */
  virtual void addExpectedAttributes(ExpectedAttributes& attributes);


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

  /**
   * Read values from the given XMLAttributes set into their specific fields.
   */
  virtual void readAttributes (const XMLAttributes& attributes,
                               const ExpectedAttributes& expectedAttributes);


  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

  /**
   * Subclasses should override this method to read (and store) XHTML,
   * MathML, etc. directly from the XMLInputStream.
   *
   * @return true if the subclass read from the stream, false otherwise.
   */
  virtual bool readOtherXML (XMLInputStream& stream);

  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

  /**
   * Write values of XMLAttributes to the output stream.
   */
  virtual void writeAttributes (XMLOutputStream& stream) const;


  /** @endcond */



};

/**
 *
 * @class ListOfFunctionTerms
 * @sbmlbrief{qual} Implementation of the %ListOfFunctionTerms construct from
 * the 'qual' package.
 * 
 * The ListOfFunctionTerms is a container for the FunctionTerms of a Transition.
 * 
 * @copydetails doc_what_is_listof
 *
 * @see Input
 */
class LIBSBML_EXTERN ListOfFunctionTerms : public ListOf
{

public:

  /**
   * Creates a new ListOfFunctionTerms with the given level, version, and package version.
   *
   * @param level an unsigned int, the SBML Level to assign to this ListOfFunctionTerms
   *
   * @param version an unsigned int, the SBML Version to assign to this ListOfFunctionTerms
   *
   * @param pkgVersion an unsigned int, the SBML Qual Version to assign to this ListOfFunctionTerms
   */
  ListOfFunctionTerms(unsigned int level      = QualExtension::getDefaultLevel(),
                      unsigned int version    = QualExtension::getDefaultVersion(),
                      unsigned int pkgVersion = QualExtension::getDefaultPackageVersion());


  /**
   * Creates a new ListOfFunctionTerms with the given QualPkgNamespaces object.
   *
   * @param qualns the QualPkgNamespaces object
   */
  ListOfFunctionTerms(QualPkgNamespaces* qualns);


  ListOfFunctionTerms(const ListOfFunctionTerms& orig);

  
  ListOfFunctionTerms& operator=(const ListOfFunctionTerms& rhs);
  
  
  /**
   * Creates and returns a deep copy of this ListOfFunctionTerms object.
   *
   * @return a (deep) copy of this ListOfFunctionTerms object.
   */
  virtual ListOfFunctionTerms* clone () const;


  /**
   * Destroys this ListOfFunctionTerms object.
   */
  virtual ~ListOfFunctionTerms();

  /**
   * Get a FunctionTerm from the ListOfFunctionTerms.
   *
   * @param n the index number of the FunctionTerm to get.
   *
   * @return the nth FunctionTerm in this ListOfFunctionTerms.
   *
   * @see size()
   */
  virtual FunctionTerm* get(unsigned int n);


  /**
   * Get a FunctionTerm from the ListOfFunctionTerms.
   *
   * @param n the index number of the FunctionTerm to get.
   *
   * @return the nth FunctionTerm in this ListOfFunctionTerms.
   *
   * @see size()
   */
  virtual const FunctionTerm* get(unsigned int n) const;


  /**
   * Get a FunctionTerm from the ListOfFunctionTerms
   * based on its identifier.
   *
   * @param sid a string representing the identifier
   * of the FunctionTerm to get.
   *
   * @return FunctionTerm in this ListOfFunctionTerms
   * with the given id or NULL if no such
   * FunctionTerm exists.
   *
   * @see get(unsigned int n)   *
   * @see size()
   */
  virtual FunctionTerm* get(const std::string& sid);


  /**
   * Get a FunctionTerm from the ListOfFunctionTerms
   * based on its identifier.
   *
   * @param sid a string representing the identifier
   * of the FunctionTerm to get.
   *
   * @return FunctionTerm in this ListOfFunctionTerms
   * with the given id or NULL if no such
   * FunctionTerm exists.
   *
   * @see get(unsigned int n)   *
   * @see size()
   */
  virtual const FunctionTerm* get(const std::string& sid) const;


  /**
   * Removes the nth FunctionTerm from this ListOfFunctionTerms
   * and returns a pointer to it.
   *
   * The caller owns the returned item and is responsible for deleting it.
   *
   * @param n the index of the FunctionTerm to remove.
   *
   * @see size()
   */
  virtual FunctionTerm* remove(unsigned int n);


  /**
   * Removes the FunctionTerm from this ListOfFunctionTerms with the given identifier
   * and returns a pointer to it.
   *
   * The caller owns the returned item and is responsible for deleting it.
   * If none of the items in this list have the identifier @p sid, then
   * @c NULL is returned.
   *
   * @param sid the identifier of the FunctionTerm to remove.
   *
   * @return the FunctionTerm removed. As mentioned above, the caller owns the
   * returned item.
   */
  virtual FunctionTerm* remove(const std::string& sid);


  /**
   * Returns a List of all child SBase objects, including those nested to an
   * arbitary depth.
   *
   * @return a List* of pointers to all child objects.
   */
   virtual List* getAllElements(ElementFilter * filter = NULL);


  /**
   * Returns the XML element name of this object, which for ListOfFunctionTerms, is
   * always @c "listOfFunctionTerms".
   *
   * @return the name of this element, i.e. @c "listOfFunctionTerms".
   */
  virtual const std::string& getElementName () const;


  /**
   * Returns the libSBML type code for the SBML objects
   * contained in this ListOf object.
   * 
   * @copydetails doc_what_are_typecodes
   *
   * @return the SBML type code for objects contained in this list:
   * @link SBMLTypeCode_t#SBML_QUAL_FUNCTION_TERM SBML_QUAL_FUNCTION_TERM@endlink (default).
   *
   * @see getElementName()
   * @see getPackageName()
   */
  virtual int getItemTypeCode () const;

  /**
   * Get the DefaultTerm from this ListOfFunctionTerms.
   *
   * @return the DefaultTerm in this ListOfFunctionTerms, or NULL if no such value is set.
   *
   * @see Transition::getDefaultTerm
   */
  DefaultTerm * getDefaultTerm();

  /**
   * Get the DefaultTerm from this ListOfFunctionTerms.
   *
   * @return the DefaultTerm in this ListOfFunctionTerms, or NULL if no such value is set.
   *
   * @see Transition::getDefaultTerm
   */
  const DefaultTerm * getDefaultTerm() const;

  /**
   * Sets the given DefaultTerm to this Transition.
   *
   * @param dt the DefaultTerm object to add
   *
   * @return integer value indicating success/failure of the
   * operation. The possible return values are:
   * @li @link OperationReturnValues_t#LIBSBML_OPERATION_SUCCESS LIBSBML_OPERATION_SUCCESS @endlink
   * @li @link OperationReturnValues_t#LIBSBML_INVALID_ATTRIBUTE_VALUE LIBSBML_INVALID_ATTRIBUTE_VALUE @endlink
   */
  int setDefaultTerm(const DefaultTerm* dt);

  /**
   * Predicate returning @c true if the defaultTerm 
   * for this ListOfFunctionTerms object has been set.
   *
   * @return a boolean value indicating whether the defaultTerm
   * child for this object has been defined.
   */
  bool isSetDefaultTerm() const;

  /** @cond doxygenLibsbmlInternal */

  /**
   * Connects to child elements.
   */
  virtual void setSBMLDocument (SBMLDocument* d);


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

  /**
   * Connects to child elements.
   */
  virtual bool accept (SBMLVisitor& v) const;


  /** @endcond */


protected:

  /** @cond doxygenLibsbmlInternal */

  /**
   * Creates a new FunctionTerm in this ListOfFunctionTerms
   */
  virtual SBase* createObject(XMLInputStream& stream);


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

  /**
   * Write the namespace for the Qual package.
   */
  virtual void writeXMLNS(XMLOutputStream& stream) const;


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

  /**
   * Write the namespace for the Qual package.
   */
  virtual void writeElements(XMLOutputStream& stream) const;


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

  /**
   * Connects to child elements.
   */
  virtual void connectToChild ();


  /** @endcond */


  DefaultTerm * mDefaultTerm;

};



LIBSBML_CPP_NAMESPACE_END

#endif  /*  __cplusplus  */

#ifndef SWIG

LIBSBML_CPP_NAMESPACE_BEGIN
BEGIN_C_DECLS

/**
 * Creates a new FunctionTerm_t structure using the given SBML @p level
 * and @p version values.
 *
 * @param level an unsigned int, the SBML Level to assign to this
 * FunctionTerm_t
 * @param version an unsigned int, the SBML Version to assign to this
 * FunctionTerm_t
 * @param pkgVersion an unsigned int, the SBML 'Qual' package Version to assign to this
 * FunctionTerm_t
 *
 * @return a pointer to the newly created FunctionTerm_t structure.
 *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
FunctionTerm_t *
FunctionTerm_create(unsigned int level, unsigned int version,
                    unsigned int pkgVersion);


/**
 * Frees the given FunctionTerm_t structure.
 *
 * @param ft the FunctionTerm_t structure to free.
 *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
void
FunctionTerm_free(FunctionTerm_t * ft);


/**
 * Returns a copy of the given FunctionTerm_t structure.
 *
 * @param ft the FunctionTerm_t structure to copy.
 * 
 * @return a (deep) copy of the FunctionTerm_t.
 *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
FunctionTerm_t *
FunctionTerm_clone(FunctionTerm_t * ft);


/**
 * Takes a FunctionTerm_t structure and returns its resultLevel.
 *
 * @param ft the FunctionTerm_t whose resultLevel is sought.
 *
 * @return the resultLevel attribute of the given FunctionTerm_t, as an @c int.
 *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
int
FunctionTerm_getResultLevel(FunctionTerm_t * ft);


/**
 * Predicate returning @c true or @c false depending on whether the given
 * FunctionTerm_t structure's resultLevel is set.
 *
 * @param ft the FunctionTerm_t structure to query
 * 
 * @return @c non-zero (true) if the "resultLevel" attribute of the given
 * FunctionTerm_t structure is set, zero (false) otherwise.
 *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
int
FunctionTerm_isSetResultLevel(FunctionTerm_t * ft);


/**
 * Sets the "resultLevel" attribute of the given FunctionTerm_t
 * structure.
 *
 * @param ft the FunctionTerm_t structure
 * 
 * @param resultLevel the value of resultLevel to assign to the "resultLevel" attribute
 *
 * @return integer value indicating success/failure of the
 * function.  @if clike The value is drawn from the
 * enumeration #OperationReturnValues_t. @endif@~ The possible values
 * returned by this function are:
 * @li @link OperationReturnValues_t#LIBSBML_OPERATION_SUCCESS LIBSBML_OPERATION_SUCCESS @endlink
 * @li @link OperationReturnValues_t#LIBSBML_UNEXPECTED_ATTRIBUTE LIBSBML_UNEXPECTED_ATTRIBUTE @endlink
 *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
int
FunctionTerm_setResultLevel(FunctionTerm_t * ft, int resultLevel);


/**
 * Unsets the "resultLevel" attribute of the given FunctionTerm_t structure.
 *
 * @param ft the FunctionTerm_t structure to unset
 *
 * @return integer value indicating success/failure of the
 * function.  @if clike The value is drawn from the
 * enumeration #OperationReturnValues_t. @endif@~ The possible values
 * returned by this function are:
 * @li @link OperationReturnValues_t#LIBSBML_OPERATION_SUCCESS LIBSBML_OPERATION_SUCCESS @endlink
 * @li @link OperationReturnValues_t#LIBSBML_OPERATION_FAILED LIBSBML_OPERATION_FAILED @endlink
 *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
int
FunctionTerm_unsetResultLevel(FunctionTerm_t * ft);


/**
  * Predicate returning @c true or @c false depending on whether
  * all the required attributes for the given FunctionTerm_t structure
  * have been set.
  *
  * @note The required attributes for a FunctionTerm_t structure are:
  * @li useValuesfromTriggerTime ( L3 onwards )
  *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
int
FunctionTerm_hasRequiredAttributes(FunctionTerm_t * ft);


/**
  * Predicate returning @c true or @c false depending on whether
  * all the required elements for the given FunctionTerm_t structure
  * have been set.
  *
  * @note The required elements for an FunctionTerm_t structure are:
  * @li trigger
  * @li listOfEventAssignments (requirement removed in L3)
  *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
int
FunctionTerm_hasRequiredElements(FunctionTerm_t * ft);


/**
 * Return the FunctionTerm_t indicated by the given @p sid.
 *
 * @param lo the ListOf_t structure to use
 *
 * @param sid a string, the identifier of the
 * FunctionTerm_t is being sought.
 *
 * @return the FunctionTerm_t for the given variable, or @c NULL if no such
 * FunctionTerm_t exits.
 *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
FunctionTerm_t *
ListOfFunctionTerms_getById(ListOf_t * lo, const char * sid);


/**
 * Removes the FunctionTerm_t structure with the given @p sid
 * from the given ListOf_t structure and returns a pointer to it.
 *
 * The caller owns the returned structure and is responsible for deleting it.
 *
 * @param lo the ListOf_t structure
 * @param sid the string of the "id" attribute of the FunctionTerm_t sought
 *
 * @return the FunctionTerm_t structure removed.  As mentioned above, the 
 * caller owns the returned structure. @c NULL is returned if no FunctionTerm_t
 * structure with the "id" attribute exists in the given ListOf_t structure.
 *
 * @memberof FunctionTerm_t
 */
LIBSBML_EXTERN
FunctionTerm_t *
ListOfFunctionTerms_removeById(ListOf_t * lo, const char * sid);




END_C_DECLS
LIBSBML_CPP_NAMESPACE_END

#endif  /*  !SWIG  */

#endif /*  FunctionTerm_H__  */
