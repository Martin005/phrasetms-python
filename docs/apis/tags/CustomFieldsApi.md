<a id="__pageTop"></a>
# openapi_client.apis.tags.custom_fields_api.CustomFieldsApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_field**](#create_custom_field) | **post** /api2/v1/customFields | Create custom field
[**get_custom_field**](#get_custom_field) | **get** /api2/v1/customFields/{fieldUid} | Get custom field
[**get_custom_field_list**](#get_custom_field_list) | **get** /api2/v1/customFields | Lists custom fields
[**get_custom_field_option_list**](#get_custom_field_option_list) | **get** /api2/v1/customFields/{fieldUid}/options | Lists options of custom field

# **create_custom_field**
<a id="create_custom_field"></a>
> CustomFieldDto create_custom_field()

Create custom field

### Example

```python
import openapi_client
from openapi_client.apis.tags import custom_fields_api
from openapi_client.model.custom_field_dto import CustomFieldDto
from openapi_client.model.create_custom_field_dto import CreateCustomFieldDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_fields_api.CustomFieldsApi(api_client)

    # example passing only optional values
    body = CreateCustomFieldDto(
        name="name_example",
        allowed_entities=[
            "PROJECT"
        ],
        options=[
            "options_example"
        ],
        type="MULTI_SELECT",
        required=True,
        description="description_example",
    )
    try:
        # Create custom field
        api_response = api_instance.create_custom_field(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomFieldsApi->create_custom_field: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateCustomFieldDto**](../../models/CreateCustomFieldDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_custom_field.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_custom_field.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_custom_field.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_custom_field.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_custom_field.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_custom_field.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_custom_field.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_custom_field.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_custom_field.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_custom_field.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_custom_field.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_custom_field.ApiResponseFor501) | Not implemented

#### create_custom_field.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomFieldDto**](../../models/CustomFieldDto.md) |  | 


#### create_custom_field.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_field.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_field.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_field.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_field.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_field.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_field.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_field.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_field.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_field.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_field.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_custom_field**
<a id="get_custom_field"></a>
> CustomFieldDto get_custom_field(field_uid)

Get custom field

### Example

```python
import openapi_client
from openapi_client.apis.tags import custom_fields_api
from openapi_client.model.custom_field_dto import CustomFieldDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_fields_api.CustomFieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fieldUid': "fieldUid_example",
    }
    try:
        # Get custom field
        api_response = api_instance.get_custom_field(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomFieldsApi->get_custom_field: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
fieldUid | FieldUidSchema | | 

# FieldUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_custom_field.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_custom_field.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_custom_field.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_custom_field.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_custom_field.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_custom_field.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_custom_field.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_custom_field.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_custom_field.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_custom_field.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_custom_field.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_custom_field.ApiResponseFor501) | Not implemented

#### get_custom_field.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomFieldDto**](../../models/CustomFieldDto.md) |  | 


#### get_custom_field.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_custom_field_list**
<a id="get_custom_field_list"></a>
> PageDtoCustomFieldDto get_custom_field_list()

Lists custom fields

### Example

```python
import openapi_client
from openapi_client.apis.tags import custom_fields_api
from openapi_client.model.page_dto_custom_field_dto import PageDtoCustomFieldDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_fields_api.CustomFieldsApi(api_client)

    # example passing only optional values
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
        'name': "name_example",
        'allowedEntities': [
        "PROJECT"
    ],
        'types': [
        "MULTI_SELECT"
    ],
        'createdBy': [
        "createdBy_example"
    ],
        'modifiedBy': [
        "modifiedBy_example"
    ],
        'uids': [
        "uids_example"
    ],
        'required': True,
        'sortField': "NAME",
        'sortTrend': "ASC",
    }
    try:
        # Lists custom fields
        api_response = api_instance.get_custom_field_list(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomFieldsApi->get_custom_field_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional
name | NameSchema | | optional
allowedEntities | AllowedEntitiesSchema | | optional
types | TypesSchema | | optional
createdBy | CreatedBySchema | | optional
modifiedBy | ModifiedBySchema | | optional
uids | UidsSchema | | optional
required | RequiredSchema | | optional
sortField | SortFieldSchema | | optional
sortTrend | SortTrendSchema | | optional


# PageNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50value must be a 32 bit integer

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AllowedEntitiesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["PROJECT", ] 

# TypesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["MULTI_SELECT", "SINGLE_SELECT", "STRING", "NUMBER", "URL", "DATE", ] 

# CreatedBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ModifiedBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# UidsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# RequiredSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# SortFieldSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NAME", "CREATED", "LAST_MODIFIED", ] 

# SortTrendSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "ASC"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_custom_field_list.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_custom_field_list.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_custom_field_list.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_custom_field_list.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_custom_field_list.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_custom_field_list.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_custom_field_list.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_custom_field_list.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_custom_field_list.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_custom_field_list.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_custom_field_list.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_custom_field_list.ApiResponseFor501) | Not implemented

#### get_custom_field_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoCustomFieldDto**](../../models/PageDtoCustomFieldDto.md) |  | 


#### get_custom_field_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_list.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_list.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_list.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_list.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_list.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_list.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_list.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_list.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_custom_field_option_list**
<a id="get_custom_field_option_list"></a>
> PageDtoCustomFieldOptionDto get_custom_field_option_list(field_uid)

Lists options of custom field

### Example

```python
import openapi_client
from openapi_client.apis.tags import custom_fields_api
from openapi_client.model.page_dto_custom_field_option_dto import PageDtoCustomFieldOptionDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = custom_fields_api.CustomFieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fieldUid': "fieldUid_example",
    }
    query_params = {
    }
    try:
        # Lists options of custom field
        api_response = api_instance.get_custom_field_option_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomFieldsApi->get_custom_field_option_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'fieldUid': "fieldUid_example",
    }
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
        'name': "name_example",
        'sortField': "NAME",
        'sortTrend': "ASC",
    }
    try:
        # Lists options of custom field
        api_response = api_instance.get_custom_field_option_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomFieldsApi->get_custom_field_option_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional
name | NameSchema | | optional
sortField | SortFieldSchema | | optional
sortTrend | SortTrendSchema | | optional


# PageNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50value must be a 32 bit integer

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortFieldSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NAME", ] 

# SortTrendSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "ASC"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
fieldUid | FieldUidSchema | | 

# FieldUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_custom_field_option_list.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_custom_field_option_list.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_custom_field_option_list.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_custom_field_option_list.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_custom_field_option_list.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_custom_field_option_list.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_custom_field_option_list.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_custom_field_option_list.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_custom_field_option_list.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_custom_field_option_list.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_custom_field_option_list.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_custom_field_option_list.ApiResponseFor501) | Not implemented

#### get_custom_field_option_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoCustomFieldOptionDto**](../../models/PageDtoCustomFieldOptionDto.md) |  | 


#### get_custom_field_option_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_option_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_option_list.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_option_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_option_list.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_option_list.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_option_list.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_option_list.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_option_list.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_option_list.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field_option_list.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

