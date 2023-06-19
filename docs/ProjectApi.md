# phrasetms_client.ProjectApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_target_language_to_project**](ProjectApi.md#add_target_language_to_project) | **POST** /api2/v1/projects/{projectUid}/targetLangs | Add target languages
[**add_workflow_steps**](ProjectApi.md#add_workflow_steps) | **POST** /api2/v1/projects/{projectUid}/workflowSteps | Add workflow steps
[**assign_linguists_from_template**](ProjectApi.md#assign_linguists_from_template) | **POST** /api2/v1/projects/{projectUid}/applyTemplate/{templateUid}/assignProviders | Assigns providers from template
[**assign_linguists_from_template_to_job_parts**](ProjectApi.md#assign_linguists_from_template_to_job_parts) | **POST** /api2/v1/projects/{projectUid}/applyTemplate/{templateUid}/assignProviders/forJobParts | Assigns providers from template (specific jobs)
[**assign_vendor_to_project**](ProjectApi.md#assign_vendor_to_project) | **POST** /api2/v1/projects/{projectUid}/assignVendor | Assign vendor
[**assignable_templates**](ProjectApi.md#assignable_templates) | **GET** /api2/v1/projects/{projectUid}/assignableTemplates | List assignable templates
[**clone_project**](ProjectApi.md#clone_project) | **POST** /api2/v1/projects/{projectUid}/clone | Clone project
[**create_custom_fields**](ProjectApi.md#create_custom_fields) | **POST** /api2/v1/projects/{projectUid}/customFields | Create custom field instances
[**create_project_from_template_v2**](ProjectApi.md#create_project_from_template_v2) | **POST** /api2/v2/projects/applyTemplate/{templateUid} | Create project from template
[**create_project_from_template_v2_async**](ProjectApi.md#create_project_from_template_v2_async) | **POST** /api2/v2/projects/applyTemplate/async/{templateUid} | Create project from template (async)
[**create_project_v3**](ProjectApi.md#create_project_v3) | **POST** /api2/v3/projects | Create project
[**delete_custom_field1**](ProjectApi.md#delete_custom_field1) | **DELETE** /api2/v1/projects/{projectUid}/customFields/{fieldInstanceUid} | Delete custom field of project
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /api2/v1/projects/{projectUid} | Delete project
[**edit_custom_field**](ProjectApi.md#edit_custom_field) | **PUT** /api2/v1/projects/{projectUid}/customFields/{fieldInstanceUid} | Edit custom field of project
[**edit_custom_fields**](ProjectApi.md#edit_custom_fields) | **PUT** /api2/v1/projects/{projectUid}/customFields | Edit custom fields of the project (batch)
[**edit_import_settings1**](ProjectApi.md#edit_import_settings1) | **PUT** /api2/v1/projects/{projectUid}/importSettings | Edit project import settings
[**edit_project_access_settings_v2**](ProjectApi.md#edit_project_access_settings_v2) | **PUT** /api2/v2/projects/{projectUid}/accessSettings | Edit access and security settings
[**edit_project_pre_translate_settings2**](ProjectApi.md#edit_project_pre_translate_settings2) | **PUT** /api2/v3/projects/{projectUid}/preTranslateSettings | Update Pre-translate settings
[**edit_project_v2**](ProjectApi.md#edit_project_v2) | **PUT** /api2/v2/projects/{projectUid} | Edit project
[**enabled_quality_checks**](ProjectApi.md#enabled_quality_checks) | **GET** /api2/v1/projects/{projectUid}/qaSettingsChecks | Get QA checks
[**get_analyse_settings_for_project**](ProjectApi.md#get_analyse_settings_for_project) | **GET** /api2/v1/projects/{projectUid}/analyseSettings | Get analyse settings
[**get_custom_field1**](ProjectApi.md#get_custom_field1) | **GET** /api2/v1/projects/{projectUid}/customFields/{fieldInstanceUid} | Get custom field of project
[**get_custom_fields_page**](ProjectApi.md#get_custom_fields_page) | **GET** /api2/v1/projects/{projectUid}/customFields | Get custom fields of project (page)
[**get_file_naming_settings**](ProjectApi.md#get_file_naming_settings) | **GET** /api2/v1/projects/{projectUid}/fileNamingSettings | Get file naming settings for project
[**get_financial_settings**](ProjectApi.md#get_financial_settings) | **GET** /api2/v1/projects/{projectUid}/financialSettings | Get financial settings
[**get_import_settings2**](ProjectApi.md#get_import_settings2) | **GET** /api2/v1/projects/{projectUid}/importSettings | Get projects&#x27;s default import settings
[**get_mt_settings_for_project**](ProjectApi.md#get_mt_settings_for_project) | **GET** /api2/v1/projects/{projectUid}/mtSettings | Get project machine translate settings
[**get_pre_translate_settings_for_project2**](ProjectApi.md#get_pre_translate_settings_for_project2) | **GET** /api2/v3/projects/{projectUid}/preTranslateSettings | Get Pre-translate settings
[**get_project**](ProjectApi.md#get_project) | **GET** /api2/v1/projects/{projectUid} | Get project
[**get_project_access_settings_v2**](ProjectApi.md#get_project_access_settings_v2) | **GET** /api2/v2/projects/{projectUid}/accessSettings | Get access and security settings
[**get_project_assignments**](ProjectApi.md#get_project_assignments) | **GET** /api2/v1/projects/{projectUid}/providers | List project providers
[**get_project_settings**](ProjectApi.md#get_project_settings) | **GET** /api2/v1/projects/{projectUid}/lqaSettings | Get LQA settings
[**get_project_term_bases**](ProjectApi.md#get_project_term_bases) | **GET** /api2/v1/projects/{projectUid}/termBases | Get term bases
[**get_project_trans_memories1**](ProjectApi.md#get_project_trans_memories1) | **GET** /api2/v3/projects/{projectUid}/transMemories | Get translation memories
[**get_project_workflow_steps_v2**](ProjectApi.md#get_project_workflow_steps_v2) | **GET** /api2/v2/projects/{projectUid}/workflowSteps | Get workflow steps
[**get_quotes_for_project**](ProjectApi.md#get_quotes_for_project) | **GET** /api2/v1/projects/{projectUid}/quotes | List quotes
[**list_assigned_projects**](ProjectApi.md#list_assigned_projects) | **GET** /api2/v1/users/{userUid}/projects | List assigned projects
[**list_by_project_v3**](ProjectApi.md#list_by_project_v3) | **GET** /api2/v3/projects/{projectUid}/analyses | List analyses by project
[**list_projects**](ProjectApi.md#list_projects) | **GET** /api2/v1/projects | List projects
[**list_providers3**](ProjectApi.md#list_providers3) | **POST** /api2/v2/projects/{projectUid}/providers/suggest | Get suggested providers
[**patch_project**](ProjectApi.md#patch_project) | **PATCH** /api2/v1/projects/{projectUid} | Edit project
[**relevant_term_bases**](ProjectApi.md#relevant_term_bases) | **GET** /api2/v1/projects/{projectUid}/termBases/relevant | List project relevant term bases
[**relevant_trans_memories1**](ProjectApi.md#relevant_trans_memories1) | **GET** /api2/v1/projects/{projectUid}/transMemories/relevant | List project relevant translation memories
[**search_segment1**](ProjectApi.md#search_segment1) | **POST** /api2/v1/projects/{projectUid}/transMemories/searchSegmentInProject | Search translation memory for segment in the project
[**set_financial_settings**](ProjectApi.md#set_financial_settings) | **PUT** /api2/v1/projects/{projectUid}/financialSettings | Edit financial settings
[**set_mt_settings_for_project**](ProjectApi.md#set_mt_settings_for_project) | **PUT** /api2/v1/projects/{projectUid}/mtSettings | Edit machine translate settings
[**set_mt_settings_per_language_for_project**](ProjectApi.md#set_mt_settings_per_language_for_project) | **PUT** /api2/v1/projects/{projectUid}/mtSettingsPerLanguage | Edit machine translate settings per language
[**set_project_qa_settings_v2**](ProjectApi.md#set_project_qa_settings_v2) | **PUT** /api2/v2/projects/{projectUid}/qaSettings | Edit quality assurance settings
[**set_project_status**](ProjectApi.md#set_project_status) | **POST** /api2/v1/projects/{projectUid}/setStatus | Edit project status
[**set_project_term_bases**](ProjectApi.md#set_project_term_bases) | **PUT** /api2/v1/projects/{projectUid}/termBases | Edit term bases
[**set_project_trans_memories_v3**](ProjectApi.md#set_project_trans_memories_v3) | **PUT** /api2/v3/projects/{projectUid}/transMemories | Edit translation memories
[**update_file_naming_settings**](ProjectApi.md#update_file_naming_settings) | **PUT** /api2/v1/projects/{projectUid}/fileNamingSettings | Update file naming settings for project

# **add_target_language_to_project**
> add_target_language_to_project(project_uid, body=body)

Add target languages

Add target languages to project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.AddTargetLangDto() # AddTargetLangDto |  (optional)

try:
    # Add target languages
    api_instance.add_target_language_to_project(project_uid, body=body)
except ApiException as e:
    print("Exception when calling ProjectApi->add_target_language_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**AddTargetLangDto**](AddTargetLangDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_workflow_steps**
> add_workflow_steps(project_uid, body=body)

Add workflow steps

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.AddWorkflowStepsDto() # AddWorkflowStepsDto |  (optional)

try:
    # Add workflow steps
    api_instance.add_workflow_steps(project_uid, body=body)
except ApiException as e:
    print("Exception when calling ProjectApi->add_workflow_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**AddWorkflowStepsDto**](AddWorkflowStepsDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_linguists_from_template**
> JobPartsDto assign_linguists_from_template(template_uid, project_uid)

Assigns providers from template

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
template_uid = 'template_uid_example' # str | 
project_uid = 'project_uid_example' # str | 

try:
    # Assigns providers from template
    api_response = api_instance.assign_linguists_from_template(template_uid, project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->assign_linguists_from_template: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_linguists_from_template_to_job_parts**
> JobPartsDto assign_linguists_from_template_to_job_parts(template_uid, project_uid, body=body)

Assigns providers from template (specific jobs)

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
template_uid = 'template_uid_example' # str | 
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.JobPartReferences() # JobPartReferences |  (optional)

try:
    # Assigns providers from template (specific jobs)
    api_response = api_instance.assign_linguists_from_template_to_job_parts(template_uid, project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->assign_linguists_from_template_to_job_parts: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_vendor_to_project**
> assign_vendor_to_project(project_uid, body=body)

Assign vendor

 To unassign Vendor from Project, use empty body: ``` {} ```     

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.AssignVendorDto() # AssignVendorDto |  (optional)

try:
    # Assign vendor
    api_instance.assign_vendor_to_project(project_uid, body=body)
except ApiException as e:
    print("Exception when calling ProjectApi->assign_vendor_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**AssignVendorDto**](AssignVendorDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignable_templates**
> AssignableTemplatesDto assignable_templates(project_uid)

List assignable templates

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # List assignable templates
    api_response = api_instance.assignable_templates(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->assignable_templates: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_project**
> AbstractProjectDto clone_project(project_uid, body=body)

Clone project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.CloneProjectDto() # CloneProjectDto |  (optional)

try:
    # Clone project
    api_response = api_instance.clone_project(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->clone_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**CloneProjectDto**](CloneProjectDto.md)|  | [optional] 

### Return type

[**AbstractProjectDto**](AbstractProjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_fields**
> CustomFieldInstancesDto create_custom_fields(project_uid, body=body)

Create custom field instances

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.CreateCustomFieldInstancesDto() # CreateCustomFieldInstancesDto |  (optional)

try:
    # Create custom field instances
    api_response = api_instance.create_custom_fields(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**CreateCustomFieldInstancesDto**](CreateCustomFieldInstancesDto.md)|  | [optional] 

### Return type

[**CustomFieldInstancesDto**](CustomFieldInstancesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_from_template_v2**
> AbstractProjectDtoV2 create_project_from_template_v2(template_uid, body=body)

Create project from template

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
template_uid = 'template_uid_example' # str | 
body = phrasetms_client.CreateProjectFromTemplateV2Dto() # CreateProjectFromTemplateV2Dto |  (optional)

try:
    # Create project from template
    api_response = api_instance.create_project_from_template_v2(template_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project_from_template_v2: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_from_template_v2_async**
> AsyncRequestWrapperV2Dto create_project_from_template_v2_async(template_uid, body=body)

Create project from template (async)

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
template_uid = 'template_uid_example' # str | 
body = phrasetms_client.CreateProjectFromTemplateAsyncV2Dto() # CreateProjectFromTemplateAsyncV2Dto |  (optional)

try:
    # Create project from template (async)
    api_response = api_instance.create_project_from_template_v2_async(template_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project_from_template_v2_async: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_v3**
> AbstractProjectDtoV2 create_project_v3(body=body)

Create project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
body = phrasetms_client.CreateProjectV3Dto() # CreateProjectV3Dto |  (optional)

try:
    # Create project
    api_response = api_instance.create_project_v3(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProjectV3Dto**](CreateProjectV3Dto.md)|  | [optional] 

### Return type

[**AbstractProjectDtoV2**](AbstractProjectDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field1**
> delete_custom_field1(project_uid, field_instance_uid)

Delete custom field of project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
field_instance_uid = 'field_instance_uid_example' # str | 

try:
    # Delete custom field of project
    api_instance.delete_custom_field1(project_uid, field_instance_uid)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_custom_field1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **field_instance_uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_uid, purge=purge)

Delete project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
purge = false # bool |  (optional) (default to false)

try:
    # Delete project
    api_instance.delete_project(project_uid, purge=purge)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **purge** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_custom_field**
> CustomFieldInstanceDto edit_custom_field(project_uid, field_instance_uid, body=body)

Edit custom field of project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
field_instance_uid = 'field_instance_uid_example' # str | 
body = phrasetms_client.UpdateCustomFieldInstanceDto() # UpdateCustomFieldInstanceDto |  (optional)

try:
    # Edit custom field of project
    api_response = api_instance.edit_custom_field(project_uid, field_instance_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->edit_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **field_instance_uid** | **str**|  | 
 **body** | [**UpdateCustomFieldInstanceDto**](UpdateCustomFieldInstanceDto.md)|  | [optional] 

### Return type

[**CustomFieldInstanceDto**](CustomFieldInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_custom_fields**
> CustomFieldInstancesDto edit_custom_fields(project_uid, body=body)

Edit custom fields of the project (batch)

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.UpdateCustomFieldInstancesDto() # UpdateCustomFieldInstancesDto |  (optional)

try:
    # Edit custom fields of the project (batch)
    api_response = api_instance.edit_custom_fields(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->edit_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**UpdateCustomFieldInstancesDto**](UpdateCustomFieldInstancesDto.md)|  | [optional] 

### Return type

[**CustomFieldInstancesDto**](CustomFieldInstancesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_import_settings1**
> FileImportSettingsDto edit_import_settings1(project_uid, body=body)

Edit project import settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.FileImportSettingsCreateDto() # FileImportSettingsCreateDto |  (optional)

try:
    # Edit project import settings
    api_response = api_instance.edit_import_settings1(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->edit_import_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**FileImportSettingsCreateDto**](FileImportSettingsCreateDto.md)|  | [optional] 

### Return type

[**FileImportSettingsDto**](FileImportSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_project_access_settings_v2**
> ProjectSecuritySettingsDtoV2 edit_project_access_settings_v2(project_uid, body=body)

Edit access and security settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.EditProjectSecuritySettingsDtoV2() # EditProjectSecuritySettingsDtoV2 |  (optional)

try:
    # Edit access and security settings
    api_response = api_instance.edit_project_access_settings_v2(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->edit_project_access_settings_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**EditProjectSecuritySettingsDtoV2**](EditProjectSecuritySettingsDtoV2.md)|  | [optional] 

### Return type

[**ProjectSecuritySettingsDtoV2**](ProjectSecuritySettingsDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_project_pre_translate_settings2**
> PreTranslateSettingsV3Dto edit_project_pre_translate_settings2(project_uid, body=body)

Update Pre-translate settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.PreTranslateSettingsV3Dto() # PreTranslateSettingsV3Dto |  (optional)

try:
    # Update Pre-translate settings
    api_response = api_instance.edit_project_pre_translate_settings2(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->edit_project_pre_translate_settings2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**PreTranslateSettingsV3Dto**](PreTranslateSettingsV3Dto.md)|  | [optional] 

### Return type

[**PreTranslateSettingsV3Dto**](PreTranslateSettingsV3Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_project_v2**
> AbstractProjectDtoV2 edit_project_v2(project_uid, body=body)

Edit project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.EditProjectV2Dto() # EditProjectV2Dto |  (optional)

try:
    # Edit project
    api_response = api_instance.edit_project_v2(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->edit_project_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**EditProjectV2Dto**](EditProjectV2Dto.md)|  | [optional] 

### Return type

[**AbstractProjectDtoV2**](AbstractProjectDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enabled_quality_checks**
> EnabledQualityChecksDto enabled_quality_checks(project_uid)

Get QA checks

Returns enabled quality assurance settings.

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get QA checks
    api_response = api_instance.enabled_quality_checks(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->enabled_quality_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**EnabledQualityChecksDto**](EnabledQualityChecksDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyse_settings_for_project**
> AnalyseSettingsDto get_analyse_settings_for_project(project_uid)

Get analyse settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get analyse settings
    api_response = api_instance.get_analyse_settings_for_project(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_analyse_settings_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**AnalyseSettingsDto**](AnalyseSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field1**
> CustomFieldInstanceDto get_custom_field1(project_uid, field_instance_uid)

Get custom field of project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
field_instance_uid = 'field_instance_uid_example' # str | 

try:
    # Get custom field of project
    api_response = api_instance.get_custom_field1(project_uid, field_instance_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_custom_field1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **field_instance_uid** | **str**|  | 

### Return type

[**CustomFieldInstanceDto**](CustomFieldInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_fields_page**
> PageDtoCustomFieldInstanceDto get_custom_fields_page(project_uid, page_number=page_number, page_size=page_size, created_by=created_by, modified_by=modified_by, sort_field=sort_field, sort_trend=sort_trend)

Get custom fields of project (page)

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 20 # int | Page size, accepts values between 1 and 50, default 20 (optional) (default to 20)
created_by = ['created_by_example'] # list[str] | Filter by webhook creators UIDs (optional)
modified_by = ['modified_by_example'] # list[str] | Filter by webhook updaters UIDs (optional)
sort_field = 'sort_field_example' # str | Sort by this field (optional)
sort_trend = 'ASC' # str | Sort direction (optional) (default to ASC)

try:
    # Get custom fields of project (page)
    api_response = api_instance.get_custom_fields_page(project_uid, page_number=page_number, page_size=page_size, created_by=created_by, modified_by=modified_by, sort_field=sort_field, sort_trend=sort_trend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_custom_fields_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 20 | [optional] [default to 20]
 **created_by** | [**list[str]**](str.md)| Filter by webhook creators UIDs | [optional] 
 **modified_by** | [**list[str]**](str.md)| Filter by webhook updaters UIDs | [optional] 
 **sort_field** | **str**| Sort by this field | [optional] 
 **sort_trend** | **str**| Sort direction | [optional] [default to ASC]

### Return type

[**PageDtoCustomFieldInstanceDto**](PageDtoCustomFieldInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_naming_settings**
> FileNamingSettingsDto get_file_naming_settings(project_uid)

Get file naming settings for project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get file naming settings for project
    api_response = api_instance.get_file_naming_settings(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_file_naming_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**FileNamingSettingsDto**](FileNamingSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_settings**
> FinancialSettingsDto get_financial_settings(project_uid)

Get financial settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get financial settings
    api_response = api_instance.get_financial_settings(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_financial_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**FinancialSettingsDto**](FinancialSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_settings2**
> FileImportSettingsDto get_import_settings2(project_uid)

Get projects's default import settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get projects's default import settings
    api_response = api_instance.get_import_settings2(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_import_settings2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**FileImportSettingsDto**](FileImportSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mt_settings_for_project**
> MTSettingsPerLanguageListDto get_mt_settings_for_project(project_uid)

Get project machine translate settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get project machine translate settings
    api_response = api_instance.get_mt_settings_for_project(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_mt_settings_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**MTSettingsPerLanguageListDto**](MTSettingsPerLanguageListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pre_translate_settings_for_project2**
> PreTranslateSettingsV3Dto get_pre_translate_settings_for_project2(project_uid)

Get Pre-translate settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get Pre-translate settings
    api_response = api_instance.get_pre_translate_settings_for_project2(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_pre_translate_settings_for_project2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**PreTranslateSettingsV3Dto**](PreTranslateSettingsV3Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> AbstractProjectDto get_project(project_uid)

Get project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get project
    api_response = api_instance.get_project(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**AbstractProjectDto**](AbstractProjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_access_settings_v2**
> ProjectSecuritySettingsDtoV2 get_project_access_settings_v2(project_uid)

Get access and security settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get access and security settings
    api_response = api_instance.get_project_access_settings_v2(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_access_settings_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**ProjectSecuritySettingsDtoV2**](ProjectSecuritySettingsDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_assignments**
> PageDtoProviderReference get_project_assignments(project_uid, provider_name=provider_name, page_number=page_number, page_size=page_size)

List project providers

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
provider_name = 'provider_name_example' # str |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List project providers
    api_response = api_instance.get_project_assignments(project_uid, provider_name=provider_name, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_assignments: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_settings**
> LqaSettingsDto get_project_settings(project_uid, workflow_level=workflow_level)

Get LQA settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
workflow_level = 1 # int |  (optional) (default to 1)

try:
    # Get LQA settings
    api_response = api_instance.get_project_settings(project_uid, workflow_level=workflow_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **workflow_level** | **int**|  | [optional] [default to 1]

### Return type

[**LqaSettingsDto**](LqaSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_term_bases**
> ProjectTermBaseListDto get_project_term_bases(project_uid)

Get term bases

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get term bases
    api_response = api_instance.get_project_term_bases(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_term_bases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**ProjectTermBaseListDto**](ProjectTermBaseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_trans_memories1**
> ProjectTransMemoryListDtoV3 get_project_trans_memories1(project_uid, target_lang=target_lang, wf_step_uid=wf_step_uid)

Get translation memories

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
target_lang = 'target_lang_example' # str | Filter project translation memories by target language (optional)
wf_step_uid = 'wf_step_uid_example' # str | Filter project translation memories by workflow step (optional)

try:
    # Get translation memories
    api_response = api_instance.get_project_trans_memories1(project_uid, target_lang=target_lang, wf_step_uid=wf_step_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_trans_memories1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **target_lang** | **str**| Filter project translation memories by target language | [optional] 
 **wf_step_uid** | **str**| Filter project translation memories by workflow step | [optional] 

### Return type

[**ProjectTransMemoryListDtoV3**](ProjectTransMemoryListDtoV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_workflow_steps_v2**
> ProjectWorkflowStepListDtoV2 get_project_workflow_steps_v2(project_uid, with_assigned_jobs=with_assigned_jobs)

Get workflow steps

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
with_assigned_jobs = false # bool | Return only steps containing jobs assigned to the calling linguist. (optional) (default to false)

try:
    # Get workflow steps
    api_response = api_instance.get_project_workflow_steps_v2(project_uid, with_assigned_jobs=with_assigned_jobs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_workflow_steps_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **with_assigned_jobs** | **bool**| Return only steps containing jobs assigned to the calling linguist. | [optional] [default to false]

### Return type

[**ProjectWorkflowStepListDtoV2**](ProjectWorkflowStepListDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotes_for_project**
> PageDtoQuoteDto get_quotes_for_project(project_uid, page_number=page_number, page_size=page_size)

List quotes

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List quotes
    api_response = api_instance.get_quotes_for_project(project_uid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_quotes_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoQuoteDto**](PageDtoQuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assigned_projects**
> PageDtoProjectReference list_assigned_projects(user_uid, status=status, target_lang=target_lang, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, project_name=project_name, page_number=page_number, page_size=page_size)

List assigned projects

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
user_uid = 'user_uid_example' # str | 
status = ['status_example'] # list[str] |  (optional)
target_lang = ['target_lang_example'] # list[str] |  (optional)
workflow_step_id = 789 # int |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
project_name = 'project_name_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned projects
    api_response = api_instance.list_assigned_projects(user_uid, status=status, target_lang=target_lang, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, project_name=project_name, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_assigned_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **target_lang** | [**list[str]**](str.md)|  | [optional] 
 **workflow_step_id** | **int**|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **project_name** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoProjectReference**](PageDtoProjectReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_by_project_v3**
> PageDtoAnalyseReference list_by_project_v3(project_uid, name=name, uid=uid, page_number=page_number, page_size=page_size, sort=sort, order=order, only_owner_org=only_owner_org)

List analyses by project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
name = 'name_example' # str | Name to search by (optional)
uid = 'uid_example' # str | Uid to search by (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
sort = 'DATE_CREATED' # str | Sorting field (optional) (default to DATE_CREATED)
order = 'desc' # str | Sorting order (optional) (default to desc)
only_owner_org = true # bool |  (optional)

try:
    # List analyses by project
    api_response = api_instance.list_by_project_v3(project_uid, name=name, uid=uid, page_number=page_number, page_size=page_size, sort=sort, order=order, only_owner_org=only_owner_org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_by_project_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **name** | **str**| Name to search by | [optional] 
 **uid** | **str**| Uid to search by | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **sort** | **str**| Sorting field | [optional] [default to DATE_CREATED]
 **order** | **str**| Sorting order | [optional] [default to desc]
 **only_owner_org** | **bool**|  | [optional] 

### Return type

[**PageDtoAnalyseReference**](PageDtoAnalyseReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> PageDtoAbstractProjectDto list_projects(name=name, client_id=client_id, client_name=client_name, business_unit_id=business_unit_id, business_unit_name=business_unit_name, statuses=statuses, target_langs=target_langs, domain_id=domain_id, domain_name=domain_name, sub_domain_id=sub_domain_id, sub_domain_name=sub_domain_name, cost_center_id=cost_center_id, cost_center_name=cost_center_name, due_in_hours=due_in_hours, created_in_last_hours=created_in_last_hours, source_langs=source_langs, owner_id=owner_id, job_statuses=job_statuses, job_status_group=job_status_group, buyer_id=buyer_id, page_number=page_number, page_size=page_size, name_or_internal_id=name_or_internal_id, include_archived=include_archived, archived_only=archived_only)

List projects

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
name = 'name_example' # str |  (optional)
client_id = 789 # int |  (optional)
client_name = 'client_name_example' # str |  (optional)
business_unit_id = 789 # int |  (optional)
business_unit_name = 'business_unit_name_example' # str |  (optional)
statuses = ['statuses_example'] # list[str] |  (optional)
target_langs = ['target_langs_example'] # list[str] |  (optional)
domain_id = 789 # int |  (optional)
domain_name = 'domain_name_example' # str |  (optional)
sub_domain_id = 789 # int |  (optional)
sub_domain_name = 'sub_domain_name_example' # str |  (optional)
cost_center_id = 789 # int |  (optional)
cost_center_name = 'cost_center_name_example' # str |  (optional)
due_in_hours = 56 # int | -1 for projects that are overdue (optional)
created_in_last_hours = 56 # int |  (optional)
source_langs = ['source_langs_example'] # list[str] |  (optional)
owner_id = 789 # int |  (optional)
job_statuses = ['job_statuses_example'] # list[str] | Allowed for linguists only (optional)
job_status_group = 'job_status_group_example' # str | Allowed for linguists only (optional)
buyer_id = 789 # int |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
name_or_internal_id = 'name_or_internal_id_example' # str | Name or internal ID of project (optional)
include_archived = false # bool | List also archived projects (optional) (default to false)
archived_only = false # bool | List only archived projects, regardless of `includeArchived` (optional) (default to false)

try:
    # List projects
    api_response = api_instance.list_projects(name=name, client_id=client_id, client_name=client_name, business_unit_id=business_unit_id, business_unit_name=business_unit_name, statuses=statuses, target_langs=target_langs, domain_id=domain_id, domain_name=domain_name, sub_domain_id=sub_domain_id, sub_domain_name=sub_domain_name, cost_center_id=cost_center_id, cost_center_name=cost_center_name, due_in_hours=due_in_hours, created_in_last_hours=created_in_last_hours, source_langs=source_langs, owner_id=owner_id, job_statuses=job_statuses, job_status_group=job_status_group, buyer_id=buyer_id, page_number=page_number, page_size=page_size, name_or_internal_id=name_or_internal_id, include_archived=include_archived, archived_only=archived_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **client_id** | **int**|  | [optional] 
 **client_name** | **str**|  | [optional] 
 **business_unit_id** | **int**|  | [optional] 
 **business_unit_name** | **str**|  | [optional] 
 **statuses** | [**list[str]**](str.md)|  | [optional] 
 **target_langs** | [**list[str]**](str.md)|  | [optional] 
 **domain_id** | **int**|  | [optional] 
 **domain_name** | **str**|  | [optional] 
 **sub_domain_id** | **int**|  | [optional] 
 **sub_domain_name** | **str**|  | [optional] 
 **cost_center_id** | **int**|  | [optional] 
 **cost_center_name** | **str**|  | [optional] 
 **due_in_hours** | **int**| -1 for projects that are overdue | [optional] 
 **created_in_last_hours** | **int**|  | [optional] 
 **source_langs** | [**list[str]**](str.md)|  | [optional] 
 **owner_id** | **int**|  | [optional] 
 **job_statuses** | [**list[str]**](str.md)| Allowed for linguists only | [optional] 
 **job_status_group** | **str**| Allowed for linguists only | [optional] 
 **buyer_id** | **int**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **name_or_internal_id** | **str**| Name or internal ID of project | [optional] 
 **include_archived** | **bool**| List also archived projects | [optional] [default to false]
 **archived_only** | **bool**| List only archived projects, regardless of &#x60;includeArchived&#x60; | [optional] [default to false]

### Return type

[**PageDtoAbstractProjectDto**](PageDtoAbstractProjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers3**
> ProviderListDtoV2 list_providers3(project_uid)

Get suggested providers

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get suggested providers
    api_response = api_instance.list_providers3(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_providers3: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project**
> AbstractProjectDto patch_project(project_uid, body=body)

Edit project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.PatchProjectDto() # PatchProjectDto |  (optional)

try:
    # Edit project
    api_response = api_instance.patch_project(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->patch_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**PatchProjectDto**](PatchProjectDto.md)|  | [optional] 

### Return type

[**AbstractProjectDto**](AbstractProjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relevant_term_bases**
> PageDtoTermBaseDto relevant_term_bases(project_uid, name=name, domain_name=domain_name, client_name=client_name, sub_domain_name=sub_domain_name, target_langs=target_langs, strict_lang_matching=strict_lang_matching, page_number=page_number, page_size=page_size)

List project relevant term bases

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
name = 'name_example' # str |  (optional)
domain_name = 'domain_name_example' # str |  (optional)
client_name = 'client_name_example' # str |  (optional)
sub_domain_name = 'sub_domain_name_example' # str |  (optional)
target_langs = ['target_langs_example'] # list[str] |  (optional)
strict_lang_matching = false # bool |  (optional) (default to false)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List project relevant term bases
    api_response = api_instance.relevant_term_bases(project_uid, name=name, domain_name=domain_name, client_name=client_name, sub_domain_name=sub_domain_name, target_langs=target_langs, strict_lang_matching=strict_lang_matching, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->relevant_term_bases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **name** | **str**|  | [optional] 
 **domain_name** | **str**|  | [optional] 
 **client_name** | **str**|  | [optional] 
 **sub_domain_name** | **str**|  | [optional] 
 **target_langs** | [**list[str]**](str.md)|  | [optional] 
 **strict_lang_matching** | **bool**|  | [optional] [default to false]
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoTermBaseDto**](PageDtoTermBaseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relevant_trans_memories1**
> PageDtoTransMemoryDto relevant_trans_memories1(project_uid, name=name, domain_name=domain_name, client_name=client_name, sub_domain_name=sub_domain_name, target_langs=target_langs, strict_lang_matching=strict_lang_matching, page_number=page_number, page_size=page_size)

List project relevant translation memories

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
name = 'name_example' # str |  (optional)
domain_name = 'domain_name_example' # str |  (optional)
client_name = 'client_name_example' # str |  (optional)
sub_domain_name = 'sub_domain_name_example' # str |  (optional)
target_langs = ['target_langs_example'] # list[str] |  (optional)
strict_lang_matching = false # bool |  (optional) (default to false)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List project relevant translation memories
    api_response = api_instance.relevant_trans_memories1(project_uid, name=name, domain_name=domain_name, client_name=client_name, sub_domain_name=sub_domain_name, target_langs=target_langs, strict_lang_matching=strict_lang_matching, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->relevant_trans_memories1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **name** | **str**|  | [optional] 
 **domain_name** | **str**|  | [optional] 
 **client_name** | **str**|  | [optional] 
 **sub_domain_name** | **str**|  | [optional] 
 **target_langs** | [**list[str]**](str.md)|  | [optional] 
 **strict_lang_matching** | **bool**|  | [optional] [default to false]
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoTransMemoryDto**](PageDtoTransMemoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_segment1**
> SearchResponseListTmDto search_segment1(project_uid, body=body)

Search translation memory for segment in the project

Returns at most <i>maxSegments</i>             records with <i>score >= scoreThreshold</i> and at most <i>maxSubsegments</i> records which are subsegment,             i.e. the source text is substring of the query text.

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.SearchTMRequestDto() # SearchTMRequestDto |  (optional)

try:
    # Search translation memory for segment in the project
    api_response = api_instance.search_segment1(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->search_segment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SearchTMRequestDto**](SearchTMRequestDto.md)|  | [optional] 

### Return type

[**SearchResponseListTmDto**](SearchResponseListTmDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_financial_settings**
> FinancialSettingsDto set_financial_settings(project_uid, body=body)

Edit financial settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.SetFinancialSettingsDto() # SetFinancialSettingsDto |  (optional)

try:
    # Edit financial settings
    api_response = api_instance.set_financial_settings(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_financial_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SetFinancialSettingsDto**](SetFinancialSettingsDto.md)|  | [optional] 

### Return type

[**FinancialSettingsDto**](FinancialSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mt_settings_for_project**
> MTSettingsPerLanguageListDto set_mt_settings_for_project(project_uid, body=body)

Edit machine translate settings

This will erase all mtSettings per language for project.         To remove all machine translate settings from project call without a machineTranslateSettings parameter.

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.EditProjectMTSettingsDto() # EditProjectMTSettingsDto |  (optional)

try:
    # Edit machine translate settings
    api_response = api_instance.set_mt_settings_for_project(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_mt_settings_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**EditProjectMTSettingsDto**](EditProjectMTSettingsDto.md)|  | [optional] 

### Return type

[**MTSettingsPerLanguageListDto**](MTSettingsPerLanguageListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mt_settings_per_language_for_project**
> MTSettingsPerLanguageListDto set_mt_settings_per_language_for_project(project_uid, body=body)

Edit machine translate settings per language

This will erase mtSettings for project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.EditProjectMTSettPerLangListDto() # EditProjectMTSettPerLangListDto |  (optional)

try:
    # Edit machine translate settings per language
    api_response = api_instance.set_mt_settings_per_language_for_project(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_mt_settings_per_language_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**EditProjectMTSettPerLangListDto**](EditProjectMTSettPerLangListDto.md)|  | [optional] 

### Return type

[**MTSettingsPerLanguageListDto**](MTSettingsPerLanguageListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_qa_settings_v2**
> QASettingsDtoV2 set_project_qa_settings_v2(project_uid, body=body)

Edit quality assurance settings

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.EditQASettingsDtoV2() # EditQASettingsDtoV2 |  (optional)

try:
    # Edit quality assurance settings
    api_response = api_instance.set_project_qa_settings_v2(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_qa_settings_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**EditQASettingsDtoV2**](EditQASettingsDtoV2.md)|  | [optional] 

### Return type

[**QASettingsDtoV2**](QASettingsDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_status**
> set_project_status(project_uid, body=body)

Edit project status

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.SetProjectStatusDto() # SetProjectStatusDto |  (optional)

try:
    # Edit project status
    api_instance.set_project_status(project_uid, body=body)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SetProjectStatusDto**](SetProjectStatusDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_term_bases**
> ProjectTermBaseListDto set_project_term_bases(project_uid, body=body)

Edit term bases

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.SetTermBaseDto() # SetTermBaseDto |  (optional)

try:
    # Edit term bases
    api_response = api_instance.set_project_term_bases(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_term_bases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SetTermBaseDto**](SetTermBaseDto.md)|  | [optional] 

### Return type

[**ProjectTermBaseListDto**](ProjectTermBaseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_trans_memories_v3**
> ProjectTransMemoryListDtoV3 set_project_trans_memories_v3(project_uid, body=body)

Edit translation memories

If user wants to edit “All target languages” or \"All workflow steps”,                         but there are already varied TM settings for individual languages or steps,                         then the user risks to overwrite these individual choices.

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.SetProjectTransMemoriesV3Dto() # SetProjectTransMemoriesV3Dto |  (optional)

try:
    # Edit translation memories
    api_response = api_instance.set_project_trans_memories_v3(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_trans_memories_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SetProjectTransMemoriesV3Dto**](SetProjectTransMemoriesV3Dto.md)|  | [optional] 

### Return type

[**ProjectTransMemoryListDtoV3**](ProjectTransMemoryListDtoV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_naming_settings**
> FileNamingSettingsDto update_file_naming_settings(project_uid, body=body)

Update file naming settings for project

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.FileNamingSettingsDto() # FileNamingSettingsDto |  (optional)

try:
    # Update file naming settings for project
    api_response = api_instance.update_file_naming_settings(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_file_naming_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**FileNamingSettingsDto**](FileNamingSettingsDto.md)|  | [optional] 

### Return type

[**FileNamingSettingsDto**](FileNamingSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

