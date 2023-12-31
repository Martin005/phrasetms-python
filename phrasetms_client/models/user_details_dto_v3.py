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
import phrasetms_client.models

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator
from phrasetms_client.models.user_reference import UserReference

class UserDetailsDtoV3(BaseModel):
    """
    User with all belonging objects
    """
    uid: constr(strict=True, max_length=255, min_length=0) = Field(...)
    user_name: constr(strict=True, max_length=255, min_length=0) = Field(..., alias="userName")
    first_name: constr(strict=True, max_length=255, min_length=0) = Field(..., alias="firstName")
    last_name: constr(strict=True, max_length=255, min_length=0) = Field(..., alias="lastName")
    email: constr(strict=True, max_length=255, min_length=0) = Field(...)
    date_created: Optional[datetime] = Field(None, alias="dateCreated")
    date_deleted: Optional[datetime] = Field(None, alias="dateDeleted")
    created_by: Optional[UserReference] = Field(None, alias="createdBy")
    role: StrictStr = Field(..., description="Enum: \"ADMIN\", \"PROJECT_MANAGER\", \"LINGUIST\", \"GUEST\", \"SUBMITTER\"")
    timezone: constr(strict=True, max_length=255, min_length=0) = Field(...)
    note: Optional[constr(strict=True, max_length=4096, min_length=0)] = None
    receive_newsletter: Optional[StrictBool] = Field(None, alias="receiveNewsletter")
    active: Optional[StrictBool] = None
    pending_email_change: Optional[StrictBool] = Field(None, alias="pendingEmailChange", description="If user has email change pending (new email not verified)")
    __properties = ["uid", "userName", "firstName", "lastName", "email", "dateCreated", "dateDeleted", "createdBy", "role", "timezone", "note", "receiveNewsletter", "active", "pendingEmailChange"]

    @validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('SYS_ADMIN', 'SYS_ADMIN_READ', 'ADMIN', 'PROJECT_MANAGER', 'LINGUIST', 'GUEST', 'SUBMITTER'):
            raise ValueError("must be one of enum values ('SYS_ADMIN', 'SYS_ADMIN_READ', 'ADMIN', 'PROJECT_MANAGER', 'LINGUIST', 'GUEST', 'SUBMITTER')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = 'role'

    # discriminator mappings
    __discriminator_value_class_map = {
        'ADMIN_RESPONSE': 'ADMINRESPONSE',
        'GUEST_RESPONSE': 'GUESTRESPONSE',
        'LINGUIST_RESPONSE': 'LINGUISTRESPONSE',
        'PROJECT_MANAGER_RESPONSE': 'PROJECTMANAGERRESPONSE',
        'SUBMITTER_RESPONSE': 'SUBMITTERRESPONSE'
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union(ADMINRESPONSE, GUESTRESPONSE, LINGUISTRESPONSE, PROJECTMANAGERRESPONSE, SUBMITTERRESPONSE):  # noqa: F821
        """Create an instance of UserDetailsDtoV3 from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(ADMINRESPONSE, GUESTRESPONSE, LINGUISTRESPONSE, PROJECTMANAGERRESPONSE, SUBMITTERRESPONSE):  # noqa: F821
        """Create an instance of UserDetailsDtoV3 from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = getattr(phrasetms_client.models, object_type)
            return klass.from_dict(obj)
        else:
            raise ValueError("UserDetailsDtoV3 failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

