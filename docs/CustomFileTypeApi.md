# phrasetms_client.CustomFileTypeApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_file_types**](CustomFileTypeApi.md#create_custom_file_types) | **POST** /api2/v1/customFileTypes | Create custom file type
[**delete_batch_custom_file_type**](CustomFileTypeApi.md#delete_batch_custom_file_type) | **DELETE** /api2/v1/customFileTypes | Delete multiple Custom file type
[**delete_custom_file_type**](CustomFileTypeApi.md#delete_custom_file_type) | **DELETE** /api2/v1/customFileTypes/{customFileTypeUid} | Delete Custom file type
[**get_all_custom_file_type**](CustomFileTypeApi.md#get_all_custom_file_type) | **GET** /api2/v1/customFileTypes | Get All Custom file type
[**get_custom_file_type**](CustomFileTypeApi.md#get_custom_file_type) | **GET** /api2/v1/customFileTypes/{customFileTypeUid} | Get Custom file type
[**update_custom_file_type**](CustomFileTypeApi.md#update_custom_file_type) | **PUT** /api2/v1/customFileTypes/{customFileTypeUid} | Update Custom file type


# **create_custom_file_types**
> CustomFileTypeDto create_custom_file_types(body=body)

Create custom file type

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.create_custom_file_type_dto import CreateCustomFileTypeDto
from phrasetms_client.models.custom_file_type_dto import CustomFileTypeDto
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
    api_instance = phrasetms_client.CustomFileTypeApi(api_client)
    body = phrasetms_client.CreateCustomFileTypeDto() # CreateCustomFileTypeDto |  (optional)

    try:
        # Create custom file type
        api_response = api_instance.create_custom_file_types(body=body)
        print("The response of CustomFileTypeApi->create_custom_file_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFileTypeApi->create_custom_file_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomFileTypeDto**](CreateCustomFileTypeDto.md)|  | [optional] 

### Return type

[**CustomFileTypeDto**](CustomFileTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **delete_batch_custom_file_type**
> delete_batch_custom_file_type(body=body)

Delete multiple Custom file type

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.delete_custom_file_type_dto import DeleteCustomFileTypeDto
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
    api_instance = phrasetms_client.CustomFileTypeApi(api_client)
    body = phrasetms_client.DeleteCustomFileTypeDto() # DeleteCustomFileTypeDto |  (optional)

    try:
        # Delete multiple Custom file type
        api_instance.delete_batch_custom_file_type(body=body)
    except Exception as e:
        print("Exception when calling CustomFileTypeApi->delete_batch_custom_file_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteCustomFileTypeDto**](DeleteCustomFileTypeDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
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

# **delete_custom_file_type**
> delete_custom_file_type(custom_file_type_uid)

Delete Custom file type

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
    api_instance = phrasetms_client.CustomFileTypeApi(api_client)
    custom_file_type_uid = 'custom_file_type_uid_example' # str | 

    try:
        # Delete Custom file type
        api_instance.delete_custom_file_type(custom_file_type_uid)
    except Exception as e:
        print("Exception when calling CustomFileTypeApi->delete_custom_file_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_file_type_uid** | **str**|  | 

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
**204** | Deleted |  -  |
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

# **get_all_custom_file_type**
> PageDtoCustomFileTypeDto get_all_custom_file_type(page_number=page_number, page_size=page_size)

Get All Custom file type

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_custom_file_type_dto import PageDtoCustomFileTypeDto
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
    api_instance = phrasetms_client.CustomFileTypeApi(api_client)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # Get All Custom file type
        api_response = api_instance.get_all_custom_file_type(page_number=page_number, page_size=page_size)
        print("The response of CustomFileTypeApi->get_all_custom_file_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFileTypeApi->get_all_custom_file_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoCustomFileTypeDto**](PageDtoCustomFileTypeDto.md)

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

# **get_custom_file_type**
> CustomFileTypeDto get_custom_file_type(custom_file_type_uid)

Get Custom file type

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.custom_file_type_dto import CustomFileTypeDto
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
    api_instance = phrasetms_client.CustomFileTypeApi(api_client)
    custom_file_type_uid = 'custom_file_type_uid_example' # str | 

    try:
        # Get Custom file type
        api_response = api_instance.get_custom_file_type(custom_file_type_uid)
        print("The response of CustomFileTypeApi->get_custom_file_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFileTypeApi->get_custom_file_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_file_type_uid** | **str**|  | 

### Return type

[**CustomFileTypeDto**](CustomFileTypeDto.md)

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

# **update_custom_file_type**
> CustomFileTypeDto update_custom_file_type(custom_file_type_uid, body=body)

Update Custom file type

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.custom_file_type_dto import CustomFileTypeDto
from phrasetms_client.models.update_custom_file_type_dto import UpdateCustomFileTypeDto
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
    api_instance = phrasetms_client.CustomFileTypeApi(api_client)
    custom_file_type_uid = 'custom_file_type_uid_example' # str | 
    body = phrasetms_client.UpdateCustomFileTypeDto() # UpdateCustomFileTypeDto |  (optional)

    try:
        # Update Custom file type
        api_response = api_instance.update_custom_file_type(custom_file_type_uid, body=body)
        print("The response of CustomFileTypeApi->update_custom_file_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFileTypeApi->update_custom_file_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_file_type_uid** | **str**|  | 
 **body** | [**UpdateCustomFileTypeDto**](UpdateCustomFileTypeDto.md)|  | [optional] 

### Return type

[**CustomFileTypeDto**](CustomFileTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

