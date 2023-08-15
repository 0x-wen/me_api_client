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

class InlineResponse20054(object):
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
        'groups': 'list[CosmosGroupV1QueryGroupsByAdminResponseGroups]',
        'pagination': 'CosmosAuthV1beta1QueryAccountsResponsePagination'
    }

    attribute_map = {
        'groups': 'groups',
        'pagination': 'pagination'
    }

    def __init__(self, groups=None, pagination=None):  # noqa: E501
        """InlineResponse20054 - a model defined in Swagger"""  # noqa: E501
        self._groups = None
        self._pagination = None
        self.discriminator = None
        if groups is not None:
            self.groups = groups
        if pagination is not None:
            self.pagination = pagination

    @property
    def groups(self):
        """Gets the groups of this InlineResponse20054.  # noqa: E501

        groups are the groups info with the provided group member.  # noqa: E501

        :return: The groups of this InlineResponse20054.  # noqa: E501
        :rtype: list[CosmosGroupV1QueryGroupsByAdminResponseGroups]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this InlineResponse20054.

        groups are the groups info with the provided group member.  # noqa: E501

        :param groups: The groups of this InlineResponse20054.  # noqa: E501
        :type: list[CosmosGroupV1QueryGroupsByAdminResponseGroups]
        """

        self._groups = groups

    @property
    def pagination(self):
        """Gets the pagination of this InlineResponse20054.  # noqa: E501


        :return: The pagination of this InlineResponse20054.  # noqa: E501
        :rtype: CosmosAuthV1beta1QueryAccountsResponsePagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this InlineResponse20054.


        :param pagination: The pagination of this InlineResponse20054.  # noqa: E501
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
        if issubclass(InlineResponse20054, dict):
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
        if not isinstance(other, InlineResponse20054):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
