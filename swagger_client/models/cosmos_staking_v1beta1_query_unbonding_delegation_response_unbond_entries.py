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

class CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries(object):
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
        'creation_height': 'str',
        'completion_time': 'datetime',
        'initial_balance': 'str',
        'balance': 'str'
    }

    attribute_map = {
        'creation_height': 'creation_height',
        'completion_time': 'completion_time',
        'initial_balance': 'initial_balance',
        'balance': 'balance'
    }

    def __init__(self, creation_height=None, completion_time=None, initial_balance=None, balance=None):  # noqa: E501
        """CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries - a model defined in Swagger"""  # noqa: E501
        self._creation_height = None
        self._completion_time = None
        self._initial_balance = None
        self._balance = None
        self.discriminator = None
        if creation_height is not None:
            self.creation_height = creation_height
        if completion_time is not None:
            self.completion_time = completion_time
        if initial_balance is not None:
            self.initial_balance = initial_balance
        if balance is not None:
            self.balance = balance

    @property
    def creation_height(self):
        """Gets the creation_height of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501

        creation_height is the height which the unbonding took place.  # noqa: E501

        :return: The creation_height of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501
        :rtype: str
        """
        return self._creation_height

    @creation_height.setter
    def creation_height(self, creation_height):
        """Sets the creation_height of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.

        creation_height is the height which the unbonding took place.  # noqa: E501

        :param creation_height: The creation_height of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501
        :type: str
        """

        self._creation_height = creation_height

    @property
    def completion_time(self):
        """Gets the completion_time of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501

        completion_time is the unix time for unbonding completion.  # noqa: E501

        :return: The completion_time of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501
        :rtype: datetime
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.

        completion_time is the unix time for unbonding completion.  # noqa: E501

        :param completion_time: The completion_time of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501
        :type: datetime
        """

        self._completion_time = completion_time

    @property
    def initial_balance(self):
        """Gets the initial_balance of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501

        initial_balance defines the tokens initially scheduled to receive at completion.  # noqa: E501

        :return: The initial_balance of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501
        :rtype: str
        """
        return self._initial_balance

    @initial_balance.setter
    def initial_balance(self, initial_balance):
        """Sets the initial_balance of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.

        initial_balance defines the tokens initially scheduled to receive at completion.  # noqa: E501

        :param initial_balance: The initial_balance of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501
        :type: str
        """

        self._initial_balance = initial_balance

    @property
    def balance(self):
        """Gets the balance of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501

        balance defines the tokens to receive at completion.  # noqa: E501

        :return: The balance of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.

        balance defines the tokens to receive at completion.  # noqa: E501

        :param balance: The balance of this CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries.  # noqa: E501
        :type: str
        """

        self._balance = balance

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
        if issubclass(CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries, dict):
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
        if not isinstance(other, CosmosStakingV1beta1QueryUnbondingDelegationResponseUnbondEntries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
