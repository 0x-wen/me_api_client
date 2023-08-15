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

class CosmosGovV1TallyParams(object):
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
        'quorum': 'str',
        'threshold': 'str',
        'veto_threshold': 'str'
    }

    attribute_map = {
        'quorum': 'quorum',
        'threshold': 'threshold',
        'veto_threshold': 'veto_threshold'
    }

    def __init__(self, quorum=None, threshold=None, veto_threshold=None):  # noqa: E501
        """CosmosGovV1TallyParams - a model defined in Swagger"""  # noqa: E501
        self._quorum = None
        self._threshold = None
        self._veto_threshold = None
        self.discriminator = None
        if quorum is not None:
            self.quorum = quorum
        if threshold is not None:
            self.threshold = threshold
        if veto_threshold is not None:
            self.veto_threshold = veto_threshold

    @property
    def quorum(self):
        """Gets the quorum of this CosmosGovV1TallyParams.  # noqa: E501

        Minimum percentage of total stake needed to vote for a result to be  considered valid.  # noqa: E501

        :return: The quorum of this CosmosGovV1TallyParams.  # noqa: E501
        :rtype: str
        """
        return self._quorum

    @quorum.setter
    def quorum(self, quorum):
        """Sets the quorum of this CosmosGovV1TallyParams.

        Minimum percentage of total stake needed to vote for a result to be  considered valid.  # noqa: E501

        :param quorum: The quorum of this CosmosGovV1TallyParams.  # noqa: E501
        :type: str
        """

        self._quorum = quorum

    @property
    def threshold(self):
        """Gets the threshold of this CosmosGovV1TallyParams.  # noqa: E501

        Minimum proportion of Yes votes for proposal to pass. Default value: 0.5.  # noqa: E501

        :return: The threshold of this CosmosGovV1TallyParams.  # noqa: E501
        :rtype: str
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this CosmosGovV1TallyParams.

        Minimum proportion of Yes votes for proposal to pass. Default value: 0.5.  # noqa: E501

        :param threshold: The threshold of this CosmosGovV1TallyParams.  # noqa: E501
        :type: str
        """

        self._threshold = threshold

    @property
    def veto_threshold(self):
        """Gets the veto_threshold of this CosmosGovV1TallyParams.  # noqa: E501

        Minimum value of Veto votes to Total votes ratio for proposal to be  vetoed. Default value: 1/3.  # noqa: E501

        :return: The veto_threshold of this CosmosGovV1TallyParams.  # noqa: E501
        :rtype: str
        """
        return self._veto_threshold

    @veto_threshold.setter
    def veto_threshold(self, veto_threshold):
        """Sets the veto_threshold of this CosmosGovV1TallyParams.

        Minimum value of Veto votes to Total votes ratio for proposal to be  vetoed. Default value: 1/3.  # noqa: E501

        :param veto_threshold: The veto_threshold of this CosmosGovV1TallyParams.  # noqa: E501
        :type: str
        """

        self._veto_threshold = veto_threshold

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
        if issubclass(CosmosGovV1TallyParams, dict):
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
        if not isinstance(other, CosmosGovV1TallyParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
