# phrasetms_client.JobApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_part**](JobApi.md#compare_part) | **POST** /api2/v1/projects/{projectUid}/jobs/compare | Compare jobs on workflow levels
[**completed_file1**](JobApi.md#completed_file1) | **PUT** /api2/v2/projects/{projectUid}/jobs/{jobUid}/targetFile | Download target file (async)
[**copy_source_to_target**](JobApi.md#copy_source_to_target) | **POST** /api2/v1/projects/{projectUid}/jobs/copySourceToTarget | Copy Source to Target
[**copy_source_to_target_job_part**](JobApi.md#copy_source_to_target_job_part) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/copySourceToTarget | Copy Source to Target job
[**create_job**](JobApi.md#create_job) | **POST** /api2/v1/projects/{projectUid}/jobs | Create job
[**create_job_from_async_download_task**](JobApi.md#create_job_from_async_download_task) | **POST** /api2/v1/projects/{projectUid}/jobs/connectorTask | Create job from connector asynchronous download task
[**create_term_by_job**](JobApi.md#create_term_by_job) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/termBases/createByJob | Create term in job&#39;s term bases
[**delete_all_translations**](JobApi.md#delete_all_translations) | **DELETE** /api2/v1/projects/{projectUid}/jobs/translations | Delete all translations
[**delete_all_translations1**](JobApi.md#delete_all_translations1) | **DELETE** /api2/v2/projects/{projectUid}/jobs/translations | Delete specific translations
[**delete_handover_file**](JobApi.md#delete_handover_file) | **DELETE** /api2/v1/projects/{projectUid}/fileHandovers | Delete handover file
[**delete_parts**](JobApi.md#delete_parts) | **DELETE** /api2/v1/projects/{projectUid}/jobs/batch | Delete job (batch)
[**download_completed_file**](JobApi.md#download_completed_file) | **GET** /api2/v2/projects/{projectUid}/jobs/{jobUid}/downloadTargetFile/{asyncRequestId} | Download target file based on async request
[**edit_job_import_settings**](JobApi.md#edit_job_import_settings) | **PUT** /api2/v1/projects/{projectUid}/jobs/{jobUid}/importSettings | Edit job import settings
[**edit_part**](JobApi.md#edit_part) | **PUT** /api2/v1/projects/{projectUid}/jobs/{jobUid} | Edit job
[**edit_parts**](JobApi.md#edit_parts) | **PUT** /api2/v1/projects/{projectUid}/jobs/batch | Edit jobs (batch)
[**export_to_online_repository**](JobApi.md#export_to_online_repository) | **POST** /api2/v3/projects/{projectUid}/jobs/export | Export jobs to online repository
[**file_preview**](JobApi.md#file_preview) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/preview | Download preview file
[**file_preview_job**](JobApi.md#file_preview_job) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/preview | Download preview file
[**get_bilingual_file**](JobApi.md#get_bilingual_file) | **POST** /api2/v1/projects/{projectUid}/jobs/bilingualFile | Download bilingual file
[**get_completed_file_warnings**](JobApi.md#get_completed_file_warnings) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/targetFileWarnings | Get target file&#39;s warnings
[**get_handover_files**](JobApi.md#get_handover_files) | **GET** /api2/v1/projects/{projectUid}/fileHandovers | Download handover file(s)
[**get_import_settings3**](JobApi.md#get_import_settings3) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/importSettings | Get import settings for job
[**get_original_file**](JobApi.md#get_original_file) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/original | Download original file
[**get_part**](JobApi.md#get_part) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid} | Get job
[**get_parts_workflow_step**](JobApi.md#get_parts_workflow_step) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/workflowStep | Get job&#39;s workflowStep
[**get_segments_count**](JobApi.md#get_segments_count) | **POST** /api2/v1/projects/{projectUid}/jobs/segmentsCount | Get segments count
[**get_translation_resources**](JobApi.md#get_translation_resources) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources | Get translation resources
[**list_part_analyse_v3**](JobApi.md#list_part_analyse_v3) | **GET** /api2/v3/projects/{projectUid}/jobs/{jobUid}/analyses | List analyses
[**list_parts_v2**](JobApi.md#list_parts_v2) | **GET** /api2/v2/projects/{projectUid}/jobs | List jobs
[**list_providers4**](JobApi.md#list_providers4) | **POST** /api2/v2/projects/{projectUid}/jobs/{jobUid}/providers/suggest | Get suggested providers
[**list_segments**](JobApi.md#list_segments) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/segments | Get segments
[**notify_assigned**](JobApi.md#notify_assigned) | **POST** /api2/v1/projects/{projectUid}/jobs/notifyAssigned | Notify assigned users
[**patch_part**](JobApi.md#patch_part) | **PATCH** /api2/v1/projects/{projectUid}/jobs/{jobUid} | Patch job
[**patch_update_job_parts**](JobApi.md#patch_update_job_parts) | **PATCH** /api2/v3/jobs | Edit jobs (with possible partial updates)
[**preview_urls**](JobApi.md#preview_urls) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/previewUrl | Get PDF preview
[**pseudo_translate1**](JobApi.md#pseudo_translate1) | **POST** /api2/v2/projects/{projectUid}/jobs/pseudoTranslate | Pseudo-translate job
[**pseudo_translate_job_part**](JobApi.md#pseudo_translate_job_part) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/pseudoTranslate | Pseudo-translates job
[**search_by_job3**](JobApi.md#search_by_job3) | **POST** /api2/v3/projects/{projectUid}/jobs/{jobUid}/transMemories/search | Search job&#39;s translation memories
[**search_parts_in_project**](JobApi.md#search_parts_in_project) | **POST** /api2/v1/projects/{projectUid}/jobs/search | Search jobs in project
[**search_segment_by_job**](JobApi.md#search_segment_by_job) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/transMemories/searchSegment | Search translation memory for segment by job
[**search_terms_by_job1**](JobApi.md#search_terms_by_job1) | **POST** /api2/v2/projects/{projectUid}/jobs/{jobUid}/termBases/searchByJob | Search job&#39;s term bases
[**search_terms_in_text_by_job_v2**](JobApi.md#search_terms_in_text_by_job_v2) | **POST** /api2/v2/projects/{projectUid}/jobs/{jobUid}/termBases/searchInTextByJob | Search terms in text
[**set_status**](JobApi.md#set_status) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/setStatus | Edit job status
[**split**](JobApi.md#split) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/split | Split job
[**status_changes**](JobApi.md#status_changes) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/statusChanges | Get status changes
[**update_source**](JobApi.md#update_source) | **POST** /api2/v1/projects/{projectUid}/jobs/source | Update source
[**update_target**](JobApi.md#update_target) | **POST** /api2/v1/projects/{projectUid}/jobs/target | Update target
[**upload_bilingual_file**](JobApi.md#upload_bilingual_file) | **PUT** /api2/v1/bilingualFiles | Upload bilingual file
[**upload_handover_file**](JobApi.md#upload_handover_file) | **PUT** /api2/v1/projects/{projectUid}/fileHandovers | Upload handover file
[**web_editor_link_v2**](JobApi.md#web_editor_link_v2) | **POST** /api2/v2/projects/{projectUid}/jobs/webEditor | Get Web Editor URL
[**wild_card_search_by_job3**](JobApi.md#wild_card_search_by_job3) | **POST** /api2/v3/projects/{projectUid}/jobs/{jobUid}/transMemories/wildCardSearch | Wildcard search job&#39;s translation memories


# **compare_part**
> ComparedSegmentsDto compare_part(project_uid, at_workflow_level=at_workflow_level, with_workflow_level=with_workflow_level, body=body)

Compare jobs on workflow levels

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.compared_segments_dto import ComparedSegmentsDto
from phrasetms_client.models.job_part_ready_references import JobPartReadyReferences
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    at_workflow_level = 1 # int |  (optional) (default to 1)
    with_workflow_level = 1 # int |  (optional) (default to 1)
    body = phrasetms_client.JobPartReadyReferences() # JobPartReadyReferences |  (optional)

    try:
        # Compare jobs on workflow levels
        api_response = api_instance.compare_part(project_uid, at_workflow_level=at_workflow_level, with_workflow_level=with_workflow_level, body=body)
        print("The response of JobApi->compare_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->compare_part: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **at_workflow_level** | **int**|  | [optional] [default to 1]
 **with_workflow_level** | **int**|  | [optional] [default to 1]
 **body** | [**JobPartReadyReferences**](JobPartReadyReferences.md)|  | [optional] 

### Return type

[**ComparedSegmentsDto**](ComparedSegmentsDto.md)

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

# **completed_file1**
> completed_file1(project_uid, job_uid)

Download target file (async)

     This call will create async request for downloading target file with translation that can be downloaded when     finished. This means even for other jobs that were created via 'split jobs' etc.     

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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Download target file (async)
        api_instance.completed_file1(project_uid, job_uid)
    except Exception as e:
        print("Exception when calling JobApi->completed_file1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

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

# **copy_source_to_target**
> copy_source_to_target(project_uid, body=body)

Copy Source to Target

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_ready_references import JobPartReadyReferences
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.JobPartReadyReferences() # JobPartReadyReferences |  (optional)

    try:
        # Copy Source to Target
        api_instance.copy_source_to_target(project_uid, body=body)
    except Exception as e:
        print("Exception when calling JobApi->copy_source_to_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**JobPartReadyReferences**](JobPartReadyReferences.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **copy_source_to_target_job_part**
> copy_source_to_target_job_part(project_uid, job_uid)

Copy Source to Target job

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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Copy Source to Target job
        api_instance.copy_source_to_target_job_part(project_uid, job_uid)
    except Exception as e:
        print("Exception when calling JobApi->copy_source_to_target_job_part: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

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

# **create_job**
> JobListDto create_job(project_uid, memsource=memsource, content_disposition=content_disposition, body=body)

Create job

 Job file can be provided directly in the message body or downloaded from connector.   Please supply job metadata in `Memsource` header.   For file in the request body provide also the filename in `Content-Disposition` header.  Accepted metadata:     - `targetLangs` - **required**   - `due` - ISO 8601   - `workflowSettings` - project with workflow - see examples bellow   - `assignments` - project without workflows - see examples bellow   - `importSettings` - re-usable import settings - see [Create import settings](#operation/createImportSettings)   - `useProjectFileImportSettings` - mutually exclusive with importSettings   - `callbackUrl` - consumer callback   - `path` - original destination directory   - `preTranslate` - set pre translate job after import      for remote file jobs also `remoteFile` - see examples bellow:   - `connectorToken` - remote connector token   - `remoteFolder`    - `remoteFileName`   - `continuous` - true for continuous job  Create and assign job in project without workflow step: ```  {   \"targetLangs\": [     \"cs_cz\"   ],   \"callbackUrl\": \"https://my-shiny-service.com/consumeCallback\",   \"importSettings\": {     \"uid\": \"abcd123\"   },   \"due\": \"2007-12-03T10:15:30.00Z\",   \"path\": \"destination directory\",   \"assignments\": [     {       \"targetLang\": \"cs_cz\",       \"providers\": [         {           \"id\": \"4321\",           \"type\": \"USER\"         }       ]     }   ],   \"notifyProvider\": {     \"organizationEmailTemplate\": {       \"id\": \"39\"     },     \"notificationIntervalInMinutes\": \"10\"   } } ```  Create job from remote file without workflow steps: ```  {   \"remoteFile\": {     \"connectorToken\": \"948123ef-e1ef-4cd3-a90e-af1617848af3\",     \"remoteFolder\": \"/\",     \"remoteFileName\": \"Few words.docx\",     \"continuous\": false   },   \"assignments\": [],   \"workflowSettings\": [],   \"targetLangs\": [     \"cs\"   ] } ```  Create and assign job in project with workflow step: ```  {   \"targetLangs\": [     \"de\"   ],   \"useProjectFileImportSettings\": \"true\",   \"workflowSettings\": [     {       \"id\": \"64\",       \"due\": \"2007-12-03T10:15:30.00Z\",       \"assignments\": [         {           \"targetLang\": \"de\",           \"providers\": [             {               \"id\": \"3\",               \"type\": \"VENDOR\"             }           ]         }       ],       \"notifyProvider\": {         \"organizationEmailTemplate\": {           \"id\": \"39\"         },         \"notificationIntervalInMinutes\": \"10\"       }     }   ] } ```     

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_list_dto import JobListDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    memsource = 'memsource_example' # str |  (optional)
    content_disposition = 'content_disposition_example' # str | must match pattern `((inline|attachment); )?(filename\\*=UTF-8''(.+)|filename=\"?(.+)\"?)` (optional)
    body = None # object |  (optional)

    try:
        # Create job
        api_response = api_instance.create_job(project_uid, memsource=memsource, content_disposition=content_disposition, body=body)
        print("The response of JobApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->create_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **memsource** | **str**|  | [optional] 
 **content_disposition** | **str**| must match pattern &#x60;((inline|attachment); )?(filename\\*&#x3D;UTF-8&#39;&#39;(.+)|filename&#x3D;\&quot;?(.+)\&quot;?)&#x60; | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**JobListDto**](JobListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
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

# **create_job_from_async_download_task**
> JobListDto create_job_from_async_download_task(project_uid, download_task_id=download_task_id, continuous=continuous, body=body)

Create job from connector asynchronous download task

 Creates the job in project specified by path param projectUid. Source file is defined by downloadTaskId parameter. That is value of finished download async task  [Connector - Download file (async)](#operation/getFile_1).  Please supply job metadata in body.  Accepted metadata:     - `targetLangs` - **required**   - `due` - ISO 8601   - `workflowSettings` - project with workflow - see examples bellow   - `assignments` - project without workflows - see examples bellow   - `importSettings` - re-usable import settings - see [Create import settings](#operation/createImportSettings)   - `useProjectFileImportSettings` - mutually exclusive with importSettings   - `callbackUrl` - consumer callback   - `path` - original destination directory   - `preTranslate` - set pre translate job after import    Create job simple (without workflow steps, without assignments): ``` {   \"targetLangs\": [     \"cs_cz\",     \"es_es\"   ] } ```  Create and assign job in project without workflow step: ``` {   \"targetLangs\": [     \"cs_cz\"   ],   \"callbackUrl\": \"https://my-shiny-service.com/consumeCallback\",   \"importSettings\": {     \"uid\": \"abcd123\"   },   \"due\": \"2007-12-03T10:15:30.00Z\",   \"path\": \"destination directory\",   \"assignments\": [     {       \"targetLang\": \"cs_cz\",       \"providers\": [         {           \"id\": \"4321\",           \"type\": \"USER\"         }       ]     }   ],   \"notifyProvider\": {     \"organizationEmailTemplate\": {       \"id\": \"39\"     },     \"notificationIntervalInMinutes\": \"10\"   } } ```  Create and assign job in project with workflow step: ``` {   \"targetLangs\": [     \"de\"   ],   \"useProjectFileImportSettings\": \"true\",   \"workflowSettings\": [     {       \"id\": \"64\",       \"due\": \"2007-12-03T10:15:30.00Z\",       \"assignments\": [         {           \"targetLang\": \"de\",           \"providers\": [             {               \"id\": \"3\",               \"type\": \"VENDOR\"             }           ]         }       ],       \"notifyProvider\": {         \"organizationEmailTemplate\": {           \"id\": \"39\"         },         \"notificationIntervalInMinutes\": \"10\"       }     }   ] } ```     

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_create_request_dto import JobCreateRequestDto
from phrasetms_client.models.job_list_dto import JobListDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    download_task_id = 'download_task_id_example' # str |  (optional)
    continuous = False # bool |  (optional) (default to False)
    body = phrasetms_client.JobCreateRequestDto() # JobCreateRequestDto |  (optional)

    try:
        # Create job from connector asynchronous download task
        api_response = api_instance.create_job_from_async_download_task(project_uid, download_task_id=download_task_id, continuous=continuous, body=body)
        print("The response of JobApi->create_job_from_async_download_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->create_job_from_async_download_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **download_task_id** | **str**|  | [optional] 
 **continuous** | **bool**|  | [optional] [default to False]
 **body** | [**JobCreateRequestDto**](JobCreateRequestDto.md)|  | [optional] 

### Return type

[**JobListDto**](JobListDto.md)

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

# **create_term_by_job**
> TermPairDto create_term_by_job(job_uid, project_uid, body=body)

Create term in job's term bases

Create new term in the write term base assigned to the job

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.create_terms_dto import CreateTermsDto
from phrasetms_client.models.term_pair_dto import TermPairDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    job_uid = 'job_uid_example' # str | 
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.CreateTermsDto() # CreateTermsDto |  (optional)

    try:
        # Create term in job's term bases
        api_response = api_instance.create_term_by_job(job_uid, project_uid, body=body)
        print("The response of JobApi->create_term_by_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->create_term_by_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **project_uid** | **str**|  | 
 **body** | [**CreateTermsDto**](CreateTermsDto.md)|  | [optional] 

### Return type

[**TermPairDto**](TermPairDto.md)

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

# **delete_all_translations**
> delete_all_translations(project_uid, body=body)

Delete all translations

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_ready_references import JobPartReadyReferences
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.JobPartReadyReferences() # JobPartReadyReferences |  (optional)

    try:
        # Delete all translations
        api_instance.delete_all_translations(project_uid, body=body)
    except Exception as e:
        print("Exception when calling JobApi->delete_all_translations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**JobPartReadyReferences**](JobPartReadyReferences.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **delete_all_translations1**
> delete_all_translations1(project_uid, body=body)

Delete specific translations

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_ready_delete_translation_dto import JobPartReadyDeleteTranslationDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.JobPartReadyDeleteTranslationDto() # JobPartReadyDeleteTranslationDto |  (optional)

    try:
        # Delete specific translations
        api_instance.delete_all_translations1(project_uid, body=body)
    except Exception as e:
        print("Exception when calling JobApi->delete_all_translations1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**JobPartReadyDeleteTranslationDto**](JobPartReadyDeleteTranslationDto.md)|  | [optional] 

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

# **delete_handover_file**
> delete_handover_file(project_uid, body=body)

Delete handover file

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_references import JobPartReferences
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.JobPartReferences() # JobPartReferences |  (optional)

    try:
        # Delete handover file
        api_instance.delete_handover_file(project_uid, body=body)
    except Exception as e:
        print("Exception when calling JobApi->delete_handover_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**JobPartReferences**](JobPartReferences.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **delete_parts**
> delete_parts(project_uid, purge=purge, body=body)

Delete job (batch)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_delete_references import JobPartDeleteReferences
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    purge = False # bool |  (optional) (default to False)
    body = phrasetms_client.JobPartDeleteReferences() # JobPartDeleteReferences |  (optional)

    try:
        # Delete job (batch)
        api_instance.delete_parts(project_uid, purge=purge, body=body)
    except Exception as e:
        print("Exception when calling JobApi->delete_parts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **purge** | **bool**|  | [optional] [default to False]
 **body** | [**JobPartDeleteReferences**](JobPartDeleteReferences.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **download_completed_file**
> download_completed_file(project_uid, job_uid, async_request_id, format=format)

Download target file based on async request

     This call will return target file with translation. This means even for other jobs that were created via     'split jobs' etc.     

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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    async_request_id = 'async_request_id_example' # str | 
    format = 'ORIGINAL' # str |  (optional) (default to 'ORIGINAL')

    try:
        # Download target file based on async request
        api_instance.download_completed_file(project_uid, job_uid, async_request_id, format=format)
    except Exception as e:
        print("Exception when calling JobApi->download_completed_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **async_request_id** | **str**|  | 
 **format** | **str**|  | [optional] [default to &#39;ORIGINAL&#39;]

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
**200** | application/octet-stream |  * Content-Disposition - Contains filename (UTF-8 encoded).    &#x60;filename*&#x3D;UTF-8&#39;&#39;ExampleFileName.md&#x60; <br>  |
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

# **edit_job_import_settings**
> FileImportSettingsDto edit_job_import_settings(project_uid, job_uid, body=body)

Edit job import settings

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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.FileImportSettingsCreateDto() # FileImportSettingsCreateDto |  (optional)

    try:
        # Edit job import settings
        api_response = api_instance.edit_job_import_settings(project_uid, job_uid, body=body)
        print("The response of JobApi->edit_job_import_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->edit_job_import_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
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

# **edit_part**
> JobPartExtendedDto edit_part(project_uid, job_uid, body=body)

Edit job

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_extended_dto import JobPartExtendedDto
from phrasetms_client.models.job_part_update_single_dto import JobPartUpdateSingleDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.JobPartUpdateSingleDto() # JobPartUpdateSingleDto |  (optional)

    try:
        # Edit job
        api_response = api_instance.edit_part(project_uid, job_uid, body=body)
        print("The response of JobApi->edit_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->edit_part: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**JobPartUpdateSingleDto**](JobPartUpdateSingleDto.md)|  | [optional] 

### Return type

[**JobPartExtendedDto**](JobPartExtendedDto.md)

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

# **edit_parts**
> JobPartsDto edit_parts(project_uid, body=body)

Edit jobs (batch)

 Returns only jobs which were updated by the batch operation. 

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_update_batch_dto import JobPartUpdateBatchDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.JobPartUpdateBatchDto() # JobPartUpdateBatchDto |  (optional)

    try:
        # Edit jobs (batch)
        api_response = api_instance.edit_parts(project_uid, body=body)
        print("The response of JobApi->edit_parts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->edit_parts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**JobPartUpdateBatchDto**](JobPartUpdateBatchDto.md)|  | [optional] 

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

# **export_to_online_repository**
> JobExportResponseDto export_to_online_repository(project_uid, body=body)

Export jobs to online repository

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_export_action_dto import JobExportActionDto
from phrasetms_client.models.job_export_response_dto import JobExportResponseDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.JobExportActionDto() # JobExportActionDto |  (optional)

    try:
        # Export jobs to online repository
        api_response = api_instance.export_to_online_repository(project_uid, body=body)
        print("The response of JobApi->export_to_online_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->export_to_online_repository: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**JobExportActionDto**](JobExportActionDto.md)|  | [optional] 

### Return type

[**JobExportResponseDto**](JobExportResponseDto.md)

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

# **file_preview**
> file_preview(project_uid, job_uid, body=body)

Download preview file

Takes bilingual file (.mxliff only) as argument. If not passed, data will be taken from database

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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = None # object |  (optional)

    try:
        # Download preview file
        api_instance.file_preview(project_uid, job_uid, body=body)
    except Exception as e:
        print("Exception when calling JobApi->file_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/octet-stream |  * Content-Disposition - Contains filename (UTF-8 encoded).    &#x60;filename*&#x3D;UTF-8&#39;&#39;ExampleFileName.md&#x60; <br>  |
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

# **file_preview_job**
> file_preview_job(project_uid, job_uid)

Download preview file

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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Download preview file
        api_instance.file_preview_job(project_uid, job_uid)
    except Exception as e:
        print("Exception when calling JobApi->file_preview_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

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
**200** | application/octet-stream |  * Content-Disposition - Contains filename (UTF-8 encoded).    &#x60;filename*&#x3D;UTF-8&#39;&#39;ExampleFileName.md&#x60; <br>  |
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

# **get_bilingual_file**
> get_bilingual_file(project_uid, format=format, preview=preview, body=body)

Download bilingual file

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.get_bilingual_file_dto import GetBilingualFileDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    format = 'MXLF' # str |  (optional) (default to 'MXLF')
    preview = True # bool |  (optional) (default to True)
    body = phrasetms_client.GetBilingualFileDto() # GetBilingualFileDto |  (optional)

    try:
        # Download bilingual file
        api_instance.get_bilingual_file(project_uid, format=format, preview=preview, body=body)
    except Exception as e:
        print("Exception when calling JobApi->get_bilingual_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **format** | **str**|  | [optional] [default to &#39;MXLF&#39;]
 **preview** | **bool**|  | [optional] [default to True]
 **body** | [**GetBilingualFileDto**](GetBilingualFileDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/octet-stream, application/mxliff, application/xliff+xml |  * Content-Disposition - Contains filename (UTF-8 encoded).    &#x60;filename*&#x3D;UTF-8&#39;&#39;ExampleFileName.md&#x60; <br>  |
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

# **get_completed_file_warnings**
> TargetFileWarningsDto get_completed_file_warnings(project_uid, job_uid)

Get target file's warnings

 This call will return target file's warnings. This means even for other jobs that were created via 'split jobs' etc. 

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.target_file_warnings_dto import TargetFileWarningsDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get target file's warnings
        api_response = api_instance.get_completed_file_warnings(project_uid, job_uid)
        print("The response of JobApi->get_completed_file_warnings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_completed_file_warnings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**TargetFileWarningsDto**](TargetFileWarningsDto.md)

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

# **get_handover_files**
> get_handover_files(project_uid, job_uid=job_uid)

Download handover file(s)

 For downloading multiple files as ZIP file provide multiple IDs in query parameters. * For example `?jobUid={id1}&jobUid={id2}` * When no files matched given IDs error 404 is returned, otherwise ZIP file will include those that were found 

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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = ['job_uid_example'] # List[str] | JobPart Id of requested handover file (optional)

    try:
        # Download handover file(s)
        api_instance.get_handover_files(project_uid, job_uid=job_uid)
    except Exception as e:
        print("Exception when calling JobApi->get_handover_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | [**List[str]**](str.md)| JobPart Id of requested handover file | [optional] 

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
**200** | File / Archive with file handovers |  -  |
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

# **get_import_settings3**
> FileImportSettingsDto get_import_settings3(project_uid, job_uid)

Get import settings for job

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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get import settings for job
        api_response = api_instance.get_import_settings3(project_uid, job_uid)
        print("The response of JobApi->get_import_settings3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_import_settings3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

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

# **get_original_file**
> get_original_file(project_uid, job_uid)

Download original file

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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Download original file
        api_instance.get_original_file(project_uid, job_uid)
    except Exception as e:
        print("Exception when calling JobApi->get_original_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

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
**200** | application/octet-stream |  * Content-Disposition - Contains filename (UTF-8 encoded).    &#x60;filename*&#x3D;UTF-8&#39;&#39;ExampleFileName.md&#x60; <br>  |
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

# **get_part**
> JobPartExtendedDto get_part(project_uid, job_uid)

Get job

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_extended_dto import JobPartExtendedDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get job
        api_response = api_instance.get_part(project_uid, job_uid)
        print("The response of JobApi->get_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_part: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**JobPartExtendedDto**](JobPartExtendedDto.md)

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

# **get_parts_workflow_step**
> ProjectWorkflowStepDto get_parts_workflow_step(project_uid, job_uid)

Get job's workflowStep

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_workflow_step_dto import ProjectWorkflowStepDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get job's workflowStep
        api_response = api_instance.get_parts_workflow_step(project_uid, job_uid)
        print("The response of JobApi->get_parts_workflow_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_parts_workflow_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**ProjectWorkflowStepDto**](ProjectWorkflowStepDto.md)

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

# **get_segments_count**
> SegmentsCountsResponseListDto get_segments_count(project_uid, body=body)

Get segments count

Provides segments count (progress data)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_ready_references import JobPartReadyReferences
from phrasetms_client.models.segments_counts_response_list_dto import SegmentsCountsResponseListDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.JobPartReadyReferences() # JobPartReadyReferences |  (optional)

    try:
        # Get segments count
        api_response = api_instance.get_segments_count(project_uid, body=body)
        print("The response of JobApi->get_segments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_segments_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**JobPartReadyReferences**](JobPartReadyReferences.md)|  | [optional] 

### Return type

[**SegmentsCountsResponseListDto**](SegmentsCountsResponseListDto.md)

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

# **get_translation_resources**
> TranslationResourcesDto get_translation_resources(project_uid, job_uid)

Get translation resources

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.translation_resources_dto import TranslationResourcesDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get translation resources
        api_response = api_instance.get_translation_resources(project_uid, job_uid)
        print("The response of JobApi->get_translation_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->get_translation_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**TranslationResourcesDto**](TranslationResourcesDto.md)

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

# **list_part_analyse_v3**
> PageDtoAnalyseReference list_part_analyse_v3(project_uid, job_uid, page_number=page_number, page_size=page_size)

List analyses

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_analyse_reference import PageDtoAnalyseReference
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    page_number = 0 # int |  (optional) (default to 0)
    page_size = 50 # int |  (optional) (default to 50)

    try:
        # List analyses
        api_response = api_instance.list_part_analyse_v3(project_uid, job_uid, page_number=page_number, page_size=page_size)
        print("The response of JobApi->list_part_analyse_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->list_part_analyse_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoAnalyseReference**](PageDtoAnalyseReference.md)

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

# **list_parts_v2**
> PageDtoJobPartReferenceV2 list_parts_v2(project_uid, page_number=page_number, page_size=page_size, count=count, workflow_level=workflow_level, status=status, assigned_user=assigned_user, due_in_hours=due_in_hours, filename=filename, target_lang=target_lang, assigned_vendor=assigned_vendor)

List jobs

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_job_part_reference_v2 import PageDtoJobPartReferenceV2
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    page_number = 0 # int |  (optional) (default to 0)
    page_size = 50 # int |  (optional) (default to 50)
    count = False # bool |  (optional) (default to False)
    workflow_level = 1 # int |  (optional) (default to 1)
    status = ['status_example'] # List[str] |  (optional)
    assigned_user = 56 # int |  (optional)
    due_in_hours = 56 # int |  (optional)
    filename = 'filename_example' # str |  (optional)
    target_lang = 'target_lang_example' # str |  (optional)
    assigned_vendor = 56 # int |  (optional)

    try:
        # List jobs
        api_response = api_instance.list_parts_v2(project_uid, page_number=page_number, page_size=page_size, count=count, workflow_level=workflow_level, status=status, assigned_user=assigned_user, due_in_hours=due_in_hours, filename=filename, target_lang=target_lang, assigned_vendor=assigned_vendor)
        print("The response of JobApi->list_parts_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->list_parts_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]
 **count** | **bool**|  | [optional] [default to False]
 **workflow_level** | **int**|  | [optional] [default to 1]
 **status** | [**List[str]**](str.md)|  | [optional] 
 **assigned_user** | **int**|  | [optional] 
 **due_in_hours** | **int**|  | [optional] 
 **filename** | **str**|  | [optional] 
 **target_lang** | **str**|  | [optional] 
 **assigned_vendor** | **int**|  | [optional] 

### Return type

[**PageDtoJobPartReferenceV2**](PageDtoJobPartReferenceV2.md)

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

# **list_providers4**
> ProviderListDtoV2 list_providers4(project_uid, job_uid)

Get suggested providers

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.provider_list_dto_v2 import ProviderListDtoV2
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get suggested providers
        api_response = api_instance.list_providers4(project_uid, job_uid)
        print("The response of JobApi->list_providers4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->list_providers4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**ProviderListDtoV2**](ProviderListDtoV2.md)

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

# **list_segments**
> SegmentListDto list_segments(project_uid, job_uid, begin_index=begin_index, end_index=end_index)

Get segments

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.segment_list_dto import SegmentListDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    begin_index = 0 # int |  (optional) (default to 0)
    end_index = 0 # int |  (optional) (default to 0)

    try:
        # Get segments
        api_response = api_instance.list_segments(project_uid, job_uid, begin_index=begin_index, end_index=end_index)
        print("The response of JobApi->list_segments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->list_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **begin_index** | **int**|  | [optional] [default to 0]
 **end_index** | **int**|  | [optional] [default to 0]

### Return type

[**SegmentListDto**](SegmentListDto.md)

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

# **notify_assigned**
> notify_assigned(project_uid, body=body)

Notify assigned users

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.notify_job_parts_request_dto import NotifyJobPartsRequestDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.NotifyJobPartsRequestDto() # NotifyJobPartsRequestDto |  (optional)

    try:
        # Notify assigned users
        api_instance.notify_assigned(project_uid, body=body)
    except Exception as e:
        print("Exception when calling JobApi->notify_assigned: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**NotifyJobPartsRequestDto**](NotifyJobPartsRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **patch_part**
> JobPartExtendedDto patch_part(project_uid, job_uid, body=body)

Patch job

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_extended_dto import JobPartExtendedDto
from phrasetms_client.models.job_part_patch_single_dto import JobPartPatchSingleDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.JobPartPatchSingleDto() # JobPartPatchSingleDto |  (optional)

    try:
        # Patch job
        api_response = api_instance.patch_part(project_uid, job_uid, body=body)
        print("The response of JobApi->patch_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->patch_part: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**JobPartPatchSingleDto**](JobPartPatchSingleDto.md)|  | [optional] 

### Return type

[**JobPartExtendedDto**](JobPartExtendedDto.md)

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

# **patch_update_job_parts**
> JobPartPatchResultDto patch_update_job_parts(body=body)

Edit jobs (with possible partial updates)

Allows partial update, not breaking whole batch if single job fails and returns list of errors

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_patch_batch_dto import JobPartPatchBatchDto
from phrasetms_client.models.job_part_patch_result_dto import JobPartPatchResultDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    body = phrasetms_client.JobPartPatchBatchDto() # JobPartPatchBatchDto |  (optional)

    try:
        # Edit jobs (with possible partial updates)
        api_response = api_instance.patch_update_job_parts(body=body)
        print("The response of JobApi->patch_update_job_parts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->patch_update_job_parts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobPartPatchBatchDto**](JobPartPatchBatchDto.md)|  | [optional] 

### Return type

[**JobPartPatchResultDto**](JobPartPatchResultDto.md)

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

# **preview_urls**
> PreviewUrlsDto preview_urls(project_uid, job_uid, workflow_level=workflow_level)

Get PDF preview

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.preview_urls_dto import PreviewUrlsDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    workflow_level = 1 # int |  (optional) (default to 1)

    try:
        # Get PDF preview
        api_response = api_instance.preview_urls(project_uid, job_uid, workflow_level=workflow_level)
        print("The response of JobApi->preview_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->preview_urls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **workflow_level** | **int**|  | [optional] [default to 1]

### Return type

[**PreviewUrlsDto**](PreviewUrlsDto.md)

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

# **pseudo_translate1**
> pseudo_translate1(project_uid, body=body)

Pseudo-translate job

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.pseudo_translate_wrapper_dto import PseudoTranslateWrapperDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.PseudoTranslateWrapperDto() # PseudoTranslateWrapperDto |  (optional)

    try:
        # Pseudo-translate job
        api_instance.pseudo_translate1(project_uid, body=body)
    except Exception as e:
        print("Exception when calling JobApi->pseudo_translate1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**PseudoTranslateWrapperDto**](PseudoTranslateWrapperDto.md)|  | [optional] 

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

# **pseudo_translate_job_part**
> pseudo_translate_job_part(project_uid, job_uid, body=body)

Pseudo-translates job

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.pseudo_translate_action_dto import PseudoTranslateActionDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.PseudoTranslateActionDto() # PseudoTranslateActionDto |  (optional)

    try:
        # Pseudo-translates job
        api_instance.pseudo_translate_job_part(project_uid, job_uid, body=body)
    except Exception as e:
        print("Exception when calling JobApi->pseudo_translate_job_part: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**PseudoTranslateActionDto**](PseudoTranslateActionDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **search_by_job3**
> SearchResponseListTmDtoV3 search_by_job3(project_uid, job_uid, body=body)

Search job's translation memories

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.search_response_list_tm_dto_v3 import SearchResponseListTmDtoV3
from phrasetms_client.models.search_tmby_job_request_dto_v3 import SearchTMByJobRequestDtoV3
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.SearchTMByJobRequestDtoV3() # SearchTMByJobRequestDtoV3 |  (optional)

    try:
        # Search job's translation memories
        api_response = api_instance.search_by_job3(project_uid, job_uid, body=body)
        print("The response of JobApi->search_by_job3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->search_by_job3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**SearchTMByJobRequestDtoV3**](SearchTMByJobRequestDtoV3.md)|  | [optional] 

### Return type

[**SearchResponseListTmDtoV3**](SearchResponseListTmDtoV3.md)

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

# **search_parts_in_project**
> SearchJobsDto search_parts_in_project(project_uid, body=body)

Search jobs in project

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.search_jobs_dto import SearchJobsDto
from phrasetms_client.models.search_jobs_request_dto import SearchJobsRequestDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.SearchJobsRequestDto() # SearchJobsRequestDto |  (optional)

    try:
        # Search jobs in project
        api_response = api_instance.search_parts_in_project(project_uid, body=body)
        print("The response of JobApi->search_parts_in_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->search_parts_in_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SearchJobsRequestDto**](SearchJobsRequestDto.md)|  | [optional] 

### Return type

[**SearchJobsDto**](SearchJobsDto.md)

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

# **search_segment_by_job**
> SearchResponseListTmDto search_segment_by_job(project_uid, job_uid, body=body)

Search translation memory for segment by job

Returns at most <i>maxSegments</i>             records with <i>score >= scoreThreshold</i> and at most <i>maxSubsegments</i> records which are subsegment,             i.e. the source text is substring of the query text.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.search_response_list_tm_dto import SearchResponseListTmDto
from phrasetms_client.models.search_tmby_job_request_dto import SearchTMByJobRequestDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.SearchTMByJobRequestDto() # SearchTMByJobRequestDto |  (optional)

    try:
        # Search translation memory for segment by job
        api_response = api_instance.search_segment_by_job(project_uid, job_uid, body=body)
        print("The response of JobApi->search_segment_by_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->search_segment_by_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**SearchTMByJobRequestDto**](SearchTMByJobRequestDto.md)|  | [optional] 

### Return type

[**SearchResponseListTmDto**](SearchResponseListTmDto.md)

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

# **search_terms_by_job1**
> SearchTbResponseListDto search_terms_by_job1(job_uid, project_uid, body=body)

Search job's term bases

Search all read term bases assigned to the job

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.search_tb_by_job_request_dto import SearchTbByJobRequestDto
from phrasetms_client.models.search_tb_response_list_dto import SearchTbResponseListDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    job_uid = 'job_uid_example' # str | 
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.SearchTbByJobRequestDto() # SearchTbByJobRequestDto |  (optional)

    try:
        # Search job's term bases
        api_response = api_instance.search_terms_by_job1(job_uid, project_uid, body=body)
        print("The response of JobApi->search_terms_by_job1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->search_terms_by_job1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **project_uid** | **str**|  | 
 **body** | [**SearchTbByJobRequestDto**](SearchTbByJobRequestDto.md)|  | [optional] 

### Return type

[**SearchTbResponseListDto**](SearchTbResponseListDto.md)

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

# **search_terms_in_text_by_job_v2**
> SearchInTextResponseList2Dto search_terms_in_text_by_job_v2(job_uid, project_uid, body=body)

Search terms in text

Search in text in all read term bases assigned to the job

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.search_in_text_response_list2_dto import SearchInTextResponseList2Dto
from phrasetms_client.models.search_tb_in_text_by_job_request_dto import SearchTbInTextByJobRequestDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    job_uid = 'job_uid_example' # str | 
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.SearchTbInTextByJobRequestDto() # SearchTbInTextByJobRequestDto |  (optional)

    try:
        # Search terms in text
        api_response = api_instance.search_terms_in_text_by_job_v2(job_uid, project_uid, body=body)
        print("The response of JobApi->search_terms_in_text_by_job_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->search_terms_in_text_by_job_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **project_uid** | **str**|  | 
 **body** | [**SearchTbInTextByJobRequestDto**](SearchTbInTextByJobRequestDto.md)|  | [optional] 

### Return type

[**SearchInTextResponseList2Dto**](SearchInTextResponseList2Dto.md)

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

# **set_status**
> set_status(project_uid, job_uid, body=body)

Edit job status

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_status_change_action_dto import JobStatusChangeActionDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.JobStatusChangeActionDto() # JobStatusChangeActionDto |  (optional)

    try:
        # Edit job status
        api_instance.set_status(project_uid, job_uid, body=body)
    except Exception as e:
        print("Exception when calling JobApi->set_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**JobStatusChangeActionDto**](JobStatusChangeActionDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **split**
> JobPartsDto split(project_uid, job_uid, body=body)

Split job

 Splits job by one of the following methods: * **After specific segments** - fill in `segmentOrdinals` * **Into X parts** - fill in `partCount`  * **Into parts with specific size** - fill in `partSize`. partSize represents segment count in each part. * **Into parts with specific word count** - fill in `wordCount`   * **By document parts** - fill in `byDocumentParts`, works only with **PowerPoint** files   Only one option at a time is allowed.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_parts_dto import JobPartsDto
from phrasetms_client.models.split_job_action_dto import SplitJobActionDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.SplitJobActionDto() # SplitJobActionDto |  (optional)

    try:
        # Split job
        api_response = api_instance.split(project_uid, job_uid, body=body)
        print("The response of JobApi->split:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->split: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**SplitJobActionDto**](SplitJobActionDto.md)|  | [optional] 

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

# **status_changes**
> JobPartStatusChangesDto status_changes(project_uid, job_uid)

Get status changes

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_status_changes_dto import JobPartStatusChangesDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get status changes
        api_response = api_instance.status_changes(project_uid, job_uid)
        print("The response of JobApi->status_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->status_changes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**JobPartStatusChangesDto**](JobPartStatusChangesDto.md)

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

# **update_source**
> JobUpdateSourceResponseDto update_source(project_uid, memsource=memsource, content_disposition=content_disposition, body=body)

Update source

 API updated source file for specified job  Job file can be provided directly in the message body.   Please supply jobs in `Memsource` header.   For file in the request body provide also the filename in `Content-Disposition` header.  If a job from a multilingual file is updated, all jobs from the same file are update too even if their UIDs aren't  listed in the jobs field.  Accepted metadata:     - `jobs` - **required** - list of jobs UID reference (maximum size `100`)   - `preTranslate` - pre translate flag (default `false`)   - `allowAutomaticPostAnalysis` - if automatic post editing analysis should be created. If not specified then value                                     is taken from the analyse settings of the project   - `callbackUrl` - consumer callback  Job restrictions:   - job must belong to project specified in path (`projectUid`)   - job `UID` must be from the first workflow step   - job cannot be split   - job cannot be continuous   - job cannot originate in a connector   - status in any of the job's workflow steps cannot be a final     status (`COMPLETED_BY_LINGUIST`, `COMPLETED`, `CANCELLED`)   - job UIDs must be from the same multilingual file if a multilingual file is updated   - multiple multilingual files or a mixture of multilingual and other jobs cannot be updated in one call  File restrictions:   - file cannot be a `.zip` file  Example:  ``` {   \"jobs\": [     {         \"uid\": \"jobIn1stWfStepAndNonFinalStatusUid\"     }   ],   \"preTranslate\": false,   \"allowAutomaticPostAnalysis\": false   \"callbackUrl\": \"https://my-shiny-service.com/consumeCallback\" } ```  

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_update_source_response_dto import JobUpdateSourceResponseDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    memsource = 'memsource_example' # str |  (optional)
    content_disposition = 'content_disposition_example' # str | must match pattern `((inline|attachment); )?(filename\\*=UTF-8''(.+)|filename=\"?(.+)\"?)` (optional)
    body = None # object |  (optional)

    try:
        # Update source
        api_response = api_instance.update_source(project_uid, memsource=memsource, content_disposition=content_disposition, body=body)
        print("The response of JobApi->update_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->update_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **memsource** | **str**|  | [optional] 
 **content_disposition** | **str**| must match pattern &#x60;((inline|attachment); )?(filename\\*&#x3D;UTF-8&#39;&#39;(.+)|filename&#x3D;\&quot;?(.+)\&quot;?)&#x60; | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**JobUpdateSourceResponseDto**](JobUpdateSourceResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
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

# **update_target**
> JobUpdateSourceResponseDto update_target(project_uid, memsource=memsource, content_disposition=content_disposition, body=body)

Update target

 API update target file for specified job  Job file can be provided directly in the message body.  Please supply jobs in `Memsource` header.  For file in the request body provide also the filename in `Content-Disposition` header.  Accepted metadata:    - `jobs` - **required** - list of jobs UID reference (maximum size `1`)   - `propagateConfirmedToTm` - sets if confirmed segments should be stored in TM (default value: true)   - `callbackUrl` - consumer callback   - `targetSegmentationRule` - ID reference to segmentation rule of organization to use for update target   - `unconfirmChangedSegments` - sets if segments should stay unconfirmed  Job restrictions:   - job must belong to project specified in path (`projectUid`)   - job cannot be split   - job cannot be continuous   - job cannot be multilingual   - job cannot originate in a connector   - job cannot have different file extension than original file  File restrictions:   - file cannot be a `.zip` file   - update target is not allowed for jobs with file extensions: xliff, po, tbx, tmx, ttx, ts  Example:  ``` {   \"jobs\": [     {         \"uid\": \"jobUid\"     }   ],   \"propagateConfirmedToTm\": true,   \"targetSegmentationRule\": {         \"id\": \"1\"    },   \"callbackUrl\": \"https://my-shiny-service.com/consumeCallback\" } ```  

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_update_source_response_dto import JobUpdateSourceResponseDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    memsource = 'memsource_example' # str |  (optional)
    content_disposition = 'content_disposition_example' # str | must match pattern `((inline|attachment); )?(filename\\*=UTF-8''(.+)|filename=\"?(.+)\"?)` (optional)
    body = None # object |  (optional)

    try:
        # Update target
        api_response = api_instance.update_target(project_uid, memsource=memsource, content_disposition=content_disposition, body=body)
        print("The response of JobApi->update_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->update_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **memsource** | **str**|  | [optional] 
 **content_disposition** | **str**| must match pattern &#x60;((inline|attachment); )?(filename\\*&#x3D;UTF-8&#39;&#39;(.+)|filename&#x3D;\&quot;?(.+)\&quot;?)&#x60; | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**JobUpdateSourceResponseDto**](JobUpdateSourceResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Updated |  -  |
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

# **upload_bilingual_file**
> JobPartsDto upload_bilingual_file(format=format, save_to_trans_memory=save_to_trans_memory, set_completed=set_completed, body=body)

Upload bilingual file

Returns updated job parts

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
    api_instance = phrasetms_client.JobApi(api_client)
    format = 'MXLF' # str |  (optional) (default to 'MXLF')
    save_to_trans_memory = 'Confirmed' # str |  (optional) (default to 'Confirmed')
    set_completed = False # bool |  (optional) (default to False)
    body = None # object |  (optional)

    try:
        # Upload bilingual file
        api_response = api_instance.upload_bilingual_file(format=format, save_to_trans_memory=save_to_trans_memory, set_completed=set_completed, body=body)
        print("The response of JobApi->upload_bilingual_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->upload_bilingual_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] [default to &#39;MXLF&#39;]
 **save_to_trans_memory** | **str**|  | [optional] [default to &#39;Confirmed&#39;]
 **set_completed** | **bool**|  | [optional] [default to False]
 **body** | **object**|  | [optional] 

### Return type

[**JobPartsDto**](JobPartsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
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

# **upload_handover_file**
> FileHandoverDto upload_handover_file(project_uid, memsource, content_disposition, content_length=content_length, body=body)

Upload handover file

 For following jobs the handover file is not supported: * Continuous jobs * Jobs from connectors * Split jobs * Multilingual jobs 

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.file_handover_dto import FileHandoverDto
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    memsource = '{\"jobs\":[{\"uid\":\"8kMckeDcgWWF4Fe4Szqjb1\"}]}' # str | 
    content_disposition = 'content_disposition_example' # str | must match pattern `((inline|attachment); )?(filename\\*=UTF-8''(.+)|filename=\"?(.+)\"?)`
    content_length = 56 # int |  (optional)
    body = None # object |  (optional)

    try:
        # Upload handover file
        api_response = api_instance.upload_handover_file(project_uid, memsource, content_disposition, content_length=content_length, body=body)
        print("The response of JobApi->upload_handover_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->upload_handover_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **memsource** | **str**|  | 
 **content_disposition** | **str**| must match pattern &#x60;((inline|attachment); )?(filename\\*&#x3D;UTF-8&#39;&#39;(.+)|filename&#x3D;\&quot;?(.+)\&quot;?)&#x60; | 
 **content_length** | **int**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**FileHandoverDto**](FileHandoverDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
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

# **web_editor_link_v2**
> WebEditorLinkDtoV2 web_editor_link_v2(project_uid, body=body)

Get Web Editor URL

 Possible warning codes are:   - `NOT_ACCEPTED_BY_LINGUIST` - Job is not accepted by linguist   - `NOT_ASSIGNED_TO_LINGUIST` - Job is not assigned to linguist   - `PDF` - One of requested jobs is PDF   - `PREVIOUS_WORKFLOW_NOT_COMPLETED` - Previous workflow step is not completed   - `PREVIOUS_WORKFLOW_NOT_COMPLETED_STRICT` - Previous workflow step is not completed and project has strictWorkflowFinish set to true   - `IN_DELIVERED_STATE` - Jobs in DELIVERED state   - `IN_COMPLETED_STATE` - Jobs in COMPLETED state   - `IN_REJECTED_STATE` - Jobs in REJECTED state  Possible error codes are:   - `ASSIGNED_TO_OTHER_USER` - Job is accepted by other user   - `NOT_UNIQUE_TARGET_LANG` - Requested jobs contains different target locales   - `TOO_MANY_SEGMENTS` - Count of requested job's segments is higher than **40000**   - `TOO_MANY_JOBS` - Count of requested jobs is higher than **290**   - `COMPLETED_JOINED_WITH_OTHER` - Jobs in COMPLETED state cannot be joined with jobs in other states   - `DELIVERED_JOINED_WITH_OTHER` - Jobs in DELIVERED state cannot be joined with jobs in other states   - `REJECTED_JOINED_WITH_OTHER` - Jobs in REJECTED state cannot be joined with jobs in other states  Warning response example: ``` {     \"warnings\": [         {             \"message\": \"Not accepted by linguist\",             \"args\": {                 \"jobs\": [                     \"abcd1234\"                 ]             },             \"code\": \"NOT_ACCEPTED_BY_LINGUIST\"         },         {             \"message\": \"Previous workflow step not completed\",             \"args\": {                 \"jobs\": [                     \"abcd1234\"                 ]             },             \"code\": \"PREVIOUS_WORKFLOW_NOT_COMPLETED\"         }     ],     \"url\": \"/web/job/abcd1234-efgh5678/translate\" } ```  Error response example: Status: `400 Bad Request` ``` {     \"errorCode\": \"NOT_UNIQUE_TARGET_LANG\",     \"errorDescription\": \"Only files with identical target languages can be joined\",     \"errorDetails\": [         {             \"code\": \"NOT_UNIQUE_TARGET_LANG\",             \"args\": {                 \"targetLocales\": [                     \"de\",                     \"en\"                 ]             },             \"message\": \"Only files with identical target languages can be joined\"         },         {             \"code\": \"TOO_MANY_SEGMENTS\",             \"args\": {                 \"maxSegments\": 40000,                 \"segments\": 400009             },             \"message\": \"Up to 40000 segments can be opened in the Memsource Web Editor, job has 400009 segments\"         }     ] } ``` 

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.create_web_editor_link_dto_v2 import CreateWebEditorLinkDtoV2
from phrasetms_client.models.web_editor_link_dto_v2 import WebEditorLinkDtoV2
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.CreateWebEditorLinkDtoV2() # CreateWebEditorLinkDtoV2 |  (optional)

    try:
        # Get Web Editor URL
        api_response = api_instance.web_editor_link_v2(project_uid, body=body)
        print("The response of JobApi->web_editor_link_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->web_editor_link_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**CreateWebEditorLinkDtoV2**](CreateWebEditorLinkDtoV2.md)|  | [optional] 

### Return type

[**WebEditorLinkDtoV2**](WebEditorLinkDtoV2.md)

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

# **wild_card_search_by_job3**
> SearchResponseListTmDtoV3 wild_card_search_by_job3(project_uid, job_uid, body=body)

Wildcard search job's translation memories

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.search_response_list_tm_dto_v3 import SearchResponseListTmDtoV3
from phrasetms_client.models.wild_card_search_by_job_request_dto_v3 import WildCardSearchByJobRequestDtoV3
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
    api_instance = phrasetms_client.JobApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.WildCardSearchByJobRequestDtoV3() # WildCardSearchByJobRequestDtoV3 |  (optional)

    try:
        # Wildcard search job's translation memories
        api_response = api_instance.wild_card_search_by_job3(project_uid, job_uid, body=body)
        print("The response of JobApi->wild_card_search_by_job3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->wild_card_search_by_job3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**WildCardSearchByJobRequestDtoV3**](WildCardSearchByJobRequestDtoV3.md)|  | [optional] 

### Return type

[**SearchResponseListTmDtoV3**](SearchResponseListTmDtoV3.md)

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

