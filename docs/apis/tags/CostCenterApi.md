<a id="__pageTop"></a>
# openapi_client.apis.tags.cost_center_api.CostCenterApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cost_center**](#create_cost_center) | **post** /api2/v1/costCenters | Create cost center
[**delete_cost_center**](#delete_cost_center) | **delete** /api2/v1/costCenters/{costCenterUid} | Delete cost center
[**get_cost_center**](#get_cost_center) | **get** /api2/v1/costCenters/{costCenterUid} | Get cost center
[**list_cost_centers**](#list_cost_centers) | **get** /api2/v1/costCenters | List of cost centers
[**update_cost_center**](#update_cost_center) | **put** /api2/v1/costCenters/{costCenterUid} | Edit cost center

# **create_cost_center**
<a id="create_cost_center"></a>
> CostCenterDto create_cost_center(body)

Create cost center

### Example

```python
import openapi_client
from openapi_client.apis.tags import cost_center_api
from openapi_client.model.cost_center_edit_dto import CostCenterEditDto
from openapi_client.model.cost_center_dto import CostCenterDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cost_center_api.CostCenterApi(api_client)

    # example passing only required values which don't have defaults set
    body = CostCenterEditDto(
        name="name_example",
    )
    try:
        # Create cost center
        api_response = api_instance.create_cost_center(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CostCenterApi->create_cost_center: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CostCenterEditDto**](../../models/CostCenterEditDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_cost_center.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_cost_center.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_cost_center.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_cost_center.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_cost_center.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_cost_center.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_cost_center.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_cost_center.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_cost_center.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_cost_center.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_cost_center.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_cost_center.ApiResponseFor501) | Not implemented

#### create_cost_center.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CostCenterDto**](../../models/CostCenterDto.md) |  | 


#### create_cost_center.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_cost_center.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_cost_center.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_cost_center.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_cost_center.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_cost_center.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_cost_center.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_cost_center.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_cost_center.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_cost_center.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_cost_center.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_cost_center**
<a id="delete_cost_center"></a>
> delete_cost_center(cost_center_uid)

Delete cost center

### Example

```python
import openapi_client
from openapi_client.apis.tags import cost_center_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cost_center_api.CostCenterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'costCenterUid': "costCenterUid_example",
    }
    try:
        # Delete cost center
        api_response = api_instance.delete_cost_center(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling CostCenterApi->delete_cost_center: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
costCenterUid | CostCenterUidSchema | | 

# CostCenterUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_cost_center.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_cost_center.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_cost_center.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_cost_center.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_cost_center.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_cost_center.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_cost_center.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_cost_center.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_cost_center.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_cost_center.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_cost_center.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_cost_center.ApiResponseFor501) | Not implemented

#### delete_cost_center.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_cost_center.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_cost_center**
<a id="get_cost_center"></a>
> CostCenterDto get_cost_center(cost_center_uid)

Get cost center

### Example

```python
import openapi_client
from openapi_client.apis.tags import cost_center_api
from openapi_client.model.cost_center_dto import CostCenterDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cost_center_api.CostCenterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'costCenterUid': "costCenterUid_example",
    }
    try:
        # Get cost center
        api_response = api_instance.get_cost_center(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CostCenterApi->get_cost_center: %s\n" % e)
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
costCenterUid | CostCenterUidSchema | | 

# CostCenterUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_cost_center.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_cost_center.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_cost_center.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_cost_center.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_cost_center.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_cost_center.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_cost_center.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_cost_center.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_cost_center.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_cost_center.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_cost_center.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_cost_center.ApiResponseFor501) | Not implemented

#### get_cost_center.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CostCenterDto**](../../models/CostCenterDto.md) |  | 


#### get_cost_center.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_cost_center.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_cost_center.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_cost_center.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_cost_center.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_cost_center.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_cost_center.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_cost_center.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_cost_center.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_cost_center.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_cost_center.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_cost_centers**
<a id="list_cost_centers"></a>
> PageDtoCostCenterDto list_cost_centers()

List of cost centers

### Example

```python
import openapi_client
from openapi_client.apis.tags import cost_center_api
from openapi_client.model.page_dto_cost_center_dto import PageDtoCostCenterDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cost_center_api.CostCenterApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'createdBy': "createdBy_example",
        'sort': "NAME",
        'order': "ASC",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List of cost centers
        api_response = api_instance.list_cost_centers(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CostCenterApi->list_cost_centers: %s\n" % e)
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
name | NameSchema | | optional
createdBy | CreatedBySchema | | optional
sort | SortSchema | | optional
order | OrderSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CreatedBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NAME", "DATE_CREATED", ] if omitted the server will use the default value of "NAME"

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "ASC"

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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_cost_centers.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_cost_centers.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_cost_centers.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_cost_centers.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_cost_centers.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_cost_centers.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_cost_centers.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_cost_centers.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_cost_centers.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_cost_centers.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_cost_centers.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_cost_centers.ApiResponseFor501) | Not implemented

#### list_cost_centers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoCostCenterDto**](../../models/PageDtoCostCenterDto.md) |  | 


#### list_cost_centers.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_cost_centers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_cost_centers.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_cost_centers.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_cost_centers.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_cost_centers.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_cost_centers.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_cost_centers.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_cost_centers.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_cost_centers.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_cost_centers.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_cost_center**
<a id="update_cost_center"></a>
> CostCenterDto update_cost_center(cost_center_uid)

Edit cost center

### Example

```python
import openapi_client
from openapi_client.apis.tags import cost_center_api
from openapi_client.model.cost_center_edit_dto import CostCenterEditDto
from openapi_client.model.cost_center_dto import CostCenterDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cost_center_api.CostCenterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'costCenterUid': "costCenterUid_example",
    }
    try:
        # Edit cost center
        api_response = api_instance.update_cost_center(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CostCenterApi->update_cost_center: %s\n" % e)

    # example passing only optional values
    path_params = {
        'costCenterUid': "costCenterUid_example",
    }
    body = CostCenterEditDto(
        name="name_example",
    )
    try:
        # Edit cost center
        api_response = api_instance.update_cost_center(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CostCenterApi->update_cost_center: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CostCenterEditDto**](../../models/CostCenterEditDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
costCenterUid | CostCenterUidSchema | | 

# CostCenterUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_cost_center.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#update_cost_center.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_cost_center.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_cost_center.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_cost_center.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_cost_center.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_cost_center.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_cost_center.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_cost_center.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_cost_center.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_cost_center.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_cost_center.ApiResponseFor501) | Not implemented

#### update_cost_center.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CostCenterDto**](../../models/CostCenterDto.md) |  | 


#### update_cost_center.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_cost_center.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_cost_center.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_cost_center.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_cost_center.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_cost_center.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_cost_center.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_cost_center.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_cost_center.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_cost_center.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_cost_center.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

