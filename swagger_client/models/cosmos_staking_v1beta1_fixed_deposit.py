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

class CosmosStakingV1beta1FixedDeposit(object):
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
        'id': 'str',
        'account': 'str',
        'principal': 'CosmosBankV1beta1InputCoins',
        'interest': 'CosmosBankV1beta1InputCoins',
        'start_time': 'datetime',
        'end_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'account': 'account',
        'principal': 'principal',
        'interest': 'interest',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, account=None, principal=None, interest=None, start_time=None, end_time=None):  # noqa: E501
        """CosmosStakingV1beta1FixedDeposit - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._account = None
        self._principal = None
        self._interest = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if account is not None:
            self.account = account
        if principal is not None:
            self.principal = principal
        if interest is not None:
            self.interest = interest
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501


        :return: The id of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CosmosStakingV1beta1FixedDeposit.


        :param id: The id of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account(self):
        """Gets the account of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501


        :return: The account of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this CosmosStakingV1beta1FixedDeposit.


        :param account: The account of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def principal(self):
        """Gets the principal of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501


        :return: The principal of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :rtype: CosmosBankV1beta1InputCoins
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this CosmosStakingV1beta1FixedDeposit.


        :param principal: The principal of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :type: CosmosBankV1beta1InputCoins
        """

        self._principal = principal

    @property
    def interest(self):
        """Gets the interest of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501


        :return: The interest of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :rtype: CosmosBankV1beta1InputCoins
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this CosmosStakingV1beta1FixedDeposit.


        :param interest: The interest of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :type: CosmosBankV1beta1InputCoins
        """

        self._interest = interest

    @property
    def start_time(self):
        """Gets the start_time of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501


        :return: The start_time of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CosmosStakingV1beta1FixedDeposit.


        :param start_time: The start_time of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501


        :return: The end_time of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CosmosStakingV1beta1FixedDeposit.


        :param end_time: The end_time of this CosmosStakingV1beta1FixedDeposit.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

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
        if issubclass(CosmosStakingV1beta1FixedDeposit, dict):
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
        if not isinstance(other, CosmosStakingV1beta1FixedDeposit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
