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


class AsyncRequestV2Dto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def createdBy() -> typing.Type['UserReference']:
                return UserReference
            dateCreated = schemas.DateTimeSchema
            
            
            class action(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PRE_ANALYSE": "PRE_ANALYSE",
                        "POST_ANALYSE": "POST_ANALYSE",
                        "COMPARE_ANALYSE": "COMPARE_ANALYSE",
                        "PARENT_ANALYSE": "PARENT_ANALYSE",
                        "PRE_TRANSLATE": "PRE_TRANSLATE",
                        "ASYNC_TRANSLATE": "ASYNC_TRANSLATE",
                        "IMPORT_JOB": "IMPORT_JOB",
                        "IMPORT_FILE": "IMPORT_FILE",
                        "ALIGN": "ALIGN",
                        "EXPORT_TMX_BY_QUERY": "EXPORT_TMX_BY_QUERY",
                        "EXPORT_TMX": "EXPORT_TMX",
                        "IMPORT_TMX": "IMPORT_TMX",
                        "INSERT_INTO_TM": "INSERT_INTO_TM",
                        "DELETE_TM": "DELETE_TM",
                        "CLEAR_TM": "CLEAR_TM",
                        "QA": "QA",
                        "QA_V3": "QA_V3",
                        "UPDATE_CONTINUOUS_JOB": "UPDATE_CONTINUOUS_JOB",
                        "UPDATE_SOURCE": "UPDATE_SOURCE",
                        "UPDATE_TARGET": "UPDATE_TARGET",
                        "EXTRACT_CLEANED_TMS": "EXTRACT_CLEANED_TMS",
                        "GLOSSARY_PUT": "GLOSSARY_PUT",
                        "GLOSSARY_DELETE": "GLOSSARY_DELETE",
                        "CREATE_PROJECT": "CREATE_PROJECT",
                        "EXPORT_COMPLETE_FILE": "EXPORT_COMPLETE_FILE",
                    }
                
                @schemas.classproperty
                def PRE_ANALYSE(cls):
                    return cls("PRE_ANALYSE")
                
                @schemas.classproperty
                def POST_ANALYSE(cls):
                    return cls("POST_ANALYSE")
                
                @schemas.classproperty
                def COMPARE_ANALYSE(cls):
                    return cls("COMPARE_ANALYSE")
                
                @schemas.classproperty
                def PARENT_ANALYSE(cls):
                    return cls("PARENT_ANALYSE")
                
                @schemas.classproperty
                def PRE_TRANSLATE(cls):
                    return cls("PRE_TRANSLATE")
                
                @schemas.classproperty
                def ASYNC_TRANSLATE(cls):
                    return cls("ASYNC_TRANSLATE")
                
                @schemas.classproperty
                def IMPORT_JOB(cls):
                    return cls("IMPORT_JOB")
                
                @schemas.classproperty
                def IMPORT_FILE(cls):
                    return cls("IMPORT_FILE")
                
                @schemas.classproperty
                def ALIGN(cls):
                    return cls("ALIGN")
                
                @schemas.classproperty
                def EXPORT_TMX_BY_QUERY(cls):
                    return cls("EXPORT_TMX_BY_QUERY")
                
                @schemas.classproperty
                def EXPORT_TMX(cls):
                    return cls("EXPORT_TMX")
                
                @schemas.classproperty
                def IMPORT_TMX(cls):
                    return cls("IMPORT_TMX")
                
                @schemas.classproperty
                def INSERT_INTO_TM(cls):
                    return cls("INSERT_INTO_TM")
                
                @schemas.classproperty
                def DELETE_TM(cls):
                    return cls("DELETE_TM")
                
                @schemas.classproperty
                def CLEAR_TM(cls):
                    return cls("CLEAR_TM")
                
                @schemas.classproperty
                def QA(cls):
                    return cls("QA")
                
                @schemas.classproperty
                def QA_V3(cls):
                    return cls("QA_V3")
                
                @schemas.classproperty
                def UPDATE_CONTINUOUS_JOB(cls):
                    return cls("UPDATE_CONTINUOUS_JOB")
                
                @schemas.classproperty
                def UPDATE_SOURCE(cls):
                    return cls("UPDATE_SOURCE")
                
                @schemas.classproperty
                def UPDATE_TARGET(cls):
                    return cls("UPDATE_TARGET")
                
                @schemas.classproperty
                def EXTRACT_CLEANED_TMS(cls):
                    return cls("EXTRACT_CLEANED_TMS")
                
                @schemas.classproperty
                def GLOSSARY_PUT(cls):
                    return cls("GLOSSARY_PUT")
                
                @schemas.classproperty
                def GLOSSARY_DELETE(cls):
                    return cls("GLOSSARY_DELETE")
                
                @schemas.classproperty
                def CREATE_PROJECT(cls):
                    return cls("CREATE_PROJECT")
                
                @schemas.classproperty
                def EXPORT_COMPLETE_FILE(cls):
                    return cls("EXPORT_COMPLETE_FILE")
        
            @staticmethod
            def asyncResponse() -> typing.Type['AsyncResponseV2Dto']:
                return AsyncResponseV2Dto
        
            @staticmethod
            def parent() -> typing.Type['AsyncRequestV2Dto']:
                return AsyncRequestV2Dto
        
            @staticmethod
            def project() -> typing.Type['ProjectReference']:
                return ProjectReference
            __annotations__ = {
                "id": id,
                "createdBy": createdBy,
                "dateCreated": dateCreated,
                "action": action,
                "asyncResponse": asyncResponse,
                "parent": parent,
                "project": project,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdBy"]) -> 'UserReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateCreated"]) -> MetaOapg.properties.dateCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asyncResponse"]) -> 'AsyncResponseV2Dto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> 'AsyncRequestV2Dto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project"]) -> 'ProjectReference': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "createdBy", "dateCreated", "action", "asyncResponse", "parent", "project", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdBy"]) -> typing.Union['UserReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateCreated"]) -> typing.Union[MetaOapg.properties.dateCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asyncResponse"]) -> typing.Union['AsyncResponseV2Dto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union['AsyncRequestV2Dto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project"]) -> typing.Union['ProjectReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "createdBy", "dateCreated", "action", "asyncResponse", "parent", "project", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        createdBy: typing.Union['UserReference', schemas.Unset] = schemas.unset,
        dateCreated: typing.Union[MetaOapg.properties.dateCreated, str, datetime, schemas.Unset] = schemas.unset,
        action: typing.Union[MetaOapg.properties.action, str, schemas.Unset] = schemas.unset,
        asyncResponse: typing.Union['AsyncResponseV2Dto', schemas.Unset] = schemas.unset,
        parent: typing.Union['AsyncRequestV2Dto', schemas.Unset] = schemas.unset,
        project: typing.Union['ProjectReference', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AsyncRequestV2Dto':
        return super().__new__(
            cls,
            *_args,
            id=id,
            createdBy=createdBy,
            dateCreated=dateCreated,
            action=action,
            asyncResponse=asyncResponse,
            parent=parent,
            project=project,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.async_response_v2_dto import AsyncResponseV2Dto
from openapi_client.model.project_reference import ProjectReference
from openapi_client.model.user_reference import UserReference