<a id="__pageTop"></a>
# openapi_client.apis.tags.scim_api.SCIMApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_scim**](#create_user_scim) | **post** /api2/v1/scim/Users | Create user using SCIM
[**delete_user**](#delete_user) | **delete** /api2/v1/scim/Users/{userId} | Delete user using SCIM
[**edit_user**](#edit_user) | **put** /api2/v1/scim/Users/{userId} | Edit user using SCIM
[**get_resource_types**](#get_resource_types) | **get** /api2/v1/scim/ResourceTypes | List the types of SCIM Resources available
[**get_schema_by_urn**](#get_schema_by_urn) | **get** /api2/v1/scim/Schemas/{schemaUrn} | Get supported SCIM Schema by urn
[**get_schemas**](#get_schemas) | **get** /api2/v1/scim/Schemas | Get supported SCIM Schemas
[**get_scim_user**](#get_scim_user) | **get** /api2/v1/scim/Users/{userId} | Get user
[**get_service_provider_config_dto**](#get_service_provider_config_dto) | **get** /api2/v1/scim/ServiceProviderConfig | Retrieve the Service Provider&#x27;s Configuration
[**patch_user**](#patch_user) | **patch** /api2/v1/scim/Users/{userId} | Patch user using SCIM
[**search_users**](#search_users) | **get** /api2/v1/scim/Users | Search users

# **create_user_scim**
<a id="create_user_scim"></a>
> ScimUserCoreDto create_user_scim()

Create user using SCIM

 Supported schema: `\"urn:ietf:params:scim:schemas:core:2.0:User\"`  Create active user: ``` {     \"schemas\": [         \"urn:ietf:params:scim:schemas:core:2.0:User\"     ],     \"active\": true,     \"userName\": \"john.doe\",     \"emails\": [         {             \"primary\": true,             \"value\": \"john.doe@example.com\",             \"type\": \"work\"         }     ],     \"name\": {         \"givenName\": \"John\",         \"familyName\": \"Doe\"     } } ``` 

### Example

```python
import openapi_client
from openapi_client.apis.tags import scim_api
from openapi_client.model.scim_user_core_dto import ScimUserCoreDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scim_api.SCIMApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = ScimUserCoreDto(
        id="id_example",
        user_name="user_name_example",
        name=Name(
            given_name="given_name_example",
            family_name="family_name_example",
        ),
        active=True,
        emails=[
            Email(
                value="value_example",
                type="type_example",
                primary=True,
            )
        ],
        meta=ScimMeta(
            created="1970-01-01T00:00:00.00Z",
            location="location_example",
        ),
    )
    try:
        # Create user using SCIM
        api_response = api_instance.create_user_scim(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->create_user_scim: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationScimjson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/scim+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


# SchemaForRequestBodyApplicationScimjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_user_scim.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_user_scim.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_user_scim.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_user_scim.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_user_scim.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_user_scim.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_user_scim.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_user_scim.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_user_scim.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_user_scim.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_user_scim.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_user_scim.ApiResponseFor501) | Not implemented

#### create_user_scim.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationScimjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


# SchemaFor201ResponseBodyApplicationScimjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


#### create_user_scim.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user_scim.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user_scim.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user_scim.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user_scim.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user_scim.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user_scim.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user_scim.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user_scim.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user_scim.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_user_scim.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_user**
<a id="delete_user"></a>
> delete_user(user_id)

Delete user using SCIM

### Example

```python
import openapi_client
from openapi_client.apis.tags import scim_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scim_api.SCIMApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': 1,
    }
    header_params = {
    }
    try:
        # Delete user using SCIM
        api_response = api_instance.delete_user(
            path_params=path_params,
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->delete_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userId': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Delete user using SCIM
        api_response = api_instance.delete_user(
            path_params=path_params,
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->delete_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_user.ApiResponseFor200) | No Content
400 | [ApiResponseFor400](#delete_user.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_user.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_user.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_user.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_user.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_user.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_user.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_user.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_user.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_user.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_user.ApiResponseFor501) | Not implemented

#### delete_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_user.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_user**
<a id="edit_user"></a>
> ScimUserCoreDto edit_user(user_id)

Edit user using SCIM

### Example

```python
import openapi_client
from openapi_client.apis.tags import scim_api
from openapi_client.model.scim_user_core_dto import ScimUserCoreDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scim_api.SCIMApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': 1,
    }
    header_params = {
    }
    try:
        # Edit user using SCIM
        api_response = api_instance.edit_user(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->edit_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userId': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = ScimUserCoreDto(
        id="id_example",
        user_name="user_name_example",
        name=Name(
            given_name="given_name_example",
            family_name="family_name_example",
        ),
        active=True,
        emails=[
            Email(
                value="value_example",
                type="type_example",
                primary=True,
            )
        ],
        meta=ScimMeta(
            created="1970-01-01T00:00:00.00Z",
            location="location_example",
        ),
    )
    try:
        # Edit user using SCIM
        api_response = api_instance.edit_user(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->edit_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationScimjson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/scim+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


# SchemaForRequestBodyApplicationScimjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_user.ApiResponseFor200) | Updated
400 | [ApiResponseFor400](#edit_user.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_user.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_user.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_user.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_user.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_user.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_user.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_user.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_user.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_user.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_user.ApiResponseFor501) | Not implemented

#### edit_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationScimjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


# SchemaFor200ResponseBodyApplicationScimjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


#### edit_user.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_user.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_user.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_user.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_user.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_user.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_user.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_user.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_resource_types**
<a id="get_resource_types"></a>
> [ScimResourceTypeSchema] get_resource_types()

List the types of SCIM Resources available

### Example

```python
import openapi_client
from openapi_client.apis.tags import scim_api
from openapi_client.model.scim_resource_type_schema import ScimResourceTypeSchema
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scim_api.SCIMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the types of SCIM Resources available
        api_response = api_instance.get_resource_types()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->get_resource_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_resource_types.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_resource_types.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_resource_types.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_resource_types.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_resource_types.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_resource_types.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_resource_types.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_resource_types.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_resource_types.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_resource_types.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_resource_types.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_resource_types.ApiResponseFor501) | Not implemented

#### get_resource_types.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ScimResourceTypeSchema**]({{complexTypePrefix}}ScimResourceTypeSchema.md) | [**ScimResourceTypeSchema**]({{complexTypePrefix}}ScimResourceTypeSchema.md) | [**ScimResourceTypeSchema**]({{complexTypePrefix}}ScimResourceTypeSchema.md) |  | 

#### get_resource_types.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_resource_types.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_resource_types.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_resource_types.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_resource_types.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_resource_types.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_resource_types.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_resource_types.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_resource_types.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_resource_types.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_resource_types.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_schema_by_urn**
<a id="get_schema_by_urn"></a>
> ScimResourceSchema get_schema_by_urn(schema_urn)

Get supported SCIM Schema by urn

### Example

```python
import openapi_client
from openapi_client.apis.tags import scim_api
from openapi_client.model.scim_resource_schema import ScimResourceSchema
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scim_api.SCIMApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'schemaUrn': "schemaUrn_example",
    }
    try:
        # Get supported SCIM Schema by urn
        api_response = api_instance.get_schema_by_urn(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->get_schema_by_urn: %s\n" % e)
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
schemaUrn | SchemaUrnSchema | | 

# SchemaUrnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_schema_by_urn.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_schema_by_urn.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_schema_by_urn.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_schema_by_urn.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_schema_by_urn.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_schema_by_urn.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_schema_by_urn.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_schema_by_urn.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_schema_by_urn.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_schema_by_urn.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_schema_by_urn.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_schema_by_urn.ApiResponseFor501) | Not implemented

#### get_schema_by_urn.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimResourceSchema**](../../models/ScimResourceSchema.md) |  | 


#### get_schema_by_urn.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schema_by_urn.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schema_by_urn.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schema_by_urn.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schema_by_urn.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schema_by_urn.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schema_by_urn.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schema_by_urn.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schema_by_urn.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schema_by_urn.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schema_by_urn.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_schemas**
<a id="get_schemas"></a>
> [ScimResourceSchema] get_schemas()

Get supported SCIM Schemas

### Example

```python
import openapi_client
from openapi_client.apis.tags import scim_api
from openapi_client.model.scim_resource_schema import ScimResourceSchema
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scim_api.SCIMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get supported SCIM Schemas
        api_response = api_instance.get_schemas()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->get_schemas: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_schemas.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_schemas.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_schemas.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_schemas.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_schemas.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_schemas.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_schemas.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_schemas.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_schemas.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_schemas.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_schemas.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_schemas.ApiResponseFor501) | Not implemented

#### get_schemas.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ScimResourceSchema**]({{complexTypePrefix}}ScimResourceSchema.md) | [**ScimResourceSchema**]({{complexTypePrefix}}ScimResourceSchema.md) | [**ScimResourceSchema**]({{complexTypePrefix}}ScimResourceSchema.md) |  | 

#### get_schemas.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schemas.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schemas.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schemas.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schemas.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schemas.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schemas.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schemas.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schemas.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schemas.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_schemas.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_scim_user**
<a id="get_scim_user"></a>
> ScimUserCoreDto get_scim_user(user_id)

Get user

### Example

```python
import openapi_client
from openapi_client.apis.tags import scim_api
from openapi_client.model.scim_user_core_dto import ScimUserCoreDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scim_api.SCIMApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': 1,
    }
    header_params = {
    }
    try:
        # Get user
        api_response = api_instance.get_scim_user(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->get_scim_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userId': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Get user
        api_response = api_instance.get_scim_user(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->get_scim_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/scim+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_scim_user.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_scim_user.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_scim_user.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_scim_user.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_scim_user.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_scim_user.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_scim_user.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_scim_user.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_scim_user.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_scim_user.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_scim_user.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_scim_user.ApiResponseFor501) | Not implemented

#### get_scim_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationScimjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


# SchemaFor200ResponseBodyApplicationScimjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


#### get_scim_user.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_scim_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_scim_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_scim_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_scim_user.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_scim_user.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_scim_user.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_scim_user.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_scim_user.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_scim_user.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_scim_user.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_service_provider_config_dto**
<a id="get_service_provider_config_dto"></a>
> ServiceProviderConfigDto get_service_provider_config_dto()

Retrieve the Service Provider's Configuration

### Example

```python
import openapi_client
from openapi_client.apis.tags import scim_api
from openapi_client.model.service_provider_config_dto import ServiceProviderConfigDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scim_api.SCIMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the Service Provider's Configuration
        api_response = api_instance.get_service_provider_config_dto()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->get_service_provider_config_dto: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_service_provider_config_dto.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_service_provider_config_dto.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_service_provider_config_dto.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_service_provider_config_dto.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_service_provider_config_dto.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_service_provider_config_dto.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_service_provider_config_dto.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_service_provider_config_dto.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_service_provider_config_dto.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_service_provider_config_dto.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_service_provider_config_dto.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_service_provider_config_dto.ApiResponseFor501) | Not implemented

#### get_service_provider_config_dto.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceProviderConfigDto**](../../models/ServiceProviderConfigDto.md) |  | 


#### get_service_provider_config_dto.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_service_provider_config_dto.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_service_provider_config_dto.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_service_provider_config_dto.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_service_provider_config_dto.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_service_provider_config_dto.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_service_provider_config_dto.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_service_provider_config_dto.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_service_provider_config_dto.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_service_provider_config_dto.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_service_provider_config_dto.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_user**
<a id="patch_user"></a>
> ScimUserCoreDto patch_user(user_id)

Patch user using SCIM

### Example

```python
import openapi_client
from openapi_client.apis.tags import scim_api
from openapi_client.model.scim_user_core_dto import ScimUserCoreDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scim_api.SCIMApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': 1,
    }
    header_params = {
    }
    try:
        # Patch user using SCIM
        api_response = api_instance.patch_user(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->patch_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userId': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        "key": dict(),
    )
    try:
        # Patch user using SCIM
        api_response = api_instance.patch_user(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->patch_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/scim+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_user.ApiResponseFor200) | Patched
400 | [ApiResponseFor400](#patch_user.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#patch_user.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#patch_user.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#patch_user.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#patch_user.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#patch_user.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#patch_user.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#patch_user.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#patch_user.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#patch_user.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#patch_user.ApiResponseFor501) | Not implemented

#### patch_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationScimjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


# SchemaFor200ResponseBodyApplicationScimjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScimUserCoreDto**](../../models/ScimUserCoreDto.md) |  | 


#### patch_user.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_user.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_user.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_user.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_user.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_user.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_user.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_user.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_users**
<a id="search_users"></a>
> search_users()

Search users

 This operation supports <a href=\"http://ldapwiki.com/wiki/SCIM%20Filtering\" target=\"_blank\">SCIM Filter</a>,  <a href=\"http://ldapwiki.com/wiki/SCIM%20Search%20Request\" target=\"_blank\">SCIM attributes</a> and  <a href=\"http://ldapwiki.com/wiki/SCIM%20Sorting\" target=\"_blank\">SCIM sort</a>  Supported attributes:   - `id`   - `active`   - `userName`   - `name.givenName`   - `name.familyName`   - `emails.value`   - `meta.created` 

### Example

```python
import openapi_client
from openapi_client.apis.tags import scim_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scim_api.SCIMApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': "filter_example",
        'attributes': "attributes_example",
        'sortBy': "sortBy_example",
        'sortOrder': "ascending",
        'startIndex': 1,
        'count': 50,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Search users
        api_response = api_instance.search_users(
            query_params=query_params,
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SCIMApi->search_users: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filter | FilterSchema | | optional
attributes | AttributesSchema | | optional
sortBy | SortBySchema | | optional
sortOrder | SortOrderSchema | | optional
startIndex | StartIndexSchema | | optional
count | CountSchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AttributesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortOrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ascending", "descending", ] if omitted the server will use the default value of "ascending"

# StartIndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# CountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50value must be a 32 bit integer

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#search_users.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#search_users.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#search_users.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_users.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#search_users.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#search_users.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#search_users.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#search_users.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#search_users.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#search_users.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#search_users.ApiResponseFor501) | Not implemented

#### search_users.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_users.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_users.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_users.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_users.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_users.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_users.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_users.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_users.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_users.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_users.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

