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

class CreateAnalyseAsyncV2Dto(object):
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
        'type': 'str',
        'include_fuzzy_repetitions': 'bool',
        'separate_fuzzy_repetitions': 'bool',
        'include_confirmed_segments': 'bool',
        'include_numbers': 'bool',
        'include_locked_segments': 'bool',
        'count_source_units': 'bool',
        'include_trans_memory': 'bool',
        'include_non_translatables': 'bool',
        'include_machine_translation_matches': 'bool',
        'trans_memory_post_editing': 'bool',
        'non_translatable_post_editing': 'bool',
        'machine_translate_post_editing': 'bool',
        'name': 'str',
        'net_rate_scheme': 'IdReference',
        'compare_workflow_level': 'int',
        'use_project_analysis_settings': 'bool',
        'callback_url': 'str',
        'provider': 'ProviderReference'
    }

    attribute_map = {
        'jobs': 'jobs',
        'type': 'type',
        'include_fuzzy_repetitions': 'includeFuzzyRepetitions',
        'separate_fuzzy_repetitions': 'separateFuzzyRepetitions',
        'include_confirmed_segments': 'includeConfirmedSegments',
        'include_numbers': 'includeNumbers',
        'include_locked_segments': 'includeLockedSegments',
        'count_source_units': 'countSourceUnits',
        'include_trans_memory': 'includeTransMemory',
        'include_non_translatables': 'includeNonTranslatables',
        'include_machine_translation_matches': 'includeMachineTranslationMatches',
        'trans_memory_post_editing': 'transMemoryPostEditing',
        'non_translatable_post_editing': 'nonTranslatablePostEditing',
        'machine_translate_post_editing': 'machineTranslatePostEditing',
        'name': 'name',
        'net_rate_scheme': 'netRateScheme',
        'compare_workflow_level': 'compareWorkflowLevel',
        'use_project_analysis_settings': 'useProjectAnalysisSettings',
        'callback_url': 'callbackUrl',
        'provider': 'provider'
    }

    def __init__(self, jobs=None, type=None, include_fuzzy_repetitions=None, separate_fuzzy_repetitions=None, include_confirmed_segments=None, include_numbers=None, include_locked_segments=None, count_source_units=None, include_trans_memory=None, include_non_translatables=None, include_machine_translation_matches=None, trans_memory_post_editing=None, non_translatable_post_editing=None, machine_translate_post_editing=None, name=None, net_rate_scheme=None, compare_workflow_level=None, use_project_analysis_settings=None, callback_url=None, provider=None):  # noqa: E501
        """CreateAnalyseAsyncV2Dto - a model defined in Swagger"""  # noqa: E501
        self._jobs = None
        self._type = None
        self._include_fuzzy_repetitions = None
        self._separate_fuzzy_repetitions = None
        self._include_confirmed_segments = None
        self._include_numbers = None
        self._include_locked_segments = None
        self._count_source_units = None
        self._include_trans_memory = None
        self._include_non_translatables = None
        self._include_machine_translation_matches = None
        self._trans_memory_post_editing = None
        self._non_translatable_post_editing = None
        self._machine_translate_post_editing = None
        self._name = None
        self._net_rate_scheme = None
        self._compare_workflow_level = None
        self._use_project_analysis_settings = None
        self._callback_url = None
        self._provider = None
        self.discriminator = None
        self.jobs = jobs
        if type is not None:
            self.type = type
        if include_fuzzy_repetitions is not None:
            self.include_fuzzy_repetitions = include_fuzzy_repetitions
        if separate_fuzzy_repetitions is not None:
            self.separate_fuzzy_repetitions = separate_fuzzy_repetitions
        if include_confirmed_segments is not None:
            self.include_confirmed_segments = include_confirmed_segments
        if include_numbers is not None:
            self.include_numbers = include_numbers
        if include_locked_segments is not None:
            self.include_locked_segments = include_locked_segments
        if count_source_units is not None:
            self.count_source_units = count_source_units
        if include_trans_memory is not None:
            self.include_trans_memory = include_trans_memory
        if include_non_translatables is not None:
            self.include_non_translatables = include_non_translatables
        if include_machine_translation_matches is not None:
            self.include_machine_translation_matches = include_machine_translation_matches
        if trans_memory_post_editing is not None:
            self.trans_memory_post_editing = trans_memory_post_editing
        if non_translatable_post_editing is not None:
            self.non_translatable_post_editing = non_translatable_post_editing
        if machine_translate_post_editing is not None:
            self.machine_translate_post_editing = machine_translate_post_editing
        if name is not None:
            self.name = name
        if net_rate_scheme is not None:
            self.net_rate_scheme = net_rate_scheme
        if compare_workflow_level is not None:
            self.compare_workflow_level = compare_workflow_level
        if use_project_analysis_settings is not None:
            self.use_project_analysis_settings = use_project_analysis_settings
        if callback_url is not None:
            self.callback_url = callback_url
        if provider is not None:
            self.provider = provider

    @property
    def jobs(self):
        """Gets the jobs of this CreateAnalyseAsyncV2Dto.  # noqa: E501


        :return: The jobs of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: list[UidReference]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this CreateAnalyseAsyncV2Dto.


        :param jobs: The jobs of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: list[UidReference]
        """
        if jobs is None:
            raise ValueError("Invalid value for `jobs`, must not be `None`")  # noqa: E501

        self._jobs = jobs

    @property
    def type(self):
        """Gets the type of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        default: PreAnalyse  # noqa: E501

        :return: The type of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateAnalyseAsyncV2Dto.

        default: PreAnalyse  # noqa: E501

        :param type: The type of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: str
        """
        allowed_values = ["PreAnalyse", "PostAnalyse", "Compare"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def include_fuzzy_repetitions(self):
        """Gets the include_fuzzy_repetitions of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: true  # noqa: E501

        :return: The include_fuzzy_repetitions of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._include_fuzzy_repetitions

    @include_fuzzy_repetitions.setter
    def include_fuzzy_repetitions(self, include_fuzzy_repetitions):
        """Sets the include_fuzzy_repetitions of this CreateAnalyseAsyncV2Dto.

        Default: true  # noqa: E501

        :param include_fuzzy_repetitions: The include_fuzzy_repetitions of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._include_fuzzy_repetitions = include_fuzzy_repetitions

    @property
    def separate_fuzzy_repetitions(self):
        """Gets the separate_fuzzy_repetitions of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: false  # noqa: E501

        :return: The separate_fuzzy_repetitions of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._separate_fuzzy_repetitions

    @separate_fuzzy_repetitions.setter
    def separate_fuzzy_repetitions(self, separate_fuzzy_repetitions):
        """Sets the separate_fuzzy_repetitions of this CreateAnalyseAsyncV2Dto.

        Default: false  # noqa: E501

        :param separate_fuzzy_repetitions: The separate_fuzzy_repetitions of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._separate_fuzzy_repetitions = separate_fuzzy_repetitions

    @property
    def include_confirmed_segments(self):
        """Gets the include_confirmed_segments of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: true  # noqa: E501

        :return: The include_confirmed_segments of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._include_confirmed_segments

    @include_confirmed_segments.setter
    def include_confirmed_segments(self, include_confirmed_segments):
        """Sets the include_confirmed_segments of this CreateAnalyseAsyncV2Dto.

        Default: true  # noqa: E501

        :param include_confirmed_segments: The include_confirmed_segments of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._include_confirmed_segments = include_confirmed_segments

    @property
    def include_numbers(self):
        """Gets the include_numbers of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: true  # noqa: E501

        :return: The include_numbers of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._include_numbers

    @include_numbers.setter
    def include_numbers(self, include_numbers):
        """Sets the include_numbers of this CreateAnalyseAsyncV2Dto.

        Default: true  # noqa: E501

        :param include_numbers: The include_numbers of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._include_numbers = include_numbers

    @property
    def include_locked_segments(self):
        """Gets the include_locked_segments of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: true  # noqa: E501

        :return: The include_locked_segments of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._include_locked_segments

    @include_locked_segments.setter
    def include_locked_segments(self, include_locked_segments):
        """Sets the include_locked_segments of this CreateAnalyseAsyncV2Dto.

        Default: true  # noqa: E501

        :param include_locked_segments: The include_locked_segments of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._include_locked_segments = include_locked_segments

    @property
    def count_source_units(self):
        """Gets the count_source_units of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: true  # noqa: E501

        :return: The count_source_units of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._count_source_units

    @count_source_units.setter
    def count_source_units(self, count_source_units):
        """Sets the count_source_units of this CreateAnalyseAsyncV2Dto.

        Default: true  # noqa: E501

        :param count_source_units: The count_source_units of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._count_source_units = count_source_units

    @property
    def include_trans_memory(self):
        """Gets the include_trans_memory of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: true. Works only for type=PreAnalyse.  # noqa: E501

        :return: The include_trans_memory of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._include_trans_memory

    @include_trans_memory.setter
    def include_trans_memory(self, include_trans_memory):
        """Sets the include_trans_memory of this CreateAnalyseAsyncV2Dto.

        Default: true. Works only for type=PreAnalyse.  # noqa: E501

        :param include_trans_memory: The include_trans_memory of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._include_trans_memory = include_trans_memory

    @property
    def include_non_translatables(self):
        """Gets the include_non_translatables of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: false. Works only for type=PreAnalyse.  # noqa: E501

        :return: The include_non_translatables of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._include_non_translatables

    @include_non_translatables.setter
    def include_non_translatables(self, include_non_translatables):
        """Sets the include_non_translatables of this CreateAnalyseAsyncV2Dto.

        Default: false. Works only for type=PreAnalyse.  # noqa: E501

        :param include_non_translatables: The include_non_translatables of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._include_non_translatables = include_non_translatables

    @property
    def include_machine_translation_matches(self):
        """Gets the include_machine_translation_matches of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: false. Works only for type=PreAnalyse.  # noqa: E501

        :return: The include_machine_translation_matches of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._include_machine_translation_matches

    @include_machine_translation_matches.setter
    def include_machine_translation_matches(self, include_machine_translation_matches):
        """Sets the include_machine_translation_matches of this CreateAnalyseAsyncV2Dto.

        Default: false. Works only for type=PreAnalyse.  # noqa: E501

        :param include_machine_translation_matches: The include_machine_translation_matches of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._include_machine_translation_matches = include_machine_translation_matches

    @property
    def trans_memory_post_editing(self):
        """Gets the trans_memory_post_editing of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: false. Works only for type=PostAnalyse.  # noqa: E501

        :return: The trans_memory_post_editing of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._trans_memory_post_editing

    @trans_memory_post_editing.setter
    def trans_memory_post_editing(self, trans_memory_post_editing):
        """Sets the trans_memory_post_editing of this CreateAnalyseAsyncV2Dto.

        Default: false. Works only for type=PostAnalyse.  # noqa: E501

        :param trans_memory_post_editing: The trans_memory_post_editing of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._trans_memory_post_editing = trans_memory_post_editing

    @property
    def non_translatable_post_editing(self):
        """Gets the non_translatable_post_editing of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: false. Works only for type=PostAnalyse.  # noqa: E501

        :return: The non_translatable_post_editing of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._non_translatable_post_editing

    @non_translatable_post_editing.setter
    def non_translatable_post_editing(self, non_translatable_post_editing):
        """Sets the non_translatable_post_editing of this CreateAnalyseAsyncV2Dto.

        Default: false. Works only for type=PostAnalyse.  # noqa: E501

        :param non_translatable_post_editing: The non_translatable_post_editing of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._non_translatable_post_editing = non_translatable_post_editing

    @property
    def machine_translate_post_editing(self):
        """Gets the machine_translate_post_editing of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: false. Works only for type=PostAnalyse.  # noqa: E501

        :return: The machine_translate_post_editing of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._machine_translate_post_editing

    @machine_translate_post_editing.setter
    def machine_translate_post_editing(self, machine_translate_post_editing):
        """Sets the machine_translate_post_editing of this CreateAnalyseAsyncV2Dto.

        Default: false. Works only for type=PostAnalyse.  # noqa: E501

        :param machine_translate_post_editing: The machine_translate_post_editing of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._machine_translate_post_editing = machine_translate_post_editing

    @property
    def name(self):
        """Gets the name of this CreateAnalyseAsyncV2Dto.  # noqa: E501


        :return: The name of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAnalyseAsyncV2Dto.


        :param name: The name of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def net_rate_scheme(self):
        """Gets the net_rate_scheme of this CreateAnalyseAsyncV2Dto.  # noqa: E501


        :return: The net_rate_scheme of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: IdReference
        """
        return self._net_rate_scheme

    @net_rate_scheme.setter
    def net_rate_scheme(self, net_rate_scheme):
        """Sets the net_rate_scheme of this CreateAnalyseAsyncV2Dto.


        :param net_rate_scheme: The net_rate_scheme of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: IdReference
        """

        self._net_rate_scheme = net_rate_scheme

    @property
    def compare_workflow_level(self):
        """Gets the compare_workflow_level of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Required for type=Compare  # noqa: E501

        :return: The compare_workflow_level of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: int
        """
        return self._compare_workflow_level

    @compare_workflow_level.setter
    def compare_workflow_level(self, compare_workflow_level):
        """Sets the compare_workflow_level of this CreateAnalyseAsyncV2Dto.

        Required for type=Compare  # noqa: E501

        :param compare_workflow_level: The compare_workflow_level of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: int
        """

        self._compare_workflow_level = compare_workflow_level

    @property
    def use_project_analysis_settings(self):
        """Gets the use_project_analysis_settings of this CreateAnalyseAsyncV2Dto.  # noqa: E501

        Default: false. Use default project settings. Will be overwritten with setting sent         in the API call.  # noqa: E501

        :return: The use_project_analysis_settings of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._use_project_analysis_settings

    @use_project_analysis_settings.setter
    def use_project_analysis_settings(self, use_project_analysis_settings):
        """Sets the use_project_analysis_settings of this CreateAnalyseAsyncV2Dto.

        Default: false. Use default project settings. Will be overwritten with setting sent         in the API call.  # noqa: E501

        :param use_project_analysis_settings: The use_project_analysis_settings of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: bool
        """

        self._use_project_analysis_settings = use_project_analysis_settings

    @property
    def callback_url(self):
        """Gets the callback_url of this CreateAnalyseAsyncV2Dto.  # noqa: E501


        :return: The callback_url of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this CreateAnalyseAsyncV2Dto.


        :param callback_url: The callback_url of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: str
        """

        self._callback_url = callback_url

    @property
    def provider(self):
        """Gets the provider of this CreateAnalyseAsyncV2Dto.  # noqa: E501


        :return: The provider of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :rtype: ProviderReference
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateAnalyseAsyncV2Dto.


        :param provider: The provider of this CreateAnalyseAsyncV2Dto.  # noqa: E501
        :type: ProviderReference
        """

        self._provider = provider

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
        if issubclass(CreateAnalyseAsyncV2Dto, dict):
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
        if not isinstance(other, CreateAnalyseAsyncV2Dto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other