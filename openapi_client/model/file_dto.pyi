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


class FileDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            encodedName = schemas.StrSchema
            contentType = schemas.StrSchema
            note = schemas.StrSchema
            size = schemas.Int64Schema
            directory = schemas.BoolSchema
            lastModified = schemas.DateTimeSchema
            selected = schemas.BoolSchema
        
            @staticmethod
            def error() -> typing.Type['ErrorDto']:
                return ErrorDto
            __annotations__ = {
                "id": id,
                "name": name,
                "encodedName": encodedName,
                "contentType": contentType,
                "note": note,
                "size": size,
                "directory": directory,
                "lastModified": lastModified,
                "selected": selected,
                "error": error,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encodedName"]) -> MetaOapg.properties.encodedName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentType"]) -> MetaOapg.properties.contentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directory"]) -> MetaOapg.properties.directory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastModified"]) -> MetaOapg.properties.lastModified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selected"]) -> MetaOapg.properties.selected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> 'ErrorDto': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "encodedName", "contentType", "note", "size", "directory", "lastModified", "selected", "error", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encodedName"]) -> typing.Union[MetaOapg.properties.encodedName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentType"]) -> typing.Union[MetaOapg.properties.contentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directory"]) -> typing.Union[MetaOapg.properties.directory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastModified"]) -> typing.Union[MetaOapg.properties.lastModified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selected"]) -> typing.Union[MetaOapg.properties.selected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union['ErrorDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "encodedName", "contentType", "note", "size", "directory", "lastModified", "selected", "error", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        encodedName: typing.Union[MetaOapg.properties.encodedName, str, schemas.Unset] = schemas.unset,
        contentType: typing.Union[MetaOapg.properties.contentType, str, schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, str, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        directory: typing.Union[MetaOapg.properties.directory, bool, schemas.Unset] = schemas.unset,
        lastModified: typing.Union[MetaOapg.properties.lastModified, str, datetime, schemas.Unset] = schemas.unset,
        selected: typing.Union[MetaOapg.properties.selected, bool, schemas.Unset] = schemas.unset,
        error: typing.Union['ErrorDto', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FileDto':
        return super().__new__(
            cls,
            *_args,
            id=id,
            name=name,
            encodedName=encodedName,
            contentType=contentType,
            note=note,
            size=size,
            directory=directory,
            lastModified=lastModified,
            selected=selected,
            error=error,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.error_dto import ErrorDto