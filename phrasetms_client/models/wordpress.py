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
from phrasetms_client.models.abstract_connector_dto import AbstractConnectorDto  # noqa: F401,E501

class Wordpress(AbstractConnectorDto):
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
        'basic_auth_user_name': 'str',
        'basic_auth_password': 'str',
        'host': 'str',
        'token': 'str'
    }
    if hasattr(AbstractConnectorDto, "swagger_types"):
        swagger_types.update(AbstractConnectorDto.swagger_types)

    attribute_map = {
        'basic_auth_user_name': 'basicAuthUserName',
        'basic_auth_password': 'basicAuthPassword',
        'host': 'host',
        'token': 'token'
    }
    if hasattr(AbstractConnectorDto, "attribute_map"):
        attribute_map.update(AbstractConnectorDto.attribute_map)

    def __init__(self, basic_auth_user_name=None, basic_auth_password=None, host=None, token=None, *args, **kwargs):  # noqa: E501
        """Wordpress - a model defined in Swagger"""  # noqa: E501
        self._basic_auth_user_name = None
        self._basic_auth_password = None
        self._host = None
        self._token = None
        self.discriminator = None
        self.basic_auth_user_name = basic_auth_user_name
        self.basic_auth_password = basic_auth_password
        self.host = host
        self.token = token
        AbstractConnectorDto.__init__(self, *args, **kwargs)

    @property
    def basic_auth_user_name(self):
        """Gets the basic_auth_user_name of this Wordpress.  # noqa: E501


        :return: The basic_auth_user_name of this Wordpress.  # noqa: E501
        :rtype: str
        """
        return self._basic_auth_user_name

    @basic_auth_user_name.setter
    def basic_auth_user_name(self, basic_auth_user_name):
        """Sets the basic_auth_user_name of this Wordpress.


        :param basic_auth_user_name: The basic_auth_user_name of this Wordpress.  # noqa: E501
        :type: str
        """
        if basic_auth_user_name is None:
            raise ValueError("Invalid value for `basic_auth_user_name`, must not be `None`")  # noqa: E501

        self._basic_auth_user_name = basic_auth_user_name

    @property
    def basic_auth_password(self):
        """Gets the basic_auth_password of this Wordpress.  # noqa: E501


        :return: The basic_auth_password of this Wordpress.  # noqa: E501
        :rtype: str
        """
        return self._basic_auth_password

    @basic_auth_password.setter
    def basic_auth_password(self, basic_auth_password):
        """Sets the basic_auth_password of this Wordpress.


        :param basic_auth_password: The basic_auth_password of this Wordpress.  # noqa: E501
        :type: str
        """
        if basic_auth_password is None:
            raise ValueError("Invalid value for `basic_auth_password`, must not be `None`")  # noqa: E501

        self._basic_auth_password = basic_auth_password

    @property
    def host(self):
        """Gets the host of this Wordpress.  # noqa: E501


        :return: The host of this Wordpress.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Wordpress.


        :param host: The host of this Wordpress.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def token(self):
        """Gets the token of this Wordpress.  # noqa: E501

        Memsource plugin token  # noqa: E501

        :return: The token of this Wordpress.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Wordpress.

        Memsource plugin token  # noqa: E501

        :param token: The token of this Wordpress.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

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
        if issubclass(Wordpress, dict):
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
        if not isinstance(other, Wordpress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other