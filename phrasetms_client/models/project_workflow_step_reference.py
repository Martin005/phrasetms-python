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

class ProjectWorkflowStepReference(object):
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
        'name': 'str',
        'id': 'str',
        'order': 'int',
        'workflow_level': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'order': 'order',
        'workflow_level': 'workflowLevel'
    }

    def __init__(self, name=None, id=None, order=None, workflow_level=None):  # noqa: E501
        """ProjectWorkflowStepReference - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._order = None
        self._workflow_level = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if order is not None:
            self.order = order
        if workflow_level is not None:
            self.workflow_level = workflow_level

    @property
    def name(self):
        """Gets the name of this ProjectWorkflowStepReference.  # noqa: E501


        :return: The name of this ProjectWorkflowStepReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectWorkflowStepReference.


        :param name: The name of this ProjectWorkflowStepReference.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this ProjectWorkflowStepReference.  # noqa: E501


        :return: The id of this ProjectWorkflowStepReference.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectWorkflowStepReference.


        :param id: The id of this ProjectWorkflowStepReference.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def order(self):
        """Gets the order of this ProjectWorkflowStepReference.  # noqa: E501


        :return: The order of this ProjectWorkflowStepReference.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ProjectWorkflowStepReference.


        :param order: The order of this ProjectWorkflowStepReference.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def workflow_level(self):
        """Gets the workflow_level of this ProjectWorkflowStepReference.  # noqa: E501


        :return: The workflow_level of this ProjectWorkflowStepReference.  # noqa: E501
        :rtype: int
        """
        return self._workflow_level

    @workflow_level.setter
    def workflow_level(self, workflow_level):
        """Sets the workflow_level of this ProjectWorkflowStepReference.


        :param workflow_level: The workflow_level of this ProjectWorkflowStepReference.  # noqa: E501
        :type: int
        """

        self._workflow_level = workflow_level

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
        if issubclass(ProjectWorkflowStepReference, dict):
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
        if not isinstance(other, ProjectWorkflowStepReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other