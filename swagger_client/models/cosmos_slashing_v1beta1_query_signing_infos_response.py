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

class CosmosSlashingV1beta1QuerySigningInfosResponse(object):
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
        'info': 'list[CosmosSlashingV1beta1QuerySigningInfosResponseInfo]',
        'pagination': 'CosmosNftV1beta1QueryClassesResponsePagination'
    }

    attribute_map = {
        'info': 'info',
        'pagination': 'pagination'
    }

    def __init__(self, info=None, pagination=None):  # noqa: E501
        """CosmosSlashingV1beta1QuerySigningInfosResponse - a model defined in Swagger"""  # noqa: E501
        self._info = None
        self._pagination = None
        self.discriminator = None
        if info is not None:
            self.info = info
        if pagination is not None:
            self.pagination = pagination

    @property
    def info(self):
        """Gets the info of this CosmosSlashingV1beta1QuerySigningInfosResponse.  # noqa: E501


        :return: The info of this CosmosSlashingV1beta1QuerySigningInfosResponse.  # noqa: E501
        :rtype: list[CosmosSlashingV1beta1QuerySigningInfosResponseInfo]
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this CosmosSlashingV1beta1QuerySigningInfosResponse.


        :param info: The info of this CosmosSlashingV1beta1QuerySigningInfosResponse.  # noqa: E501
        :type: list[CosmosSlashingV1beta1QuerySigningInfosResponseInfo]
        """

        self._info = info

    @property
    def pagination(self):
        """Gets the pagination of this CosmosSlashingV1beta1QuerySigningInfosResponse.  # noqa: E501


        :return: The pagination of this CosmosSlashingV1beta1QuerySigningInfosResponse.  # noqa: E501
        :rtype: CosmosNftV1beta1QueryClassesResponsePagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this CosmosSlashingV1beta1QuerySigningInfosResponse.


        :param pagination: The pagination of this CosmosSlashingV1beta1QuerySigningInfosResponse.  # noqa: E501
        :type: CosmosNftV1beta1QueryClassesResponsePagination
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
        if issubclass(CosmosSlashingV1beta1QuerySigningInfosResponse, dict):
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
        if not isinstance(other, CosmosSlashingV1beta1QuerySigningInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
