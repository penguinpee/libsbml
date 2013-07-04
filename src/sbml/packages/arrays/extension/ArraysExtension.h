/**
 * @file:   ArraysExtension.h
 * @brief:  Implementation of the ArraysExtension class
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
 */


#ifndef ArraysExtension_H__
#define ArraysExtension_H__


#include <sbml/common/extern.h>
#include <sbml/SBMLTypeCodes.h>


#ifdef __cplusplus


#include <sbml/extension/SBMLExtension.h>
#include <sbml/extension/SBMLExtensionNamespaces.h>
#include <sbml/extension/SBMLExtensionRegister.h>


#ifndef ARRAYS_CREATE_NS
	#define ARRAYS_CREATE_NS(variable, sbmlns)\
		EXTENSION_CREATE_NS(ArraysPkgNamespaces, variable, sbmlns);
#endif


#include <vector>


LIBSBML_CPP_NAMESPACE_BEGIN


class LIBSBML_EXTERN ArraysExtension : public SBMLExtension
{
public:

	//---------------------------------------------------------------
	//
	// Required class methods
	//
	//---------------------------------------------------------------

	/**
	 * Returns the package name of this extension.
	 */
	static const std::string& getPackageName ();


	/**
	 * Returns the default SBML Level this extension.
	 */
	static unsigned int getDefaultLevel();


	/**
	 * Returns the default SBML Version this extension.
	 */
	static unsigned int getDefaultVersion();


	/**
	 * Returns the default SBML version this extension.
	 */
	static unsigned int getDefaultPackageVersion();


	/**
	 * Returns URI of supported versions of this package.
	 */
	static const std::string&  getXmlnsL3V1V1();


	//
	// Other URI needed in this package (if any)
	//
	//---------------------------------------------------------------


	/**
	 * Creates a new ArraysExtension	 */
	ArraysExtension();


	/**
	 * Copy constructor for ArraysExtension.
	 *
	 * @param orig; the ArraysExtension instance to copy.
	 */
	ArraysExtension(const ArraysExtension& orig);


 	/**
	 * Assignment operator for ArraysExtension.
	 *
	 * @param rhs; the object whose values are used as the basis
	 * of the assignment
	 */
	ArraysExtension& operator=(const ArraysExtension& rhs);


 	/**
	 * Creates and returns a deep copy of this ArraysExtension object.
	 *
	 * @return a (deep) copy of this ArraysExtension object.
	 */
	virtual ArraysExtension* clone () const;


 	/**
	 * Destructor for ArraysExtension.
	 */
	virtual ~ArraysExtension();


 	/**
	 * Returns the name of this package ("arrays")
	 *
	 * @return a string representing the name of this package ("arrays")
	 */
	virtual const std::string& getName() const;


	/**
	 * Returns the URI (namespace) of the package corresponding to the combination of 
	 * the given sbml level, sbml version, and package version.
	 * Empty string will be returned if no corresponding URI exists.
	 *
	 * @param sbmlLevel the level of SBML
	 * @param sbmlVersion the version of SBML
	 * @param pkgVersion the version of package
	 *
	 * @return a string of the package URI
	 */
	virtual const std::string& getURI(unsigned int sbmlLevel,
	                                  unsigned int sbmlVersion,
	                                  unsigned int pkgVersion) const;


	/**
	 * Returns the SBML level with the given URI of this package.
	 *
	 * @param uri the string of URI that represents one of versions of arrays package
	 *
	 * @return the SBML level with the given URI of this package. 0 will be returned
	 * if the given URI is invalid.
	 *
	 */
	virtual unsigned int getLevel(const std::string &uri) const;


	/**
	 * Returns the SBML version with the given URI of this package.
	 *
	 * @param uri the string of URI that represents one of versions of arrays package
	 *
	 * @return the SBML version with the given URI of this package. 0 will be returned
	 * if the given URI is invalid.
	 *
	 */
	virtual unsigned int getVersion(const std::string &uri) const;


	/**
	 * Returns the package version with the given URI of this package.
	 *
	 * @param uri the string of URI that represents one of versions of arrays package
	 *
	 * @return the package version with the given URI of this package. 0 will be returned
	 * if the given URI is invalid.
	 *
	 */
	virtual unsigned int getPackageVersion(const std::string &uri) const;


	/**
	 * Returns an SBMLExtensionNamespaces<ArraysExtension> object whose alias type is 
	 * ArraysPkgNamespace.
	 * Null will be returned if the given uri is not defined in the arrays package.
	 *
	 * @param uri the string of URI that represents one of versions of arrays package
	 *
	 * @return an ArraysPkgNamespace object corresponding to the given uri. NULL will
	 * be returned if the given URI is not defined in arrays package.
	 */
	virtual SBMLNamespaces* getSBMLExtensionNamespaces(const std::string &uri) const;


	/**
	 * This method takes a type code from the Arrays package and returns a string representing 
	 * the code.
	 */
	virtual const char* getStringFromTypeCode(int typeCode) const;


	/** @cond doxygen-libsbml-internal */

	/**
	 * Initializes arrays extension by creating an object of this class with 
	 * required SBasePlugin derived objects and registering the object 
	 * to the SBMLExtensionRegistry class.
	 *
	 * (NOTE) This function is automatically invoked when creating the following
	 *        global object in ArraysExtension.cpp
	 *
	 *        static SBMLExtensionRegister<ArraysExtension> arraysExtensionRegistry;
	 *
	 */
	static void init();


	/** @endcond doxygen-libsbml-internal */


};


// --------------------------------------------------------------------
//
// Required typedef definitions
//
// ArraysPkgNamespaces is derived from the SBMLNamespaces class and
// used when creating an object of SBase derived classes defined in
// arrays package.
//
// --------------------------------------------------------------------
//
// (NOTE)
//
// SBMLExtensionNamespaces<ArraysExtension> must be instantiated
// in ArraysExtension.cpp for DLL.
//
typedef SBMLExtensionNamespaces<ArraysExtension> ArraysPkgNamespaces;

typedef enum
{
	  SBML_ARRAYS_DIMENSION  = 1200
	, SBML_ARRAYS_INDEX              = 1201
} SBMLArraysTypeCode_t;

typedef enum
{
     AST_ARRAYS_FUNCTION_SELECTOR = 11001
     , AST_FUNCTION_SUM    = 11002
} ArrayASTNodeType_t;



LIBSBML_CPP_NAMESPACE_END


#endif /* __cplusplus */
#endif /* ArraysExtension_H__ */


