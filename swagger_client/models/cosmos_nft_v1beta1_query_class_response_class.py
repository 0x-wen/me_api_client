# coding: utf-8

"""
    HTTP API Console

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CosmosNftV1beta1QueryClassResponseClass(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'symbol': 'str',
        'description': 'str',
        'uri': 'str',
        'uri_hash': 'str',
        'data': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'symbol': 'symbol',
        'description': 'description',
        'uri': 'uri',
        'uri_hash': 'uri_hash',
        'data': 'data'
    }

    def __init__(self, id=None, name=None, symbol=None, description=None, uri=None, uri_hash=None, data=None):  # noqa: E501
        """CosmosNftV1beta1QueryClassResponseClass - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._symbol = None
        self._description = None
        self._uri = None
        self._uri_hash = None
        self._data = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if symbol is not None:
            self.symbol = symbol
        if description is not None:
            self.description = description
        if uri is not None:
            self.uri = uri
        if uri_hash is not None:
            self.uri_hash = uri_hash
        if data is not None:
            self.data = data

    @property
    def id(self):
        """Gets the id of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501


        :return: The id of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CosmosNftV1beta1QueryClassResponseClass.


        :param id: The id of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501


        :return: The name of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CosmosNftV1beta1QueryClassResponseClass.


        :param name: The name of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def symbol(self):
        """Gets the symbol of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501


        :return: The symbol of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this CosmosNftV1beta1QueryClassResponseClass.


        :param symbol: The symbol of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def description(self):
        """Gets the description of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501


        :return: The description of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CosmosNftV1beta1QueryClassResponseClass.


        :param description: The description of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def uri(self):
        """Gets the uri of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501


        :return: The uri of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this CosmosNftV1beta1QueryClassResponseClass.


        :param uri: The uri of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def uri_hash(self):
        """Gets the uri_hash of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501


        :return: The uri_hash of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :rtype: str
        """
        return self._uri_hash

    @uri_hash.setter
    def uri_hash(self, uri_hash):
        """Sets the uri_hash of this CosmosNftV1beta1QueryClassResponseClass.


        :param uri_hash: The uri_hash of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :type: str
        """

        self._uri_hash = uri_hash

    @property
    def data(self):
        """Gets the data of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501

        `Any` contains an arbitrary serialized protocol buffer message along with a URL that describes the type of the serialized message.  Protobuf library provides support to pack/unpack Any values in the form of utility functions or additional generated methods of the Any type.  Example 1: Pack and unpack a message in C++.      Foo foo = ...;     Any any;     any.PackFrom(foo);     ...     if (any.UnpackTo(&foo)) {       ...     }  Example 2: Pack and unpack a message in Java.      Foo foo = ...;     Any any = Any.pack(foo);     ...     if (any.is(Foo.class)) {       foo = any.unpack(Foo.class);     }   Example 3: Pack and unpack a message in Python.      foo = Foo(...)     any = Any()     any.Pack(foo)     ...     if any.Is(Foo.DESCRIPTOR):       any.Unpack(foo)       ...   Example 4: Pack and unpack a message in Go       foo := &pb.Foo{...}      any, err := anypb.New(foo)      if err != nil {        ...      }      ...      foo := &pb.Foo{}      if err := any.UnmarshalTo(foo); err != nil {        ...      }  The pack methods provided by protobuf library will by default use 'type.googleapis.com/full.type.name' as the type URL and the unpack methods only use the fully qualified type name after the last '/' in the type URL, for example \"foo.bar.com/x/y.z\" will yield type name \"y.z\".   JSON ==== The JSON representation of an `Any` value uses the regular representation of the deserialized, embedded message, with an additional field `@type` which contains the type URL. Example:      package google.profile;     message Person {       string first_name = 1;       string last_name = 2;     }      {       \"@type\": \"type.googleapis.com/google.profile.Person\",       \"firstName\": <string>,       \"lastName\": <string>     }  If the embedded message type is well-known and has a custom JSON representation, that representation will be embedded adding a field `value` which holds the custom JSON in addition to the `@type` field. Example (for message [google.protobuf.Duration][]):      {       \"@type\": \"type.googleapis.com/google.protobuf.Duration\",       \"value\": \"1.212s\"     }  # noqa: E501

        :return: The data of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CosmosNftV1beta1QueryClassResponseClass.

        `Any` contains an arbitrary serialized protocol buffer message along with a URL that describes the type of the serialized message.  Protobuf library provides support to pack/unpack Any values in the form of utility functions or additional generated methods of the Any type.  Example 1: Pack and unpack a message in C++.      Foo foo = ...;     Any any;     any.PackFrom(foo);     ...     if (any.UnpackTo(&foo)) {       ...     }  Example 2: Pack and unpack a message in Java.      Foo foo = ...;     Any any = Any.pack(foo);     ...     if (any.is(Foo.class)) {       foo = any.unpack(Foo.class);     }   Example 3: Pack and unpack a message in Python.      foo = Foo(...)     any = Any()     any.Pack(foo)     ...     if any.Is(Foo.DESCRIPTOR):       any.Unpack(foo)       ...   Example 4: Pack and unpack a message in Go       foo := &pb.Foo{...}      any, err := anypb.New(foo)      if err != nil {        ...      }      ...      foo := &pb.Foo{}      if err := any.UnmarshalTo(foo); err != nil {        ...      }  The pack methods provided by protobuf library will by default use 'type.googleapis.com/full.type.name' as the type URL and the unpack methods only use the fully qualified type name after the last '/' in the type URL, for example \"foo.bar.com/x/y.z\" will yield type name \"y.z\".   JSON ==== The JSON representation of an `Any` value uses the regular representation of the deserialized, embedded message, with an additional field `@type` which contains the type URL. Example:      package google.profile;     message Person {       string first_name = 1;       string last_name = 2;     }      {       \"@type\": \"type.googleapis.com/google.profile.Person\",       \"firstName\": <string>,       \"lastName\": <string>     }  If the embedded message type is well-known and has a custom JSON representation, that representation will be embedded adding a field `value` which holds the custom JSON in addition to the `@type` field. Example (for message [google.protobuf.Duration][]):      {       \"@type\": \"type.googleapis.com/google.protobuf.Duration\",       \"value\": \"1.212s\"     }  # noqa: E501

        :param data: The data of this CosmosNftV1beta1QueryClassResponseClass.  # noqa: E501
        :type: dict(str, object)
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CosmosNftV1beta1QueryClassResponseClass, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CosmosNftV1beta1QueryClassResponseClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
