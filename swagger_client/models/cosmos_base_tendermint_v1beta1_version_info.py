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

class CosmosBaseTendermintV1beta1VersionInfo(object):
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
        'name': 'str',
        'app_name': 'str',
        'version': 'str',
        'git_commit': 'str',
        'build_tags': 'str',
        'go_version': 'str',
        'build_deps': 'list[ModuleIsTheTypeForVersionInfo]',
        'cosmos_sdk_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'app_name': 'app_name',
        'version': 'version',
        'git_commit': 'git_commit',
        'build_tags': 'build_tags',
        'go_version': 'go_version',
        'build_deps': 'build_deps',
        'cosmos_sdk_version': 'cosmos_sdk_version'
    }

    def __init__(self, name=None, app_name=None, version=None, git_commit=None, build_tags=None, go_version=None, build_deps=None, cosmos_sdk_version=None):  # noqa: E501
        """CosmosBaseTendermintV1beta1VersionInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._app_name = None
        self._version = None
        self._git_commit = None
        self._build_tags = None
        self._go_version = None
        self._build_deps = None
        self._cosmos_sdk_version = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if app_name is not None:
            self.app_name = app_name
        if version is not None:
            self.version = version
        if git_commit is not None:
            self.git_commit = git_commit
        if build_tags is not None:
            self.build_tags = build_tags
        if go_version is not None:
            self.go_version = go_version
        if build_deps is not None:
            self.build_deps = build_deps
        if cosmos_sdk_version is not None:
            self.cosmos_sdk_version = cosmos_sdk_version

    @property
    def name(self):
        """Gets the name of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501


        :return: The name of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CosmosBaseTendermintV1beta1VersionInfo.


        :param name: The name of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def app_name(self):
        """Gets the app_name of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501


        :return: The app_name of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this CosmosBaseTendermintV1beta1VersionInfo.


        :param app_name: The app_name of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :type: str
        """

        self._app_name = app_name

    @property
    def version(self):
        """Gets the version of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501


        :return: The version of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CosmosBaseTendermintV1beta1VersionInfo.


        :param version: The version of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def git_commit(self):
        """Gets the git_commit of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501


        :return: The git_commit of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._git_commit

    @git_commit.setter
    def git_commit(self, git_commit):
        """Sets the git_commit of this CosmosBaseTendermintV1beta1VersionInfo.


        :param git_commit: The git_commit of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :type: str
        """

        self._git_commit = git_commit

    @property
    def build_tags(self):
        """Gets the build_tags of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501


        :return: The build_tags of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._build_tags

    @build_tags.setter
    def build_tags(self, build_tags):
        """Sets the build_tags of this CosmosBaseTendermintV1beta1VersionInfo.


        :param build_tags: The build_tags of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :type: str
        """

        self._build_tags = build_tags

    @property
    def go_version(self):
        """Gets the go_version of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501


        :return: The go_version of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._go_version

    @go_version.setter
    def go_version(self, go_version):
        """Sets the go_version of this CosmosBaseTendermintV1beta1VersionInfo.


        :param go_version: The go_version of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :type: str
        """

        self._go_version = go_version

    @property
    def build_deps(self):
        """Gets the build_deps of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501


        :return: The build_deps of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :rtype: list[ModuleIsTheTypeForVersionInfo]
        """
        return self._build_deps

    @build_deps.setter
    def build_deps(self, build_deps):
        """Sets the build_deps of this CosmosBaseTendermintV1beta1VersionInfo.


        :param build_deps: The build_deps of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :type: list[ModuleIsTheTypeForVersionInfo]
        """

        self._build_deps = build_deps

    @property
    def cosmos_sdk_version(self):
        """Gets the cosmos_sdk_version of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501


        :return: The cosmos_sdk_version of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._cosmos_sdk_version

    @cosmos_sdk_version.setter
    def cosmos_sdk_version(self, cosmos_sdk_version):
        """Sets the cosmos_sdk_version of this CosmosBaseTendermintV1beta1VersionInfo.


        :param cosmos_sdk_version: The cosmos_sdk_version of this CosmosBaseTendermintV1beta1VersionInfo.  # noqa: E501
        :type: str
        """

        self._cosmos_sdk_version = cosmos_sdk_version

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
        if issubclass(CosmosBaseTendermintV1beta1VersionInfo, dict):
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
        if not isinstance(other, CosmosBaseTendermintV1beta1VersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other