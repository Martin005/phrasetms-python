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
from phrasetms_client.models.user_details_dto_v3 import UserDetailsDtoV3  # noqa: F401,E501

class GUESTRESPONSE(UserDetailsDtoV3):
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
        'client': 'ClientReference',
        'enable_mt': 'bool',
        'project_view_other': 'bool',
        'project_view_other_linguist': 'bool',
        'project_view_other_editor': 'bool',
        'trans_memory_view_other': 'bool',
        'trans_memory_edit_other': 'bool',
        'trans_memory_export_other': 'bool',
        'trans_memory_import_other': 'bool',
        'term_base_view_other': 'bool',
        'term_base_edit_other': 'bool',
        'term_base_export_other': 'bool',
        'term_base_import_other': 'bool',
        'term_base_approve_other': 'bool'
    }
    if hasattr(UserDetailsDtoV3, "swagger_types"):
        swagger_types.update(UserDetailsDtoV3.swagger_types)

    attribute_map = {
        'client': 'client',
        'enable_mt': 'enableMT',
        'project_view_other': 'projectViewOther',
        'project_view_other_linguist': 'projectViewOtherLinguist',
        'project_view_other_editor': 'projectViewOtherEditor',
        'trans_memory_view_other': 'transMemoryViewOther',
        'trans_memory_edit_other': 'transMemoryEditOther',
        'trans_memory_export_other': 'transMemoryExportOther',
        'trans_memory_import_other': 'transMemoryImportOther',
        'term_base_view_other': 'termBaseViewOther',
        'term_base_edit_other': 'termBaseEditOther',
        'term_base_export_other': 'termBaseExportOther',
        'term_base_import_other': 'termBaseImportOther',
        'term_base_approve_other': 'termBaseApproveOther'
    }
    if hasattr(UserDetailsDtoV3, "attribute_map"):
        attribute_map.update(UserDetailsDtoV3.attribute_map)

    def __init__(self, client=None, enable_mt=None, project_view_other=None, project_view_other_linguist=None, project_view_other_editor=None, trans_memory_view_other=None, trans_memory_edit_other=None, trans_memory_export_other=None, trans_memory_import_other=None, term_base_view_other=None, term_base_edit_other=None, term_base_export_other=None, term_base_import_other=None, term_base_approve_other=None, *args, **kwargs):  # noqa: E501
        """GUESTRESPONSE - a model defined in Swagger"""  # noqa: E501
        self._client = None
        self._enable_mt = None
        self._project_view_other = None
        self._project_view_other_linguist = None
        self._project_view_other_editor = None
        self._trans_memory_view_other = None
        self._trans_memory_edit_other = None
        self._trans_memory_export_other = None
        self._trans_memory_import_other = None
        self._term_base_view_other = None
        self._term_base_edit_other = None
        self._term_base_export_other = None
        self._term_base_import_other = None
        self._term_base_approve_other = None
        self.discriminator = None
        self.client = client
        if enable_mt is not None:
            self.enable_mt = enable_mt
        if project_view_other is not None:
            self.project_view_other = project_view_other
        if project_view_other_linguist is not None:
            self.project_view_other_linguist = project_view_other_linguist
        if project_view_other_editor is not None:
            self.project_view_other_editor = project_view_other_editor
        if trans_memory_view_other is not None:
            self.trans_memory_view_other = trans_memory_view_other
        if trans_memory_edit_other is not None:
            self.trans_memory_edit_other = trans_memory_edit_other
        if trans_memory_export_other is not None:
            self.trans_memory_export_other = trans_memory_export_other
        if trans_memory_import_other is not None:
            self.trans_memory_import_other = trans_memory_import_other
        if term_base_view_other is not None:
            self.term_base_view_other = term_base_view_other
        if term_base_edit_other is not None:
            self.term_base_edit_other = term_base_edit_other
        if term_base_export_other is not None:
            self.term_base_export_other = term_base_export_other
        if term_base_import_other is not None:
            self.term_base_import_other = term_base_import_other
        if term_base_approve_other is not None:
            self.term_base_approve_other = term_base_approve_other
        UserDetailsDtoV3.__init__(self, *args, **kwargs)

    @property
    def client(self):
        """Gets the client of this GUESTRESPONSE.  # noqa: E501


        :return: The client of this GUESTRESPONSE.  # noqa: E501
        :rtype: ClientReference
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this GUESTRESPONSE.


        :param client: The client of this GUESTRESPONSE.  # noqa: E501
        :type: ClientReference
        """
        if client is None:
            raise ValueError("Invalid value for `client`, must not be `None`")  # noqa: E501

        self._client = client

    @property
    def enable_mt(self):
        """Gets the enable_mt of this GUESTRESPONSE.  # noqa: E501


        :return: The enable_mt of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._enable_mt

    @enable_mt.setter
    def enable_mt(self, enable_mt):
        """Sets the enable_mt of this GUESTRESPONSE.


        :param enable_mt: The enable_mt of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._enable_mt = enable_mt

    @property
    def project_view_other(self):
        """Gets the project_view_other of this GUESTRESPONSE.  # noqa: E501


        :return: The project_view_other of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._project_view_other

    @project_view_other.setter
    def project_view_other(self, project_view_other):
        """Sets the project_view_other of this GUESTRESPONSE.


        :param project_view_other: The project_view_other of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._project_view_other = project_view_other

    @property
    def project_view_other_linguist(self):
        """Gets the project_view_other_linguist of this GUESTRESPONSE.  # noqa: E501


        :return: The project_view_other_linguist of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._project_view_other_linguist

    @project_view_other_linguist.setter
    def project_view_other_linguist(self, project_view_other_linguist):
        """Sets the project_view_other_linguist of this GUESTRESPONSE.


        :param project_view_other_linguist: The project_view_other_linguist of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._project_view_other_linguist = project_view_other_linguist

    @property
    def project_view_other_editor(self):
        """Gets the project_view_other_editor of this GUESTRESPONSE.  # noqa: E501


        :return: The project_view_other_editor of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._project_view_other_editor

    @project_view_other_editor.setter
    def project_view_other_editor(self, project_view_other_editor):
        """Sets the project_view_other_editor of this GUESTRESPONSE.


        :param project_view_other_editor: The project_view_other_editor of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._project_view_other_editor = project_view_other_editor

    @property
    def trans_memory_view_other(self):
        """Gets the trans_memory_view_other of this GUESTRESPONSE.  # noqa: E501


        :return: The trans_memory_view_other of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._trans_memory_view_other

    @trans_memory_view_other.setter
    def trans_memory_view_other(self, trans_memory_view_other):
        """Sets the trans_memory_view_other of this GUESTRESPONSE.


        :param trans_memory_view_other: The trans_memory_view_other of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._trans_memory_view_other = trans_memory_view_other

    @property
    def trans_memory_edit_other(self):
        """Gets the trans_memory_edit_other of this GUESTRESPONSE.  # noqa: E501


        :return: The trans_memory_edit_other of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._trans_memory_edit_other

    @trans_memory_edit_other.setter
    def trans_memory_edit_other(self, trans_memory_edit_other):
        """Sets the trans_memory_edit_other of this GUESTRESPONSE.


        :param trans_memory_edit_other: The trans_memory_edit_other of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._trans_memory_edit_other = trans_memory_edit_other

    @property
    def trans_memory_export_other(self):
        """Gets the trans_memory_export_other of this GUESTRESPONSE.  # noqa: E501


        :return: The trans_memory_export_other of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._trans_memory_export_other

    @trans_memory_export_other.setter
    def trans_memory_export_other(self, trans_memory_export_other):
        """Sets the trans_memory_export_other of this GUESTRESPONSE.


        :param trans_memory_export_other: The trans_memory_export_other of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._trans_memory_export_other = trans_memory_export_other

    @property
    def trans_memory_import_other(self):
        """Gets the trans_memory_import_other of this GUESTRESPONSE.  # noqa: E501


        :return: The trans_memory_import_other of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._trans_memory_import_other

    @trans_memory_import_other.setter
    def trans_memory_import_other(self, trans_memory_import_other):
        """Sets the trans_memory_import_other of this GUESTRESPONSE.


        :param trans_memory_import_other: The trans_memory_import_other of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._trans_memory_import_other = trans_memory_import_other

    @property
    def term_base_view_other(self):
        """Gets the term_base_view_other of this GUESTRESPONSE.  # noqa: E501


        :return: The term_base_view_other of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._term_base_view_other

    @term_base_view_other.setter
    def term_base_view_other(self, term_base_view_other):
        """Sets the term_base_view_other of this GUESTRESPONSE.


        :param term_base_view_other: The term_base_view_other of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._term_base_view_other = term_base_view_other

    @property
    def term_base_edit_other(self):
        """Gets the term_base_edit_other of this GUESTRESPONSE.  # noqa: E501


        :return: The term_base_edit_other of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._term_base_edit_other

    @term_base_edit_other.setter
    def term_base_edit_other(self, term_base_edit_other):
        """Sets the term_base_edit_other of this GUESTRESPONSE.


        :param term_base_edit_other: The term_base_edit_other of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._term_base_edit_other = term_base_edit_other

    @property
    def term_base_export_other(self):
        """Gets the term_base_export_other of this GUESTRESPONSE.  # noqa: E501


        :return: The term_base_export_other of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._term_base_export_other

    @term_base_export_other.setter
    def term_base_export_other(self, term_base_export_other):
        """Sets the term_base_export_other of this GUESTRESPONSE.


        :param term_base_export_other: The term_base_export_other of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._term_base_export_other = term_base_export_other

    @property
    def term_base_import_other(self):
        """Gets the term_base_import_other of this GUESTRESPONSE.  # noqa: E501


        :return: The term_base_import_other of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._term_base_import_other

    @term_base_import_other.setter
    def term_base_import_other(self, term_base_import_other):
        """Sets the term_base_import_other of this GUESTRESPONSE.


        :param term_base_import_other: The term_base_import_other of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._term_base_import_other = term_base_import_other

    @property
    def term_base_approve_other(self):
        """Gets the term_base_approve_other of this GUESTRESPONSE.  # noqa: E501


        :return: The term_base_approve_other of this GUESTRESPONSE.  # noqa: E501
        :rtype: bool
        """
        return self._term_base_approve_other

    @term_base_approve_other.setter
    def term_base_approve_other(self, term_base_approve_other):
        """Sets the term_base_approve_other of this GUESTRESPONSE.


        :param term_base_approve_other: The term_base_approve_other of this GUESTRESPONSE.  # noqa: E501
        :type: bool
        """

        self._term_base_approve_other = term_base_approve_other

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
        if issubclass(GUESTRESPONSE, dict):
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
        if not isinstance(other, GUESTRESPONSE):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other