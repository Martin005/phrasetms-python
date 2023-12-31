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
from pydantic import BaseModel, Field, StrictStr, conlist
from phrasetms_client.models.term_base_dto import TermBaseDto
from phrasetms_client.models.term_dto import TermDto

class SearchResponseTbDto(BaseModel):
    """
    SearchResponseTbDto
    """
    term_base: Optional[TermBaseDto] = Field(None, alias="termBase")
    concept_id: Optional[StrictStr] = Field(None, alias="conceptId")
    source_term: Optional[TermDto] = Field(None, alias="sourceTerm")
    translation_terms: Optional[conlist(TermDto)] = Field(None, alias="translationTerms")
    __properties = ["termBase", "conceptId", "sourceTerm", "translationTerms"]

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
    def from_json(cls, json_str: str) -> SearchResponseTbDto:
        """Create an instance of SearchResponseTbDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of term_base
        if self.term_base:
            _dict['termBase'] = self.term_base.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_term
        if self.source_term:
            _dict['sourceTerm'] = self.source_term.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in translation_terms (list)
        _items = []
        if self.translation_terms:
            for _item in self.translation_terms:
                if _item:
                    _items.append(_item.to_dict())
            _dict['translationTerms'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchResponseTbDto:
        """Create an instance of SearchResponseTbDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchResponseTbDto.parse_obj(obj)

        _obj = SearchResponseTbDto.parse_obj({
            "term_base": TermBaseDto.from_dict(obj.get("termBase")) if obj.get("termBase") is not None else None,
            "concept_id": obj.get("conceptId"),
            "source_term": TermDto.from_dict(obj.get("sourceTerm")) if obj.get("sourceTerm") is not None else None,
            "translation_terms": [TermDto.from_dict(_item) for _item in obj.get("translationTerms")] if obj.get("translationTerms") is not None else None
        })
        return _obj

