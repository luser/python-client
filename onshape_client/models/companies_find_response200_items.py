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

from onshape_client.models.companies_get_response200_address import CompaniesGetResponse200Address  # noqa: F401,E501


class CompaniesFindResponse200Items(object):
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
        'description': 'str',
        'admin': 'bool',
        'image': 'str',
        'href': 'str',
        'address': 'CompaniesGetResponse200Address',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'admin': 'admin',
        'image': 'image',
        'href': 'href',
        'address': 'address',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, description=None, admin=None, image=None, href=None, address=None, id=None, name=None):  # noqa: E501
        """CompaniesFindResponse200Items - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._admin = None
        self._image = None
        self._href = None
        self._address = None
        self._id = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if admin is not None:
            self.admin = admin
        if image is not None:
            self.image = image
        if href is not None:
            self.href = href
        if address is not None:
            self.address = address
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this CompaniesFindResponse200Items.  # noqa: E501

        Company description  # noqa: E501

        :return: The description of this CompaniesFindResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CompaniesFindResponse200Items.

        Company description  # noqa: E501

        :param description: The description of this CompaniesFindResponse200Items.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def admin(self):
        """Gets the admin of this CompaniesFindResponse200Items.  # noqa: E501

        Whether current user is administrator of company  # noqa: E501

        :return: The admin of this CompaniesFindResponse200Items.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this CompaniesFindResponse200Items.

        Whether current user is administrator of company  # noqa: E501

        :param admin: The admin of this CompaniesFindResponse200Items.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def image(self):
        """Gets the image of this CompaniesFindResponse200Items.  # noqa: E501

        URL for company image  # noqa: E501

        :return: The image of this CompaniesFindResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CompaniesFindResponse200Items.

        URL for company image  # noqa: E501

        :param image: The image of this CompaniesFindResponse200Items.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def href(self):
        """Gets the href of this CompaniesFindResponse200Items.  # noqa: E501

        URL of this company information  # noqa: E501

        :return: The href of this CompaniesFindResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CompaniesFindResponse200Items.

        URL of this company information  # noqa: E501

        :param href: The href of this CompaniesFindResponse200Items.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def address(self):
        """Gets the address of this CompaniesFindResponse200Items.  # noqa: E501


        :return: The address of this CompaniesFindResponse200Items.  # noqa: E501
        :rtype: CompaniesGetResponse200Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CompaniesFindResponse200Items.


        :param address: The address of this CompaniesFindResponse200Items.  # noqa: E501
        :type: CompaniesGetResponse200Address
        """

        self._address = address

    @property
    def id(self):
        """Gets the id of this CompaniesFindResponse200Items.  # noqa: E501

        Company ID  # noqa: E501

        :return: The id of this CompaniesFindResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompaniesFindResponse200Items.

        Company ID  # noqa: E501

        :param id: The id of this CompaniesFindResponse200Items.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CompaniesFindResponse200Items.  # noqa: E501

        Company name  # noqa: E501

        :return: The name of this CompaniesFindResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompaniesFindResponse200Items.

        Company name  # noqa: E501

        :param name: The name of this CompaniesFindResponse200Items.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, CompaniesFindResponse200Items):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
