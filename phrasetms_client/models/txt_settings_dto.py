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

class TxtSettingsDto(object):
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
        'tag_regexp': 'str',
        'translatable_text_regexp': 'str',
        'context_key': 'str',
        'regexp_capturing_groups': 'bool'
    }

    attribute_map = {
        'tag_regexp': 'tagRegexp',
        'translatable_text_regexp': 'translatableTextRegexp',
        'context_key': 'contextKey',
        'regexp_capturing_groups': 'regexpCapturingGroups'
    }

    def __init__(self, tag_regexp=None, translatable_text_regexp=None, context_key=None, regexp_capturing_groups=None):  # noqa: E501
        """TxtSettingsDto - a model defined in Swagger"""  # noqa: E501
        self._tag_regexp = None
        self._translatable_text_regexp = None
        self._context_key = None
        self._regexp_capturing_groups = None
        self.discriminator = None
        if tag_regexp is not None:
            self.tag_regexp = tag_regexp
        if translatable_text_regexp is not None:
            self.translatable_text_regexp = translatable_text_regexp
        if context_key is not None:
            self.context_key = context_key
        if regexp_capturing_groups is not None:
            self.regexp_capturing_groups = regexp_capturing_groups

    @property
    def tag_regexp(self):
        """Gets the tag_regexp of this TxtSettingsDto.  # noqa: E501


        :return: The tag_regexp of this TxtSettingsDto.  # noqa: E501
        :rtype: str
        """
        return self._tag_regexp

    @tag_regexp.setter
    def tag_regexp(self, tag_regexp):
        """Sets the tag_regexp of this TxtSettingsDto.


        :param tag_regexp: The tag_regexp of this TxtSettingsDto.  # noqa: E501
        :type: str
        """

        self._tag_regexp = tag_regexp

    @property
    def translatable_text_regexp(self):
        """Gets the translatable_text_regexp of this TxtSettingsDto.  # noqa: E501


        :return: The translatable_text_regexp of this TxtSettingsDto.  # noqa: E501
        :rtype: str
        """
        return self._translatable_text_regexp

    @translatable_text_regexp.setter
    def translatable_text_regexp(self, translatable_text_regexp):
        """Sets the translatable_text_regexp of this TxtSettingsDto.


        :param translatable_text_regexp: The translatable_text_regexp of this TxtSettingsDto.  # noqa: E501
        :type: str
        """

        self._translatable_text_regexp = translatable_text_regexp

    @property
    def context_key(self):
        """Gets the context_key of this TxtSettingsDto.  # noqa: E501


        :return: The context_key of this TxtSettingsDto.  # noqa: E501
        :rtype: str
        """
        return self._context_key

    @context_key.setter
    def context_key(self, context_key):
        """Sets the context_key of this TxtSettingsDto.


        :param context_key: The context_key of this TxtSettingsDto.  # noqa: E501
        :type: str
        """

        self._context_key = context_key

    @property
    def regexp_capturing_groups(self):
        """Gets the regexp_capturing_groups of this TxtSettingsDto.  # noqa: E501

        Default: false  # noqa: E501

        :return: The regexp_capturing_groups of this TxtSettingsDto.  # noqa: E501
        :rtype: bool
        """
        return self._regexp_capturing_groups

    @regexp_capturing_groups.setter
    def regexp_capturing_groups(self, regexp_capturing_groups):
        """Sets the regexp_capturing_groups of this TxtSettingsDto.

        Default: false  # noqa: E501

        :param regexp_capturing_groups: The regexp_capturing_groups of this TxtSettingsDto.  # noqa: E501
        :type: bool
        """

        self._regexp_capturing_groups = regexp_capturing_groups

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
        if issubclass(TxtSettingsDto, dict):
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
        if not isinstance(other, TxtSettingsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other