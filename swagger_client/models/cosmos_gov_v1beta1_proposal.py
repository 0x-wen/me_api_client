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

class CosmosGovV1beta1Proposal(object):
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
        'proposal_id': 'str',
        'content': 'dict(str, object)',
        'status': 'str',
        'final_tally_result': 'CosmosGovV1beta1ProposalFinalTallyResult',
        'submit_time': 'datetime',
        'deposit_end_time': 'datetime',
        'total_deposit': 'list[CosmosBankV1beta1InputCoins]',
        'voting_start_time': 'datetime',
        'voting_end_time': 'datetime'
    }

    attribute_map = {
        'proposal_id': 'proposal_id',
        'content': 'content',
        'status': 'status',
        'final_tally_result': 'final_tally_result',
        'submit_time': 'submit_time',
        'deposit_end_time': 'deposit_end_time',
        'total_deposit': 'total_deposit',
        'voting_start_time': 'voting_start_time',
        'voting_end_time': 'voting_end_time'
    }

    def __init__(self, proposal_id=None, content=None, status='PROPOSAL_STATUS_UNSPECIFIED', final_tally_result=None, submit_time=None, deposit_end_time=None, total_deposit=None, voting_start_time=None, voting_end_time=None):  # noqa: E501
        """CosmosGovV1beta1Proposal - a model defined in Swagger"""  # noqa: E501
        self._proposal_id = None
        self._content = None
        self._status = None
        self._final_tally_result = None
        self._submit_time = None
        self._deposit_end_time = None
        self._total_deposit = None
        self._voting_start_time = None
        self._voting_end_time = None
        self.discriminator = None
        if proposal_id is not None:
            self.proposal_id = proposal_id
        if content is not None:
            self.content = content
        if status is not None:
            self.status = status
        if final_tally_result is not None:
            self.final_tally_result = final_tally_result
        if submit_time is not None:
            self.submit_time = submit_time
        if deposit_end_time is not None:
            self.deposit_end_time = deposit_end_time
        if total_deposit is not None:
            self.total_deposit = total_deposit
        if voting_start_time is not None:
            self.voting_start_time = voting_start_time
        if voting_end_time is not None:
            self.voting_end_time = voting_end_time

    @property
    def proposal_id(self):
        """Gets the proposal_id of this CosmosGovV1beta1Proposal.  # noqa: E501


        :return: The proposal_id of this CosmosGovV1beta1Proposal.  # noqa: E501
        :rtype: str
        """
        return self._proposal_id

    @proposal_id.setter
    def proposal_id(self, proposal_id):
        """Sets the proposal_id of this CosmosGovV1beta1Proposal.


        :param proposal_id: The proposal_id of this CosmosGovV1beta1Proposal.  # noqa: E501
        :type: str
        """

        self._proposal_id = proposal_id

    @property
    def content(self):
        """Gets the content of this CosmosGovV1beta1Proposal.  # noqa: E501

        `Any` contains an arbitrary serialized protocol buffer message along with a URL that describes the type of the serialized message.  Protobuf library provides support to pack/unpack Any values in the form of utility functions or additional generated methods of the Any type.  Example 1: Pack and unpack a message in C++.      Foo foo = ...;     Any any;     any.PackFrom(foo);     ...     if (any.UnpackTo(&foo)) {       ...     }  Example 2: Pack and unpack a message in Java.      Foo foo = ...;     Any any = Any.pack(foo);     ...     if (any.is(Foo.class)) {       foo = any.unpack(Foo.class);     }   Example 3: Pack and unpack a message in Python.      foo = Foo(...)     any = Any()     any.Pack(foo)     ...     if any.Is(Foo.DESCRIPTOR):       any.Unpack(foo)       ...   Example 4: Pack and unpack a message in Go       foo := &pb.Foo{...}      any, err := anypb.New(foo)      if err != nil {        ...      }      ...      foo := &pb.Foo{}      if err := any.UnmarshalTo(foo); err != nil {        ...      }  The pack methods provided by protobuf library will by default use 'type.googleapis.com/full.type.name' as the type URL and the unpack methods only use the fully qualified type name after the last '/' in the type URL, for example \"foo.bar.com/x/y.z\" will yield type name \"y.z\".   JSON ==== The JSON representation of an `Any` value uses the regular representation of the deserialized, embedded message, with an additional field `@type` which contains the type URL. Example:      package google.profile;     message Person {       string first_name = 1;       string last_name = 2;     }      {       \"@type\": \"type.googleapis.com/google.profile.Person\",       \"firstName\": <string>,       \"lastName\": <string>     }  If the embedded message type is well-known and has a custom JSON representation, that representation will be embedded adding a field `value` which holds the custom JSON in addition to the `@type` field. Example (for message [google.protobuf.Duration][]):      {       \"@type\": \"type.googleapis.com/google.protobuf.Duration\",       \"value\": \"1.212s\"     }  # noqa: E501

        :return: The content of this CosmosGovV1beta1Proposal.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CosmosGovV1beta1Proposal.

        `Any` contains an arbitrary serialized protocol buffer message along with a URL that describes the type of the serialized message.  Protobuf library provides support to pack/unpack Any values in the form of utility functions or additional generated methods of the Any type.  Example 1: Pack and unpack a message in C++.      Foo foo = ...;     Any any;     any.PackFrom(foo);     ...     if (any.UnpackTo(&foo)) {       ...     }  Example 2: Pack and unpack a message in Java.      Foo foo = ...;     Any any = Any.pack(foo);     ...     if (any.is(Foo.class)) {       foo = any.unpack(Foo.class);     }   Example 3: Pack and unpack a message in Python.      foo = Foo(...)     any = Any()     any.Pack(foo)     ...     if any.Is(Foo.DESCRIPTOR):       any.Unpack(foo)       ...   Example 4: Pack and unpack a message in Go       foo := &pb.Foo{...}      any, err := anypb.New(foo)      if err != nil {        ...      }      ...      foo := &pb.Foo{}      if err := any.UnmarshalTo(foo); err != nil {        ...      }  The pack methods provided by protobuf library will by default use 'type.googleapis.com/full.type.name' as the type URL and the unpack methods only use the fully qualified type name after the last '/' in the type URL, for example \"foo.bar.com/x/y.z\" will yield type name \"y.z\".   JSON ==== The JSON representation of an `Any` value uses the regular representation of the deserialized, embedded message, with an additional field `@type` which contains the type URL. Example:      package google.profile;     message Person {       string first_name = 1;       string last_name = 2;     }      {       \"@type\": \"type.googleapis.com/google.profile.Person\",       \"firstName\": <string>,       \"lastName\": <string>     }  If the embedded message type is well-known and has a custom JSON representation, that representation will be embedded adding a field `value` which holds the custom JSON in addition to the `@type` field. Example (for message [google.protobuf.Duration][]):      {       \"@type\": \"type.googleapis.com/google.protobuf.Duration\",       \"value\": \"1.212s\"     }  # noqa: E501

        :param content: The content of this CosmosGovV1beta1Proposal.  # noqa: E501
        :type: dict(str, object)
        """

        self._content = content

    @property
    def status(self):
        """Gets the status of this CosmosGovV1beta1Proposal.  # noqa: E501

        ProposalStatus enumerates the valid statuses of a proposal.   - PROPOSAL_STATUS_UNSPECIFIED: PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status.  - PROPOSAL_STATUS_DEPOSIT_PERIOD: PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit period.  - PROPOSAL_STATUS_VOTING_PERIOD: PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting period.  - PROPOSAL_STATUS_PASSED: PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has passed.  - PROPOSAL_STATUS_REJECTED: PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has been rejected.  - PROPOSAL_STATUS_FAILED: PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has failed.  # noqa: E501

        :return: The status of this CosmosGovV1beta1Proposal.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CosmosGovV1beta1Proposal.

        ProposalStatus enumerates the valid statuses of a proposal.   - PROPOSAL_STATUS_UNSPECIFIED: PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status.  - PROPOSAL_STATUS_DEPOSIT_PERIOD: PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit period.  - PROPOSAL_STATUS_VOTING_PERIOD: PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting period.  - PROPOSAL_STATUS_PASSED: PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has passed.  - PROPOSAL_STATUS_REJECTED: PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has been rejected.  - PROPOSAL_STATUS_FAILED: PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has failed.  # noqa: E501

        :param status: The status of this CosmosGovV1beta1Proposal.  # noqa: E501
        :type: str
        """
        allowed_values = ["PROPOSAL_STATUS_UNSPECIFIED", "PROPOSAL_STATUS_DEPOSIT_PERIOD", "PROPOSAL_STATUS_VOTING_PERIOD", "PROPOSAL_STATUS_PASSED", "PROPOSAL_STATUS_REJECTED", "PROPOSAL_STATUS_FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def final_tally_result(self):
        """Gets the final_tally_result of this CosmosGovV1beta1Proposal.  # noqa: E501


        :return: The final_tally_result of this CosmosGovV1beta1Proposal.  # noqa: E501
        :rtype: CosmosGovV1beta1ProposalFinalTallyResult
        """
        return self._final_tally_result

    @final_tally_result.setter
    def final_tally_result(self, final_tally_result):
        """Sets the final_tally_result of this CosmosGovV1beta1Proposal.


        :param final_tally_result: The final_tally_result of this CosmosGovV1beta1Proposal.  # noqa: E501
        :type: CosmosGovV1beta1ProposalFinalTallyResult
        """

        self._final_tally_result = final_tally_result

    @property
    def submit_time(self):
        """Gets the submit_time of this CosmosGovV1beta1Proposal.  # noqa: E501


        :return: The submit_time of this CosmosGovV1beta1Proposal.  # noqa: E501
        :rtype: datetime
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """Sets the submit_time of this CosmosGovV1beta1Proposal.


        :param submit_time: The submit_time of this CosmosGovV1beta1Proposal.  # noqa: E501
        :type: datetime
        """

        self._submit_time = submit_time

    @property
    def deposit_end_time(self):
        """Gets the deposit_end_time of this CosmosGovV1beta1Proposal.  # noqa: E501


        :return: The deposit_end_time of this CosmosGovV1beta1Proposal.  # noqa: E501
        :rtype: datetime
        """
        return self._deposit_end_time

    @deposit_end_time.setter
    def deposit_end_time(self, deposit_end_time):
        """Sets the deposit_end_time of this CosmosGovV1beta1Proposal.


        :param deposit_end_time: The deposit_end_time of this CosmosGovV1beta1Proposal.  # noqa: E501
        :type: datetime
        """

        self._deposit_end_time = deposit_end_time

    @property
    def total_deposit(self):
        """Gets the total_deposit of this CosmosGovV1beta1Proposal.  # noqa: E501


        :return: The total_deposit of this CosmosGovV1beta1Proposal.  # noqa: E501
        :rtype: list[CosmosBankV1beta1InputCoins]
        """
        return self._total_deposit

    @total_deposit.setter
    def total_deposit(self, total_deposit):
        """Sets the total_deposit of this CosmosGovV1beta1Proposal.


        :param total_deposit: The total_deposit of this CosmosGovV1beta1Proposal.  # noqa: E501
        :type: list[CosmosBankV1beta1InputCoins]
        """

        self._total_deposit = total_deposit

    @property
    def voting_start_time(self):
        """Gets the voting_start_time of this CosmosGovV1beta1Proposal.  # noqa: E501


        :return: The voting_start_time of this CosmosGovV1beta1Proposal.  # noqa: E501
        :rtype: datetime
        """
        return self._voting_start_time

    @voting_start_time.setter
    def voting_start_time(self, voting_start_time):
        """Sets the voting_start_time of this CosmosGovV1beta1Proposal.


        :param voting_start_time: The voting_start_time of this CosmosGovV1beta1Proposal.  # noqa: E501
        :type: datetime
        """

        self._voting_start_time = voting_start_time

    @property
    def voting_end_time(self):
        """Gets the voting_end_time of this CosmosGovV1beta1Proposal.  # noqa: E501


        :return: The voting_end_time of this CosmosGovV1beta1Proposal.  # noqa: E501
        :rtype: datetime
        """
        return self._voting_end_time

    @voting_end_time.setter
    def voting_end_time(self, voting_end_time):
        """Sets the voting_end_time of this CosmosGovV1beta1Proposal.


        :param voting_end_time: The voting_end_time of this CosmosGovV1beta1Proposal.  # noqa: E501
        :type: datetime
        """

        self._voting_end_time = voting_end_time

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
        if issubclass(CosmosGovV1beta1Proposal, dict):
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
        if not isinstance(other, CosmosGovV1beta1Proposal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
