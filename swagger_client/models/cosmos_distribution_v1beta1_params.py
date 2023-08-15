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

class CosmosDistributionV1beta1Params(object):
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
        'community_tax': 'str',
        'base_proposer_reward': 'str',
        'bonus_proposer_reward': 'str',
        'withdraw_addr_enabled': 'bool'
    }

    attribute_map = {
        'community_tax': 'community_tax',
        'base_proposer_reward': 'base_proposer_reward',
        'bonus_proposer_reward': 'bonus_proposer_reward',
        'withdraw_addr_enabled': 'withdraw_addr_enabled'
    }

    def __init__(self, community_tax=None, base_proposer_reward=None, bonus_proposer_reward=None, withdraw_addr_enabled=None):  # noqa: E501
        """CosmosDistributionV1beta1Params - a model defined in Swagger"""  # noqa: E501
        self._community_tax = None
        self._base_proposer_reward = None
        self._bonus_proposer_reward = None
        self._withdraw_addr_enabled = None
        self.discriminator = None
        if community_tax is not None:
            self.community_tax = community_tax
        if base_proposer_reward is not None:
            self.base_proposer_reward = base_proposer_reward
        if bonus_proposer_reward is not None:
            self.bonus_proposer_reward = bonus_proposer_reward
        if withdraw_addr_enabled is not None:
            self.withdraw_addr_enabled = withdraw_addr_enabled

    @property
    def community_tax(self):
        """Gets the community_tax of this CosmosDistributionV1beta1Params.  # noqa: E501


        :return: The community_tax of this CosmosDistributionV1beta1Params.  # noqa: E501
        :rtype: str
        """
        return self._community_tax

    @community_tax.setter
    def community_tax(self, community_tax):
        """Sets the community_tax of this CosmosDistributionV1beta1Params.


        :param community_tax: The community_tax of this CosmosDistributionV1beta1Params.  # noqa: E501
        :type: str
        """

        self._community_tax = community_tax

    @property
    def base_proposer_reward(self):
        """Gets the base_proposer_reward of this CosmosDistributionV1beta1Params.  # noqa: E501


        :return: The base_proposer_reward of this CosmosDistributionV1beta1Params.  # noqa: E501
        :rtype: str
        """
        return self._base_proposer_reward

    @base_proposer_reward.setter
    def base_proposer_reward(self, base_proposer_reward):
        """Sets the base_proposer_reward of this CosmosDistributionV1beta1Params.


        :param base_proposer_reward: The base_proposer_reward of this CosmosDistributionV1beta1Params.  # noqa: E501
        :type: str
        """

        self._base_proposer_reward = base_proposer_reward

    @property
    def bonus_proposer_reward(self):
        """Gets the bonus_proposer_reward of this CosmosDistributionV1beta1Params.  # noqa: E501


        :return: The bonus_proposer_reward of this CosmosDistributionV1beta1Params.  # noqa: E501
        :rtype: str
        """
        return self._bonus_proposer_reward

    @bonus_proposer_reward.setter
    def bonus_proposer_reward(self, bonus_proposer_reward):
        """Sets the bonus_proposer_reward of this CosmosDistributionV1beta1Params.


        :param bonus_proposer_reward: The bonus_proposer_reward of this CosmosDistributionV1beta1Params.  # noqa: E501
        :type: str
        """

        self._bonus_proposer_reward = bonus_proposer_reward

    @property
    def withdraw_addr_enabled(self):
        """Gets the withdraw_addr_enabled of this CosmosDistributionV1beta1Params.  # noqa: E501


        :return: The withdraw_addr_enabled of this CosmosDistributionV1beta1Params.  # noqa: E501
        :rtype: bool
        """
        return self._withdraw_addr_enabled

    @withdraw_addr_enabled.setter
    def withdraw_addr_enabled(self, withdraw_addr_enabled):
        """Sets the withdraw_addr_enabled of this CosmosDistributionV1beta1Params.


        :param withdraw_addr_enabled: The withdraw_addr_enabled of this CosmosDistributionV1beta1Params.  # noqa: E501
        :type: bool
        """

        self._withdraw_addr_enabled = withdraw_addr_enabled

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
        if issubclass(CosmosDistributionV1beta1Params, dict):
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
        if not isinstance(other, CosmosDistributionV1beta1Params):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other