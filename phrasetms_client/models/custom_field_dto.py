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

class CustomFieldDto(object):
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
        'type': 'str',
        'allowed_entities': 'list[str]',
        'options': 'CustomFieldOptionsTruncatedDto',
        'created_at': 'datetime',
        'created_by': 'UserReference',
        'last_modified': 'datetime',
        'last_modified_by': 'UserReference',
        'required_from': 'datetime',
        'required': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'type': 'type',
        'allowed_entities': 'allowedEntities',
        'options': 'options',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'last_modified': 'lastModified',
        'last_modified_by': 'lastModifiedBy',
        'required_from': 'requiredFrom',
        'required': 'required',
        'description': 'description'
    }

    def __init__(self, uid=None, name=None, type=None, allowed_entities=None, options=None, created_at=None, created_by=None, last_modified=None, last_modified_by=None, required_from=None, required=None, description=None):  # noqa: E501
        """CustomFieldDto - a model defined in Swagger"""  # noqa: E501
        self._uid = None
        self._name = None
        self._type = None
        self._allowed_entities = None
        self._options = None
        self._created_at = None
        self._created_by = None
        self._last_modified = None
        self._last_modified_by = None
        self._required_from = None
        self._required = None
        self._description = None
        self.discriminator = None
        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if allowed_entities is not None:
            self.allowed_entities = allowed_entities
        if options is not None:
            self.options = options
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if last_modified is not None:
            self.last_modified = last_modified
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if required_from is not None:
            self.required_from = required_from
        if required is not None:
            self.required = required
        if description is not None:
            self.description = description

    @property
    def uid(self):
        """Gets the uid of this CustomFieldDto.  # noqa: E501


        :return: The uid of this CustomFieldDto.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this CustomFieldDto.


        :param uid: The uid of this CustomFieldDto.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this CustomFieldDto.  # noqa: E501


        :return: The name of this CustomFieldDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomFieldDto.


        :param name: The name of this CustomFieldDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this CustomFieldDto.  # noqa: E501


        :return: The type of this CustomFieldDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomFieldDto.


        :param type: The type of this CustomFieldDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["MULTI_SELECT", "SINGLE_SELECT", "STRING", "NUMBER", "URL", "DATE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def allowed_entities(self):
        """Gets the allowed_entities of this CustomFieldDto.  # noqa: E501


        :return: The allowed_entities of this CustomFieldDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_entities

    @allowed_entities.setter
    def allowed_entities(self, allowed_entities):
        """Sets the allowed_entities of this CustomFieldDto.


        :param allowed_entities: The allowed_entities of this CustomFieldDto.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["PROJECT"]  # noqa: E501
        if not set(allowed_entities).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `allowed_entities` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allowed_entities) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allowed_entities = allowed_entities

    @property
    def options(self):
        """Gets the options of this CustomFieldDto.  # noqa: E501


        :return: The options of this CustomFieldDto.  # noqa: E501
        :rtype: CustomFieldOptionsTruncatedDto
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CustomFieldDto.


        :param options: The options of this CustomFieldDto.  # noqa: E501
        :type: CustomFieldOptionsTruncatedDto
        """

        self._options = options

    @property
    def created_at(self):
        """Gets the created_at of this CustomFieldDto.  # noqa: E501


        :return: The created_at of this CustomFieldDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CustomFieldDto.


        :param created_at: The created_at of this CustomFieldDto.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this CustomFieldDto.  # noqa: E501


        :return: The created_by of this CustomFieldDto.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CustomFieldDto.


        :param created_by: The created_by of this CustomFieldDto.  # noqa: E501
        :type: UserReference
        """

        self._created_by = created_by

    @property
    def last_modified(self):
        """Gets the last_modified of this CustomFieldDto.  # noqa: E501


        :return: The last_modified of this CustomFieldDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this CustomFieldDto.


        :param last_modified: The last_modified of this CustomFieldDto.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this CustomFieldDto.  # noqa: E501


        :return: The last_modified_by of this CustomFieldDto.  # noqa: E501
        :rtype: UserReference
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this CustomFieldDto.


        :param last_modified_by: The last_modified_by of this CustomFieldDto.  # noqa: E501
        :type: UserReference
        """

        self._last_modified_by = last_modified_by

    @property
    def required_from(self):
        """Gets the required_from of this CustomFieldDto.  # noqa: E501


        :return: The required_from of this CustomFieldDto.  # noqa: E501
        :rtype: datetime
        """
        return self._required_from

    @required_from.setter
    def required_from(self, required_from):
        """Sets the required_from of this CustomFieldDto.


        :param required_from: The required_from of this CustomFieldDto.  # noqa: E501
        :type: datetime
        """

        self._required_from = required_from

    @property
    def required(self):
        """Gets the required of this CustomFieldDto.  # noqa: E501


        :return: The required of this CustomFieldDto.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this CustomFieldDto.


        :param required: The required of this CustomFieldDto.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def description(self):
        """Gets the description of this CustomFieldDto.  # noqa: E501


        :return: The description of this CustomFieldDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomFieldDto.


        :param description: The description of this CustomFieldDto.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(CustomFieldDto, dict):
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
        if not isinstance(other, CustomFieldDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other