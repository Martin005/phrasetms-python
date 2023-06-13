<a id="__pageTop"></a>
# openapi_client.apis.tags.workflow_step_api.WorkflowStepApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wf_step**](#create_wf_step) | **post** /api2/v1/workflowSteps | Create workflow step
[**edit_wf_step**](#edit_wf_step) | **put** /api2/v1/workflowSteps/{workflowStepUid} | Edit workflow step
[**list_wf_steps**](#list_wf_steps) | **get** /api2/v1/workflowSteps | List workflow steps
[**list_workflow_steps**](#list_workflow_steps) | **get** /api2/v1/users/{userUid}/workflowSteps | List assigned workflow steps

# **create_wf_step**
<a id="create_wf_step"></a>
> WorkflowStepDto create_wf_step()

Create workflow step

### Example

```python
import openapi_client
from openapi_client.apis.tags import workflow_step_api
from openapi_client.model.workflow_step_dto import WorkflowStepDto
from openapi_client.model.create_workflow_step_dto import CreateWorkflowStepDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_step_api.WorkflowStepApi(api_client)

    # example passing only optional values
    body = CreateWorkflowStepDto(
        name="name_example",
        order=1,
        lqa_enabled=True,
        abbr="abbr_example",
    )
    try:
        # Create workflow step
        api_response = api_instance.create_wf_step(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WorkflowStepApi->create_wf_step: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateWorkflowStepDto**](../../models/CreateWorkflowStepDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_wf_step.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_wf_step.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_wf_step.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_wf_step.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_wf_step.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_wf_step.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_wf_step.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_wf_step.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_wf_step.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_wf_step.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_wf_step.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_wf_step.ApiResponseFor501) | Not implemented

#### create_wf_step.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WorkflowStepDto**](../../models/WorkflowStepDto.md) |  | 


#### create_wf_step.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_wf_step.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_wf_step.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_wf_step.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_wf_step.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_wf_step.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_wf_step.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_wf_step.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_wf_step.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_wf_step.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_wf_step.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_wf_step**
<a id="edit_wf_step"></a>
> WorkflowStepDto edit_wf_step(workflow_step_uid)

Edit workflow step

### Example

```python
import openapi_client
from openapi_client.apis.tags import workflow_step_api
from openapi_client.model.workflow_step_dto import WorkflowStepDto
from openapi_client.model.edit_workflow_step_dto import EditWorkflowStepDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_step_api.WorkflowStepApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'workflowStepUid': "workflowStepUid_example",
    }
    try:
        # Edit workflow step
        api_response = api_instance.edit_wf_step(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WorkflowStepApi->edit_wf_step: %s\n" % e)

    # example passing only optional values
    path_params = {
        'workflowStepUid': "workflowStepUid_example",
    }
    body = EditWorkflowStepDto(
        name="name_example",
        order=1,
        lqa_enabled=True,
        abbr="abbr_example",
    )
    try:
        # Edit workflow step
        api_response = api_instance.edit_wf_step(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WorkflowStepApi->edit_wf_step: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditWorkflowStepDto**](../../models/EditWorkflowStepDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
workflowStepUid | WorkflowStepUidSchema | | 

# WorkflowStepUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_wf_step.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_wf_step.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_wf_step.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_wf_step.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_wf_step.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_wf_step.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_wf_step.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_wf_step.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_wf_step.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_wf_step.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_wf_step.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_wf_step.ApiResponseFor501) | Not implemented

#### edit_wf_step.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WorkflowStepDto**](../../models/WorkflowStepDto.md) |  | 


#### edit_wf_step.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_wf_step.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_wf_step.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_wf_step.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_wf_step.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_wf_step.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_wf_step.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_wf_step.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_wf_step.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_wf_step.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_wf_step.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_wf_steps**
<a id="list_wf_steps"></a>
> PageDtoWorkflowStepDto list_wf_steps()

List workflow steps

### Example

```python
import openapi_client
from openapi_client.apis.tags import workflow_step_api
from openapi_client.model.page_dto_workflow_step_dto import PageDtoWorkflowStepDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_step_api.WorkflowStepApi(api_client)

    # example passing only optional values
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
        'sort': "ID",
        'order': "ASC",
        'name': "name_example",
        'abbr': "abbr_example",
    }
    try:
        # List workflow steps
        api_response = api_instance.list_wf_steps(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WorkflowStepApi->list_wf_steps: %s\n" % e)
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
sort | SortSchema | | optional
order | OrderSchema | | optional
name | NameSchema | | optional
abbr | AbbrSchema | | optional


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

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ID", "NAME", "ORDER", "ABBR", ] if omitted the server will use the default value of "ID"

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "ASC"

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AbbrSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_wf_steps.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_wf_steps.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_wf_steps.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_wf_steps.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_wf_steps.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_wf_steps.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_wf_steps.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_wf_steps.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_wf_steps.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_wf_steps.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_wf_steps.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_wf_steps.ApiResponseFor501) | Not implemented

#### list_wf_steps.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoWorkflowStepDto**](../../models/PageDtoWorkflowStepDto.md) |  | 


#### list_wf_steps.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_wf_steps.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_wf_steps.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_wf_steps.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_wf_steps.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_wf_steps.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_wf_steps.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_wf_steps.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_wf_steps.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_wf_steps.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_wf_steps.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_workflow_steps**
<a id="list_workflow_steps"></a>
> PageDtoWorkflowStepReference list_workflow_steps(user_uid)

List assigned workflow steps

### Example

```python
import openapi_client
from openapi_client.apis.tags import workflow_step_api
from openapi_client.model.page_dto_workflow_step_reference import PageDtoWorkflowStepReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_step_api.WorkflowStepApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
    }
    try:
        # List assigned workflow steps
        api_response = api_instance.list_workflow_steps(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WorkflowStepApi->list_workflow_steps: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
        'status': [
        "NEW"
    ],
        'projectUid': "projectUid_example",
        'targetLang': [
        "targetLang_example"
    ],
        'dueInHours': -1,
        'filename': "filename_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List assigned workflow steps
        api_response = api_instance.list_workflow_steps(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling WorkflowStepApi->list_workflow_steps: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
status | StatusSchema | | optional
projectUid | ProjectUidSchema | | optional
targetLang | TargetLangSchema | | optional
dueInHours | DueInHoursSchema | | optional
filename | FilenameSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["NEW", "ACCEPTED", "DECLINED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TargetLangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# DueInHoursSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# FilenameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userUid | UserUidSchema | | 

# UserUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_workflow_steps.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_workflow_steps.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_workflow_steps.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_workflow_steps.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_workflow_steps.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_workflow_steps.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_workflow_steps.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_workflow_steps.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_workflow_steps.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_workflow_steps.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_workflow_steps.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_workflow_steps.ApiResponseFor501) | Not implemented

#### list_workflow_steps.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoWorkflowStepReference**](../../models/PageDtoWorkflowStepReference.md) |  | 


#### list_workflow_steps.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_workflow_steps.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_workflow_steps.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_workflow_steps.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_workflow_steps.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_workflow_steps.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_workflow_steps.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_workflow_steps.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_workflow_steps.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_workflow_steps.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_workflow_steps.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

