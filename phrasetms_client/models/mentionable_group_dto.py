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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from phrasetms_client.models.uid_reference import UidReference

class MentionableGroupDto(BaseModel):
    """
    MentionableGroupDto
    """
    group_type: Optional[StrictStr] = Field(None, alias="groupType")
    group_name: Optional[StrictStr] = Field(None, alias="groupName")
    group_reference: Optional[UidReference] = Field(None, alias="groupReference")
    __properties = ["groupType", "groupName", "groupReference"]

    @validator('group_type')
    def group_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('JOB', 'OWNERS', 'PROVIDERS', 'GUESTS', 'WORKFLOW_STEP'):
            raise ValueError("must be one of enum values ('JOB', 'OWNERS', 'PROVIDERS', 'GUESTS', 'WORKFLOW_STEP')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MentionableGroupDto:
        """Create an instance of MentionableGroupDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of group_reference
        if self.group_reference:
            _dict['groupReference'] = self.group_reference.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MentionableGroupDto:
        """Create an instance of MentionableGroupDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MentionableGroupDto.parse_obj(obj)

        _obj = MentionableGroupDto.parse_obj({
            "group_type": obj.get("groupType"),
            "group_name": obj.get("groupName"),
            "group_reference": UidReference.from_dict(obj.get("groupReference")) if obj.get("groupReference") is not None else None
        })
        return _obj

