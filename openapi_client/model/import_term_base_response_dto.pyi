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


class ImportTermBaseResponseDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class langs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'langs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            createdTermsCount = schemas.Int64Schema
            updatedTermsCount = schemas.Int64Schema
            __annotations__ = {
                "langs": langs,
                "createdTermsCount": createdTermsCount,
                "updatedTermsCount": updatedTermsCount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["langs"]) -> MetaOapg.properties.langs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdTermsCount"]) -> MetaOapg.properties.createdTermsCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedTermsCount"]) -> MetaOapg.properties.updatedTermsCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["langs", "createdTermsCount", "updatedTermsCount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["langs"]) -> typing.Union[MetaOapg.properties.langs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdTermsCount"]) -> typing.Union[MetaOapg.properties.createdTermsCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedTermsCount"]) -> typing.Union[MetaOapg.properties.updatedTermsCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["langs", "createdTermsCount", "updatedTermsCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        langs: typing.Union[MetaOapg.properties.langs, list, tuple, schemas.Unset] = schemas.unset,
        createdTermsCount: typing.Union[MetaOapg.properties.createdTermsCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        updatedTermsCount: typing.Union[MetaOapg.properties.updatedTermsCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImportTermBaseResponseDto':
        return super().__new__(
            cls,
            *_args,
            langs=langs,
            createdTermsCount=createdTermsCount,
            updatedTermsCount=updatedTermsCount,
            _configuration=_configuration,
            **kwargs,
        )