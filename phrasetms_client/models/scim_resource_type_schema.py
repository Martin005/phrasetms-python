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

class ScimResourceTypeSchema(object):
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
        'schemas': 'list[str]',
        'id': 'str',
        'name': 'str',
        'endpoint': 'str',
        'description': 'str',
        'schema': 'str',
        'schema_extensions': 'list[SchemaExtension]'
    }

    attribute_map = {
        'schemas': 'schemas',
        'id': 'id',
        'name': 'name',
        'endpoint': 'endpoint',
        'description': 'description',
        'schema': 'schema',
        'schema_extensions': 'schemaExtensions'
    }

    def __init__(self, schemas=None, id=None, name=None, endpoint=None, description=None, schema=None, schema_extensions=None):  # noqa: E501
        """ScimResourceTypeSchema - a model defined in Swagger"""  # noqa: E501
        self._schemas = None
        self._id = None
        self._name = None
        self._endpoint = None
        self._description = None
        self._schema = None
        self._schema_extensions = None
        self.discriminator = None
        if schemas is not None:
            self.schemas = schemas
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if endpoint is not None:
            self.endpoint = endpoint
        if description is not None:
            self.description = description
        if schema is not None:
            self.schema = schema
        if schema_extensions is not None:
            self.schema_extensions = schema_extensions

    @property
    def schemas(self):
        """Gets the schemas of this ScimResourceTypeSchema.  # noqa: E501


        :return: The schemas of this ScimResourceTypeSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this ScimResourceTypeSchema.


        :param schemas: The schemas of this ScimResourceTypeSchema.  # noqa: E501
        :type: list[str]
        """

        self._schemas = schemas

    @property
    def id(self):
        """Gets the id of this ScimResourceTypeSchema.  # noqa: E501


        :return: The id of this ScimResourceTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScimResourceTypeSchema.


        :param id: The id of this ScimResourceTypeSchema.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ScimResourceTypeSchema.  # noqa: E501


        :return: The name of this ScimResourceTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScimResourceTypeSchema.


        :param name: The name of this ScimResourceTypeSchema.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def endpoint(self):
        """Gets the endpoint of this ScimResourceTypeSchema.  # noqa: E501


        :return: The endpoint of this ScimResourceTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ScimResourceTypeSchema.


        :param endpoint: The endpoint of this ScimResourceTypeSchema.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def description(self):
        """Gets the description of this ScimResourceTypeSchema.  # noqa: E501


        :return: The description of this ScimResourceTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScimResourceTypeSchema.


        :param description: The description of this ScimResourceTypeSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def schema(self):
        """Gets the schema of this ScimResourceTypeSchema.  # noqa: E501


        :return: The schema of this ScimResourceTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ScimResourceTypeSchema.


        :param schema: The schema of this ScimResourceTypeSchema.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def schema_extensions(self):
        """Gets the schema_extensions of this ScimResourceTypeSchema.  # noqa: E501


        :return: The schema_extensions of this ScimResourceTypeSchema.  # noqa: E501
        :rtype: list[SchemaExtension]
        """
        return self._schema_extensions

    @schema_extensions.setter
    def schema_extensions(self, schema_extensions):
        """Sets the schema_extensions of this ScimResourceTypeSchema.


        :param schema_extensions: The schema_extensions of this ScimResourceTypeSchema.  # noqa: E501
        :type: list[SchemaExtension]
        """

        self._schema_extensions = schema_extensions

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
        if issubclass(ScimResourceTypeSchema, dict):
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
        if not isinstance(other, ScimResourceTypeSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other