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

from onshape_client.models.translations_get_translations_response200_items import TranslationsGetTranslationsResponse200Items  # noqa: F401,E501


class TranslationsGetTranslationsResponse200(object):
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
        'items': 'list[TranslationsGetTranslationsResponse200Items]',
        'previous': 'str',
        'has_next': 'bool',
        'next': 'str'
    }

    attribute_map = {
        'items': 'items',
        'previous': 'previous',
        'has_next': 'hasNext',
        'next': 'next'
    }

    def __init__(self, items=None, previous=None, has_next=None, next=None):  # noqa: E501
        """TranslationsGetTranslationsResponse200 - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._previous = None
        self._has_next = None
        self._next = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if previous is not None:
            self.previous = previous
        if has_next is not None:
            self.has_next = has_next
        if next is not None:
            self.next = next

    @property
    def items(self):
        """Gets the items of this TranslationsGetTranslationsResponse200.  # noqa: E501

        List of items  # noqa: E501

        :return: The items of this TranslationsGetTranslationsResponse200.  # noqa: E501
        :rtype: list[TranslationsGetTranslationsResponse200Items]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this TranslationsGetTranslationsResponse200.

        List of items  # noqa: E501

        :param items: The items of this TranslationsGetTranslationsResponse200.  # noqa: E501
        :type: list[TranslationsGetTranslationsResponse200Items]
        """

        self._items = items

    @property
    def previous(self):
        """Gets the previous of this TranslationsGetTranslationsResponse200.  # noqa: E501

        URI to retrieve previous batch  # noqa: E501

        :return: The previous of this TranslationsGetTranslationsResponse200.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this TranslationsGetTranslationsResponse200.

        URI to retrieve previous batch  # noqa: E501

        :param previous: The previous of this TranslationsGetTranslationsResponse200.  # noqa: E501
        :type: str
        """

        self._previous = previous

    @property
    def has_next(self):
        """Gets the has_next of this TranslationsGetTranslationsResponse200.  # noqa: E501

        Whether there are more entries to retrieve  # noqa: E501

        :return: The has_next of this TranslationsGetTranslationsResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this TranslationsGetTranslationsResponse200.

        Whether there are more entries to retrieve  # noqa: E501

        :param has_next: The has_next of this TranslationsGetTranslationsResponse200.  # noqa: E501
        :type: bool
        """

        self._has_next = has_next

    @property
    def next(self):
        """Gets the next of this TranslationsGetTranslationsResponse200.  # noqa: E501

        URI to retrieve next batch  # noqa: E501

        :return: The next of this TranslationsGetTranslationsResponse200.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this TranslationsGetTranslationsResponse200.

        URI to retrieve next batch  # noqa: E501

        :param next: The next of this TranslationsGetTranslationsResponse200.  # noqa: E501
        :type: str
        """

        self._next = next

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
        if not isinstance(other, TranslationsGetTranslationsResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
