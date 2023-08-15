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

class InlineResponse2002(object):
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
        'bech32_prefix': 'str'
    }

    attribute_map = {
        'bech32_prefix': 'bech32_prefix'
    }

    def __init__(self, bech32_prefix=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501
        self._bech32_prefix = None
        self.discriminator = None
        if bech32_prefix is not None:
            self.bech32_prefix = bech32_prefix

    @property
    def bech32_prefix(self):
        """Gets the bech32_prefix of this InlineResponse2002.  # noqa: E501


        :return: The bech32_prefix of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._bech32_prefix

    @bech32_prefix.setter
    def bech32_prefix(self, bech32_prefix):
        """Sets the bech32_prefix of this InlineResponse2002.


        :param bech32_prefix: The bech32_prefix of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._bech32_prefix = bech32_prefix

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
        if issubclass(InlineResponse2002, dict):
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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
