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

class CosmosStakingV1beta1CommissionCommissionRates(object):
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
        'rate': 'str',
        'max_rate': 'str',
        'max_change_rate': 'str'
    }

    attribute_map = {
        'rate': 'rate',
        'max_rate': 'max_rate',
        'max_change_rate': 'max_change_rate'
    }

    def __init__(self, rate=None, max_rate=None, max_change_rate=None):  # noqa: E501
        """CosmosStakingV1beta1CommissionCommissionRates - a model defined in Swagger"""  # noqa: E501
        self._rate = None
        self._max_rate = None
        self._max_change_rate = None
        self.discriminator = None
        if rate is not None:
            self.rate = rate
        if max_rate is not None:
            self.max_rate = max_rate
        if max_change_rate is not None:
            self.max_change_rate = max_change_rate

    @property
    def rate(self):
        """Gets the rate of this CosmosStakingV1beta1CommissionCommissionRates.  # noqa: E501

        rate is the commission rate charged to delegators, as a fraction.  # noqa: E501

        :return: The rate of this CosmosStakingV1beta1CommissionCommissionRates.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this CosmosStakingV1beta1CommissionCommissionRates.

        rate is the commission rate charged to delegators, as a fraction.  # noqa: E501

        :param rate: The rate of this CosmosStakingV1beta1CommissionCommissionRates.  # noqa: E501
        :type: str
        """

        self._rate = rate

    @property
    def max_rate(self):
        """Gets the max_rate of this CosmosStakingV1beta1CommissionCommissionRates.  # noqa: E501

        max_rate defines the maximum commission rate which validator can ever charge, as a fraction.  # noqa: E501

        :return: The max_rate of this CosmosStakingV1beta1CommissionCommissionRates.  # noqa: E501
        :rtype: str
        """
        return self._max_rate

    @max_rate.setter
    def max_rate(self, max_rate):
        """Sets the max_rate of this CosmosStakingV1beta1CommissionCommissionRates.

        max_rate defines the maximum commission rate which validator can ever charge, as a fraction.  # noqa: E501

        :param max_rate: The max_rate of this CosmosStakingV1beta1CommissionCommissionRates.  # noqa: E501
        :type: str
        """

        self._max_rate = max_rate

    @property
    def max_change_rate(self):
        """Gets the max_change_rate of this CosmosStakingV1beta1CommissionCommissionRates.  # noqa: E501

        max_change_rate defines the maximum daily increase of the validator commission, as a fraction.  # noqa: E501

        :return: The max_change_rate of this CosmosStakingV1beta1CommissionCommissionRates.  # noqa: E501
        :rtype: str
        """
        return self._max_change_rate

    @max_change_rate.setter
    def max_change_rate(self, max_change_rate):
        """Sets the max_change_rate of this CosmosStakingV1beta1CommissionCommissionRates.

        max_change_rate defines the maximum daily increase of the validator commission, as a fraction.  # noqa: E501

        :param max_change_rate: The max_change_rate of this CosmosStakingV1beta1CommissionCommissionRates.  # noqa: E501
        :type: str
        """

        self._max_change_rate = max_change_rate

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
        if issubclass(CosmosStakingV1beta1CommissionCommissionRates, dict):
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
        if not isinstance(other, CosmosStakingV1beta1CommissionCommissionRates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
