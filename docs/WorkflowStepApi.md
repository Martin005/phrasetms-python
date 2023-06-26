# phrasetms_client.WorkflowStepApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wf_step**](WorkflowStepApi.md#create_wf_step) | **POST** /api2/v1/workflowSteps | Create workflow step
[**edit_wf_step**](WorkflowStepApi.md#edit_wf_step) | **PUT** /api2/v1/workflowSteps/{workflowStepUid} | Edit workflow step
[**list_wf_steps**](WorkflowStepApi.md#list_wf_steps) | **GET** /api2/v1/workflowSteps | List workflow steps
[**list_workflow_steps**](WorkflowStepApi.md#list_workflow_steps) | **GET** /api2/v1/users/{userUid}/workflowSteps | List assigned workflow steps


# **create_wf_step**
> WorkflowStepDto create_wf_step(body=body)

Create workflow step

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.create_workflow_step_dto import CreateWorkflowStepDto
from phrasetms_client.models.workflow_step_dto import WorkflowStepDto
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
    api_instance = phrasetms_client.WorkflowStepApi(api_client)
    body = phrasetms_client.CreateWorkflowStepDto() # CreateWorkflowStepDto |  (optional)

    try:
        # Create workflow step
        api_response = api_instance.create_wf_step(body=body)
        print("The response of WorkflowStepApi->create_wf_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowStepApi->create_wf_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWorkflowStepDto**](CreateWorkflowStepDto.md)|  | [optional] 

### Return type

[**WorkflowStepDto**](WorkflowStepDto.md)

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

# **edit_wf_step**
> WorkflowStepDto edit_wf_step(workflow_step_uid, body=body)

Edit workflow step

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.edit_workflow_step_dto import EditWorkflowStepDto
from phrasetms_client.models.workflow_step_dto import WorkflowStepDto
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
    api_instance = phrasetms_client.WorkflowStepApi(api_client)
    workflow_step_uid = 'workflow_step_uid_example' # str | 
    body = phrasetms_client.EditWorkflowStepDto() # EditWorkflowStepDto |  (optional)

    try:
        # Edit workflow step
        api_response = api_instance.edit_wf_step(workflow_step_uid, body=body)
        print("The response of WorkflowStepApi->edit_wf_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowStepApi->edit_wf_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_step_uid** | **str**|  | 
 **body** | [**EditWorkflowStepDto**](EditWorkflowStepDto.md)|  | [optional] 

### Return type

[**WorkflowStepDto**](WorkflowStepDto.md)

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

# **list_wf_steps**
> PageDtoWorkflowStepDto list_wf_steps(page_number=page_number, page_size=page_size, sort=sort, order=order, name=name, abbr=abbr)

List workflow steps

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_workflow_step_dto import PageDtoWorkflowStepDto
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
    api_instance = phrasetms_client.WorkflowStepApi(api_client)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    sort = 'ID' # str |  (optional) (default to 'ID')
    order = 'ASC' # str |  (optional) (default to 'ASC')
    name = 'name_example' # str | Name of the workflow step (optional)
    abbr = 'abbr_example' # str | Abbreviation of workflow step (optional)

    try:
        # List workflow steps
        api_response = api_instance.list_wf_steps(page_number=page_number, page_size=page_size, sort=sort, order=order, name=name, abbr=abbr)
        print("The response of WorkflowStepApi->list_wf_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowStepApi->list_wf_steps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **sort** | **str**|  | [optional] [default to &#39;ID&#39;]
 **order** | **str**|  | [optional] [default to &#39;ASC&#39;]
 **name** | **str**| Name of the workflow step | [optional] 
 **abbr** | **str**| Abbreviation of workflow step | [optional] 

### Return type

[**PageDtoWorkflowStepDto**](PageDtoWorkflowStepDto.md)

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

# **list_workflow_steps**
> PageDtoWorkflowStepReference list_workflow_steps(user_uid, status=status, project_uid=project_uid, target_lang=target_lang, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)

List assigned workflow steps

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_workflow_step_reference import PageDtoWorkflowStepReference
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
    api_instance = phrasetms_client.WorkflowStepApi(api_client)
    user_uid = 'user_uid_example' # str | 
    status = ['status_example'] # List[str] |  (optional)
    project_uid = 'project_uid_example' # str |  (optional)
    target_lang = ['target_lang_example'] # List[str] |  (optional)
    due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
    filename = 'filename_example' # str |  (optional)
    page_number = 0 # int |  (optional) (default to 0)
    page_size = 50 # int |  (optional) (default to 50)

    try:
        # List assigned workflow steps
        api_response = api_instance.list_workflow_steps(user_uid, status=status, project_uid=project_uid, target_lang=target_lang, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)
        print("The response of WorkflowStepApi->list_workflow_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowStepApi->list_workflow_steps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 
 **status** | [**List[str]**](str.md)|  | [optional] 
 **project_uid** | **str**|  | [optional] 
 **target_lang** | [**List[str]**](str.md)|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoWorkflowStepReference**](PageDtoWorkflowStepReference.md)

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

