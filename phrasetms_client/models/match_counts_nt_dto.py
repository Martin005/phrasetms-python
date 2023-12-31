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
from pydantic import BaseModel
from phrasetms_client.models.counts_dto import CountsDto

class MatchCountsNTDto(BaseModel):
    """
    MatchCountsNTDto
    """
    match100: Optional[CountsDto] = None
    match95: Optional[CountsDto] = None
    match85: Optional[CountsDto] = None
    match75: Optional[CountsDto] = None
    match50: Optional[CountsDto] = None
    match0: Optional[CountsDto] = None
    __properties = ["match100", "match95", "match85", "match75", "match50", "match0"]

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
    def from_json(cls, json_str: str) -> MatchCountsNTDto:
        """Create an instance of MatchCountsNTDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of match100
        if self.match100:
            _dict['match100'] = self.match100.to_dict()
        # override the default output from pydantic by calling `to_dict()` of match95
        if self.match95:
            _dict['match95'] = self.match95.to_dict()
        # override the default output from pydantic by calling `to_dict()` of match85
        if self.match85:
            _dict['match85'] = self.match85.to_dict()
        # override the default output from pydantic by calling `to_dict()` of match75
        if self.match75:
            _dict['match75'] = self.match75.to_dict()
        # override the default output from pydantic by calling `to_dict()` of match50
        if self.match50:
            _dict['match50'] = self.match50.to_dict()
        # override the default output from pydantic by calling `to_dict()` of match0
        if self.match0:
            _dict['match0'] = self.match0.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MatchCountsNTDto:
        """Create an instance of MatchCountsNTDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MatchCountsNTDto.parse_obj(obj)

        _obj = MatchCountsNTDto.parse_obj({
            "match100": CountsDto.from_dict(obj.get("match100")) if obj.get("match100") is not None else None,
            "match95": CountsDto.from_dict(obj.get("match95")) if obj.get("match95") is not None else None,
            "match85": CountsDto.from_dict(obj.get("match85")) if obj.get("match85") is not None else None,
            "match75": CountsDto.from_dict(obj.get("match75")) if obj.get("match75") is not None else None,
            "match50": CountsDto.from_dict(obj.get("match50")) if obj.get("match50") is not None else None,
            "match0": CountsDto.from_dict(obj.get("match0")) if obj.get("match0") is not None else None
        })
        return _obj

