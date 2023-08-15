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

class InlineResponse20020(object):
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
        'code': 'int',
        'log': 'str',
        'info': 'str',
        'index': 'str',
        'key': 'str',
        'value': 'str',
        'proof_ops': 'CosmosBaseTendermintV1beta1ABCIQueryResponseProofOps',
        'height': 'str',
        'codespace': 'str'
    }

    attribute_map = {
        'code': 'code',
        'log': 'log',
        'info': 'info',
        'index': 'index',
        'key': 'key',
        'value': 'value',
        'proof_ops': 'proof_ops',
        'height': 'height',
        'codespace': 'codespace'
    }

    def __init__(self, code=None, log=None, info=None, index=None, key=None, value=None, proof_ops=None, height=None, codespace=None):  # noqa: E501
        """InlineResponse20020 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._log = None
        self._info = None
        self._index = None
        self._key = None
        self._value = None
        self._proof_ops = None
        self._height = None
        self._codespace = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if log is not None:
            self.log = log
        if info is not None:
            self.info = info
        if index is not None:
            self.index = index
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if proof_ops is not None:
            self.proof_ops = proof_ops
        if height is not None:
            self.height = height
        if codespace is not None:
            self.codespace = codespace

    @property
    def code(self):
        """Gets the code of this InlineResponse20020.  # noqa: E501


        :return: The code of this InlineResponse20020.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse20020.


        :param code: The code of this InlineResponse20020.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def log(self):
        """Gets the log of this InlineResponse20020.  # noqa: E501


        :return: The log of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this InlineResponse20020.


        :param log: The log of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._log = log

    @property
    def info(self):
        """Gets the info of this InlineResponse20020.  # noqa: E501


        :return: The info of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this InlineResponse20020.


        :param info: The info of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._info = info

    @property
    def index(self):
        """Gets the index of this InlineResponse20020.  # noqa: E501


        :return: The index of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this InlineResponse20020.


        :param index: The index of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._index = index

    @property
    def key(self):
        """Gets the key of this InlineResponse20020.  # noqa: E501


        :return: The key of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this InlineResponse20020.


        :param key: The key of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this InlineResponse20020.  # noqa: E501


        :return: The value of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InlineResponse20020.


        :param value: The value of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def proof_ops(self):
        """Gets the proof_ops of this InlineResponse20020.  # noqa: E501


        :return: The proof_ops of this InlineResponse20020.  # noqa: E501
        :rtype: CosmosBaseTendermintV1beta1ABCIQueryResponseProofOps
        """
        return self._proof_ops

    @proof_ops.setter
    def proof_ops(self, proof_ops):
        """Sets the proof_ops of this InlineResponse20020.


        :param proof_ops: The proof_ops of this InlineResponse20020.  # noqa: E501
        :type: CosmosBaseTendermintV1beta1ABCIQueryResponseProofOps
        """

        self._proof_ops = proof_ops

    @property
    def height(self):
        """Gets the height of this InlineResponse20020.  # noqa: E501


        :return: The height of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this InlineResponse20020.


        :param height: The height of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def codespace(self):
        """Gets the codespace of this InlineResponse20020.  # noqa: E501


        :return: The codespace of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._codespace

    @codespace.setter
    def codespace(self, codespace):
        """Sets the codespace of this InlineResponse20020.


        :param codespace: The codespace of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._codespace = codespace

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
        if issubclass(InlineResponse20020, dict):
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
        if not isinstance(other, InlineResponse20020):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
