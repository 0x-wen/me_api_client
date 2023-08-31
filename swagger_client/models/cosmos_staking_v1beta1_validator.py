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

class CosmosStakingV1beta1Validator(object):
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
        'operator_address': 'str',
        'consensus_pubkey': 'dict(str, object)',
        'jailed': 'bool',
        'status': 'str',
        'tokens': 'str',
        'staker_shares': 'str',
        'description': 'CosmosStakingV1beta1HistoricalInfoDescription',
        'unbonding_height': 'str',
        'unbonding_time': 'datetime',
        'commission': 'CosmosStakingV1beta1HistoricalInfoCommission',
        'min_self_stake': 'str',
        'unbonding_on_hold_ref_count': 'str',
        'unbonding_ids': 'list[str]',
        'delegation_amount': 'str',
        'kyc_amount': 'str',
        'owner_address': 'str'
    }

    attribute_map = {
        'operator_address': 'operator_address',
        'consensus_pubkey': 'consensus_pubkey',
        'jailed': 'jailed',
        'status': 'status',
        'tokens': 'tokens',
        'staker_shares': 'staker_shares',
        'description': 'description',
        'unbonding_height': 'unbonding_height',
        'unbonding_time': 'unbonding_time',
        'commission': 'commission',
        'min_self_stake': 'min_self_stake',
        'unbonding_on_hold_ref_count': 'unbonding_on_hold_ref_count',
        'unbonding_ids': 'unbonding_ids',
        'delegation_amount': 'delegation_amount',
        'kyc_amount': 'kyc_amount',
        'owner_address': 'owner_address'
    }

    def __init__(self, operator_address=None, consensus_pubkey=None, jailed=None, status='BOND_STATUS_UNSPECIFIED', tokens=None, staker_shares=None, description=None, unbonding_height=None, unbonding_time=None, commission=None, min_self_stake=None, unbonding_on_hold_ref_count=None, unbonding_ids=None, delegation_amount=None, kyc_amount=None, owner_address=None):  # noqa: E501
        """CosmosStakingV1beta1Validator - a model defined in Swagger"""  # noqa: E501
        self._operator_address = None
        self._consensus_pubkey = None
        self._jailed = None
        self._status = None
        self._tokens = None
        self._staker_shares = None
        self._description = None
        self._unbonding_height = None
        self._unbonding_time = None
        self._commission = None
        self._min_self_stake = None
        self._unbonding_on_hold_ref_count = None
        self._unbonding_ids = None
        self._delegation_amount = None
        self._kyc_amount = None
        self._owner_address = None
        self.discriminator = None
        if operator_address is not None:
            self.operator_address = operator_address
        if consensus_pubkey is not None:
            self.consensus_pubkey = consensus_pubkey
        if jailed is not None:
            self.jailed = jailed
        if status is not None:
            self.status = status
        if tokens is not None:
            self.tokens = tokens
        if staker_shares is not None:
            self.staker_shares = staker_shares
        if description is not None:
            self.description = description
        if unbonding_height is not None:
            self.unbonding_height = unbonding_height
        if unbonding_time is not None:
            self.unbonding_time = unbonding_time
        if commission is not None:
            self.commission = commission
        if min_self_stake is not None:
            self.min_self_stake = min_self_stake
        if unbonding_on_hold_ref_count is not None:
            self.unbonding_on_hold_ref_count = unbonding_on_hold_ref_count
        if unbonding_ids is not None:
            self.unbonding_ids = unbonding_ids
        if delegation_amount is not None:
            self.delegation_amount = delegation_amount
        if kyc_amount is not None:
            self.kyc_amount = kyc_amount
        if owner_address is not None:
            self.owner_address = owner_address

    @property
    def operator_address(self):
        """Gets the operator_address of this CosmosStakingV1beta1Validator.  # noqa: E501

        operator_address defines the address of the validator's operator; bech encoded in JSON.  # noqa: E501

        :return: The operator_address of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: str
        """
        return self._operator_address

    @operator_address.setter
    def operator_address(self, operator_address):
        """Sets the operator_address of this CosmosStakingV1beta1Validator.

        operator_address defines the address of the validator's operator; bech encoded in JSON.  # noqa: E501

        :param operator_address: The operator_address of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: str
        """

        self._operator_address = operator_address

    @property
    def consensus_pubkey(self):
        """Gets the consensus_pubkey of this CosmosStakingV1beta1Validator.  # noqa: E501

        consensus_pubkey is the consensus public key of the validator, as a Protobuf Any.  # noqa: E501

        :return: The consensus_pubkey of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._consensus_pubkey

    @consensus_pubkey.setter
    def consensus_pubkey(self, consensus_pubkey):
        """Sets the consensus_pubkey of this CosmosStakingV1beta1Validator.

        consensus_pubkey is the consensus public key of the validator, as a Protobuf Any.  # noqa: E501

        :param consensus_pubkey: The consensus_pubkey of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: dict(str, object)
        """

        self._consensus_pubkey = consensus_pubkey

    @property
    def jailed(self):
        """Gets the jailed of this CosmosStakingV1beta1Validator.  # noqa: E501

        jailed defined whether the validator has been jailed from bonded status or not.  # noqa: E501

        :return: The jailed of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: bool
        """
        return self._jailed

    @jailed.setter
    def jailed(self, jailed):
        """Sets the jailed of this CosmosStakingV1beta1Validator.

        jailed defined whether the validator has been jailed from bonded status or not.  # noqa: E501

        :param jailed: The jailed of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: bool
        """

        self._jailed = jailed

    @property
    def status(self):
        """Gets the status of this CosmosStakingV1beta1Validator.  # noqa: E501

        status is the validator status (bonded/unbonding/unbonded).  # noqa: E501

        :return: The status of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CosmosStakingV1beta1Validator.

        status is the validator status (bonded/unbonding/unbonded).  # noqa: E501

        :param status: The status of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: str
        """
        allowed_values = ["BOND_STATUS_UNSPECIFIED", "BOND_STATUS_UNBONDED", "BOND_STATUS_UNBONDING", "BOND_STATUS_BONDED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tokens(self):
        """Gets the tokens of this CosmosStakingV1beta1Validator.  # noqa: E501

        tokens define the staked tokens (incl. self-stake).  # noqa: E501

        :return: The tokens of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: str
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this CosmosStakingV1beta1Validator.

        tokens define the staked tokens (incl. self-stake).  # noqa: E501

        :param tokens: The tokens of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: str
        """

        self._tokens = tokens

    @property
    def staker_shares(self):
        """Gets the staker_shares of this CosmosStakingV1beta1Validator.  # noqa: E501

        staker_shares defines total shares issued to a validator's stakers.  # noqa: E501

        :return: The staker_shares of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: str
        """
        return self._staker_shares

    @staker_shares.setter
    def staker_shares(self, staker_shares):
        """Sets the staker_shares of this CosmosStakingV1beta1Validator.

        staker_shares defines total shares issued to a validator's stakers.  # noqa: E501

        :param staker_shares: The staker_shares of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: str
        """

        self._staker_shares = staker_shares

    @property
    def description(self):
        """Gets the description of this CosmosStakingV1beta1Validator.  # noqa: E501


        :return: The description of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: CosmosStakingV1beta1HistoricalInfoDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CosmosStakingV1beta1Validator.


        :param description: The description of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: CosmosStakingV1beta1HistoricalInfoDescription
        """

        self._description = description

    @property
    def unbonding_height(self):
        """Gets the unbonding_height of this CosmosStakingV1beta1Validator.  # noqa: E501

        unbonding_height defines, if unbonding, the height at which this validator has begun unbonding.  # noqa: E501

        :return: The unbonding_height of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: str
        """
        return self._unbonding_height

    @unbonding_height.setter
    def unbonding_height(self, unbonding_height):
        """Sets the unbonding_height of this CosmosStakingV1beta1Validator.

        unbonding_height defines, if unbonding, the height at which this validator has begun unbonding.  # noqa: E501

        :param unbonding_height: The unbonding_height of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: str
        """

        self._unbonding_height = unbonding_height

    @property
    def unbonding_time(self):
        """Gets the unbonding_time of this CosmosStakingV1beta1Validator.  # noqa: E501

        unbonding_time defines, if unbonding, the min time for the validator to complete unbonding.  # noqa: E501

        :return: The unbonding_time of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: datetime
        """
        return self._unbonding_time

    @unbonding_time.setter
    def unbonding_time(self, unbonding_time):
        """Sets the unbonding_time of this CosmosStakingV1beta1Validator.

        unbonding_time defines, if unbonding, the min time for the validator to complete unbonding.  # noqa: E501

        :param unbonding_time: The unbonding_time of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: datetime
        """

        self._unbonding_time = unbonding_time

    @property
    def commission(self):
        """Gets the commission of this CosmosStakingV1beta1Validator.  # noqa: E501


        :return: The commission of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: CosmosStakingV1beta1HistoricalInfoCommission
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """Sets the commission of this CosmosStakingV1beta1Validator.


        :param commission: The commission of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: CosmosStakingV1beta1HistoricalInfoCommission
        """

        self._commission = commission

    @property
    def min_self_stake(self):
        """Gets the min_self_stake of this CosmosStakingV1beta1Validator.  # noqa: E501

        min_self_stake is the validator's self declared minimum self stake.  Since: cosmos-sdk 0.46  # noqa: E501

        :return: The min_self_stake of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: str
        """
        return self._min_self_stake

    @min_self_stake.setter
    def min_self_stake(self, min_self_stake):
        """Sets the min_self_stake of this CosmosStakingV1beta1Validator.

        min_self_stake is the validator's self declared minimum self stake.  Since: cosmos-sdk 0.46  # noqa: E501

        :param min_self_stake: The min_self_stake of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: str
        """

        self._min_self_stake = min_self_stake

    @property
    def unbonding_on_hold_ref_count(self):
        """Gets the unbonding_on_hold_ref_count of this CosmosStakingV1beta1Validator.  # noqa: E501


        :return: The unbonding_on_hold_ref_count of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: str
        """
        return self._unbonding_on_hold_ref_count

    @unbonding_on_hold_ref_count.setter
    def unbonding_on_hold_ref_count(self, unbonding_on_hold_ref_count):
        """Sets the unbonding_on_hold_ref_count of this CosmosStakingV1beta1Validator.


        :param unbonding_on_hold_ref_count: The unbonding_on_hold_ref_count of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: str
        """

        self._unbonding_on_hold_ref_count = unbonding_on_hold_ref_count

    @property
    def unbonding_ids(self):
        """Gets the unbonding_ids of this CosmosStakingV1beta1Validator.  # noqa: E501


        :return: The unbonding_ids of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: list[str]
        """
        return self._unbonding_ids

    @unbonding_ids.setter
    def unbonding_ids(self, unbonding_ids):
        """Sets the unbonding_ids of this CosmosStakingV1beta1Validator.


        :param unbonding_ids: The unbonding_ids of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: list[str]
        """

        self._unbonding_ids = unbonding_ids

    @property
    def delegation_amount(self):
        """Gets the delegation_amount of this CosmosStakingV1beta1Validator.  # noqa: E501


        :return: The delegation_amount of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: str
        """
        return self._delegation_amount

    @delegation_amount.setter
    def delegation_amount(self, delegation_amount):
        """Sets the delegation_amount of this CosmosStakingV1beta1Validator.


        :param delegation_amount: The delegation_amount of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: str
        """

        self._delegation_amount = delegation_amount

    @property
    def kyc_amount(self):
        """Gets the kyc_amount of this CosmosStakingV1beta1Validator.  # noqa: E501


        :return: The kyc_amount of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: str
        """
        return self._kyc_amount

    @kyc_amount.setter
    def kyc_amount(self, kyc_amount):
        """Sets the kyc_amount of this CosmosStakingV1beta1Validator.


        :param kyc_amount: The kyc_amount of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: str
        """

        self._kyc_amount = kyc_amount

    @property
    def owner_address(self):
        """Gets the owner_address of this CosmosStakingV1beta1Validator.  # noqa: E501


        :return: The owner_address of this CosmosStakingV1beta1Validator.  # noqa: E501
        :rtype: str
        """
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address):
        """Sets the owner_address of this CosmosStakingV1beta1Validator.


        :param owner_address: The owner_address of this CosmosStakingV1beta1Validator.  # noqa: E501
        :type: str
        """

        self._owner_address = owner_address

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
        if issubclass(CosmosStakingV1beta1Validator, dict):
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
        if not isinstance(other, CosmosStakingV1beta1Validator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
