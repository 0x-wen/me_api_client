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

class QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved(object):
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
        'commitment': 'str',
        'proof': 'str',
        'proof_height': 'HeightAtWhichTheProofWasRetrieved'
    }

    attribute_map = {
        'commitment': 'commitment',
        'proof': 'proof',
        'proof_height': 'proof_height'
    }

    def __init__(self, commitment=None, proof=None, proof_height=None):  # noqa: E501
        """QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved - a model defined in Swagger"""  # noqa: E501
        self._commitment = None
        self._proof = None
        self._proof_height = None
        self.discriminator = None
        if commitment is not None:
            self.commitment = commitment
        if proof is not None:
            self.proof = proof
        if proof_height is not None:
            self.proof_height = proof_height

    @property
    def commitment(self):
        """Gets the commitment of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.  # noqa: E501


        :return: The commitment of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.  # noqa: E501
        :rtype: str
        """
        return self._commitment

    @commitment.setter
    def commitment(self, commitment):
        """Sets the commitment of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.


        :param commitment: The commitment of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.  # noqa: E501
        :type: str
        """

        self._commitment = commitment

    @property
    def proof(self):
        """Gets the proof of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.  # noqa: E501


        :return: The proof of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.  # noqa: E501
        :rtype: str
        """
        return self._proof

    @proof.setter
    def proof(self, proof):
        """Sets the proof of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.


        :param proof: The proof of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.  # noqa: E501
        :type: str
        """

        self._proof = proof

    @property
    def proof_height(self):
        """Gets the proof_height of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.  # noqa: E501


        :return: The proof_height of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.  # noqa: E501
        :rtype: HeightAtWhichTheProofWasRetrieved
        """
        return self._proof_height

    @proof_height.setter
    def proof_height(self, proof_height):
        """Sets the proof_height of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.


        :param proof_height: The proof_height of this QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved.  # noqa: E501
        :type: HeightAtWhichTheProofWasRetrieved
        """

        self._proof_height = proof_height

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
        if issubclass(QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved, dict):
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
        if not isinstance(other, QueryPacketCommitmentResponseDefinesTheClientQueryResponseForAPacketwhichAlsoIncludesAProofAndTheHeightFromWhichTheProofWasretrieved):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
