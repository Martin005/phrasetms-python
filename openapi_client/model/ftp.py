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


class Ftp(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "password",
                    "port",
                    "host",
                    "userName",
                }
                
                class properties:
                    userName = schemas.StrSchema
                    password = schemas.StrSchema
                    host = schemas.StrSchema
                    port = schemas.Int32Schema
                    encryption = schemas.StrSchema
                    __annotations__ = {
                        "userName": userName,
                        "password": password,
                        "host": host,
                        "port": port,
                        "encryption": encryption,
                    }
            
            password: MetaOapg.properties.password
            port: MetaOapg.properties.port
            host: MetaOapg.properties.host
            userName: MetaOapg.properties.userName
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["userName"]) -> MetaOapg.properties.userName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["encryption"]) -> MetaOapg.properties.encryption: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["userName", "password", "host", "port", "encryption", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["userName"]) -> MetaOapg.properties.userName: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["encryption"]) -> typing.Union[MetaOapg.properties.encryption, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["userName", "password", "host", "port", "encryption", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                password: typing.Union[MetaOapg.properties.password, str, ],
                port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, ],
                host: typing.Union[MetaOapg.properties.host, str, ],
                userName: typing.Union[MetaOapg.properties.userName, str, ],
                encryption: typing.Union[MetaOapg.properties.encryption, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    password=password,
                    port=port,
                    host=host,
                    userName=userName,
                    encryption=encryption,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                AbstractConnectorDto,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Ftp':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.abstract_connector_dto import AbstractConnectorDto