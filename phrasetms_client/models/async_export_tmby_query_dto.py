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

class AsyncExportTMByQueryDto(object):
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
        'async_request': 'ObjectReference',
        'trans_memory': 'ObjectReference',
        'export_target_langs': 'list[str]',
        'queries': 'list[Query]'
    }

    attribute_map = {
        'async_request': 'asyncRequest',
        'trans_memory': 'transMemory',
        'export_target_langs': 'exportTargetLangs',
        'queries': 'queries'
    }

    def __init__(self, async_request=None, trans_memory=None, export_target_langs=None, queries=None):  # noqa: E501
        """AsyncExportTMByQueryDto - a model defined in Swagger"""  # noqa: E501
        self._async_request = None
        self._trans_memory = None
        self._export_target_langs = None
        self._queries = None
        self.discriminator = None
        if async_request is not None:
            self.async_request = async_request
        if trans_memory is not None:
            self.trans_memory = trans_memory
        if export_target_langs is not None:
            self.export_target_langs = export_target_langs
        if queries is not None:
            self.queries = queries

    @property
    def async_request(self):
        """Gets the async_request of this AsyncExportTMByQueryDto.  # noqa: E501


        :return: The async_request of this AsyncExportTMByQueryDto.  # noqa: E501
        :rtype: ObjectReference
        """
        return self._async_request

    @async_request.setter
    def async_request(self, async_request):
        """Sets the async_request of this AsyncExportTMByQueryDto.


        :param async_request: The async_request of this AsyncExportTMByQueryDto.  # noqa: E501
        :type: ObjectReference
        """

        self._async_request = async_request

    @property
    def trans_memory(self):
        """Gets the trans_memory of this AsyncExportTMByQueryDto.  # noqa: E501


        :return: The trans_memory of this AsyncExportTMByQueryDto.  # noqa: E501
        :rtype: ObjectReference
        """
        return self._trans_memory

    @trans_memory.setter
    def trans_memory(self, trans_memory):
        """Sets the trans_memory of this AsyncExportTMByQueryDto.


        :param trans_memory: The trans_memory of this AsyncExportTMByQueryDto.  # noqa: E501
        :type: ObjectReference
        """

        self._trans_memory = trans_memory

    @property
    def export_target_langs(self):
        """Gets the export_target_langs of this AsyncExportTMByQueryDto.  # noqa: E501


        :return: The export_target_langs of this AsyncExportTMByQueryDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._export_target_langs

    @export_target_langs.setter
    def export_target_langs(self, export_target_langs):
        """Sets the export_target_langs of this AsyncExportTMByQueryDto.


        :param export_target_langs: The export_target_langs of this AsyncExportTMByQueryDto.  # noqa: E501
        :type: list[str]
        """

        self._export_target_langs = export_target_langs

    @property
    def queries(self):
        """Gets the queries of this AsyncExportTMByQueryDto.  # noqa: E501


        :return: The queries of this AsyncExportTMByQueryDto.  # noqa: E501
        :rtype: list[Query]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this AsyncExportTMByQueryDto.


        :param queries: The queries of this AsyncExportTMByQueryDto.  # noqa: E501
        :type: list[Query]
        """

        self._queries = queries

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
        if issubclass(AsyncExportTMByQueryDto, dict):
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
        if not isinstance(other, AsyncExportTMByQueryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other