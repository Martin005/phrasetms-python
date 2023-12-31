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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from phrasetms_client.models.assignment_per_target_lang_dto import AssignmentPerTargetLangDto
from phrasetms_client.models.business_unit_reference import BusinessUnitReference
from phrasetms_client.models.client_reference import ClientReference
from phrasetms_client.models.domain_reference import DomainReference
from phrasetms_client.models.project_template_notify_provider_dto import ProjectTemplateNotifyProviderDto
from phrasetms_client.models.sub_domain_reference import SubDomainReference
from phrasetms_client.models.uid_reference import UidReference
from phrasetms_client.models.user_reference import UserReference
from phrasetms_client.models.vendor_reference import VendorReference
from phrasetms_client.models.workflow_step_dto import WorkflowStepDto
from phrasetms_client.models.workflow_step_settings_dto import WorkflowStepSettingsDto

class ProjectTemplateDto(BaseModel):
    """
    ProjectTemplateDto
    """
    id: Optional[StrictStr] = None
    uid: Optional[StrictStr] = None
    template_name: Optional[StrictStr] = Field(None, alias="templateName")
    name: Optional[StrictStr] = None
    source_lang: Optional[StrictStr] = Field(None, alias="sourceLang")
    target_langs: Optional[conlist(StrictStr)] = Field(None, alias="targetLangs")
    note: Optional[StrictStr] = None
    use_dynamic_title: Optional[StrictBool] = Field(None, alias="useDynamicTitle")
    dynamic_title: Optional[StrictStr] = Field(None, alias="dynamicTitle")
    owner: Optional[UserReference] = None
    client: Optional[ClientReference] = None
    domain: Optional[DomainReference] = None
    sub_domain: Optional[SubDomainReference] = Field(None, alias="subDomain")
    vendor: Optional[VendorReference] = None
    created_by: Optional[UserReference] = Field(None, alias="createdBy")
    date_created: Optional[datetime] = Field(None, alias="dateCreated")
    modified_by: Optional[UserReference] = Field(None, alias="modifiedBy")
    date_modified: Optional[datetime] = Field(None, alias="dateModified", description="Deprecated - use dateTimeModified field instead")
    date_time_modified: Optional[datetime] = Field(None, alias="dateTimeModified")
    workflow_steps: Optional[conlist(WorkflowStepDto)] = Field(None, alias="workflowSteps")
    workflow_settings: Optional[conlist(WorkflowStepSettingsDto)] = Field(None, alias="workflowSettings")
    business_unit: Optional[BusinessUnitReference] = Field(None, alias="businessUnit")
    notify_providers: Optional[ProjectTemplateNotifyProviderDto] = Field(None, alias="notifyProviders")
    assigned_to: Optional[conlist(AssignmentPerTargetLangDto)] = Field(None, alias="assignedTo")
    import_settings: Optional[UidReference] = Field(None, alias="importSettings")
    __properties = ["id", "uid", "templateName", "name", "sourceLang", "targetLangs", "note", "useDynamicTitle", "dynamicTitle", "owner", "client", "domain", "subDomain", "vendor", "createdBy", "dateCreated", "modifiedBy", "dateModified", "dateTimeModified", "workflowSteps", "workflowSettings", "businessUnit", "notifyProviders", "assignedTo", "importSettings"]

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
    def from_json(cls, json_str: str) -> ProjectTemplateDto:
        """Create an instance of ProjectTemplateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client
        if self.client:
            _dict['client'] = self.client.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain
        if self.domain:
            _dict['domain'] = self.domain.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_domain
        if self.sub_domain:
            _dict['subDomain'] = self.sub_domain.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vendor
        if self.vendor:
            _dict['vendor'] = self.vendor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_by
        if self.modified_by:
            _dict['modifiedBy'] = self.modified_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in workflow_steps (list)
        _items = []
        if self.workflow_steps:
            for _item in self.workflow_steps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['workflowSteps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in workflow_settings (list)
        _items = []
        if self.workflow_settings:
            for _item in self.workflow_settings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['workflowSettings'] = _items
        # override the default output from pydantic by calling `to_dict()` of business_unit
        if self.business_unit:
            _dict['businessUnit'] = self.business_unit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notify_providers
        if self.notify_providers:
            _dict['notifyProviders'] = self.notify_providers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in assigned_to (list)
        _items = []
        if self.assigned_to:
            for _item in self.assigned_to:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assignedTo'] = _items
        # override the default output from pydantic by calling `to_dict()` of import_settings
        if self.import_settings:
            _dict['importSettings'] = self.import_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProjectTemplateDto:
        """Create an instance of ProjectTemplateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProjectTemplateDto.parse_obj(obj)

        _obj = ProjectTemplateDto.parse_obj({
            "id": obj.get("id"),
            "uid": obj.get("uid"),
            "template_name": obj.get("templateName"),
            "name": obj.get("name"),
            "source_lang": obj.get("sourceLang"),
            "target_langs": obj.get("targetLangs"),
            "note": obj.get("note"),
            "use_dynamic_title": obj.get("useDynamicTitle"),
            "dynamic_title": obj.get("dynamicTitle"),
            "owner": UserReference.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "client": ClientReference.from_dict(obj.get("client")) if obj.get("client") is not None else None,
            "domain": DomainReference.from_dict(obj.get("domain")) if obj.get("domain") is not None else None,
            "sub_domain": SubDomainReference.from_dict(obj.get("subDomain")) if obj.get("subDomain") is not None else None,
            "vendor": VendorReference.from_dict(obj.get("vendor")) if obj.get("vendor") is not None else None,
            "created_by": UserReference.from_dict(obj.get("createdBy")) if obj.get("createdBy") is not None else None,
            "date_created": obj.get("dateCreated"),
            "modified_by": UserReference.from_dict(obj.get("modifiedBy")) if obj.get("modifiedBy") is not None else None,
            "date_modified": obj.get("dateModified"),
            "date_time_modified": obj.get("dateTimeModified"),
            "workflow_steps": [WorkflowStepDto.from_dict(_item) for _item in obj.get("workflowSteps")] if obj.get("workflowSteps") is not None else None,
            "workflow_settings": [WorkflowStepSettingsDto.from_dict(_item) for _item in obj.get("workflowSettings")] if obj.get("workflowSettings") is not None else None,
            "business_unit": BusinessUnitReference.from_dict(obj.get("businessUnit")) if obj.get("businessUnit") is not None else None,
            "notify_providers": ProjectTemplateNotifyProviderDto.from_dict(obj.get("notifyProviders")) if obj.get("notifyProviders") is not None else None,
            "assigned_to": [AssignmentPerTargetLangDto.from_dict(_item) for _item in obj.get("assignedTo")] if obj.get("assignedTo") is not None else None,
            "import_settings": UidReference.from_dict(obj.get("importSettings")) if obj.get("importSettings") is not None else None
        })
        return _obj

