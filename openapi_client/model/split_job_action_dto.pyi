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


class SplitJobActionDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class segmentOrdinals(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'segmentOrdinals':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            partCount = schemas.Int32Schema
            partSize = schemas.Int32Schema
            wordCount = schemas.Int32Schema
            byDocumentPart = schemas.BoolSchema
            __annotations__ = {
                "segmentOrdinals": segmentOrdinals,
                "partCount": partCount,
                "partSize": partSize,
                "wordCount": wordCount,
                "byDocumentPart": byDocumentPart,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["segmentOrdinals"]) -> MetaOapg.properties.segmentOrdinals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partCount"]) -> MetaOapg.properties.partCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partSize"]) -> MetaOapg.properties.partSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wordCount"]) -> MetaOapg.properties.wordCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["byDocumentPart"]) -> MetaOapg.properties.byDocumentPart: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["segmentOrdinals", "partCount", "partSize", "wordCount", "byDocumentPart", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["segmentOrdinals"]) -> typing.Union[MetaOapg.properties.segmentOrdinals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partCount"]) -> typing.Union[MetaOapg.properties.partCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partSize"]) -> typing.Union[MetaOapg.properties.partSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wordCount"]) -> typing.Union[MetaOapg.properties.wordCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["byDocumentPart"]) -> typing.Union[MetaOapg.properties.byDocumentPart, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["segmentOrdinals", "partCount", "partSize", "wordCount", "byDocumentPart", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        segmentOrdinals: typing.Union[MetaOapg.properties.segmentOrdinals, list, tuple, schemas.Unset] = schemas.unset,
        partCount: typing.Union[MetaOapg.properties.partCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        partSize: typing.Union[MetaOapg.properties.partSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wordCount: typing.Union[MetaOapg.properties.wordCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        byDocumentPart: typing.Union[MetaOapg.properties.byDocumentPart, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SplitJobActionDto':
        return super().__new__(
            cls,
            *_args,
            segmentOrdinals=segmentOrdinals,
            partCount=partCount,
            partSize=partSize,
            wordCount=wordCount,
            byDocumentPart=byDocumentPart,
            _configuration=_configuration,
            **kwargs,
        )