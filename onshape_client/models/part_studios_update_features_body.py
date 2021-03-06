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


class PartStudiosUpdateFeaturesBody(object):
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
        'serialization_version': 'str',
        'reject_microversion_skew': 'bool',
        'update_suppression_attributes': 'bool',
        'features': 'list[object]',
        'source_microversion': 'str'
    }

    attribute_map = {
        'serialization_version': 'serializationVersion',
        'reject_microversion_skew': 'rejectMicroversionSkew',
        'update_suppression_attributes': 'updateSuppressionAttributes',
        'features': 'features',
        'source_microversion': 'sourceMicroversion'
    }

    def __init__(self, serialization_version=None, reject_microversion_skew=None, update_suppression_attributes=None, features=None, source_microversion=None):  # noqa: E501
        """PartStudiosUpdateFeaturesBody - a model defined in Swagger"""  # noqa: E501

        self._serialization_version = None
        self._reject_microversion_skew = None
        self._update_suppression_attributes = None
        self._features = None
        self._source_microversion = None
        self.discriminator = None

        if serialization_version is not None:
            self.serialization_version = serialization_version
        if reject_microversion_skew is not None:
            self.reject_microversion_skew = reject_microversion_skew
        if update_suppression_attributes is not None:
            self.update_suppression_attributes = update_suppression_attributes
        if features is not None:
            self.features = features
        if source_microversion is not None:
            self.source_microversion = source_microversion

    @property
    def serialization_version(self):
        """Gets the serialization_version of this PartStudiosUpdateFeaturesBody.  # noqa: E501

        The version of the serialization protocol for features  # noqa: E501

        :return: The serialization_version of this PartStudiosUpdateFeaturesBody.  # noqa: E501
        :rtype: str
        """
        return self._serialization_version

    @serialization_version.setter
    def serialization_version(self, serialization_version):
        """Sets the serialization_version of this PartStudiosUpdateFeaturesBody.

        The version of the serialization protocol for features  # noqa: E501

        :param serialization_version: The serialization_version of this PartStudiosUpdateFeaturesBody.  # noqa: E501
        :type: str
        """

        self._serialization_version = serialization_version

    @property
    def reject_microversion_skew(self):
        """Gets the reject_microversion_skew of this PartStudiosUpdateFeaturesBody.  # noqa: E501

        If set to true and the element has changed since     sourceMicroversion, return an HTTP Conflict status.  # noqa: E501

        :return: The reject_microversion_skew of this PartStudiosUpdateFeaturesBody.  # noqa: E501
        :rtype: bool
        """
        return self._reject_microversion_skew

    @reject_microversion_skew.setter
    def reject_microversion_skew(self, reject_microversion_skew):
        """Sets the reject_microversion_skew of this PartStudiosUpdateFeaturesBody.

        If set to true and the element has changed since     sourceMicroversion, return an HTTP Conflict status.  # noqa: E501

        :param reject_microversion_skew: The reject_microversion_skew of this PartStudiosUpdateFeaturesBody.  # noqa: E501
        :type: bool
        """

        self._reject_microversion_skew = reject_microversion_skew

    @property
    def update_suppression_attributes(self):
        """Gets the update_suppression_attributes of this PartStudiosUpdateFeaturesBody.  # noqa: E501

        If true, suppression attributes of the feature         (suppress, suppressionState) will be updated  # noqa: E501

        :return: The update_suppression_attributes of this PartStudiosUpdateFeaturesBody.  # noqa: E501
        :rtype: bool
        """
        return self._update_suppression_attributes

    @update_suppression_attributes.setter
    def update_suppression_attributes(self, update_suppression_attributes):
        """Sets the update_suppression_attributes of this PartStudiosUpdateFeaturesBody.

        If true, suppression attributes of the feature         (suppress, suppressionState) will be updated  # noqa: E501

        :param update_suppression_attributes: The update_suppression_attributes of this PartStudiosUpdateFeaturesBody.  # noqa: E501
        :type: bool
        """

        self._update_suppression_attributes = update_suppression_attributes

    @property
    def features(self):
        """Gets the features of this PartStudiosUpdateFeaturesBody.  # noqa: E501

        A list of features containing updates to apply  # noqa: E501

        :return: The features of this PartStudiosUpdateFeaturesBody.  # noqa: E501
        :rtype: list[object]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this PartStudiosUpdateFeaturesBody.

        A list of features containing updates to apply  # noqa: E501

        :param features: The features of this PartStudiosUpdateFeaturesBody.  # noqa: E501
        :type: list[object]
        """

        self._features = features

    @property
    def source_microversion(self):
        """Gets the source_microversion of this PartStudiosUpdateFeaturesBody.  # noqa: E501

        The document microversion from which the features were extracted  # noqa: E501

        :return: The source_microversion of this PartStudiosUpdateFeaturesBody.  # noqa: E501
        :rtype: str
        """
        return self._source_microversion

    @source_microversion.setter
    def source_microversion(self, source_microversion):
        """Sets the source_microversion of this PartStudiosUpdateFeaturesBody.

        The document microversion from which the features were extracted  # noqa: E501

        :param source_microversion: The source_microversion of this PartStudiosUpdateFeaturesBody.  # noqa: E501
        :type: str
        """

        self._source_microversion = source_microversion

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
        if not isinstance(other, PartStudiosUpdateFeaturesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
