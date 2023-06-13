<a id="__pageTop"></a>
# openapi_client.apis.tags.project_template_api.ProjectTemplateApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_linguists_from_template**](#assign_linguists_from_template) | **post** /api2/v1/projects/{projectUid}/applyTemplate/{templateUid}/assignProviders | Assigns providers from template
[**assign_linguists_from_template_to_job_parts**](#assign_linguists_from_template_to_job_parts) | **post** /api2/v1/projects/{projectUid}/applyTemplate/{templateUid}/assignProviders/forJobParts | Assigns providers from template (specific jobs)
[**assignable_templates**](#assignable_templates) | **get** /api2/v1/projects/{projectUid}/assignableTemplates | List assignable templates
[**create_custom_fields1**](#create_custom_fields1) | **post** /api2/v1/projectTemplates/{projectTemplateUid}/customFields | Create custom field instances
[**create_project_from_template_v2**](#create_project_from_template_v2) | **post** /api2/v2/projects/applyTemplate/{templateUid} | Create project from template
[**create_project_from_template_v2_async**](#create_project_from_template_v2_async) | **post** /api2/v2/projects/applyTemplate/async/{templateUid} | Create project from template (async)
[**create_project_template**](#create_project_template) | **post** /api2/v1/projectTemplates | Create project template
[**delete_custom_field2**](#delete_custom_field2) | **delete** /api2/v1/projectTemplates/{projectTemplateUid}/customFields/{fieldInstanceUid} | Delete custom field of project template
[**delete_project_template**](#delete_project_template) | **delete** /api2/v1/projectTemplates/{projectTemplateUid} | Delete project template
[**edit_custom_field1**](#edit_custom_field1) | **put** /api2/v1/projectTemplates/{projectTemplateUid}/customFields/{fieldInstanceUid} | Edit custom field of project template
[**edit_custom_fields1**](#edit_custom_fields1) | **put** /api2/v1/projectTemplates/{projectTemplateUid}/customFields | Edit custom fields of the project template (batch)
[**edit_project_template**](#edit_project_template) | **put** /api2/v1/projectTemplates/{projectTemplateUid} | Edit project template
[**edit_project_template_access_settings**](#edit_project_template_access_settings) | **put** /api2/v1/projectTemplates/{projectTemplateUid}/accessSettings | Edit project template access and security settings
[**edit_project_template_import_settings**](#edit_project_template_import_settings) | **put** /api2/v1/projectTemplates/{projectTemplateUid}/importSettings | Edit project template import settings
[**get_analyse_settings_for_project_template**](#get_analyse_settings_for_project_template) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/analyseSettings | Get analyse settings
[**get_custom_field2**](#get_custom_field2) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/customFields/{fieldInstanceUid} | Get custom field of project template
[**get_custom_fields_page1**](#get_custom_fields_page1) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/customFields | Get custom fields of project template (page)
[**get_import_settings_for_project_template**](#get_import_settings_for_project_template) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/importSettings | Get import settings
[**get_machine_translate_settings_for_project_template**](#get_machine_translate_settings_for_project_template) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/mtSettings | Get project template machine translate settings
[**get_pre_translate_settings_for_project_template2**](#get_pre_translate_settings_for_project_template2) | **get** /api2/v3/projectTemplates/{projectTemplateUid}/preTranslateSettings | Get Pre-translate settings
[**get_project_template**](#get_project_template) | **get** /api2/v1/projectTemplates/{projectTemplateUid} | Get project template
[**get_project_template_access_settings**](#get_project_template_access_settings) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/accessSettings | Get project template access and security settings
[**get_project_template_qa_settings**](#get_project_template_qa_settings) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/qaSettings | Get quality assurance settings
[**get_project_template_term_bases**](#get_project_template_term_bases) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/termBases | Get term bases
[**get_project_template_trans_memories2**](#get_project_template_trans_memories2) | **get** /api2/v3/projectTemplates/{projectTemplateUid}/transMemories | Get translation memories
[**get_project_templates**](#get_project_templates) | **get** /api2/v1/projectTemplates | List project templates
[**relevant_trans_memories**](#relevant_trans_memories) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/transMemories/relevant | List project template relevant translation memories
[**set_project_template_qa_settings**](#set_project_template_qa_settings) | **put** /api2/v1/projectTemplates/{projectTemplateUid}/qaSettings | Edit quality assurance settings
[**set_project_template_term_bases**](#set_project_template_term_bases) | **put** /api2/v1/projectTemplates/{projectTemplateUid}/termBases | Edit term bases in project template
[**set_project_template_trans_memories_v2**](#set_project_template_trans_memories_v2) | **put** /api2/v2/projectTemplates/{projectTemplateUid}/transMemories | Edit translation memories
[**update_analyse_settings_for_project_template**](#update_analyse_settings_for_project_template) | **put** /api2/v1/projectTemplates/{projectTemplateUid}/analyseSettings | Edit analyse settings
[**update_pre_translate_settings_for_project_template2**](#update_pre_translate_settings_for_project_template2) | **put** /api2/v3/projectTemplates/{projectTemplateUid}/preTranslateSettings | Update Pre-translate settings

# **assign_linguists_from_template**
<a id="assign_linguists_from_template"></a>
> JobPartsDto assign_linguists_from_template(template_uidproject_uid)

Assigns providers from template

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

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
        print("Exception when calling ProjectTemplateApi->assign_linguists_from_template: %s\n" % e)
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
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

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
        print("Exception when calling ProjectTemplateApi->assign_linguists_from_template_to_job_parts: %s\n" % e)

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
        print("Exception when calling ProjectTemplateApi->assign_linguists_from_template_to_job_parts: %s\n" % e)
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

# **assignable_templates**
<a id="assignable_templates"></a>
> AssignableTemplatesDto assignable_templates(project_uid)

List assignable templates

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

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
        print("Exception when calling ProjectTemplateApi->assignable_templates: %s\n" % e)
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

# **create_custom_fields1**
<a id="create_custom_fields1"></a>
> CustomFieldInstancesDto create_custom_fields1(project_template_uid)

Create custom field instances

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Create custom field instances
        api_response = api_instance.create_custom_fields1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->create_custom_fields1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
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
        api_response = api_instance.create_custom_fields1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->create_custom_fields1: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_custom_fields1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#create_custom_fields1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_custom_fields1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_custom_fields1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_custom_fields1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_custom_fields1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_custom_fields1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_custom_fields1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_custom_fields1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_custom_fields1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_custom_fields1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_custom_fields1.ApiResponseFor501) | Not implemented

#### create_custom_fields1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomFieldInstancesDto**](../../models/CustomFieldInstancesDto.md) |  | 


#### create_custom_fields1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_custom_fields1.ApiResponseFor501
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
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

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
        print("Exception when calling ProjectTemplateApi->create_project_from_template_v2: %s\n" % e)

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
        print("Exception when calling ProjectTemplateApi->create_project_from_template_v2: %s\n" % e)
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
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

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
        print("Exception when calling ProjectTemplateApi->create_project_from_template_v2_async: %s\n" % e)

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
        print("Exception when calling ProjectTemplateApi->create_project_from_template_v2_async: %s\n" % e)
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

# **create_project_template**
<a id="create_project_template"></a>
> ProjectTemplateDto create_project_template(body)

Create project template

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from openapi_client.model.project_template_create_action_dto import ProjectTemplateCreateActionDto
from openapi_client.model.project_template_dto import ProjectTemplateDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    body = ProjectTemplateCreateActionDto(
        project=UidReference(
            uid="uid_example",
        ),
        name="name_example",
,
        use_dynamic_title=True,
        dynamic_title="dynamic_title_example",
    )
    try:
        # Create project template
        api_response = api_instance.create_project_template(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->create_project_template: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTemplateCreateActionDto**](../../models/ProjectTemplateCreateActionDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_project_template.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_project_template.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_project_template.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_project_template.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_project_template.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_project_template.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_project_template.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_project_template.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_project_template.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_project_template.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_project_template.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_project_template.ApiResponseFor501) | Not implemented

#### create_project_template.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTemplateDto**](../../models/ProjectTemplateDto.md) |  | 


#### create_project_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_template.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_template.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_template.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_template.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_template.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_template.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_project_template.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_custom_field2**
<a id="delete_custom_field2"></a>
> delete_custom_field2(project_template_uidfield_instance_uid)

Delete custom field of project template

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
        'fieldInstanceUid': "fieldInstanceUid_example",
    }
    try:
        # Delete custom field of project template
        api_response = api_instance.delete_custom_field2(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->delete_custom_field2: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 
fieldInstanceUid | FieldInstanceUidSchema | | 

# ProjectTemplateUidSchema

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
400 | [ApiResponseFor400](#delete_custom_field2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_custom_field2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_custom_field2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_custom_field2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_custom_field2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_custom_field2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_custom_field2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_custom_field2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_custom_field2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_custom_field2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_custom_field2.ApiResponseFor501) | Not implemented

#### delete_custom_field2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_custom_field2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_project_template**
<a id="delete_project_template"></a>
> delete_project_template(project_template_uid)

Delete project template

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Delete project template
        api_response = api_instance.delete_project_template(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->delete_project_template: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_project_template.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_project_template.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_project_template.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_project_template.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_project_template.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_project_template.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_project_template.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_project_template.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_project_template.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_project_template.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_project_template.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_project_template.ApiResponseFor501) | Not implemented

#### delete_project_template.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_project_template.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_custom_field1**
<a id="edit_custom_field1"></a>
> CustomFieldInstanceDto edit_custom_field1(project_template_uidfield_instance_uid)

Edit custom field of project template

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
        'fieldInstanceUid': "fieldInstanceUid_example",
    }
    try:
        # Edit custom field of project template
        api_response = api_instance.edit_custom_field1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->edit_custom_field1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
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
        # Edit custom field of project template
        api_response = api_instance.edit_custom_field1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->edit_custom_field1: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 
fieldInstanceUid | FieldInstanceUidSchema | | 

# ProjectTemplateUidSchema

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
200 | [ApiResponseFor200](#edit_custom_field1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_custom_field1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_custom_field1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_custom_field1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_custom_field1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_custom_field1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_custom_field1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_custom_field1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_custom_field1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_custom_field1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_custom_field1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_custom_field1.ApiResponseFor501) | Not implemented

#### edit_custom_field1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomFieldInstanceDto**](../../models/CustomFieldInstanceDto.md) |  | 


#### edit_custom_field1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_field1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_custom_fields1**
<a id="edit_custom_fields1"></a>
> CustomFieldInstancesDto edit_custom_fields1(project_template_uid)

Edit custom fields of the project template (batch)

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Edit custom fields of the project template (batch)
        api_response = api_instance.edit_custom_fields1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->edit_custom_fields1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
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
        # Edit custom fields of the project template (batch)
        api_response = api_instance.edit_custom_fields1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->edit_custom_fields1: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_custom_fields1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_custom_fields1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_custom_fields1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_custom_fields1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_custom_fields1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_custom_fields1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_custom_fields1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_custom_fields1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_custom_fields1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_custom_fields1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_custom_fields1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_custom_fields1.ApiResponseFor501) | Not implemented

#### edit_custom_fields1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomFieldInstancesDto**](../../models/CustomFieldInstancesDto.md) |  | 


#### edit_custom_fields1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_custom_fields1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_project_template**
<a id="edit_project_template"></a>
> ProjectTemplateDto edit_project_template(project_template_uidbody)

Edit project template

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from openapi_client.model.project_template_edit_dto import ProjectTemplateEditDto
from openapi_client.model.project_template_dto import ProjectTemplateDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    body = ProjectTemplateEditDto(
        name="name_example",
        template_name="template_name_example",
        source_lang="source_lang_example",
        target_langs=[
            "target_langs_example"
        ],
        use_dynamic_title=True,
        dynamic_title="dynamic_title_example",
        notify_provider=ProjectTemplateNotifyProviderDto(
            organization_email_template=dict(),
            notification_interval_in_minutes=0,
        ),
        work_flow_settings=[
            WorkflowStepSettingsEditDto(
                workflow_step=IdReference(
                    id="id_example",
                ),
                assigned_to=[
                    ProjectTemplateWorkflowSettingsAssignedToDto(
                        target_lang="target_lang_example",
                        providers=[
                            ProviderReference()
                        ],
                    )
                ],
                notify_provider=ProjectTemplateNotifyProviderDto(),
                lqa_profile=UidReference(
                    uid="uid_example",
                ),
            )
        ],
        client=IdReference(),
        cost_center=IdReference(),
        business_unit=IdReference(),
        domain=IdReference(),
        sub_domain=IdReference(),
        vendor=IdReference(),
,
        note="note_example",
        file_handover=True,
        assigned_to=[
            ProjectTemplateWorkflowSettingsAssignedToDto()
        ],
    )
    try:
        # Edit project template
        api_response = api_instance.edit_project_template(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->edit_project_template: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**ProjectTemplateEditDto**](../../models/ProjectTemplateEditDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_project_template.ApiResponseFor200) | Edited
400 | [ApiResponseFor400](#edit_project_template.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_project_template.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_project_template.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_project_template.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_project_template.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_project_template.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_project_template.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_project_template.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_project_template.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_project_template.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_project_template.ApiResponseFor501) | Not implemented

#### edit_project_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTemplateDto**](../../models/ProjectTemplateDto.md) |  | 


#### edit_project_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_project_template_access_settings**
<a id="edit_project_template_access_settings"></a>
> ProjectSecuritySettingsDtoV2 edit_project_template_access_settings(project_template_uid)

Edit project template access and security settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Edit project template access and security settings
        api_response = api_instance.edit_project_template_access_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->edit_project_template_access_settings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
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
        # Edit project template access and security settings
        api_response = api_instance.edit_project_template_access_settings(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->edit_project_template_access_settings: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_project_template_access_settings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_project_template_access_settings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_project_template_access_settings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_project_template_access_settings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_project_template_access_settings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_project_template_access_settings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_project_template_access_settings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_project_template_access_settings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_project_template_access_settings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_project_template_access_settings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_project_template_access_settings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_project_template_access_settings.ApiResponseFor501) | Not implemented

#### edit_project_template_access_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectSecuritySettingsDtoV2**](../../models/ProjectSecuritySettingsDtoV2.md) |  | 


#### edit_project_template_access_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_access_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_access_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_access_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_access_settings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_access_settings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_access_settings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_access_settings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_access_settings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_access_settings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_access_settings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_project_template_import_settings**
<a id="edit_project_template_import_settings"></a>
> FileImportSettingsDto edit_project_template_import_settings(project_template_uid)

Edit project template import settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Edit project template import settings
        api_response = api_instance.edit_project_template_import_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->edit_project_template_import_settings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
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
        # Edit project template import settings
        api_response = api_instance.edit_project_template_import_settings(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->edit_project_template_import_settings: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_project_template_import_settings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_project_template_import_settings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_project_template_import_settings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_project_template_import_settings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_project_template_import_settings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_project_template_import_settings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_project_template_import_settings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_project_template_import_settings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_project_template_import_settings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_project_template_import_settings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_project_template_import_settings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_project_template_import_settings.ApiResponseFor501) | Not implemented

#### edit_project_template_import_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FileImportSettingsDto**](../../models/FileImportSettingsDto.md) |  | 


#### edit_project_template_import_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_import_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_import_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_import_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_import_settings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_import_settings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_import_settings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_import_settings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_import_settings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_import_settings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_project_template_import_settings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_analyse_settings_for_project_template**
<a id="get_analyse_settings_for_project_template"></a>
> AbstractAnalyseSettingsDto get_analyse_settings_for_project_template(project_template_uid)

Get analyse settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from openapi_client.model.abstract_analyse_settings_dto import AbstractAnalyseSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Get analyse settings
        api_response = api_instance.get_analyse_settings_for_project_template(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_analyse_settings_for_project_template: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_analyse_settings_for_project_template.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_analyse_settings_for_project_template.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_analyse_settings_for_project_template.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_analyse_settings_for_project_template.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_analyse_settings_for_project_template.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_analyse_settings_for_project_template.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_analyse_settings_for_project_template.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_analyse_settings_for_project_template.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_analyse_settings_for_project_template.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_analyse_settings_for_project_template.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_analyse_settings_for_project_template.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_analyse_settings_for_project_template.ApiResponseFor501) | Not implemented

#### get_analyse_settings_for_project_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AbstractAnalyseSettingsDto**](../../models/AbstractAnalyseSettingsDto.md) |  | 


#### get_analyse_settings_for_project_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project_template.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project_template.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project_template.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project_template.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project_template.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project_template.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_settings_for_project_template.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_custom_field2**
<a id="get_custom_field2"></a>
> CustomFieldInstanceDto get_custom_field2(project_template_uidfield_instance_uid)

Get custom field of project template

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
        'fieldInstanceUid': "fieldInstanceUid_example",
    }
    try:
        # Get custom field of project template
        api_response = api_instance.get_custom_field2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_custom_field2: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 
fieldInstanceUid | FieldInstanceUidSchema | | 

# ProjectTemplateUidSchema

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
200 | [ApiResponseFor200](#get_custom_field2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_custom_field2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_custom_field2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_custom_field2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_custom_field2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_custom_field2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_custom_field2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_custom_field2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_custom_field2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_custom_field2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_custom_field2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_custom_field2.ApiResponseFor501) | Not implemented

#### get_custom_field2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomFieldInstanceDto**](../../models/CustomFieldInstanceDto.md) |  | 


#### get_custom_field2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_field2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_custom_fields_page1**
<a id="get_custom_fields_page1"></a>
> PageDtoCustomFieldInstanceDto get_custom_fields_page1(project_template_uid)

Get custom fields of project template (page)

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    query_params = {
    }
    try:
        # Get custom fields of project template (page)
        api_response = api_instance.get_custom_fields_page1(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_custom_fields_page1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
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
        # Get custom fields of project template (page)
        api_response = api_instance.get_custom_fields_page1(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_custom_fields_page1: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_custom_fields_page1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_custom_fields_page1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_custom_fields_page1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_custom_fields_page1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_custom_fields_page1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_custom_fields_page1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_custom_fields_page1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_custom_fields_page1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_custom_fields_page1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_custom_fields_page1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_custom_fields_page1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_custom_fields_page1.ApiResponseFor501) | Not implemented

#### get_custom_fields_page1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoCustomFieldInstanceDto**](../../models/PageDtoCustomFieldInstanceDto.md) |  | 


#### get_custom_fields_page1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_custom_fields_page1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_import_settings_for_project_template**
<a id="get_import_settings_for_project_template"></a>
> FileImportSettingsDto get_import_settings_for_project_template(project_template_uid)

Get import settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Get import settings
        api_response = api_instance.get_import_settings_for_project_template(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_import_settings_for_project_template: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_import_settings_for_project_template.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_import_settings_for_project_template.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_import_settings_for_project_template.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_import_settings_for_project_template.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_import_settings_for_project_template.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_import_settings_for_project_template.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_import_settings_for_project_template.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_import_settings_for_project_template.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_import_settings_for_project_template.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_import_settings_for_project_template.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_import_settings_for_project_template.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_import_settings_for_project_template.ApiResponseFor501) | Not implemented

#### get_import_settings_for_project_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FileImportSettingsDto**](../../models/FileImportSettingsDto.md) |  | 


#### get_import_settings_for_project_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings_for_project_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings_for_project_template.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings_for_project_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings_for_project_template.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings_for_project_template.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings_for_project_template.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings_for_project_template.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings_for_project_template.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings_for_project_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_import_settings_for_project_template.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_machine_translate_settings_for_project_template**
<a id="get_machine_translate_settings_for_project_template"></a>
> MTSettingsPerLanguageListDto get_machine_translate_settings_for_project_template(project_template_uid)

Get project template machine translate settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Get project template machine translate settings
        api_response = api_instance.get_machine_translate_settings_for_project_template(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_machine_translate_settings_for_project_template: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_machine_translate_settings_for_project_template.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_machine_translate_settings_for_project_template.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_machine_translate_settings_for_project_template.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_machine_translate_settings_for_project_template.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_machine_translate_settings_for_project_template.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_machine_translate_settings_for_project_template.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_machine_translate_settings_for_project_template.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_machine_translate_settings_for_project_template.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_machine_translate_settings_for_project_template.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_machine_translate_settings_for_project_template.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_machine_translate_settings_for_project_template.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_machine_translate_settings_for_project_template.ApiResponseFor501) | Not implemented

#### get_machine_translate_settings_for_project_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MTSettingsPerLanguageListDto**](../../models/MTSettingsPerLanguageListDto.md) |  | 


#### get_machine_translate_settings_for_project_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_machine_translate_settings_for_project_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_machine_translate_settings_for_project_template.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_machine_translate_settings_for_project_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_machine_translate_settings_for_project_template.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_machine_translate_settings_for_project_template.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_machine_translate_settings_for_project_template.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_machine_translate_settings_for_project_template.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_machine_translate_settings_for_project_template.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_machine_translate_settings_for_project_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_machine_translate_settings_for_project_template.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pre_translate_settings_for_project_template2**
<a id="get_pre_translate_settings_for_project_template2"></a>
> PreTranslateSettingsV3Dto get_pre_translate_settings_for_project_template2(project_template_uid)

Get Pre-translate settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Get Pre-translate settings
        api_response = api_instance.get_pre_translate_settings_for_project_template2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_pre_translate_settings_for_project_template2: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pre_translate_settings_for_project_template2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_pre_translate_settings_for_project_template2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_pre_translate_settings_for_project_template2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_pre_translate_settings_for_project_template2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_pre_translate_settings_for_project_template2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_pre_translate_settings_for_project_template2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_pre_translate_settings_for_project_template2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_pre_translate_settings_for_project_template2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_pre_translate_settings_for_project_template2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_pre_translate_settings_for_project_template2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_pre_translate_settings_for_project_template2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_pre_translate_settings_for_project_template2.ApiResponseFor501) | Not implemented

#### get_pre_translate_settings_for_project_template2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PreTranslateSettingsV3Dto**](../../models/PreTranslateSettingsV3Dto.md) |  | 


#### get_pre_translate_settings_for_project_template2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project_template2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project_template2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project_template2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project_template2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project_template2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project_template2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project_template2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project_template2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project_template2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_pre_translate_settings_for_project_template2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_template**
<a id="get_project_template"></a>
> ProjectTemplateDto get_project_template(project_template_uid)

Get project template

Note: importSettings in response is deprecated and will be always null

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from openapi_client.model.project_template_dto import ProjectTemplateDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Get project template
        api_response = api_instance.get_project_template(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_project_template: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_template.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_template.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_template.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_template.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_template.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_template.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_template.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_template.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_template.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_template.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_template.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_template.ApiResponseFor501) | Not implemented

#### get_project_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTemplateDto**](../../models/ProjectTemplateDto.md) |  | 


#### get_project_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_template_access_settings**
<a id="get_project_template_access_settings"></a>
> ProjectSecuritySettingsDtoV2 get_project_template_access_settings(project_template_uid)

Get project template access and security settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Get project template access and security settings
        api_response = api_instance.get_project_template_access_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_project_template_access_settings: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_template_access_settings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_template_access_settings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_template_access_settings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_template_access_settings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_template_access_settings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_template_access_settings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_template_access_settings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_template_access_settings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_template_access_settings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_template_access_settings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_template_access_settings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_template_access_settings.ApiResponseFor501) | Not implemented

#### get_project_template_access_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectSecuritySettingsDtoV2**](../../models/ProjectSecuritySettingsDtoV2.md) |  | 


#### get_project_template_access_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_access_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_access_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_access_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_access_settings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_access_settings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_access_settings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_access_settings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_access_settings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_access_settings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_access_settings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_template_qa_settings**
<a id="get_project_template_qa_settings"></a>
> QASettingsDtoV2 get_project_template_qa_settings(project_template_uid)

Get quality assurance settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Get quality assurance settings
        api_response = api_instance.get_project_template_qa_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_project_template_qa_settings: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_template_qa_settings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_template_qa_settings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_template_qa_settings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_template_qa_settings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_template_qa_settings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_template_qa_settings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_template_qa_settings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_template_qa_settings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_template_qa_settings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_template_qa_settings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_template_qa_settings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_template_qa_settings.ApiResponseFor501) | Not implemented

#### get_project_template_qa_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**QASettingsDtoV2**](../../models/QASettingsDtoV2.md) |  | 


#### get_project_template_qa_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_qa_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_qa_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_qa_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_qa_settings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_qa_settings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_qa_settings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_qa_settings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_qa_settings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_qa_settings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_qa_settings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_template_term_bases**
<a id="get_project_template_term_bases"></a>
> ProjectTemplateTermBaseListDto get_project_template_term_bases(project_template_uid)

Get term bases

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from openapi_client.model.project_template_term_base_list_dto import ProjectTemplateTermBaseListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Get term bases
        api_response = api_instance.get_project_template_term_bases(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_project_template_term_bases: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_template_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_template_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_template_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_template_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_template_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_template_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_template_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_template_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_template_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_template_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_template_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_template_term_bases.ApiResponseFor501) | Not implemented

#### get_project_template_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTemplateTermBaseListDto**](../../models/ProjectTemplateTermBaseListDto.md) |  | 


#### get_project_template_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_template_trans_memories2**
<a id="get_project_template_trans_memories2"></a>
> ProjectTemplateTransMemoryListDtoV3 get_project_template_trans_memories2(project_template_uid)

Get translation memories

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from openapi_client.model.project_template_trans_memory_list_dto_v3 import ProjectTemplateTransMemoryListDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    query_params = {
    }
    try:
        # Get translation memories
        api_response = api_instance.get_project_template_trans_memories2(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_project_template_trans_memories2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    query_params = {
        'targetLang': "targetLang_example",
        'wfStepUid': "wfStepUid_example",
    }
    try:
        # Get translation memories
        api_response = api_instance.get_project_template_trans_memories2(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_project_template_trans_memories2: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_template_trans_memories2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_template_trans_memories2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_template_trans_memories2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_template_trans_memories2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_template_trans_memories2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_template_trans_memories2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_template_trans_memories2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_template_trans_memories2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_template_trans_memories2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_template_trans_memories2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_template_trans_memories2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_template_trans_memories2.ApiResponseFor501) | Not implemented

#### get_project_template_trans_memories2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTemplateTransMemoryListDtoV3**](../../models/ProjectTemplateTransMemoryListDtoV3.md) |  | 


#### get_project_template_trans_memories2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_trans_memories2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_trans_memories2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_trans_memories2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_trans_memories2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_trans_memories2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_trans_memories2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_trans_memories2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_trans_memories2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_trans_memories2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_trans_memories2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_templates**
<a id="get_project_templates"></a>
> PageDtoProjectTemplateReference get_project_templates()

List project templates

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from openapi_client.model.page_dto_project_template_reference import PageDtoProjectTemplateReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'clientId': 1,
        'clientName': "clientName_example",
        'ownerUid': "ownerUid_example",
        'domainName': "domainName_example",
        'subDomainName': "subDomainName_example",
        'costCenterId': 1,
        'costCenterName': "costCenterName_example",
        'businessUnitName': "businessUnitName_example",
        'sort': "dateCreated",
        'direction': "desc",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List project templates
        api_response = api_instance.get_project_templates(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->get_project_templates: %s\n" % e)
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
ownerUid | OwnerUidSchema | | optional
domainName | DomainNameSchema | | optional
subDomainName | SubDomainNameSchema | | optional
costCenterId | CostCenterIdSchema | | optional
costCenterName | CostCenterNameSchema | | optional
businessUnitName | BusinessUnitNameSchema | | optional
sort | SortSchema | | optional
direction | DirectionSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


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

# OwnerUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DomainNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

# BusinessUnitNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "dateCreated"

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "desc"

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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_templates.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_templates.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_templates.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_templates.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_templates.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_templates.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_templates.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_templates.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_templates.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_templates.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_templates.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_templates.ApiResponseFor501) | Not implemented

#### get_project_templates.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoProjectTemplateReference**](../../models/PageDtoProjectTemplateReference.md) |  | 


#### get_project_templates.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_templates.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_templates.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_templates.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_templates.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_templates.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_templates.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_templates.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_templates.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_templates.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_templates.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **relevant_trans_memories**
<a id="relevant_trans_memories"></a>
> PageDtoTransMemoryDto relevant_trans_memories(project_template_uid)

List project template relevant translation memories

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    query_params = {
    }
    try:
        # List project template relevant translation memories
        api_response = api_instance.relevant_trans_memories(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->relevant_trans_memories: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
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
        # List project template relevant translation memories
        api_response = api_instance.relevant_trans_memories(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->relevant_trans_memories: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#relevant_trans_memories.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#relevant_trans_memories.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#relevant_trans_memories.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#relevant_trans_memories.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#relevant_trans_memories.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#relevant_trans_memories.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#relevant_trans_memories.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#relevant_trans_memories.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#relevant_trans_memories.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#relevant_trans_memories.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#relevant_trans_memories.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#relevant_trans_memories.ApiResponseFor501) | Not implemented

#### relevant_trans_memories.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoTransMemoryDto**](../../models/PageDtoTransMemoryDto.md) |  | 


#### relevant_trans_memories.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_trans_memories.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_project_template_qa_settings**
<a id="set_project_template_qa_settings"></a>
> QASettingsDtoV2 set_project_template_qa_settings(project_template_uid)

Edit quality assurance settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Edit quality assurance settings
        api_response = api_instance.set_project_template_qa_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->set_project_template_qa_settings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
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
        api_response = api_instance.set_project_template_qa_settings(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->set_project_template_qa_settings: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_project_template_qa_settings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#set_project_template_qa_settings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_project_template_qa_settings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_project_template_qa_settings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_project_template_qa_settings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_project_template_qa_settings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_project_template_qa_settings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_project_template_qa_settings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_project_template_qa_settings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_project_template_qa_settings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_project_template_qa_settings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_project_template_qa_settings.ApiResponseFor501) | Not implemented

#### set_project_template_qa_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**QASettingsDtoV2**](../../models/QASettingsDtoV2.md) |  | 


#### set_project_template_qa_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_qa_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_qa_settings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_qa_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_qa_settings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_qa_settings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_qa_settings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_qa_settings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_qa_settings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_qa_settings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_qa_settings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_project_template_term_bases**
<a id="set_project_template_term_bases"></a>
> ProjectTemplateTermBaseListDto set_project_template_term_bases(project_template_uid)

Edit term bases in project template

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from openapi_client.model.project_template_term_base_list_dto import ProjectTemplateTermBaseListDto
from openapi_client.model.set_project_template_term_base_dto import SetProjectTemplateTermBaseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Edit term bases in project template
        api_response = api_instance.set_project_template_term_bases(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->set_project_template_term_bases: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    body = SetProjectTemplateTermBaseDto(
        read_term_bases=[
            IdReference(
                id="id_example",
            )
        ],
,
,
        target_lang="target_lang_example",
,
    )
    try:
        # Edit term bases in project template
        api_response = api_instance.set_project_template_term_bases(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->set_project_template_term_bases: %s\n" % e)
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
[**SetProjectTemplateTermBaseDto**](../../models/SetProjectTemplateTermBaseDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_project_template_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#set_project_template_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_project_template_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_project_template_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_project_template_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_project_template_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_project_template_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_project_template_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_project_template_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_project_template_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_project_template_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_project_template_term_bases.ApiResponseFor501) | Not implemented

#### set_project_template_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTemplateTermBaseListDto**](../../models/ProjectTemplateTermBaseListDto.md) |  | 


#### set_project_template_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_project_template_trans_memories_v2**
<a id="set_project_template_trans_memories_v2"></a>
> ProjectTemplateTransMemoryListV2Dto set_project_template_trans_memories_v2(project_template_uid)

Edit translation memories

If user wants to edit “All target languages” or \"All workflow steps”,                         but there are already varied TM settings for individual languages or steps,                         then the user risks to overwrite these individual choices.

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from openapi_client.model.project_template_trans_memory_list_v2_dto import ProjectTemplateTransMemoryListV2Dto
from openapi_client.model.set_project_template_trans_memories_v2_dto import SetProjectTemplateTransMemoriesV2Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Edit translation memories
        api_response = api_instance.set_project_template_trans_memories_v2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->set_project_template_trans_memories_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    body = SetProjectTemplateTransMemoriesV2Dto(
        data_per_context=[
            SetContextPTTransMemoriesV2Dto(
                trans_memories=[
                    SetProjectTemplateTransMemoryV2Dto(
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
        api_response = api_instance.set_project_template_trans_memories_v2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->set_project_template_trans_memories_v2: %s\n" % e)
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
[**SetProjectTemplateTransMemoriesV2Dto**](../../models/SetProjectTemplateTransMemoriesV2Dto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_project_template_trans_memories_v2.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#set_project_template_trans_memories_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_project_template_trans_memories_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_project_template_trans_memories_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_project_template_trans_memories_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_project_template_trans_memories_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_project_template_trans_memories_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_project_template_trans_memories_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_project_template_trans_memories_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_project_template_trans_memories_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_project_template_trans_memories_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_project_template_trans_memories_v2.ApiResponseFor501) | Not implemented

#### set_project_template_trans_memories_v2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTemplateTransMemoryListV2Dto**](../../models/ProjectTemplateTransMemoryListV2Dto.md) |  | 


#### set_project_template_trans_memories_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_trans_memories_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_trans_memories_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_trans_memories_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_trans_memories_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_trans_memories_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_trans_memories_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_trans_memories_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_trans_memories_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_trans_memories_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_trans_memories_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_analyse_settings_for_project_template**
<a id="update_analyse_settings_for_project_template"></a>
> AbstractAnalyseSettingsDto update_analyse_settings_for_project_template(project_template_uid)

Edit analyse settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
from openapi_client.model.abstract_analyse_settings_dto import AbstractAnalyseSettingsDto
from openapi_client.model.edit_analyse_settings_dto import EditAnalyseSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Edit analyse settings
        api_response = api_instance.update_analyse_settings_for_project_template(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->update_analyse_settings_for_project_template: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    body = EditAnalyseSettingsDto(
        type="PreAnalyse",
        include_fuzzy_repetitions=True,
        separate_fuzzy_repetitions=True,
        include_non_translatables=True,
        include_machine_translation_matches=True,
        include_confirmed_segments=True,
        include_numbers=True,
        include_locked_segments=True,
        trans_memory_post_editing=True,
        non_translatable_post_editing=True,
        machine_translate_post_editing=True,
        count_source_units=True,
        include_trans_memory=True,
        naming_pattern="naming_pattern_example",
        analyze_by_language=True,
        analyze_by_provider=True,
        allow_automatic_post_analysis=True,
    )
    try:
        # Edit analyse settings
        api_response = api_instance.update_analyse_settings_for_project_template(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->update_analyse_settings_for_project_template: %s\n" % e)
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
[**EditAnalyseSettingsDto**](../../models/EditAnalyseSettingsDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_analyse_settings_for_project_template.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_analyse_settings_for_project_template.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_analyse_settings_for_project_template.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_analyse_settings_for_project_template.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_analyse_settings_for_project_template.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_analyse_settings_for_project_template.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_analyse_settings_for_project_template.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_analyse_settings_for_project_template.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_analyse_settings_for_project_template.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_analyse_settings_for_project_template.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_analyse_settings_for_project_template.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_analyse_settings_for_project_template.ApiResponseFor501) | Not implemented

#### update_analyse_settings_for_project_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AbstractAnalyseSettingsDto**](../../models/AbstractAnalyseSettingsDto.md) |  | 


#### update_analyse_settings_for_project_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_analyse_settings_for_project_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_analyse_settings_for_project_template.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_analyse_settings_for_project_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_analyse_settings_for_project_template.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_analyse_settings_for_project_template.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_analyse_settings_for_project_template.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_analyse_settings_for_project_template.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_analyse_settings_for_project_template.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_analyse_settings_for_project_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_analyse_settings_for_project_template.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_pre_translate_settings_for_project_template2**
<a id="update_pre_translate_settings_for_project_template2"></a>
> PreTranslateSettingsV3Dto update_pre_translate_settings_for_project_template2(project_template_uid)

Update Pre-translate settings

### Example

```python
import openapi_client
from openapi_client.apis.tags import project_template_api
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
    api_instance = project_template_api.ProjectTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Update Pre-translate settings
        api_response = api_instance.update_pre_translate_settings_for_project_template2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->update_pre_translate_settings_for_project_template2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
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
        api_response = api_instance.update_pre_translate_settings_for_project_template2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProjectTemplateApi->update_pre_translate_settings_for_project_template2: %s\n" % e)
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
projectTemplateUid | ProjectTemplateUidSchema | | 

# ProjectTemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_pre_translate_settings_for_project_template2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#update_pre_translate_settings_for_project_template2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_pre_translate_settings_for_project_template2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_pre_translate_settings_for_project_template2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_pre_translate_settings_for_project_template2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_pre_translate_settings_for_project_template2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_pre_translate_settings_for_project_template2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_pre_translate_settings_for_project_template2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_pre_translate_settings_for_project_template2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_pre_translate_settings_for_project_template2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_pre_translate_settings_for_project_template2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_pre_translate_settings_for_project_template2.ApiResponseFor501) | Not implemented

#### update_pre_translate_settings_for_project_template2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PreTranslateSettingsV3Dto**](../../models/PreTranslateSettingsV3Dto.md) |  | 


#### update_pre_translate_settings_for_project_template2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_pre_translate_settings_for_project_template2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_pre_translate_settings_for_project_template2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_pre_translate_settings_for_project_template2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_pre_translate_settings_for_project_template2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_pre_translate_settings_for_project_template2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_pre_translate_settings_for_project_template2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_pre_translate_settings_for_project_template2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_pre_translate_settings_for_project_template2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_pre_translate_settings_for_project_template2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_pre_translate_settings_for_project_template2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

