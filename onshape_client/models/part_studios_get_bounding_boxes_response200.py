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


class PartStudiosGetBoundingBoxesResponse200(object):
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
        'high_y': 'float',
        'high_x': 'float',
        'high_z': 'float',
        'low_z': 'float',
        'low_x': 'float',
        'low_y': 'float'
    }

    attribute_map = {
        'high_y': 'highY',
        'high_x': 'highX',
        'high_z': 'highZ',
        'low_z': 'lowZ',
        'low_x': 'lowX',
        'low_y': 'lowY'
    }

    def __init__(self, high_y=None, high_x=None, high_z=None, low_z=None, low_x=None, low_y=None):  # noqa: E501
        """PartStudiosGetBoundingBoxesResponse200 - a model defined in Swagger"""  # noqa: E501

        self._high_y = None
        self._high_x = None
        self._high_z = None
        self._low_z = None
        self._low_x = None
        self._low_y = None
        self.discriminator = None

        if high_y is not None:
            self.high_y = high_y
        if high_x is not None:
            self.high_x = high_x
        if high_z is not None:
            self.high_z = high_z
        if low_z is not None:
            self.low_z = low_z
        if low_x is not None:
            self.low_x = low_x
        if low_y is not None:
            self.low_y = low_y

    @property
    def high_y(self):
        """Gets the high_y of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501

        highest Y point  # noqa: E501

        :return: The high_y of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :rtype: float
        """
        return self._high_y

    @high_y.setter
    def high_y(self, high_y):
        """Sets the high_y of this PartStudiosGetBoundingBoxesResponse200.

        highest Y point  # noqa: E501

        :param high_y: The high_y of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :type: float
        """

        self._high_y = high_y

    @property
    def high_x(self):
        """Gets the high_x of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501

        highest X point  # noqa: E501

        :return: The high_x of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :rtype: float
        """
        return self._high_x

    @high_x.setter
    def high_x(self, high_x):
        """Sets the high_x of this PartStudiosGetBoundingBoxesResponse200.

        highest X point  # noqa: E501

        :param high_x: The high_x of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :type: float
        """

        self._high_x = high_x

    @property
    def high_z(self):
        """Gets the high_z of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501

        highest Z point  # noqa: E501

        :return: The high_z of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :rtype: float
        """
        return self._high_z

    @high_z.setter
    def high_z(self, high_z):
        """Sets the high_z of this PartStudiosGetBoundingBoxesResponse200.

        highest Z point  # noqa: E501

        :param high_z: The high_z of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :type: float
        """

        self._high_z = high_z

    @property
    def low_z(self):
        """Gets the low_z of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501

        lowest Z point  # noqa: E501

        :return: The low_z of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :rtype: float
        """
        return self._low_z

    @low_z.setter
    def low_z(self, low_z):
        """Sets the low_z of this PartStudiosGetBoundingBoxesResponse200.

        lowest Z point  # noqa: E501

        :param low_z: The low_z of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :type: float
        """

        self._low_z = low_z

    @property
    def low_x(self):
        """Gets the low_x of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501

        lowest X point  # noqa: E501

        :return: The low_x of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :rtype: float
        """
        return self._low_x

    @low_x.setter
    def low_x(self, low_x):
        """Sets the low_x of this PartStudiosGetBoundingBoxesResponse200.

        lowest X point  # noqa: E501

        :param low_x: The low_x of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :type: float
        """

        self._low_x = low_x

    @property
    def low_y(self):
        """Gets the low_y of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501

        lowest Y point  # noqa: E501

        :return: The low_y of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :rtype: float
        """
        return self._low_y

    @low_y.setter
    def low_y(self, low_y):
        """Sets the low_y of this PartStudiosGetBoundingBoxesResponse200.

        lowest Y point  # noqa: E501

        :param low_y: The low_y of this PartStudiosGetBoundingBoxesResponse200.  # noqa: E501
        :type: float
        """

        self._low_y = low_y

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
        if not isinstance(other, PartStudiosGetBoundingBoxesResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
