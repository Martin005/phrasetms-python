# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
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

from . import path

# Query params
FilterSchema = schemas.StrSchema
AttributesSchema = schemas.StrSchema
SortBySchema = schemas.StrSchema


class SortOrderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "ascending": "ASCENDING",
            "descending": "DESCENDING",
        }
    
    @schemas.classproperty
    def ASCENDING(cls):
        return cls("ascending")
    
    @schemas.classproperty
    def DESCENDING(cls):
        return cls("descending")


class StartIndexSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_minimum = 1


class CountSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_maximum = 100
        inclusive_minimum = 0
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'filter': typing.Union[FilterSchema, str, ],
        'attributes': typing.Union[AttributesSchema, str, ],
        'sortBy': typing.Union[SortBySchema, str, ],
        'sortOrder': typing.Union[SortOrderSchema, str, ],
        'startIndex': typing.Union[StartIndexSchema, decimal.Decimal, int, ],
        'count': typing.Union[CountSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
    explode=True,
)
request_query_attributes = api_client.QueryParameter(
    name="attributes",
    style=api_client.ParameterStyle.FORM,
    schema=AttributesSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sortBy",
    style=api_client.ParameterStyle.FORM,
    schema=SortBySchema,
    explode=True,
)
request_query_sort_order = api_client.QueryParameter(
    name="sortOrder",
    style=api_client.ParameterStyle.FORM,
    schema=SortOrderSchema,
    explode=True,
)
request_query_start_index = api_client.QueryParameter(
    name="startIndex",
    style=api_client.ParameterStyle.FORM,
    schema=StartIndexSchema,
    explode=True,
)
request_query_count = api_client.QueryParameter(
    name="count",
    style=api_client.ParameterStyle.FORM,
    schema=CountSchema,
    explode=True,
)
# Header params
AuthorizationSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'Authorization': typing.Union[AuthorizationSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_authorization = api_client.HeaderParameter(
    name="Authorization",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AuthorizationSchema,
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
)


@dataclass
class ApiResponseFor405(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
)


@dataclass
class ApiResponseFor408(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_408 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor408,
)


@dataclass
class ApiResponseFor410(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_410 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor410,
)


@dataclass
class ApiResponseFor415(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_415 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor415,
)


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
)


@dataclass
class ApiResponseFor501(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
    ]
    headers: schemas.Unset = schemas.unset


_response_for_501 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor501,
)
_status_code_to_response = {
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '405': _response_for_405,
    '408': _response_for_408,
    '410': _response_for_410,
    '415': _response_for_415,
    '429': _response_for_429,
    '500': _response_for_500,
    '501': _response_for_501,
}


class BaseApi(api_client.Api):
    @typing.overload
    def _search_users_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _search_users_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _search_users_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _search_users_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Search users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_filter,
            request_query_attributes,
            request_query_sort_by,
            request_query_sort_order,
            request_query_start_index,
            request_query_count,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_authorization,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class SearchUsers(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def search_users(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def search_users(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def search_users(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def search_users(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._search_users_oapg(
            query_params=query_params,
            header_params=header_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._search_users_oapg(
            query_params=query_params,
            header_params=header_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

