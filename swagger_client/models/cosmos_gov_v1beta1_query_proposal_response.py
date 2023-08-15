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

class CosmosGovV1beta1QueryProposalResponse(object):
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
        'proposal': 'CosmosGovV1beta1QueryProposalResponseProposal'
    }

    attribute_map = {
        'proposal': 'proposal'
    }

    def __init__(self, proposal=None):  # noqa: E501
        """CosmosGovV1beta1QueryProposalResponse - a model defined in Swagger"""  # noqa: E501
        self._proposal = None
        self.discriminator = None
        if proposal is not None:
            self.proposal = proposal

    @property
    def proposal(self):
        """Gets the proposal of this CosmosGovV1beta1QueryProposalResponse.  # noqa: E501


        :return: The proposal of this CosmosGovV1beta1QueryProposalResponse.  # noqa: E501
        :rtype: CosmosGovV1beta1QueryProposalResponseProposal
        """
        return self._proposal

    @proposal.setter
    def proposal(self, proposal):
        """Sets the proposal of this CosmosGovV1beta1QueryProposalResponse.


        :param proposal: The proposal of this CosmosGovV1beta1QueryProposalResponse.  # noqa: E501
        :type: CosmosGovV1beta1QueryProposalResponseProposal
        """

        self._proposal = proposal

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
        if issubclass(CosmosGovV1beta1QueryProposalResponse, dict):
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
        if not isinstance(other, CosmosGovV1beta1QueryProposalResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
