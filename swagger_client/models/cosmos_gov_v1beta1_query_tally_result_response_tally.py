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

class CosmosGovV1beta1QueryTallyResultResponseTally(object):
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
        'yes': 'str',
        'abstain': 'str',
        'no': 'str',
        'no_with_veto': 'str'
    }

    attribute_map = {
        'yes': 'yes',
        'abstain': 'abstain',
        'no': 'no',
        'no_with_veto': 'no_with_veto'
    }

    def __init__(self, yes=None, abstain=None, no=None, no_with_veto=None):  # noqa: E501
        """CosmosGovV1beta1QueryTallyResultResponseTally - a model defined in Swagger"""  # noqa: E501
        self._yes = None
        self._abstain = None
        self._no = None
        self._no_with_veto = None
        self.discriminator = None
        if yes is not None:
            self.yes = yes
        if abstain is not None:
            self.abstain = abstain
        if no is not None:
            self.no = no
        if no_with_veto is not None:
            self.no_with_veto = no_with_veto

    @property
    def yes(self):
        """Gets the yes of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501

        yes is the number of yes votes on a proposal.  # noqa: E501

        :return: The yes of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501
        :rtype: str
        """
        return self._yes

    @yes.setter
    def yes(self, yes):
        """Sets the yes of this CosmosGovV1beta1QueryTallyResultResponseTally.

        yes is the number of yes votes on a proposal.  # noqa: E501

        :param yes: The yes of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501
        :type: str
        """

        self._yes = yes

    @property
    def abstain(self):
        """Gets the abstain of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501

        abstain is the number of abstain votes on a proposal.  # noqa: E501

        :return: The abstain of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501
        :rtype: str
        """
        return self._abstain

    @abstain.setter
    def abstain(self, abstain):
        """Sets the abstain of this CosmosGovV1beta1QueryTallyResultResponseTally.

        abstain is the number of abstain votes on a proposal.  # noqa: E501

        :param abstain: The abstain of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501
        :type: str
        """

        self._abstain = abstain

    @property
    def no(self):
        """Gets the no of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501

        no is the number of no votes on a proposal.  # noqa: E501

        :return: The no of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501
        :rtype: str
        """
        return self._no

    @no.setter
    def no(self, no):
        """Sets the no of this CosmosGovV1beta1QueryTallyResultResponseTally.

        no is the number of no votes on a proposal.  # noqa: E501

        :param no: The no of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501
        :type: str
        """

        self._no = no

    @property
    def no_with_veto(self):
        """Gets the no_with_veto of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501

        no_with_veto is the number of no with veto votes on a proposal.  # noqa: E501

        :return: The no_with_veto of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501
        :rtype: str
        """
        return self._no_with_veto

    @no_with_veto.setter
    def no_with_veto(self, no_with_veto):
        """Sets the no_with_veto of this CosmosGovV1beta1QueryTallyResultResponseTally.

        no_with_veto is the number of no with veto votes on a proposal.  # noqa: E501

        :param no_with_veto: The no_with_veto of this CosmosGovV1beta1QueryTallyResultResponseTally.  # noqa: E501
        :type: str
        """

        self._no_with_veto = no_with_veto

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
        if issubclass(CosmosGovV1beta1QueryTallyResultResponseTally, dict):
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
        if not isinstance(other, CosmosGovV1beta1QueryTallyResultResponseTally):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
