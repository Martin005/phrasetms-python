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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from phrasetms_client.models.workflow_step_reference import WorkflowStepReference

class JobPartUpdateSourceDto(BaseModel):
    """
    JobPartUpdateSourceDto
    """
    uid: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    target_lang: Optional[StrictStr] = Field(None, alias="targetLang")
    filename: Optional[StrictStr] = None
    workflow_level: Optional[StrictInt] = Field(None, alias="workflowLevel")
    workflow_step: Optional[WorkflowStepReference] = Field(None, alias="workflowStep")
    __properties = ["uid", "status", "targetLang", "filename", "workflowLevel", "workflowStep"]

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
    def from_json(cls, json_str: str) -> JobPartUpdateSourceDto:
        """Create an instance of JobPartUpdateSourceDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of workflow_step
        if self.workflow_step:
            _dict['workflowStep'] = self.workflow_step.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobPartUpdateSourceDto:
        """Create an instance of JobPartUpdateSourceDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobPartUpdateSourceDto.parse_obj(obj)

        _obj = JobPartUpdateSourceDto.parse_obj({
            "uid": obj.get("uid"),
            "status": obj.get("status"),
            "target_lang": obj.get("targetLang"),
            "filename": obj.get("filename"),
            "workflow_level": obj.get("workflowLevel"),
            "workflow_step": WorkflowStepReference.from_dict(obj.get("workflowStep")) if obj.get("workflowStep") is not None else None
        })
        return _obj

