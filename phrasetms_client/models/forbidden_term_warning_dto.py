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
from phrasetms_client.models.segment_warning import SegmentWarning  # noqa: F401,E501

class ForbiddenTermWarningDto(SegmentWarning):
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
        'term': 'str',
        'positions': 'list[Position]',
        'source_terms': 'list[Term]'
    }
    if hasattr(SegmentWarning, "swagger_types"):
        swagger_types.update(SegmentWarning.swagger_types)

    attribute_map = {
        'term': 'term',
        'positions': 'positions',
        'source_terms': 'sourceTerms'
    }
    if hasattr(SegmentWarning, "attribute_map"):
        attribute_map.update(SegmentWarning.attribute_map)

    def __init__(self, term=None, positions=None, source_terms=None, *args, **kwargs):  # noqa: E501
        """ForbiddenTermWarningDto - a model defined in Swagger"""  # noqa: E501
        self._term = None
        self._positions = None
        self._source_terms = None
        self.discriminator = None
        if term is not None:
            self.term = term
        if positions is not None:
            self.positions = positions
        if source_terms is not None:
            self.source_terms = source_terms
        SegmentWarning.__init__(self, *args, **kwargs)

    @property
    def term(self):
        """Gets the term of this ForbiddenTermWarningDto.  # noqa: E501


        :return: The term of this ForbiddenTermWarningDto.  # noqa: E501
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this ForbiddenTermWarningDto.


        :param term: The term of this ForbiddenTermWarningDto.  # noqa: E501
        :type: str
        """

        self._term = term

    @property
    def positions(self):
        """Gets the positions of this ForbiddenTermWarningDto.  # noqa: E501


        :return: The positions of this ForbiddenTermWarningDto.  # noqa: E501
        :rtype: list[Position]
        """
        return self._positions

    @positions.setter
    def positions(self, positions):
        """Sets the positions of this ForbiddenTermWarningDto.


        :param positions: The positions of this ForbiddenTermWarningDto.  # noqa: E501
        :type: list[Position]
        """

        self._positions = positions

    @property
    def source_terms(self):
        """Gets the source_terms of this ForbiddenTermWarningDto.  # noqa: E501


        :return: The source_terms of this ForbiddenTermWarningDto.  # noqa: E501
        :rtype: list[Term]
        """
        return self._source_terms

    @source_terms.setter
    def source_terms(self, source_terms):
        """Sets the source_terms of this ForbiddenTermWarningDto.


        :param source_terms: The source_terms of this ForbiddenTermWarningDto.  # noqa: E501
        :type: list[Term]
        """

        self._source_terms = source_terms

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
        if issubclass(ForbiddenTermWarningDto, dict):
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
        if not isinstance(other, ForbiddenTermWarningDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other