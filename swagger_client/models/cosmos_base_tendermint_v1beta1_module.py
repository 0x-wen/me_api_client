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

class CosmosBaseTendermintV1beta1Module(object):
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
        'path': 'str',
        'version': 'str',
        'sum': 'str'
    }

    attribute_map = {
        'path': 'path',
        'version': 'version',
        'sum': 'sum'
    }

    def __init__(self, path=None, version=None, sum=None):  # noqa: E501
        """CosmosBaseTendermintV1beta1Module - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._version = None
        self._sum = None
        self.discriminator = None
        if path is not None:
            self.path = path
        if version is not None:
            self.version = version
        if sum is not None:
            self.sum = sum

    @property
    def path(self):
        """Gets the path of this CosmosBaseTendermintV1beta1Module.  # noqa: E501


        :return: The path of this CosmosBaseTendermintV1beta1Module.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CosmosBaseTendermintV1beta1Module.


        :param path: The path of this CosmosBaseTendermintV1beta1Module.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def version(self):
        """Gets the version of this CosmosBaseTendermintV1beta1Module.  # noqa: E501


        :return: The version of this CosmosBaseTendermintV1beta1Module.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CosmosBaseTendermintV1beta1Module.


        :param version: The version of this CosmosBaseTendermintV1beta1Module.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def sum(self):
        """Gets the sum of this CosmosBaseTendermintV1beta1Module.  # noqa: E501


        :return: The sum of this CosmosBaseTendermintV1beta1Module.  # noqa: E501
        :rtype: str
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this CosmosBaseTendermintV1beta1Module.


        :param sum: The sum of this CosmosBaseTendermintV1beta1Module.  # noqa: E501
        :type: str
        """

        self._sum = sum

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
        if issubclass(CosmosBaseTendermintV1beta1Module, dict):
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
        if not isinstance(other, CosmosBaseTendermintV1beta1Module):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
