# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CustomFileTypeDto(object):
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
        'uid': 'str',
        'name': 'str',
        'filename_pattern': 'str',
        'type': 'str',
        'created_by': 'UserReference',
        'date_created': 'datetime',
        'file_import_settings': 'FileImportSettingsDto'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'filename_pattern': 'filenamePattern',
        'type': 'type',
        'created_by': 'createdBy',
        'date_created': 'dateCreated',
        'file_import_settings': 'fileImportSettings'
    }

    def __init__(self, uid=None, name=None, filename_pattern=None, type=None, created_by=None, date_created=None, file_import_settings=None):  # noqa: E501
        """CustomFileTypeDto - a model defined in Swagger"""  # noqa: E501
        self._uid = None
        self._name = None
        self._filename_pattern = None
        self._type = None
        self._created_by = None
        self._date_created = None
        self._file_import_settings = None
        self.discriminator = None
        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if filename_pattern is not None:
            self.filename_pattern = filename_pattern
        if type is not None:
            self.type = type
        if created_by is not None:
            self.created_by = created_by
        if date_created is not None:
            self.date_created = date_created
        if file_import_settings is not None:
            self.file_import_settings = file_import_settings

    @property
    def uid(self):
        """Gets the uid of this CustomFileTypeDto.  # noqa: E501


        :return: The uid of this CustomFileTypeDto.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this CustomFileTypeDto.


        :param uid: The uid of this CustomFileTypeDto.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this CustomFileTypeDto.  # noqa: E501


        :return: The name of this CustomFileTypeDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomFileTypeDto.


        :param name: The name of this CustomFileTypeDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def filename_pattern(self):
        """Gets the filename_pattern of this CustomFileTypeDto.  # noqa: E501


        :return: The filename_pattern of this CustomFileTypeDto.  # noqa: E501
        :rtype: str
        """
        return self._filename_pattern

    @filename_pattern.setter
    def filename_pattern(self, filename_pattern):
        """Sets the filename_pattern of this CustomFileTypeDto.


        :param filename_pattern: The filename_pattern of this CustomFileTypeDto.  # noqa: E501
        :type: str
        """

        self._filename_pattern = filename_pattern

    @property
    def type(self):
        """Gets the type of this CustomFileTypeDto.  # noqa: E501


        :return: The type of this CustomFileTypeDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomFileTypeDto.


        :param type: The type of this CustomFileTypeDto.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_by(self):
        """Gets the created_by of this CustomFileTypeDto.  # noqa: E501


        :return: The created_by of this CustomFileTypeDto.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CustomFileTypeDto.


        :param created_by: The created_by of this CustomFileTypeDto.  # noqa: E501
        :type: UserReference
        """

        self._created_by = created_by

    @property
    def date_created(self):
        """Gets the date_created of this CustomFileTypeDto.  # noqa: E501


        :return: The date_created of this CustomFileTypeDto.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this CustomFileTypeDto.


        :param date_created: The date_created of this CustomFileTypeDto.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def file_import_settings(self):
        """Gets the file_import_settings of this CustomFileTypeDto.  # noqa: E501


        :return: The file_import_settings of this CustomFileTypeDto.  # noqa: E501
        :rtype: FileImportSettingsDto
        """
        return self._file_import_settings

    @file_import_settings.setter
    def file_import_settings(self, file_import_settings):
        """Sets the file_import_settings of this CustomFileTypeDto.


        :param file_import_settings: The file_import_settings of this CustomFileTypeDto.  # noqa: E501
        :type: FileImportSettingsDto
        """

        self._file_import_settings = file_import_settings

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
        if issubclass(CustomFileTypeDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomFileTypeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other