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


class TranslationsCreateTranslationBody(object):
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
        'import_in_background': 'bool',
        'version_string': 'str',
        'format_name': 'str',
        'flatten_assemblies': 'bool',
        'y_axis_is_up': 'bool',
        'notify_user': 'bool',
        'store_in_document': 'bool',
        'allow_faulty_parts': 'bool'
    }

    attribute_map = {
        'import_in_background': 'importInBackground',
        'version_string': 'versionString',
        'format_name': 'formatName',
        'flatten_assemblies': 'flattenAssemblies',
        'y_axis_is_up': 'yAxisIsUp',
        'notify_user': 'notifyUser',
        'store_in_document': 'storeInDocument',
        'allow_faulty_parts': 'allowFaultyParts'
    }

    def __init__(self, import_in_background=None, version_string=None, format_name=None, flatten_assemblies=None, y_axis_is_up=None, notify_user=None, store_in_document=None, allow_faulty_parts=None):  # noqa: E501
        """TranslationsCreateTranslationBody - a model defined in Swagger"""  # noqa: E501

        self._import_in_background = None
        self._version_string = None
        self._format_name = None
        self._flatten_assemblies = None
        self._y_axis_is_up = None
        self._notify_user = None
        self._store_in_document = None
        self._allow_faulty_parts = None
        self.discriminator = None

        if import_in_background is not None:
            self.import_in_background = import_in_background
        if version_string is not None:
            self.version_string = version_string
        if format_name is not None:
            self.format_name = format_name
        if flatten_assemblies is not None:
            self.flatten_assemblies = flatten_assemblies
        if y_axis_is_up is not None:
            self.y_axis_is_up = y_axis_is_up
        if notify_user is not None:
            self.notify_user = notify_user
        if store_in_document is not None:
            self.store_in_document = store_in_document
        if allow_faulty_parts is not None:
            self.allow_faulty_parts = allow_faulty_parts

    @property
    def import_in_background(self):
        """Gets the import_in_background of this TranslationsCreateTranslationBody.  # noqa: E501

        If storeInDocument is true and formatName is ONSHAPE and        the source is a Parasolid file, this specifies the preference as to whether the import should be completed        prior to the completion of the request (importInBackground=false) or whether it should be performed        asynchronously (importInBackground=true). Historically, this parameter was implicitly set to false, but large        imports can take long enough that the request could result in a timeout. Applications are encouraged to set        this parameter to true for reliable operation.  # noqa: E501

        :return: The import_in_background of this TranslationsCreateTranslationBody.  # noqa: E501
        :rtype: bool
        """
        return self._import_in_background

    @import_in_background.setter
    def import_in_background(self, import_in_background):
        """Sets the import_in_background of this TranslationsCreateTranslationBody.

        If storeInDocument is true and formatName is ONSHAPE and        the source is a Parasolid file, this specifies the preference as to whether the import should be completed        prior to the completion of the request (importInBackground=false) or whether it should be performed        asynchronously (importInBackground=true). Historically, this parameter was implicitly set to false, but large        imports can take long enough that the request could result in a timeout. Applications are encouraged to set        this parameter to true for reliable operation.  # noqa: E501

        :param import_in_background: The import_in_background of this TranslationsCreateTranslationBody.  # noqa: E501
        :type: bool
        """

        self._import_in_background = import_in_background

    @property
    def version_string(self):
        """Gets the version_string of this TranslationsCreateTranslationBody.  # noqa: E501

        Version of output format to use (format-dependent)  # noqa: E501

        :return: The version_string of this TranslationsCreateTranslationBody.  # noqa: E501
        :rtype: str
        """
        return self._version_string

    @version_string.setter
    def version_string(self, version_string):
        """Sets the version_string of this TranslationsCreateTranslationBody.

        Version of output format to use (format-dependent)  # noqa: E501

        :param version_string: The version_string of this TranslationsCreateTranslationBody.  # noqa: E501
        :type: str
        """

        self._version_string = version_string

    @property
    def format_name(self):
        """Gets the format_name of this TranslationsCreateTranslationBody.  # noqa: E501

        Name of format into which this element should be translated. ONSHAPE        indicates that the model file should be translated into a Part Studio or Assembly.  # noqa: E501

        :return: The format_name of this TranslationsCreateTranslationBody.  # noqa: E501
        :rtype: str
        """
        return self._format_name

    @format_name.setter
    def format_name(self, format_name):
        """Sets the format_name of this TranslationsCreateTranslationBody.

        Name of format into which this element should be translated. ONSHAPE        indicates that the model file should be translated into a Part Studio or Assembly.  # noqa: E501

        :param format_name: The format_name of this TranslationsCreateTranslationBody.  # noqa: E501
        :type: str
        """

        self._format_name = format_name

    @property
    def flatten_assemblies(self):
        """Gets the flatten_assemblies of this TranslationsCreateTranslationBody.  # noqa: E501

        If true, remove assembly structure and create only a        Part Studio  # noqa: E501

        :return: The flatten_assemblies of this TranslationsCreateTranslationBody.  # noqa: E501
        :rtype: bool
        """
        return self._flatten_assemblies

    @flatten_assemblies.setter
    def flatten_assemblies(self, flatten_assemblies):
        """Sets the flatten_assemblies of this TranslationsCreateTranslationBody.

        If true, remove assembly structure and create only a        Part Studio  # noqa: E501

        :param flatten_assemblies: The flatten_assemblies of this TranslationsCreateTranslationBody.  # noqa: E501
        :type: bool
        """

        self._flatten_assemblies = flatten_assemblies

    @property
    def y_axis_is_up(self):
        """Gets the y_axis_is_up of this TranslationsCreateTranslationBody.  # noqa: E501

        If true, treat the model's Y axis as the vertical axis.  Otherwise,        Z is treated as the vertical axis.  # noqa: E501

        :return: The y_axis_is_up of this TranslationsCreateTranslationBody.  # noqa: E501
        :rtype: bool
        """
        return self._y_axis_is_up

    @y_axis_is_up.setter
    def y_axis_is_up(self, y_axis_is_up):
        """Sets the y_axis_is_up of this TranslationsCreateTranslationBody.

        If true, treat the model's Y axis as the vertical axis.  Otherwise,        Z is treated as the vertical axis.  # noqa: E501

        :param y_axis_is_up: The y_axis_is_up of this TranslationsCreateTranslationBody.  # noqa: E501
        :type: bool
        """

        self._y_axis_is_up = y_axis_is_up

    @property
    def notify_user(self):
        """Gets the notify_user of this TranslationsCreateTranslationBody.  # noqa: E501

        Whether a user notification should be generated on completion  # noqa: E501

        :return: The notify_user of this TranslationsCreateTranslationBody.  # noqa: E501
        :rtype: bool
        """
        return self._notify_user

    @notify_user.setter
    def notify_user(self, notify_user):
        """Sets the notify_user of this TranslationsCreateTranslationBody.

        Whether a user notification should be generated on completion  # noqa: E501

        :param notify_user: The notify_user of this TranslationsCreateTranslationBody.  # noqa: E501
        :type: bool
        """

        self._notify_user = notify_user

    @property
    def store_in_document(self):
        """Gets the store_in_document of this TranslationsCreateTranslationBody.  # noqa: E501

        controls whether the translation is stored as a new element or        whether the data is stored as external data (storeInDocument=false).  # noqa: E501

        :return: The store_in_document of this TranslationsCreateTranslationBody.  # noqa: E501
        :rtype: bool
        """
        return self._store_in_document

    @store_in_document.setter
    def store_in_document(self, store_in_document):
        """Sets the store_in_document of this TranslationsCreateTranslationBody.

        controls whether the translation is stored as a new element or        whether the data is stored as external data (storeInDocument=false).  # noqa: E501

        :param store_in_document: The store_in_document of this TranslationsCreateTranslationBody.  # noqa: E501
        :type: bool
        """

        self._store_in_document = store_in_document

    @property
    def allow_faulty_parts(self):
        """Gets the allow_faulty_parts of this TranslationsCreateTranslationBody.  # noqa: E501

        If not specified or if specified as false, bodies to be imported        are examined for validity and any found to be faulty are removed from the import. If all bodies are found to        be faulty, the import fails. If the value is specified as true, we attempt to import the bodies that appear to        have faults.  # noqa: E501

        :return: The allow_faulty_parts of this TranslationsCreateTranslationBody.  # noqa: E501
        :rtype: bool
        """
        return self._allow_faulty_parts

    @allow_faulty_parts.setter
    def allow_faulty_parts(self, allow_faulty_parts):
        """Sets the allow_faulty_parts of this TranslationsCreateTranslationBody.

        If not specified or if specified as false, bodies to be imported        are examined for validity and any found to be faulty are removed from the import. If all bodies are found to        be faulty, the import fails. If the value is specified as true, we attempt to import the bodies that appear to        have faults.  # noqa: E501

        :param allow_faulty_parts: The allow_faulty_parts of this TranslationsCreateTranslationBody.  # noqa: E501
        :type: bool
        """

        self._allow_faulty_parts = allow_faulty_parts

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
        if not isinstance(other, TranslationsCreateTranslationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
