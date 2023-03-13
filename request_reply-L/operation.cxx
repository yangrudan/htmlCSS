// Copyright 2016 Proyectos y Sistemas de Mantenimiento SL (eProsima).
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/*!
 * @file operation.cpp
 * This source file contains the definition of the described types in the IDL file.
 *
 * This file was generated by the tool gen.
 */

#ifdef _WIN32
// Remove linker warning LNK4221 on Visual Studio
namespace {
char dummy;
}  // namespace
#endif  // _WIN32

#include "operation.h"
#include <fastcdr/Cdr.h>

#include <fastcdr/exceptions/BadParamException.h>
using namespace eprosima::fastcdr::exception;

#include <utility>


RequestType::RequestType()
{
    // m_operation com.eprosima.idl.parser.typecode.EnumTypeCode@6043cd28
    m_operation = ::ADDITION;
    // m_x com.eprosima.idl.parser.typecode.PrimitiveTypeCode@cb51256
    m_x = 0;
    // m_y com.eprosima.idl.parser.typecode.PrimitiveTypeCode@59906517
    m_y = 0;

}

RequestType::~RequestType()
{



}

RequestType::RequestType(
        const RequestType& x)
{
    m_operation = x.m_operation;
    m_x = x.m_x;
    m_y = x.m_y;
}

RequestType::RequestType(
        RequestType&& x)
{
    m_operation = x.m_operation;
    m_x = x.m_x;
    m_y = x.m_y;
}

RequestType& RequestType::operator =(
        const RequestType& x)
{

    m_operation = x.m_operation;
    m_x = x.m_x;
    m_y = x.m_y;

    return *this;
}

RequestType& RequestType::operator =(
        RequestType&& x)
{

    m_operation = x.m_operation;
    m_x = x.m_x;
    m_y = x.m_y;

    return *this;
}

bool RequestType::operator ==(
        const RequestType& x) const
{

    return (m_operation == x.m_operation && m_x == x.m_x && m_y == x.m_y);
}

bool RequestType::operator !=(
        const RequestType& x) const
{
    return !(*this == x);
}

size_t RequestType::getMaxCdrSerializedSize(
        size_t current_alignment)
{
    size_t initial_alignment = current_alignment;


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);



    return current_alignment - initial_alignment;
}

size_t RequestType::getCdrSerializedSize(
        const RequestType& data,
        size_t current_alignment)
{
    (void)data;
    size_t initial_alignment = current_alignment;


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);



    return current_alignment - initial_alignment;
}

void RequestType::serialize(
        eprosima::fastcdr::Cdr& scdr) const
{

    scdr << (uint32_t)m_operation;
    scdr << m_x;
    scdr << m_y;

}

void RequestType::deserialize(
        eprosima::fastcdr::Cdr& dcdr)
{

    {
        uint32_t enum_value = 0;
        dcdr >> enum_value;
        m_operation = (OperationType)enum_value;
    }

    dcdr >> m_x;
    dcdr >> m_y;
}

/*!
 * @brief This function sets a value in member operation
 * @param _operation New value for member operation
 */
void RequestType::operation(
        OperationType _operation)
{
    m_operation = _operation;
}

/*!
 * @brief This function returns the value of member operation
 * @return Value of member operation
 */
OperationType RequestType::operation() const
{
    return m_operation;
}

/*!
 * @brief This function returns a reference to member operation
 * @return Reference to member operation
 */
OperationType& RequestType::operation()
{
    return m_operation;
}

/*!
 * @brief This function sets a value in member x
 * @param _x New value for member x
 */
void RequestType::x(
        int32_t _x)
{
    m_x = _x;
}

/*!
 * @brief This function returns the value of member x
 * @return Value of member x
 */
int32_t RequestType::x() const
{
    return m_x;
}

/*!
 * @brief This function returns a reference to member x
 * @return Reference to member x
 */
int32_t& RequestType::x()
{
    return m_x;
}

/*!
 * @brief This function sets a value in member y
 * @param _y New value for member y
 */
void RequestType::y(
        int32_t _y)
{
    m_y = _y;
}

/*!
 * @brief This function returns the value of member y
 * @return Value of member y
 */
int32_t RequestType::y() const
{
    return m_y;
}

/*!
 * @brief This function returns a reference to member y
 * @return Reference to member y
 */
int32_t& RequestType::y()
{
    return m_y;
}


size_t RequestType::getKeyMaxCdrSerializedSize(
        size_t current_alignment)
{
    size_t current_align = current_alignment;






    return current_align;
}

bool RequestType::isKeyDefined()
{
    return false;
}

void RequestType::serializeKey(
        eprosima::fastcdr::Cdr& scdr) const
{
    (void) scdr;
       
}

ReplyType::ReplyType()
{
    // m_z com.eprosima.idl.parser.typecode.PrimitiveTypeCode@27f723
    m_z = 0;

}

ReplyType::~ReplyType()
{
}

ReplyType::ReplyType(
        const ReplyType& x)
{
    m_z = x.m_z;
}

ReplyType::ReplyType(
        ReplyType&& x)
{
    m_z = x.m_z;
}

ReplyType& ReplyType::operator =(
        const ReplyType& x)
{

    m_z = x.m_z;

    return *this;
}

ReplyType& ReplyType::operator =(
        ReplyType&& x)
{

    m_z = x.m_z;

    return *this;
}

bool ReplyType::operator ==(
        const ReplyType& x) const
{

    return (m_z == x.m_z);
}

bool ReplyType::operator !=(
        const ReplyType& x) const
{
    return !(*this == x);
}

size_t ReplyType::getMaxCdrSerializedSize(
        size_t current_alignment)
{
    size_t initial_alignment = current_alignment;


    current_alignment += 8 + eprosima::fastcdr::Cdr::alignment(current_alignment, 8);


    return current_alignment - initial_alignment;
}

size_t ReplyType::getCdrSerializedSize(
        const ReplyType& data,
        size_t current_alignment)
{
    (void)data;
    size_t initial_alignment = current_alignment;


    current_alignment += 8 + eprosima::fastcdr::Cdr::alignment(current_alignment, 8);


    return current_alignment - initial_alignment;
}

void ReplyType::serialize(
        eprosima::fastcdr::Cdr& scdr) const
{

    scdr << m_z;

}

void ReplyType::deserialize(
        eprosima::fastcdr::Cdr& dcdr)
{

    dcdr >> m_z;
}

/*!
 * @brief This function sets a value in member z
 * @param _z New value for member z
 */
void ReplyType::z(
        int64_t _z)
{
    m_z = _z;
}

/*!
 * @brief This function returns the value of member z
 * @return Value of member z
 */
int64_t ReplyType::z() const
{
    return m_z;
}

/*!
 * @brief This function returns a reference to member z
 * @return Reference to member z
 */
int64_t& ReplyType::z()
{
    return m_z;
}


size_t ReplyType::getKeyMaxCdrSerializedSize(
        size_t current_alignment)
{
    size_t current_align = current_alignment;



    return current_align;
}

bool ReplyType::isKeyDefined()
{
    return false;
}

void ReplyType::serializeKey(
        eprosima::fastcdr::Cdr& scdr) const
{
    (void) scdr;
     
}
