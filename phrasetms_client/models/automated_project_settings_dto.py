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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from phrasetms_client.models.name_dto import NameDto

class AutomatedProjectSettingsDto(BaseModel):
    """
    AutomatedProjectSettingsDto
    """
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    organization: Optional[NameDto] = None
    active: Optional[StrictBool] = None
    source_lang: Optional[StrictStr] = Field(None, alias="sourceLang")
    target_langs: Optional[conlist(StrictStr, unique_items=True)] = Field(None, alias="targetLangs")
    connector: Optional[NameDto] = None
    remote_folder: Optional[StrictStr] = Field(None, alias="remoteFolder")
    __properties = ["id", "name", "organization", "active", "sourceLang", "targetLangs", "connector", "remoteFolder"]

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
    def from_json(cls, json_str: str) -> AutomatedProjectSettingsDto:
        """Create an instance of AutomatedProjectSettingsDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connector
        if self.connector:
            _dict['connector'] = self.connector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AutomatedProjectSettingsDto:
        """Create an instance of AutomatedProjectSettingsDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AutomatedProjectSettingsDto.parse_obj(obj)

        _obj = AutomatedProjectSettingsDto.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "organization": NameDto.from_dict(obj.get("organization")) if obj.get("organization") is not None else None,
            "active": obj.get("active"),
            "source_lang": obj.get("sourceLang"),
            "target_langs": obj.get("targetLangs"),
            "connector": NameDto.from_dict(obj.get("connector")) if obj.get("connector") is not None else None,
            "remote_folder": obj.get("remoteFolder")
        })
        return _obj

