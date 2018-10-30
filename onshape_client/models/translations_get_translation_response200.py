# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TranslationsGetTranslationResponse200(object):
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
        'href': 'str',
        'request_element_id': 'str',
        'request_state': 'str',
        'version_id': 'str',
        'workspace_id': 'str',
        'id': 'str',
        'document_id': 'str'
    }

    attribute_map = {
        'href': 'href',
        'request_element_id': 'requestElementId',
        'request_state': 'requestState',
        'version_id': 'versionId',
        'workspace_id': 'workspaceId',
        'id': 'id',
        'document_id': 'documentId'
    }

    def __init__(self, href=None, request_element_id=None, request_state=None, version_id=None, workspace_id=None, id=None, document_id=None):  # noqa: E501
        """TranslationsGetTranslationResponse200 - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._request_element_id = None
        self._request_state = None
        self._version_id = None
        self._workspace_id = None
        self._id = None
        self._document_id = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if request_element_id is not None:
            self.request_element_id = request_element_id
        if request_state is not None:
            self.request_state = request_state
        if version_id is not None:
            self.version_id = version_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if id is not None:
            self.id = id
        if document_id is not None:
            self.document_id = document_id

    @property
    def href(self):
        """Gets the href of this TranslationsGetTranslationResponse200.  # noqa: E501

        The URI for accessing this translation  # noqa: E501

        :return: The href of this TranslationsGetTranslationResponse200.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TranslationsGetTranslationResponse200.

        The URI for accessing this translation  # noqa: E501

        :param href: The href of this TranslationsGetTranslationResponse200.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def request_element_id(self):
        """Gets the request_element_id of this TranslationsGetTranslationResponse200.  # noqa: E501

        The id of the element being translated  # noqa: E501

        :return: The request_element_id of this TranslationsGetTranslationResponse200.  # noqa: E501
        :rtype: str
        """
        return self._request_element_id

    @request_element_id.setter
    def request_element_id(self, request_element_id):
        """Sets the request_element_id of this TranslationsGetTranslationResponse200.

        The id of the element being translated  # noqa: E501

        :param request_element_id: The request_element_id of this TranslationsGetTranslationResponse200.  # noqa: E501
        :type: str
        """

        self._request_element_id = request_element_id

    @property
    def request_state(self):
        """Gets the request_state of this TranslationsGetTranslationResponse200.  # noqa: E501

        The state of this translation request. (ACTIVE|DONE|FAILED)  # noqa: E501

        :return: The request_state of this TranslationsGetTranslationResponse200.  # noqa: E501
        :rtype: str
        """
        return self._request_state

    @request_state.setter
    def request_state(self, request_state):
        """Sets the request_state of this TranslationsGetTranslationResponse200.

        The state of this translation request. (ACTIVE|DONE|FAILED)  # noqa: E501

        :param request_state: The request_state of this TranslationsGetTranslationResponse200.  # noqa: E501
        :type: str
        """

        self._request_state = request_state

    @property
    def version_id(self):
        """Gets the version_id of this TranslationsGetTranslationResponse200.  # noqa: E501

        The id of the document version that contains the translation source  # noqa: E501

        :return: The version_id of this TranslationsGetTranslationResponse200.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this TranslationsGetTranslationResponse200.

        The id of the document version that contains the translation source  # noqa: E501

        :param version_id: The version_id of this TranslationsGetTranslationResponse200.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this TranslationsGetTranslationResponse200.  # noqa: E501

        The id of the document workspace that contains the translation source  # noqa: E501

        :return: The workspace_id of this TranslationsGetTranslationResponse200.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this TranslationsGetTranslationResponse200.

        The id of the document workspace that contains the translation source  # noqa: E501

        :param workspace_id: The workspace_id of this TranslationsGetTranslationResponse200.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def id(self):
        """Gets the id of this TranslationsGetTranslationResponse200.  # noqa: E501

        The id of this translation  # noqa: E501

        :return: The id of this TranslationsGetTranslationResponse200.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TranslationsGetTranslationResponse200.

        The id of this translation  # noqa: E501

        :param id: The id of this TranslationsGetTranslationResponse200.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def document_id(self):
        """Gets the document_id of this TranslationsGetTranslationResponse200.  # noqa: E501

        The id of the document that contains the translation source  # noqa: E501

        :return: The document_id of this TranslationsGetTranslationResponse200.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this TranslationsGetTranslationResponse200.

        The id of the document that contains the translation source  # noqa: E501

        :param document_id: The document_id of this TranslationsGetTranslationResponse200.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

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
        if not isinstance(other, TranslationsGetTranslationResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other