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

class CosmosGroupV1QueryGroupMembersResponseMembers(object):
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
        'group_id': 'str',
        'member': 'CosmosGroupV1GroupMemberMember'
    }

    attribute_map = {
        'group_id': 'group_id',
        'member': 'member'
    }

    def __init__(self, group_id=None, member=None):  # noqa: E501
        """CosmosGroupV1QueryGroupMembersResponseMembers - a model defined in Swagger"""  # noqa: E501
        self._group_id = None
        self._member = None
        self.discriminator = None
        if group_id is not None:
            self.group_id = group_id
        if member is not None:
            self.member = member

    @property
    def group_id(self):
        """Gets the group_id of this CosmosGroupV1QueryGroupMembersResponseMembers.  # noqa: E501

        group_id is the unique ID of the group.  # noqa: E501

        :return: The group_id of this CosmosGroupV1QueryGroupMembersResponseMembers.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CosmosGroupV1QueryGroupMembersResponseMembers.

        group_id is the unique ID of the group.  # noqa: E501

        :param group_id: The group_id of this CosmosGroupV1QueryGroupMembersResponseMembers.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def member(self):
        """Gets the member of this CosmosGroupV1QueryGroupMembersResponseMembers.  # noqa: E501


        :return: The member of this CosmosGroupV1QueryGroupMembersResponseMembers.  # noqa: E501
        :rtype: CosmosGroupV1GroupMemberMember
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this CosmosGroupV1QueryGroupMembersResponseMembers.


        :param member: The member of this CosmosGroupV1QueryGroupMembersResponseMembers.  # noqa: E501
        :type: CosmosGroupV1GroupMemberMember
        """

        self._member = member

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
        if issubclass(CosmosGroupV1QueryGroupMembersResponseMembers, dict):
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
        if not isinstance(other, CosmosGroupV1QueryGroupMembersResponseMembers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
