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


class ElementsDecodeConfigurationStringResponse200Parameters(object):
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
        'parameter_value': 'str',
        'parameter_id': 'str'
    }

    attribute_map = {
        'parameter_value': 'parameterValue',
        'parameter_id': 'parameterId'
    }

    def __init__(self, parameter_value=None, parameter_id=None):  # noqa: E501
        """ElementsDecodeConfigurationStringResponse200Parameters - a model defined in Swagger"""  # noqa: E501

        self._parameter_value = None
        self._parameter_id = None
        self.discriminator = None

        if parameter_value is not None:
            self.parameter_value = parameter_value
        if parameter_id is not None:
            self.parameter_id = parameter_id

    @property
    def parameter_value(self):
        """Gets the parameter_value of this ElementsDecodeConfigurationStringResponse200Parameters.  # noqa: E501

        The parameter value  # noqa: E501

        :return: The parameter_value of this ElementsDecodeConfigurationStringResponse200Parameters.  # noqa: E501
        :rtype: str
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value):
        """Sets the parameter_value of this ElementsDecodeConfigurationStringResponse200Parameters.

        The parameter value  # noqa: E501

        :param parameter_value: The parameter_value of this ElementsDecodeConfigurationStringResponse200Parameters.  # noqa: E501
        :type: str
        """

        self._parameter_value = parameter_value

    @property
    def parameter_id(self):
        """Gets the parameter_id of this ElementsDecodeConfigurationStringResponse200Parameters.  # noqa: E501

        The id of the parameter  # noqa: E501

        :return: The parameter_id of this ElementsDecodeConfigurationStringResponse200Parameters.  # noqa: E501
        :rtype: str
        """
        return self._parameter_id

    @parameter_id.setter
    def parameter_id(self, parameter_id):
        """Sets the parameter_id of this ElementsDecodeConfigurationStringResponse200Parameters.

        The id of the parameter  # noqa: E501

        :param parameter_id: The parameter_id of this ElementsDecodeConfigurationStringResponse200Parameters.  # noqa: E501
        :type: str
        """

        self._parameter_id = parameter_id

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
        if not isinstance(other, ElementsDecodeConfigurationStringResponse200Parameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
