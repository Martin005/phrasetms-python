# phrasetms_client.ProjectTemplateApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_linguists_from_template**](ProjectTemplateApi.md#assign_linguists_from_template) | **POST** /api2/v1/projects/{projectUid}/applyTemplate/{templateUid}/assignProviders | Assigns providers from template
[**assign_linguists_from_template_to_job_parts**](ProjectTemplateApi.md#assign_linguists_from_template_to_job_parts) | **POST** /api2/v1/projects/{projectUid}/applyTemplate/{templateUid}/assignProviders/forJobParts | Assigns providers from template (specific jobs)
[**assignable_templates**](ProjectTemplateApi.md#assignable_templates) | **GET** /api2/v1/projects/{projectUid}/assignableTemplates | List assignable templates
[**create_custom_fields1**](ProjectTemplateApi.md#create_custom_fields1) | **POST** /api2/v1/projectTemplates/{projectTemplateUid}/customFields | Create custom field instances
[**create_project_from_template_v2**](ProjectTemplateApi.md#create_project_from_template_v2) | **POST** /api2/v2/projects/applyTemplate/{templateUid} | Create project from template
[**create_project_from_template_v2_async**](ProjectTemplateApi.md#create_project_from_template_v2_async) | **POST** /api2/v2/projects/applyTemplate/async/{templateUid} | Create project from template (async)
[**create_project_template**](ProjectTemplateApi.md#create_project_template) | **POST** /api2/v1/projectTemplates | Create project template
[**delete_custom_field2**](ProjectTemplateApi.md#delete_custom_field2) | **DELETE** /api2/v1/projectTemplates/{projectTemplateUid}/customFields/{fieldInstanceUid} | Delete custom field of project template
[**delete_project_template**](ProjectTemplateApi.md#delete_project_template) | **DELETE** /api2/v1/projectTemplates/{projectTemplateUid} | Delete project template
[**edit_custom_field1**](ProjectTemplateApi.md#edit_custom_field1) | **PUT** /api2/v1/projectTemplates/{projectTemplateUid}/customFields/{fieldInstanceUid} | Edit custom field of project template
[**edit_custom_fields1**](ProjectTemplateApi.md#edit_custom_fields1) | **PUT** /api2/v1/projectTemplates/{projectTemplateUid}/customFields | Edit custom fields of the project template (batch)
[**edit_project_template**](ProjectTemplateApi.md#edit_project_template) | **PUT** /api2/v1/projectTemplates/{projectTemplateUid} | Edit project template
[**edit_project_template_access_settings**](ProjectTemplateApi.md#edit_project_template_access_settings) | **PUT** /api2/v1/projectTemplates/{projectTemplateUid}/accessSettings | Edit project template access and security settings
[**edit_project_template_import_settings**](ProjectTemplateApi.md#edit_project_template_import_settings) | **PUT** /api2/v1/projectTemplates/{projectTemplateUid}/importSettings | Edit project template import settings
[**get_analyse_settings_for_project_template**](ProjectTemplateApi.md#get_analyse_settings_for_project_template) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/analyseSettings | Get analyse settings
[**get_custom_field2**](ProjectTemplateApi.md#get_custom_field2) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/customFields/{fieldInstanceUid} | Get custom field of project template
[**get_custom_fields_page1**](ProjectTemplateApi.md#get_custom_fields_page1) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/customFields | Get custom fields of project template (page)
[**get_import_settings_for_project_template**](ProjectTemplateApi.md#get_import_settings_for_project_template) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/importSettings | Get import settings
[**get_machine_translate_settings_for_project_template**](ProjectTemplateApi.md#get_machine_translate_settings_for_project_template) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/mtSettings | Get project template machine translate settings
[**get_pre_translate_settings_for_project_template2**](ProjectTemplateApi.md#get_pre_translate_settings_for_project_template2) | **GET** /api2/v3/projectTemplates/{projectTemplateUid}/preTranslateSettings | Get Pre-translate settings
[**get_project_template**](ProjectTemplateApi.md#get_project_template) | **GET** /api2/v1/projectTemplates/{projectTemplateUid} | Get project template
[**get_project_template_access_settings**](ProjectTemplateApi.md#get_project_template_access_settings) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/accessSettings | Get project template access and security settings
[**get_project_template_qa_settings**](ProjectTemplateApi.md#get_project_template_qa_settings) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/qaSettings | Get quality assurance settings
[**get_project_template_term_bases**](ProjectTemplateApi.md#get_project_template_term_bases) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/termBases | Get term bases
[**get_project_template_trans_memories2**](ProjectTemplateApi.md#get_project_template_trans_memories2) | **GET** /api2/v3/projectTemplates/{projectTemplateUid}/transMemories | Get translation memories
[**get_project_templates**](ProjectTemplateApi.md#get_project_templates) | **GET** /api2/v1/projectTemplates | List project templates
[**relevant_trans_memories**](ProjectTemplateApi.md#relevant_trans_memories) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/transMemories/relevant | List project template relevant translation memories
[**set_project_template_qa_settings**](ProjectTemplateApi.md#set_project_template_qa_settings) | **PUT** /api2/v1/projectTemplates/{projectTemplateUid}/qaSettings | Edit quality assurance settings
[**set_project_template_term_bases**](ProjectTemplateApi.md#set_project_template_term_bases) | **PUT** /api2/v1/projectTemplates/{projectTemplateUid}/termBases | Edit term bases in project template
[**set_project_template_trans_memories_v2**](ProjectTemplateApi.md#set_project_template_trans_memories_v2) | **PUT** /api2/v2/projectTemplates/{projectTemplateUid}/transMemories | Edit translation memories
[**update_analyse_settings_for_project_template**](ProjectTemplateApi.md#update_analyse_settings_for_project_template) | **PUT** /api2/v1/projectTemplates/{projectTemplateUid}/analyseSettings | Edit analyse settings
[**update_pre_translate_settings_for_project_template2**](ProjectTemplateApi.md#update_pre_translate_settings_for_project_template2) | **PUT** /api2/v3/projectTemplates/{projectTemplateUid}/preTranslateSettings | Update Pre-translate settings


# **assign_linguists_from_template**
> JobPartsDto assign_linguists_from_template(template_uid, project_uid)

Assigns providers from template

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_parts_dto import JobPartsDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    template_uid = 'template_uid_example' # str | 
    project_uid = 'project_uid_example' # str | 

    try:
        # Assigns providers from template
        api_response = api_instance.assign_linguists_from_template(template_uid, project_uid)
        print("The response of ProjectTemplateApi->assign_linguists_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->assign_linguists_from_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_uid** | **str**|  | 
 **project_uid** | **str**|  | 

### Return type

[**JobPartsDto**](JobPartsDto.md)

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

# **assign_linguists_from_template_to_job_parts**
> JobPartsDto assign_linguists_from_template_to_job_parts(template_uid, project_uid, body=body)

Assigns providers from template (specific jobs)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_references import JobPartReferences
from phrasetms_client.models.job_parts_dto import JobPartsDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    template_uid = 'template_uid_example' # str | 
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.JobPartReferences() # JobPartReferences |  (optional)

    try:
        # Assigns providers from template (specific jobs)
        api_response = api_instance.assign_linguists_from_template_to_job_parts(template_uid, project_uid, body=body)
        print("The response of ProjectTemplateApi->assign_linguists_from_template_to_job_parts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->assign_linguists_from_template_to_job_parts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_uid** | **str**|  | 
 **project_uid** | **str**|  | 
 **body** | [**JobPartReferences**](JobPartReferences.md)|  | [optional] 

### Return type

[**JobPartsDto**](JobPartsDto.md)

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

# **assignable_templates**
> AssignableTemplatesDto assignable_templates(project_uid)

List assignable templates

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.assignable_templates_dto import AssignableTemplatesDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_uid = 'project_uid_example' # str | 

    try:
        # List assignable templates
        api_response = api_instance.assignable_templates(project_uid)
        print("The response of ProjectTemplateApi->assignable_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->assignable_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**AssignableTemplatesDto**](AssignableTemplatesDto.md)

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

# **create_custom_fields1**
> CustomFieldInstancesDto create_custom_fields1(project_template_uid, body=body)

Create custom field instances

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.create_custom_field_instances_dto import CreateCustomFieldInstancesDto
from phrasetms_client.models.custom_field_instances_dto import CustomFieldInstancesDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.CreateCustomFieldInstancesDto() # CreateCustomFieldInstancesDto |  (optional)

    try:
        # Create custom field instances
        api_response = api_instance.create_custom_fields1(project_template_uid, body=body)
        print("The response of ProjectTemplateApi->create_custom_fields1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->create_custom_fields1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**CreateCustomFieldInstancesDto**](CreateCustomFieldInstancesDto.md)|  | [optional] 

### Return type

[**CustomFieldInstancesDto**](CustomFieldInstancesDto.md)

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

# **create_project_from_template_v2**
> AbstractProjectDtoV2 create_project_from_template_v2(template_uid, body=body)

Create project from template

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.abstract_project_dto_v2 import AbstractProjectDtoV2
from phrasetms_client.models.create_project_from_template_v2_dto import CreateProjectFromTemplateV2Dto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    template_uid = 'template_uid_example' # str | 
    body = phrasetms_client.CreateProjectFromTemplateV2Dto() # CreateProjectFromTemplateV2Dto |  (optional)

    try:
        # Create project from template
        api_response = api_instance.create_project_from_template_v2(template_uid, body=body)
        print("The response of ProjectTemplateApi->create_project_from_template_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->create_project_from_template_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_uid** | **str**|  | 
 **body** | [**CreateProjectFromTemplateV2Dto**](CreateProjectFromTemplateV2Dto.md)|  | [optional] 

### Return type

[**AbstractProjectDtoV2**](AbstractProjectDtoV2.md)

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

# **create_project_from_template_v2_async**
> AsyncRequestWrapperV2Dto create_project_from_template_v2_async(template_uid, body=body)

Create project from template (async)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_request_wrapper_v2_dto import AsyncRequestWrapperV2Dto
from phrasetms_client.models.create_project_from_template_async_v2_dto import CreateProjectFromTemplateAsyncV2Dto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    template_uid = 'template_uid_example' # str | 
    body = phrasetms_client.CreateProjectFromTemplateAsyncV2Dto() # CreateProjectFromTemplateAsyncV2Dto |  (optional)

    try:
        # Create project from template (async)
        api_response = api_instance.create_project_from_template_v2_async(template_uid, body=body)
        print("The response of ProjectTemplateApi->create_project_from_template_v2_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->create_project_from_template_v2_async: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_uid** | **str**|  | 
 **body** | [**CreateProjectFromTemplateAsyncV2Dto**](CreateProjectFromTemplateAsyncV2Dto.md)|  | [optional] 

### Return type

[**AsyncRequestWrapperV2Dto**](AsyncRequestWrapperV2Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
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

# **create_project_template**
> ProjectTemplateDto create_project_template(body)

Create project template

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_template_create_action_dto import ProjectTemplateCreateActionDto
from phrasetms_client.models.project_template_dto import ProjectTemplateDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    body = phrasetms_client.ProjectTemplateCreateActionDto() # ProjectTemplateCreateActionDto | 

    try:
        # Create project template
        api_response = api_instance.create_project_template(body)
        print("The response of ProjectTemplateApi->create_project_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->create_project_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectTemplateCreateActionDto**](ProjectTemplateCreateActionDto.md)|  | 

### Return type

[**ProjectTemplateDto**](ProjectTemplateDto.md)

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

# **delete_custom_field2**
> delete_custom_field2(project_template_uid, field_instance_uid)

Delete custom field of project template

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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    field_instance_uid = 'field_instance_uid_example' # str | 

    try:
        # Delete custom field of project template
        api_instance.delete_custom_field2(project_template_uid, field_instance_uid)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->delete_custom_field2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **field_instance_uid** | **str**|  | 

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

# **delete_project_template**
> delete_project_template(project_template_uid)

Delete project template

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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 

    try:
        # Delete project template
        api_instance.delete_project_template(project_template_uid)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->delete_project_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 

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
**204** | No Content |  -  |
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

# **edit_custom_field1**
> CustomFieldInstanceDto edit_custom_field1(project_template_uid, field_instance_uid, body=body)

Edit custom field of project template

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.custom_field_instance_dto import CustomFieldInstanceDto
from phrasetms_client.models.update_custom_field_instance_dto import UpdateCustomFieldInstanceDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    field_instance_uid = 'field_instance_uid_example' # str | 
    body = phrasetms_client.UpdateCustomFieldInstanceDto() # UpdateCustomFieldInstanceDto |  (optional)

    try:
        # Edit custom field of project template
        api_response = api_instance.edit_custom_field1(project_template_uid, field_instance_uid, body=body)
        print("The response of ProjectTemplateApi->edit_custom_field1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->edit_custom_field1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **field_instance_uid** | **str**|  | 
 **body** | [**UpdateCustomFieldInstanceDto**](UpdateCustomFieldInstanceDto.md)|  | [optional] 

### Return type

[**CustomFieldInstanceDto**](CustomFieldInstanceDto.md)

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

# **edit_custom_fields1**
> CustomFieldInstancesDto edit_custom_fields1(project_template_uid, body=body)

Edit custom fields of the project template (batch)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.custom_field_instances_dto import CustomFieldInstancesDto
from phrasetms_client.models.update_custom_field_instances_dto import UpdateCustomFieldInstancesDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.UpdateCustomFieldInstancesDto() # UpdateCustomFieldInstancesDto |  (optional)

    try:
        # Edit custom fields of the project template (batch)
        api_response = api_instance.edit_custom_fields1(project_template_uid, body=body)
        print("The response of ProjectTemplateApi->edit_custom_fields1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->edit_custom_fields1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**UpdateCustomFieldInstancesDto**](UpdateCustomFieldInstancesDto.md)|  | [optional] 

### Return type

[**CustomFieldInstancesDto**](CustomFieldInstancesDto.md)

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

# **edit_project_template**
> ProjectTemplateDto edit_project_template(project_template_uid, body)

Edit project template

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_template_dto import ProjectTemplateDto
from phrasetms_client.models.project_template_edit_dto import ProjectTemplateEditDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.ProjectTemplateEditDto() # ProjectTemplateEditDto | 

    try:
        # Edit project template
        api_response = api_instance.edit_project_template(project_template_uid, body)
        print("The response of ProjectTemplateApi->edit_project_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->edit_project_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**ProjectTemplateEditDto**](ProjectTemplateEditDto.md)|  | 

### Return type

[**ProjectTemplateDto**](ProjectTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edited |  -  |
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

# **edit_project_template_access_settings**
> ProjectSecuritySettingsDtoV2 edit_project_template_access_settings(project_template_uid, body=body)

Edit project template access and security settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.edit_project_security_settings_dto_v2 import EditProjectSecuritySettingsDtoV2
from phrasetms_client.models.project_security_settings_dto_v2 import ProjectSecuritySettingsDtoV2
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.EditProjectSecuritySettingsDtoV2() # EditProjectSecuritySettingsDtoV2 |  (optional)

    try:
        # Edit project template access and security settings
        api_response = api_instance.edit_project_template_access_settings(project_template_uid, body=body)
        print("The response of ProjectTemplateApi->edit_project_template_access_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->edit_project_template_access_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**EditProjectSecuritySettingsDtoV2**](EditProjectSecuritySettingsDtoV2.md)|  | [optional] 

### Return type

[**ProjectSecuritySettingsDtoV2**](ProjectSecuritySettingsDtoV2.md)

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

# **edit_project_template_import_settings**
> FileImportSettingsDto edit_project_template_import_settings(project_template_uid, body=body)

Edit project template import settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.file_import_settings_create_dto import FileImportSettingsCreateDto
from phrasetms_client.models.file_import_settings_dto import FileImportSettingsDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.FileImportSettingsCreateDto() # FileImportSettingsCreateDto |  (optional)

    try:
        # Edit project template import settings
        api_response = api_instance.edit_project_template_import_settings(project_template_uid, body=body)
        print("The response of ProjectTemplateApi->edit_project_template_import_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->edit_project_template_import_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**FileImportSettingsCreateDto**](FileImportSettingsCreateDto.md)|  | [optional] 

### Return type

[**FileImportSettingsDto**](FileImportSettingsDto.md)

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

# **get_analyse_settings_for_project_template**
> AbstractAnalyseSettingsDto get_analyse_settings_for_project_template(project_template_uid)

Get analyse settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.abstract_analyse_settings_dto import AbstractAnalyseSettingsDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 

    try:
        # Get analyse settings
        api_response = api_instance.get_analyse_settings_for_project_template(project_template_uid)
        print("The response of ProjectTemplateApi->get_analyse_settings_for_project_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_analyse_settings_for_project_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 

### Return type

[**AbstractAnalyseSettingsDto**](AbstractAnalyseSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
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

# **get_custom_field2**
> CustomFieldInstanceDto get_custom_field2(project_template_uid, field_instance_uid)

Get custom field of project template

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.custom_field_instance_dto import CustomFieldInstanceDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    field_instance_uid = 'field_instance_uid_example' # str | 

    try:
        # Get custom field of project template
        api_response = api_instance.get_custom_field2(project_template_uid, field_instance_uid)
        print("The response of ProjectTemplateApi->get_custom_field2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_custom_field2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **field_instance_uid** | **str**|  | 

### Return type

[**CustomFieldInstanceDto**](CustomFieldInstanceDto.md)

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

# **get_custom_fields_page1**
> PageDtoCustomFieldInstanceDto get_custom_fields_page1(project_template_uid, page_number=page_number, page_size=page_size, created_by=created_by, modified_by=modified_by, sort_field=sort_field, sort_trend=sort_trend)

Get custom fields of project template (page)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_custom_field_instance_dto import PageDtoCustomFieldInstanceDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 20 # int | Page size, accepts values between 1 and 50, default 20 (optional) (default to 20)
    created_by = ['created_by_example'] # List[str] | Filter by webhook creators UIDs (optional)
    modified_by = ['modified_by_example'] # List[str] | Filter by webhook updaters UIDs (optional)
    sort_field = 'sort_field_example' # str | Sort by this field (optional)
    sort_trend = 'ASC' # str | Sort direction (optional) (default to 'ASC')

    try:
        # Get custom fields of project template (page)
        api_response = api_instance.get_custom_fields_page1(project_template_uid, page_number=page_number, page_size=page_size, created_by=created_by, modified_by=modified_by, sort_field=sort_field, sort_trend=sort_trend)
        print("The response of ProjectTemplateApi->get_custom_fields_page1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_custom_fields_page1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 20 | [optional] [default to 20]
 **created_by** | [**List[str]**](str.md)| Filter by webhook creators UIDs | [optional] 
 **modified_by** | [**List[str]**](str.md)| Filter by webhook updaters UIDs | [optional] 
 **sort_field** | **str**| Sort by this field | [optional] 
 **sort_trend** | **str**| Sort direction | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageDtoCustomFieldInstanceDto**](PageDtoCustomFieldInstanceDto.md)

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

# **get_import_settings_for_project_template**
> FileImportSettingsDto get_import_settings_for_project_template(project_template_uid)

Get import settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.file_import_settings_dto import FileImportSettingsDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 

    try:
        # Get import settings
        api_response = api_instance.get_import_settings_for_project_template(project_template_uid)
        print("The response of ProjectTemplateApi->get_import_settings_for_project_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_import_settings_for_project_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 

### Return type

[**FileImportSettingsDto**](FileImportSettingsDto.md)

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

# **get_machine_translate_settings_for_project_template**
> MTSettingsPerLanguageListDto get_machine_translate_settings_for_project_template(project_template_uid)

Get project template machine translate settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.mt_settings_per_language_list_dto import MTSettingsPerLanguageListDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 

    try:
        # Get project template machine translate settings
        api_response = api_instance.get_machine_translate_settings_for_project_template(project_template_uid)
        print("The response of ProjectTemplateApi->get_machine_translate_settings_for_project_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_machine_translate_settings_for_project_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 

### Return type

[**MTSettingsPerLanguageListDto**](MTSettingsPerLanguageListDto.md)

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

# **get_pre_translate_settings_for_project_template2**
> PreTranslateSettingsV3Dto get_pre_translate_settings_for_project_template2(project_template_uid)

Get Pre-translate settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.pre_translate_settings_v3_dto import PreTranslateSettingsV3Dto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 

    try:
        # Get Pre-translate settings
        api_response = api_instance.get_pre_translate_settings_for_project_template2(project_template_uid)
        print("The response of ProjectTemplateApi->get_pre_translate_settings_for_project_template2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_pre_translate_settings_for_project_template2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 

### Return type

[**PreTranslateSettingsV3Dto**](PreTranslateSettingsV3Dto.md)

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

# **get_project_template**
> ProjectTemplateDto get_project_template(project_template_uid)

Get project template

Note: importSettings in response is deprecated and will be always null

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_template_dto import ProjectTemplateDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 

    try:
        # Get project template
        api_response = api_instance.get_project_template(project_template_uid)
        print("The response of ProjectTemplateApi->get_project_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_project_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 

### Return type

[**ProjectTemplateDto**](ProjectTemplateDto.md)

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

# **get_project_template_access_settings**
> ProjectSecuritySettingsDtoV2 get_project_template_access_settings(project_template_uid)

Get project template access and security settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_security_settings_dto_v2 import ProjectSecuritySettingsDtoV2
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 

    try:
        # Get project template access and security settings
        api_response = api_instance.get_project_template_access_settings(project_template_uid)
        print("The response of ProjectTemplateApi->get_project_template_access_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_project_template_access_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 

### Return type

[**ProjectSecuritySettingsDtoV2**](ProjectSecuritySettingsDtoV2.md)

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

# **get_project_template_qa_settings**
> QASettingsDtoV2 get_project_template_qa_settings(project_template_uid)

Get quality assurance settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.qa_settings_dto_v2 import QASettingsDtoV2
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 

    try:
        # Get quality assurance settings
        api_response = api_instance.get_project_template_qa_settings(project_template_uid)
        print("The response of ProjectTemplateApi->get_project_template_qa_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_project_template_qa_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 

### Return type

[**QASettingsDtoV2**](QASettingsDtoV2.md)

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

# **get_project_template_term_bases**
> ProjectTemplateTermBaseListDto get_project_template_term_bases(project_template_uid)

Get term bases

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_template_term_base_list_dto import ProjectTemplateTermBaseListDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 

    try:
        # Get term bases
        api_response = api_instance.get_project_template_term_bases(project_template_uid)
        print("The response of ProjectTemplateApi->get_project_template_term_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_project_template_term_bases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 

### Return type

[**ProjectTemplateTermBaseListDto**](ProjectTemplateTermBaseListDto.md)

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

# **get_project_template_trans_memories2**
> ProjectTemplateTransMemoryListDtoV3 get_project_template_trans_memories2(project_template_uid, target_lang=target_lang, wf_step_uid=wf_step_uid)

Get translation memories

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_template_trans_memory_list_dto_v3 import ProjectTemplateTransMemoryListDtoV3
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    target_lang = 'target_lang_example' # str | Filter project translation memories by target language (optional)
    wf_step_uid = 'wf_step_uid_example' # str | Filter project translation memories by workflow step (optional)

    try:
        # Get translation memories
        api_response = api_instance.get_project_template_trans_memories2(project_template_uid, target_lang=target_lang, wf_step_uid=wf_step_uid)
        print("The response of ProjectTemplateApi->get_project_template_trans_memories2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_project_template_trans_memories2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **target_lang** | **str**| Filter project translation memories by target language | [optional] 
 **wf_step_uid** | **str**| Filter project translation memories by workflow step | [optional] 

### Return type

[**ProjectTemplateTransMemoryListDtoV3**](ProjectTemplateTransMemoryListDtoV3.md)

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

# **get_project_templates**
> PageDtoProjectTemplateReference get_project_templates(name=name, client_id=client_id, client_name=client_name, owner_uid=owner_uid, domain_name=domain_name, sub_domain_name=sub_domain_name, cost_center_id=cost_center_id, cost_center_name=cost_center_name, business_unit_name=business_unit_name, sort=sort, direction=direction, page_number=page_number, page_size=page_size)

List project templates

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_project_template_reference import PageDtoProjectTemplateReference
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    name = 'name_example' # str |  (optional)
    client_id = 56 # int |  (optional)
    client_name = 'client_name_example' # str |  (optional)
    owner_uid = 'owner_uid_example' # str |  (optional)
    domain_name = 'domain_name_example' # str |  (optional)
    sub_domain_name = 'sub_domain_name_example' # str |  (optional)
    cost_center_id = 56 # int |  (optional)
    cost_center_name = 'cost_center_name_example' # str |  (optional)
    business_unit_name = 'business_unit_name_example' # str |  (optional)
    sort = 'dateCreated' # str |  (optional) (default to 'dateCreated')
    direction = 'desc' # str |  (optional) (default to 'desc')
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List project templates
        api_response = api_instance.get_project_templates(name=name, client_id=client_id, client_name=client_name, owner_uid=owner_uid, domain_name=domain_name, sub_domain_name=sub_domain_name, cost_center_id=cost_center_id, cost_center_name=cost_center_name, business_unit_name=business_unit_name, sort=sort, direction=direction, page_number=page_number, page_size=page_size)
        print("The response of ProjectTemplateApi->get_project_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->get_project_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **client_id** | **int**|  | [optional] 
 **client_name** | **str**|  | [optional] 
 **owner_uid** | **str**|  | [optional] 
 **domain_name** | **str**|  | [optional] 
 **sub_domain_name** | **str**|  | [optional] 
 **cost_center_id** | **int**|  | [optional] 
 **cost_center_name** | **str**|  | [optional] 
 **business_unit_name** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;dateCreated&#39;]
 **direction** | **str**|  | [optional] [default to &#39;desc&#39;]
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoProjectTemplateReference**](PageDtoProjectTemplateReference.md)

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

# **relevant_trans_memories**
> PageDtoTransMemoryDto relevant_trans_memories(project_template_uid, name=name, domain_name=domain_name, client_name=client_name, sub_domain_name=sub_domain_name, target_langs=target_langs, strict_lang_matching=strict_lang_matching, page_number=page_number, page_size=page_size)

List project template relevant translation memories

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_trans_memory_dto import PageDtoTransMemoryDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    name = 'name_example' # str |  (optional)
    domain_name = 'domain_name_example' # str |  (optional)
    client_name = 'client_name_example' # str |  (optional)
    sub_domain_name = 'sub_domain_name_example' # str |  (optional)
    target_langs = ['target_langs_example'] # List[str] |  (optional)
    strict_lang_matching = False # bool |  (optional) (default to False)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List project template relevant translation memories
        api_response = api_instance.relevant_trans_memories(project_template_uid, name=name, domain_name=domain_name, client_name=client_name, sub_domain_name=sub_domain_name, target_langs=target_langs, strict_lang_matching=strict_lang_matching, page_number=page_number, page_size=page_size)
        print("The response of ProjectTemplateApi->relevant_trans_memories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->relevant_trans_memories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **name** | **str**|  | [optional] 
 **domain_name** | **str**|  | [optional] 
 **client_name** | **str**|  | [optional] 
 **sub_domain_name** | **str**|  | [optional] 
 **target_langs** | [**List[str]**](str.md)|  | [optional] 
 **strict_lang_matching** | **bool**|  | [optional] [default to False]
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoTransMemoryDto**](PageDtoTransMemoryDto.md)

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

# **set_project_template_qa_settings**
> QASettingsDtoV2 set_project_template_qa_settings(project_template_uid, body=body)

Edit quality assurance settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.edit_qa_settings_dto_v2 import EditQASettingsDtoV2
from phrasetms_client.models.qa_settings_dto_v2 import QASettingsDtoV2
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.EditQASettingsDtoV2() # EditQASettingsDtoV2 |  (optional)

    try:
        # Edit quality assurance settings
        api_response = api_instance.set_project_template_qa_settings(project_template_uid, body=body)
        print("The response of ProjectTemplateApi->set_project_template_qa_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->set_project_template_qa_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**EditQASettingsDtoV2**](EditQASettingsDtoV2.md)|  | [optional] 

### Return type

[**QASettingsDtoV2**](QASettingsDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **set_project_template_term_bases**
> ProjectTemplateTermBaseListDto set_project_template_term_bases(project_template_uid, body=body)

Edit term bases in project template

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_template_term_base_list_dto import ProjectTemplateTermBaseListDto
from phrasetms_client.models.set_project_template_term_base_dto import SetProjectTemplateTermBaseDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.SetProjectTemplateTermBaseDto() # SetProjectTemplateTermBaseDto |  (optional)

    try:
        # Edit term bases in project template
        api_response = api_instance.set_project_template_term_bases(project_template_uid, body=body)
        print("The response of ProjectTemplateApi->set_project_template_term_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->set_project_template_term_bases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**SetProjectTemplateTermBaseDto**](SetProjectTemplateTermBaseDto.md)|  | [optional] 

### Return type

[**ProjectTemplateTermBaseListDto**](ProjectTemplateTermBaseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **set_project_template_trans_memories_v2**
> ProjectTemplateTransMemoryListV2Dto set_project_template_trans_memories_v2(project_template_uid, body=body)

Edit translation memories

If user wants to edit “All target languages” or \"All workflow steps”,                         but there are already varied TM settings for individual languages or steps,                         then the user risks to overwrite these individual choices.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_template_trans_memory_list_v2_dto import ProjectTemplateTransMemoryListV2Dto
from phrasetms_client.models.set_project_template_trans_memories_v2_dto import SetProjectTemplateTransMemoriesV2Dto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.SetProjectTemplateTransMemoriesV2Dto() # SetProjectTemplateTransMemoriesV2Dto |  (optional)

    try:
        # Edit translation memories
        api_response = api_instance.set_project_template_trans_memories_v2(project_template_uid, body=body)
        print("The response of ProjectTemplateApi->set_project_template_trans_memories_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->set_project_template_trans_memories_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**SetProjectTemplateTransMemoriesV2Dto**](SetProjectTemplateTransMemoriesV2Dto.md)|  | [optional] 

### Return type

[**ProjectTemplateTransMemoryListV2Dto**](ProjectTemplateTransMemoryListV2Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
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

# **update_analyse_settings_for_project_template**
> AbstractAnalyseSettingsDto update_analyse_settings_for_project_template(project_template_uid, body=body)

Edit analyse settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.abstract_analyse_settings_dto import AbstractAnalyseSettingsDto
from phrasetms_client.models.edit_analyse_settings_dto import EditAnalyseSettingsDto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.EditAnalyseSettingsDto() # EditAnalyseSettingsDto |  (optional)

    try:
        # Edit analyse settings
        api_response = api_instance.update_analyse_settings_for_project_template(project_template_uid, body=body)
        print("The response of ProjectTemplateApi->update_analyse_settings_for_project_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->update_analyse_settings_for_project_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**EditAnalyseSettingsDto**](EditAnalyseSettingsDto.md)|  | [optional] 

### Return type

[**AbstractAnalyseSettingsDto**](AbstractAnalyseSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
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

# **update_pre_translate_settings_for_project_template2**
> PreTranslateSettingsV3Dto update_pre_translate_settings_for_project_template2(project_template_uid, body=body)

Update Pre-translate settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.pre_translate_settings_v3_dto import PreTranslateSettingsV3Dto
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
    api_instance = phrasetms_client.ProjectTemplateApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.PreTranslateSettingsV3Dto() # PreTranslateSettingsV3Dto |  (optional)

    try:
        # Update Pre-translate settings
        api_response = api_instance.update_pre_translate_settings_for_project_template2(project_template_uid, body=body)
        print("The response of ProjectTemplateApi->update_pre_translate_settings_for_project_template2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateApi->update_pre_translate_settings_for_project_template2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**PreTranslateSettingsV3Dto**](PreTranslateSettingsV3Dto.md)|  | [optional] 

### Return type

[**PreTranslateSettingsV3Dto**](PreTranslateSettingsV3Dto.md)

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

