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

class LastLoginDto(object):
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
        'user': 'UserReference',
        'last_login_date': 'datetime'
    }

    attribute_map = {
        'user': 'user',
        'last_login_date': 'lastLoginDate'
    }

    def __init__(self, user=None, last_login_date=None):  # noqa: E501
        """LastLoginDto - a model defined in Swagger"""  # noqa: E501
        self._user = None
        self._last_login_date = None
        self.discriminator = None
        if user is not None:
            self.user = user
        if last_login_date is not None:
            self.last_login_date = last_login_date

    @property
    def user(self):
        """Gets the user of this LastLoginDto.  # noqa: E501


        :return: The user of this LastLoginDto.  # noqa: E501
        :rtype: UserReference
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LastLoginDto.


        :param user: The user of this LastLoginDto.  # noqa: E501
        :type: UserReference
        """

        self._user = user

    @property
    def last_login_date(self):
        """Gets the last_login_date of this LastLoginDto.  # noqa: E501


        :return: The last_login_date of this LastLoginDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_date

    @last_login_date.setter
    def last_login_date(self, last_login_date):
        """Sets the last_login_date of this LastLoginDto.


        :param last_login_date: The last_login_date of this LastLoginDto.  # noqa: E501
        :type: datetime
        """

        self._last_login_date = last_login_date

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
        if issubclass(LastLoginDto, dict):
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
        if not isinstance(other, LastLoginDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other