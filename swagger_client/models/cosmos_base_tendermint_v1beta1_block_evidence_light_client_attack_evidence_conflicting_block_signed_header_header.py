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

class CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader(object):
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
        'version': 'BasicBlockInfo',
        'chain_id': 'str',
        'height': 'str',
        'time': 'datetime',
        'last_block_id': 'BlockID',
        'last_commit_hash': 'str',
        'data_hash': 'str',
        'validators_hash': 'str',
        'next_validators_hash': 'str',
        'consensus_hash': 'str',
        'app_hash': 'str',
        'last_results_hash': 'str',
        'evidence_hash': 'str',
        'proposer_address': 'str'
    }

    attribute_map = {
        'version': 'version',
        'chain_id': 'chain_id',
        'height': 'height',
        'time': 'time',
        'last_block_id': 'last_block_id',
        'last_commit_hash': 'last_commit_hash',
        'data_hash': 'data_hash',
        'validators_hash': 'validators_hash',
        'next_validators_hash': 'next_validators_hash',
        'consensus_hash': 'consensus_hash',
        'app_hash': 'app_hash',
        'last_results_hash': 'last_results_hash',
        'evidence_hash': 'evidence_hash',
        'proposer_address': 'proposer_address'
    }

    def __init__(self, version=None, chain_id=None, height=None, time=None, last_block_id=None, last_commit_hash=None, data_hash=None, validators_hash=None, next_validators_hash=None, consensus_hash=None, app_hash=None, last_results_hash=None, evidence_hash=None, proposer_address=None):  # noqa: E501
        """CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._chain_id = None
        self._height = None
        self._time = None
        self._last_block_id = None
        self._last_commit_hash = None
        self._data_hash = None
        self._validators_hash = None
        self._next_validators_hash = None
        self._consensus_hash = None
        self._app_hash = None
        self._last_results_hash = None
        self._evidence_hash = None
        self._proposer_address = None
        self.discriminator = None
        if version is not None:
            self.version = version
        if chain_id is not None:
            self.chain_id = chain_id
        if height is not None:
            self.height = height
        if time is not None:
            self.time = time
        if last_block_id is not None:
            self.last_block_id = last_block_id
        if last_commit_hash is not None:
            self.last_commit_hash = last_commit_hash
        if data_hash is not None:
            self.data_hash = data_hash
        if validators_hash is not None:
            self.validators_hash = validators_hash
        if next_validators_hash is not None:
            self.next_validators_hash = next_validators_hash
        if consensus_hash is not None:
            self.consensus_hash = consensus_hash
        if app_hash is not None:
            self.app_hash = app_hash
        if last_results_hash is not None:
            self.last_results_hash = last_results_hash
        if evidence_hash is not None:
            self.evidence_hash = evidence_hash
        if proposer_address is not None:
            self.proposer_address = proposer_address

    @property
    def version(self):
        """Gets the version of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The version of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: BasicBlockInfo
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param version: The version of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: BasicBlockInfo
        """

        self._version = version

    @property
    def chain_id(self):
        """Gets the chain_id of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The chain_id of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id):
        """Sets the chain_id of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param chain_id: The chain_id of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._chain_id = chain_id

    @property
    def height(self):
        """Gets the height of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The height of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param height: The height of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def time(self):
        """Gets the time of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The time of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param time: The time of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def last_block_id(self):
        """Gets the last_block_id of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The last_block_id of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: BlockID
        """
        return self._last_block_id

    @last_block_id.setter
    def last_block_id(self, last_block_id):
        """Sets the last_block_id of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param last_block_id: The last_block_id of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: BlockID
        """

        self._last_block_id = last_block_id

    @property
    def last_commit_hash(self):
        """Gets the last_commit_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501

        commit from validators from the last block  # noqa: E501

        :return: The last_commit_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._last_commit_hash

    @last_commit_hash.setter
    def last_commit_hash(self, last_commit_hash):
        """Sets the last_commit_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.

        commit from validators from the last block  # noqa: E501

        :param last_commit_hash: The last_commit_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._last_commit_hash = last_commit_hash

    @property
    def data_hash(self):
        """Gets the data_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The data_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._data_hash

    @data_hash.setter
    def data_hash(self, data_hash):
        """Sets the data_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param data_hash: The data_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._data_hash = data_hash

    @property
    def validators_hash(self):
        """Gets the validators_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501

        validators for the current block  # noqa: E501

        :return: The validators_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._validators_hash

    @validators_hash.setter
    def validators_hash(self, validators_hash):
        """Sets the validators_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.

        validators for the current block  # noqa: E501

        :param validators_hash: The validators_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._validators_hash = validators_hash

    @property
    def next_validators_hash(self):
        """Gets the next_validators_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The next_validators_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._next_validators_hash

    @next_validators_hash.setter
    def next_validators_hash(self, next_validators_hash):
        """Sets the next_validators_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param next_validators_hash: The next_validators_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._next_validators_hash = next_validators_hash

    @property
    def consensus_hash(self):
        """Gets the consensus_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The consensus_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._consensus_hash

    @consensus_hash.setter
    def consensus_hash(self, consensus_hash):
        """Sets the consensus_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param consensus_hash: The consensus_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._consensus_hash = consensus_hash

    @property
    def app_hash(self):
        """Gets the app_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The app_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._app_hash

    @app_hash.setter
    def app_hash(self, app_hash):
        """Sets the app_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param app_hash: The app_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._app_hash = app_hash

    @property
    def last_results_hash(self):
        """Gets the last_results_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The last_results_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._last_results_hash

    @last_results_hash.setter
    def last_results_hash(self, last_results_hash):
        """Sets the last_results_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param last_results_hash: The last_results_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._last_results_hash = last_results_hash

    @property
    def evidence_hash(self):
        """Gets the evidence_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501

        evidence included in the block  # noqa: E501

        :return: The evidence_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._evidence_hash

    @evidence_hash.setter
    def evidence_hash(self, evidence_hash):
        """Sets the evidence_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.

        evidence included in the block  # noqa: E501

        :param evidence_hash: The evidence_hash of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._evidence_hash = evidence_hash

    @property
    def proposer_address(self):
        """Gets the proposer_address of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501


        :return: The proposer_address of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :rtype: str
        """
        return self._proposer_address

    @proposer_address.setter
    def proposer_address(self, proposer_address):
        """Sets the proposer_address of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.


        :param proposer_address: The proposer_address of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader.  # noqa: E501
        :type: str
        """

        self._proposer_address = proposer_address

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
        if issubclass(CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader, dict):
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
        if not isinstance(other, CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
