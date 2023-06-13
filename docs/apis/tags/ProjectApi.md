<a id="__pageTop"></a>
# openapi_client.apis.tags.project_api.ProjectApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_target_language_to_project**](#add_target_language_to_project) | **post** /api2/v1/projects/{projectUid}/targetLangs | Add target languages
[**add_workflow_steps**](#add_workflow_steps) | **post** /api2/v1/projects/{projectUid}/workflowSteps | Add workflow steps
[**assign_linguists_from_template**](#assign_linguists_from_template) | **post** /api2/v1/projects/{projectUid}/applyTemplate/{templateUid}/assignProviders | Assigns providers from template
[**assign_linguists_from_template_to_job_parts**](#assign_linguists_from_template_to_job_parts) | **post** /api2/v1/projects/{projectUid}/applyTemplate/{templateUid}/assignProviders/forJobParts | Assigns providers from template (specific jobs)
[**assign_vendor_to_project**](#assign_vendor_to_project) | **post** /api2/v1/projects/{projectUid}/assignVendor | Assign vendor
[**assignable_templates**](#assignable_templates) | **get** /api2/v1/projects/{projectUid}/assignableTemplates | List assignable templates
[**clone_project**](#clone_project) | **post** /api2/v1/projects/{projectUid}/clone | Clone project
[**create_custom_fields**](#create_custom_fields) | **post** /api2/v1/projects/{projectUid}/customFields | Create custom field instances
[**create_project_from_template_v2**](#create_project_from_template_v2) | **post** /api2/v2/projects/applyTemplate/{templateUid} | Create project from template
[**create_project_from_template_v2_async**](#create_project_from_template_v2_async) | **post** /api2/v2/projects/applyTemplate/async/{templateUid} | Create project from template (async)
[**create_project_v3**](#create_project_v3) | **post** /api2/v3/projects | Create project
[**delete_custom_field1**](#delete_custom_field1) | **delete** /api2/v1/projects/{projectUid}/customFields/{fieldInstanceUid} | Delete custom field of project
[**delete_project**](#delete_project) | **delete** /api2/v1/projects/{projectUid} | Delete project
[**edit_custom_field**](#edit_custom_field) | **put** /api2/v1/projects/{projectUid}/customFields/{fieldInstanceUid} | Edit custom field of project
[**edit_custom_fields**](#edit_custom_fields) | **put** /api2/v1/projects/{projectUid}/customFields | Edit custom fields of the project (batch)
[**edit_import_settings1**](#edit_import_settings1) | **put** /api2/v1/projects/{projectUid}/importSettings | Edit project import settings
[**edit_project_access_settings_v2**](#edit_project_access_settings_v2) | **put** /api2/v2/projects/{projectUid}/accessSettings | Edit access and security settings
[**edit_project_pre_translate_settings2**](#edit_project_pre_translate_settings2) | **put** /api2/v3/projects/{projectUid}/preTranslateSettings | Update Pre-translate settings
[**edit_project_v2**](#edit_project_v2) | **put** /api2/v2/projects/{projectUid} | Edit project
[**enabled_quality_checks**](#enabled_quality_checks) | **get** /api2/v1/projects/{projectUid}/qaSettingsChecks | Get QA checks
[**get_analyse_settings_for_project**](#get_analyse_settings_for_project) | **get** /api2/v1/projects/{projectUid}/analyseSettings | Get analyse settings
[**get_custom_field1**](#get_custom_field1) | **get** /api2/v1/projects/{projectUid}/customFields/{fieldInstanceUid} | Get custom field of project
[**get_custom_fields_page**](#get_custom_fields_page) | **get** /api2/v1/projects/{projectUid}/customFields | Get custom fields of project (page)
[**get_file_naming_settings**](#get_file_naming_settings) | **get** /api2/v1/projects/{projectUid}/fileNamingSettings | Get file naming settings for project
[**get_financial_settings**](#get_financial_settings) | **get** /api2/v1/projects/{projectUid}/financialSettings | Get financial settings
[**get_import_settings2**](#get_import_settings2) | **get** /api2/v1/projects/{projectUid}/importSettings | Get projects&#x27;s default import settings
[**get_mt_settings_for_project**](#get_mt_settings_for_project) | **get** /api2/v1/projects/{projectUid}/mtSettings | Get project machine translate settings
[**get_pre_translate_settings_for_project2**](#get_pre_translate_settings_for_project2) | **get** /api2/v3/projects/{projectUid}/preTranslateSettings | Get Pre-translate settings
[**get_project**](#get_project) | **get** /api2/v1/projects/{projectUid} | Get project
[**get_project_access_settings_v2**](#get_project_access_settings_v2) | **get** /api2/v2/projects/{projectUid}/accessSettings | Get access and security settings
[**get_project_assignments**](#get_project_assignments) | **get** /api2/v1/projects/{projectUid}/providers | List project providers
[**get_project_settings**](#get_project_settings) | **get** /api2/v1/projects/{projectUid}/lqaSettings | Get LQA settings
[**get_project_term_bases**](#get_project_term_bases) | **get** /api2/v1/projects/{projectUid}/termBases | Get term bases
[**get_project_trans_memories1**](#get_project_trans_memories1) | **get** /api2/v3/projects/{projectUid}/transMemories | Get translation memories
[**get_project_workflow_steps_v2**](#get_project_workflow_steps_v2) | **get** /api2/v2/projects/{projectUid}/workflowSteps | Get workflow steps
[**get_quotes_for_project**](#get_quotes_for_project) | **get** /api2/v1/projects/{projectUid}/quotes | List quotes
[**list_assigned_projects**](#list_assigned_projects) | **get** /api2/v1/users/{userUid}/projects | List assigned projects
[**list_by_project_v3**](#list_by_project_v3) | **get** /api2/v3/projects/{projectUid}/analyses | List analyses by project
[**list_projects**](#list_projects) | **get** /api2/v1/projects | List projects
[**list_providers3**](#list_providers3) | **post** /api2/v2/projects/{projectUid}/providers/suggest | Get suggested providers
[**patch_project**](#patch_project) | **patch** /api2/v1/projects/{projectUid} | Edit project
[**relevant_term_bases**](#relevant_term_bases) | **get** /api2/v1/projects/{projectUid}/termBases/relevant | List project relevant term bases
[**relevant_trans_memories1**](#relevant_trans_memories1) | **get** /api2/v1/projects/{projectUid}/transMemories/relevant | List project relevant translation memories
[**search_segment1**](#search_segment1) | **post** /api2/v1/projects/{projectUid}/transMemories/searchSegmentInProject | Search translation memory for segment in the project
[**set_financial_settings**](#set_financial_settings) | **put** /api2/v1/projects/{projectUid}/financialSettings | Edit financial settings
[**set_mt_settings_for_project**](#set_mt_settings_for_project) | **put** /api2/v1/projects/{projectUid}/mtSettings | Edit machine translate settings
[**set_mt_settings_per_language_for_project**](#set_mt_settings_per_language_for_project) | **put** /api2/v1/projects/{projectUid}/mtSettingsPerLanguage | Edit machine translate settings per language
[**set_project_qa_settings_v2**](#set_project_qa_settings_v2) | **put** /api2/v2/projects/{projectUid}/qaSettings | Edit quality assurance settings
[**set_project_status**](#set_project_status) | **post** /api2/v1/projects/{projectUid}/setStatus | Edit project status
[**set_project_term_bases**](#set_project_term_bases) | **put** /api2/v1/projects/{projectUid}/termBases | Edit term bases
[**set_project_trans_memories_v3**](#set_project_trans_memories_v3) | **put** /api2/v3/projects/{projectUid}/transMemories | Edit translation memories
[**update_file_naming_settings**](#update_file_naming_settings) | **put** /api2/v1/projects/{projectUid}/fileNamingSettings | Update file naming settings for project

# **add_target_language_to_project**
<a id="add_target_language_to_project"></a>
> add_target_language_to_project(project_uid)

Add target languages

Add target languages to project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.add_target_lang_dto import AddTargetLangDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Add target languages
        api_response = api_instance.add_target_language_to_project(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->add_target_language_to_project: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = AddTargetLangDto(
        target_langs=[
            "target_langs_example"
        ],
    )
    try:
        # Add target languages
        api_response = api_instance.add_target_language_to_project(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->add_target_language_to_project: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddTargetLangDto**](../../models/AddTargetLangDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#add_target_language_to_project.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#add_target_language_to_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#add_target_language_to_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#add_target_language_to_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#add_target_language_to_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#add_target_language_to_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#add_target_language_to_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#add_target_language_to_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#add_target_language_to_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#add_target_language_to_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#add_target_language_to_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#add_target_language_to_project.ApiResponseFor501) | Not implemented

#### add_target_language_to_project.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_language_to_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **add_workflow_steps**
<a id="add_workflow_steps"></a>
> add_workflow_steps(project_uid)

Add workflow steps

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.add_workflow_steps_dto import AddWorkflowStepsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Add workflow steps
        api_response = api_instance.add_workflow_steps(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->add_workflow_steps: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = AddWorkflowStepsDto(
        workflow_steps=[
            IdReference(
                id="id_example",
            )
        ],
    )
    try:
        # Add workflow steps
        api_response = api_instance.add_workflow_steps(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->add_workflow_steps: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddWorkflowStepsDto**](../../models/AddWorkflowStepsDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#add_workflow_steps.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#add_workflow_steps.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#add_workflow_steps.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#add_workflow_steps.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#add_workflow_steps.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#add_workflow_steps.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#add_workflow_steps.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#add_workflow_steps.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#add_workflow_steps.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#add_workflow_steps.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#add_workflow_steps.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#add_workflow_steps.ApiResponseFor501) | Not implemented

#### add_workflow_steps.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_workflow_steps.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **assign_linguists_from_template**
<a id="assign_linguists_from_template"></a>
> JobPartsDto assign_linguists_from_template(template_uidproject_uid)

Assigns providers from template

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.job_parts_dto import JobPartsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'templateUid': "templateUid_example",
        'projectUid': "projectUid_example",
    }
    try:
        # Assigns providers from template
        api_response = api_instance.assign_linguists_from_template(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->assign_linguists_from_template: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
templateUid | TemplateUidSchema | | 
projectUid | ProjectUidSchema | | 

# TemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#assign_linguists_from_template.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#assign_linguists_from_template.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#assign_linguists_from_template.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#assign_linguists_from_template.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#assign_linguists_from_template.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#assign_linguists_from_template.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#assign_linguists_from_template.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#assign_linguists_from_template.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#assign_linguists_from_template.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#assign_linguists_from_template.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#assign_linguists_from_template.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#assign_linguists_from_template.ApiResponseFor501) | Not implemented

#### assign_linguists_from_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobPartsDto**](../../models/JobPartsDto.md) |  | 


#### assign_linguists_from_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **assign_linguists_from_template_to_job_parts**
<a id="assign_linguists_from_template_to_job_parts"></a>
> JobPartsDto assign_linguists_from_template_to_job_parts(template_uidproject_uid)

Assigns providers from template (specific jobs)

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.job_part_references import JobPartReferences
from openapi_client.model.job_parts_dto import JobPartsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'templateUid': "templateUid_example",
        'projectUid': "projectUid_example",
    }
    try:
        # Assigns providers from template (specific jobs)
        api_response = api_instance.assign_linguists_from_template_to_job_parts(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->assign_linguists_from_template_to_job_parts: %s\n" % e)

    # example passing only optional values
    path_params = {
        'templateUid': "templateUid_example",
        'projectUid': "projectUid_example",
    }
    body = JobPartReferences(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
    )
    try:
        # Assigns providers from template (specific jobs)
        api_response = api_instance.assign_linguists_from_template_to_job_parts(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->assign_linguists_from_template_to_job_parts: %s\n" % e)
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
[**JobPartReferences**](../../models/JobPartReferences.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
templateUid | TemplateUidSchema | | 
projectUid | ProjectUidSchema | | 

# TemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#assign_linguists_from_template_to_job_parts.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#assign_linguists_from_template_to_job_parts.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#assign_linguists_from_template_to_job_parts.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#assign_linguists_from_template_to_job_parts.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#assign_linguists_from_template_to_job_parts.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#assign_linguists_from_template_to_job_parts.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#assign_linguists_from_template_to_job_parts.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#assign_linguists_from_template_to_job_parts.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#assign_linguists_from_template_to_job_parts.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#assign_linguists_from_template_to_job_parts.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#assign_linguists_from_template_to_job_parts.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#assign_linguists_from_template_to_job_parts.ApiResponseFor501) | Not implemented

#### assign_linguists_from_template_to_job_parts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobPartsDto**](../../models/JobPartsDto.md) |  | 


#### assign_linguists_from_template_to_job_parts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template_to_job_parts.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template_to_job_parts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template_to_job_parts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template_to_job_parts.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template_to_job_parts.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template_to_job_parts.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template_to_job_parts.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template_to_job_parts.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template_to_job_parts.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_linguists_from_template_to_job_parts.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **assign_vendor_to_project**
<a id="assign_vendor_to_project"></a>
> assign_vendor_to_project(project_uid)

Assign vendor

 To unassign Vendor from Project, use empty body: ``` {} ```     

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.assign_vendor_dto import AssignVendorDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Assign vendor
        api_response = api_instance.assign_vendor_to_project(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->assign_vendor_to_project: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = AssignVendorDto(
        vendor=IdReference(
            id="id_example",
        ),
        date_due="1970-01-01T00:00:00.00Z",
    )
    try:
        # Assign vendor
        api_response = api_instance.assign_vendor_to_project(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->assign_vendor_to_project: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssignVendorDto**](../../models/AssignVendorDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#assign_vendor_to_project.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#assign_vendor_to_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#assign_vendor_to_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#assign_vendor_to_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#assign_vendor_to_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#assign_vendor_to_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#assign_vendor_to_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#assign_vendor_to_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#assign_vendor_to_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#assign_vendor_to_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#assign_vendor_to_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#assign_vendor_to_project.ApiResponseFor501) | Not implemented

#### assign_vendor_to_project.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assign_vendor_to_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **assignable_templates**
<a id="assignable_templates"></a>
> AssignableTemplatesDto assignable_templates(project_uid)

List assignable templates

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.assignable_templates_dto import AssignableTemplatesDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # List assignable templates
        api_response = api_instance.assignable_templates(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->assignable_templates: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#assignable_templates.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#assignable_templates.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#assignable_templates.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#assignable_templates.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#assignable_templates.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#assignable_templates.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#assignable_templates.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#assignable_templates.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#assignable_templates.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#assignable_templates.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#assignable_templates.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#assignable_templates.ApiResponseFor501) | Not implemented

#### assignable_templates.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssignableTemplatesDto**](../../models/AssignableTemplatesDto.md) |  | 


#### assignable_templates.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assignable_templates.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assignable_templates.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assignable_templates.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assignable_templates.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assignable_templates.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assignable_templates.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assignable_templates.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assignable_templates.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assignable_templates.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### assignable_templates.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **clone_project**
<a id="clone_project"></a>
> AbstractProjectDto clone_project(project_uid)

Clone project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.abstract_project_dto import AbstractProjectDto
from openapi_client.model.clone_project_dto import CloneProjectDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Clone project
        api_response = api_instance.clone_project(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->clone_project: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = CloneProjectDto(
        name="name_example",
    )
    try:
        # Clone project
        api_response = api_instance.clone_project(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->clone_project: %s\n" % e)
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
[**CloneProjectDto**](../../models/CloneProjectDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#clone_project.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#clone_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#clone_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#clone_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#clone_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#clone_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#clone_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#clone_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#clone_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#clone_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#clone_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#clone_project.ApiResponseFor501) | Not implemented

#### clone_project.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AbstractProjectDto**](../../models/AbstractProjectDto.md) |  | 


#### clone_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clone_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clone_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clone_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clone_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clone_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clone_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clone_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clone_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clone_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clone_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_custom_fields**
<a id="create_custom_fields"></a>
> CustomFieldInstancesDto create_custom_fields(project_uid)

Create custom field instances

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.create_custom_field_instances_dto import CreateCustomFieldInstancesDto
from openapi_client.model.custom_field_instances_dto import CustomFieldInstancesDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Create custom field instances
        api_response = api_instance.create_custom_fields(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->create_custom_fields: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = CreateCustomFieldInstancesDto(
        custom_field_instances=[
            CreateCustomFieldInstanceDto(
                custom_field=UidReference(
                    uid="uid_example",
                ),
                selected_options=[
                    UidReference()
                ],
                value="value_example",
            )
        ],
    )
    try:
        # Create custom field instances
        api_response = api_instance.create_custom_fields(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->create_custom_fields: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateCustomFieldInstancesDto**](../../models/CreateCustomFieldInstancesDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_custom_fields.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#create_custom_fields.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_custom_fields.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_custom_fields.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_custom_fields.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_custom_fields.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_custom_fields.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_custom_fields.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_custom_fields.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_custom_fields.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_custom_fields.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_custom_fields.ApiResponseFor501) | Not implemented

#### create_custom_fields.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomFieldInstancesDto**](../../models/CustomFieldInstancesDto.md) |  | 


#### create_custom_fields.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_project_from_template_v2**
<a id="create_project_from_template_v2"></a>
> AbstractProjectDtoV2 create_project_from_template_v2(template_uid)

Create project from template

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.abstract_project_dto_v2 import AbstractProjectDtoV2
from openapi_client.model.create_project_from_template_v2_dto import CreateProjectFromTemplateV2Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'templateUid': "templateUid_example",
    }
    try:
        # Create project from template
        api_response = api_instance.create_project_from_template_v2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->create_project_from_template_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'templateUid': "templateUid_example",
    }
    body = CreateProjectFromTemplateV2Dto(
        name="name_example",
        source_lang="source_lang_example",
        target_langs=[
            "target_langs_example"
        ],
        workflow_steps=[
            IdReference(
                id="id_example",
            )
        ],
        date_due="1970-01-01T00:00:00.00Z",
        note="note_example",
,
,
,
,
,
    )
    try:
        # Create project from template
        api_response = api_instance.create_project_from_template_v2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->create_project_from_template_v2: %s\n" % e)
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
[**CreateProjectFromTemplateV2Dto**](../../models/CreateProjectFromTemplateV2Dto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
templateUid | TemplateUidSchema | | 

# TemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_project_from_template_v2.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_project_from_template_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_project_from_template_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_project_from_template_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_project_from_template_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_project_from_template_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_project_from_template_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_project_from_template_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_project_from_template_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_project_from_template_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_project_from_template_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_project_from_template_v2.ApiResponseFor501) | Not implemented

#### create_project_from_template_v2.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AbstractProjectDtoV2**](../../models/AbstractProjectDtoV2.md) |  | 


#### create_project_from_template_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_project_from_template_v2_async**
<a id="create_project_from_template_v2_async"></a>
> AsyncRequestWrapperV2Dto create_project_from_template_v2_async(template_uid)

Create project from template (async)

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.create_project_from_template_async_v2_dto import CreateProjectFromTemplateAsyncV2Dto
from openapi_client.model.async_request_wrapper_v2_dto import AsyncRequestWrapperV2Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'templateUid': "templateUid_example",
    }
    try:
        # Create project from template (async)
        api_response = api_instance.create_project_from_template_v2_async(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->create_project_from_template_v2_async: %s\n" % e)

    # example passing only optional values
    path_params = {
        'templateUid': "templateUid_example",
    }
    body = CreateProjectFromTemplateAsyncV2Dto(
        name="name_example",
        source_lang="source_lang_example",
        target_langs=[
            "target_langs_example"
        ],
        workflow_steps=[
            IdReference(
                id="id_example",
            )
        ],
        date_due="1970-01-01T00:00:00.00Z",
        note="note_example",
,
,
,
,
,
        callback_url="callback_url_example",
    )
    try:
        # Create project from template (async)
        api_response = api_instance.create_project_from_template_v2_async(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->create_project_from_template_v2_async: %s\n" % e)
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
[**CreateProjectFromTemplateAsyncV2Dto**](../../models/CreateProjectFromTemplateAsyncV2Dto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
templateUid | TemplateUidSchema | | 

# TemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#create_project_from_template_v2_async.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#create_project_from_template_v2_async.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_project_from_template_v2_async.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_project_from_template_v2_async.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_project_from_template_v2_async.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_project_from_template_v2_async.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_project_from_template_v2_async.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_project_from_template_v2_async.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_project_from_template_v2_async.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_project_from_template_v2_async.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_project_from_template_v2_async.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_project_from_template_v2_async.ApiResponseFor501) | Not implemented

#### create_project_from_template_v2_async.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsyncRequestWrapperV2Dto**](../../models/AsyncRequestWrapperV2Dto.md) |  | 


#### create_project_from_template_v2_async.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2_async.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2_async.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2_async.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2_async.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2_async.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2_async.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2_async.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2_async.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2_async.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_from_template_v2_async.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_project_v3**
<a id="create_project_v3"></a>
> AbstractProjectDtoV2 create_project_v3()

Create project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.create_project_v3_dto import CreateProjectV3Dto
from openapi_client.model.abstract_project_dto_v2 import AbstractProjectDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only optional values
    body = CreateProjectV3Dto(
        name="name_example",
        source_lang="source_lang_example",
        target_langs=[
            "target_langs_example"
        ],
        client=IdReference(
            id="id_example",
        ),
,
,
,
,
        purchase_order="purchase_order_example",
        workflow_steps=[
            IdReference()
        ],
        date_due="1970-01-01T00:00:00.00Z",
        note="note_example",
        lqa_profiles=[
            LqaProfilesForWsV2Dto(
                workflow_step=IdReference(),
                lqa_profile=UidReference(
                    uid="uid_example",
                ),
            )
        ],
        custom_fields=[
            CustomFieldInstanceApiDto(
                custom_field=UidReference(),
                selected_options=[
                    UidReference()
                ],
                value="value_example",
            )
        ],
        file_handover=True,
    )
    try:
        # Create project
        api_response = api_instance.create_project_v3(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->create_project_v3: %s\n" % e)
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
[**CreateProjectV3Dto**](../../models/CreateProjectV3Dto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_project_v3.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_project_v3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_project_v3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_project_v3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_project_v3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_project_v3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_project_v3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_project_v3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_project_v3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_project_v3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_project_v3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_project_v3.ApiResponseFor501) | Not implemented

#### create_project_v3.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AbstractProjectDtoV2**](../../models/AbstractProjectDtoV2.md) |  | 


#### create_project_v3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_v3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_v3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_v3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_v3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_v3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_v3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_v3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_v3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_v3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_v3.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_custom_field1**
<a id="delete_custom_field1"></a>
> delete_custom_field1(project_uidfield_instance_uid)

Delete custom field of project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'fieldInstanceUid': "fieldInstanceUid_example",
    }
    try:
        # Delete custom field of project
        api_response = api_instance.delete_custom_field1(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->delete_custom_field1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 
fieldInstanceUid | FieldInstanceUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldInstanceUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#delete_custom_field1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_custom_field1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_custom_field1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_custom_field1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_custom_field1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_custom_field1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_custom_field1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_custom_field1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_custom_field1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_custom_field1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_custom_field1.ApiResponseFor501) | Not implemented

#### delete_custom_field1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_project**
<a id="delete_project"></a>
> delete_project(project_uid)

Delete project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Delete project
        api_response = api_instance.delete_project(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'purge': False,
    }
    try:
        # Delete project
        api_response = api_instance.delete_project(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
purge | PurgeSchema | | optional


# PurgeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_project.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_project.ApiResponseFor501) | Not implemented

#### delete_project.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_custom_field**
<a id="edit_custom_field"></a>
> CustomFieldInstanceDto edit_custom_field(project_uidfield_instance_uid)

Edit custom field of project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.update_custom_field_instance_dto import UpdateCustomFieldInstanceDto
from openapi_client.model.custom_field_instance_dto import CustomFieldInstanceDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'fieldInstanceUid': "fieldInstanceUid_example",
    }
    try:
        # Edit custom field of project
        api_response = api_instance.edit_custom_field(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_custom_field: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'fieldInstanceUid': "fieldInstanceUid_example",
    }
    body = UpdateCustomFieldInstanceDto(
        selected_options=[
            UidReference(
                uid="uid_example",
            )
        ],
        value="value_example",
    )
    try:
        # Edit custom field of project
        api_response = api_instance.edit_custom_field(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_custom_field: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateCustomFieldInstanceDto**](../../models/UpdateCustomFieldInstanceDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 
fieldInstanceUid | FieldInstanceUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldInstanceUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_custom_field.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_custom_field.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_custom_field.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_custom_field.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_custom_field.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_custom_field.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_custom_field.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_custom_field.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_custom_field.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_custom_field.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_custom_field.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_custom_field.ApiResponseFor501) | Not implemented

#### edit_custom_field.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomFieldInstanceDto**](../../models/CustomFieldInstanceDto.md) |  | 


#### edit_custom_field.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_custom_fields**
<a id="edit_custom_fields"></a>
> CustomFieldInstancesDto edit_custom_fields(project_uid)

Edit custom fields of the project (batch)

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.update_custom_field_instances_dto import UpdateCustomFieldInstancesDto
from openapi_client.model.custom_field_instances_dto import CustomFieldInstancesDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit custom fields of the project (batch)
        api_response = api_instance.edit_custom_fields(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_custom_fields: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = UpdateCustomFieldInstancesDto(
        add_instances=[
            CreateCustomFieldInstanceDto(
                custom_field=UidReference(
                    uid="uid_example",
                ),
                selected_options=[
                    UidReference()
                ],
                value="value_example",
            )
        ],
,
        update_instances=[
            UpdateCustomFieldInstanceWithUidDto(
                custom_field_instance=UidReference(),
                custom_field=UidReference(),
,
                value="value_example",
            )
        ],
    )
    try:
        # Edit custom fields of the project (batch)
        api_response = api_instance.edit_custom_fields(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_custom_fields: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateCustomFieldInstancesDto**](../../models/UpdateCustomFieldInstancesDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_custom_fields.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_custom_fields.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_custom_fields.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_custom_fields.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_custom_fields.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_custom_fields.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_custom_fields.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_custom_fields.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_custom_fields.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_custom_fields.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_custom_fields.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_custom_fields.ApiResponseFor501) | Not implemented

#### edit_custom_fields.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomFieldInstancesDto**](../../models/CustomFieldInstancesDto.md) |  | 


#### edit_custom_fields.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_import_settings1**
<a id="edit_import_settings1"></a>
> FileImportSettingsDto edit_import_settings1(project_uid)

Edit project import settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.file_import_settings_create_dto import FileImportSettingsCreateDto
from openapi_client.model.file_import_settings_dto import FileImportSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit project import settings
        api_response = api_instance.edit_import_settings1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_import_settings1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = FileImportSettingsCreateDto(
        input_charset="input_charset_example",
        output_charset="output_charset_example",
        zip_charset="zip_charset_example",
        file_format="doc",
        autodetect_multilingual_files=True,
        target_length=True,
        target_length_max=1,
        target_length_percent=True,
        target_length_percent_value=3.14,
        segmentation_rule_id=1,
        target_segmentation_rule_id=1,
        android=AndroidSettingsDto(
            tag_regexp="tag_regexp_example",
            icu_sub_filter=True,
        ),
        csv=CsvSettingsDto(
            delimiter="delimiter_example",
            delimiter_type="TAB",
            html_sub_filter=True,
            tag_regexp="tag_regexp_example",
            import_columns="import_columns_example",
            context_note_columns="context_note_columns_example",
            context_key_column="context_key_column_example",
            max_len_column="max_len_column_example",
            import_rows="import_rows_example",
        ),
        dita=DitaSettingsDto(
            include_tags="include_tags_example",
            exclude_tags="exclude_tags_example",
            inline_tags="inline_tags_example",
            inline_tags_non_translatable="inline_tags_non_translatable_example",
            tag_regexp="tag_regexp_example",
        ),
,
        doc=DocSettingsDto(
            comments=True,
            index=True,
            other=True,
            tag_regexp="tag_regexp_example",
            hyperlink_target=True,
            join_similar_runs=True,
            target_font="target_font_example",
            properties=True,
            hidden=True,
            header_footer=True,
        ),
        html=HtmlSettingsDto(
            break_tag_creates_segment=True,
            unknown_tag_creates_tag=True,
            preserve_whitespace=True,
            import_comments=True,
            exclude_elements="exclude_elements_example",
            tag_regexp="tag_regexp_example",
            char_entities_to_tags="char_entities_to_tags_example",
            translate_meta_tag_regexp="translate_meta_tag_regexp_example",
            import_default_meta_tags=True,
            translatable_attributes="translatable_attributes_example",
            import_default_attributes=True,
            non_translatable_inline_elements="non_translatable_inline_elements_example",
            translatable_inline_elements="translatable_inline_elements_example",
            update_lang=True,
            escape_disabled=True,
        ),
        idml=IdmlSettingsDto(
            extract_notes=True,
            simplify_codes=True,
            extract_master_spreads=True,
            extract_locked_layers=True,
            extract_invisible_layers=True,
            extract_hidden_conditional_text=True,
            extract_hyperlinks=True,
            keep_kerning=True,
            keep_tracking=True,
            target_font="target_font_example",
            replace_font=True,
            remove_xml_elements=True,
            tag_regexp="tag_regexp_example",
            extract_cross_reference_formats=True,
            extract_variables=True,
        ),
        json=JsonSettingsDto(
            tag_regexp="tag_regexp_example",
            html_sub_filter=True,
            icu_sub_filter=True,
            exclude_key_regexp="exclude_key_regexp_example",
            include_key_regexp="include_key_regexp_example",
            context_note_path="context_note_path_example",
            max_len_path="max_len_path_example",
            context_key_path="context_key_path_example",
        ),
        mac=MacSettingsDto(
            html_subfilter=True,
            tag_regexp="tag_regexp_example",
            icu_sub_filter=True,
        ),
        md=MdSettingsDto(
            hard_line_breaks_segments=True,
            preserve_white_spaces=True,
            tag_regexp="tag_regexp_example",
            custom_elements="custom_elements_example",
            ignored_block_prefixes="ignored_block_prefixes_example",
            flavor="PLAIN",
            process_jekyll_front_matter=True,
            extract_code_blocks=True,
            not_escaped_characters="not_escaped_characters_example",
            exclude_code_elements=True,
        ),
        mif=MifSettingsDto(
            extract_body_pages=True,
            extract_reference_pages=True,
            extract_master_pages=True,
            extract_hidden_pages=True,
            extract_variables=True,
            extract_index_markers=True,
            extract_links=True,
            extract_x_ref_def=True,
            extract_pgf_num_format=True,
            extract_custom_reference_pages=True,
            extract_default_reference_pages=True,
            extract_used_variables=True,
            extract_hidden_cond_text=True,
            extract_used_x_ref_def=True,
            extract_used_pgf_num_format=True,
            tag_regexp="tag_regexp_example",
        ),
        multilingual_xls=MultilingualXlsSettingsDto(
            source_column="source_column_example",
            target_columns=dict(
                "key": "key_example",
            ),
            context_note_column="context_note_column_example",
            context_key_column="context_key_column_example",
            tag_regexp="tag_regexp_example",
            html_sub_filter=True,
            segmentation=True,
            import_rows="import_rows_example",
            max_len_column="max_len_column_example",
            non_empty_segment_action="NONE",
            save_confirmed_segments_to_tm=True,
        ),
        multilingual_csv=MultilingualCsvSettingsDto(
            source_columns="source_columns_example",
            target_columns="target_columns_example",
            context_note_columns="context_note_columns_example",
            context_key_columns="context_key_columns_example",
            tag_regexp="tag_regexp_example",
            html_sub_filter=True,
            segmentation=True,
            delimiter="delimiter_example",
            delimiter_type="TAB",
            import_rows="import_rows_example",
            max_len_columns="max_len_columns_example",
            all_target_columns=dict(),
            non_empty_segment_action="NONE",
            save_confirmed_segments_to_tm=True,
        ),
        multilingual_xml=MultilingualXmlSettingsDto(
            translatable_elements_x_path="translatable_elements_x_path_example",
            source_elements_x_path="source_elements_x_path_example",
            target_elements_x_paths=dict(
                "key": "key_example",
            ),
            inline_elements_non_translatable_x_path="inline_elements_non_translatable_x_path_example",
            tag_regexp="tag_regexp_example",
            segmentation=True,
            html_sub_filter=True,
            context_key_x_path="context_key_x_path_example",
            context_note_x_path="context_note_x_path_example",
            max_len_x_path="max_len_x_path_example",
            preserve_whitespace=True,
            preserve_char_entities="preserve_char_entities_example",
            xsl_url="xsl_url_example",
            xsl_file="xsl_file_example",
            non_empty_segment_action="NONE",
            save_confirmed_segments_to_tm=True,
            icu_sub_filter=True,
        ),
        pdf=PdfSettingsDto(
            filter="TRANS_PDF",
        ),
        php=PhpSettingsDto(
            tag_regexp="tag_regexp_example",
            html_sub_filter=True,
        ),
        po=PoSettingsDto(
            tag_regexp="tag_regexp_example",
            export_multiline=True,
            html_sub_filter=True,
            segment=True,
            markup_sub_filter_translatable="markup_sub_filter_translatable_example",
            markup_sub_filter_non_translatable="markup_sub_filter_non_translatable_example",
            save_confirmed_segments=True,
            import_set_segment_confirmed_when="FUZZY",
            import_set_segment_locked_when="FUZZY",
            export_confirmed_locked="FUZZY",
            export_confirmed_not_locked="FUZZY",
            export_not_confirmed_locked="FUZZY",
            export_not_confirmed_not_locked="FUZZY",
            icu_sub_filter=True,
        ),
        ppt=PptSettingsDto(
            hidden_slides=True,
            other=True,
            notes=True,
            master_slides=True,
        ),
        properties=PropertiesSettingsDto(
            tag_regexp="tag_regexp_example",
        ),
        psd=PsdSettingsDto(
            extract_hidden_layers=True,
            extract_locked_layers=True,
            tag_regexp="tag_regexp_example",
        ),
        quark_tag=QuarkTagSettingsDto(
            remove_kerning_tracking_tags=True,
            tag_regexp="tag_regexp_example",
        ),
        resx=ResxSettingsDto(
            tag_regexp="tag_regexp_example",
            html_sub_filter=True,
        ),
        sdl_xlf=SdlXlfSettingsDto(
            icu_sub_filter=True,
            skip_import_rules="skip_import_rules_example",
            import_as_confirmed_rules="import_as_confirmed_rules_example",
            import_as_locked_rules="import_as_locked_rules_example",
            export_attrs_when_confirmed_and_locked="export_attrs_when_confirmed_and_locked_example",
            export_attrs_when_confirmed_and_not_locked="export_attrs_when_confirmed_and_not_locked_example",
            export_attrs_when_not_confirmed_and_locked="export_attrs_when_not_confirmed_and_locked_example",
            export_attrs_when_not_confirmed_and_not_locked="export_attrs_when_not_confirmed_and_not_locked_example",
            save_confirmed_segments=True,
            tag_regexp="tag_regexp_example",
        ),
        tm_match=TMMatchSettingsDto(
            context_type="AUTO",
            prev_or_next_segment=True,
            penalize_multi_context_match=True,
            ignore_tag_metadata=True,
            metadata_priority=MetadataPrioritySettingsDto(
                prioritized_fields=[
                    MetadataField(
                        type="CLIENT",
                    )
                ],
            ),
        ),
        ttx=TtxSettingsDto(
            save_confirmed_segments=True,
        ),
        txt=TxtSettingsDto(
            tag_regexp="tag_regexp_example",
            translatable_text_regexp="translatable_text_regexp_example",
            context_key="context_key_example",
            regexp_capturing_groups=True,
        ),
        xlf2=Xlf2SettingsDto(
            icu_sub_filter=True,
            import_notes=True,
            save_confirmed_segments=True,
            segmentation=True,
            line_break_tags=True,
            preserve_whitespace=True,
            copy_source_to_target_if_not_imported=True,
            respect_translate_attr=True,
            skip_import_rules="skip_import_rules_example",
            import_as_confirmed_rules="import_as_confirmed_rules_example",
            import_as_locked_rules="import_as_locked_rules_example",
            export_attrs_when_confirmed_and_locked="export_attrs_when_confirmed_and_locked_example",
            export_attrs_when_confirmed_and_not_locked="export_attrs_when_confirmed_and_not_locked_example",
            export_attrs_when_not_confirmed_and_locked="export_attrs_when_not_confirmed_and_locked_example",
            export_attrs_when_not_confirmed_and_not_locked="export_attrs_when_not_confirmed_and_not_locked_example",
            context_key_x_path="context_key_x_path_example",
            preserve_char_entities="preserve_char_entities_example",
            xsl_url="xsl_url_example",
            xsl_file="xsl_file_example",
            tag_regexp="tag_regexp_example",
        ),
        xlf=XlfSettingsDto(
            icu_sub_filter=True,
            import_notes=True,
            segmentation=True,
            skip_import_rules="skip_import_rules_example",
            import_as_confirmed_rules="import_as_confirmed_rules_example",
            import_as_locked_rules="import_as_locked_rules_example",
            export_attrs_when_confirmed_and_locked="export_attrs_when_confirmed_and_locked_example",
            export_attrs_when_confirmed_and_not_locked="export_attrs_when_confirmed_and_not_locked_example",
            export_attrs_when_not_confirmed_and_locked="export_attrs_when_not_confirmed_and_locked_example",
            export_attrs_when_not_confirmed_and_not_locked="export_attrs_when_not_confirmed_and_not_locked_example",
            save_confirmed_segments=True,
            line_break_tags=True,
            preserve_whitespace=True,
            context_type="context_type_example",
            preserve_char_entities="preserve_char_entities_example",
            copy_source_to_target_if_not_imported=True,
            import_x_path="import_x_path_example",
            import_as_confirmed_x_path="import_as_confirmed_x_path_example",
            import_as_locked_x_path="import_as_locked_x_path_example",
            xsl_url="xsl_url_example",
            xsl_file="xsl_file_example",
            tag_regexp="tag_regexp_example",
        ),
        xls=XlsSettingsDto(
            sheet_names=True,
            hidden=True,
            comments=True,
            other=True,
            cell_flow="DownRight",
            html_subfilter=True,
            tag_regexp="tag_regexp_example",
            specified_columns="specified_columns_example",
        ),
        xml=XmlSettingsDto(
            rules_format="PLAIN",
            include_elements_plain="include_elements_plain_example",
            exclude_elements_plain="exclude_elements_plain_example",
            include_attributes_plain="include_attributes_plain_example",
            exclude_attributes_plain="exclude_attributes_plain_example",
            inline_elements_non_translatable_plain="inline_elements_non_translatable_plain_example",
            inline_elements_plain="inline_elements_plain_example",
            inline_elements_auto_plain=True,
            html_subfilter_elements_plain="html_subfilter_elements_plain_example",
            entities=True,
            lock_elements_plain="lock_elements_plain_example",
            lock_attributes_plain="lock_attributes_plain_example",
            include_x_path="include_x_path_example",
            inline_elements_xpath="inline_elements_xpath_example",
            inline_elements_non_translatable_x_path="inline_elements_non_translatable_x_path_example",
            inline_elements_auto_x_path=True,
            html_subfilter_elements_xpath="html_subfilter_elements_xpath_example",
            lock_x_path="lock_x_path_example",
            segmentation=True,
            tag_regexp="tag_regexp_example",
            context_note_xpath="context_note_xpath_example",
            max_len_x_path="max_len_x_path_example",
            preserve_whitespace_x_path="preserve_whitespace_x_path_example",
            preserve_char_entities="preserve_char_entities_example",
            context_key_x_path="context_key_x_path_example",
            xsl_url="xsl_url_example",
            xsl_file="xsl_file_example",
            import_comments=True,
            icu_sub_filter=True,
        ),
        yaml=YamlSettingsDto(
            html_sub_filter=True,
            tag_regexp="tag_regexp_example",
            include_key_regexp="include_key_regexp_example",
            exclude_value_regexp="exclude_value_regexp_example",
            context_path="context_path_example",
            context_key_path="context_key_path_example",
            markdown_subfilter=True,
            update_root_element_lang=True,
            locale_format="MEMSOURCE",
            indent_empty_lines_in_string=True,
            icu_sub_filter=True,
        ),
        asciidoc=AsciidocSettingsDto(
            tag_regexp="tag_regexp_example",
            html_in_passthrough=True,
            nontranslatable_monospace_custom_styles_regexp="nontranslatable_monospace_custom_styles_regexp_example",
            extract_custom_document_attribute_name_regexp="extract_custom_document_attribute_name_regexp_example",
            extract_btn_menu_labels=True,
        ),
    )
    try:
        # Edit project import settings
        api_response = api_instance.edit_import_settings1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_import_settings1: %s\n" % e)
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
[**FileImportSettingsCreateDto**](../../models/FileImportSettingsCreateDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_import_settings1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_import_settings1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_import_settings1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_import_settings1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_import_settings1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_import_settings1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_import_settings1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_import_settings1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_import_settings1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_import_settings1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_import_settings1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_import_settings1.ApiResponseFor501) | Not implemented

#### edit_import_settings1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FileImportSettingsDto**](../../models/FileImportSettingsDto.md) |  | 


#### edit_import_settings1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_import_settings1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_import_settings1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_import_settings1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_import_settings1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_import_settings1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_import_settings1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_import_settings1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_import_settings1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_import_settings1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_import_settings1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_project_access_settings_v2**
<a id="edit_project_access_settings_v2"></a>
> ProjectSecuritySettingsDtoV2 edit_project_access_settings_v2(project_uid)

Edit access and security settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.project_security_settings_dto_v2 import ProjectSecuritySettingsDtoV2
from openapi_client.model.edit_project_security_settings_dto_v2 import EditProjectSecuritySettingsDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit access and security settings
        api_response = api_instance.edit_project_access_settings_v2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_project_access_settings_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = EditProjectSecuritySettingsDtoV2(
        download_enabled=True,
        web_editor_enabled_for_linguists=True,
        show_user_data_to_linguists=True,
        email_notifications=True,
        strict_workflow_finish=True,
        use_vendors=True,
        linguists_may_edit_locked_segments=True,
        users_may_set_auto_propagation=True,
        allow_loading_external_content_in_editors=True,
        allow_loading_iframes=True,
        linguists_may_edit_source=True,
        linguists_may_edit_tag_content=True,
        linguists_may_download_lqa_report=True,
        usernames_displayed_in_lqa_report=True,
        user_may_set_instant_qa=True,
        trigger_webhooks=True,
        notify_job_owner_status_changed=True,
        vendors=VendorSecuritySettingsDto(
            can_change_shared_job_due_date_enabled=True,
            can_change_shared_job_due_date=[
                UidReference(
                    uid="uid_example",
                )
            ],
            job_vendors_may_upload_references=True,
        ),
        allowed_domains=[
            "allowed_domains_example"
        ],
    )
    try:
        # Edit access and security settings
        api_response = api_instance.edit_project_access_settings_v2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_project_access_settings_v2: %s\n" % e)
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
[**EditProjectSecuritySettingsDtoV2**](../../models/EditProjectSecuritySettingsDtoV2.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_project_access_settings_v2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_project_access_settings_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_project_access_settings_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_project_access_settings_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_project_access_settings_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_project_access_settings_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_project_access_settings_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_project_access_settings_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_project_access_settings_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_project_access_settings_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_project_access_settings_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_project_access_settings_v2.ApiResponseFor501) | Not implemented

#### edit_project_access_settings_v2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectSecuritySettingsDtoV2**](../../models/ProjectSecuritySettingsDtoV2.md) |  | 


#### edit_project_access_settings_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_access_settings_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_access_settings_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_access_settings_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_access_settings_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_access_settings_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_access_settings_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_access_settings_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_access_settings_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_access_settings_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_access_settings_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_project_pre_translate_settings2**
<a id="edit_project_pre_translate_settings2"></a>
> PreTranslateSettingsV3Dto edit_project_pre_translate_settings2(project_uid)

Update Pre-translate settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.pre_translate_settings_v3_dto import PreTranslateSettingsV3Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Update Pre-translate settings
        api_response = api_instance.edit_project_pre_translate_settings2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_project_pre_translate_settings2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = PreTranslateSettingsV3Dto(
        pre_translate_on_job_creation=True,
        set_job_status_completed=True,
        set_job_status_completed_when_confirmed=True,
        set_project_status_completed=True,
        overwrite_existing_translations=True,
        translation_memory_settings=TranslationMemorySettingsDto(
            use_translation_memory=True,
            translation_memory_threshold=0,
            confirm100_percent_matches=True,
            confirm101_percent_matches=True,
            lock100_percent_matches=True,
            lock101_percent_matches=True,
        ),
        machine_translation_settings=MachineTranslationSettingsDto(
            use_machine_translation=True,
            lock100_percent_matches=True,
            confirm100_percent_matches=True,
            use_alt_trans_only=True,
            mt_qe_matches_in_editors=True,
            mt_for_tm_above100=True,
        ),
        non_translatable_settings=NonTranslatableSettingsDto(
            pre_translate_non_translatables=True,
            confirm100_percent_matches=True,
            lock100_percent_matches=True,
            non_translatables_in_editors=True,
        ),
        repetitions_settings=RepetitionsSettingsDto(
            auto_propagate_repetitions=True,
            confirm_repetitions=True,
            auto_propagate_to_locked_repetitions=True,
            lock_subsequent_repetitions=True,
        ),
    )
    try:
        # Update Pre-translate settings
        api_response = api_instance.edit_project_pre_translate_settings2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_project_pre_translate_settings2: %s\n" % e)
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
[**PreTranslateSettingsV3Dto**](../../models/PreTranslateSettingsV3Dto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_project_pre_translate_settings2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_project_pre_translate_settings2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_project_pre_translate_settings2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_project_pre_translate_settings2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_project_pre_translate_settings2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_project_pre_translate_settings2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_project_pre_translate_settings2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_project_pre_translate_settings2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_project_pre_translate_settings2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_project_pre_translate_settings2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_project_pre_translate_settings2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_project_pre_translate_settings2.ApiResponseFor501) | Not implemented

#### edit_project_pre_translate_settings2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PreTranslateSettingsV3Dto**](../../models/PreTranslateSettingsV3Dto.md) |  | 


#### edit_project_pre_translate_settings2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_pre_translate_settings2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_pre_translate_settings2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_pre_translate_settings2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_pre_translate_settings2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_pre_translate_settings2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_pre_translate_settings2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_pre_translate_settings2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_pre_translate_settings2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_pre_translate_settings2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_pre_translate_settings2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_project_v2**
<a id="edit_project_v2"></a>
> AbstractProjectDtoV2 edit_project_v2(project_uid)

Edit project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.edit_project_v2_dto import EditProjectV2Dto
from openapi_client.model.abstract_project_dto_v2 import AbstractProjectDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit project
        api_response = api_instance.edit_project_v2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_project_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = EditProjectV2Dto(
        name="name_example",
        status="NEW",
        client=IdReference(
            id="id_example",
        ),
,
,
,
,
        purchase_order="purchase_order_example",
        date_due="1970-01-01T00:00:00.00Z",
        note="note_example",
        file_handover=True,
        lqa_profiles=[
            LqaProfilesForWsV2Dto(
                workflow_step=IdReference(),
                lqa_profile=UidReference(
                    uid="uid_example",
                ),
            )
        ],
        archived=True,
        custom_fields=[
            CustomFieldInstanceApiDto(
                custom_field=UidReference(),
                selected_options=[
                    UidReference()
                ],
                value="value_example",
            )
        ],
    )
    try:
        # Edit project
        api_response = api_instance.edit_project_v2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->edit_project_v2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**EditProjectV2Dto**](../../models/EditProjectV2Dto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_project_v2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_project_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_project_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_project_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_project_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_project_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_project_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_project_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_project_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_project_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_project_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_project_v2.ApiResponseFor501) | Not implemented

#### edit_project_v2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**AbstractProjectDtoV2**](../../models/AbstractProjectDtoV2.md) |  | 


#### edit_project_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enabled_quality_checks**
<a id="enabled_quality_checks"></a>
> EnabledQualityChecksDto enabled_quality_checks(project_uid)

Get QA checks

Returns enabled quality assurance settings.

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.enabled_quality_checks_dto import EnabledQualityChecksDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get QA checks
        api_response = api_instance.enabled_quality_checks(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->enabled_quality_checks: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#enabled_quality_checks.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#enabled_quality_checks.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#enabled_quality_checks.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#enabled_quality_checks.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#enabled_quality_checks.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#enabled_quality_checks.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#enabled_quality_checks.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#enabled_quality_checks.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#enabled_quality_checks.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#enabled_quality_checks.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#enabled_quality_checks.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#enabled_quality_checks.ApiResponseFor501) | Not implemented

#### enabled_quality_checks.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnabledQualityChecksDto**](../../models/EnabledQualityChecksDto.md) |  | 


#### enabled_quality_checks.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_analyse_settings_for_project**
<a id="get_analyse_settings_for_project"></a>
> AnalyseSettingsDto get_analyse_settings_for_project(project_uid)

Get analyse settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.analyse_settings_dto import AnalyseSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get analyse settings
        api_response = api_instance.get_analyse_settings_for_project(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_analyse_settings_for_project: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_analyse_settings_for_project.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_analyse_settings_for_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_analyse_settings_for_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_analyse_settings_for_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_analyse_settings_for_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_analyse_settings_for_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_analyse_settings_for_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_analyse_settings_for_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_analyse_settings_for_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_analyse_settings_for_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_analyse_settings_for_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_analyse_settings_for_project.ApiResponseFor501) | Not implemented

#### get_analyse_settings_for_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalyseSettingsDto**](../../models/AnalyseSettingsDto.md) |  | 


#### get_analyse_settings_for_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_custom_field1**
<a id="get_custom_field1"></a>
> CustomFieldInstanceDto get_custom_field1(project_uidfield_instance_uid)

Get custom field of project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.custom_field_instance_dto import CustomFieldInstanceDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'fieldInstanceUid': "fieldInstanceUid_example",
    }
    try:
        # Get custom field of project
        api_response = api_instance.get_custom_field1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_custom_field1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 
fieldInstanceUid | FieldInstanceUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldInstanceUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_custom_field1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_custom_field1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_custom_field1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_custom_field1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_custom_field1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_custom_field1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_custom_field1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_custom_field1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_custom_field1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_custom_field1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_custom_field1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_custom_field1.ApiResponseFor501) | Not implemented

#### get_custom_field1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomFieldInstanceDto**](../../models/CustomFieldInstanceDto.md) |  | 


#### get_custom_field1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_custom_fields_page**
<a id="get_custom_fields_page"></a>
> PageDtoCustomFieldInstanceDto get_custom_fields_page(project_uid)

Get custom fields of project (page)

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.page_dto_custom_field_instance_dto import PageDtoCustomFieldInstanceDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Get custom fields of project (page)
        api_response = api_instance.get_custom_fields_page(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_custom_fields_page: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'pageNumber': 0,
        'pageSize': 20,
        'createdBy': [
        "createdBy_example"
    ],
        'modifiedBy': [
        "modifiedBy_example"
    ],
        'sortField': "CREATED",
        'sortTrend': "ASC",
    }
    try:
        # Get custom fields of project (page)
        api_response = api_instance.get_custom_fields_page(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_custom_fields_page: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional
createdBy | CreatedBySchema | | optional
modifiedBy | ModifiedBySchema | | optional
sortField | SortFieldSchema | | optional
sortTrend | SortTrendSchema | | optional


# PageNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20value must be a 32 bit integer

# CreatedBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ModifiedBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# SortFieldSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["CREATED", "LAST_MODIFIED", ] 

# SortTrendSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "ASC"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_custom_fields_page.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_custom_fields_page.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_custom_fields_page.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_custom_fields_page.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_custom_fields_page.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_custom_fields_page.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_custom_fields_page.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_custom_fields_page.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_custom_fields_page.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_custom_fields_page.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_custom_fields_page.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_custom_fields_page.ApiResponseFor501) | Not implemented

#### get_custom_fields_page.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoCustomFieldInstanceDto**](../../models/PageDtoCustomFieldInstanceDto.md) |  | 


#### get_custom_fields_page.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_file_naming_settings**
<a id="get_file_naming_settings"></a>
> FileNamingSettingsDto get_file_naming_settings(project_uid)

Get file naming settings for project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.file_naming_settings_dto import FileNamingSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get file naming settings for project
        api_response = api_instance.get_file_naming_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_file_naming_settings: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_file_naming_settings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_file_naming_settings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_file_naming_settings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_file_naming_settings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_file_naming_settings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_file_naming_settings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_file_naming_settings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_file_naming_settings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_file_naming_settings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_file_naming_settings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_file_naming_settings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_file_naming_settings.ApiResponseFor501) | Not implemented

#### get_file_naming_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FileNamingSettingsDto**](../../models/FileNamingSettingsDto.md) |  | 


#### get_file_naming_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_naming_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_naming_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_naming_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_naming_settings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_naming_settings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_naming_settings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_naming_settings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_naming_settings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_naming_settings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_file_naming_settings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_financial_settings**
<a id="get_financial_settings"></a>
> FinancialSettingsDto get_financial_settings(project_uid)

Get financial settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.financial_settings_dto import FinancialSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get financial settings
        api_response = api_instance.get_financial_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_financial_settings: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_financial_settings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_financial_settings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_financial_settings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_financial_settings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_financial_settings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_financial_settings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_financial_settings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_financial_settings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_financial_settings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_financial_settings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_financial_settings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_financial_settings.ApiResponseFor501) | Not implemented

#### get_financial_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FinancialSettingsDto**](../../models/FinancialSettingsDto.md) |  | 


#### get_financial_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_financial_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_financial_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_financial_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_financial_settings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_financial_settings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_financial_settings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_financial_settings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_financial_settings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_financial_settings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_financial_settings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_import_settings2**
<a id="get_import_settings2"></a>
> FileImportSettingsDto get_import_settings2(project_uid)

Get projects's default import settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.file_import_settings_dto import FileImportSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get projects's default import settings
        api_response = api_instance.get_import_settings2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_import_settings2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_import_settings2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_import_settings2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_import_settings2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_import_settings2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_import_settings2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_import_settings2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_import_settings2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_import_settings2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_import_settings2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_import_settings2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_import_settings2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_import_settings2.ApiResponseFor501) | Not implemented

#### get_import_settings2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FileImportSettingsDto**](../../models/FileImportSettingsDto.md) |  | 


#### get_import_settings2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_mt_settings_for_project**
<a id="get_mt_settings_for_project"></a>
> MTSettingsPerLanguageListDto get_mt_settings_for_project(project_uid)

Get project machine translate settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.mt_settings_per_language_list_dto import MTSettingsPerLanguageListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get project machine translate settings
        api_response = api_instance.get_mt_settings_for_project(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_mt_settings_for_project: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_mt_settings_for_project.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_mt_settings_for_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_mt_settings_for_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_mt_settings_for_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_mt_settings_for_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_mt_settings_for_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_mt_settings_for_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_mt_settings_for_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_mt_settings_for_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_mt_settings_for_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_mt_settings_for_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_mt_settings_for_project.ApiResponseFor501) | Not implemented

#### get_mt_settings_for_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MTSettingsPerLanguageListDto**](../../models/MTSettingsPerLanguageListDto.md) |  | 


#### get_mt_settings_for_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_mt_settings_for_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_mt_settings_for_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_mt_settings_for_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_mt_settings_for_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_mt_settings_for_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_mt_settings_for_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_mt_settings_for_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_mt_settings_for_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_mt_settings_for_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_mt_settings_for_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pre_translate_settings_for_project2**
<a id="get_pre_translate_settings_for_project2"></a>
> PreTranslateSettingsV3Dto get_pre_translate_settings_for_project2(project_uid)

Get Pre-translate settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.pre_translate_settings_v3_dto import PreTranslateSettingsV3Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get Pre-translate settings
        api_response = api_instance.get_pre_translate_settings_for_project2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_pre_translate_settings_for_project2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pre_translate_settings_for_project2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_pre_translate_settings_for_project2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_pre_translate_settings_for_project2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_pre_translate_settings_for_project2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_pre_translate_settings_for_project2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_pre_translate_settings_for_project2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_pre_translate_settings_for_project2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_pre_translate_settings_for_project2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_pre_translate_settings_for_project2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_pre_translate_settings_for_project2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_pre_translate_settings_for_project2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_pre_translate_settings_for_project2.ApiResponseFor501) | Not implemented

#### get_pre_translate_settings_for_project2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PreTranslateSettingsV3Dto**](../../models/PreTranslateSettingsV3Dto.md) |  | 


#### get_pre_translate_settings_for_project2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project**
<a id="get_project"></a>
> AbstractProjectDto get_project(project_uid)

Get project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.abstract_project_dto import AbstractProjectDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get project
        api_response = api_instance.get_project(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project.ApiResponseFor501) | Not implemented

#### get_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AbstractProjectDto**](../../models/AbstractProjectDto.md) |  | 


#### get_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_access_settings_v2**
<a id="get_project_access_settings_v2"></a>
> ProjectSecuritySettingsDtoV2 get_project_access_settings_v2(project_uid)

Get access and security settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.project_security_settings_dto_v2 import ProjectSecuritySettingsDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get access and security settings
        api_response = api_instance.get_project_access_settings_v2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_access_settings_v2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_access_settings_v2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_access_settings_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_access_settings_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_access_settings_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_access_settings_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_access_settings_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_access_settings_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_access_settings_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_access_settings_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_access_settings_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_access_settings_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_access_settings_v2.ApiResponseFor501) | Not implemented

#### get_project_access_settings_v2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectSecuritySettingsDtoV2**](../../models/ProjectSecuritySettingsDtoV2.md) |  | 


#### get_project_access_settings_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_access_settings_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_access_settings_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_access_settings_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_access_settings_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_access_settings_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_access_settings_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_access_settings_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_access_settings_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_access_settings_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_access_settings_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_assignments**
<a id="get_project_assignments"></a>
> PageDtoProviderReference get_project_assignments(project_uid)

List project providers

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.page_dto_provider_reference import PageDtoProviderReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # List project providers
        api_response = api_instance.get_project_assignments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_assignments: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'providerName': "providerName_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List project providers
        api_response = api_instance.get_project_assignments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_assignments: %s\n" % e)
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
providerName | ProviderNameSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


# ProviderNameSchema

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
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_assignments.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_assignments.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_assignments.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_assignments.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_assignments.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_assignments.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_assignments.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_assignments.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_assignments.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_assignments.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_assignments.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_assignments.ApiResponseFor501) | Not implemented

#### get_project_assignments.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoProviderReference**](../../models/PageDtoProviderReference.md) |  | 


#### get_project_assignments.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_assignments.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_assignments.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_assignments.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_assignments.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_assignments.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_assignments.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_assignments.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_assignments.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_assignments.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_assignments.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_settings**
<a id="get_project_settings"></a>
> LqaSettingsDto get_project_settings(project_uid)

Get LQA settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.lqa_settings_dto import LqaSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Get LQA settings
        api_response = api_instance.get_project_settings(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_settings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'workflowLevel': 1,
    }
    try:
        # Get LQA settings
        api_response = api_instance.get_project_settings(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_settings: %s\n" % e)
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
workflowLevel | WorkflowLevelSchema | | optional


# WorkflowLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_settings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_settings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_settings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_settings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_settings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_settings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_settings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_settings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_settings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_settings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_settings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_settings.ApiResponseFor501) | Not implemented

#### get_project_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LqaSettingsDto**](../../models/LqaSettingsDto.md) |  | 


#### get_project_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_settings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_settings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_settings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_settings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_settings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_settings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_settings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_term_bases**
<a id="get_project_term_bases"></a>
> ProjectTermBaseListDto get_project_term_bases(project_uid)

Get term bases

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.project_term_base_list_dto import ProjectTermBaseListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get term bases
        api_response = api_instance.get_project_term_bases(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_term_bases: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_term_bases.ApiResponseFor501) | Not implemented

#### get_project_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTermBaseListDto**](../../models/ProjectTermBaseListDto.md) |  | 


#### get_project_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_trans_memories1**
<a id="get_project_trans_memories1"></a>
> ProjectTransMemoryListDtoV3 get_project_trans_memories1(project_uid)

Get translation memories

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.project_trans_memory_list_dto_v3 import ProjectTransMemoryListDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Get translation memories
        api_response = api_instance.get_project_trans_memories1(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_trans_memories1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'targetLang': "targetLang_example",
        'wfStepUid': "wfStepUid_example",
    }
    try:
        # Get translation memories
        api_response = api_instance.get_project_trans_memories1(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_trans_memories1: %s\n" % e)
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
targetLang | TargetLangSchema | | optional
wfStepUid | WfStepUidSchema | | optional


# TargetLangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# WfStepUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_trans_memories1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_trans_memories1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_trans_memories1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_trans_memories1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_trans_memories1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_trans_memories1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_trans_memories1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_trans_memories1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_trans_memories1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_trans_memories1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_trans_memories1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_trans_memories1.ApiResponseFor501) | Not implemented

#### get_project_trans_memories1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTransMemoryListDtoV3**](../../models/ProjectTransMemoryListDtoV3.md) |  | 


#### get_project_trans_memories1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_trans_memories1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_trans_memories1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_trans_memories1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_trans_memories1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_trans_memories1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_trans_memories1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_trans_memories1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_trans_memories1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_trans_memories1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_trans_memories1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_workflow_steps_v2**
<a id="get_project_workflow_steps_v2"></a>
> ProjectWorkflowStepListDtoV2 get_project_workflow_steps_v2(project_uid)

Get workflow steps

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.project_workflow_step_list_dto_v2 import ProjectWorkflowStepListDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Get workflow steps
        api_response = api_instance.get_project_workflow_steps_v2(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_workflow_steps_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'withAssignedJobs': False,
    }
    try:
        # Get workflow steps
        api_response = api_instance.get_project_workflow_steps_v2(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_project_workflow_steps_v2: %s\n" % e)
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
withAssignedJobs | WithAssignedJobsSchema | | optional


# WithAssignedJobsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_workflow_steps_v2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_workflow_steps_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_workflow_steps_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_workflow_steps_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_workflow_steps_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_workflow_steps_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_workflow_steps_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_workflow_steps_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_workflow_steps_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_workflow_steps_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_workflow_steps_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_workflow_steps_v2.ApiResponseFor501) | Not implemented

#### get_project_workflow_steps_v2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectWorkflowStepListDtoV2**](../../models/ProjectWorkflowStepListDtoV2.md) |  | 


#### get_project_workflow_steps_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_workflow_steps_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_workflow_steps_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_workflow_steps_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_workflow_steps_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_workflow_steps_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_workflow_steps_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_workflow_steps_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_workflow_steps_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_workflow_steps_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_workflow_steps_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_quotes_for_project**
<a id="get_quotes_for_project"></a>
> PageDtoQuoteDto get_quotes_for_project(project_uid)

List quotes

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.page_dto_quote_dto import PageDtoQuoteDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # List quotes
        api_response = api_instance.get_quotes_for_project(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_quotes_for_project: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List quotes
        api_response = api_instance.get_quotes_for_project(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->get_quotes_for_project: %s\n" % e)
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
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


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
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_quotes_for_project.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_quotes_for_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_quotes_for_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_quotes_for_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_quotes_for_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_quotes_for_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_quotes_for_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_quotes_for_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_quotes_for_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_quotes_for_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_quotes_for_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_quotes_for_project.ApiResponseFor501) | Not implemented

#### get_quotes_for_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoQuoteDto**](../../models/PageDtoQuoteDto.md) |  | 


#### get_quotes_for_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_quotes_for_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_quotes_for_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_quotes_for_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_quotes_for_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_quotes_for_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_quotes_for_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_quotes_for_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_quotes_for_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_quotes_for_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_quotes_for_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_assigned_projects**
<a id="list_assigned_projects"></a>
> PageDtoProjectReference list_assigned_projects(user_uid)

List assigned projects

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.page_dto_project_reference import PageDtoProjectReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
    }
    try:
        # List assigned projects
        api_response = api_instance.list_assigned_projects(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->list_assigned_projects: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
        'status': [
        "NEW"
    ],
        'targetLang': [
        "targetLang_example"
    ],
        'workflowStepId': 1,
        'dueInHours': -1,
        'filename': "filename_example",
        'projectName': "projectName_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List assigned projects
        api_response = api_instance.list_assigned_projects(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->list_assigned_projects: %s\n" % e)
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
targetLang | TargetLangSchema | | optional
workflowStepId | WorkflowStepIdSchema | | optional
dueInHours | DueInHoursSchema | | optional
filename | FilenameSchema | | optional
projectName | ProjectNameSchema | | optional
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

# TargetLangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# WorkflowStepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

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

# ProjectNameSchema

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
200 | [ApiResponseFor200](#list_assigned_projects.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_assigned_projects.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_assigned_projects.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_assigned_projects.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_assigned_projects.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_assigned_projects.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_assigned_projects.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_assigned_projects.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_assigned_projects.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_assigned_projects.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_assigned_projects.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_assigned_projects.ApiResponseFor501) | Not implemented

#### list_assigned_projects.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoProjectReference**](../../models/PageDtoProjectReference.md) |  | 


#### list_assigned_projects.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_assigned_projects.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_assigned_projects.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_assigned_projects.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_assigned_projects.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_assigned_projects.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_assigned_projects.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_assigned_projects.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_assigned_projects.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_assigned_projects.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_assigned_projects.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_by_project_v3**
<a id="list_by_project_v3"></a>
> PageDtoAnalyseReference list_by_project_v3(project_uid)

List analyses by project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.page_dto_analyse_reference import PageDtoAnalyseReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # List analyses by project
        api_response = api_instance.list_by_project_v3(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->list_by_project_v3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'name': "name_example",
        'uid': "uid_example",
        'pageNumber': 0,
        'pageSize': 50,
        'sort': "DATE_CREATED",
        'order': "desc",
        'onlyOwnerOrg': True,
    }
    try:
        # List analyses by project
        api_response = api_instance.list_by_project_v3(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->list_by_project_v3: %s\n" % e)
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
name | NameSchema | | optional
uid | UidSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional
sort | SortSchema | | optional
order | OrderSchema | | optional
onlyOwnerOrg | OnlyOwnerOrgSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UidSchema

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

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["DATE_CREATED", ] if omitted the server will use the default value of "DATE_CREATED"

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] if omitted the server will use the default value of "desc"

# OnlyOwnerOrgSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_by_project_v3.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_by_project_v3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_by_project_v3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_by_project_v3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_by_project_v3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_by_project_v3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_by_project_v3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_by_project_v3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_by_project_v3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_by_project_v3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_by_project_v3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_by_project_v3.ApiResponseFor501) | Not implemented

#### list_by_project_v3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoAnalyseReference**](../../models/PageDtoAnalyseReference.md) |  | 


#### list_by_project_v3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_by_project_v3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_by_project_v3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_by_project_v3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_by_project_v3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_by_project_v3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_by_project_v3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_by_project_v3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_by_project_v3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_by_project_v3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_by_project_v3.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_projects**
<a id="list_projects"></a>
> PageDtoAbstractProjectDto list_projects()

List projects

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.page_dto_abstract_project_dto import PageDtoAbstractProjectDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'clientId': 1,
        'clientName': "clientName_example",
        'businessUnitId': 1,
        'businessUnitName': "businessUnitName_example",
        'statuses': [
        "NEW"
    ],
        'targetLangs': [
        "targetLangs_example"
    ],
        'domainId': 1,
        'domainName': "domainName_example",
        'subDomainId': 1,
        'subDomainName': "subDomainName_example",
        'costCenterId': 1,
        'costCenterName': "costCenterName_example",
        'dueInHours': -1,
        'createdInLastHours': 0,
        'sourceLangs': [
        "sourceLangs_example"
    ],
        'ownerId': 1,
        'jobStatuses': [
        "NEW"
    ],
        'jobStatusGroup': "NEW",
        'buyerId': 1,
        'pageNumber': 0,
        'pageSize': 50,
        'nameOrInternalId': "nameOrInternalId_example",
        'includeArchived': False,
        'archivedOnly': False,
    }
    try:
        # List projects
        api_response = api_instance.list_projects(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->list_projects: %s\n" % e)
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
name | NameSchema | | optional
clientId | ClientIdSchema | | optional
clientName | ClientNameSchema | | optional
businessUnitId | BusinessUnitIdSchema | | optional
businessUnitName | BusinessUnitNameSchema | | optional
statuses | StatusesSchema | | optional
targetLangs | TargetLangsSchema | | optional
domainId | DomainIdSchema | | optional
domainName | DomainNameSchema | | optional
subDomainId | SubDomainIdSchema | | optional
subDomainName | SubDomainNameSchema | | optional
costCenterId | CostCenterIdSchema | | optional
costCenterName | CostCenterNameSchema | | optional
dueInHours | DueInHoursSchema | | optional
createdInLastHours | CreatedInLastHoursSchema | | optional
sourceLangs | SourceLangsSchema | | optional
ownerId | OwnerIdSchema | | optional
jobStatuses | JobStatusesSchema | | optional
jobStatusGroup | JobStatusGroupSchema | | optional
buyerId | BuyerIdSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional
nameOrInternalId | NameOrInternalIdSchema | | optional
includeArchived | IncludeArchivedSchema | | optional
archivedOnly | ArchivedOnlySchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClientIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# ClientNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BusinessUnitIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# BusinessUnitNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["NEW", "ASSIGNED", "COMPLETED", "ACCEPTED_BY_VENDOR", "DECLINED_BY_VENDOR", "COMPLETED_BY_VENDOR", "CANCELLED", ] 

# TargetLangsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# DomainIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# DomainNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubDomainIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# SubDomainNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CostCenterIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# CostCenterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DueInHoursSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# CreatedInLastHoursSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# SourceLangsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# OwnerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# JobStatusesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["NEW", "ACCEPTED", "DECLINED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] 

# JobStatusGroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NEW", "ACCEPTED", "COMPLETED", ] 

# BuyerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

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

# NameOrInternalIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IncludeArchivedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# ArchivedOnlySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_projects.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_projects.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_projects.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_projects.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_projects.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_projects.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_projects.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_projects.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_projects.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_projects.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_projects.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_projects.ApiResponseFor501) | Not implemented

#### list_projects.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoAbstractProjectDto**](../../models/PageDtoAbstractProjectDto.md) |  | 


#### list_projects.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_projects.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_projects.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_projects.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_projects.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_projects.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_projects.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_projects.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_projects.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_projects.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_projects.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_providers3**
<a id="list_providers3"></a>
> ProviderListDtoV2 list_providers3(project_uid)

Get suggested providers

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.provider_list_dto_v2 import ProviderListDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get suggested providers
        api_response = api_instance.list_providers3(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->list_providers3: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_providers3.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_providers3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_providers3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_providers3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_providers3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_providers3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_providers3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_providers3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_providers3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_providers3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_providers3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_providers3.ApiResponseFor501) | Not implemented

#### list_providers3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ProviderListDtoV2**](../../models/ProviderListDtoV2.md) |  | 


#### list_providers3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_providers3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_providers3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_providers3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_providers3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_providers3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_providers3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_providers3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_providers3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_providers3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_providers3.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_project**
<a id="patch_project"></a>
> AbstractProjectDto patch_project(project_uid)

Edit project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.patch_project_dto import PatchProjectDto
from openapi_client.model.abstract_project_dto import AbstractProjectDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit project
        api_response = api_instance.patch_project(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->patch_project: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = PatchProjectDto(
        name="name_example",
        status="NEW",
        client=IdReference(
            id="id_example",
        ),
,
,
,
,
        purchase_order="purchase_order_example",
        date_due="1970-01-01T00:00:00.00Z",
        note="note_example",
        machine_translate_settings=UidReference(
            uid="uid_example",
        ),
        machine_translate_settings_per_langs=[
            ProjectMTSettingsPerLangDto(
                target_lang="target_lang_example",
                machine_translate_settings=UidReference(),
            )
        ],
        archived=True,
    )
    try:
        # Edit project
        api_response = api_instance.patch_project(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->patch_project: %s\n" % e)
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
[**PatchProjectDto**](../../models/PatchProjectDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_project.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#patch_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#patch_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#patch_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#patch_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#patch_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#patch_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#patch_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#patch_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#patch_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#patch_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#patch_project.ApiResponseFor501) | Not implemented

#### patch_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AbstractProjectDto**](../../models/AbstractProjectDto.md) |  | 


#### patch_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### patch_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **relevant_term_bases**
<a id="relevant_term_bases"></a>
> PageDtoTermBaseDto relevant_term_bases(project_uid)

List project relevant term bases

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.page_dto_term_base_dto import PageDtoTermBaseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # List project relevant term bases
        api_response = api_instance.relevant_term_bases(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->relevant_term_bases: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'name': "name_example",
        'domainName': "domainName_example",
        'clientName': "clientName_example",
        'subDomainName': "subDomainName_example",
        'targetLangs': [
        "targetLangs_example"
    ],
        'strictLangMatching': False,
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List project relevant term bases
        api_response = api_instance.relevant_term_bases(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->relevant_term_bases: %s\n" % e)
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
name | NameSchema | | optional
domainName | DomainNameSchema | | optional
clientName | ClientNameSchema | | optional
subDomainName | SubDomainNameSchema | | optional
targetLangs | TargetLangsSchema | | optional
strictLangMatching | StrictLangMatchingSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DomainNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClientNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubDomainNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TargetLangsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StrictLangMatchingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

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
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#relevant_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#relevant_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#relevant_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#relevant_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#relevant_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#relevant_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#relevant_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#relevant_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#relevant_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#relevant_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#relevant_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#relevant_term_bases.ApiResponseFor501) | Not implemented

#### relevant_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoTermBaseDto**](../../models/PageDtoTermBaseDto.md) |  | 


#### relevant_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **relevant_trans_memories1**
<a id="relevant_trans_memories1"></a>
> PageDtoTransMemoryDto relevant_trans_memories1(project_uid)

List project relevant translation memories

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.page_dto_trans_memory_dto import PageDtoTransMemoryDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # List project relevant translation memories
        api_response = api_instance.relevant_trans_memories1(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->relevant_trans_memories1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'name': "name_example",
        'domainName': "domainName_example",
        'clientName': "clientName_example",
        'subDomainName': "subDomainName_example",
        'targetLangs': [
        "targetLangs_example"
    ],
        'strictLangMatching': False,
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List project relevant translation memories
        api_response = api_instance.relevant_trans_memories1(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->relevant_trans_memories1: %s\n" % e)
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
name | NameSchema | | optional
domainName | DomainNameSchema | | optional
clientName | ClientNameSchema | | optional
subDomainName | SubDomainNameSchema | | optional
targetLangs | TargetLangsSchema | | optional
strictLangMatching | StrictLangMatchingSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DomainNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClientNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubDomainNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TargetLangsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# StrictLangMatchingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

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
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#relevant_trans_memories1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#relevant_trans_memories1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#relevant_trans_memories1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#relevant_trans_memories1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#relevant_trans_memories1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#relevant_trans_memories1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#relevant_trans_memories1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#relevant_trans_memories1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#relevant_trans_memories1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#relevant_trans_memories1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#relevant_trans_memories1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#relevant_trans_memories1.ApiResponseFor501) | Not implemented

#### relevant_trans_memories1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoTransMemoryDto**](../../models/PageDtoTransMemoryDto.md) |  | 


#### relevant_trans_memories1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_segment1**
<a id="search_segment1"></a>
> SearchResponseListTmDto search_segment1(project_uid)

Search translation memory for segment in the project

Returns at most <i>maxSegments</i>             records with <i>score >= scoreThreshold</i> and at most <i>maxSubsegments</i> records which are subsegment,             i.e. the source text is substring of the query text.

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.search_response_list_tm_dto import SearchResponseListTmDto
from openapi_client.model.search_tm_request_dto import SearchTMRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Search translation memory for segment in the project
        api_response = api_instance.search_segment1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->search_segment1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = SearchTMRequestDto(
        segment="segment_example",
        workflow_level=1,
        score_threshold=0,
        previous_segment="previous_segment_example",
        next_segment="next_segment_example",
        context_key="context_key_example",
        max_segments=0,
        max_sub_segments=0,
        tag_metadata=[
            TagMetadataDto(
                id="id_example",
                type="type_example",
                content="content_example",
                trans_attributes="trans_attributes_example",
            )
        ],
        target_langs=[
            "target_langs_example"
        ],
    )
    try:
        # Search translation memory for segment in the project
        api_response = api_instance.search_segment1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->search_segment1: %s\n" % e)
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
[**SearchTMRequestDto**](../../models/SearchTMRequestDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_segment1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#search_segment1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#search_segment1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#search_segment1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_segment1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#search_segment1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#search_segment1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#search_segment1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#search_segment1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#search_segment1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#search_segment1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#search_segment1.ApiResponseFor501) | Not implemented

#### search_segment1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchResponseListTmDto**](../../models/SearchResponseListTmDto.md) |  | 


#### search_segment1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_financial_settings**
<a id="set_financial_settings"></a>
> FinancialSettingsDto set_financial_settings(project_uid)

Edit financial settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.set_financial_settings_dto import SetFinancialSettingsDto
from openapi_client.model.financial_settings_dto import FinancialSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit financial settings
        api_response = api_instance.set_financial_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_financial_settings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = SetFinancialSettingsDto(
        net_rate_scheme=IdReference(
            id="id_example",
        ),
,
    )
    try:
        # Edit financial settings
        api_response = api_instance.set_financial_settings(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_financial_settings: %s\n" % e)
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
[**SetFinancialSettingsDto**](../../models/SetFinancialSettingsDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_financial_settings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#set_financial_settings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_financial_settings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_financial_settings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_financial_settings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_financial_settings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_financial_settings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_financial_settings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_financial_settings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_financial_settings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_financial_settings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_financial_settings.ApiResponseFor501) | Not implemented

#### set_financial_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FinancialSettingsDto**](../../models/FinancialSettingsDto.md) |  | 


#### set_financial_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_financial_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_financial_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_financial_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_financial_settings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_financial_settings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_financial_settings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_financial_settings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_financial_settings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_financial_settings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_financial_settings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_mt_settings_for_project**
<a id="set_mt_settings_for_project"></a>
> MTSettingsPerLanguageListDto set_mt_settings_for_project(project_uid)

Edit machine translate settings

This will erase all mtSettings per language for project.         To remove all machine translate settings from project call without a machineTranslateSettings parameter.

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.mt_settings_per_language_list_dto import MTSettingsPerLanguageListDto
from openapi_client.model.edit_project_mt_settings_dto import EditProjectMTSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit machine translate settings
        api_response = api_instance.set_mt_settings_for_project(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_mt_settings_for_project: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = EditProjectMTSettingsDto(
        machine_translate_settings=IdReference(
            id="id_example",
        ),
    )
    try:
        # Edit machine translate settings
        api_response = api_instance.set_mt_settings_for_project(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_mt_settings_for_project: %s\n" % e)
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
[**EditProjectMTSettingsDto**](../../models/EditProjectMTSettingsDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_mt_settings_for_project.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#set_mt_settings_for_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_mt_settings_for_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_mt_settings_for_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_mt_settings_for_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_mt_settings_for_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_mt_settings_for_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_mt_settings_for_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_mt_settings_for_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_mt_settings_for_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_mt_settings_for_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_mt_settings_for_project.ApiResponseFor501) | Not implemented

#### set_mt_settings_for_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MTSettingsPerLanguageListDto**](../../models/MTSettingsPerLanguageListDto.md) |  | 


#### set_mt_settings_for_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_for_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_for_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_for_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_for_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_for_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_for_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_for_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_for_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_for_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_for_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_mt_settings_per_language_for_project**
<a id="set_mt_settings_per_language_for_project"></a>
> MTSettingsPerLanguageListDto set_mt_settings_per_language_for_project(project_uid)

Edit machine translate settings per language

This will erase mtSettings for project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.mt_settings_per_language_list_dto import MTSettingsPerLanguageListDto
from openapi_client.model.edit_project_mt_sett_per_lang_list_dto import EditProjectMTSettPerLangListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit machine translate settings per language
        api_response = api_instance.set_mt_settings_per_language_for_project(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_mt_settings_per_language_for_project: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = EditProjectMTSettPerLangListDto(
        mt_settings_per_lang_list=[
            EditProjectMTSettPerLangDto(
                target_lang="target_lang_example",
                machine_translate_settings=IdReference(
                    id="id_example",
                ),
            )
        ],
    )
    try:
        # Edit machine translate settings per language
        api_response = api_instance.set_mt_settings_per_language_for_project(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_mt_settings_per_language_for_project: %s\n" % e)
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
[**EditProjectMTSettPerLangListDto**](../../models/EditProjectMTSettPerLangListDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_mt_settings_per_language_for_project.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#set_mt_settings_per_language_for_project.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_mt_settings_per_language_for_project.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_mt_settings_per_language_for_project.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_mt_settings_per_language_for_project.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_mt_settings_per_language_for_project.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_mt_settings_per_language_for_project.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_mt_settings_per_language_for_project.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_mt_settings_per_language_for_project.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_mt_settings_per_language_for_project.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_mt_settings_per_language_for_project.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_mt_settings_per_language_for_project.ApiResponseFor501) | Not implemented

#### set_mt_settings_per_language_for_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MTSettingsPerLanguageListDto**](../../models/MTSettingsPerLanguageListDto.md) |  | 


#### set_mt_settings_per_language_for_project.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_per_language_for_project.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_per_language_for_project.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_per_language_for_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_per_language_for_project.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_per_language_for_project.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_per_language_for_project.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_per_language_for_project.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_per_language_for_project.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_per_language_for_project.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_mt_settings_per_language_for_project.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_project_qa_settings_v2**
<a id="set_project_qa_settings_v2"></a>
> QASettingsDtoV2 set_project_qa_settings_v2(project_uid)

Edit quality assurance settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.edit_qa_settings_dto_v2 import EditQASettingsDtoV2
from openapi_client.model.qa_settings_dto_v2 import QASettingsDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit quality assurance settings
        api_response = api_instance.set_project_qa_settings_v2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_project_qa_settings_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = EditQASettingsDtoV2(
        checks=[
            dict(
                "key": dict(),
            )
        ],
    )
    try:
        # Edit quality assurance settings
        api_response = api_instance.set_project_qa_settings_v2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_project_qa_settings_v2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EditQASettingsDtoV2**](../../models/EditQASettingsDtoV2.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_project_qa_settings_v2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#set_project_qa_settings_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_project_qa_settings_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_project_qa_settings_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_project_qa_settings_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_project_qa_settings_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_project_qa_settings_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_project_qa_settings_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_project_qa_settings_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_project_qa_settings_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_project_qa_settings_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_project_qa_settings_v2.ApiResponseFor501) | Not implemented

#### set_project_qa_settings_v2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**QASettingsDtoV2**](../../models/QASettingsDtoV2.md) |  | 


#### set_project_qa_settings_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_qa_settings_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_qa_settings_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_qa_settings_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_qa_settings_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_qa_settings_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_qa_settings_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_qa_settings_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_qa_settings_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_qa_settings_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_qa_settings_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_project_status**
<a id="set_project_status"></a>
> set_project_status(project_uid)

Edit project status

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.set_project_status_dto import SetProjectStatusDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit project status
        api_response = api_instance.set_project_status(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_project_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = SetProjectStatusDto(
        status="NEW",
    )
    try:
        # Edit project status
        api_response = api_instance.set_project_status(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_project_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetProjectStatusDto**](../../models/SetProjectStatusDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#set_project_status.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#set_project_status.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_project_status.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_project_status.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_project_status.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_project_status.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_project_status.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_project_status.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_project_status.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_project_status.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_project_status.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_project_status.ApiResponseFor501) | Not implemented

#### set_project_status.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_status.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_project_term_bases**
<a id="set_project_term_bases"></a>
> ProjectTermBaseListDto set_project_term_bases(project_uid)

Edit term bases

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.set_term_base_dto import SetTermBaseDto
from openapi_client.model.project_term_base_list_dto import ProjectTermBaseListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit term bases
        api_response = api_instance.set_project_term_bases(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_project_term_bases: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = SetTermBaseDto(
        read_term_bases=[
            IdReference(
                id="id_example",
            )
        ],
,
,
        target_lang="target_lang_example",
    )
    try:
        # Edit term bases
        api_response = api_instance.set_project_term_bases(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_project_term_bases: %s\n" % e)
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
[**SetTermBaseDto**](../../models/SetTermBaseDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_project_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#set_project_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_project_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_project_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_project_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_project_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_project_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_project_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_project_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_project_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_project_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_project_term_bases.ApiResponseFor501) | Not implemented

#### set_project_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTermBaseListDto**](../../models/ProjectTermBaseListDto.md) |  | 


#### set_project_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_project_trans_memories_v3**
<a id="set_project_trans_memories_v3"></a>
> ProjectTransMemoryListDtoV3 set_project_trans_memories_v3(project_uid)

Edit translation memories

If user wants to edit “All target languages” or \"All workflow steps”,                         but there are already varied TM settings for individual languages or steps,                         then the user risks to overwrite these individual choices.

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.set_project_trans_memories_v3_dto import SetProjectTransMemoriesV3Dto
from openapi_client.model.project_trans_memory_list_dto_v3 import ProjectTransMemoryListDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit translation memories
        api_response = api_instance.set_project_trans_memories_v3(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_project_trans_memories_v3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = SetProjectTransMemoriesV3Dto(
        data_per_context=[
            SetContextTransMemoriesDtoV3Dto(
                trans_memories=[
                    SetProjectTransMemoryV3Dto(
                        trans_memory=UidReference(
                            uid="uid_example",
                        ),
                        read_mode=True,
                        write_mode=True,
                        penalty=0,
                        apply_penalty_to101_only=True,
                        order=1,
                    )
                ],
                target_lang="target_lang_example",
,
                order_enabled=True,
            )
        ],
    )
    try:
        # Edit translation memories
        api_response = api_instance.set_project_trans_memories_v3(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->set_project_trans_memories_v3: %s\n" % e)
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
[**SetProjectTransMemoriesV3Dto**](../../models/SetProjectTransMemoriesV3Dto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_project_trans_memories_v3.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#set_project_trans_memories_v3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_project_trans_memories_v3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_project_trans_memories_v3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_project_trans_memories_v3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_project_trans_memories_v3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_project_trans_memories_v3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_project_trans_memories_v3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_project_trans_memories_v3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_project_trans_memories_v3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_project_trans_memories_v3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_project_trans_memories_v3.ApiResponseFor501) | Not implemented

#### set_project_trans_memories_v3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTransMemoryListDtoV3**](../../models/ProjectTransMemoryListDtoV3.md) |  | 


#### set_project_trans_memories_v3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_trans_memories_v3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_trans_memories_v3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_trans_memories_v3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_trans_memories_v3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_trans_memories_v3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_trans_memories_v3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_trans_memories_v3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_trans_memories_v3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_trans_memories_v3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_trans_memories_v3.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_file_naming_settings**
<a id="update_file_naming_settings"></a>
> FileNamingSettingsDto update_file_naming_settings(project_uid)

Update file naming settings for project

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_api
from openapi_client.model.file_naming_settings_dto import FileNamingSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_api.ProjectApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Update file naming settings for project
        api_response = api_instance.update_file_naming_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->update_file_naming_settings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = FileNamingSettingsDto(
        rename_completed=True,
        completed_file_pattern="completed_file_pattern_example",
        target_folder_path="target_folder_path_example",
    )
    try:
        # Update file naming settings for project
        api_response = api_instance.update_file_naming_settings(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectApi->update_file_naming_settings: %s\n" % e)
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
[**FileNamingSettingsDto**](../../models/FileNamingSettingsDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_file_naming_settings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#update_file_naming_settings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_file_naming_settings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_file_naming_settings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_file_naming_settings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_file_naming_settings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_file_naming_settings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_file_naming_settings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_file_naming_settings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_file_naming_settings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_file_naming_settings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_file_naming_settings.ApiResponseFor501) | Not implemented

#### update_file_naming_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FileNamingSettingsDto**](../../models/FileNamingSettingsDto.md) |  | 


#### update_file_naming_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_file_naming_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_file_naming_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_file_naming_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_file_naming_settings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_file_naming_settings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_file_naming_settings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_file_naming_settings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_file_naming_settings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_file_naming_settings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_file_naming_settings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

