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

class AnalyseLanguagePartReference(object):
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
        'id': 'str',
        'source_lang': 'str',
        'target_lang': 'str',
        'jobs': 'list[AnalyseJobReference]'
    }

    attribute_map = {
        'id': 'id',
        'source_lang': 'sourceLang',
        'target_lang': 'targetLang',
        'jobs': 'jobs'
    }

    def __init__(self, id=None, source_lang=None, target_lang=None, jobs=None):  # noqa: E501
        """AnalyseLanguagePartReference - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._source_lang = None
        self._target_lang = None
        self._jobs = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if source_lang is not None:
            self.source_lang = source_lang
        if target_lang is not None:
            self.target_lang = target_lang
        if jobs is not None:
            self.jobs = jobs

    @property
    def id(self):
        """Gets the id of this AnalyseLanguagePartReference.  # noqa: E501


        :return: The id of this AnalyseLanguagePartReference.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnalyseLanguagePartReference.


        :param id: The id of this AnalyseLanguagePartReference.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source_lang(self):
        """Gets the source_lang of this AnalyseLanguagePartReference.  # noqa: E501


        :return: The source_lang of this AnalyseLanguagePartReference.  # noqa: E501
        :rtype: str
        """
        return self._source_lang

    @source_lang.setter
    def source_lang(self, source_lang):
        """Sets the source_lang of this AnalyseLanguagePartReference.


        :param source_lang: The source_lang of this AnalyseLanguagePartReference.  # noqa: E501
        :type: str
        """

        self._source_lang = source_lang

    @property
    def target_lang(self):
        """Gets the target_lang of this AnalyseLanguagePartReference.  # noqa: E501


        :return: The target_lang of this AnalyseLanguagePartReference.  # noqa: E501
        :rtype: str
        """
        return self._target_lang

    @target_lang.setter
    def target_lang(self, target_lang):
        """Sets the target_lang of this AnalyseLanguagePartReference.


        :param target_lang: The target_lang of this AnalyseLanguagePartReference.  # noqa: E501
        :type: str
        """

        self._target_lang = target_lang

    @property
    def jobs(self):
        """Gets the jobs of this AnalyseLanguagePartReference.  # noqa: E501


        :return: The jobs of this AnalyseLanguagePartReference.  # noqa: E501
        :rtype: list[AnalyseJobReference]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this AnalyseLanguagePartReference.


        :param jobs: The jobs of this AnalyseLanguagePartReference.  # noqa: E501
        :type: list[AnalyseJobReference]
        """

        self._jobs = jobs

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
        if issubclass(AnalyseLanguagePartReference, dict):
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
        if not isinstance(other, AnalyseLanguagePartReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other