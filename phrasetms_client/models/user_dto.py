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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from phrasetms_client.models.discount_scheme_reference import DiscountSchemeReference
from phrasetms_client.models.price_list_reference import PriceListReference
from phrasetms_client.models.user_reference import UserReference

class UserDto(BaseModel):
    """
    UserDto
    """
    id: Optional[StrictStr] = None
    uid: Optional[StrictStr] = None
    user_name: Optional[StrictStr] = Field(None, alias="userName")
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    email: Optional[StrictStr] = None
    date_created: Optional[datetime] = Field(None, alias="dateCreated")
    date_deleted: Optional[datetime] = Field(None, alias="dateDeleted")
    created_by: Optional[UserReference] = Field(None, alias="createdBy")
    role: Optional[StrictStr] = None
    timezone: Optional[StrictStr] = None
    note: Optional[StrictStr] = None
    terminologist: Optional[StrictBool] = None
    source_langs: Optional[conlist(StrictStr)] = Field(None, alias="sourceLangs")
    target_langs: Optional[conlist(StrictStr)] = Field(None, alias="targetLangs")
    active: Optional[StrictBool] = None
    price_list: Optional[PriceListReference] = Field(None, alias="priceList")
    net_rate_scheme: Optional[DiscountSchemeReference] = Field(None, alias="netRateScheme")
    __properties = ["id", "uid", "userName", "firstName", "lastName", "email", "dateCreated", "dateDeleted", "createdBy", "role", "timezone", "note", "terminologist", "sourceLangs", "targetLangs", "active", "priceList", "netRateScheme"]

    @validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SYS_ADMIN', 'SYS_ADMIN_READ', 'ADMIN', 'PROJECT_MANAGER', 'LINGUIST', 'GUEST', 'SUBMITTER'):
            raise ValueError("must be one of enum values ('SYS_ADMIN', 'SYS_ADMIN_READ', 'ADMIN', 'PROJECT_MANAGER', 'LINGUIST', 'GUEST', 'SUBMITTER')")
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
    def from_json(cls, json_str: str) -> UserDto:
        """Create an instance of UserDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price_list
        if self.price_list:
            _dict['priceList'] = self.price_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of net_rate_scheme
        if self.net_rate_scheme:
            _dict['netRateScheme'] = self.net_rate_scheme.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserDto:
        """Create an instance of UserDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserDto.parse_obj(obj)

        _obj = UserDto.parse_obj({
            "id": obj.get("id"),
            "uid": obj.get("uid"),
            "user_name": obj.get("userName"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "email": obj.get("email"),
            "date_created": obj.get("dateCreated"),
            "date_deleted": obj.get("dateDeleted"),
            "created_by": UserReference.from_dict(obj.get("createdBy")) if obj.get("createdBy") is not None else None,
            "role": obj.get("role"),
            "timezone": obj.get("timezone"),
            "note": obj.get("note"),
            "terminologist": obj.get("terminologist"),
            "source_langs": obj.get("sourceLangs"),
            "target_langs": obj.get("targetLangs"),
            "active": obj.get("active"),
            "price_list": PriceListReference.from_dict(obj.get("priceList")) if obj.get("priceList") is not None else None,
            "net_rate_scheme": DiscountSchemeReference.from_dict(obj.get("netRateScheme")) if obj.get("netRateScheme") is not None else None
        })
        return _obj

