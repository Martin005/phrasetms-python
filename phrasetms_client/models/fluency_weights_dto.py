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
from pydantic import BaseModel, Field
from phrasetms_client.models.toggleable_weight_dto import ToggleableWeightDto

class FluencyWeightsDto(BaseModel):
    """
    FluencyWeightsDto
    """
    fluency: Optional[ToggleableWeightDto] = None
    punctuation: Optional[ToggleableWeightDto] = None
    spelling: Optional[ToggleableWeightDto] = None
    grammar: Optional[ToggleableWeightDto] = None
    grammatical_register: Optional[ToggleableWeightDto] = Field(None, alias="grammaticalRegister")
    inconsistency: Optional[ToggleableWeightDto] = None
    cross_reference: Optional[ToggleableWeightDto] = Field(None, alias="crossReference")
    character_encoding: Optional[ToggleableWeightDto] = Field(None, alias="characterEncoding")
    __properties = ["fluency", "punctuation", "spelling", "grammar", "grammaticalRegister", "inconsistency", "crossReference", "characterEncoding"]

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
    def from_json(cls, json_str: str) -> FluencyWeightsDto:
        """Create an instance of FluencyWeightsDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of fluency
        if self.fluency:
            _dict['fluency'] = self.fluency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of punctuation
        if self.punctuation:
            _dict['punctuation'] = self.punctuation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spelling
        if self.spelling:
            _dict['spelling'] = self.spelling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of grammar
        if self.grammar:
            _dict['grammar'] = self.grammar.to_dict()
        # override the default output from pydantic by calling `to_dict()` of grammatical_register
        if self.grammatical_register:
            _dict['grammaticalRegister'] = self.grammatical_register.to_dict()
        # override the default output from pydantic by calling `to_dict()` of inconsistency
        if self.inconsistency:
            _dict['inconsistency'] = self.inconsistency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cross_reference
        if self.cross_reference:
            _dict['crossReference'] = self.cross_reference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of character_encoding
        if self.character_encoding:
            _dict['characterEncoding'] = self.character_encoding.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FluencyWeightsDto:
        """Create an instance of FluencyWeightsDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FluencyWeightsDto.parse_obj(obj)

        _obj = FluencyWeightsDto.parse_obj({
            "fluency": ToggleableWeightDto.from_dict(obj.get("fluency")) if obj.get("fluency") is not None else None,
            "punctuation": ToggleableWeightDto.from_dict(obj.get("punctuation")) if obj.get("punctuation") is not None else None,
            "spelling": ToggleableWeightDto.from_dict(obj.get("spelling")) if obj.get("spelling") is not None else None,
            "grammar": ToggleableWeightDto.from_dict(obj.get("grammar")) if obj.get("grammar") is not None else None,
            "grammatical_register": ToggleableWeightDto.from_dict(obj.get("grammaticalRegister")) if obj.get("grammaticalRegister") is not None else None,
            "inconsistency": ToggleableWeightDto.from_dict(obj.get("inconsistency")) if obj.get("inconsistency") is not None else None,
            "cross_reference": ToggleableWeightDto.from_dict(obj.get("crossReference")) if obj.get("crossReference") is not None else None,
            "character_encoding": ToggleableWeightDto.from_dict(obj.get("characterEncoding")) if obj.get("characterEncoding") is not None else None
        })
        return _obj

