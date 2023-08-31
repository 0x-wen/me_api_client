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

class CosmosVestingV1beta1Period(object):
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
        'length': 'str',
        'amount': 'list[CosmosBankV1beta1InputCoins]'
    }

    attribute_map = {
        'length': 'length',
        'amount': 'amount'
    }

    def __init__(self, length=None, amount=None):  # noqa: E501
        """CosmosVestingV1beta1Period - a model defined in Swagger"""  # noqa: E501
        self._length = None
        self._amount = None
        self.discriminator = None
        if length is not None:
            self.length = length
        if amount is not None:
            self.amount = amount

    @property
    def length(self):
        """Gets the length of this CosmosVestingV1beta1Period.  # noqa: E501

        Period duration in seconds.  # noqa: E501

        :return: The length of this CosmosVestingV1beta1Period.  # noqa: E501
        :rtype: str
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this CosmosVestingV1beta1Period.

        Period duration in seconds.  # noqa: E501

        :param length: The length of this CosmosVestingV1beta1Period.  # noqa: E501
        :type: str
        """

        self._length = length

    @property
    def amount(self):
        """Gets the amount of this CosmosVestingV1beta1Period.  # noqa: E501


        :return: The amount of this CosmosVestingV1beta1Period.  # noqa: E501
        :rtype: list[CosmosBankV1beta1InputCoins]
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CosmosVestingV1beta1Period.


        :param amount: The amount of this CosmosVestingV1beta1Period.  # noqa: E501
        :type: list[CosmosBankV1beta1InputCoins]
        """

        self._amount = amount

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
        if issubclass(CosmosVestingV1beta1Period, dict):
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
        if not isinstance(other, CosmosVestingV1beta1Period):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
