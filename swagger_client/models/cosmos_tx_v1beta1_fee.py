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

class CosmosTxV1beta1Fee(object):
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
        'gas_limit': 'str',
        'payer': 'str',
        'granter': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'gas_limit': 'gas_limit',
        'payer': 'payer',
        'granter': 'granter'
    }

    def __init__(self, amount=None, gas_limit=None, payer=None, granter=None):  # noqa: E501
        """CosmosTxV1beta1Fee - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._gas_limit = None
        self._payer = None
        self._granter = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if gas_limit is not None:
            self.gas_limit = gas_limit
        if payer is not None:
            self.payer = payer
        if granter is not None:
            self.granter = granter

    @property
    def amount(self):
        """Gets the amount of this CosmosTxV1beta1Fee.  # noqa: E501


        :return: The amount of this CosmosTxV1beta1Fee.  # noqa: E501
        :rtype: list[CosmosBankV1beta1InputCoins]
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CosmosTxV1beta1Fee.


        :param amount: The amount of this CosmosTxV1beta1Fee.  # noqa: E501
        :type: list[CosmosBankV1beta1InputCoins]
        """

        self._amount = amount

    @property
    def gas_limit(self):
        """Gets the gas_limit of this CosmosTxV1beta1Fee.  # noqa: E501


        :return: The gas_limit of this CosmosTxV1beta1Fee.  # noqa: E501
        :rtype: str
        """
        return self._gas_limit

    @gas_limit.setter
    def gas_limit(self, gas_limit):
        """Sets the gas_limit of this CosmosTxV1beta1Fee.


        :param gas_limit: The gas_limit of this CosmosTxV1beta1Fee.  # noqa: E501
        :type: str
        """

        self._gas_limit = gas_limit

    @property
    def payer(self):
        """Gets the payer of this CosmosTxV1beta1Fee.  # noqa: E501

        if unset, the first signer is responsible for paying the fees. If set, the specified account must pay the fees. the payer must be a tx signer (and thus have signed this field in AuthInfo). setting this field does *not* change the ordering of required signers for the transaction.  # noqa: E501

        :return: The payer of this CosmosTxV1beta1Fee.  # noqa: E501
        :rtype: str
        """
        return self._payer

    @payer.setter
    def payer(self, payer):
        """Sets the payer of this CosmosTxV1beta1Fee.

        if unset, the first signer is responsible for paying the fees. If set, the specified account must pay the fees. the payer must be a tx signer (and thus have signed this field in AuthInfo). setting this field does *not* change the ordering of required signers for the transaction.  # noqa: E501

        :param payer: The payer of this CosmosTxV1beta1Fee.  # noqa: E501
        :type: str
        """

        self._payer = payer

    @property
    def granter(self):
        """Gets the granter of this CosmosTxV1beta1Fee.  # noqa: E501


        :return: The granter of this CosmosTxV1beta1Fee.  # noqa: E501
        :rtype: str
        """
        return self._granter

    @granter.setter
    def granter(self, granter):
        """Sets the granter of this CosmosTxV1beta1Fee.


        :param granter: The granter of this CosmosTxV1beta1Fee.  # noqa: E501
        :type: str
        """

        self._granter = granter

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
        if issubclass(CosmosTxV1beta1Fee, dict):
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
        if not isinstance(other, CosmosTxV1beta1Fee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
