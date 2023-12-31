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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class MultilingualXlsSettingsDto(BaseModel):
    """
    MultilingualXlsSettingsDto
    """
    source_column: Optional[StrictStr] = Field(None, alias="sourceColumn")
    target_columns: Optional[Dict[str, StrictStr]] = Field(None, alias="targetColumns", description="Format: \"language\":\"column\"; example: {\"en\": \"A\", \"sk\": \"B\"}")
    context_note_column: Optional[StrictStr] = Field(None, alias="contextNoteColumn")
    context_key_column: Optional[StrictStr] = Field(None, alias="contextKeyColumn")
    tag_regexp: Optional[StrictStr] = Field(None, alias="tagRegexp")
    html_sub_filter: Optional[StrictBool] = Field(None, alias="htmlSubFilter", description="Default: false")
    segmentation: Optional[StrictBool] = Field(None, description="Default: true")
    import_rows: Optional[StrictStr] = Field(None, alias="importRows")
    max_len_column: Optional[StrictStr] = Field(None, alias="maxLenColumn")
    non_empty_segment_action: Optional[StrictStr] = Field(None, alias="nonEmptySegmentAction")
    save_confirmed_segments_to_tm: Optional[StrictBool] = Field(None, alias="saveConfirmedSegmentsToTm")
    __properties = ["sourceColumn", "targetColumns", "contextNoteColumn", "contextKeyColumn", "tagRegexp", "htmlSubFilter", "segmentation", "importRows", "maxLenColumn", "nonEmptySegmentAction", "saveConfirmedSegmentsToTm"]

    @validator('non_empty_segment_action')
    def non_empty_segment_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NONE', 'CONFIRM', 'LOCK', 'CONFIRM_LOCK'):
            raise ValueError("must be one of enum values ('NONE', 'CONFIRM', 'LOCK', 'CONFIRM_LOCK')")
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
    def from_json(cls, json_str: str) -> MultilingualXlsSettingsDto:
        """Create an instance of MultilingualXlsSettingsDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MultilingualXlsSettingsDto:
        """Create an instance of MultilingualXlsSettingsDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MultilingualXlsSettingsDto.parse_obj(obj)

        _obj = MultilingualXlsSettingsDto.parse_obj({
            "source_column": obj.get("sourceColumn"),
            "target_columns": obj.get("targetColumns"),
            "context_note_column": obj.get("contextNoteColumn"),
            "context_key_column": obj.get("contextKeyColumn"),
            "tag_regexp": obj.get("tagRegexp"),
            "html_sub_filter": obj.get("htmlSubFilter"),
            "segmentation": obj.get("segmentation"),
            "import_rows": obj.get("importRows"),
            "max_len_column": obj.get("maxLenColumn"),
            "non_empty_segment_action": obj.get("nonEmptySegmentAction"),
            "save_confirmed_segments_to_tm": obj.get("saveConfirmedSegmentsToTm")
        })
        return _obj

