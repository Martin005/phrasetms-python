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
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AdditionalWorkflowStepApi()
body = phrasetms_client.AdditionalWorkflowStepRequestDto() # AdditionalWorkflowStepRequestDto |  (optional)

try:
    # Create additional workflow step
    api_response = api_instance.create_awf_step(body=body)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_awf_step**
> delete_awf_step(id)

Delete additional workflow step

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AdditionalWorkflowStepApi()
id = 'id_example' # str | 

try:
    # Delete additional workflow step
    api_instance.delete_awf_step(id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_awf_steps**
> PageDtoAdditionalWorkflowStepDto list_awf_steps(page_number=page_number, page_size=page_size, name=name)

List additional workflow steps

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AdditionalWorkflowStepApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
name = 'name_example' # str | Name of the additional workflow step to filter (optional)

try:
    # List additional workflow steps
    api_response = api_instance.list_awf_steps(page_number=page_number, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

