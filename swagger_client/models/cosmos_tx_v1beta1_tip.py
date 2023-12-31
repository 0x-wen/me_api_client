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

class CosmosTxV1beta1Tip(object):
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
        'amount': 'list[CosmosBankV1beta1InputCoins]',
        'tipper': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'tipper': 'tipper'
    }

    def __init__(self, amount=None, tipper=None):  # noqa: E501
        """CosmosTxV1beta1Tip - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._tipper = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if tipper is not None:
            self.tipper = tipper

    @property
    def amount(self):
        """Gets the amount of this CosmosTxV1beta1Tip.  # noqa: E501


        :return: The amount of this CosmosTxV1beta1Tip.  # noqa: E501
        :rtype: list[CosmosBankV1beta1InputCoins]
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CosmosTxV1beta1Tip.


        :param amount: The amount of this CosmosTxV1beta1Tip.  # noqa: E501
        :type: list[CosmosBankV1beta1InputCoins]
        """

        self._amount = amount

    @property
    def tipper(self):
        """Gets the tipper of this CosmosTxV1beta1Tip.  # noqa: E501


        :return: The tipper of this CosmosTxV1beta1Tip.  # noqa: E501
        :rtype: str
        """
        return self._tipper

    @tipper.setter
    def tipper(self, tipper):
        """Sets the tipper of this CosmosTxV1beta1Tip.


        :param tipper: The tipper of this CosmosTxV1beta1Tip.  # noqa: E501
        :type: str
        """

        self._tipper = tipper

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
        if issubclass(CosmosTxV1beta1Tip, dict):
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
        if not isinstance(other, CosmosTxV1beta1Tip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
