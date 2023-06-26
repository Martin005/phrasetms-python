# phrasetms_client.AdditionalWorkflowStepApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_awf_step**](AdditionalWorkflowStepApi.md#create_awf_step) | **POST** /api2/v1/additionalWorkflowSteps | Create additional workflow step
[**delete_awf_step**](AdditionalWorkflowStepApi.md#delete_awf_step) | **DELETE** /api2/v1/additionalWorkflowSteps/{id} | Delete additional workflow step
[**list_awf_steps**](AdditionalWorkflowStepApi.md#list_awf_steps) | **GET** /api2/v1/additionalWorkflowSteps | List additional workflow steps


# **create_awf_step**
> AdditionalWorkflowStepDto create_awf_step(body=body)

Create additional workflow step

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.additional_workflow_step_dto import AdditionalWorkflowStepDto
from phrasetms_client.models.additional_workflow_step_request_dto import AdditionalWorkflowStepRequestDto
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
    api_instance = phrasetms_client.AdditionalWorkflowStepApi(api_client)
    body = phrasetms_client.AdditionalWorkflowStepRequestDto() # AdditionalWorkflowStepRequestDto |  (optional)

    try:
        # Create additional workflow step
        api_response = api_instance.create_awf_step(body=body)
        print("The response of AdditionalWorkflowStepApi->create_awf_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdditionalWorkflowStepApi->create_awf_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdditionalWorkflowStepRequestDto**](AdditionalWorkflowStepRequestDto.md)|  | [optional] 

### Return type

[**AdditionalWorkflowStepDto**](AdditionalWorkflowStepDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

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

# **delete_awf_step**
> delete_awf_step(id)

Delete additional workflow step

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
    api_instance = phrasetms_client.AdditionalWorkflowStepApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete additional workflow step
        api_instance.delete_awf_step(id)
    except Exception as e:
        print("Exception when calling AdditionalWorkflowStepApi->delete_awf_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **list_awf_steps**
> PageDtoAdditionalWorkflowStepDto list_awf_steps(page_number=page_number, page_size=page_size, name=name)

List additional workflow steps

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_additional_workflow_step_dto import PageDtoAdditionalWorkflowStepDto
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
    api_instance = phrasetms_client.AdditionalWorkflowStepApi(api_client)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    name = 'name_example' # str | Name of the additional workflow step to filter (optional)

    try:
        # List additional workflow steps
        api_response = api_instance.list_awf_steps(page_number=page_number, page_size=page_size, name=name)
        print("The response of AdditionalWorkflowStepApi->list_awf_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdditionalWorkflowStepApi->list_awf_steps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **name** | **str**| Name of the additional workflow step to filter | [optional] 

### Return type

[**PageDtoAdditionalWorkflowStepDto**](PageDtoAdditionalWorkflowStepDto.md)

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

