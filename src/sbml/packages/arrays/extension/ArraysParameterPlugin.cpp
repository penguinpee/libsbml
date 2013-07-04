/**
 * @file:   ArraysParameterPlugin.cpp
 * @brief:  Implementation of the ArraysParameterPlugin class
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


#include <sbml/packages/arrays/extension/ArraysParameterPlugin.h>


using namespace std;


#ifdef __cplusplus


LIBSBML_CPP_NAMESPACE_BEGIN


/*
 * Creates a new ArraysParameterPlugin
 */
ArraysParameterPlugin::ArraysParameterPlugin(const std::string& uri,  
                                 const std::string& prefix, 
                               ArraysPkgNamespaces* arraysns) :
	  SBasePlugin(uri, prefix, arraysns)
	, mDimensions (arraysns)
{
}


/*
 * Copy constructor for ArraysParameterPlugin.
 */
ArraysParameterPlugin::ArraysParameterPlugin(const ArraysParameterPlugin& orig) :
	  SBasePlugin(orig)
	, mDimensions ( orig.mDimensions)
{
}


/*
 * Assignment operator for ArraysParameterPlugin.
 */
ArraysParameterPlugin& 
ArraysParameterPlugin::operator=(const ArraysParameterPlugin& rhs)
{
	if (&rhs != this)
	{
		this->SBasePlugin::operator=(rhs);
		mDimensions = rhs.mDimensions;
	}

	return *this;
}


/*
 * Creates and returns a deep copy of this ArraysParameterPlugin object.
 */
ArraysParameterPlugin* 
ArraysParameterPlugin::clone () const
{
	return new ArraysParameterPlugin(*this);
}


/*
 * Destructor for ArraysParameterPlugin.
 */
ArraysParameterPlugin::~ArraysParameterPlugin()
{
}


//---------------------------------------------------------------
//
// overridden virtual functions for read/write/check
//
//---------------------------------------------------------------

/*
 * create object
 */
SBase*
ArraysParameterPlugin::createObject (XMLInputStream& stream)
{
	SBase* object = NULL; 

	const std::string&      name   = stream.peek().getName(); 
	const XMLNamespaces&    xmlns  = stream.peek().getNamespaces(); 
	const std::string&      prefix = stream.peek().getPrefix(); 

	const std::string& targetPrefix = (xmlns.hasURI(mURI)) ? xmlns.getPrefix(mURI) : mPrefix;

	if (prefix == targetPrefix) 
	{ 
		if (name == "orderedListOfDimensions" ) 
		{ 
			object = &mDimensions;

			if (targetPrefix.empty() == true) 
			{ 
				mDimensions.getSBMLDocument()->enableDefaultNS(mURI, true); 
			} 
		} 
	} 

	return object; 
}


/*
 * write elements
 */
void
ArraysParameterPlugin::writeElements (XMLOutputStream& stream) const
{
	if (getNumDimensions() > 0) 
	{ 
		mDimensions.write(stream);
	} 
}


/*
 * Checks if this plugin object has all the required elements.
 */
bool
ArraysParameterPlugin::hasRequiredElements () const
{
	bool allPresent = true; 

	// TO DO 

	return allPresent; 
}


//---------------------------------------------------------------
//
// Functions for interacting with the members of the plugin
//
//---------------------------------------------------------------

/*
 * Returns the ListOfDimensions in this plugin object.
 */
const ListOfDimensions* 
ArraysParameterPlugin::getListOfDimensions () const
{
	return static_cast<const ListOfDimensions*>(&this->mDimensions);
}


/*
 * Returns the ListOfDimensions in this plugin object.
 */
ListOfDimensions* 
ArraysParameterPlugin::getListOfDimensions ()
{
	return &this->mDimensions;
}


/*
 * Returns the Dimension object that belongs to the given index.
 */
const Dimension*
ArraysParameterPlugin::getDimension(unsigned int n) const
{
	return static_cast<const Dimension*>(mDimensions.get(n));
}


/*
 * Returns the Dimension object that belongs to the given index.
 */
Dimension*
ArraysParameterPlugin::getDimension(unsigned int n)
{
	return static_cast<Dimension*>(mDimensions.get(n));
}


/*
 * Returns the Dimension object based on its identifier.
 */
const Dimension*
ArraysParameterPlugin::getDimension(const std::string& sid) const
{
	return static_cast<const Dimension*>(mDimensions.get(sid));
}


/*
 * Returns the Dimension object based on its identifier.
Dimension*
ArraysParameterPlugin::getDimension(const std::string& sid)
{
	return static_cast<const Dimension*>(mDimensions.get(sid));
}


/*
 * Adds a copy of the given Dimension to the ListOfDimensions in this plugin object.
 */
int
ArraysParameterPlugin::addDimension (const Dimension* dimension)
{
	if (dimension == NULL)
	{
		return LIBSBML_OPERATION_FAILED;
	}
	else if (dimension->hasRequiredElements() == false)
	{
		return LIBSBML_INVALID_OBJECT;
	}
	else if (getLevel() != dimension->getLevel())
	{
		return LIBSBML_LEVEL_MISMATCH;
	}
	else if (getVersion() != dimension->getVersion())
	{
		return LIBSBML_VERSION_MISMATCH;
	}
	else if (getPackageVersion() != dimension->getPackageVersion())
	{
		return LIBSBML_PKG_VERSION_MISMATCH;
	}
	else
	{
		mDimensions.append(dimension);
	}

	return LIBSBML_OPERATION_SUCCESS;

}


/*
 * Creates a new Dimension object and adds it to the ListOfDimensions in this plugin object.
 */
Dimension* 
ArraysParameterPlugin::createDimension ()
{
	 Dimension* d = NULL;

	try
	{
		ARRAYS_CREATE_NS(arraysns, getSBMLNamespaces());
		d = new Dimension(arraysns);
	}
	catch(...)
	{
	}

	if (d != NULL)
	{
		mDimensions.appendAndOwn(d);
	}

	return d;
}


/*
 * Removes the nth Dimension object from this plugin object
 */
Dimension* 
ArraysParameterPlugin::removeDimension(unsigned int n)
{
	return static_cast<Dimension*>(mDimensions.remove(n));
}


/*
 * Removes the Dimension object with the given id from this plugin object
 */
Dimension* 
ArraysParameterPlugin::removeDimension(const std::string& sid)
{
	return static_cast<Dimension*>(mDimensions.remove(sid));
}


/*
 * Returns the number of Dimension objects in this plugin object.
 */
unsigned int 
ArraysParameterPlugin::getNumDimensions () const
{
	return mDimensions.size();
}


//---------------------------------------------------------------


/*
 * Set the SBMLDocument.
 */
void
ArraysParameterPlugin::setSBMLDocument(SBMLDocument* d)
{
	SBasePlugin::setSBMLDocument(d);

	mDimensions.setSBMLDocument(d);
}


/*
 * Connect to parent.
 */
void
ArraysParameterPlugin::connectToParent(SBase* sbase)
{
	SBasePlugin::connectToParent(sbase);

	mDimensions.connectToParent(sbase);
}


/*
 * Enables the given package.
 */
void
ArraysParameterPlugin::enablePackageInternal(const std::string& pkgURI,
                                   const std::string& pkgPrefix, bool flag)
{
	mDimensions.enablePackageInternal(pkgURI, pkgPrefix, flag);
}




LIBSBML_CPP_NAMESPACE_END


#endif /* __cplusplus */


