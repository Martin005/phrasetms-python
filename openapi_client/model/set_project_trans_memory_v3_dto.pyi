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


class SetProjectTransMemoryV3Dto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "transMemory",
        }
        
        class properties:
        
            @staticmethod
            def transMemory() -> typing.Type['UidReference']:
                return UidReference
            readMode = schemas.BoolSchema
            writeMode = schemas.BoolSchema
            
            
            class penalty(
                schemas.Float64Schema
            ):
                pass
            applyPenaltyTo101Only = schemas.BoolSchema
            order = schemas.Int32Schema
            __annotations__ = {
                "transMemory": transMemory,
                "readMode": readMode,
                "writeMode": writeMode,
                "penalty": penalty,
                "applyPenaltyTo101Only": applyPenaltyTo101Only,
                "order": order,
            }
    
    transMemory: 'UidReference'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transMemory"]) -> 'UidReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readMode"]) -> MetaOapg.properties.readMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["writeMode"]) -> MetaOapg.properties.writeMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["penalty"]) -> MetaOapg.properties.penalty: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applyPenaltyTo101Only"]) -> MetaOapg.properties.applyPenaltyTo101Only: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transMemory", "readMode", "writeMode", "penalty", "applyPenaltyTo101Only", "order", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transMemory"]) -> 'UidReference': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readMode"]) -> typing.Union[MetaOapg.properties.readMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["writeMode"]) -> typing.Union[MetaOapg.properties.writeMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["penalty"]) -> typing.Union[MetaOapg.properties.penalty, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applyPenaltyTo101Only"]) -> typing.Union[MetaOapg.properties.applyPenaltyTo101Only, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transMemory", "readMode", "writeMode", "penalty", "applyPenaltyTo101Only", "order", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        transMemory: 'UidReference',
        readMode: typing.Union[MetaOapg.properties.readMode, bool, schemas.Unset] = schemas.unset,
        writeMode: typing.Union[MetaOapg.properties.writeMode, bool, schemas.Unset] = schemas.unset,
        penalty: typing.Union[MetaOapg.properties.penalty, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        applyPenaltyTo101Only: typing.Union[MetaOapg.properties.applyPenaltyTo101Only, bool, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SetProjectTransMemoryV3Dto':
        return super().__new__(
            cls,
            *_args,
            transMemory=transMemory,
            readMode=readMode,
            writeMode=writeMode,
            penalty=penalty,
            applyPenaltyTo101Only=applyPenaltyTo101Only,
            order=order,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.uid_reference import UidReference