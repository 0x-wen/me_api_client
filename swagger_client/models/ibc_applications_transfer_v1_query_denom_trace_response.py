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

class IbcApplicationsTransferV1QueryDenomTraceResponse(object):
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
        'denom_trace': 'IbcApplicationsTransferV1QueryDenomTraceResponseDenomTrace'
    }

    attribute_map = {
        'denom_trace': 'denom_trace'
    }

    def __init__(self, denom_trace=None):  # noqa: E501
        """IbcApplicationsTransferV1QueryDenomTraceResponse - a model defined in Swagger"""  # noqa: E501
        self._denom_trace = None
        self.discriminator = None
        if denom_trace is not None:
            self.denom_trace = denom_trace

    @property
    def denom_trace(self):
        """Gets the denom_trace of this IbcApplicationsTransferV1QueryDenomTraceResponse.  # noqa: E501


        :return: The denom_trace of this IbcApplicationsTransferV1QueryDenomTraceResponse.  # noqa: E501
        :rtype: IbcApplicationsTransferV1QueryDenomTraceResponseDenomTrace
        """
        return self._denom_trace

    @denom_trace.setter
    def denom_trace(self, denom_trace):
        """Sets the denom_trace of this IbcApplicationsTransferV1QueryDenomTraceResponse.


        :param denom_trace: The denom_trace of this IbcApplicationsTransferV1QueryDenomTraceResponse.  # noqa: E501
        :type: IbcApplicationsTransferV1QueryDenomTraceResponseDenomTrace
        """

        self._denom_trace = denom_trace

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
        if issubclass(IbcApplicationsTransferV1QueryDenomTraceResponse, dict):
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
        if not isinstance(other, IbcApplicationsTransferV1QueryDenomTraceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
