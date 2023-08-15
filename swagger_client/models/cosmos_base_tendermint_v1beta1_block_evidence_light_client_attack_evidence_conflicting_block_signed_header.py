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

class CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader(object):
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
        'header': 'CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader',
        'commit': 'CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommit'
    }

    attribute_map = {
        'header': 'header',
        'commit': 'commit'
    }

    def __init__(self, header=None, commit=None):  # noqa: E501
        """CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader - a model defined in Swagger"""  # noqa: E501
        self._header = None
        self._commit = None
        self.discriminator = None
        if header is not None:
            self.header = header
        if commit is not None:
            self.commit = commit

    @property
    def header(self):
        """Gets the header of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader.  # noqa: E501


        :return: The header of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader.  # noqa: E501
        :rtype: CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader.


        :param header: The header of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader.  # noqa: E501
        :type: CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader
        """

        self._header = header

    @property
    def commit(self):
        """Gets the commit of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader.  # noqa: E501


        :return: The commit of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader.  # noqa: E501
        :rtype: CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommit
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader.


        :param commit: The commit of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader.  # noqa: E501
        :type: CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommit
        """

        self._commit = commit

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
        if issubclass(CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader, dict):
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
        if not isinstance(other, CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
