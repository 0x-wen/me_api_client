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

class CosmwasmWasmV1MsgStoreCodeResponse(object):
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
        'code_id': 'str',
        'checksum': 'str'
    }

    attribute_map = {
        'code_id': 'code_id',
        'checksum': 'checksum'
    }

    def __init__(self, code_id=None, checksum=None):  # noqa: E501
        """CosmwasmWasmV1MsgStoreCodeResponse - a model defined in Swagger"""  # noqa: E501
        self._code_id = None
        self._checksum = None
        self.discriminator = None
        if code_id is not None:
            self.code_id = code_id
        if checksum is not None:
            self.checksum = checksum

    @property
    def code_id(self):
        """Gets the code_id of this CosmwasmWasmV1MsgStoreCodeResponse.  # noqa: E501


        :return: The code_id of this CosmwasmWasmV1MsgStoreCodeResponse.  # noqa: E501
        :rtype: str
        """
        return self._code_id

    @code_id.setter
    def code_id(self, code_id):
        """Sets the code_id of this CosmwasmWasmV1MsgStoreCodeResponse.


        :param code_id: The code_id of this CosmwasmWasmV1MsgStoreCodeResponse.  # noqa: E501
        :type: str
        """

        self._code_id = code_id

    @property
    def checksum(self):
        """Gets the checksum of this CosmwasmWasmV1MsgStoreCodeResponse.  # noqa: E501


        :return: The checksum of this CosmwasmWasmV1MsgStoreCodeResponse.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this CosmwasmWasmV1MsgStoreCodeResponse.


        :param checksum: The checksum of this CosmwasmWasmV1MsgStoreCodeResponse.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

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
        if issubclass(CosmwasmWasmV1MsgStoreCodeResponse, dict):
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
        if not isinstance(other, CosmwasmWasmV1MsgStoreCodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
