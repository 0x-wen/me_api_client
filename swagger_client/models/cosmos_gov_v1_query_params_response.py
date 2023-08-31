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

class CosmosGovV1QueryParamsResponse(object):
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
        'voting_params': 'CosmosGovV1QueryParamsResponseVotingParams',
        'deposit_params': 'CosmosGovV1QueryParamsResponseDepositParams',
        'tally_params': 'CosmosGovV1QueryParamsResponseTallyParams',
        'params': 'CosmosGovV1QueryParamsResponseParams'
    }

    attribute_map = {
        'voting_params': 'voting_params',
        'deposit_params': 'deposit_params',
        'tally_params': 'tally_params',
        'params': 'params'
    }

    def __init__(self, voting_params=None, deposit_params=None, tally_params=None, params=None):  # noqa: E501
        """CosmosGovV1QueryParamsResponse - a model defined in Swagger"""  # noqa: E501
        self._voting_params = None
        self._deposit_params = None
        self._tally_params = None
        self._params = None
        self.discriminator = None
        if voting_params is not None:
            self.voting_params = voting_params
        if deposit_params is not None:
            self.deposit_params = deposit_params
        if tally_params is not None:
            self.tally_params = tally_params
        if params is not None:
            self.params = params

    @property
    def voting_params(self):
        """Gets the voting_params of this CosmosGovV1QueryParamsResponse.  # noqa: E501


        :return: The voting_params of this CosmosGovV1QueryParamsResponse.  # noqa: E501
        :rtype: CosmosGovV1QueryParamsResponseVotingParams
        """
        return self._voting_params

    @voting_params.setter
    def voting_params(self, voting_params):
        """Sets the voting_params of this CosmosGovV1QueryParamsResponse.


        :param voting_params: The voting_params of this CosmosGovV1QueryParamsResponse.  # noqa: E501
        :type: CosmosGovV1QueryParamsResponseVotingParams
        """

        self._voting_params = voting_params

    @property
    def deposit_params(self):
        """Gets the deposit_params of this CosmosGovV1QueryParamsResponse.  # noqa: E501


        :return: The deposit_params of this CosmosGovV1QueryParamsResponse.  # noqa: E501
        :rtype: CosmosGovV1QueryParamsResponseDepositParams
        """
        return self._deposit_params

    @deposit_params.setter
    def deposit_params(self, deposit_params):
        """Sets the deposit_params of this CosmosGovV1QueryParamsResponse.


        :param deposit_params: The deposit_params of this CosmosGovV1QueryParamsResponse.  # noqa: E501
        :type: CosmosGovV1QueryParamsResponseDepositParams
        """

        self._deposit_params = deposit_params

    @property
    def tally_params(self):
        """Gets the tally_params of this CosmosGovV1QueryParamsResponse.  # noqa: E501


        :return: The tally_params of this CosmosGovV1QueryParamsResponse.  # noqa: E501
        :rtype: CosmosGovV1QueryParamsResponseTallyParams
        """
        return self._tally_params

    @tally_params.setter
    def tally_params(self, tally_params):
        """Sets the tally_params of this CosmosGovV1QueryParamsResponse.


        :param tally_params: The tally_params of this CosmosGovV1QueryParamsResponse.  # noqa: E501
        :type: CosmosGovV1QueryParamsResponseTallyParams
        """

        self._tally_params = tally_params

    @property
    def params(self):
        """Gets the params of this CosmosGovV1QueryParamsResponse.  # noqa: E501


        :return: The params of this CosmosGovV1QueryParamsResponse.  # noqa: E501
        :rtype: CosmosGovV1QueryParamsResponseParams
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this CosmosGovV1QueryParamsResponse.


        :param params: The params of this CosmosGovV1QueryParamsResponse.  # noqa: E501
        :type: CosmosGovV1QueryParamsResponseParams
        """

        self._params = params

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
        if issubclass(CosmosGovV1QueryParamsResponse, dict):
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
        if not isinstance(other, CosmosGovV1QueryParamsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
