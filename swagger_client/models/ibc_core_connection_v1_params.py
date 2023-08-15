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

class IbcCoreConnectionV1Params(object):
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
        'max_expected_time_per_block': 'str'
    }

    attribute_map = {
        'max_expected_time_per_block': 'max_expected_time_per_block'
    }

    def __init__(self, max_expected_time_per_block=None):  # noqa: E501
        """IbcCoreConnectionV1Params - a model defined in Swagger"""  # noqa: E501
        self._max_expected_time_per_block = None
        self.discriminator = None
        if max_expected_time_per_block is not None:
            self.max_expected_time_per_block = max_expected_time_per_block

    @property
    def max_expected_time_per_block(self):
        """Gets the max_expected_time_per_block of this IbcCoreConnectionV1Params.  # noqa: E501

        maximum expected time per block (in nanoseconds), used to enforce block delay. This parameter should reflect the largest amount of time that the chain might reasonably take to produce the next block under normal operating conditions. A safe choice is 3-5x the expected time per block.  # noqa: E501

        :return: The max_expected_time_per_block of this IbcCoreConnectionV1Params.  # noqa: E501
        :rtype: str
        """
        return self._max_expected_time_per_block

    @max_expected_time_per_block.setter
    def max_expected_time_per_block(self, max_expected_time_per_block):
        """Sets the max_expected_time_per_block of this IbcCoreConnectionV1Params.

        maximum expected time per block (in nanoseconds), used to enforce block delay. This parameter should reflect the largest amount of time that the chain might reasonably take to produce the next block under normal operating conditions. A safe choice is 3-5x the expected time per block.  # noqa: E501

        :param max_expected_time_per_block: The max_expected_time_per_block of this IbcCoreConnectionV1Params.  # noqa: E501
        :type: str
        """

        self._max_expected_time_per_block = max_expected_time_per_block

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
        if issubclass(IbcCoreConnectionV1Params, dict):
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
        if not isinstance(other, IbcCoreConnectionV1Params):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
