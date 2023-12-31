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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from phrasetms_client.models.user_reference import UserReference

class JobPartStatusChangeDto(BaseModel):
    """
    JobPartStatusChangeDto
    """
    status: Optional[StrictStr] = None
    changed_date: Optional[datetime] = Field(None, alias="changedDate")
    changed_by: Optional[UserReference] = Field(None, alias="changedBy")
    __properties = ["status", "changedDate", "changedBy"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NEW', 'ACCEPTED', 'DECLINED', 'REJECTED', 'DELIVERED', 'EMAILED', 'COMPLETED', 'CANCELLED'):
            raise ValueError("must be one of enum values ('NEW', 'ACCEPTED', 'DECLINED', 'REJECTED', 'DELIVERED', 'EMAILED', 'COMPLETED', 'CANCELLED')")
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
    def from_json(cls, json_str: str) -> JobPartStatusChangeDto:
        """Create an instance of JobPartStatusChangeDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of changed_by
        if self.changed_by:
            _dict['changedBy'] = self.changed_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobPartStatusChangeDto:
        """Create an instance of JobPartStatusChangeDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobPartStatusChangeDto.parse_obj(obj)

        _obj = JobPartStatusChangeDto.parse_obj({
            "status": obj.get("status"),
            "changed_date": obj.get("changedDate"),
            "changed_by": UserReference.from_dict(obj.get("changedBy")) if obj.get("changedBy") is not None else None
        })
        return _obj

