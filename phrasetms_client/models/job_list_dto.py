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
from phrasetms_client.models.async_request_reference import AsyncRequestReference
from phrasetms_client.models.job_part_reference import JobPartReference

class JobListDto(BaseModel):
    """
    JobListDto
    """
    unsupported_files: Optional[conlist(StrictStr)] = Field(None, alias="unsupportedFiles")
    jobs: Optional[conlist(JobPartReference)] = None
    async_request: Optional[AsyncRequestReference] = Field(None, alias="asyncRequest")
    __properties = ["unsupportedFiles", "jobs", "asyncRequest"]

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
    def from_json(cls, json_str: str) -> JobListDto:
        """Create an instance of JobListDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in jobs (list)
        _items = []
        if self.jobs:
            for _item in self.jobs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['jobs'] = _items
        # override the default output from pydantic by calling `to_dict()` of async_request
        if self.async_request:
            _dict['asyncRequest'] = self.async_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobListDto:
        """Create an instance of JobListDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobListDto.parse_obj(obj)

        _obj = JobListDto.parse_obj({
            "unsupported_files": obj.get("unsupportedFiles"),
            "jobs": [JobPartReference.from_dict(_item) for _item in obj.get("jobs")] if obj.get("jobs") is not None else None,
            "async_request": AsyncRequestReference.from_dict(obj.get("asyncRequest")) if obj.get("asyncRequest") is not None else None
        })
        return _obj

