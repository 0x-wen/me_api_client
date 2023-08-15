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

class InlineResponse20029(object):
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
        'evidence': 'list[dict(str, object)]',
        'pagination': 'CosmosAuthV1beta1QueryAccountsResponsePagination'
    }

    attribute_map = {
        'evidence': 'evidence',
        'pagination': 'pagination'
    }

    def __init__(self, evidence=None, pagination=None):  # noqa: E501
        """InlineResponse20029 - a model defined in Swagger"""  # noqa: E501
        self._evidence = None
        self._pagination = None
        self.discriminator = None
        if evidence is not None:
            self.evidence = evidence
        if pagination is not None:
            self.pagination = pagination

    @property
    def evidence(self):
        """Gets the evidence of this InlineResponse20029.  # noqa: E501

        evidence returns all evidences.  # noqa: E501

        :return: The evidence of this InlineResponse20029.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._evidence

    @evidence.setter
    def evidence(self, evidence):
        """Sets the evidence of this InlineResponse20029.

        evidence returns all evidences.  # noqa: E501

        :param evidence: The evidence of this InlineResponse20029.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._evidence = evidence

    @property
    def pagination(self):
        """Gets the pagination of this InlineResponse20029.  # noqa: E501


        :return: The pagination of this InlineResponse20029.  # noqa: E501
        :rtype: CosmosAuthV1beta1QueryAccountsResponsePagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this InlineResponse20029.


        :param pagination: The pagination of this InlineResponse20029.  # noqa: E501
        :type: CosmosAuthV1beta1QueryAccountsResponsePagination
        """

        self._pagination = pagination

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
        if issubclass(InlineResponse20029, dict):
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
        if not isinstance(other, InlineResponse20029):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other