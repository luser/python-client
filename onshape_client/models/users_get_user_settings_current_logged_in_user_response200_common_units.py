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

from onshape_client.models.users_get_user_settings_current_logged_in_user_response200_common_units_units import UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits  # noqa: F401,E501


class UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnits(object):
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
        'units': 'list[UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits]'
    }

    attribute_map = {
        'units': 'units'
    }

    def __init__(self, units=None):  # noqa: E501
        """UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnits - a model defined in Swagger"""  # noqa: E501

        self._units = None
        self.discriminator = None

        if units is not None:
            self.units = units

    @property
    def units(self):
        """Gets the units of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnits.  # noqa: E501

        List of recognized units  # noqa: E501

        :return: The units of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnits.  # noqa: E501
        :rtype: list[UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits]
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnits.

        List of recognized units  # noqa: E501

        :param units: The units of this UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnits.  # noqa: E501
        :type: list[UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnitsUnits]
        """

        self._units = units

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
        if not isinstance(other, UsersGetUserSettingsCurrentLoggedInUserResponse200CommonUnits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
