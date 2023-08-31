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

class CosmosTxV1beta1TxDecodeResponse(object):
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
        'tx': 'CosmosTxV1beta1Tx'
    }

    attribute_map = {
        'tx': 'tx'
    }

    def __init__(self, tx=None):  # noqa: E501
        """CosmosTxV1beta1TxDecodeResponse - a model defined in Swagger"""  # noqa: E501
        self._tx = None
        self.discriminator = None
        if tx is not None:
            self.tx = tx

    @property
    def tx(self):
        """Gets the tx of this CosmosTxV1beta1TxDecodeResponse.  # noqa: E501


        :return: The tx of this CosmosTxV1beta1TxDecodeResponse.  # noqa: E501
        :rtype: CosmosTxV1beta1Tx
        """
        return self._tx

    @tx.setter
    def tx(self, tx):
        """Sets the tx of this CosmosTxV1beta1TxDecodeResponse.


        :param tx: The tx of this CosmosTxV1beta1TxDecodeResponse.  # noqa: E501
        :type: CosmosTxV1beta1Tx
        """

        self._tx = tx

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
        if issubclass(CosmosTxV1beta1TxDecodeResponse, dict):
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
        if not isinstance(other, CosmosTxV1beta1TxDecodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
