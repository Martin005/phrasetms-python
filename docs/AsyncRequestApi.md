# phrasetms_client.AsyncRequestApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_async_request**](AsyncRequestApi.md#get_async_request) | **GET** /api2/v1/async/{asyncRequestId} | Get asynchronous request
[**get_current_limit_status**](AsyncRequestApi.md#get_current_limit_status) | **GET** /api2/v1/async/status | Get current limits
[**list_pending_requests**](AsyncRequestApi.md#list_pending_requests) | **GET** /api2/v1/async | List pending requests


# **get_async_request**
> AsyncRequestDto get_async_request(async_request_id)

Get asynchronous request

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_request_dto import AsyncRequestDto
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
    api_instance = phrasetms_client.AsyncRequestApi(api_client)
    async_request_id = 56 # int | 

    try:
        # Get asynchronous request
        api_response = api_instance.get_async_request(async_request_id)
        print("The response of AsyncRequestApi->get_async_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsyncRequestApi->get_async_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_request_id** | **int**|  | 

### Return type

[**AsyncRequestDto**](AsyncRequestDto.md)

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

# **get_current_limit_status**
> AsyncRequestStatusDto get_current_limit_status()

Get current limits

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_request_status_dto import AsyncRequestStatusDto
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
    api_instance = phrasetms_client.AsyncRequestApi(api_client)

    try:
        # Get current limits
        api_response = api_instance.get_current_limit_status()
        print("The response of AsyncRequestApi->get_current_limit_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsyncRequestApi->get_current_limit_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AsyncRequestStatusDto**](AsyncRequestStatusDto.md)

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

# **list_pending_requests**
> PageDtoAsyncRequestDto list_pending_requests(all=all, page_number=page_number, page_size=page_size)

List pending requests

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_async_request_dto import PageDtoAsyncRequestDto
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
    api_instance = phrasetms_client.AsyncRequestApi(api_client)
    all = False # bool | Pending requests for organization instead of current user. Only for ADMIN. (optional) (default to False)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List pending requests
        api_response = api_instance.list_pending_requests(all=all, page_number=page_number, page_size=page_size)
        print("The response of AsyncRequestApi->list_pending_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsyncRequestApi->list_pending_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Pending requests for organization instead of current user. Only for ADMIN. | [optional] [default to False]
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoAsyncRequestDto**](PageDtoAsyncRequestDto.md)

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

