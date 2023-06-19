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
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WorkflowStepApi()
body = phrasetms_client.CreateWorkflowStepDto() # CreateWorkflowStepDto |  (optional)

try:
    # Create workflow step
    api_response = api_instance.create_wf_step(body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_wf_step**
> WorkflowStepDto edit_wf_step(workflow_step_uid, body=body)

Edit workflow step

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WorkflowStepApi()
workflow_step_uid = 'workflow_step_uid_example' # str | 
body = phrasetms_client.EditWorkflowStepDto() # EditWorkflowStepDto |  (optional)

try:
    # Edit workflow step
    api_response = api_instance.edit_wf_step(workflow_step_uid, body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wf_steps**
> PageDtoWorkflowStepDto list_wf_steps(page_number=page_number, page_size=page_size, sort=sort, order=order, name=name, abbr=abbr)

List workflow steps

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WorkflowStepApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
sort = 'ID' # str |  (optional) (default to ID)
order = 'ASC' # str |  (optional) (default to ASC)
name = 'name_example' # str | Name of the workflow step (optional)
abbr = 'abbr_example' # str | Abbreviation of workflow step (optional)

try:
    # List workflow steps
    api_response = api_instance.list_wf_steps(page_number=page_number, page_size=page_size, sort=sort, order=order, name=name, abbr=abbr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowStepApi->list_wf_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **sort** | **str**|  | [optional] [default to ID]
 **order** | **str**|  | [optional] [default to ASC]
 **name** | **str**| Name of the workflow step | [optional] 
 **abbr** | **str**| Abbreviation of workflow step | [optional] 

### Return type

[**PageDtoWorkflowStepDto**](PageDtoWorkflowStepDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_steps**
> PageDtoWorkflowStepReference list_workflow_steps(user_uid, status=status, project_uid=project_uid, target_lang=target_lang, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)

List assigned workflow steps

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WorkflowStepApi()
user_uid = 'user_uid_example' # str | 
status = ['status_example'] # list[str] |  (optional)
project_uid = 'project_uid_example' # str |  (optional)
target_lang = ['target_lang_example'] # list[str] |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned workflow steps
    api_response = api_instance.list_workflow_steps(user_uid, status=status, project_uid=project_uid, target_lang=target_lang, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowStepApi->list_workflow_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **project_uid** | **str**|  | [optional] 
 **target_lang** | [**list[str]**](str.md)|  | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

