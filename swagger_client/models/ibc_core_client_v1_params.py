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

class IbcCoreClientV1Params(object):
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
        'allowed_clients': 'list[str]'
    }

    attribute_map = {
        'allowed_clients': 'allowed_clients'
    }

    def __init__(self, allowed_clients=None):  # noqa: E501
        """IbcCoreClientV1Params - a model defined in Swagger"""  # noqa: E501
        self._allowed_clients = None
        self.discriminator = None
        if allowed_clients is not None:
            self.allowed_clients = allowed_clients

    @property
    def allowed_clients(self):
        """Gets the allowed_clients of this IbcCoreClientV1Params.  # noqa: E501

        allowed_clients defines the list of allowed client state types which can be created and interacted with. If a client type is removed from the allowed clients list, usage of this client will be disabled until it is added again to the list.  # noqa: E501

        :return: The allowed_clients of this IbcCoreClientV1Params.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_clients

    @allowed_clients.setter
    def allowed_clients(self, allowed_clients):
        """Sets the allowed_clients of this IbcCoreClientV1Params.

        allowed_clients defines the list of allowed client state types which can be created and interacted with. If a client type is removed from the allowed clients list, usage of this client will be disabled until it is added again to the list.  # noqa: E501

        :param allowed_clients: The allowed_clients of this IbcCoreClientV1Params.  # noqa: E501
        :type: list[str]
        """

        self._allowed_clients = allowed_clients

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
        if issubclass(IbcCoreClientV1Params, dict):
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
        if not isinstance(other, IbcCoreClientV1Params):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
