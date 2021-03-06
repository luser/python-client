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

from onshape_client.models.part_material_properties import PartMaterialProperties  # noqa: F401,E501


class PartMaterial(object):
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
        'library_name': 'str',
        'id': 'str',
        'properties': 'list[PartMaterialProperties]'
    }

    attribute_map = {
        'library_name': 'libraryName',
        'id': 'id',
        'properties': 'properties'
    }

    def __init__(self, library_name=None, id=None, properties=None):  # noqa: E501
        """PartMaterial - a model defined in Swagger"""  # noqa: E501

        self._library_name = None
        self._id = None
        self._properties = None
        self.discriminator = None

        if library_name is not None:
            self.library_name = library_name
        if id is not None:
            self.id = id
        if properties is not None:
            self.properties = properties

    @property
    def library_name(self):
        """Gets the library_name of this PartMaterial.  # noqa: E501

        Name of the material library  # noqa: E501

        :return: The library_name of this PartMaterial.  # noqa: E501
        :rtype: str
        """
        return self._library_name

    @library_name.setter
    def library_name(self, library_name):
        """Sets the library_name of this PartMaterial.

        Name of the material library  # noqa: E501

        :param library_name: The library_name of this PartMaterial.  # noqa: E501
        :type: str
        """

        self._library_name = library_name

    @property
    def id(self):
        """Gets the id of this PartMaterial.  # noqa: E501

        Id of the material  # noqa: E501

        :return: The id of this PartMaterial.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartMaterial.

        Id of the material  # noqa: E501

        :param id: The id of this PartMaterial.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def properties(self):
        """Gets the properties of this PartMaterial.  # noqa: E501

        Properties of the material  # noqa: E501

        :return: The properties of this PartMaterial.  # noqa: E501
        :rtype: list[PartMaterialProperties]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PartMaterial.

        Properties of the material  # noqa: E501

        :param properties: The properties of this PartMaterial.  # noqa: E501
        :type: list[PartMaterialProperties]
        """

        self._properties = properties

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
        if not isinstance(other, PartMaterial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
