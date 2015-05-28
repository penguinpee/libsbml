/**
 * @file:   Output.cpp
 * @brief:  Implementation of the Output class
 * @author: Generated by autocreate code
 *
 * <!--------------------------------------------------------------------------
 * This file is part of libSBML.  Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 *
 * Copyright (C) 2013-2015 jointly by the following organizations:
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
 * ------------------------------------------------------------------------ -->
 */


#include <sbml/packages/qual/sbml/Output.h>
#include <sbml/packages/qual/validator/QualSBMLError.h>


using namespace std;


LIBSBML_CPP_NAMESPACE_BEGIN
#ifdef __cplusplus


/*
 * Creates a new Output with the given level, version, and package version.
 */
Output::Output (unsigned int level, unsigned int version, unsigned int pkgVersion)
  : SBase(level, version)
   ,mId ("")
   ,mQualitativeSpecies ("")
   ,mTransitionEffect (OUTPUT_TRANSITION_EFFECT_UNKNOWN)
   ,mName ("")
   ,mOutputLevel (SBML_INT_MAX)
   ,mIsSetOutputLevel (false)
{
  // set an SBMLNamespaces derived object of this package
  setSBMLNamespacesAndOwn(new QualPkgNamespaces(level, version, pkgVersion));
}


/*
 * Creates a new Output with the given QualPkgNamespaces object.
 */
Output::Output (QualPkgNamespaces* qualns)
  : SBase(qualns)
   ,mId ("")
   ,mQualitativeSpecies ("")
   ,mTransitionEffect (OUTPUT_TRANSITION_EFFECT_UNKNOWN)
   ,mName ("")
   ,mOutputLevel (SBML_INT_MAX)
   ,mIsSetOutputLevel (false)
{
  // set the element namespace of this object
  setElementNamespace(qualns->getURI());

  // load package extensions bound with this object (if any) 
  loadPlugins(qualns);
}


/*
 * Copy constructor for Output.
 */
Output::Output (const Output& orig)
  : SBase ( orig )
  , mId ( orig.mId )
  , mQualitativeSpecies ( orig.mQualitativeSpecies )
  , mTransitionEffect ( orig.mTransitionEffect )
  , mName ( orig.mName )
  , mOutputLevel ( orig.mOutputLevel )
  , mIsSetOutputLevel ( orig.mIsSetOutputLevel )
{
}


/*
 * Assignment for Output.
 */
Output&
Output::operator=(const Output& rhs)
{
  if (&rhs != this)
  {
    SBase::operator=(rhs);
    mId  = rhs.mId;
    mQualitativeSpecies  = rhs.mQualitativeSpecies;
    mTransitionEffect  = rhs.mTransitionEffect;
    mName  = rhs.mName;
    mOutputLevel  = rhs.mOutputLevel;
    mIsSetOutputLevel  = rhs.mIsSetOutputLevel;
  }
  return *this;
}


/*
 * Clone for Output.
 */
Output*
Output::clone () const
{
  return new Output(*this);
}


/*
 * Destructor for Output.
 */
Output::~Output ()
{
}


/*
 * Returns the value of the "id" attribute of this Output.
 */
const std::string&
Output::getId() const
{
  return mId;
}


/*
 * Returns the value of the "qualitativeSpecies" attribute of this Output.
 */
const std::string&
Output::getQualitativeSpecies() const
{
  return mQualitativeSpecies;
}


/*
 * Returns the value of the "transitionEffect" attribute of this Output.
 */
OutputTransitionEffect_t
Output::getTransitionEffect() const
{
  return mTransitionEffect;
}


/*
 * Returns the value of the "name" attribute of this Output.
 */
const std::string&
Output::getName() const
{
  return mName;
}


/*
 * Returns the value of the "outputLevel" attribute of this Output.
 */
int
Output::getOutputLevel() const
{
  return mOutputLevel;
}


/*
 * Returns true/false if id is set.
 */
bool
Output::isSetId() const
{
  return (mId.empty() == false);
}


/*
 * Returns true/false if qualitativeSpecies is set.
 */
bool
Output::isSetQualitativeSpecies() const
{
  return (mQualitativeSpecies.empty() == false);
}


/*
 * Returns true/false if transitionEffect is set.
 */
bool
Output::isSetTransitionEffect() const
{
  return (mTransitionEffect != OUTPUT_TRANSITION_EFFECT_UNKNOWN);
}


/*
 * Returns true/false if name is set.
 */
bool
Output::isSetName() const
{
  return (mName.empty() == false);
}


/*
 * Returns true/false if outputLevel is set.
 */
bool
Output::isSetOutputLevel() const
{
  return mIsSetOutputLevel;
}


/*
 * Sets id and returns value indicating success.
 */
int
Output::setId(const std::string& id)
{
  return SyntaxChecker::checkAndSetSId(id, mId);
}


/*
 * Sets qualitativeSpecies and returns value indicating success.
 */
int
Output::setQualitativeSpecies(const std::string& qualitativeSpecies)
{
  if (!(SyntaxChecker::isValidInternalSId(qualitativeSpecies)))
  {
    return LIBSBML_INVALID_ATTRIBUTE_VALUE;
  }
  else
  {
    mQualitativeSpecies = qualitativeSpecies;
    return LIBSBML_OPERATION_SUCCESS;
  }
}


/*
 * Sets transitionEffect and returns value indicating success.
 */
int
Output::setTransitionEffect(const OutputTransitionEffect_t transitionEffect)
{
  if (OutputTransitionEffect_isValidOutputTransitionEffect(transitionEffect) == 0)
  {
    mTransitionEffect = OUTPUT_TRANSITION_EFFECT_UNKNOWN;
    return LIBSBML_INVALID_ATTRIBUTE_VALUE;
  }
  else
  {
    mTransitionEffect = transitionEffect;
    return LIBSBML_OPERATION_SUCCESS;
  }
}


/*
 * Sets name and returns value indicating success.
 */
int
Output::setName(const std::string& name)
{

 mName = name;
 return LIBSBML_OPERATION_SUCCESS;

}


/*
 * Sets outputLevel and returns value indicating success.
 */
int
Output::setOutputLevel(int outputLevel)
{
  mOutputLevel = outputLevel;
  mIsSetOutputLevel = true;
  return LIBSBML_OPERATION_SUCCESS;
}


/*
 * Unsets id and returns value indicating success.
 */
int
Output::unsetId()
{
  mId.erase();

  if (mId.empty() == true)
  {
    return LIBSBML_OPERATION_SUCCESS;
  }
  else
  {
    return LIBSBML_OPERATION_FAILED;
  }
}


/*
 * Unsets qualitativeSpecies and returns value indicating success.
 */
int
Output::unsetQualitativeSpecies()
{
  mQualitativeSpecies.erase();

  if (mQualitativeSpecies.empty() == true)
  {
    return LIBSBML_OPERATION_SUCCESS;
  }
  else
  {
    return LIBSBML_OPERATION_FAILED;
  }
}


/*
 * Unsets transitionEffect and returns value indicating success.
 */
int
Output::unsetTransitionEffect()
{
  mTransitionEffect = OUTPUT_TRANSITION_EFFECT_UNKNOWN;
  return LIBSBML_OPERATION_SUCCESS;
}


/*
 * Unsets name and returns value indicating success.
 */
int
Output::unsetName()
{
  mName.erase();

  if (mName.empty() == true)
  {
    return LIBSBML_OPERATION_SUCCESS;
  }
  else
  {
    return LIBSBML_OPERATION_FAILED;
  }
}


/*
 * Unsets outputLevel and returns value indicating success.
 */
int
Output::unsetOutputLevel()
{
  mOutputLevel = SBML_INT_MAX;
  mIsSetOutputLevel = false;

  if (isSetOutputLevel() == false)
  {
    return LIBSBML_OPERATION_SUCCESS;
  }
  else
  {
    return LIBSBML_OPERATION_FAILED;
  }
}


/*
 * rename attributes that are SIdRefs or instances in math
 */
void
Output::renameSIdRefs(const std::string& oldid, const std::string& newid)
{
  if (isSetQualitativeSpecies() == true && mQualitativeSpecies == oldid)
  {
    setQualitativeSpecies(newid);
  }

}


/*
 * Returns the XML element name of this object
 */
const std::string&
Output::getElementName () const
{
  static const string name = "output";
  return name;
}


/*
 * Returns the libSBML type code for this SBML object.
 */
int
Output::getTypeCode () const
{
  return SBML_QUAL_OUTPUT;
}


/*
 * check if all the required attributes are set
 */
bool
Output::hasRequiredAttributes () const
{
  bool allPresent = true;

  if (isSetQualitativeSpecies() == false)
    allPresent = false;

  if (isSetTransitionEffect() == false)
    allPresent = false;

  return allPresent;
}


  /** @cond doxygenLibsbmlInternal */

/*
 * write contained elements
 */
void
Output::writeElements (XMLOutputStream& stream) const
{
  SBase::writeElements(stream);

  SBase::writeExtensionElements(stream);
}


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

/*
 * Accepts the given SBMLVisitor.
 */
bool
Output::accept (SBMLVisitor& v) const
{
  return v.visit(*this);
}


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

/*
 * Sets the parent SBMLDocument.
 */
void
Output::setSBMLDocument (SBMLDocument* d)
{
  SBase::setSBMLDocument(d);
}


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

/*
 * Enables/Disables the given package with this element.
 */
void
Output::enablePackageInternal(const std::string& pkgURI,
             const std::string& pkgPrefix, bool flag)
{
  SBase::enablePackageInternal(pkgURI, pkgPrefix, flag);
}


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

/*
 * Get the list of expected attributes for this element.
 */
void
Output::addExpectedAttributes(ExpectedAttributes& attributes)
{
  SBase::addExpectedAttributes(attributes);

  attributes.add("id");
  attributes.add("qualitativeSpecies");
  attributes.add("transitionEffect");
  attributes.add("name");
  attributes.add("outputLevel");
}


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

/*
 * Read values from the given XMLAttributes set into their specific fields.
 */
void
Output::readAttributes (const XMLAttributes& attributes,
                             const ExpectedAttributes& expectedAttributes)
{
  const unsigned int sbmlLevel   = getLevel  ();
  const unsigned int sbmlVersion = getVersion();

  unsigned int numErrs;

  /* look to see whether an unknown attribute error was logged
   * during the read of the listOfOutputs - which will have
   * happened immediately prior to this read
  */

  if (getErrorLog() != NULL && 
    static_cast<ListOfOutputs*>(getParentSBMLObject())->size() < 2)
  {
    numErrs = getErrorLog()->getNumErrors();
    for (int n = numErrs-1; n >= 0; n--)      
    {
      if (getErrorLog()->getError(n)->getErrorId() == UnknownPackageAttribute)
      {
        const std::string details = 
          getErrorLog()->getError(n)->getMessage();
        getErrorLog()->remove(UnknownPackageAttribute);
        getErrorLog()->logPackageError("qual", QualTransitionLOOutputAttributes,
          getPackageVersion(), sbmlLevel, sbmlVersion, details);
      } 
      else if (getErrorLog()->getError(n)->getErrorId() == UnknownCoreAttribute)
      {
        const std::string details = 
          getErrorLog()->getError(n)->getMessage();
        getErrorLog()->remove(UnknownCoreAttribute);
        getErrorLog()->logPackageError("qual", QualTransitionLOOutputAttributes,
          getPackageVersion(), sbmlLevel, sbmlVersion, details);
      } 
    }
  }

  SBase::readAttributes(attributes, expectedAttributes);

  // look to see whether an unknown attribute error was logged
  if (getErrorLog() != NULL)
  {
    numErrs = getErrorLog()->getNumErrors();
    for (int n = numErrs-1; n >= 0; n--)
    {
      if (getErrorLog()->getError(n)->getErrorId() == UnknownPackageAttribute)
      {
        const std::string details =
                          getErrorLog()->getError(n)->getMessage();
        getErrorLog()->remove(UnknownPackageAttribute);
        getErrorLog()->logPackageError("qual", QualOutputAllowedAttributes,
                       getPackageVersion(), sbmlLevel, sbmlVersion, details);
      }
      else if (getErrorLog()->getError(n)->getErrorId() == UnknownCoreAttribute)
      {
        const std::string details =
                          getErrorLog()->getError(n)->getMessage();
        getErrorLog()->remove(UnknownCoreAttribute);
        getErrorLog()->logPackageError("qual", QualOutputAllowedCoreAttributes,
                       getPackageVersion(), sbmlLevel, sbmlVersion, details);
      }
    }
  }

  bool assigned = false;

  //
  // id SId  ( use = "optional" )
  //
  assigned = attributes.readInto("id", mId);

   if (assigned == true)
  {
    // check string is not empty and correct syntax

    if (mId.empty() == true)
    {
      logEmptyString(mId, getLevel(), getVersion(), "<Output>");
    }
    else if (SyntaxChecker::isValidSBMLSId(mId) == false)
    {
      logError(InvalidIdSyntax, sbmlLevel, sbmlVersion, "The id '" + mId + "' does not conform to the syntax.");
    }
  }

  //
  // qualitativeSpecies SIdRef   ( use = "required" )
  //
  assigned = attributes.readInto("qualitativeSpecies", mQualitativeSpecies);

  if (assigned == true)
  {
    // check string is not empty and correct syntax

    if (mQualitativeSpecies.empty() == true)
    {
      logEmptyString(mQualitativeSpecies, getLevel(), getVersion(), "<Output>");
    }
    else if (SyntaxChecker::isValidSBMLSId(mQualitativeSpecies) == false)
    {
      logError(InvalidIdSyntax, getLevel(), getVersion(), 
        "The syntax of the attribute qualitativeSpecies='" + mQualitativeSpecies 
        + "' does not conform to the syntax.");
    }
  }
  else
  {
    std::string message = "Qual attribute 'qualitativeSpecies' is missing.";
    getErrorLog()->logPackageError("qual", QualOutputAllowedAttributes,
                   getPackageVersion(), sbmlLevel, sbmlVersion, message);
  }

  //
  // transitionEffect string   ( use = "required" )
  //
  std::string effect;
  assigned = attributes.readInto("transitionEffect", effect);

  if (assigned == true)
  {
    // check string is not empty

    if (effect.empty() == true)
    {
      logEmptyString(effect, getLevel(), getVersion(), "<Output>");
    }
    else 
    {
       mTransitionEffect = OutputTransitionEffect_fromString( effect.c_str() );
       if (OutputTransitionEffect_isValidOutputTransitionEffect(mTransitionEffect) == 0)
       {
          std::string msg = "The transitionEffect on the <output> ";
          if (isSetId()) {
            msg += "with id '" + getId() + "' ";
          }
          msg += "is '" + effect + "', which is not a valid option.";
          getErrorLog()->logPackageError("qual", QualOutputTransEffectMustBeOutput,
                         getPackageVersion(), sbmlLevel, sbmlVersion, msg);
       }
    }
  }
  else
  {
    std::string message = "Qual attribute 'transitionEffect' is missing.";
    getErrorLog()->logPackageError("qual", QualOutputAllowedAttributes,
                   getPackageVersion(), sbmlLevel, sbmlVersion, message);
  }

  //
  // name string   ( use = "optional" )
  //
  assigned = attributes.readInto("name", mName);

  if (assigned == true)
  {
    // check string is not empty

    if (mName.empty() == true)
    {
      logEmptyString(mName, getLevel(), getVersion(), "<Output>");
    }
  }

  //
  // outputLevel int   ( use = "optional" )
  //
  numErrs = getErrorLog()->getNumErrors();
  mIsSetOutputLevel = attributes.readInto("outputLevel", mOutputLevel);

  if (mIsSetOutputLevel == false)
  {
    if (getErrorLog() != NULL)
    {
      if (getErrorLog()->getNumErrors() == numErrs + 1 &&
              getErrorLog()->contains(XMLAttributeTypeMismatch))
      {
        getErrorLog()->remove(XMLAttributeTypeMismatch);
        getErrorLog()->logPackageError("qual", QualOutputLevelMustBeInteger,
                     getPackageVersion(), sbmlLevel, sbmlVersion);
      }
    }
  }
  else
  {
    if (mOutputLevel < 0)
    {
      std::stringstream msg;
      msg << "The outputLevel of the <output> ";
      if (isSetId()) {
        msg << "with id '" << getId() << "' ";
      }
      msg << "is '" << mOutputLevel << "', which is negative.";
      getErrorLog()->logPackageError("qual", QualOutputLevelMustBeNonNegative,
                   getPackageVersion(), sbmlLevel, sbmlVersion, msg.str());
    }
  }

}


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

/*
 * Write values of XMLAttributes to the output stream.
 */
  void
Output::writeAttributes (XMLOutputStream& stream) const
{
  SBase::writeAttributes(stream);

  if (isSetId() == true)
    stream.writeAttribute("id", getPrefix(), mId);

  if (isSetQualitativeSpecies() == true)
    stream.writeAttribute("qualitativeSpecies", getPrefix(), mQualitativeSpecies);

  if (isSetTransitionEffect() == true)
    stream.writeAttribute("transitionEffect", getPrefix(), 
                     OutputTransitionEffect_toString(mTransitionEffect));

  if (isSetName() == true)
    stream.writeAttribute("name", getPrefix(), mName);

  if (isSetOutputLevel() == true)
    stream.writeAttribute("outputLevel", getPrefix(), mOutputLevel);

  SBase::writeExtensionAttributes(stream);

}


  /** @endcond */


/*
 * Constructor 
 */
ListOfOutputs::ListOfOutputs(unsigned int level, 
                             unsigned int version, 
                             unsigned int pkgVersion)
 : ListOf(level, version)
{
  setSBMLNamespacesAndOwn(new QualPkgNamespaces(level, version, pkgVersion)); 
}


/*
 * Constructor 
 */
ListOfOutputs::ListOfOutputs(QualPkgNamespaces* qualns)
  : ListOf(qualns)
{
  setElementNamespace(qualns->getURI());
}


/*
 * Returns a deep copy of this ListOfOutputs 
 */
ListOfOutputs* 
ListOfOutputs::clone () const
 {
  return new ListOfOutputs(*this);
}


/*
 * Get a Output from the ListOfOutputs by index.
*/
Output*
ListOfOutputs::get(unsigned int n)
{
  return static_cast<Output*>(ListOf::get(n));
}


/*
 * Get a Output from the ListOfOutputs by index.
 */
const Output*
ListOfOutputs::get(unsigned int n) const
{
  return static_cast<const Output*>(ListOf::get(n));
}


/*
 * Get a Output from the ListOfOutputs by id.
 */
Output*
ListOfOutputs::get(const std::string& sid)
{
  return const_cast<Output*>(
    static_cast<const ListOfOutputs&>(*this).get(sid));
}


/*
 * Get a Output from the ListOfOutputs by id.
 */
const Output*
ListOfOutputs::get(const std::string& sid) const
{
  vector<SBase*>::const_iterator result;

  result = find_if( mItems.begin(), mItems.end(), IdEq<Output>(sid) );
  return (result == mItems.end()) ? 0 : static_cast <Output*> (*result);
}


Output*
ListOfOutputs::getBySpecies(const std::string& sid)
{
  return const_cast<Output*>(
    static_cast<const ListOfOutputs&>(*this).getBySpecies(sid));
}

/**
 * Used by ListOfOutputs::get() to lookup an Output based by its 
 * qualitativeSpecies.
 */
struct IdEqQS : public std::unary_function<SBase*, bool>
{
  const string& id;

  IdEqQS (const string& id) : id(id) { }
  bool operator() (SBase* sb)
       { return (static_cast <Output *> (sb)->getQualitativeSpecies()  == id); } 
};



/*
 * Get a Output from the ListOfOutputs by id.
 */
const Output*
ListOfOutputs::getBySpecies(const std::string& sid) const
{
  vector<SBase*>::const_iterator result;

  result = find_if( mItems.begin(), mItems.end(), IdEqQS(sid) );
  return (result == mItems.end()) ? 0 : static_cast <Output*> (*result);
}


/*
 * Removes the nth Output from this ListOfOutputs
 */
Output*
ListOfOutputs::remove(unsigned int n)
{
  return static_cast<Output*>(ListOf::remove(n));
}


/*
 * Removes the Output from this ListOfOutputs with the given identifier
 */
Output*
ListOfOutputs::remove(const std::string& sid)
{
  SBase* item = NULL;
  vector<SBase*>::iterator result;

  result = find_if( mItems.begin(), mItems.end(), IdEq<Output>(sid) );

  if (result != mItems.end())
  {
    item = *result;
    mItems.erase(result);
  }

  return static_cast <Output*> (item);
}


/*
 * Returns the XML element name of this object
 */
const std::string&
ListOfOutputs::getElementName () const
{
  static const string name = "listOfOutputs";
  return name;
}


/*
 * Returns the libSBML type code for the objects in this LIST_OF.
 */
int
ListOfOutputs::getItemTypeCode () const
{
  return SBML_QUAL_OUTPUT;
}


  /** @cond doxygenLibsbmlInternal */

/*
 * Creates a new Output in this ListOfOutputs
 */
SBase*
ListOfOutputs::createObject(XMLInputStream& stream)
{
  const std::string& name   = stream.peek().getName();
  SBase* object = NULL;

  if (name == "output")
  {
    QUAL_CREATE_NS(qualns, getSBMLNamespaces());
    object = new Output(qualns);
    appendAndOwn(object);
    delete qualns;
  }

  return object;
}


  /** @endcond */


  /** @cond doxygenLibsbmlInternal */

/*
 * Write the namespace for the Qual package.
 */
void
ListOfOutputs::writeXMLNS(XMLOutputStream& stream) const
{
  XMLNamespaces xmlns;

  std::string prefix = getPrefix();

  if (prefix.empty())
  {
    XMLNamespaces* thisxmlns = getNamespaces();
    if (thisxmlns && thisxmlns->hasURI(QualExtension::getXmlnsL3V1V1()))
    {
      xmlns.add(QualExtension::getXmlnsL3V1V1(),prefix);
    }
  }

  stream << xmlns;
}


  /** @endcond */


#endif /* __cplusplus */  
/** @cond doxygenIgnored */

LIBSBML_EXTERN
Output_t *
Output_create(unsigned int level, unsigned int version,
              unsigned int pkgVersion)
{
  return new Output(level, version, pkgVersion);
}


LIBSBML_EXTERN
void
Output_free(Output_t * o)
{
  if (o != NULL)
    delete o;
}


LIBSBML_EXTERN
Output_t *
Output_clone(Output_t * o)
{
  if (o != NULL)
  {
    return static_cast<Output_t*>(o->clone());
  }
  else
  {
    return NULL;
  }
}


LIBSBML_EXTERN
char *
Output_getId(Output_t * o)
{
  if (o == NULL)
    return NULL;

  return o->getId().empty() ? NULL : safe_strdup(o->getId().c_str());
}


LIBSBML_EXTERN
char *
Output_getQualitativeSpecies(Output_t * o)
{
  if (o == NULL)
    return NULL;

  return o->getQualitativeSpecies().empty() ? NULL : safe_strdup(o->getQualitativeSpecies().c_str());
}


LIBSBML_EXTERN
OutputTransitionEffect_t
Output_getTransitionEffect(Output_t * o)
{
  if (o == NULL)
    return OUTPUT_TRANSITION_EFFECT_UNKNOWN;

  return o->getTransitionEffect();
}


LIBSBML_EXTERN
char *
Output_getName(Output_t * o)
{
  if (o == NULL)
    return NULL;

  return o->getName().empty() ? NULL : safe_strdup(o->getName().c_str());
}


LIBSBML_EXTERN
int
Output_getOutputLevel(Output_t * o)
{
  return (o != NULL) ? o->getOutputLevel() : SBML_INT_MAX;
}


LIBSBML_EXTERN
int
Output_isSetId(Output_t * o)
{
  return (o != NULL) ? static_cast<int>(o->isSetId()) : 0;
}


LIBSBML_EXTERN
int
Output_isSetQualitativeSpecies(Output_t * o)
{
  return (o != NULL) ? static_cast<int>(o->isSetQualitativeSpecies()) : 0;
}


LIBSBML_EXTERN
int
Output_isSetTransitionEffect(Output_t * o)
{
  return (o != NULL) ? static_cast<int>(o->isSetTransitionEffect()) : 0;
}


LIBSBML_EXTERN
int
Output_isSetName(Output_t * o)
{
  return (o != NULL) ? static_cast<int>(o->isSetName()) : 0;
}


LIBSBML_EXTERN
int
Output_isSetOutputLevel(Output_t * o)
{
  return (o != NULL) ? static_cast<int>(o->isSetOutputLevel()) : 0;
}


LIBSBML_EXTERN
int
Output_setId(Output_t * o, const char * id)
{
  return (o != NULL) ? o->setId(id) : LIBSBML_INVALID_OBJECT;
}


LIBSBML_EXTERN
int
Output_setQualitativeSpecies(Output_t * o, const char * qualitativeSpecies)
{
  return (o != NULL) ? o->setQualitativeSpecies(qualitativeSpecies) : LIBSBML_INVALID_OBJECT;
}


LIBSBML_EXTERN
int
Output_setTransitionEffect(Output_t * o, OutputTransitionEffect_t transitionEffect)
{
  return (o != NULL) ? o->setTransitionEffect(transitionEffect) : LIBSBML_INVALID_OBJECT;
}


LIBSBML_EXTERN
int
Output_setName(Output_t * o, const char * name)
{
  return (o != NULL) ? o->setName(name) : LIBSBML_INVALID_OBJECT;
}


LIBSBML_EXTERN
int
Output_setOutputLevel(Output_t * o, int outputLevel)
{
  return (o != NULL) ? o->setOutputLevel(outputLevel) : LIBSBML_INVALID_OBJECT;
}


LIBSBML_EXTERN
int
Output_unsetId(Output_t * o)
{
  return (o != NULL) ? o->unsetId() : LIBSBML_INVALID_OBJECT;
}


LIBSBML_EXTERN
int
Output_unsetQualitativeSpecies(Output_t * o)
{
  return (o != NULL) ? o->unsetQualitativeSpecies() : LIBSBML_INVALID_OBJECT;
}


LIBSBML_EXTERN
int
Output_unsetTransitionEffect(Output_t * o)
{
  return (o != NULL) ? o->unsetTransitionEffect() : LIBSBML_INVALID_OBJECT;
}


LIBSBML_EXTERN
int
Output_unsetName(Output_t * o)
{
  return (o != NULL) ? o->unsetName() : LIBSBML_INVALID_OBJECT;
}


LIBSBML_EXTERN
int
Output_unsetOutputLevel(Output_t * o)
{
  return (o != NULL) ? o->unsetOutputLevel() : LIBSBML_INVALID_OBJECT;
}


LIBSBML_EXTERN
int
Output_hasRequiredAttributes(Output_t * o)
{
  return (o != NULL) ? static_cast<int>(o->hasRequiredAttributes()) : 0;
}


LIBSBML_EXTERN
Output_t *
ListOfOutputs_getById(ListOf_t * lo, const char * sid)
{
  if (lo == NULL)
    return NULL;

  return (sid != NULL) ? static_cast <ListOfOutputs *>(lo)->get(sid) : NULL;
}


LIBSBML_EXTERN
Output_t *
ListOfOutputs_removeById(ListOf_t * lo, const char * sid)
{
  if (lo == NULL)
    return NULL;

  return (sid != NULL) ? static_cast <ListOfOutputs *>(lo)->remove(sid) : NULL;
}

static
const char* OUTPUT_TRANSITION_EFFECT_STRINGS[] =
{
    "production"
  , "assignmentLevel"
  , "unknown"
};


LIBSBML_EXTERN
const char* 
OutputTransitionEffect_toString(OutputTransitionEffect_t effect)
{
  int max = OUTPUT_TRANSITION_EFFECT_UNKNOWN;

  if (effect < OUTPUT_TRANSITION_EFFECT_PRODUCTION || effect >= max)
  {
      return NULL;
  }

  return OUTPUT_TRANSITION_EFFECT_STRINGS[effect];
}


LIBSBML_EXTERN
OutputTransitionEffect_t 
OutputTransitionEffect_fromString(const char* s)
{
  if (s == NULL) 
  {
    return OUTPUT_TRANSITION_EFFECT_UNKNOWN;
  }

  int max = OUTPUT_TRANSITION_EFFECT_UNKNOWN;
  for (int i = 0; i < max; i++)
  {
    if (strcmp(OUTPUT_TRANSITION_EFFECT_STRINGS[i], s) == 0)
      return (OutputTransitionEffect_t)i;
  }
  return OUTPUT_TRANSITION_EFFECT_UNKNOWN;
}


LIBSBML_EXTERN
int 
OutputTransitionEffect_isValidOutputTransitionEffect(OutputTransitionEffect_t effect)
{
  int max = OUTPUT_TRANSITION_EFFECT_UNKNOWN;

  if (effect < OUTPUT_TRANSITION_EFFECT_PRODUCTION || effect >= max)
  {
    return 0;
  }
  else
  {
    return 1;
  }
}


LIBSBML_EXTERN
int 
OutputTransitionEffect_isValidOutputTransitionEffectString(const char* s)
{
  return OutputTransitionEffect_isValidOutputTransitionEffect
                                         (OutputTransitionEffect_fromString(s));
}


/** @endcond */
LIBSBML_CPP_NAMESPACE_END


