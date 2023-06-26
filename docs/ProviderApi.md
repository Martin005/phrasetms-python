# phrasetms_client.ProviderApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_assignments**](ProviderApi.md#get_project_assignments) | **GET** /api2/v1/projects/{projectUid}/providers | List project providers
[**list_providers3**](ProviderApi.md#list_providers3) | **POST** /api2/v2/projects/{projectUid}/providers/suggest | Get suggested providers
[**list_providers4**](ProviderApi.md#list_providers4) | **POST** /api2/v2/projects/{projectUid}/jobs/{jobUid}/providers/suggest | Get suggested providers


# **get_project_assignments**
> PageDtoProviderReference get_project_assignments(project_uid, provider_name=provider_name, page_number=page_number, page_size=page_size)

List project providers

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_provider_reference import PageDtoProviderReference
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
    api_instance = phrasetms_client.ProviderApi(api_client)
    project_uid = 'project_uid_example' # str | 
    provider_name = 'provider_name_example' # str |  (optional)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List project providers
        api_response = api_instance.get_project_assignments(project_uid, provider_name=provider_name, page_number=page_number, page_size=page_size)
        print("The response of ProviderApi->get_project_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->get_project_assignments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **provider_name** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoProviderReference**](PageDtoProviderReference.md)

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

# **list_providers3**
> ProviderListDtoV2 list_providers3(project_uid)

Get suggested providers

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.provider_list_dto_v2 import ProviderListDtoV2
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
    api_instance = phrasetms_client.ProviderApi(api_client)
    project_uid = 'project_uid_example' # str | 

    try:
        # Get suggested providers
        api_response = api_instance.list_providers3(project_uid)
        print("The response of ProviderApi->list_providers3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->list_providers3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**ProviderListDtoV2**](ProviderListDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

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

# **list_providers4**
> ProviderListDtoV2 list_providers4(project_uid, job_uid)

Get suggested providers

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.provider_list_dto_v2 import ProviderListDtoV2
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
    api_instance = phrasetms_client.ProviderApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get suggested providers
        api_response = api_instance.list_providers4(project_uid, job_uid)
        print("The response of ProviderApi->list_providers4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderApi->list_providers4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**ProviderListDtoV2**](ProviderListDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

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

