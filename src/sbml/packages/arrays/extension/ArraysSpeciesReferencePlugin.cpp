/**
 * @file:   ArraysSpeciesReferencePlugin.cpp
 * @brief:  Implementation of the ArraysSpeciesReferencePlugin class
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


#include <sbml/packages/arrays/extension/ArraysSpeciesReferencePlugin.h>


using namespace std;


#ifdef __cplusplus


LIBSBML_CPP_NAMESPACE_BEGIN


/*
 * Creates a new ArraysSpeciesReferencePlugin
 */
ArraysSpeciesReferencePlugin::ArraysSpeciesReferencePlugin(const std::string& uri,  
                                 const std::string& prefix, 
                               ArraysPkgNamespaces* arraysns) :
	  SBasePlugin(uri, prefix, arraysns)
	, mDimensions (arraysns)
	, mIndexs (arraysns)
{
}


/*
 * Copy constructor for ArraysSpeciesReferencePlugin.
 */
ArraysSpeciesReferencePlugin::ArraysSpeciesReferencePlugin(const ArraysSpeciesReferencePlugin& orig) :
	  SBasePlugin(orig)
	, mDimensions ( orig.mDimensions)
	, mIndexs ( orig.mIndexs)
{
}


/*
 * Assignment operator for ArraysSpeciesReferencePlugin.
 */
ArraysSpeciesReferencePlugin& 
ArraysSpeciesReferencePlugin::operator=(const ArraysSpeciesReferencePlugin& rhs)
{
	if (&rhs != this)
	{
		this->SBasePlugin::operator=(rhs);
		mDimensions = rhs.mDimensions;
		mIndexs = rhs.mIndexs;
	}

	return *this;
}


/*
 * Creates and returns a deep copy of this ArraysSpeciesReferencePlugin object.
 */
ArraysSpeciesReferencePlugin* 
ArraysSpeciesReferencePlugin::clone () const
{
	return new ArraysSpeciesReferencePlugin(*this);
}


/*
 * Destructor for ArraysSpeciesReferencePlugin.
 */
ArraysSpeciesReferencePlugin::~ArraysSpeciesReferencePlugin()
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
ArraysSpeciesReferencePlugin::createObject (XMLInputStream& stream)
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
		else if (name == "orderedListOfIndices" ) 
		{ 
			object = &mIndexs;

			if (targetPrefix.empty() == true) 
			{ 
				mIndexs.getSBMLDocument()->enableDefaultNS(mURI, true); 
			} 
		} 
	} 

	return object; 
}


/*
 * write elements
 */
void
ArraysSpeciesReferencePlugin::writeElements (XMLOutputStream& stream) const
{
	if (getNumDimensions() > 0) 
	{ 
		mDimensions.write(stream);
	} 
	if (getNumIndexs() > 0) 
	{ 
		mIndexs.write(stream);
	} 
}


/*
 * Checks if this plugin object has all the required elements.
 */
bool
ArraysSpeciesReferencePlugin::hasRequiredElements () const
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
ArraysSpeciesReferencePlugin::getListOfDimensions () const
{
	return static_cast<const ListOfDimensions*>(&this->mDimensions);
}


/*
 * Returns the ListOfDimensions in this plugin object.
 */
ListOfDimensions* 
ArraysSpeciesReferencePlugin::getListOfDimensions ()
{
	return &this->mDimensions;
}


/*
 * Returns the Dimension object that belongs to the given index.
 */
const Dimension*
ArraysSpeciesReferencePlugin::getDimension(unsigned int n) const
{
	return static_cast<const Dimension*>(mDimensions.get(n));
}


/*
 * Returns the Dimension object that belongs to the given index.
 */
Dimension*
ArraysSpeciesReferencePlugin::getDimension(unsigned int n)
{
	return static_cast<Dimension*>(mDimensions.get(n));
}


/*
 * Returns the Dimension object based on its identifier.
 */
const Dimension*
ArraysSpeciesReferencePlugin::getDimension(const std::string& sid) const
{
	return static_cast<const Dimension*>(mDimensions.get(sid));
}


/*
 * Returns the Dimension object based on its identifier.
Dimension*
ArraysSpeciesReferencePlugin::getDimension(const std::string& sid)
{
	return static_cast<const Dimension*>(mDimensions.get(sid));
}


/*
 * Adds a copy of the given Dimension to the ListOfDimensions in this plugin object.
 */
int
ArraysSpeciesReferencePlugin::addDimension (const Dimension* dimension)
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
ArraysSpeciesReferencePlugin::createDimension ()
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
ArraysSpeciesReferencePlugin::removeDimension(unsigned int n)
{
	return static_cast<Dimension*>(mDimensions.remove(n));
}


/*
 * Removes the Dimension object with the given id from this plugin object
 */
Dimension* 
ArraysSpeciesReferencePlugin::removeDimension(const std::string& sid)
{
	return static_cast<Dimension*>(mDimensions.remove(sid));
}


/*
 * Returns the number of Dimension objects in this plugin object.
 */
unsigned int 
ArraysSpeciesReferencePlugin::getNumDimensions () const
{
	return mDimensions.size();
}


/*
 * Returns the ListOfIndices in this plugin object.
 */
const ListOfIndices* 
ArraysSpeciesReferencePlugin::getListOfIndices () const
{
	return static_cast<const ListOfIndices*>(&this->mIndexs);
}


/*
 * Returns the ListOfIndices in this plugin object.
 */
ListOfIndices* 
ArraysSpeciesReferencePlugin::getListOfIndices ()
{
	return &this->mIndexs;
}


/*
 * Returns the Index object that belongs to the given index.
 */
const Index*
ArraysSpeciesReferencePlugin::getIndex(unsigned int n) const
{
	return static_cast<const Index*>(mIndexs.get(n));
}


/*
 * Returns the Index object that belongs to the given index.
 */
Index*
ArraysSpeciesReferencePlugin::getIndex(unsigned int n)
{
	return static_cast<Index*>(mIndexs.get(n));
}


/*
 * Returns the Index object based on its identifier.
 */
const Index*
ArraysSpeciesReferencePlugin::getIndex(const std::string& sid) const
{
	return static_cast<const Index*>(mIndexs.get(sid));
}


/*
 * Returns the Index object based on its identifier.
Index*
ArraysSpeciesReferencePlugin::getIndex(const std::string& sid)
{
	return static_cast<const Index*>(mIndexs.get(sid));
}


/*
 * Adds a copy of the given Index to the ListOfIndices in this plugin object.
 */
int
ArraysSpeciesReferencePlugin::addIndex (const Index* index)
{
	if (index == NULL)
	{
		return LIBSBML_OPERATION_FAILED;
	}
	else if (index->hasRequiredElements() == false)
	{
		return LIBSBML_INVALID_OBJECT;
	}
	else if (getLevel() != index->getLevel())
	{
		return LIBSBML_LEVEL_MISMATCH;
	}
	else if (getVersion() != index->getVersion())
	{
		return LIBSBML_VERSION_MISMATCH;
	}
	else if (getPackageVersion() != index->getPackageVersion())
	{
		return LIBSBML_PKG_VERSION_MISMATCH;
	}
	else
	{
		mIndexs.append(index);
	}

	return LIBSBML_OPERATION_SUCCESS;

}


/*
 * Creates a new Index object and adds it to the ListOfIndices in this plugin object.
 */
Index* 
ArraysSpeciesReferencePlugin::createIndex ()
{
	 Index* i = NULL;

	try
	{
		ARRAYS_CREATE_NS(arraysns, getSBMLNamespaces());
		i = new Index(arraysns);
	}
	catch(...)
	{
	}

	if (i != NULL)
	{
		mIndexs.appendAndOwn(i);
	}

	return i;
}


/*
 * Removes the nth Index object from this plugin object
 */
Index* 
ArraysSpeciesReferencePlugin::removeIndex(unsigned int n)
{
	return static_cast<Index*>(mIndexs.remove(n));
}


/*
 * Removes the Index object with the given id from this plugin object
 */
Index* 
ArraysSpeciesReferencePlugin::removeIndex(const std::string& sid)
{
	return static_cast<Index*>(mIndexs.remove(sid));
}


/*
 * Returns the number of Index objects in this plugin object.
 */
unsigned int 
ArraysSpeciesReferencePlugin::getNumIndexs () const
{
	return mIndexs.size();
}


//---------------------------------------------------------------


/*
 * Set the SBMLDocument.
 */
void
ArraysSpeciesReferencePlugin::setSBMLDocument(SBMLDocument* d)
{
	SBasePlugin::setSBMLDocument(d);

	mDimensions.setSBMLDocument(d);
	mIndexs.setSBMLDocument(d);
}


/*
 * Connect to parent.
 */
void
ArraysSpeciesReferencePlugin::connectToParent(SBase* sbase)
{
	SBasePlugin::connectToParent(sbase);

	mDimensions.connectToParent(sbase);
	mIndexs.connectToParent(sbase);
}


/*
 * Enables the given package.
 */
void
ArraysSpeciesReferencePlugin::enablePackageInternal(const std::string& pkgURI,
                                   const std::string& pkgPrefix, bool flag)
{
	mDimensions.enablePackageInternal(pkgURI, pkgPrefix, flag);
	mIndexs.enablePackageInternal(pkgURI, pkgPrefix, flag);
}




LIBSBML_CPP_NAMESPACE_END


#endif /* __cplusplus */


