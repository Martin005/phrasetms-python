# phrasetms_client.FileApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_url_file**](FileApi.md#create_url_file) | **POST** /api2/v1/files | Upload file
[**deletes_file**](FileApi.md#deletes_file) | **DELETE** /api2/v1/files/{fileUid} | Delete file
[**get_file_json**](FileApi.md#get_file_json) | **GET** /api2/v1/files/{fileUid} | Get file
[**get_files**](FileApi.md#get_files) | **GET** /api2/v1/files | List files


# **create_url_file**
> UploadedFileDto create_url_file(content_disposition, body)

Upload file

Accepts multipart/form-data, application/octet-stream or application/json.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.remote_uploaded_file_dto import RemoteUploadedFileDto
from phrasetms_client.models.uploaded_file_dto import UploadedFileDto
from phrasetms_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)


# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrasetms_client.FileApi(api_client)
    content_disposition = 'content_disposition_example' # str | must match pattern `((inline|attachment); )?filename\\*=UTF-8''(.+)`
    body = phrasetms_client.RemoteUploadedFileDto() # RemoteUploadedFileDto | file

    try:
        # Upload file
        api_response = api_instance.create_url_file(content_disposition, body)
        print("The response of FileApi->create_url_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->create_url_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_disposition** | **str**| must match pattern &#x60;((inline|attachment); )?filename\\*&#x3D;UTF-8&#39;&#39;(.+)&#x60; | 
 **body** | [**RemoteUploadedFileDto**](RemoteUploadedFileDto.md)| file | 

### Return type

[**UploadedFileDto**](UploadedFileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Not authorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**405** | Method not allowed |  -  |
**408** | Timeout |  -  |
**410** | Gone |  -  |
**415** | Unsupported media type |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**501** | Not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletes_file**
> deletes_file(file_uid)

Delete file

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)


# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrasetms_client.FileApi(api_client)
    file_uid = 'file_uid_example' # str | 

    try:
        # Delete file
        api_instance.deletes_file(file_uid)
    except Exception as e:
        print("Exception when calling FileApi->deletes_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad request |  -  |
**401** | Not authorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**405** | Method not allowed |  -  |
**408** | Timeout |  -  |
**410** | Gone |  -  |
**415** | Unsupported media type |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**501** | Not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_json**
> UploadedFileDto get_file_json(file_uid)

Get file

Get uploaded file as <b>octet-stream</b> or as <b>json</b> based on 'Accept' header

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.uploaded_file_dto import UploadedFileDto
from phrasetms_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)


# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrasetms_client.FileApi(api_client)
    file_uid = 'file_uid_example' # str | 

    try:
        # Get file
        api_response = api_instance.get_file_json(file_uid)
        print("The response of FileApi->get_file_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->get_file_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_uid** | **str**|  | 

### Return type

[**UploadedFileDto**](UploadedFileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**401** | Not authorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**405** | Method not allowed |  -  |
**408** | Timeout |  -  |
**410** | Gone |  -  |
**415** | Unsupported media type |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**501** | Not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> PageDtoUploadedFileDto get_files(page_number=page_number, page_size=page_size, name=name, types=types, created_by=created_by, bigger_than=bigger_than)

List files

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_uploaded_file_dto import PageDtoUploadedFileDto
from phrasetms_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)


# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrasetms_client.FileApi(api_client)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    name = 'name_example' # str |  (optional)
    types = ['types_example'] # List[str] |  (optional)
    created_by = 56 # int |  (optional)
    bigger_than = 56 # int | Size in bytes (optional)

    try:
        # List files
        api_response = api_instance.get_files(page_number=page_number, page_size=page_size, name=name, types=types, created_by=created_by, bigger_than=bigger_than)
        print("The response of FileApi->get_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->get_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **name** | **str**|  | [optional] 
 **types** | [**List[str]**](str.md)|  | [optional] 
 **created_by** | **int**|  | [optional] 
 **bigger_than** | **int**| Size in bytes | [optional] 

### Return type

[**PageDtoUploadedFileDto**](PageDtoUploadedFileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**401** | Not authorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**405** | Method not allowed |  -  |
**408** | Timeout |  -  |
**410** | Gone |  -  |
**415** | Unsupported media type |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**501** | Not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

