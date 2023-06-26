# phrasetms_client.MappingApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mapping_for_task**](MappingApi.md#get_mapping_for_task) | **GET** /api2/v1/mappings/tasks/{id} | Returns mapping for taskId (mxliff)


# **get_mapping_for_task**
> TaskMappingDto get_mapping_for_task(id, workflow_level=workflow_level)

Returns mapping for taskId (mxliff)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.task_mapping_dto import TaskMappingDto
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
    api_instance = phrasetms_client.MappingApi(api_client)
    id = 'id_example' # str | 
    workflow_level = 1 # int |  (optional) (default to 1)

    try:
        # Returns mapping for taskId (mxliff)
        api_response = api_instance.get_mapping_for_task(id, workflow_level=workflow_level)
        print("The response of MappingApi->get_mapping_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->get_mapping_for_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **workflow_level** | **int**|  | [optional] [default to 1]

### Return type

[**TaskMappingDto**](TaskMappingDto.md)

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

