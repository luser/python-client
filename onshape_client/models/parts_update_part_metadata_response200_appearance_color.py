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


class PartsUpdatePartMetadataResponse200AppearanceColor(object):
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
        'blue': 'object',
        'green': 'object',
        'red': 'object'
    }

    attribute_map = {
        'blue': 'blue',
        'green': 'green',
        'red': 'red'
    }

    def __init__(self, blue=None, green=None, red=None):  # noqa: E501
        """PartsUpdatePartMetadataResponse200AppearanceColor - a model defined in Swagger"""  # noqa: E501

        self._blue = None
        self._green = None
        self._red = None
        self.discriminator = None

        if blue is not None:
            self.blue = blue
        if green is not None:
            self.green = green
        if red is not None:
            self.red = red

    @property
    def blue(self):
        """Gets the blue of this PartsUpdatePartMetadataResponse200AppearanceColor.  # noqa: E501

        Blue RGB value  # noqa: E501

        :return: The blue of this PartsUpdatePartMetadataResponse200AppearanceColor.  # noqa: E501
        :rtype: object
        """
        return self._blue

    @blue.setter
    def blue(self, blue):
        """Sets the blue of this PartsUpdatePartMetadataResponse200AppearanceColor.

        Blue RGB value  # noqa: E501

        :param blue: The blue of this PartsUpdatePartMetadataResponse200AppearanceColor.  # noqa: E501
        :type: object
        """

        self._blue = blue

    @property
    def green(self):
        """Gets the green of this PartsUpdatePartMetadataResponse200AppearanceColor.  # noqa: E501

        Green RGB value  # noqa: E501

        :return: The green of this PartsUpdatePartMetadataResponse200AppearanceColor.  # noqa: E501
        :rtype: object
        """
        return self._green

    @green.setter
    def green(self, green):
        """Sets the green of this PartsUpdatePartMetadataResponse200AppearanceColor.

        Green RGB value  # noqa: E501

        :param green: The green of this PartsUpdatePartMetadataResponse200AppearanceColor.  # noqa: E501
        :type: object
        """

        self._green = green

    @property
    def red(self):
        """Gets the red of this PartsUpdatePartMetadataResponse200AppearanceColor.  # noqa: E501

        Red RGB value  # noqa: E501

        :return: The red of this PartsUpdatePartMetadataResponse200AppearanceColor.  # noqa: E501
        :rtype: object
        """
        return self._red

    @red.setter
    def red(self, red):
        """Sets the red of this PartsUpdatePartMetadataResponse200AppearanceColor.

        Red RGB value  # noqa: E501

        :param red: The red of this PartsUpdatePartMetadataResponse200AppearanceColor.  # noqa: E501
        :type: object
        """

        self._red = red

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
        if not isinstance(other, PartsUpdatePartMetadataResponse200AppearanceColor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
