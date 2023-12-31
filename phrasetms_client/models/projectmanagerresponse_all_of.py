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
from phrasetms_client.models.business_unit_reference import BusinessUnitReference
from phrasetms_client.models.client_reference import ClientReference
from phrasetms_client.models.domain_reference import DomainReference
from phrasetms_client.models.sub_domain_reference import SubDomainReference
from phrasetms_client.models.workflow_step_reference_v3 import WorkflowStepReferenceV3

class PROJECTMANAGERRESPONSEAllOf(BaseModel):
    """
    PROJECTMANAGERRESPONSEAllOf
    """
    source_locales: Optional[conlist(StrictStr)] = Field(None, alias="sourceLocales")
    target_locales: Optional[conlist(StrictStr)] = Field(None, alias="targetLocales")
    workflow_steps: Optional[conlist(WorkflowStepReferenceV3)] = Field(None, alias="workflowSteps")
    clients: Optional[conlist(ClientReference)] = None
    domains: Optional[conlist(DomainReference)] = None
    sub_domains: Optional[conlist(SubDomainReference)] = Field(None, alias="subDomains")
    project_create: Optional[StrictBool] = Field(None, alias="projectCreate")
    project_view_other: Optional[StrictBool] = Field(None, alias="projectViewOther")
    project_edit_other: Optional[StrictBool] = Field(None, alias="projectEditOther")
    project_delete_other: Optional[StrictBool] = Field(None, alias="projectDeleteOther")
    project_clients: Optional[conlist(ClientReference)] = Field(None, alias="projectClients")
    project_business_units: Optional[conlist(BusinessUnitReference)] = Field(None, alias="projectBusinessUnits")
    project_template_create: Optional[StrictBool] = Field(None, alias="projectTemplateCreate")
    project_template_view_other: Optional[StrictBool] = Field(None, alias="projectTemplateViewOther")
    project_template_edit_other: Optional[StrictBool] = Field(None, alias="projectTemplateEditOther")
    project_template_delete_other: Optional[StrictBool] = Field(None, alias="projectTemplateDeleteOther")
    project_template_clients: Optional[conlist(ClientReference)] = Field(None, alias="projectTemplateClients")
    project_template_business_units: Optional[conlist(BusinessUnitReference)] = Field(None, alias="projectTemplateBusinessUnits")
    trans_memory_create: Optional[StrictBool] = Field(None, alias="transMemoryCreate")
    trans_memory_view_other: Optional[StrictBool] = Field(None, alias="transMemoryViewOther")
    trans_memory_edit_other: Optional[StrictBool] = Field(None, alias="transMemoryEditOther")
    trans_memory_delete_other: Optional[StrictBool] = Field(None, alias="transMemoryDeleteOther")
    trans_memory_export_other: Optional[StrictBool] = Field(None, alias="transMemoryExportOther")
    trans_memory_import_other: Optional[StrictBool] = Field(None, alias="transMemoryImportOther")
    trans_memory_clients: Optional[conlist(ClientReference)] = Field(None, alias="transMemoryClients")
    trans_memory_business_units: Optional[conlist(BusinessUnitReference)] = Field(None, alias="transMemoryBusinessUnits")
    term_base_create: Optional[StrictBool] = Field(None, alias="termBaseCreate")
    term_base_view_other: Optional[StrictBool] = Field(None, alias="termBaseViewOther")
    term_base_edit_other: Optional[StrictBool] = Field(None, alias="termBaseEditOther")
    term_base_delete_other: Optional[StrictBool] = Field(None, alias="termBaseDeleteOther")
    term_base_export_other: Optional[StrictBool] = Field(None, alias="termBaseExportOther")
    term_base_import_other: Optional[StrictBool] = Field(None, alias="termBaseImportOther")
    term_base_approve_other: Optional[StrictBool] = Field(None, alias="termBaseApproveOther")
    term_base_clients: Optional[conlist(ClientReference)] = Field(None, alias="termBaseClients")
    term_base_business_units: Optional[conlist(BusinessUnitReference)] = Field(None, alias="termBaseBusinessUnits")
    user_create: Optional[StrictBool] = Field(None, alias="userCreate")
    user_view_other: Optional[StrictBool] = Field(None, alias="userViewOther")
    user_edit_other: Optional[StrictBool] = Field(None, alias="userEditOther")
    user_delete_other: Optional[StrictBool] = Field(None, alias="userDeleteOther")
    client_domain_sub_domain_create: Optional[StrictBool] = Field(None, alias="clientDomainSubDomainCreate")
    client_domain_sub_domain_view_other: Optional[StrictBool] = Field(None, alias="clientDomainSubDomainViewOther")
    client_domain_sub_domain_edit_other: Optional[StrictBool] = Field(None, alias="clientDomainSubDomainEditOther")
    client_domain_sub_domain_delete_other: Optional[StrictBool] = Field(None, alias="clientDomainSubDomainDeleteOther")
    vendor_create: Optional[StrictBool] = Field(None, alias="vendorCreate")
    vendor_view_other: Optional[StrictBool] = Field(None, alias="vendorViewOther")
    vendor_edit_other: Optional[StrictBool] = Field(None, alias="vendorEditOther")
    vendor_delete_other: Optional[StrictBool] = Field(None, alias="vendorDeleteOther")
    dashboard_setting: Optional[StrictStr] = Field(None, alias="dashboardSetting")
    setup_server: Optional[StrictBool] = Field(None, alias="setupServer")
    __properties = ["sourceLocales", "targetLocales", "workflowSteps", "clients", "domains", "subDomains", "projectCreate", "projectViewOther", "projectEditOther", "projectDeleteOther", "projectClients", "projectBusinessUnits", "projectTemplateCreate", "projectTemplateViewOther", "projectTemplateEditOther", "projectTemplateDeleteOther", "projectTemplateClients", "projectTemplateBusinessUnits", "transMemoryCreate", "transMemoryViewOther", "transMemoryEditOther", "transMemoryDeleteOther", "transMemoryExportOther", "transMemoryImportOther", "transMemoryClients", "transMemoryBusinessUnits", "termBaseCreate", "termBaseViewOther", "termBaseEditOther", "termBaseDeleteOther", "termBaseExportOther", "termBaseImportOther", "termBaseApproveOther", "termBaseClients", "termBaseBusinessUnits", "userCreate", "userViewOther", "userEditOther", "userDeleteOther", "clientDomainSubDomainCreate", "clientDomainSubDomainViewOther", "clientDomainSubDomainEditOther", "clientDomainSubDomainDeleteOther", "vendorCreate", "vendorViewOther", "vendorEditOther", "vendorDeleteOther", "dashboardSetting", "setupServer"]

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
    def from_json(cls, json_str: str) -> PROJECTMANAGERRESPONSEAllOf:
        """Create an instance of PROJECTMANAGERRESPONSEAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in workflow_steps (list)
        _items = []
        if self.workflow_steps:
            for _item in self.workflow_steps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['workflowSteps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in clients (list)
        _items = []
        if self.clients:
            for _item in self.clients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['clients'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in domains (list)
        _items = []
        if self.domains:
            for _item in self.domains:
                if _item:
                    _items.append(_item.to_dict())
            _dict['domains'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sub_domains (list)
        _items = []
        if self.sub_domains:
            for _item in self.sub_domains:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subDomains'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in project_clients (list)
        _items = []
        if self.project_clients:
            for _item in self.project_clients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['projectClients'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in project_business_units (list)
        _items = []
        if self.project_business_units:
            for _item in self.project_business_units:
                if _item:
                    _items.append(_item.to_dict())
            _dict['projectBusinessUnits'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in project_template_clients (list)
        _items = []
        if self.project_template_clients:
            for _item in self.project_template_clients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['projectTemplateClients'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in project_template_business_units (list)
        _items = []
        if self.project_template_business_units:
            for _item in self.project_template_business_units:
                if _item:
                    _items.append(_item.to_dict())
            _dict['projectTemplateBusinessUnits'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in trans_memory_clients (list)
        _items = []
        if self.trans_memory_clients:
            for _item in self.trans_memory_clients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transMemoryClients'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in trans_memory_business_units (list)
        _items = []
        if self.trans_memory_business_units:
            for _item in self.trans_memory_business_units:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transMemoryBusinessUnits'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in term_base_clients (list)
        _items = []
        if self.term_base_clients:
            for _item in self.term_base_clients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['termBaseClients'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in term_base_business_units (list)
        _items = []
        if self.term_base_business_units:
            for _item in self.term_base_business_units:
                if _item:
                    _items.append(_item.to_dict())
            _dict['termBaseBusinessUnits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PROJECTMANAGERRESPONSEAllOf:
        """Create an instance of PROJECTMANAGERRESPONSEAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PROJECTMANAGERRESPONSEAllOf.parse_obj(obj)

        _obj = PROJECTMANAGERRESPONSEAllOf.parse_obj({
            "source_locales": obj.get("sourceLocales"),
            "target_locales": obj.get("targetLocales"),
            "workflow_steps": [WorkflowStepReferenceV3.from_dict(_item) for _item in obj.get("workflowSteps")] if obj.get("workflowSteps") is not None else None,
            "clients": [ClientReference.from_dict(_item) for _item in obj.get("clients")] if obj.get("clients") is not None else None,
            "domains": [DomainReference.from_dict(_item) for _item in obj.get("domains")] if obj.get("domains") is not None else None,
            "sub_domains": [SubDomainReference.from_dict(_item) for _item in obj.get("subDomains")] if obj.get("subDomains") is not None else None,
            "project_create": obj.get("projectCreate"),
            "project_view_other": obj.get("projectViewOther"),
            "project_edit_other": obj.get("projectEditOther"),
            "project_delete_other": obj.get("projectDeleteOther"),
            "project_clients": [ClientReference.from_dict(_item) for _item in obj.get("projectClients")] if obj.get("projectClients") is not None else None,
            "project_business_units": [BusinessUnitReference.from_dict(_item) for _item in obj.get("projectBusinessUnits")] if obj.get("projectBusinessUnits") is not None else None,
            "project_template_create": obj.get("projectTemplateCreate"),
            "project_template_view_other": obj.get("projectTemplateViewOther"),
            "project_template_edit_other": obj.get("projectTemplateEditOther"),
            "project_template_delete_other": obj.get("projectTemplateDeleteOther"),
            "project_template_clients": [ClientReference.from_dict(_item) for _item in obj.get("projectTemplateClients")] if obj.get("projectTemplateClients") is not None else None,
            "project_template_business_units": [BusinessUnitReference.from_dict(_item) for _item in obj.get("projectTemplateBusinessUnits")] if obj.get("projectTemplateBusinessUnits") is not None else None,
            "trans_memory_create": obj.get("transMemoryCreate"),
            "trans_memory_view_other": obj.get("transMemoryViewOther"),
            "trans_memory_edit_other": obj.get("transMemoryEditOther"),
            "trans_memory_delete_other": obj.get("transMemoryDeleteOther"),
            "trans_memory_export_other": obj.get("transMemoryExportOther"),
            "trans_memory_import_other": obj.get("transMemoryImportOther"),
            "trans_memory_clients": [ClientReference.from_dict(_item) for _item in obj.get("transMemoryClients")] if obj.get("transMemoryClients") is not None else None,
            "trans_memory_business_units": [BusinessUnitReference.from_dict(_item) for _item in obj.get("transMemoryBusinessUnits")] if obj.get("transMemoryBusinessUnits") is not None else None,
            "term_base_create": obj.get("termBaseCreate"),
            "term_base_view_other": obj.get("termBaseViewOther"),
            "term_base_edit_other": obj.get("termBaseEditOther"),
            "term_base_delete_other": obj.get("termBaseDeleteOther"),
            "term_base_export_other": obj.get("termBaseExportOther"),
            "term_base_import_other": obj.get("termBaseImportOther"),
            "term_base_approve_other": obj.get("termBaseApproveOther"),
            "term_base_clients": [ClientReference.from_dict(_item) for _item in obj.get("termBaseClients")] if obj.get("termBaseClients") is not None else None,
            "term_base_business_units": [BusinessUnitReference.from_dict(_item) for _item in obj.get("termBaseBusinessUnits")] if obj.get("termBaseBusinessUnits") is not None else None,
            "user_create": obj.get("userCreate"),
            "user_view_other": obj.get("userViewOther"),
            "user_edit_other": obj.get("userEditOther"),
            "user_delete_other": obj.get("userDeleteOther"),
            "client_domain_sub_domain_create": obj.get("clientDomainSubDomainCreate"),
            "client_domain_sub_domain_view_other": obj.get("clientDomainSubDomainViewOther"),
            "client_domain_sub_domain_edit_other": obj.get("clientDomainSubDomainEditOther"),
            "client_domain_sub_domain_delete_other": obj.get("clientDomainSubDomainDeleteOther"),
            "vendor_create": obj.get("vendorCreate"),
            "vendor_view_other": obj.get("vendorViewOther"),
            "vendor_edit_other": obj.get("vendorEditOther"),
            "vendor_delete_other": obj.get("vendorDeleteOther"),
            "dashboard_setting": obj.get("dashboardSetting"),
            "setup_server": obj.get("setupServer")
        })
        return _obj

