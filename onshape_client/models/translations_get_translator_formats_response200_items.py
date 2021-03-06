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


class TranslationsGetTranslatorFormatsResponse200Items(object):
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
        'translator_name': 'str',
        'valid_destination_format': 'bool',
        'could_be_assembly': 'bool',
        'name': 'str',
        'valid_source_format': 'bool'
    }

    attribute_map = {
        'translator_name': 'translatorName',
        'valid_destination_format': 'validDestinationFormat',
        'could_be_assembly': 'couldBeAssembly',
        'name': 'name',
        'valid_source_format': 'validSourceFormat'
    }

    def __init__(self, translator_name=None, valid_destination_format=None, could_be_assembly=None, name=None, valid_source_format=None):  # noqa: E501
        """TranslationsGetTranslatorFormatsResponse200Items - a model defined in Swagger"""  # noqa: E501

        self._translator_name = None
        self._valid_destination_format = None
        self._could_be_assembly = None
        self._name = None
        self._valid_source_format = None
        self.discriminator = None

        if translator_name is not None:
            self.translator_name = translator_name
        if valid_destination_format is not None:
            self.valid_destination_format = valid_destination_format
        if could_be_assembly is not None:
            self.could_be_assembly = could_be_assembly
        if name is not None:
            self.name = name
        if valid_source_format is not None:
            self.valid_source_format = valid_source_format

    @property
    def translator_name(self):
        """Gets the translator_name of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501

        For internal use  # noqa: E501

        :return: The translator_name of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._translator_name

    @translator_name.setter
    def translator_name(self, translator_name):
        """Sets the translator_name of this TranslationsGetTranslatorFormatsResponse200Items.

        For internal use  # noqa: E501

        :param translator_name: The translator_name of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501
        :type: str
        """

        self._translator_name = translator_name

    @property
    def valid_destination_format(self):
        """Gets the valid_destination_format of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501

        True if the format is valid as a destination format        for translation. Note that ONSHAPE is a valid destination format, but represents translation to Part Studio        and Assembly elements, which cannot be directly downloaded.  # noqa: E501

        :return: The valid_destination_format of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501
        :rtype: bool
        """
        return self._valid_destination_format

    @valid_destination_format.setter
    def valid_destination_format(self, valid_destination_format):
        """Sets the valid_destination_format of this TranslationsGetTranslatorFormatsResponse200Items.

        True if the format is valid as a destination format        for translation. Note that ONSHAPE is a valid destination format, but represents translation to Part Studio        and Assembly elements, which cannot be directly downloaded.  # noqa: E501

        :param valid_destination_format: The valid_destination_format of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501
        :type: bool
        """

        self._valid_destination_format = valid_destination_format

    @property
    def could_be_assembly(self):
        """Gets the could_be_assembly of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501

        True if the format can contain an assembly  # noqa: E501

        :return: The could_be_assembly of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501
        :rtype: bool
        """
        return self._could_be_assembly

    @could_be_assembly.setter
    def could_be_assembly(self, could_be_assembly):
        """Sets the could_be_assembly of this TranslationsGetTranslatorFormatsResponse200Items.

        True if the format can contain an assembly  # noqa: E501

        :param could_be_assembly: The could_be_assembly of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501
        :type: bool
        """

        self._could_be_assembly = could_be_assembly

    @property
    def name(self):
        """Gets the name of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501

        Name of translation format  # noqa: E501

        :return: The name of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TranslationsGetTranslatorFormatsResponse200Items.

        Name of translation format  # noqa: E501

        :param name: The name of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def valid_source_format(self):
        """Gets the valid_source_format of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501

        True if the format is valid as an input to translation  # noqa: E501

        :return: The valid_source_format of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501
        :rtype: bool
        """
        return self._valid_source_format

    @valid_source_format.setter
    def valid_source_format(self, valid_source_format):
        """Sets the valid_source_format of this TranslationsGetTranslatorFormatsResponse200Items.

        True if the format is valid as an input to translation  # noqa: E501

        :param valid_source_format: The valid_source_format of this TranslationsGetTranslatorFormatsResponse200Items.  # noqa: E501
        :type: bool
        """

        self._valid_source_format = valid_source_format

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
        if not isinstance(other, TranslationsGetTranslatorFormatsResponse200Items):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
