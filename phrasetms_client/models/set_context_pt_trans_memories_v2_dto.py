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
from phrasetms_client.models.set_project_template_trans_memory_v2_dto import SetProjectTemplateTransMemoryV2Dto
from phrasetms_client.models.uid_reference import UidReference

class SetContextPTTransMemoriesV2Dto(BaseModel):
    """
    SetContextPTTransMemoriesV2Dto
    """
    trans_memories: conlist(SetProjectTemplateTransMemoryV2Dto) = Field(..., alias="transMemories")
    target_lang: Optional[StrictStr] = Field(None, alias="targetLang", description="Set translation memory only for the specific project target language")
    workflow_step: Optional[UidReference] = Field(None, alias="workflowStep")
    order_enabled: Optional[StrictBool] = Field(None, alias="orderEnabled", description="Default: false")
    __properties = ["transMemories", "targetLang", "workflowStep", "orderEnabled"]

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
    def from_json(cls, json_str: str) -> SetContextPTTransMemoriesV2Dto:
        """Create an instance of SetContextPTTransMemoriesV2Dto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in trans_memories (list)
        _items = []
        if self.trans_memories:
            for _item in self.trans_memories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transMemories'] = _items
        # override the default output from pydantic by calling `to_dict()` of workflow_step
        if self.workflow_step:
            _dict['workflowStep'] = self.workflow_step.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SetContextPTTransMemoriesV2Dto:
        """Create an instance of SetContextPTTransMemoriesV2Dto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SetContextPTTransMemoriesV2Dto.parse_obj(obj)

        _obj = SetContextPTTransMemoriesV2Dto.parse_obj({
            "trans_memories": [SetProjectTemplateTransMemoryV2Dto.from_dict(_item) for _item in obj.get("transMemories")] if obj.get("transMemories") is not None else None,
            "target_lang": obj.get("targetLang"),
            "workflow_step": UidReference.from_dict(obj.get("workflowStep")) if obj.get("workflowStep") is not None else None,
            "order_enabled": obj.get("orderEnabled")
        })
        return _obj

