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

from onshape_client.models.part_studios_compare_part_studio_response200_changes_parts_changes import PartStudiosComparePartStudioResponse200ChangesPartsChanges  # noqa: F401,E501


class PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges(object):
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
        'source_id': 'str',
        'type': 'str',
        'target_id': 'str',
        'changes': 'PartStudiosComparePartStudioResponse200ChangesPartsChanges'
    }

    attribute_map = {
        'source_id': 'sourceId',
        'type': 'type',
        'target_id': 'targetId',
        'changes': 'changes'
    }

    def __init__(self, source_id=None, type=None, target_id=None, changes=None):  # noqa: E501
        """PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges - a model defined in Swagger"""  # noqa: E501

        self._source_id = None
        self._type = None
        self._target_id = None
        self._changes = None
        self.discriminator = None

        if source_id is not None:
            self.source_id = source_id
        if type is not None:
            self.type = type
        if target_id is not None:
            self.target_id = target_id
        if changes is not None:
            self.changes = changes

    @property
    def source_id(self):
        """Gets the source_id of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501

        Part Id of the Part in the source             microversion, can be null for new Parts  # noqa: E501

        :return: The source_id of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.

        Part Id of the Part in the source             microversion, can be null for new Parts  # noqa: E501

        :param source_id: The source_id of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def type(self):
        """Gets the type of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501

        Type of the change (see API description             for values)  # noqa: E501

        :return: The type of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.

        Type of the change (see API description             for values)  # noqa: E501

        :param type: The type of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def target_id(self):
        """Gets the target_id of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501

        Part Id of the Part in the target             microversion, can be null for deleted Parts  # noqa: E501

        :return: The target_id of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.

        Part Id of the Part in the target             microversion, can be null for deleted Parts  # noqa: E501

        :param target_id: The target_id of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501
        :type: str
        """

        self._target_id = target_id

    @property
    def changes(self):
        """Gets the changes of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501


        :return: The changes of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501
        :rtype: PartStudiosComparePartStudioResponse200ChangesPartsChanges
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.


        :param changes: The changes of this PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges.  # noqa: E501
        :type: PartStudiosComparePartStudioResponse200ChangesPartsChanges
        """

        self._changes = changes

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
        if not isinstance(other, PartStudiosComparePartStudioResponse200ChangesPartsCollectionChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
