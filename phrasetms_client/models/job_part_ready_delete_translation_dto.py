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

class JobPartReadyDeleteTranslationDto(object):
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
        'jobs': 'list[UidReference]',
        'delete_settings': 'TranslationSegmentsReferenceV2',
        'for_all_jobs': 'bool',
        'workflow_level': 'int',
        'filter': 'JobPartReadyDeleteTranslationFilterDto',
        'get_parts': 'object'
    }

    attribute_map = {
        'jobs': 'jobs',
        'delete_settings': 'deleteSettings',
        'for_all_jobs': 'forAllJobs',
        'workflow_level': 'workflowLevel',
        'filter': 'filter',
        'get_parts': 'getParts'
    }

    def __init__(self, jobs=None, delete_settings=None, for_all_jobs=None, workflow_level=None, filter=None, get_parts=None):  # noqa: E501
        """JobPartReadyDeleteTranslationDto - a model defined in Swagger"""  # noqa: E501
        self._jobs = None
        self._delete_settings = None
        self._for_all_jobs = None
        self._workflow_level = None
        self._filter = None
        self._get_parts = None
        self.discriminator = None
        if jobs is not None:
            self.jobs = jobs
        if delete_settings is not None:
            self.delete_settings = delete_settings
        if for_all_jobs is not None:
            self.for_all_jobs = for_all_jobs
        if workflow_level is not None:
            self.workflow_level = workflow_level
        if filter is not None:
            self.filter = filter
        if get_parts is not None:
            self.get_parts = get_parts

    @property
    def jobs(self):
        """Gets the jobs of this JobPartReadyDeleteTranslationDto.  # noqa: E501


        :return: The jobs of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :rtype: list[UidReference]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this JobPartReadyDeleteTranslationDto.


        :param jobs: The jobs of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :type: list[UidReference]
        """

        self._jobs = jobs

    @property
    def delete_settings(self):
        """Gets the delete_settings of this JobPartReadyDeleteTranslationDto.  # noqa: E501


        :return: The delete_settings of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :rtype: TranslationSegmentsReferenceV2
        """
        return self._delete_settings

    @delete_settings.setter
    def delete_settings(self, delete_settings):
        """Sets the delete_settings of this JobPartReadyDeleteTranslationDto.


        :param delete_settings: The delete_settings of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :type: TranslationSegmentsReferenceV2
        """

        self._delete_settings = delete_settings

    @property
    def for_all_jobs(self):
        """Gets the for_all_jobs of this JobPartReadyDeleteTranslationDto.  # noqa: E501

        Set true if you want to delete translations for all jobs from project from specific workflow step.                Default: false  # noqa: E501

        :return: The for_all_jobs of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :rtype: bool
        """
        return self._for_all_jobs

    @for_all_jobs.setter
    def for_all_jobs(self, for_all_jobs):
        """Sets the for_all_jobs of this JobPartReadyDeleteTranslationDto.

        Set true if you want to delete translations for all jobs from project from specific workflow step.                Default: false  # noqa: E501

        :param for_all_jobs: The for_all_jobs of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :type: bool
        """

        self._for_all_jobs = for_all_jobs

    @property
    def workflow_level(self):
        """Gets the workflow_level of this JobPartReadyDeleteTranslationDto.  # noqa: E501

        Specifies workflow level for all jobs  # noqa: E501

        :return: The workflow_level of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :rtype: int
        """
        return self._workflow_level

    @workflow_level.setter
    def workflow_level(self, workflow_level):
        """Sets the workflow_level of this JobPartReadyDeleteTranslationDto.

        Specifies workflow level for all jobs  # noqa: E501

        :param workflow_level: The workflow_level of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :type: int
        """

        self._workflow_level = workflow_level

    @property
    def filter(self):
        """Gets the filter of this JobPartReadyDeleteTranslationDto.  # noqa: E501


        :return: The filter of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :rtype: JobPartReadyDeleteTranslationFilterDto
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this JobPartReadyDeleteTranslationDto.


        :param filter: The filter of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :type: JobPartReadyDeleteTranslationFilterDto
        """

        self._filter = filter

    @property
    def get_parts(self):
        """Gets the get_parts of this JobPartReadyDeleteTranslationDto.  # noqa: E501


        :return: The get_parts of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :rtype: object
        """
        return self._get_parts

    @get_parts.setter
    def get_parts(self, get_parts):
        """Sets the get_parts of this JobPartReadyDeleteTranslationDto.


        :param get_parts: The get_parts of this JobPartReadyDeleteTranslationDto.  # noqa: E501
        :type: object
        """

        self._get_parts = get_parts

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
        if issubclass(JobPartReadyDeleteTranslationDto, dict):
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
        if not isinstance(other, JobPartReadyDeleteTranslationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other