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

class CosmosGovV1QueryVoteResponseVoteOptions(object):
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
        'option': 'str',
        'weight': 'str'
    }

    attribute_map = {
        'option': 'option',
        'weight': 'weight'
    }

    def __init__(self, option='VOTE_OPTION_UNSPECIFIED', weight=None):  # noqa: E501
        """CosmosGovV1QueryVoteResponseVoteOptions - a model defined in Swagger"""  # noqa: E501
        self._option = None
        self._weight = None
        self.discriminator = None
        if option is not None:
            self.option = option
        if weight is not None:
            self.weight = weight

    @property
    def option(self):
        """Gets the option of this CosmosGovV1QueryVoteResponseVoteOptions.  # noqa: E501

        VoteOption enumerates the valid vote options for a given governance proposal.   - VOTE_OPTION_UNSPECIFIED: VOTE_OPTION_UNSPECIFIED defines a no-op vote option.  - VOTE_OPTION_YES: VOTE_OPTION_YES defines a yes vote option.  - VOTE_OPTION_ABSTAIN: VOTE_OPTION_ABSTAIN defines an abstain vote option.  - VOTE_OPTION_NO: VOTE_OPTION_NO defines a no vote option.  - VOTE_OPTION_NO_WITH_VETO: VOTE_OPTION_NO_WITH_VETO defines a no with veto vote option.  # noqa: E501

        :return: The option of this CosmosGovV1QueryVoteResponseVoteOptions.  # noqa: E501
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this CosmosGovV1QueryVoteResponseVoteOptions.

        VoteOption enumerates the valid vote options for a given governance proposal.   - VOTE_OPTION_UNSPECIFIED: VOTE_OPTION_UNSPECIFIED defines a no-op vote option.  - VOTE_OPTION_YES: VOTE_OPTION_YES defines a yes vote option.  - VOTE_OPTION_ABSTAIN: VOTE_OPTION_ABSTAIN defines an abstain vote option.  - VOTE_OPTION_NO: VOTE_OPTION_NO defines a no vote option.  - VOTE_OPTION_NO_WITH_VETO: VOTE_OPTION_NO_WITH_VETO defines a no with veto vote option.  # noqa: E501

        :param option: The option of this CosmosGovV1QueryVoteResponseVoteOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["VOTE_OPTION_UNSPECIFIED", "VOTE_OPTION_YES", "VOTE_OPTION_ABSTAIN", "VOTE_OPTION_NO", "VOTE_OPTION_NO_WITH_VETO"]  # noqa: E501
        if option not in allowed_values:
            raise ValueError(
                "Invalid value for `option` ({0}), must be one of {1}"  # noqa: E501
                .format(option, allowed_values)
            )

        self._option = option

    @property
    def weight(self):
        """Gets the weight of this CosmosGovV1QueryVoteResponseVoteOptions.  # noqa: E501


        :return: The weight of this CosmosGovV1QueryVoteResponseVoteOptions.  # noqa: E501
        :rtype: str
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CosmosGovV1QueryVoteResponseVoteOptions.


        :param weight: The weight of this CosmosGovV1QueryVoteResponseVoteOptions.  # noqa: E501
        :type: str
        """

        self._weight = weight

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
        if issubclass(CosmosGovV1QueryVoteResponseVoteOptions, dict):
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
        if not isinstance(other, CosmosGovV1QueryVoteResponseVoteOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
