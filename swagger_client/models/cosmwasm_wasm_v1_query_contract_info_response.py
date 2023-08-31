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

class CosmwasmWasmV1QueryContractInfoResponse(object):
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
        'address': 'str',
        'contract_info': 'ContractInfoStoresAWASMContractInstance'
    }

    attribute_map = {
        'address': 'address',
        'contract_info': 'contract_info'
    }

    def __init__(self, address=None, contract_info=None):  # noqa: E501
        """CosmwasmWasmV1QueryContractInfoResponse - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._contract_info = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if contract_info is not None:
            self.contract_info = contract_info

    @property
    def address(self):
        """Gets the address of this CosmwasmWasmV1QueryContractInfoResponse.  # noqa: E501


        :return: The address of this CosmwasmWasmV1QueryContractInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CosmwasmWasmV1QueryContractInfoResponse.


        :param address: The address of this CosmwasmWasmV1QueryContractInfoResponse.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def contract_info(self):
        """Gets the contract_info of this CosmwasmWasmV1QueryContractInfoResponse.  # noqa: E501


        :return: The contract_info of this CosmwasmWasmV1QueryContractInfoResponse.  # noqa: E501
        :rtype: ContractInfoStoresAWASMContractInstance
        """
        return self._contract_info

    @contract_info.setter
    def contract_info(self, contract_info):
        """Sets the contract_info of this CosmwasmWasmV1QueryContractInfoResponse.


        :param contract_info: The contract_info of this CosmwasmWasmV1QueryContractInfoResponse.  # noqa: E501
        :type: ContractInfoStoresAWASMContractInstance
        """

        self._contract_info = contract_info

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
        if issubclass(CosmwasmWasmV1QueryContractInfoResponse, dict):
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
        if not isinstance(other, CosmwasmWasmV1QueryContractInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
