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
from pydantic import BaseModel, Field, conlist
from phrasetms_client.models.search_tm_response_dto_v3 import SearchTMResponseDtoV3

class SearchResponseListTmDtoV3(BaseModel):
    """
    SearchResponseListTmDtoV3
    """
    search_results: Optional[conlist(SearchTMResponseDtoV3)] = Field(None, alias="searchResults")
    __properties = ["searchResults"]

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
    def from_json(cls, json_str: str) -> SearchResponseListTmDtoV3:
        """Create an instance of SearchResponseListTmDtoV3 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in search_results (list)
        _items = []
        if self.search_results:
            for _item in self.search_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['searchResults'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchResponseListTmDtoV3:
        """Create an instance of SearchResponseListTmDtoV3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SearchResponseListTmDtoV3.parse_obj(obj)

        _obj = SearchResponseListTmDtoV3.parse_obj({
            "search_results": [SearchTMResponseDtoV3.from_dict(_item) for _item in obj.get("searchResults")] if obj.get("searchResults") is not None else None
        })
        return _obj

