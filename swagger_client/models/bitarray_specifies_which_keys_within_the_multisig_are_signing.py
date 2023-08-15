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

class BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning(object):
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
        'extra_bits_stored': 'int',
        'elems': 'str'
    }

    attribute_map = {
        'extra_bits_stored': 'extra_bits_stored',
        'elems': 'elems'
    }

    def __init__(self, extra_bits_stored=None, elems=None):  # noqa: E501
        """BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning - a model defined in Swagger"""  # noqa: E501
        self._extra_bits_stored = None
        self._elems = None
        self.discriminator = None
        if extra_bits_stored is not None:
            self.extra_bits_stored = extra_bits_stored
        if elems is not None:
            self.elems = elems

    @property
    def extra_bits_stored(self):
        """Gets the extra_bits_stored of this BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning.  # noqa: E501


        :return: The extra_bits_stored of this BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning.  # noqa: E501
        :rtype: int
        """
        return self._extra_bits_stored

    @extra_bits_stored.setter
    def extra_bits_stored(self, extra_bits_stored):
        """Sets the extra_bits_stored of this BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning.


        :param extra_bits_stored: The extra_bits_stored of this BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning.  # noqa: E501
        :type: int
        """

        self._extra_bits_stored = extra_bits_stored

    @property
    def elems(self):
        """Gets the elems of this BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning.  # noqa: E501


        :return: The elems of this BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning.  # noqa: E501
        :rtype: str
        """
        return self._elems

    @elems.setter
    def elems(self, elems):
        """Sets the elems of this BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning.


        :param elems: The elems of this BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning.  # noqa: E501
        :type: str
        """

        self._elems = elems

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
        if issubclass(BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning, dict):
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
        if not isinstance(other, BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
