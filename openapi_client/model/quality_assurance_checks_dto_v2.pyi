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


class QualityAssuranceChecksDtoV2(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class forbiddenStrings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'forbiddenStrings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class enabledChecks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EnabledCheckDtoV2']:
                        return EnabledCheckDtoV2
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['EnabledCheckDtoV2'], typing.List['EnabledCheckDtoV2']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'enabledChecks':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EnabledCheckDtoV2':
                    return super().__getitem__(i)
            excludeLockedSegments = schemas.BoolSchema
            userCanSetInstantQA = schemas.BoolSchema
            strictJobStatus = schemas.BoolSchema
            
            
            class regexpRules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RegexpCheckRuleDtoV2']:
                        return RegexpCheckRuleDtoV2
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RegexpCheckRuleDtoV2'], typing.List['RegexpCheckRuleDtoV2']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'regexpRules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RegexpCheckRuleDtoV2':
                    return super().__getitem__(i)
            __annotations__ = {
                "forbiddenStrings": forbiddenStrings,
                "enabledChecks": enabledChecks,
                "excludeLockedSegments": excludeLockedSegments,
                "userCanSetInstantQA": userCanSetInstantQA,
                "strictJobStatus": strictJobStatus,
                "regexpRules": regexpRules,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forbiddenStrings"]) -> MetaOapg.properties.forbiddenStrings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabledChecks"]) -> MetaOapg.properties.enabledChecks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excludeLockedSegments"]) -> MetaOapg.properties.excludeLockedSegments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userCanSetInstantQA"]) -> MetaOapg.properties.userCanSetInstantQA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["strictJobStatus"]) -> MetaOapg.properties.strictJobStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regexpRules"]) -> MetaOapg.properties.regexpRules: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["forbiddenStrings", "enabledChecks", "excludeLockedSegments", "userCanSetInstantQA", "strictJobStatus", "regexpRules", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forbiddenStrings"]) -> typing.Union[MetaOapg.properties.forbiddenStrings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabledChecks"]) -> typing.Union[MetaOapg.properties.enabledChecks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excludeLockedSegments"]) -> typing.Union[MetaOapg.properties.excludeLockedSegments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userCanSetInstantQA"]) -> typing.Union[MetaOapg.properties.userCanSetInstantQA, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["strictJobStatus"]) -> typing.Union[MetaOapg.properties.strictJobStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regexpRules"]) -> typing.Union[MetaOapg.properties.regexpRules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["forbiddenStrings", "enabledChecks", "excludeLockedSegments", "userCanSetInstantQA", "strictJobStatus", "regexpRules", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        forbiddenStrings: typing.Union[MetaOapg.properties.forbiddenStrings, list, tuple, schemas.Unset] = schemas.unset,
        enabledChecks: typing.Union[MetaOapg.properties.enabledChecks, list, tuple, schemas.Unset] = schemas.unset,
        excludeLockedSegments: typing.Union[MetaOapg.properties.excludeLockedSegments, bool, schemas.Unset] = schemas.unset,
        userCanSetInstantQA: typing.Union[MetaOapg.properties.userCanSetInstantQA, bool, schemas.Unset] = schemas.unset,
        strictJobStatus: typing.Union[MetaOapg.properties.strictJobStatus, bool, schemas.Unset] = schemas.unset,
        regexpRules: typing.Union[MetaOapg.properties.regexpRules, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'QualityAssuranceChecksDtoV2':
        return super().__new__(
            cls,
            *_args,
            forbiddenStrings=forbiddenStrings,
            enabledChecks=enabledChecks,
            excludeLockedSegments=excludeLockedSegments,
            userCanSetInstantQA=userCanSetInstantQA,
            strictJobStatus=strictJobStatus,
            regexpRules=regexpRules,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.enabled_check_dto_v2 import EnabledCheckDtoV2
from openapi_client.model.regexp_check_rule_dto_v2 import RegexpCheckRuleDtoV2