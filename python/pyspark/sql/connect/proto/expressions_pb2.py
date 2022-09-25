#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/expressions.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyspark.sql.connect.proto import types_pb2 as spark_dot_connect_dot_types__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1fspark/connect/expressions.proto\x12\rspark.connect\x1a\x19spark/connect/types.proto\x1a\x19google/protobuf/any.proto"\xd8\x14\n\nExpression\x12=\n\x07literal\x18\x01 \x01(\x0b\x32!.spark.connect.Expression.LiteralH\x00R\x07literal\x12\x62\n\x14unresolved_attribute\x18\x02 \x01(\x0b\x32-.spark.connect.Expression.UnresolvedAttributeH\x00R\x13unresolvedAttribute\x12_\n\x13unresolved_function\x18\x03 \x01(\x0b\x32,.spark.connect.Expression.UnresolvedFunctionH\x00R\x12unresolvedFunction\x12Y\n\x11\x65xpression_string\x18\x04 \x01(\x0b\x32*.spark.connect.Expression.ExpressionStringH\x00R\x10\x65xpressionString\x1a\x97\x10\n\x07Literal\x12\x1a\n\x07\x62oolean\x18\x01 \x01(\x08H\x00R\x07\x62oolean\x12\x10\n\x02i8\x18\x02 \x01(\x05H\x00R\x02i8\x12\x12\n\x03i16\x18\x03 \x01(\x05H\x00R\x03i16\x12\x12\n\x03i32\x18\x05 \x01(\x05H\x00R\x03i32\x12\x12\n\x03i64\x18\x07 \x01(\x03H\x00R\x03i64\x12\x14\n\x04\x66p32\x18\n \x01(\x02H\x00R\x04\x66p32\x12\x14\n\x04\x66p64\x18\x0b \x01(\x01H\x00R\x04\x66p64\x12\x18\n\x06string\x18\x0c \x01(\tH\x00R\x06string\x12\x18\n\x06\x62inary\x18\r \x01(\x0cH\x00R\x06\x62inary\x12\x1e\n\ttimestamp\x18\x0e \x01(\x03H\x00R\ttimestamp\x12\x14\n\x04\x64\x61te\x18\x10 \x01(\x05H\x00R\x04\x64\x61te\x12\x14\n\x04time\x18\x11 \x01(\x03H\x00R\x04time\x12l\n\x16interval_year_to_month\x18\x13 \x01(\x0b\x32\x35.spark.connect.Expression.Literal.IntervalYearToMonthH\x00R\x13intervalYearToMonth\x12l\n\x16interval_day_to_second\x18\x14 \x01(\x0b\x32\x35.spark.connect.Expression.Literal.IntervalDayToSecondH\x00R\x13intervalDayToSecond\x12\x1f\n\nfixed_char\x18\x15 \x01(\tH\x00R\tfixedChar\x12\x46\n\x08var_char\x18\x16 \x01(\x0b\x32).spark.connect.Expression.Literal.VarCharH\x00R\x07varChar\x12#\n\x0c\x66ixed_binary\x18\x17 \x01(\x0cH\x00R\x0b\x66ixedBinary\x12\x45\n\x07\x64\x65\x63imal\x18\x18 \x01(\x0b\x32).spark.connect.Expression.Literal.DecimalH\x00R\x07\x64\x65\x63imal\x12\x42\n\x06struct\x18\x19 \x01(\x0b\x32(.spark.connect.Expression.Literal.StructH\x00R\x06struct\x12\x39\n\x03map\x18\x1a \x01(\x0b\x32%.spark.connect.Expression.Literal.MapH\x00R\x03map\x12#\n\x0ctimestamp_tz\x18\x1b \x01(\x03H\x00R\x0btimestampTz\x12\x14\n\x04uuid\x18\x1c \x01(\x0cH\x00R\x04uuid\x12)\n\x04null\x18\x1d \x01(\x0b\x32\x13.spark.connect.TypeH\x00R\x04null\x12<\n\x04list\x18\x1e \x01(\x0b\x32&.spark.connect.Expression.Literal.ListH\x00R\x04list\x12\x39\n\nempty_list\x18\x1f \x01(\x0b\x32\x18.spark.connect.Type.ListH\x00R\temptyList\x12\x36\n\tempty_map\x18  \x01(\x0b\x32\x17.spark.connect.Type.MapH\x00R\x08\x65mptyMap\x12R\n\x0cuser_defined\x18! \x01(\x0b\x32-.spark.connect.Expression.Literal.UserDefinedH\x00R\x0buserDefined\x12\x1a\n\x08nullable\x18\x32 \x01(\x08R\x08nullable\x12\x38\n\x18type_variation_reference\x18\x33 \x01(\rR\x16typeVariationReference\x1a\x37\n\x07VarChar\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12\x16\n\x06length\x18\x02 \x01(\rR\x06length\x1aS\n\x07\x44\x65\x63imal\x12\x14\n\x05value\x18\x01 \x01(\x0cR\x05value\x12\x1c\n\tprecision\x18\x02 \x01(\x05R\tprecision\x12\x14\n\x05scale\x18\x03 \x01(\x05R\x05scale\x1a\xce\x01\n\x03Map\x12M\n\nkey_values\x18\x01 \x03(\x0b\x32..spark.connect.Expression.Literal.Map.KeyValueR\tkeyValues\x1ax\n\x08KeyValue\x12\x33\n\x03key\x18\x01 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x03key\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x05value\x1a\x43\n\x13IntervalYearToMonth\x12\x14\n\x05years\x18\x01 \x01(\x05R\x05years\x12\x16\n\x06months\x18\x02 \x01(\x05R\x06months\x1ag\n\x13IntervalDayToSecond\x12\x12\n\x04\x64\x61ys\x18\x01 \x01(\x05R\x04\x64\x61ys\x12\x18\n\x07seconds\x18\x02 \x01(\x05R\x07seconds\x12"\n\x0cmicroseconds\x18\x03 \x01(\x05R\x0cmicroseconds\x1a\x43\n\x06Struct\x12\x39\n\x06\x66ields\x18\x01 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\x06\x66ields\x1a\x41\n\x04List\x12\x39\n\x06values\x18\x01 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\x06values\x1a`\n\x0bUserDefined\x12%\n\x0etype_reference\x18\x01 \x01(\rR\rtypeReference\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05valueB\x0e\n\x0cliteral_type\x1a+\n\x13UnresolvedAttribute\x12\x14\n\x05parts\x18\x01 \x03(\tR\x05parts\x1a\x63\n\x12UnresolvedFunction\x12\x14\n\x05parts\x18\x01 \x03(\tR\x05parts\x12\x37\n\targuments\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\targuments\x1a\x32\n\x10\x45xpressionString\x12\x1e\n\nexpression\x18\x01 \x01(\tR\nexpressionB\x0b\n\texpr_typeBM\n\x1eorg.apache.spark.connect.protoP\x01Z)github.com/databricks/spark-connect/protob\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "spark.connect.expressions_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\n\036org.apache.spark.connect.protoP\001Z)github.com/databricks/spark-connect/proto"
    )
    _EXPRESSION._serialized_start = 105
    _EXPRESSION._serialized_end = 2753
    _EXPRESSION_LITERAL._serialized_start = 471
    _EXPRESSION_LITERAL._serialized_end = 2542
    _EXPRESSION_LITERAL_VARCHAR._serialized_start = 1769
    _EXPRESSION_LITERAL_VARCHAR._serialized_end = 1824
    _EXPRESSION_LITERAL_DECIMAL._serialized_start = 1826
    _EXPRESSION_LITERAL_DECIMAL._serialized_end = 1909
    _EXPRESSION_LITERAL_MAP._serialized_start = 1912
    _EXPRESSION_LITERAL_MAP._serialized_end = 2118
    _EXPRESSION_LITERAL_MAP_KEYVALUE._serialized_start = 1998
    _EXPRESSION_LITERAL_MAP_KEYVALUE._serialized_end = 2118
    _EXPRESSION_LITERAL_INTERVALYEARTOMONTH._serialized_start = 2120
    _EXPRESSION_LITERAL_INTERVALYEARTOMONTH._serialized_end = 2187
    _EXPRESSION_LITERAL_INTERVALDAYTOSECOND._serialized_start = 2189
    _EXPRESSION_LITERAL_INTERVALDAYTOSECOND._serialized_end = 2292
    _EXPRESSION_LITERAL_STRUCT._serialized_start = 2294
    _EXPRESSION_LITERAL_STRUCT._serialized_end = 2361
    _EXPRESSION_LITERAL_LIST._serialized_start = 2363
    _EXPRESSION_LITERAL_LIST._serialized_end = 2428
    _EXPRESSION_LITERAL_USERDEFINED._serialized_start = 2430
    _EXPRESSION_LITERAL_USERDEFINED._serialized_end = 2526
    _EXPRESSION_UNRESOLVEDATTRIBUTE._serialized_start = 2544
    _EXPRESSION_UNRESOLVEDATTRIBUTE._serialized_end = 2587
    _EXPRESSION_UNRESOLVEDFUNCTION._serialized_start = 2589
    _EXPRESSION_UNRESOLVEDFUNCTION._serialized_end = 2688
    _EXPRESSION_EXPRESSIONSTRING._serialized_start = 2690
    _EXPRESSION_EXPRESSIONSTRING._serialized_end = 2740
# @@protoc_insertion_point(module_scope)
