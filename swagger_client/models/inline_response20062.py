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

class InlineResponse20062(object):
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
        'param': 'CosmosParamsV1beta1QueryParamsResponseParam'
    }

    attribute_map = {
        'param': 'param'
    }

    def __init__(self, param=None):  # noqa: E501
        """InlineResponse20062 - a model defined in Swagger"""  # noqa: E501
        self._param = None
        self.discriminator = None
        if param is not None:
            self.param = param

    @property
    def param(self):
        """Gets the param of this InlineResponse20062.  # noqa: E501


        :return: The param of this InlineResponse20062.  # noqa: E501
        :rtype: CosmosParamsV1beta1QueryParamsResponseParam
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this InlineResponse20062.


        :param param: The param of this InlineResponse20062.  # noqa: E501
        :type: CosmosParamsV1beta1QueryParamsResponseParam
        """

        self._param = param

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
        if issubclass(InlineResponse20062, dict):
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
        if not isinstance(other, InlineResponse20062):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
