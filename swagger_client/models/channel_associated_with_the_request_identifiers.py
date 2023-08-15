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

class ChannelAssociatedWithTheRequestIdentifiers(object):
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
        'state': 'str',
        'ordering': 'str',
        'counterparty': 'CounterpartyChannelEnd',
        'connection_hops': 'list[str]',
        'version': 'str'
    }

    attribute_map = {
        'state': 'state',
        'ordering': 'ordering',
        'counterparty': 'counterparty',
        'connection_hops': 'connection_hops',
        'version': 'version'
    }

    def __init__(self, state='STATE_UNINITIALIZED_UNSPECIFIED', ordering='ORDER_NONE_UNSPECIFIED', counterparty=None, connection_hops=None, version=None):  # noqa: E501
        """ChannelAssociatedWithTheRequestIdentifiers - a model defined in Swagger"""  # noqa: E501
        self._state = None
        self._ordering = None
        self._counterparty = None
        self._connection_hops = None
        self._version = None
        self.discriminator = None
        if state is not None:
            self.state = state
        if ordering is not None:
            self.ordering = ordering
        if counterparty is not None:
            self.counterparty = counterparty
        if connection_hops is not None:
            self.connection_hops = connection_hops
        if version is not None:
            self.version = version

    @property
    def state(self):
        """Gets the state of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501

        State defines if a channel is in one of the following states: CLOSED, INIT, TRYOPEN, OPEN or UNINITIALIZED.   - STATE_UNINITIALIZED_UNSPECIFIED: Default State  - STATE_INIT: A channel has just started the opening handshake.  - STATE_TRYOPEN: A channel has acknowledged the handshake step on the counterparty chain.  - STATE_OPEN: A channel has completed the handshake. Open channels are ready to send and receive packets.  - STATE_CLOSED: A channel has been closed and can no longer be used to send or receive packets.  # noqa: E501

        :return: The state of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ChannelAssociatedWithTheRequestIdentifiers.

        State defines if a channel is in one of the following states: CLOSED, INIT, TRYOPEN, OPEN or UNINITIALIZED.   - STATE_UNINITIALIZED_UNSPECIFIED: Default State  - STATE_INIT: A channel has just started the opening handshake.  - STATE_TRYOPEN: A channel has acknowledged the handshake step on the counterparty chain.  - STATE_OPEN: A channel has completed the handshake. Open channels are ready to send and receive packets.  - STATE_CLOSED: A channel has been closed and can no longer be used to send or receive packets.  # noqa: E501

        :param state: The state of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501
        :type: str
        """
        allowed_values = ["STATE_UNINITIALIZED_UNSPECIFIED", "STATE_INIT", "STATE_TRYOPEN", "STATE_OPEN", "STATE_CLOSED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def ordering(self):
        """Gets the ordering of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501

        - ORDER_NONE_UNSPECIFIED: zero-value for channel ordering  - ORDER_UNORDERED: packets can be delivered in any order, which may differ from the order in which they were sent.  - ORDER_ORDERED: packets are delivered exactly in the order which they were sent  # noqa: E501

        :return: The ordering of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._ordering

    @ordering.setter
    def ordering(self, ordering):
        """Sets the ordering of this ChannelAssociatedWithTheRequestIdentifiers.

        - ORDER_NONE_UNSPECIFIED: zero-value for channel ordering  - ORDER_UNORDERED: packets can be delivered in any order, which may differ from the order in which they were sent.  - ORDER_ORDERED: packets are delivered exactly in the order which they were sent  # noqa: E501

        :param ordering: The ordering of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501
        :type: str
        """
        allowed_values = ["ORDER_NONE_UNSPECIFIED", "ORDER_UNORDERED", "ORDER_ORDERED"]  # noqa: E501
        if ordering not in allowed_values:
            raise ValueError(
                "Invalid value for `ordering` ({0}), must be one of {1}"  # noqa: E501
                .format(ordering, allowed_values)
            )

        self._ordering = ordering

    @property
    def counterparty(self):
        """Gets the counterparty of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501


        :return: The counterparty of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501
        :rtype: CounterpartyChannelEnd
        """
        return self._counterparty

    @counterparty.setter
    def counterparty(self, counterparty):
        """Sets the counterparty of this ChannelAssociatedWithTheRequestIdentifiers.


        :param counterparty: The counterparty of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501
        :type: CounterpartyChannelEnd
        """

        self._counterparty = counterparty

    @property
    def connection_hops(self):
        """Gets the connection_hops of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501


        :return: The connection_hops of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501
        :rtype: list[str]
        """
        return self._connection_hops

    @connection_hops.setter
    def connection_hops(self, connection_hops):
        """Sets the connection_hops of this ChannelAssociatedWithTheRequestIdentifiers.


        :param connection_hops: The connection_hops of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501
        :type: list[str]
        """

        self._connection_hops = connection_hops

    @property
    def version(self):
        """Gets the version of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501


        :return: The version of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChannelAssociatedWithTheRequestIdentifiers.


        :param version: The version of this ChannelAssociatedWithTheRequestIdentifiers.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(ChannelAssociatedWithTheRequestIdentifiers, dict):
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
        if not isinstance(other, ChannelAssociatedWithTheRequestIdentifiers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
