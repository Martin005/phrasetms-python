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

class JobListDto(object):
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
        'unsupported_files': 'list[str]',
        'jobs': 'list[JobPartReference]',
        'async_request': 'AsyncRequestReference'
    }

    attribute_map = {
        'unsupported_files': 'unsupportedFiles',
        'jobs': 'jobs',
        'async_request': 'asyncRequest'
    }

    def __init__(self, unsupported_files=None, jobs=None, async_request=None):  # noqa: E501
        """JobListDto - a model defined in Swagger"""  # noqa: E501
        self._unsupported_files = None
        self._jobs = None
        self._async_request = None
        self.discriminator = None
        if unsupported_files is not None:
            self.unsupported_files = unsupported_files
        if jobs is not None:
            self.jobs = jobs
        if async_request is not None:
            self.async_request = async_request

    @property
    def unsupported_files(self):
        """Gets the unsupported_files of this JobListDto.  # noqa: E501


        :return: The unsupported_files of this JobListDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._unsupported_files

    @unsupported_files.setter
    def unsupported_files(self, unsupported_files):
        """Sets the unsupported_files of this JobListDto.


        :param unsupported_files: The unsupported_files of this JobListDto.  # noqa: E501
        :type: list[str]
        """

        self._unsupported_files = unsupported_files

    @property
    def jobs(self):
        """Gets the jobs of this JobListDto.  # noqa: E501


        :return: The jobs of this JobListDto.  # noqa: E501
        :rtype: list[JobPartReference]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this JobListDto.


        :param jobs: The jobs of this JobListDto.  # noqa: E501
        :type: list[JobPartReference]
        """

        self._jobs = jobs

    @property
    def async_request(self):
        """Gets the async_request of this JobListDto.  # noqa: E501


        :return: The async_request of this JobListDto.  # noqa: E501
        :rtype: AsyncRequestReference
        """
        return self._async_request

    @async_request.setter
    def async_request(self, async_request):
        """Sets the async_request of this JobListDto.


        :param async_request: The async_request of this JobListDto.  # noqa: E501
        :type: AsyncRequestReference
        """

        self._async_request = async_request

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
        if issubclass(JobListDto, dict):
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
        if not isinstance(other, JobListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other