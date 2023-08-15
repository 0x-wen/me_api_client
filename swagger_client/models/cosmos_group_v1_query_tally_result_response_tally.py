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

class CosmosGroupV1QueryTallyResultResponseTally(object):
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
        'yes_count': 'str',
        'abstain_count': 'str',
        'no_count': 'str',
        'no_with_veto_count': 'str'
    }

    attribute_map = {
        'yes_count': 'yes_count',
        'abstain_count': 'abstain_count',
        'no_count': 'no_count',
        'no_with_veto_count': 'no_with_veto_count'
    }

    def __init__(self, yes_count=None, abstain_count=None, no_count=None, no_with_veto_count=None):  # noqa: E501
        """CosmosGroupV1QueryTallyResultResponseTally - a model defined in Swagger"""  # noqa: E501
        self._yes_count = None
        self._abstain_count = None
        self._no_count = None
        self._no_with_veto_count = None
        self.discriminator = None
        if yes_count is not None:
            self.yes_count = yes_count
        if abstain_count is not None:
            self.abstain_count = abstain_count
        if no_count is not None:
            self.no_count = no_count
        if no_with_veto_count is not None:
            self.no_with_veto_count = no_with_veto_count

    @property
    def yes_count(self):
        """Gets the yes_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501

        yes_count is the weighted sum of yes votes.  # noqa: E501

        :return: The yes_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501
        :rtype: str
        """
        return self._yes_count

    @yes_count.setter
    def yes_count(self, yes_count):
        """Sets the yes_count of this CosmosGroupV1QueryTallyResultResponseTally.

        yes_count is the weighted sum of yes votes.  # noqa: E501

        :param yes_count: The yes_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501
        :type: str
        """

        self._yes_count = yes_count

    @property
    def abstain_count(self):
        """Gets the abstain_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501

        abstain_count is the weighted sum of abstainers.  # noqa: E501

        :return: The abstain_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501
        :rtype: str
        """
        return self._abstain_count

    @abstain_count.setter
    def abstain_count(self, abstain_count):
        """Sets the abstain_count of this CosmosGroupV1QueryTallyResultResponseTally.

        abstain_count is the weighted sum of abstainers.  # noqa: E501

        :param abstain_count: The abstain_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501
        :type: str
        """

        self._abstain_count = abstain_count

    @property
    def no_count(self):
        """Gets the no_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501

        no_count is the weighted sum of no votes.  # noqa: E501

        :return: The no_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501
        :rtype: str
        """
        return self._no_count

    @no_count.setter
    def no_count(self, no_count):
        """Sets the no_count of this CosmosGroupV1QueryTallyResultResponseTally.

        no_count is the weighted sum of no votes.  # noqa: E501

        :param no_count: The no_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501
        :type: str
        """

        self._no_count = no_count

    @property
    def no_with_veto_count(self):
        """Gets the no_with_veto_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501

        no_with_veto_count is the weighted sum of veto.  # noqa: E501

        :return: The no_with_veto_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501
        :rtype: str
        """
        return self._no_with_veto_count

    @no_with_veto_count.setter
    def no_with_veto_count(self, no_with_veto_count):
        """Sets the no_with_veto_count of this CosmosGroupV1QueryTallyResultResponseTally.

        no_with_veto_count is the weighted sum of veto.  # noqa: E501

        :param no_with_veto_count: The no_with_veto_count of this CosmosGroupV1QueryTallyResultResponseTally.  # noqa: E501
        :type: str
        """

        self._no_with_veto_count = no_with_veto_count

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
        if issubclass(CosmosGroupV1QueryTallyResultResponseTally, dict):
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
        if not isinstance(other, CosmosGroupV1QueryTallyResultResponseTally):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
