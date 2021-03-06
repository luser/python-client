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

from onshape_client.models.metadata_get_metadata_response200_elements_parts import MetadataGetMetadataResponse200ElementsParts  # noqa: F401,E501


class MetadataGetMetadataResponse200ElementsItems(object):
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
        'mime_type': 'str',
        'parts': 'list[MetadataGetMetadataResponse200ElementsParts]',
        'thumbnail': 'object',
        'href': 'str',
        'element_type': 'float',
        'properties': 'list[object]',
        'element_id': 'str'
    }

    attribute_map = {
        'mime_type': 'mimeType',
        'parts': 'parts',
        'thumbnail': 'thumbnail',
        'href': 'href',
        'element_type': 'elementType',
        'properties': 'properties',
        'element_id': 'elementId'
    }

    def __init__(self, mime_type=None, parts=None, thumbnail=None, href=None, element_type=None, properties=None, element_id=None):  # noqa: E501
        """MetadataGetMetadataResponse200ElementsItems - a model defined in Swagger"""  # noqa: E501

        self._mime_type = None
        self._parts = None
        self._thumbnail = None
        self._href = None
        self._element_type = None
        self._properties = None
        self._element_id = None
        self.discriminator = None

        if mime_type is not None:
            self.mime_type = mime_type
        if parts is not None:
            self.parts = parts
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if href is not None:
            self.href = href
        if element_type is not None:
            self.element_type = element_type
        if properties is not None:
            self.properties = properties
        if element_id is not None:
            self.element_id = element_id

    @property
    def mime_type(self):
        """Gets the mime_type of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501

        Element mime type  # noqa: E501

        :return: The mime_type of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this MetadataGetMetadataResponse200ElementsItems.

        Element mime type  # noqa: E501

        :param mime_type: The mime_type of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def parts(self):
        """Gets the parts of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501

        Part list if element is a PartStudio  # noqa: E501

        :return: The parts of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :rtype: list[MetadataGetMetadataResponse200ElementsParts]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this MetadataGetMetadataResponse200ElementsItems.

        Part list if element is a PartStudio  # noqa: E501

        :param parts: The parts of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :type: list[MetadataGetMetadataResponse200ElementsParts]
        """

        self._parts = parts

    @property
    def thumbnail(self):
        """Gets the thumbnail of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501

        Element's thumbnail  # noqa: E501

        :return: The thumbnail of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :rtype: object
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this MetadataGetMetadataResponse200ElementsItems.

        Element's thumbnail  # noqa: E501

        :param thumbnail: The thumbnail of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :type: object
        """

        self._thumbnail = thumbnail

    @property
    def href(self):
        """Gets the href of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501

        URI of Element metadata  # noqa: E501

        :return: The href of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this MetadataGetMetadataResponse200ElementsItems.

        URI of Element metadata  # noqa: E501

        :param href: The href of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def element_type(self):
        """Gets the element_type of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501

        Element type  # noqa: E501

        :return: The element_type of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :rtype: float
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this MetadataGetMetadataResponse200ElementsItems.

        Element type  # noqa: E501

        :param element_type: The element_type of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :type: float
        """

        self._element_type = element_type

    @property
    def properties(self):
        """Gets the properties of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501

        Element properties  # noqa: E501

        :return: The properties of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :rtype: list[object]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this MetadataGetMetadataResponse200ElementsItems.

        Element properties  # noqa: E501

        :param properties: The properties of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :type: list[object]
        """

        self._properties = properties

    @property
    def element_id(self):
        """Gets the element_id of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501

        Element id  # noqa: E501

        :return: The element_id of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this MetadataGetMetadataResponse200ElementsItems.

        Element id  # noqa: E501

        :param element_id: The element_id of this MetadataGetMetadataResponse200ElementsItems.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

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
        if not isinstance(other, MetadataGetMetadataResponse200ElementsItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
