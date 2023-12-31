# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
import phrasetms_client.models

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from phrasetms_client.models.comment_dto import CommentDto
from phrasetms_client.models.mentionable_user_dto import MentionableUserDto
from phrasetms_client.models.status_dto import StatusDto

class CommonConversationDto(BaseModel):
    """
    CommonConversationDto
    """
    id: Optional[StrictStr] = None
    type: Optional[StrictStr] = Field(None, description="Field references differs based on the Conversation Type.")
    date_created: Optional[datetime] = Field(None, alias="dateCreated")
    date_modified: Optional[datetime] = Field(None, alias="dateModified")
    date_edited: Optional[datetime] = Field(None, alias="dateEdited")
    created_by: Optional[MentionableUserDto] = Field(None, alias="createdBy")
    comments: Optional[conlist(CommentDto)] = None
    status: Optional[StatusDto] = None
    deleted: Optional[StrictBool] = None
    __properties = ["id", "type", "dateCreated", "dateModified", "dateEdited", "createdBy", "comments", "status", "deleted"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = 'type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'LQA': 'LQA',
        'SEGMENT_TARGET': 'SEGMENTTARGET'
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union(LQA, SEGMENTTARGET):  # noqa: F821
        """Create an instance of CommonConversationDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in comments (list)
        _items = []
        if self.comments:
            for _item in self.comments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['comments'] = _items
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(LQA, SEGMENTTARGET):  # noqa: F821
        """Create an instance of CommonConversationDto from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = getattr(phrasetms_client.models, object_type)
            return klass.from_dict(obj)
        else:
            raise ValueError("CommonConversationDto failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

