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

class IbcCoreConnectionV1IdentifiedConnectionCounterparty(object):
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
        'client_id': 'str',
        'connection_id': 'str',
        'prefix': 'MerklePrefixIsMerklePathPrefixedToTheKeyTheConstructedKeyFromThePathAndTheKeyWillBeAppendPathKeyPathappendPathKeyPrefixKey_'
    }

    attribute_map = {
        'client_id': 'client_id',
        'connection_id': 'connection_id',
        'prefix': 'prefix'
    }

    def __init__(self, client_id=None, connection_id=None, prefix=None):  # noqa: E501
        """IbcCoreConnectionV1IdentifiedConnectionCounterparty - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._connection_id = None
        self._prefix = None
        self.discriminator = None
        if client_id is not None:
            self.client_id = client_id
        if connection_id is not None:
            self.connection_id = connection_id
        if prefix is not None:
            self.prefix = prefix

    @property
    def client_id(self):
        """Gets the client_id of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.  # noqa: E501

        identifies the client on the counterparty chain associated with a given connection.  # noqa: E501

        :return: The client_id of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.

        identifies the client on the counterparty chain associated with a given connection.  # noqa: E501

        :param client_id: The client_id of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def connection_id(self):
        """Gets the connection_id of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.  # noqa: E501

        identifies the connection end on the counterparty chain associated with a given connection.  # noqa: E501

        :return: The connection_id of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.

        identifies the connection end on the counterparty chain associated with a given connection.  # noqa: E501

        :param connection_id: The connection_id of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def prefix(self):
        """Gets the prefix of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.  # noqa: E501


        :return: The prefix of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.  # noqa: E501
        :rtype: MerklePrefixIsMerklePathPrefixedToTheKeyTheConstructedKeyFromThePathAndTheKeyWillBeAppendPathKeyPathappendPathKeyPrefixKey_
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.


        :param prefix: The prefix of this IbcCoreConnectionV1IdentifiedConnectionCounterparty.  # noqa: E501
        :type: MerklePrefixIsMerklePathPrefixedToTheKeyTheConstructedKeyFromThePathAndTheKeyWillBeAppendPathKeyPathappendPathKeyPrefixKey_
        """

        self._prefix = prefix

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
        if issubclass(IbcCoreConnectionV1IdentifiedConnectionCounterparty, dict):
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
        if not isinstance(other, IbcCoreConnectionV1IdentifiedConnectionCounterparty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
