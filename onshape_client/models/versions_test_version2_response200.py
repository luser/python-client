# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.87
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VersionsTestVersion2Response200(object):
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
        'supported_versions': 'list[float]',
        'earliest_version': 'float'
    }

    attribute_map = {
        'supported_versions': 'supportedVersions',
        'earliest_version': 'earliestVersion'
    }

    def __init__(self, supported_versions=None, earliest_version=None):  # noqa: E501
        """VersionsTestVersion2Response200 - a model defined in Swagger"""  # noqa: E501

        self._supported_versions = None
        self._earliest_version = None
        self.discriminator = None

        if supported_versions is not None:
            self.supported_versions = supported_versions
        if earliest_version is not None:
            self.earliest_version = earliest_version

    @property
    def supported_versions(self):
        """Gets the supported_versions of this VersionsTestVersion2Response200.  # noqa: E501

        The list of supported version numbers  # noqa: E501

        :return: The supported_versions of this VersionsTestVersion2Response200.  # noqa: E501
        :rtype: list[float]
        """
        return self._supported_versions

    @supported_versions.setter
    def supported_versions(self, supported_versions):
        """Sets the supported_versions of this VersionsTestVersion2Response200.

        The list of supported version numbers  # noqa: E501

        :param supported_versions: The supported_versions of this VersionsTestVersion2Response200.  # noqa: E501
        :type: list[float]
        """

        self._supported_versions = supported_versions

    @property
    def earliest_version(self):
        """Gets the earliest_version of this VersionsTestVersion2Response200.  # noqa: E501

        The earliest support version  # noqa: E501

        :return: The earliest_version of this VersionsTestVersion2Response200.  # noqa: E501
        :rtype: float
        """
        return self._earliest_version

    @earliest_version.setter
    def earliest_version(self, earliest_version):
        """Sets the earliest_version of this VersionsTestVersion2Response200.

        The earliest support version  # noqa: E501

        :param earliest_version: The earliest_version of this VersionsTestVersion2Response200.  # noqa: E501
        :type: float
        """

        self._earliest_version = earliest_version

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VersionsTestVersion2Response200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
