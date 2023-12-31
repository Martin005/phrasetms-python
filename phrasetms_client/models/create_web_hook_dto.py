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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator

class CreateWebHookDto(BaseModel):
    """
    CreateWebHookDto
    """
    name: Optional[constr(strict=True, max_length=255, min_length=0)] = None
    url: StrictStr = Field(...)
    events: conlist(StrictStr) = Field(...)
    secret_token: Optional[constr(strict=True, max_length=255, min_length=0)] = Field(None, alias="secretToken")
    hidden: Optional[StrictBool] = Field(None, description="Default: false")
    status: Optional[StrictStr] = Field(None, description="Default: ENABLED")
    __properties = ["name", "url", "events", "secretToken", "hidden", "status"]

    @validator('events')
    def events_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in ('JOB_STATUS_CHANGED', 'JOB_CREATED', 'JOB_DELETED', 'JOB_ASSIGNED', 'JOB_DUE_DATE_CHANGED', 'JOB_UPDATED', 'JOB_TARGET_UPDATED', 'JOB_EXPORTED', 'JOB_UNEXPORTED', 'PROJECT_CREATED', 'PROJECT_DELETED', 'PROJECT_STATUS_CHANGED', 'PROJECT_DUE_DATE_CHANGED', 'SHARED_PROJECT_ASSIGNED', 'PROJECT_METADATA_UPDATED', 'PRE_TRANSLATION_FINISHED', 'ANALYSIS_CREATED', 'CONTINUOUS_JOB_UPDATED', 'PROJECT_TEMPLATE_CREATED', 'PROJECT_TEMPLATE_UPDATED', 'PROJECT_TEMPLATE_DELETED'):
                raise ValueError("each list item must be one of ('JOB_STATUS_CHANGED', 'JOB_CREATED', 'JOB_DELETED', 'JOB_ASSIGNED', 'JOB_DUE_DATE_CHANGED', 'JOB_UPDATED', 'JOB_TARGET_UPDATED', 'JOB_EXPORTED', 'JOB_UNEXPORTED', 'PROJECT_CREATED', 'PROJECT_DELETED', 'PROJECT_STATUS_CHANGED', 'PROJECT_DUE_DATE_CHANGED', 'SHARED_PROJECT_ASSIGNED', 'PROJECT_METADATA_UPDATED', 'PRE_TRANSLATION_FINISHED', 'ANALYSIS_CREATED', 'CONTINUOUS_JOB_UPDATED', 'PROJECT_TEMPLATE_CREATED', 'PROJECT_TEMPLATE_UPDATED', 'PROJECT_TEMPLATE_DELETED')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ENABLED', 'DISABLED'):
            raise ValueError("must be one of enum values ('ENABLED', 'DISABLED')")
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
    def from_json(cls, json_str: str) -> CreateWebHookDto:
        """Create an instance of CreateWebHookDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateWebHookDto:
        """Create an instance of CreateWebHookDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateWebHookDto.parse_obj(obj)

        _obj = CreateWebHookDto.parse_obj({
            "name": obj.get("name"),
            "url": obj.get("url"),
            "events": obj.get("events"),
            "secret_token": obj.get("secretToken"),
            "hidden": obj.get("hidden"),
            "status": obj.get("status")
        })
        return _obj

