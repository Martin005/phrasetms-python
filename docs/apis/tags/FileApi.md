<a id="__pageTop"></a>
# openapi_client.apis.tags.file_api.FileApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_url_file**](#create_url_file) | **post** /api2/v1/files | Upload file
[**deletes_file**](#deletes_file) | **delete** /api2/v1/files/{fileUid} | Delete file
[**get_file_json**](#get_file_json) | **get** /api2/v1/files/{fileUid} | Get file
[**get_files**](#get_files) | **get** /api2/v1/files | List files

# **create_url_file**
<a id="create_url_file"></a>
> UploadedFileDto create_url_file(content_dispositionbody)

Upload file

Accepts multipart/form-data, application/octet-stream or application/json.

### Example

```python
import openapi_client
from openapi_client.apis.tags import file_api
from openapi_client.model.uploaded_file_dto import UploadedFileDto
from openapi_client.model.remote_uploaded_file_dto import RemoteUploadedFileDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = file_api.FileApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Content-Disposition': "Content-Disposition_example",
    }
    body = RemoteUploadedFileDto(
        uid="uid_example",
        name="name_example",
        size=1,
        type="type_example",
        url="url_example",
    )
    try:
        # Upload file
        api_response = api_instance.create_url_file(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FileApi->create_url_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationOctetStream, SchemaForRequestBodyMultipartFormData] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteUploadedFileDto**](../../models/RemoteUploadedFileDto.md) |  | 


# SchemaForRequestBodyApplicationOctetStream
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteUploadedFileDto**](../../models/RemoteUploadedFileDto.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteUploadedFileDto**](../../models/RemoteUploadedFileDto.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Disposition | ContentDispositionSchema | | 

# ContentDispositionSchema

Contains filename (UTF-8 encoded).    `filename*=UTF-8''ExampleFileName.md`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Contains filename (UTF-8 encoded).    &#x60;filename*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_url_file.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_url_file.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_url_file.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_url_file.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_url_file.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_url_file.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_url_file.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_url_file.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_url_file.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_url_file.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_url_file.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_url_file.ApiResponseFor501) | Not implemented

#### create_url_file.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UploadedFileDto**](../../models/UploadedFileDto.md) |  | 


#### create_url_file.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_url_file.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_url_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_url_file.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_url_file.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_url_file.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_url_file.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_url_file.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_url_file.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_url_file.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_url_file.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **deletes_file**
<a id="deletes_file"></a>
> deletes_file(file_uid)

Delete file

### Example

```python
import openapi_client
from openapi_client.apis.tags import file_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = file_api.FileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fileUid': "fileUid_example",
    }
    try:
        # Delete file
        api_response = api_instance.deletes_file(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling FileApi->deletes_file: %s\n" % e)
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
fileUid | FileUidSchema | | 

# FileUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#deletes_file.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#deletes_file.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#deletes_file.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#deletes_file.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#deletes_file.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#deletes_file.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#deletes_file.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#deletes_file.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#deletes_file.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#deletes_file.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#deletes_file.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#deletes_file.ApiResponseFor501) | Not implemented

#### deletes_file.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### deletes_file.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_file_json**
<a id="get_file_json"></a>
> UploadedFileDto get_file_json(file_uid)

Get file

Get uploaded file as <b>octet-stream</b> or as <b>json</b> based on 'Accept' header

### Example

```python
import openapi_client
from openapi_client.apis.tags import file_api
from openapi_client.model.uploaded_file_dto import UploadedFileDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = file_api.FileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fileUid': "fileUid_example",
    }
    try:
        # Get file
        api_response = api_instance.get_file_json(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FileApi->get_file_json: %s\n" % e)
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
fileUid | FileUidSchema | | 

# FileUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_file_json.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_file_json.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_file_json.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_file_json.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_file_json.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_file_json.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_file_json.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_file_json.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_file_json.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_file_json.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_file_json.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_file_json.ApiResponseFor501) | Not implemented

#### get_file_json.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UploadedFileDto**](../../models/UploadedFileDto.md) |  | 


#### get_file_json.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_json.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_json.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_json.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_json.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_json.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_json.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_json.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_json.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_json.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_json.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_files**
<a id="get_files"></a>
> PageDtoUploadedFileDto get_files()

List files

### Example

```python
import openapi_client
from openapi_client.apis.tags import file_api
from openapi_client.model.page_dto_uploaded_file_dto import PageDtoUploadedFileDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = file_api.FileApi(api_client)

    # example passing only optional values
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
        'name': "name_example",
        'types': [
        "types_example"
    ],
        'createdBy': 1,
        'biggerThan': 1,
    }
    try:
        # List files
        api_response = api_instance.get_files(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FileApi->get_files: %s\n" % e)
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
types | TypesSchema | | optional
createdBy | CreatedBySchema | | optional
biggerThan | BiggerThanSchema | | optional


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

# TypesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# CreatedBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# BiggerThanSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_files.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_files.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_files.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_files.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_files.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_files.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_files.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_files.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_files.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_files.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_files.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_files.ApiResponseFor501) | Not implemented

#### get_files.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoUploadedFileDto**](../../models/PageDtoUploadedFileDto.md) |  | 


#### get_files.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_files.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_files.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_files.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_files.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_files.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_files.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_files.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_files.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_files.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_files.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

