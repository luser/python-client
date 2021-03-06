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

from onshape_client.models.body import Body  # noqa: F401,E501


class PartsGetMassPropertiesResponse200(object):
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
        'microversion_id': 'str',
        'bodies': 'dict(str, Body)'
    }

    attribute_map = {
        'microversion_id': 'microversionId',
        'bodies': 'bodies'
    }

    def __init__(self, microversion_id=None, bodies=None):  # noqa: E501
        """PartsGetMassPropertiesResponse200 - a model defined in Swagger"""  # noqa: E501

        self._microversion_id = None
        self._bodies = None
        self.discriminator = None

        if microversion_id is not None:
            self.microversion_id = microversion_id
        if bodies is not None:
            self.bodies = bodies

    @property
    def microversion_id(self):
        """Gets the microversion_id of this PartsGetMassPropertiesResponse200.  # noqa: E501

        Current microversion  # noqa: E501

        :return: The microversion_id of this PartsGetMassPropertiesResponse200.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this PartsGetMassPropertiesResponse200.

        Current microversion  # noqa: E501

        :param microversion_id: The microversion_id of this PartsGetMassPropertiesResponse200.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def bodies(self):
        """Gets the bodies of this PartsGetMassPropertiesResponse200.  # noqa: E501

        Object containing parts with mass properties, with the keys being the part             ID or \"-all-\" for a set of parts considered together  # noqa: E501

        :return: The bodies of this PartsGetMassPropertiesResponse200.  # noqa: E501
        :rtype: dict(str, Body)
        """
        return self._bodies

    @bodies.setter
    def bodies(self, bodies):
        """Sets the bodies of this PartsGetMassPropertiesResponse200.

        Object containing parts with mass properties, with the keys being the part             ID or \"-all-\" for a set of parts considered together  # noqa: E501

        :param bodies: The bodies of this PartsGetMassPropertiesResponse200.  # noqa: E501
        :type: dict(str, Body)
        """

        self._bodies = bodies

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
        if not isinstance(other, PartsGetMassPropertiesResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
