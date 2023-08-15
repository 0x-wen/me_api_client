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

class CosmosBaseAbciV1beta1Result(object):
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
        'data': 'str',
        'log': 'str',
        'events': 'list[CosmosBaseAbciV1beta1ResultEvents]',
        'msg_responses': 'list[dict(str, object)]'
    }

    attribute_map = {
        'data': 'data',
        'log': 'log',
        'events': 'events',
        'msg_responses': 'msg_responses'
    }

    def __init__(self, data=None, log=None, events=None, msg_responses=None):  # noqa: E501
        """CosmosBaseAbciV1beta1Result - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._log = None
        self._events = None
        self._msg_responses = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if log is not None:
            self.log = log
        if events is not None:
            self.events = events
        if msg_responses is not None:
            self.msg_responses = msg_responses

    @property
    def data(self):
        """Gets the data of this CosmosBaseAbciV1beta1Result.  # noqa: E501

        Data is any data returned from message or handler execution. It MUST be length prefixed in order to separate data from multiple message executions. Deprecated. This field is still populated, but prefer msg_response instead because it also contains the Msg response typeURL.  # noqa: E501

        :return: The data of this CosmosBaseAbciV1beta1Result.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CosmosBaseAbciV1beta1Result.

        Data is any data returned from message or handler execution. It MUST be length prefixed in order to separate data from multiple message executions. Deprecated. This field is still populated, but prefer msg_response instead because it also contains the Msg response typeURL.  # noqa: E501

        :param data: The data of this CosmosBaseAbciV1beta1Result.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def log(self):
        """Gets the log of this CosmosBaseAbciV1beta1Result.  # noqa: E501

        Log contains the log information from message or handler execution.  # noqa: E501

        :return: The log of this CosmosBaseAbciV1beta1Result.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this CosmosBaseAbciV1beta1Result.

        Log contains the log information from message or handler execution.  # noqa: E501

        :param log: The log of this CosmosBaseAbciV1beta1Result.  # noqa: E501
        :type: str
        """

        self._log = log

    @property
    def events(self):
        """Gets the events of this CosmosBaseAbciV1beta1Result.  # noqa: E501

        Events contains a slice of Event objects that were emitted during message or handler execution.  # noqa: E501

        :return: The events of this CosmosBaseAbciV1beta1Result.  # noqa: E501
        :rtype: list[CosmosBaseAbciV1beta1ResultEvents]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this CosmosBaseAbciV1beta1Result.

        Events contains a slice of Event objects that were emitted during message or handler execution.  # noqa: E501

        :param events: The events of this CosmosBaseAbciV1beta1Result.  # noqa: E501
        :type: list[CosmosBaseAbciV1beta1ResultEvents]
        """

        self._events = events

    @property
    def msg_responses(self):
        """Gets the msg_responses of this CosmosBaseAbciV1beta1Result.  # noqa: E501

        msg_responses contains the Msg handler responses type packed in Anys.  Since: cosmos-sdk 0.46  # noqa: E501

        :return: The msg_responses of this CosmosBaseAbciV1beta1Result.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._msg_responses

    @msg_responses.setter
    def msg_responses(self, msg_responses):
        """Sets the msg_responses of this CosmosBaseAbciV1beta1Result.

        msg_responses contains the Msg handler responses type packed in Anys.  Since: cosmos-sdk 0.46  # noqa: E501

        :param msg_responses: The msg_responses of this CosmosBaseAbciV1beta1Result.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._msg_responses = msg_responses

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
        if issubclass(CosmosBaseAbciV1beta1Result, dict):
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
        if not isinstance(other, CosmosBaseAbciV1beta1Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
