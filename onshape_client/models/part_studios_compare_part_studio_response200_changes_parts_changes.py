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

from onshape_client.models.part_studios_compare_part_studio_response200_changes_parts_changes_appearance import PartStudiosComparePartStudioResponse200ChangesPartsChangesAppearance  # noqa: F401,E501
from onshape_client.models.part_studios_compare_part_studio_response200_changes_parts_changes_geometry import PartStudiosComparePartStudioResponse200ChangesPartsChangesGeometry  # noqa: F401,E501
from onshape_client.models.part_studios_compare_part_studio_response200_changes_parts_changes_material import PartStudiosComparePartStudioResponse200ChangesPartsChangesMaterial  # noqa: F401,E501
from onshape_client.models.part_studios_compare_part_studio_response200_changes_parts_changes_metadata import PartStudiosComparePartStudioResponse200ChangesPartsChangesMetadata  # noqa: F401,E501
from onshape_client.models.part_studios_compare_part_studio_response200_changes_parts_changes_name import PartStudiosComparePartStudioResponse200ChangesPartsChangesName  # noqa: F401,E501
from onshape_client.models.part_studios_compare_part_studio_response200_changes_parts_changes_other import PartStudiosComparePartStudioResponse200ChangesPartsChangesOther  # noqa: F401,E501
from onshape_client.models.part_studios_compare_part_studio_response200_changes_parts_changes_visibility import PartStudiosComparePartStudioResponse200ChangesPartsChangesVisibility  # noqa: F401,E501


class PartStudiosComparePartStudioResponse200ChangesPartsChanges(object):
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
        'name': 'PartStudiosComparePartStudioResponse200ChangesPartsChangesName',
        'geometry': 'PartStudiosComparePartStudioResponse200ChangesPartsChangesGeometry',
        'material': 'PartStudiosComparePartStudioResponse200ChangesPartsChangesMaterial',
        'appearance': 'PartStudiosComparePartStudioResponse200ChangesPartsChangesAppearance',
        'visibility': 'PartStudiosComparePartStudioResponse200ChangesPartsChangesVisibility',
        'other': 'PartStudiosComparePartStudioResponse200ChangesPartsChangesOther',
        'metadata': 'PartStudiosComparePartStudioResponse200ChangesPartsChangesMetadata'
    }

    attribute_map = {
        'name': 'name',
        'geometry': 'geometry',
        'material': 'material',
        'appearance': 'appearance',
        'visibility': 'visibility',
        'other': 'other',
        'metadata': 'metadata'
    }

    def __init__(self, name=None, geometry=None, material=None, appearance=None, visibility=None, other=None, metadata=None):  # noqa: E501
        """PartStudiosComparePartStudioResponse200ChangesPartsChanges - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._geometry = None
        self._material = None
        self._appearance = None
        self._visibility = None
        self._other = None
        self._metadata = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if geometry is not None:
            self.geometry = geometry
        if material is not None:
            self.material = material
        if appearance is not None:
            self.appearance = appearance
        if visibility is not None:
            self.visibility = visibility
        if other is not None:
            self.other = other
        if metadata is not None:
            self.metadata = metadata

    @property
    def name(self):
        """Gets the name of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501


        :return: The name of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :rtype: PartStudiosComparePartStudioResponse200ChangesPartsChangesName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.


        :param name: The name of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :type: PartStudiosComparePartStudioResponse200ChangesPartsChangesName
        """

        self._name = name

    @property
    def geometry(self):
        """Gets the geometry of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501


        :return: The geometry of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :rtype: PartStudiosComparePartStudioResponse200ChangesPartsChangesGeometry
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.


        :param geometry: The geometry of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :type: PartStudiosComparePartStudioResponse200ChangesPartsChangesGeometry
        """

        self._geometry = geometry

    @property
    def material(self):
        """Gets the material of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501


        :return: The material of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :rtype: PartStudiosComparePartStudioResponse200ChangesPartsChangesMaterial
        """
        return self._material

    @material.setter
    def material(self, material):
        """Sets the material of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.


        :param material: The material of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :type: PartStudiosComparePartStudioResponse200ChangesPartsChangesMaterial
        """

        self._material = material

    @property
    def appearance(self):
        """Gets the appearance of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501


        :return: The appearance of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :rtype: PartStudiosComparePartStudioResponse200ChangesPartsChangesAppearance
        """
        return self._appearance

    @appearance.setter
    def appearance(self, appearance):
        """Sets the appearance of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.


        :param appearance: The appearance of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :type: PartStudiosComparePartStudioResponse200ChangesPartsChangesAppearance
        """

        self._appearance = appearance

    @property
    def visibility(self):
        """Gets the visibility of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501


        :return: The visibility of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :rtype: PartStudiosComparePartStudioResponse200ChangesPartsChangesVisibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.


        :param visibility: The visibility of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :type: PartStudiosComparePartStudioResponse200ChangesPartsChangesVisibility
        """

        self._visibility = visibility

    @property
    def other(self):
        """Gets the other of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501


        :return: The other of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :rtype: PartStudiosComparePartStudioResponse200ChangesPartsChangesOther
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.


        :param other: The other of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :type: PartStudiosComparePartStudioResponse200ChangesPartsChangesOther
        """

        self._other = other

    @property
    def metadata(self):
        """Gets the metadata of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501


        :return: The metadata of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :rtype: PartStudiosComparePartStudioResponse200ChangesPartsChangesMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.


        :param metadata: The metadata of this PartStudiosComparePartStudioResponse200ChangesPartsChanges.  # noqa: E501
        :type: PartStudiosComparePartStudioResponse200ChangesPartsChangesMetadata
        """

        self._metadata = metadata

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
        if not isinstance(other, PartStudiosComparePartStudioResponse200ChangesPartsChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
