# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class ProjectTemplateDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            uid = schemas.StrSchema
            templateName = schemas.StrSchema
            name = schemas.StrSchema
            sourceLang = schemas.StrSchema
            
            
            class targetLangs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'targetLangs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            note = schemas.StrSchema
            useDynamicTitle = schemas.BoolSchema
            dynamicTitle = schemas.StrSchema
        
            @staticmethod
            def owner() -> typing.Type['UserReference']:
                return UserReference
        
            @staticmethod
            def client() -> typing.Type['ClientReference']:
                return ClientReference
        
            @staticmethod
            def domain() -> typing.Type['DomainReference']:
                return DomainReference
        
            @staticmethod
            def subDomain() -> typing.Type['SubDomainReference']:
                return SubDomainReference
        
            @staticmethod
            def vendor() -> typing.Type['VendorReference']:
                return VendorReference
        
            @staticmethod
            def createdBy() -> typing.Type['UserReference']:
                return UserReference
            dateCreated = schemas.DateTimeSchema
        
            @staticmethod
            def modifiedBy() -> typing.Type['UserReference']:
                return UserReference
            dateModified = schemas.DateTimeSchema
            dateTimeModified = schemas.DateTimeSchema
            
            
            class workflowSteps(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowStepDto']:
                        return WorkflowStepDto
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['WorkflowStepDto'], typing.List['WorkflowStepDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'workflowSteps':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowStepDto':
                    return super().__getitem__(i)
            
            
            class workflowSettings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkflowStepSettingsDto']:
                        return WorkflowStepSettingsDto
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['WorkflowStepSettingsDto'], typing.List['WorkflowStepSettingsDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'workflowSettings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkflowStepSettingsDto':
                    return super().__getitem__(i)
        
            @staticmethod
            def businessUnit() -> typing.Type['BusinessUnitReference']:
                return BusinessUnitReference
        
            @staticmethod
            def notifyProviders() -> typing.Type['ProjectTemplateNotifyProviderDto']:
                return ProjectTemplateNotifyProviderDto
            
            
            class assignedTo(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AssignmentPerTargetLangDto']:
                        return AssignmentPerTargetLangDto
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['AssignmentPerTargetLangDto'], typing.List['AssignmentPerTargetLangDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assignedTo':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AssignmentPerTargetLangDto':
                    return super().__getitem__(i)
        
            @staticmethod
            def importSettings() -> typing.Type['UidReference']:
                return UidReference
            __annotations__ = {
                "id": id,
                "uid": uid,
                "templateName": templateName,
                "name": name,
                "sourceLang": sourceLang,
                "targetLangs": targetLangs,
                "note": note,
                "useDynamicTitle": useDynamicTitle,
                "dynamicTitle": dynamicTitle,
                "owner": owner,
                "client": client,
                "domain": domain,
                "subDomain": subDomain,
                "vendor": vendor,
                "createdBy": createdBy,
                "dateCreated": dateCreated,
                "modifiedBy": modifiedBy,
                "dateModified": dateModified,
                "dateTimeModified": dateTimeModified,
                "workflowSteps": workflowSteps,
                "workflowSettings": workflowSettings,
                "businessUnit": businessUnit,
                "notifyProviders": notifyProviders,
                "assignedTo": assignedTo,
                "importSettings": importSettings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uid"]) -> MetaOapg.properties.uid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateName"]) -> MetaOapg.properties.templateName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceLang"]) -> MetaOapg.properties.sourceLang: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetLangs"]) -> MetaOapg.properties.targetLangs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useDynamicTitle"]) -> MetaOapg.properties.useDynamicTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dynamicTitle"]) -> MetaOapg.properties.dynamicTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> 'UserReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client"]) -> 'ClientReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain"]) -> 'DomainReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subDomain"]) -> 'SubDomainReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendor"]) -> 'VendorReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdBy"]) -> 'UserReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateCreated"]) -> MetaOapg.properties.dateCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedBy"]) -> 'UserReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateModified"]) -> MetaOapg.properties.dateModified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTimeModified"]) -> MetaOapg.properties.dateTimeModified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowSteps"]) -> MetaOapg.properties.workflowSteps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowSettings"]) -> MetaOapg.properties.workflowSettings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["businessUnit"]) -> 'BusinessUnitReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifyProviders"]) -> 'ProjectTemplateNotifyProviderDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignedTo"]) -> MetaOapg.properties.assignedTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["importSettings"]) -> 'UidReference': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "uid", "templateName", "name", "sourceLang", "targetLangs", "note", "useDynamicTitle", "dynamicTitle", "owner", "client", "domain", "subDomain", "vendor", "createdBy", "dateCreated", "modifiedBy", "dateModified", "dateTimeModified", "workflowSteps", "workflowSettings", "businessUnit", "notifyProviders", "assignedTo", "importSettings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uid"]) -> typing.Union[MetaOapg.properties.uid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateName"]) -> typing.Union[MetaOapg.properties.templateName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceLang"]) -> typing.Union[MetaOapg.properties.sourceLang, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetLangs"]) -> typing.Union[MetaOapg.properties.targetLangs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useDynamicTitle"]) -> typing.Union[MetaOapg.properties.useDynamicTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dynamicTitle"]) -> typing.Union[MetaOapg.properties.dynamicTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union['UserReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client"]) -> typing.Union['ClientReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain"]) -> typing.Union['DomainReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subDomain"]) -> typing.Union['SubDomainReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor"]) -> typing.Union['VendorReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdBy"]) -> typing.Union['UserReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateCreated"]) -> typing.Union[MetaOapg.properties.dateCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedBy"]) -> typing.Union['UserReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateModified"]) -> typing.Union[MetaOapg.properties.dateModified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTimeModified"]) -> typing.Union[MetaOapg.properties.dateTimeModified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowSteps"]) -> typing.Union[MetaOapg.properties.workflowSteps, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowSettings"]) -> typing.Union[MetaOapg.properties.workflowSettings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["businessUnit"]) -> typing.Union['BusinessUnitReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifyProviders"]) -> typing.Union['ProjectTemplateNotifyProviderDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignedTo"]) -> typing.Union[MetaOapg.properties.assignedTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["importSettings"]) -> typing.Union['UidReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "uid", "templateName", "name", "sourceLang", "targetLangs", "note", "useDynamicTitle", "dynamicTitle", "owner", "client", "domain", "subDomain", "vendor", "createdBy", "dateCreated", "modifiedBy", "dateModified", "dateTimeModified", "workflowSteps", "workflowSettings", "businessUnit", "notifyProviders", "assignedTo", "importSettings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        uid: typing.Union[MetaOapg.properties.uid, str, schemas.Unset] = schemas.unset,
        templateName: typing.Union[MetaOapg.properties.templateName, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        sourceLang: typing.Union[MetaOapg.properties.sourceLang, str, schemas.Unset] = schemas.unset,
        targetLangs: typing.Union[MetaOapg.properties.targetLangs, list, tuple, schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, str, schemas.Unset] = schemas.unset,
        useDynamicTitle: typing.Union[MetaOapg.properties.useDynamicTitle, bool, schemas.Unset] = schemas.unset,
        dynamicTitle: typing.Union[MetaOapg.properties.dynamicTitle, str, schemas.Unset] = schemas.unset,
        owner: typing.Union['UserReference', schemas.Unset] = schemas.unset,
        client: typing.Union['ClientReference', schemas.Unset] = schemas.unset,
        domain: typing.Union['DomainReference', schemas.Unset] = schemas.unset,
        subDomain: typing.Union['SubDomainReference', schemas.Unset] = schemas.unset,
        vendor: typing.Union['VendorReference', schemas.Unset] = schemas.unset,
        createdBy: typing.Union['UserReference', schemas.Unset] = schemas.unset,
        dateCreated: typing.Union[MetaOapg.properties.dateCreated, str, datetime, schemas.Unset] = schemas.unset,
        modifiedBy: typing.Union['UserReference', schemas.Unset] = schemas.unset,
        dateModified: typing.Union[MetaOapg.properties.dateModified, str, datetime, schemas.Unset] = schemas.unset,
        dateTimeModified: typing.Union[MetaOapg.properties.dateTimeModified, str, datetime, schemas.Unset] = schemas.unset,
        workflowSteps: typing.Union[MetaOapg.properties.workflowSteps, list, tuple, schemas.Unset] = schemas.unset,
        workflowSettings: typing.Union[MetaOapg.properties.workflowSettings, list, tuple, schemas.Unset] = schemas.unset,
        businessUnit: typing.Union['BusinessUnitReference', schemas.Unset] = schemas.unset,
        notifyProviders: typing.Union['ProjectTemplateNotifyProviderDto', schemas.Unset] = schemas.unset,
        assignedTo: typing.Union[MetaOapg.properties.assignedTo, list, tuple, schemas.Unset] = schemas.unset,
        importSettings: typing.Union['UidReference', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectTemplateDto':
        return super().__new__(
            cls,
            *_args,
            id=id,
            uid=uid,
            templateName=templateName,
            name=name,
            sourceLang=sourceLang,
            targetLangs=targetLangs,
            note=note,
            useDynamicTitle=useDynamicTitle,
            dynamicTitle=dynamicTitle,
            owner=owner,
            client=client,
            domain=domain,
            subDomain=subDomain,
            vendor=vendor,
            createdBy=createdBy,
            dateCreated=dateCreated,
            modifiedBy=modifiedBy,
            dateModified=dateModified,
            dateTimeModified=dateTimeModified,
            workflowSteps=workflowSteps,
            workflowSettings=workflowSettings,
            businessUnit=businessUnit,
            notifyProviders=notifyProviders,
            assignedTo=assignedTo,
            importSettings=importSettings,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.assignment_per_target_lang_dto import AssignmentPerTargetLangDto
from openapi_client.model.business_unit_reference import BusinessUnitReference
from openapi_client.model.client_reference import ClientReference
from openapi_client.model.domain_reference import DomainReference
from openapi_client.model.project_template_notify_provider_dto import ProjectTemplateNotifyProviderDto
from openapi_client.model.sub_domain_reference import SubDomainReference
from openapi_client.model.uid_reference import UidReference
from openapi_client.model.user_reference import UserReference
from openapi_client.model.vendor_reference import VendorReference
from openapi_client.model.workflow_step_dto import WorkflowStepDto
from openapi_client.model.workflow_step_settings_dto import WorkflowStepSettingsDto