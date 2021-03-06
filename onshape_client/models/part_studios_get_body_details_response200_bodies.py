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

from onshape_client.models.part_studios_get_body_details_response200_edges import PartStudiosGetBodyDetailsResponse200Edges  # noqa: F401,E501
from onshape_client.models.part_studios_get_body_details_response200_faces import PartStudiosGetBodyDetailsResponse200Faces  # noqa: F401,E501
from onshape_client.models.parts_get_body_details_response200_vertices import PartsGetBodyDetailsResponse200Vertices  # noqa: F401,E501


class PartStudiosGetBodyDetailsResponse200Bodies(object):
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
        'vertices': 'list[PartsGetBodyDetailsResponse200Vertices]',
        'edges': 'list[PartStudiosGetBodyDetailsResponse200Edges]',
        'type': 'str',
        'id': 'str',
        'faces': 'list[PartStudiosGetBodyDetailsResponse200Faces]'
    }

    attribute_map = {
        'vertices': 'vertices',
        'edges': 'edges',
        'type': 'type',
        'id': 'id',
        'faces': 'faces'
    }

    def __init__(self, vertices=None, edges=None, type=None, id=None, faces=None):  # noqa: E501
        """PartStudiosGetBodyDetailsResponse200Bodies - a model defined in Swagger"""  # noqa: E501

        self._vertices = None
        self._edges = None
        self._type = None
        self._id = None
        self._faces = None
        self.discriminator = None

        if vertices is not None:
            self.vertices = vertices
        if edges is not None:
            self.edges = edges
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if faces is not None:
            self.faces = faces

    @property
    def vertices(self):
        """Gets the vertices of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501

        Vertices of part  # noqa: E501

        :return: The vertices of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501
        :rtype: list[PartsGetBodyDetailsResponse200Vertices]
        """
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        """Sets the vertices of this PartStudiosGetBodyDetailsResponse200Bodies.

        Vertices of part  # noqa: E501

        :param vertices: The vertices of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501
        :type: list[PartsGetBodyDetailsResponse200Vertices]
        """

        self._vertices = vertices

    @property
    def edges(self):
        """Gets the edges of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501

        Edges of a part  # noqa: E501

        :return: The edges of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501
        :rtype: list[PartStudiosGetBodyDetailsResponse200Edges]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this PartStudiosGetBodyDetailsResponse200Bodies.

        Edges of a part  # noqa: E501

        :param edges: The edges of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501
        :type: list[PartStudiosGetBodyDetailsResponse200Edges]
        """

        self._edges = edges

    @property
    def type(self):
        """Gets the type of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501

        Type of a part  # noqa: E501

        :return: The type of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartStudiosGetBodyDetailsResponse200Bodies.

        Type of a part  # noqa: E501

        :param type: The type of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501

        ID of a part  # noqa: E501

        :return: The id of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartStudiosGetBodyDetailsResponse200Bodies.

        ID of a part  # noqa: E501

        :param id: The id of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def faces(self):
        """Gets the faces of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501

        Array of info for each face of a part  # noqa: E501

        :return: The faces of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501
        :rtype: list[PartStudiosGetBodyDetailsResponse200Faces]
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this PartStudiosGetBodyDetailsResponse200Bodies.

        Array of info for each face of a part  # noqa: E501

        :param faces: The faces of this PartStudiosGetBodyDetailsResponse200Bodies.  # noqa: E501
        :type: list[PartStudiosGetBodyDetailsResponse200Faces]
        """

        self._faces = faces

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
        if not isinstance(other, PartStudiosGetBodyDetailsResponse200Bodies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
