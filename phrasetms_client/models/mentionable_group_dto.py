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

class MentionableGroupDto(object):
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
        'group_type': 'str',
        'group_name': 'str',
        'group_reference': 'UidReference'
    }

    attribute_map = {
        'group_type': 'groupType',
        'group_name': 'groupName',
        'group_reference': 'groupReference'
    }

    def __init__(self, group_type=None, group_name=None, group_reference=None):  # noqa: E501
        """MentionableGroupDto - a model defined in Swagger"""  # noqa: E501
        self._group_type = None
        self._group_name = None
        self._group_reference = None
        self.discriminator = None
        if group_type is not None:
            self.group_type = group_type
        if group_name is not None:
            self.group_name = group_name
        if group_reference is not None:
            self.group_reference = group_reference

    @property
    def group_type(self):
        """Gets the group_type of this MentionableGroupDto.  # noqa: E501


        :return: The group_type of this MentionableGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this MentionableGroupDto.


        :param group_type: The group_type of this MentionableGroupDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["JOB", "OWNERS", "PROVIDERS", "GUESTS", "WORKFLOW_STEP"]  # noqa: E501
        if group_type not in allowed_values:
            raise ValueError(
                "Invalid value for `group_type` ({0}), must be one of {1}"  # noqa: E501
                .format(group_type, allowed_values)
            )

        self._group_type = group_type

    @property
    def group_name(self):
        """Gets the group_name of this MentionableGroupDto.  # noqa: E501


        :return: The group_name of this MentionableGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this MentionableGroupDto.


        :param group_name: The group_name of this MentionableGroupDto.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def group_reference(self):
        """Gets the group_reference of this MentionableGroupDto.  # noqa: E501


        :return: The group_reference of this MentionableGroupDto.  # noqa: E501
        :rtype: UidReference
        """
        return self._group_reference

    @group_reference.setter
    def group_reference(self, group_reference):
        """Sets the group_reference of this MentionableGroupDto.


        :param group_reference: The group_reference of this MentionableGroupDto.  # noqa: E501
        :type: UidReference
        """

        self._group_reference = group_reference

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
        if issubclass(MentionableGroupDto, dict):
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
        if not isinstance(other, MentionableGroupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other