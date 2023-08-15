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

class HeightAtWhichTheProofWasRetrieved(object):
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
        'revision_number': 'str',
        'revision_height': 'str'
    }

    attribute_map = {
        'revision_number': 'revision_number',
        'revision_height': 'revision_height'
    }

    def __init__(self, revision_number=None, revision_height=None):  # noqa: E501
        """HeightAtWhichTheProofWasRetrieved - a model defined in Swagger"""  # noqa: E501
        self._revision_number = None
        self._revision_height = None
        self.discriminator = None
        if revision_number is not None:
            self.revision_number = revision_number
        if revision_height is not None:
            self.revision_height = revision_height

    @property
    def revision_number(self):
        """Gets the revision_number of this HeightAtWhichTheProofWasRetrieved.  # noqa: E501


        :return: The revision_number of this HeightAtWhichTheProofWasRetrieved.  # noqa: E501
        :rtype: str
        """
        return self._revision_number

    @revision_number.setter
    def revision_number(self, revision_number):
        """Sets the revision_number of this HeightAtWhichTheProofWasRetrieved.


        :param revision_number: The revision_number of this HeightAtWhichTheProofWasRetrieved.  # noqa: E501
        :type: str
        """

        self._revision_number = revision_number

    @property
    def revision_height(self):
        """Gets the revision_height of this HeightAtWhichTheProofWasRetrieved.  # noqa: E501


        :return: The revision_height of this HeightAtWhichTheProofWasRetrieved.  # noqa: E501
        :rtype: str
        """
        return self._revision_height

    @revision_height.setter
    def revision_height(self, revision_height):
        """Sets the revision_height of this HeightAtWhichTheProofWasRetrieved.


        :param revision_height: The revision_height of this HeightAtWhichTheProofWasRetrieved.  # noqa: E501
        :type: str
        """

        self._revision_height = revision_height

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
        if issubclass(HeightAtWhichTheProofWasRetrieved, dict):
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
        if not isinstance(other, HeightAtWhichTheProofWasRetrieved):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other