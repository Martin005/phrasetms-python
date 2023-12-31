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
from pydantic import BaseModel, Field, StrictBool, constr
from phrasetms_client.models.uid_reference import UidReference

class ProjectTemplateCreateActionDto(BaseModel):
    """
    ProjectTemplateCreateActionDto
    """
    project: UidReference = Field(...)
    name: constr(strict=True, max_length=255, min_length=0) = Field(...)
    import_settings: Optional[UidReference] = Field(None, alias="importSettings")
    use_dynamic_title: Optional[StrictBool] = Field(None, alias="useDynamicTitle")
    dynamic_title: Optional[constr(strict=True, max_length=255, min_length=0)] = Field(None, alias="dynamicTitle")
    __properties = ["project", "name", "importSettings", "useDynamicTitle", "dynamicTitle"]

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
    def from_json(cls, json_str: str) -> ProjectTemplateCreateActionDto:
        """Create an instance of ProjectTemplateCreateActionDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of import_settings
        if self.import_settings:
            _dict['importSettings'] = self.import_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProjectTemplateCreateActionDto:
        """Create an instance of ProjectTemplateCreateActionDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProjectTemplateCreateActionDto.parse_obj(obj)

        _obj = ProjectTemplateCreateActionDto.parse_obj({
            "project": UidReference.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "name": obj.get("name"),
            "import_settings": UidReference.from_dict(obj.get("importSettings")) if obj.get("importSettings") is not None else None,
            "use_dynamic_title": obj.get("useDynamicTitle"),
            "dynamic_title": obj.get("dynamicTitle")
        })
        return _obj

