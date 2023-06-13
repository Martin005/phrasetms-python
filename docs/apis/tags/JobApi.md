<a id="__pageTop"></a>

# phrasetms_client.apis.tags.job_api.JobApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                                          | HTTP request                                                                             | Description                                          |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| [**compare_part**](#compare_part)                                               | **post** /api2/v1/projects/{projectUid}/jobs/compare                                     | Compare jobs on workflow levels                      |
| [**completed_file1**](#completed_file1)                                         | **put** /api2/v2/projects/{projectUid}/jobs/{jobUid}/targetFile                          | Download target file (async)                         |
| [**copy_source_to_target**](#copy_source_to_target)                             | **post** /api2/v1/projects/{projectUid}/jobs/copySourceToTarget                          | Copy Source to Target                                |
| [**copy_source_to_target_job_part**](#copy_source_to_target_job_part)           | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/copySourceToTarget                 | Copy Source to Target job                            |
| [**create_job**](#create_job)                                                   | **post** /api2/v1/projects/{projectUid}/jobs                                             | Create job                                           |
| [**create_job_from_async_download_task**](#create_job_from_async_download_task) | **post** /api2/v1/projects/{projectUid}/jobs/connectorTask                               | Create job from connector asynchronous download task |
| [**create_term_by_job**](#create_term_by_job)                                   | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/termBases/createByJob              | Create term in job&#x27;s term bases                 |
| [**delete_all_translations**](#delete_all_translations)                         | **delete** /api2/v1/projects/{projectUid}/jobs/translations                              | Delete all translations                              |
| [**delete_all_translations1**](#delete_all_translations1)                       | **delete** /api2/v2/projects/{projectUid}/jobs/translations                              | Delete specific translations                         |
| [**delete_handover_file**](#delete_handover_file)                               | **delete** /api2/v1/projects/{projectUid}/fileHandovers                                  | Delete handover file                                 |
| [**delete_parts**](#delete_parts)                                               | **delete** /api2/v1/projects/{projectUid}/jobs/batch                                     | Delete job (batch)                                   |
| [**download_completed_file**](#download_completed_file)                         | **get** /api2/v2/projects/{projectUid}/jobs/{jobUid}/downloadTargetFile/{asyncRequestId} | Download target file based on async request          |
| [**edit_job_import_settings**](#edit_job_import_settings)                       | **put** /api2/v1/projects/{projectUid}/jobs/{jobUid}/importSettings                      | Edit job import settings                             |
| [**edit_part**](#edit_part)                                                     | **put** /api2/v1/projects/{projectUid}/jobs/{jobUid}                                     | Edit job                                             |
| [**edit_parts**](#edit_parts)                                                   | **put** /api2/v1/projects/{projectUid}/jobs/batch                                        | Edit jobs (batch)                                    |
| [**export_to_online_repository**](#export_to_online_repository)                 | **post** /api2/v3/projects/{projectUid}/jobs/export                                      | Export jobs to online repository                     |
| [**file_preview**](#file_preview)                                               | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/preview                            | Download preview file                                |
| [**file_preview_job**](#file_preview_job)                                       | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/preview                             | Download preview file                                |
| [**get_bilingual_file**](#get_bilingual_file)                                   | **post** /api2/v1/projects/{projectUid}/jobs/bilingualFile                               | Download bilingual file                              |
| [**get_completed_file_warnings**](#get_completed_file_warnings)                 | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/targetFileWarnings                  | Get target file&#x27;s warnings                      |
| [**get_handover_files**](#get_handover_files)                                   | **get** /api2/v1/projects/{projectUid}/fileHandovers                                     | Download handover file(s)                            |
| [**get_import_settings3**](#get_import_settings3)                               | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/importSettings                      | Get import settings for job                          |
| [**get_original_file**](#get_original_file)                                     | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/original                            | Download original file                               |
| [**get_part**](#get_part)                                                       | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}                                     | Get job                                              |
| [**get_parts_workflow_step**](#get_parts_workflow_step)                         | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/workflowStep                        | Get job&#x27;s workflowStep                          |
| [**get_segments_count**](#get_segments_count)                                   | **post** /api2/v1/projects/{projectUid}/jobs/segmentsCount                               | Get segments count                                   |
| [**get_translation_resources**](#get_translation_resources)                     | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources                | Get translation resources                            |
| [**list_part_analyse_v3**](#list_part_analyse_v3)                               | **get** /api2/v3/projects/{projectUid}/jobs/{jobUid}/analyses                            | List analyses                                        |
| [**list_parts_v2**](#list_parts_v2)                                             | **get** /api2/v2/projects/{projectUid}/jobs                                              | List jobs                                            |
| [**list_providers4**](#list_providers4)                                         | **post** /api2/v2/projects/{projectUid}/jobs/{jobUid}/providers/suggest                  | Get suggested providers                              |
| [**list_segments**](#list_segments)                                             | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/segments                            | Get segments                                         |
| [**notify_assigned**](#notify_assigned)                                         | **post** /api2/v1/projects/{projectUid}/jobs/notifyAssigned                              | Notify assigned users                                |
| [**patch_part**](#patch_part)                                                   | **patch** /api2/v1/projects/{projectUid}/jobs/{jobUid}                                   | Patch job                                            |
| [**patch_update_job_parts**](#patch_update_job_parts)                           | **patch** /api2/v3/jobs                                                                  | Edit jobs (with possible partial updates)            |
| [**preview_urls**](#preview_urls)                                               | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/previewUrl                          | Get PDF preview                                      |
| [**pseudo_translate1**](#pseudo_translate1)                                     | **post** /api2/v2/projects/{projectUid}/jobs/pseudoTranslate                             | Pseudo-translate job                                 |
| [**pseudo_translate_job_part**](#pseudo_translate_job_part)                     | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/pseudoTranslate                    | Pseudo-translates job                                |
| [**search_by_job3**](#search_by_job3)                                           | **post** /api2/v3/projects/{projectUid}/jobs/{jobUid}/transMemories/search               | Search job&#x27;s translation memories               |
| [**search_parts_in_project**](#search_parts_in_project)                         | **post** /api2/v1/projects/{projectUid}/jobs/search                                      | Search jobs in project                               |
| [**search_segment_by_job**](#search_segment_by_job)                             | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/transMemories/searchSegment        | Search translation memory for segment by job         |
| [**search_terms_by_job1**](#search_terms_by_job1)                               | **post** /api2/v2/projects/{projectUid}/jobs/{jobUid}/termBases/searchByJob              | Search job&#x27;s term bases                         |
| [**search_terms_in_text_by_job_v2**](#search_terms_in_text_by_job_v2)           | **post** /api2/v2/projects/{projectUid}/jobs/{jobUid}/termBases/searchInTextByJob        | Search terms in text                                 |
| [**set_status**](#set_status)                                                   | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/setStatus                          | Edit job status                                      |
| [**split**](#split)                                                             | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/split                              | Split job                                            |
| [**status_changes**](#status_changes)                                           | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/statusChanges                       | Get status changes                                   |
| [**update_source**](#update_source)                                             | **post** /api2/v1/projects/{projectUid}/jobs/source                                      | Update source                                        |
| [**update_target**](#update_target)                                             | **post** /api2/v1/projects/{projectUid}/jobs/target                                      | Update target                                        |
| [**upload_bilingual_file**](#upload_bilingual_file)                             | **put** /api2/v1/bilingualFiles                                                          | Upload bilingual file                                |
| [**upload_handover_file**](#upload_handover_file)                               | **put** /api2/v1/projects/{projectUid}/fileHandovers                                     | Upload handover file                                 |
| [**web_editor_link_v2**](#web_editor_link_v2)                                   | **post** /api2/v2/projects/{projectUid}/jobs/webEditor                                   | Get Web Editor URL                                   |
| [**wild_card_search_by_job3**](#wild_card_search_by_job3)                       | **post** /api2/v3/projects/{projectUid}/jobs/{jobUid}/transMemories/wildCardSearch       | Wildcard search job&#x27;s translation memories      |

# **compare_part**

<a id="compare_part"></a>

> ComparedSegmentsDto compare_part(project_uid)

Compare jobs on workflow levels

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_ready_references import JobPartReadyReferences
from phrasetms_client.model.compared_segments_dto import ComparedSegmentsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Compare jobs on workflow levels
        api_response = api_instance.compare_part(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->compare_part: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'atWorkflowLevel': 1,
        'withWorkflowLevel': 1,
    }
    body = JobPartReadyReferences(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        get_parts=dict(),
    )
    try:
        # Compare jobs on workflow levels
        api_response = api_instance.compare_part(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->compare_part: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| query_params         | RequestQueryParams                                       |                                         |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**JobPartReadyReferences**](../../models/JobPartReadyReferences.md) |             |

### query_params

#### RequestQueryParams

| Name              | Type                    | Description | Notes    |
| ----------------- | ----------------------- | ----------- | -------- |
| atWorkflowLevel   | AtWorkflowLevelSchema   |             | optional |
| withWorkflowLevel | WithWorkflowLevelSchema |             | optional |

# AtWorkflowLevelSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 1value must be a 32 bit integer |

# WithWorkflowLevelSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 1value must be a 32 bit integer |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#compare_part.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#compare_part.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#compare_part.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#compare_part.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#compare_part.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#compare_part.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#compare_part.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#compare_part.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#compare_part.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#compare_part.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#compare_part.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#compare_part.ApiResponseFor501) | Not implemented                                             |

#### compare_part.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**ComparedSegmentsDto**](../../models/ComparedSegmentsDto.md) |             |

#### compare_part.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_part.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_part.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_part.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_part.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_part.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_part.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_part.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_part.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_part.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_part.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **completed_file1**

<a id="completed_file1"></a>

> completed_file1(project_uidjob_uid)

Download target file (async)

     This call will create async request for downloading target file with translation that can be downloaded when     finished. This means even for other jobs that were created via 'split jobs' etc.

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Download target file (async)
        api_response = api_instance.completed_file1(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->completed_file1: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 400  | [ApiResponseFor400](#completed_file1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#completed_file1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#completed_file1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#completed_file1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#completed_file1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#completed_file1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#completed_file1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#completed_file1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#completed_file1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#completed_file1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#completed_file1.ApiResponseFor501) | Not implemented                                             |

#### completed_file1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### completed_file1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### completed_file1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### completed_file1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### completed_file1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### completed_file1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### completed_file1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### completed_file1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### completed_file1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### completed_file1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### completed_file1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **copy_source_to_target**

<a id="copy_source_to_target"></a>

> copy_source_to_target(project_uid)

Copy Source to Target

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_ready_references import JobPartReadyReferences
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Copy Source to Target
        api_response = api_instance.copy_source_to_target(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->copy_source_to_target: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = JobPartReadyReferences(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        get_parts=dict(),
    )
    try:
        # Copy Source to Target
        api_response = api_instance.copy_source_to_target(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->copy_source_to_target: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**JobPartReadyReferences**](../../models/JobPartReadyReferences.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                         | Description                                                 |
| ---- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                  | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#copy_source_to_target.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#copy_source_to_target.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#copy_source_to_target.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#copy_source_to_target.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#copy_source_to_target.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#copy_source_to_target.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#copy_source_to_target.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#copy_source_to_target.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#copy_source_to_target.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#copy_source_to_target.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#copy_source_to_target.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#copy_source_to_target.ApiResponseFor501) | Not implemented                                             |

#### copy_source_to_target.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **copy_source_to_target_job_part**

<a id="copy_source_to_target_job_part"></a>

> copy_source_to_target_job_part(project_uidjob_uid)

Copy Source to Target job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Copy Source to Target job
        api_response = api_instance.copy_source_to_target_job_part(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->copy_source_to_target_job_part: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                                  | Description                                                 |
| ---- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                           | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#copy_source_to_target_job_part.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#copy_source_to_target_job_part.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#copy_source_to_target_job_part.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#copy_source_to_target_job_part.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#copy_source_to_target_job_part.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#copy_source_to_target_job_part.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#copy_source_to_target_job_part.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#copy_source_to_target_job_part.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#copy_source_to_target_job_part.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#copy_source_to_target_job_part.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#copy_source_to_target_job_part.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#copy_source_to_target_job_part.ApiResponseFor501) | Not implemented                                             |

#### copy_source_to_target_job_part.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### copy_source_to_target_job_part.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_job**

<a id="create_job"></a>

> JobListDto create_job(project_uid)

Create job

Job file can be provided directly in the message body or downloaded from connector. Please supply job metadata in `Memsource` header. For file in the request body provide also the filename in `Content-Disposition` header. Accepted metadata: - `targetLangs` - **required** - `due` - ISO 8601 - `workflowSettings` - project with workflow - see examples bellow - `assignments` - project without workflows - see examples bellow - `importSettings` - re-usable import settings - see [Create import settings](#operation/createImportSettings) - `useProjectFileImportSettings` - mutually exclusive with importSettings - `callbackUrl` - consumer callback - `path` - original destination directory - `preTranslate` - set pre translate job after import for remote file jobs also `remoteFile` - see examples bellow: - `connectorToken` - remote connector token - `remoteFolder` - `remoteFileName` - `continuous` - true for continuous job Create and assign job in project without workflow step: ` {   \"targetLangs\": [     \"cs_cz\"   ],   \"callbackUrl\": \"https://my-shiny-service.com/consumeCallback\",   \"importSettings\": {     \"uid\": \"abcd123\"   },   \"due\": \"2007-12-03T10:15:30.00Z\",   \"path\": \"destination directory\",   \"assignments\": [     {       \"targetLang\": \"cs_cz\",       \"providers\": [         {           \"id\": \"4321\",           \"type\": \"USER\"         }       ]     }   ],   \"notifyProvider\": {     \"organizationEmailTemplate\": {       \"id\": \"39\"     },     \"notificationIntervalInMinutes\": \"10\"   } }` Create job from remote file without workflow steps: ` {   \"remoteFile\": {     \"connectorToken\": \"948123ef-e1ef-4cd3-a90e-af1617848af3\",     \"remoteFolder\": \"/\",     \"remoteFileName\": \"Few words.docx\",     \"continuous\": false   },   \"assignments\": [],   \"workflowSettings\": [],   \"targetLangs\": [     \"cs\"   ] }` Create and assign job in project with workflow step: ` {   \"targetLangs\": [     \"de\"   ],   \"useProjectFileImportSettings\": \"true\",   \"workflowSettings\": [     {       \"id\": \"64\",       \"due\": \"2007-12-03T10:15:30.00Z\",       \"assignments\": [         {           \"targetLang\": \"de\",           \"providers\": [             {               \"id\": \"3\",               \"type\": \"VENDOR\"             }           ]         }       ],       \"notifyProvider\": {         \"organizationEmailTemplate\": {           \"id\": \"39\"         },         \"notificationIntervalInMinutes\": \"10\"       }     }   ] }`

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_list_dto import JobListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    header_params = {
    }
    try:
        # Create job
        api_response = api_instance.create_job(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->create_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    header_params = {
        'Memsource': "Memsource_example",
        'Content-Disposition': "Content-Disposition_example",
    }
    body = dict()
    try:
        # Create job
        api_response = api_instance.create_job(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->create_job: %s\n" % e)
```

### Parameters

| Name                 | Type                                                            | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset                      |
| header_params        | RequestHeaderParams                                             |                                                 |
| path_params          | RequestPathParams                                               |                                                 |
| content_type         | str                                                             | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                               | default is ('application/json', )               | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                            | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                            | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### header_params

#### RequestHeaderParams

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Memsource           | MemsourceSchema          |             | optional |
| Content-Disposition | ContentDispositionSchema |             | optional |

# MemsourceSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                              | Description                                                 |
| ---- | -------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization       | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_job.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_job.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_job.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_job.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_job.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_job.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_job.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_job.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_job.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_job.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_job.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_job.ApiResponseFor501) | Not implemented                                             |

#### create_job.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                         | Description | Notes |
| -------------------------------------------- | ----------- | ----- |
| [**JobListDto**](../../models/JobListDto.md) |             |

#### create_job.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_job_from_async_download_task**

<a id="create_job_from_async_download_task"></a>

> JobListDto create_job_from_async_download_task(project_uid)

Create job from connector asynchronous download task

Creates the job in project specified by path param projectUid. Source file is defined by downloadTaskId parameter. That is value of finished download async task [Connector - Download file (async)](#operation/getFile_1). Please supply job metadata in body. Accepted metadata: - `targetLangs` - **required** - `due` - ISO 8601 - `workflowSettings` - project with workflow - see examples bellow - `assignments` - project without workflows - see examples bellow - `importSettings` - re-usable import settings - see [Create import settings](#operation/createImportSettings) - `useProjectFileImportSettings` - mutually exclusive with importSettings - `callbackUrl` - consumer callback - `path` - original destination directory - `preTranslate` - set pre translate job after import Create job simple (without workflow steps, without assignments): `{   \"targetLangs\": [     \"cs_cz\",     \"es_es\"   ] }` Create and assign job in project without workflow step: `{   \"targetLangs\": [     \"cs_cz\"   ],   \"callbackUrl\": \"https://my-shiny-service.com/consumeCallback\",   \"importSettings\": {     \"uid\": \"abcd123\"   },   \"due\": \"2007-12-03T10:15:30.00Z\",   \"path\": \"destination directory\",   \"assignments\": [     {       \"targetLang\": \"cs_cz\",       \"providers\": [         {           \"id\": \"4321\",           \"type\": \"USER\"         }       ]     }   ],   \"notifyProvider\": {     \"organizationEmailTemplate\": {       \"id\": \"39\"     },     \"notificationIntervalInMinutes\": \"10\"   } }` Create and assign job in project with workflow step: `{   \"targetLangs\": [     \"de\"   ],   \"useProjectFileImportSettings\": \"true\",   \"workflowSettings\": [     {       \"id\": \"64\",       \"due\": \"2007-12-03T10:15:30.00Z\",       \"assignments\": [         {           \"targetLang\": \"de\",           \"providers\": [             {               \"id\": \"3\",               \"type\": \"VENDOR\"             }           ]         }       ],       \"notifyProvider\": {         \"organizationEmailTemplate\": {           \"id\": \"39\"         },         \"notificationIntervalInMinutes\": \"10\"       }     }   ] }`

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_create_request_dto import JobCreateRequestDto
from phrasetms_client.model.job_list_dto import JobListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Create job from connector asynchronous download task
        api_response = api_instance.create_job_from_async_download_task(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->create_job_from_async_download_task: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'downloadTaskId': "downloadTaskId_example",
        'continuous': False,
    }
    body = JobCreateRequestDto(
        target_langs=[
            "target_langs_example"
        ],
        due="1970-01-01T00:00:00.00Z",
        workflow_settings=[
            WorkflowStepConfiguration(
                id="id_example",
                assignments=[
                    ProvidersPerLanguage(
                        target_lang="target_lang_example",
                        providers=[
                            ProviderReference()
                        ],
                        assigned_users=[
                            User(
                                id=1,
                            )
                        ],
                    )
                ],
                due="1970-01-01T00:00:00.00Z",
                notify_provider=NotifyProviderDto(
                    organization_email_template=IdReference(
                        id="id_example",
                    ),
                    notification_interval_in_minutes=0,
                ),
            )
        ],
        assignments=[
            ProvidersPerLanguage()
        ],
        import_settings=UidReference(
            uid="uid_example",
        ),
        use_project_file_import_settings=True,
        pre_translate=True,
        notify_provider=NotifyProviderDto(),
        callback_url="callback_url_example",
        path="path_example",
        remote_file=JobCreateRemoteFileDto(
            connector_token="connector_token_example",
            remote_folder="remote_folder_example",
            remote_file_name="remote_file_name_example",
            remote_file_name_regex=True,
            continuous=True,
        ),
    )
    try:
        # Create job from connector asynchronous download task
        api_response = api_instance.create_job_from_async_download_task(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->create_job_from_async_download_task: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| query_params         | RequestQueryParams                                       |                                         |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**JobCreateRequestDto**](../../models/JobCreateRequestDto.md) |             |

### query_params

#### RequestQueryParams

| Name           | Type                 | Description | Notes    |
| -------------- | -------------------- | ----------- | -------- |
| downloadTaskId | DownloadTaskIdSchema |             | optional |
| continuous     | ContinuousSchema     |             | optional |

# DownloadTaskIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ContinuousSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                                       | Description                                                 |
| ---- | --------------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_job_from_async_download_task.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_job_from_async_download_task.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_job_from_async_download_task.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_job_from_async_download_task.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_job_from_async_download_task.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_job_from_async_download_task.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_job_from_async_download_task.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_job_from_async_download_task.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_job_from_async_download_task.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_job_from_async_download_task.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_job_from_async_download_task.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_job_from_async_download_task.ApiResponseFor501) | Not implemented                                             |

#### create_job_from_async_download_task.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                         | Description | Notes |
| -------------------------------------------- | ----------- | ----- |
| [**JobListDto**](../../models/JobListDto.md) |             |

#### create_job_from_async_download_task.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job_from_async_download_task.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job_from_async_download_task.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job_from_async_download_task.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job_from_async_download_task.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job_from_async_download_task.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job_from_async_download_task.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job_from_async_download_task.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job_from_async_download_task.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job_from_async_download_task.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_job_from_async_download_task.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_term_by_job**

<a id="create_term_by_job"></a>

> TermPairDto create_term_by_job(job_uidproject_uid)

Create term in job's term bases

Create new term in the write term base assigned to the job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.create_terms_dto import CreateTermsDto
from phrasetms_client.model.term_pair_dto import TermPairDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'projectUid': "projectUid_example",
    }
    try:
        # Create term in job's term bases
        api_response = api_instance.create_term_by_job(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->create_term_by_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
        'projectUid': "projectUid_example",
    }
    body = CreateTermsDto(
        source_term=TermCreateByJobDto(
            text="text_example",
            case_sensitive=True,
            exact_match=True,
            forbidden=True,
            preferred=True,
            usage="usage_example",
            note="note_example",
            short_translation="short_translation_example",
            term_type="FULL_FORM",
            part_of_speech="ADJECTIVE",
            gender="MASCULINE",
            number="SINGULAR",
        ),
,
    )
    try:
        # Create term in job's term bases
        api_response = api_instance.create_term_by_job(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->create_term_by_job: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                 | Description | Notes |
| ---------------------------------------------------- | ----------- | ----- |
| [**CreateTermsDto**](../../models/CreateTermsDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| jobUid     | JobUidSchema     |             |
| projectUid | ProjectUidSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#create_term_by_job.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#create_term_by_job.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_term_by_job.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_term_by_job.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_term_by_job.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_term_by_job.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_term_by_job.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_term_by_job.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_term_by_job.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_term_by_job.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_term_by_job.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_term_by_job.ApiResponseFor501) | Not implemented                                             |

#### create_term_by_job.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**TermPairDto**](../../models/TermPairDto.md) |             |

#### create_term_by_job.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_term_by_job.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_term_by_job.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_term_by_job.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_term_by_job.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_term_by_job.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_term_by_job.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_term_by_job.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_term_by_job.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_term_by_job.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_term_by_job.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_all_translations**

<a id="delete_all_translations"></a>

> delete_all_translations(project_uid)

Delete all translations

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_ready_references import JobPartReadyReferences
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Delete all translations
        api_response = api_instance.delete_all_translations(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->delete_all_translations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = JobPartReadyReferences(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        get_parts=dict(),
    )
    try:
        # Delete all translations
        api_response = api_instance.delete_all_translations(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->delete_all_translations: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**JobPartReadyReferences**](../../models/JobPartReadyReferences.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                           | Description                                                 |
| ---- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                    | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_all_translations.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_all_translations.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_all_translations.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_all_translations.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_all_translations.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_all_translations.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_all_translations.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_all_translations.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_all_translations.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_all_translations.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_all_translations.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_all_translations.ApiResponseFor501) | Not implemented                                             |

#### delete_all_translations.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_all_translations1**

<a id="delete_all_translations1"></a>

> delete_all_translations1(project_uid)

Delete specific translations

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_ready_delete_translation_dto import JobPartReadyDeleteTranslationDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Delete specific translations
        api_response = api_instance.delete_all_translations1(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->delete_all_translations1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = JobPartReadyDeleteTranslationDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        delete_settings=TranslationSegmentsReferenceV2(
            confirmed=True,
            locked=True,
        ),
        for_all_jobs=True,
        workflow_level=1,
        filter=JobPartReadyDeleteTranslationFilterDto(
            filename="filename_example",
            statuses=[
                "statuses_example"
            ],
            target_lang="target_lang_example",
            provider=ProviderReference(),
            owner=UidReference(),
            date_due="1970-01-01T00:00:00.00Z",
            due_in_hours=1,
            overdue=True,
        ),
        get_parts=dict(),
    )
    try:
        # Delete specific translations
        api_response = api_instance.delete_all_translations1(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->delete_all_translations1: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBody, Unset]        | optional, default is unset |
| path_params          | RequestPathParams                                |                            |
| content_type         | str                                              | optional, default is '_/_' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                             | default is False           | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None            | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False           | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBody

| Type                                                                                     | Description | Notes |
| ---------------------------------------------------------------------------------------- | ----------- | ----- |
| [**JobPartReadyDeleteTranslationDto**](../../models/JobPartReadyDeleteTranslationDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                            | Description                                                 |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                     | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_all_translations1.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_all_translations1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_all_translations1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_all_translations1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_all_translations1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_all_translations1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_all_translations1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_all_translations1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_all_translations1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_all_translations1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_all_translations1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_all_translations1.ApiResponseFor501) | Not implemented                                             |

#### delete_all_translations1.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_all_translations1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_handover_file**

<a id="delete_handover_file"></a>

> delete_handover_file(project_uid)

Delete handover file

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_references import JobPartReferences
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Delete handover file
        api_response = api_instance.delete_handover_file(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->delete_handover_file: %s\n" % e)

    # example passing only optional values
    path_params = {
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
        # Delete handover file
        api_response = api_instance.delete_handover_file(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->delete_handover_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**JobPartReferences**](../../models/JobPartReferences.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_handover_file.ApiResponseFor204) | Deleted                                                     |
| 400  | [ApiResponseFor400](#delete_handover_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_handover_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_handover_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_handover_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_handover_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_handover_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_handover_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_handover_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_handover_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_handover_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_handover_file.ApiResponseFor501) | Not implemented                                             |

#### delete_handover_file.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_handover_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_parts**

<a id="delete_parts"></a>

> delete_parts(project_uid)

Delete job (batch)

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_delete_references import JobPartDeleteReferences
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Delete job (batch)
        api_response = api_instance.delete_parts(
            path_params=path_params,
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->delete_parts: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'purge': False,
    }
    body = JobPartDeleteReferences(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        get_parts=dict(),
    )
    try:
        # Delete job (batch)
        api_response = api_instance.delete_parts(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->delete_parts: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| query_params         | RequestQueryParams                                       |                                         |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**JobPartDeleteReferences**](../../models/JobPartDeleteReferences.md) |             |

### query_params

#### RequestQueryParams

| Name  | Type        | Description | Notes    |
| ----- | ----------- | ----------- | -------- |
| purge | PurgeSchema |             | optional |

# PurgeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_parts.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_parts.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_parts.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_parts.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_parts.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_parts.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_parts.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_parts.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_parts.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_parts.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_parts.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_parts.ApiResponseFor501) | Not implemented                                             |

#### delete_parts.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_parts.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_completed_file**

<a id="download_completed_file"></a>

> download_completed_file(project_uidjob_uidasync_request_id)

Download target file based on async request

     This call will return target file with translation. This means even for other jobs that were created via     'split jobs' etc.

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
        'asyncRequestId': "asyncRequestId_example",
    }
    query_params = {
    }
    try:
        # Download target file based on async request
        api_response = api_instance.download_completed_file(
            path_params=path_params,
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->download_completed_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
        'asyncRequestId': "asyncRequestId_example",
    }
    query_params = {
        'format': "ORIGINAL",
    }
    try:
        # Download target file based on async request
        api_response = api_instance.download_completed_file(
            path_params=path_params,
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->download_completed_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                  |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name   | Type         | Description | Notes    |
| ------ | ------------ | ----------- | -------- |
| format | FormatSchema |             | optional |

# FormatSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                               |
| ---------- | ------------- | ----------- | --------------------------------------------------------------------------------------------------- |
| str,       | str,          |             | must be one of ["ORIGINAL", "PDF", ] if omitted the server will use the default value of "ORIGINAL" |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| projectUid     | ProjectUidSchema     |             |
| jobUid         | JobUidSchema         |             |
| asyncRequestId | AsyncRequestIdSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# AsyncRequestIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                           | Description                                                 |
| ---- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                    | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#download_completed_file.ApiResponseFor200) | application/octet-stream                                    |
| 400  | [ApiResponseFor400](#download_completed_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#download_completed_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#download_completed_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#download_completed_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#download_completed_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#download_completed_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#download_completed_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#download_completed_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#download_completed_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#download_completed_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#download_completed_file.ApiResponseFor501) | Not implemented                                             |

#### download_completed_file.ApiResponseFor200

| Name     | Type                  | Description  | Notes |
| -------- | --------------------- | ------------ | ----- |
| response | urllib3.HTTPResponse  | Raw response |
| body     | typing.Union[]        |              |
| headers  | ResponseHeadersFor200 |              |

#### ResponseHeadersFor200

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Content-Disposition | ContentDispositionSchema |             | optional |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

#### download_completed_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_completed_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_completed_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_completed_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_completed_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_completed_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_completed_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_completed_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_completed_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_completed_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_completed_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_job_import_settings**

<a id="edit_job_import_settings"></a>

> FileImportSettingsDto edit_job_import_settings(project_uidjob_uid)

Edit job import settings

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.file_import_settings_create_dto import FileImportSettingsCreateDto
from phrasetms_client.model.file_import_settings_dto import FileImportSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Edit job import settings
        api_response = api_instance.edit_job_import_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->edit_job_import_settings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
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
        # Edit job import settings
        api_response = api_instance.edit_job_import_settings(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->edit_job_import_settings: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------ | ----------- | ----- |
| [**FileImportSettingsCreateDto**](../../models/FileImportSettingsCreateDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                            | Description                                                 |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                     | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#edit_job_import_settings.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#edit_job_import_settings.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#edit_job_import_settings.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#edit_job_import_settings.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#edit_job_import_settings.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#edit_job_import_settings.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#edit_job_import_settings.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#edit_job_import_settings.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#edit_job_import_settings.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#edit_job_import_settings.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#edit_job_import_settings.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#edit_job_import_settings.ApiResponseFor501) | Not implemented                                             |

#### edit_job_import_settings.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**FileImportSettingsDto**](../../models/FileImportSettingsDto.md) |             |

#### edit_job_import_settings.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_job_import_settings.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_job_import_settings.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_job_import_settings.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_job_import_settings.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_job_import_settings.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_job_import_settings.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_job_import_settings.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_job_import_settings.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_job_import_settings.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_job_import_settings.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_part**

<a id="edit_part"></a>

> JobPartExtendedDto edit_part(project_uidjob_uid)

Edit job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_extended_dto import JobPartExtendedDto
from phrasetms_client.model.job_part_update_single_dto import JobPartUpdateSingleDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Edit job
        api_response = api_instance.edit_part(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->edit_part: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = JobPartUpdateSingleDto(
        status="NEW",
        date_due="1970-01-01T00:00:00.00Z",
        providers=[
            ProviderReference()
        ],
    )
    try:
        # Edit job
        api_response = api_instance.edit_part(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->edit_part: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**JobPartUpdateSingleDto**](../../models/JobPartUpdateSingleDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                             | Description                                                 |
| ---- | ------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization      | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#edit_part.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#edit_part.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#edit_part.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#edit_part.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#edit_part.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#edit_part.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#edit_part.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#edit_part.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#edit_part.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#edit_part.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#edit_part.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#edit_part.ApiResponseFor501) | Not implemented                                             |

#### edit_part.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**JobPartExtendedDto**](../../models/JobPartExtendedDto.md) |             |

#### edit_part.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_part.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_part.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_part.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_part.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_part.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_part.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_part.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_part.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_part.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_part.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_parts**

<a id="edit_parts"></a>

> JobPartsDto edit_parts(project_uid)

Edit jobs (batch)

Returns only jobs which were updated by the batch operation.

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_update_batch_dto import JobPartUpdateBatchDto
from phrasetms_client.model.job_parts_dto import JobPartsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit jobs (batch)
        api_response = api_instance.edit_parts(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->edit_parts: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = JobPartUpdateBatchDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        status="NEW",
        date_due="1970-01-01T00:00:00.00Z",
        providers=[
            ProviderReference()
        ],
    )
    try:
        # Edit jobs (batch)
        api_response = api_instance.edit_parts(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->edit_parts: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**JobPartUpdateBatchDto**](../../models/JobPartUpdateBatchDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                              | Description                                                 |
| ---- | -------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization       | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#edit_parts.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#edit_parts.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#edit_parts.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#edit_parts.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#edit_parts.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#edit_parts.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#edit_parts.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#edit_parts.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#edit_parts.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#edit_parts.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#edit_parts.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#edit_parts.ApiResponseFor501) | Not implemented                                             |

#### edit_parts.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**JobPartsDto**](../../models/JobPartsDto.md) |             |

#### edit_parts.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_parts.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_parts.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_parts.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_parts.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_parts.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_parts.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_parts.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_parts.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_parts.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_parts.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_to_online_repository**

<a id="export_to_online_repository"></a>

> JobExportResponseDto export_to_online_repository(project_uid)

Export jobs to online repository

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_export_response_dto import JobExportResponseDto
from phrasetms_client.model.job_export_action_dto import JobExportActionDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Export jobs to online repository
        api_response = api_instance.export_to_online_repository(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->export_to_online_repository: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = JobExportActionDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
    )
    try:
        # Export jobs to online repository
        api_response = api_instance.export_to_online_repository(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->export_to_online_repository: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBody, Unset]        | optional, default is unset        |
| path_params          | RequestPathParams                                |                                   |
| content_type         | str                                              | optional, default is '_/_'        | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBody

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**JobExportActionDto**](../../models/JobExportActionDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                               | Description                                                 |
| ---- | ------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                        | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#export_to_online_repository.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#export_to_online_repository.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#export_to_online_repository.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#export_to_online_repository.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#export_to_online_repository.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#export_to_online_repository.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#export_to_online_repository.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#export_to_online_repository.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#export_to_online_repository.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#export_to_online_repository.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#export_to_online_repository.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#export_to_online_repository.ApiResponseFor501) | Not implemented                                             |

#### export_to_online_repository.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**JobExportResponseDto**](../../models/JobExportResponseDto.md) |             |

#### export_to_online_repository.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### export_to_online_repository.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### export_to_online_repository.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### export_to_online_repository.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### export_to_online_repository.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### export_to_online_repository.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### export_to_online_repository.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### export_to_online_repository.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### export_to_online_repository.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### export_to_online_repository.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### export_to_online_repository.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **file_preview**

<a id="file_preview"></a>

> file_preview(project_uidjob_uid)

Download preview file

Takes bilingual file (.mxliff only) as argument. If not passed, data will be taken from database

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Download preview file
        api_response = api_instance.file_preview(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->file_preview: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = dict()
    try:
        # Download preview file
        api_response = api_instance.file_preview(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->file_preview: %s\n" % e)
```

### Parameters

| Name                 | Type                                                            | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset                      |
| path_params          | RequestPathParams                                               |                                                 |
| content_type         | str                                                             | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                            | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                            | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#file_preview.ApiResponseFor200) | application/octet-stream                                    |
| 400  | [ApiResponseFor400](#file_preview.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#file_preview.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#file_preview.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#file_preview.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#file_preview.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#file_preview.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#file_preview.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#file_preview.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#file_preview.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#file_preview.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#file_preview.ApiResponseFor501) | Not implemented                                             |

#### file_preview.ApiResponseFor200

| Name     | Type                  | Description  | Notes |
| -------- | --------------------- | ------------ | ----- |
| response | urllib3.HTTPResponse  | Raw response |
| body     | typing.Union[]        |              |
| headers  | ResponseHeadersFor200 |              |

#### ResponseHeadersFor200

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Content-Disposition | ContentDispositionSchema |             | optional |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

#### file_preview.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **file_preview_job**

<a id="file_preview_job"></a>

> file_preview_job(project_uidjob_uid)

Download preview file

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Download preview file
        api_response = api_instance.file_preview_job(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->file_preview_job: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#file_preview_job.ApiResponseFor200) | application/octet-stream                                    |
| 400  | [ApiResponseFor400](#file_preview_job.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#file_preview_job.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#file_preview_job.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#file_preview_job.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#file_preview_job.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#file_preview_job.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#file_preview_job.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#file_preview_job.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#file_preview_job.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#file_preview_job.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#file_preview_job.ApiResponseFor501) | Not implemented                                             |

#### file_preview_job.ApiResponseFor200

| Name     | Type                  | Description  | Notes |
| -------- | --------------------- | ------------ | ----- |
| response | urllib3.HTTPResponse  | Raw response |
| body     | typing.Union[]        |              |
| headers  | ResponseHeadersFor200 |              |

#### ResponseHeadersFor200

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Content-Disposition | ContentDispositionSchema |             | optional |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

#### file_preview_job.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview_job.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview_job.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview_job.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview_job.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview_job.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview_job.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview_job.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview_job.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview_job.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### file_preview_job.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_bilingual_file**

<a id="get_bilingual_file"></a>

> get_bilingual_file(project_uid)

Download bilingual file

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.get_bilingual_file_dto import GetBilingualFileDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Download bilingual file
        api_response = api_instance.get_bilingual_file(
            path_params=path_params,
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_bilingual_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'format': "MXLF",
        'preview': True,
    }
    body = GetBilingualFileDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
    )
    try:
        # Download bilingual file
        api_response = api_instance.get_bilingual_file(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_bilingual_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| query_params         | RequestQueryParams                                       |                                         |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**GetBilingualFileDto**](../../models/GetBilingualFileDto.md) |             |

### query_params

#### RequestQueryParams

| Name    | Type          | Description | Notes    |
| ------- | ------------- | ----------- | -------- |
| format  | FormatSchema  |             | optional |
| preview | PreviewSchema |             | optional |

# FormatSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                                        |
| ---------- | ------------- | ----------- | ------------------------------------------------------------------------------------------------------------ |
| str,       | str,          |             | must be one of ["MXLF", "DOCX", "XLIFF", "TMX", ] if omitted the server will use the default value of "MXLF" |

# PreviewSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                    |
| ---------- | ------------- | ----------- | -------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of True |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                         |
| ---- | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned         |
| 200  | [ApiResponseFor200](#get_bilingual_file.ApiResponseFor200) | application/octet-stream, application/mxliff, application/xliff+xml |
| 400  | [ApiResponseFor400](#get_bilingual_file.ApiResponseFor400) | Bad request                                                         |
| 401  | [ApiResponseFor401](#get_bilingual_file.ApiResponseFor401) | Not authorized                                                      |
| 403  | [ApiResponseFor403](#get_bilingual_file.ApiResponseFor403) | Forbidden                                                           |
| 404  | [ApiResponseFor404](#get_bilingual_file.ApiResponseFor404) | Resource not found                                                  |
| 405  | [ApiResponseFor405](#get_bilingual_file.ApiResponseFor405) | Method not allowed                                                  |
| 408  | [ApiResponseFor408](#get_bilingual_file.ApiResponseFor408) | Timeout                                                             |
| 410  | [ApiResponseFor410](#get_bilingual_file.ApiResponseFor410) | Gone                                                                |
| 415  | [ApiResponseFor415](#get_bilingual_file.ApiResponseFor415) | Unsupported media type                                              |
| 429  | [ApiResponseFor429](#get_bilingual_file.ApiResponseFor429) | Too many requests                                                   |
| 500  | [ApiResponseFor500](#get_bilingual_file.ApiResponseFor500) | Internal server error                                               |
| 501  | [ApiResponseFor501](#get_bilingual_file.ApiResponseFor501) | Not implemented                                                     |

#### get_bilingual_file.ApiResponseFor200

| Name     | Type                  | Description  | Notes |
| -------- | --------------------- | ------------ | ----- |
| response | urllib3.HTTPResponse  | Raw response |
| body     | typing.Union[]        |              |
| headers  | ResponseHeadersFor200 |              |

#### ResponseHeadersFor200

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Content-Disposition | ContentDispositionSchema |             | optional |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

#### get_bilingual_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_completed_file_warnings**

<a id="get_completed_file_warnings"></a>

> TargetFileWarningsDto get_completed_file_warnings(project_uidjob_uid)

Get target file's warnings

This call will return target file's warnings. This means even for other jobs that were created via 'split jobs' etc.

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.target_file_warnings_dto import TargetFileWarningsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get target file's warnings
        api_response = api_instance.get_completed_file_warnings(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_completed_file_warnings: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                               | Description                                                 |
| ---- | ------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                        | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_completed_file_warnings.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_completed_file_warnings.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_completed_file_warnings.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_completed_file_warnings.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_completed_file_warnings.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_completed_file_warnings.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_completed_file_warnings.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_completed_file_warnings.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_completed_file_warnings.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_completed_file_warnings.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_completed_file_warnings.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_completed_file_warnings.ApiResponseFor501) | Not implemented                                             |

#### get_completed_file_warnings.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**TargetFileWarningsDto**](../../models/TargetFileWarningsDto.md) |             |

#### get_completed_file_warnings.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_completed_file_warnings.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_completed_file_warnings.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_completed_file_warnings.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_completed_file_warnings.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_completed_file_warnings.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_completed_file_warnings.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_completed_file_warnings.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_completed_file_warnings.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_completed_file_warnings.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_completed_file_warnings.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_handover_files**

<a id="get_handover_files"></a>

> get_handover_files(project_uid)

Download handover file(s)

For downloading multiple files as ZIP file provide multiple IDs in query parameters. _ For example `?jobUid={id1}&jobUid={id2}` _ When no files matched given IDs error 404 is returned, otherwise ZIP file will include those that were found

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Download handover file(s)
        api_response = api_instance.get_handover_files(
            path_params=path_params,
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_handover_files: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'jobUid': [
        "jobUid_example"
    ],
    }
    try:
        # Download handover file(s)
        api_response = api_instance.get_handover_files(
            path_params=path_params,
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_handover_files: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                  |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name   | Type         | Description | Notes    |
| ------ | ------------ | ----------- | -------- |
| jobUid | JobUidSchema |             | optional |

# JobUidSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_handover_files.ApiResponseFor200) | File / Archive with file handovers                          |
| 400  | [ApiResponseFor400](#get_handover_files.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_handover_files.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_handover_files.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_handover_files.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_handover_files.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_handover_files.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_handover_files.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_handover_files.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_handover_files.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_handover_files.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_handover_files.ApiResponseFor501) | Not implemented                                             |

#### get_handover_files.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_handover_files.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_import_settings3**

<a id="get_import_settings3"></a>

> FileImportSettingsDto get_import_settings3(project_uidjob_uid)

Get import settings for job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.file_import_settings_dto import FileImportSettingsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get import settings for job
        api_response = api_instance.get_import_settings3(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_import_settings3: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_import_settings3.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_import_settings3.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_import_settings3.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_import_settings3.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_import_settings3.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_import_settings3.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_import_settings3.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_import_settings3.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_import_settings3.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_import_settings3.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_import_settings3.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_import_settings3.ApiResponseFor501) | Not implemented                                             |

#### get_import_settings3.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**FileImportSettingsDto**](../../models/FileImportSettingsDto.md) |             |

#### get_import_settings3.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings3.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings3.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings3.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings3.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings3.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings3.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings3.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_import_settings3.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_original_file**

<a id="get_original_file"></a>

> get_original_file(project_uidjob_uid)

Download original file

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Download original file
        api_response = api_instance.get_original_file(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_original_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_original_file.ApiResponseFor200) | application/octet-stream                                    |
| 400  | [ApiResponseFor400](#get_original_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_original_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_original_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_original_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_original_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_original_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_original_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_original_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_original_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_original_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_original_file.ApiResponseFor501) | Not implemented                                             |

#### get_original_file.ApiResponseFor200

| Name     | Type                  | Description  | Notes |
| -------- | --------------------- | ------------ | ----- |
| response | urllib3.HTTPResponse  | Raw response |
| body     | typing.Union[]        |              |
| headers  | ResponseHeadersFor200 |              |

#### ResponseHeadersFor200

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Content-Disposition | ContentDispositionSchema |             | optional |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

#### get_original_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_original_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_original_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_original_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_original_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_original_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_original_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_original_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_original_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_original_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_original_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_part**

<a id="get_part"></a>

> JobPartExtendedDto get_part(project_uidjob_uid)

Get job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_extended_dto import JobPartExtendedDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get job
        api_response = api_instance.get_part(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_part: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                            | Description                                                 |
| ---- | ------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization     | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_part.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_part.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_part.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_part.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_part.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_part.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_part.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_part.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_part.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_part.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_part.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_part.ApiResponseFor501) | Not implemented                                             |

#### get_part.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**JobPartExtendedDto**](../../models/JobPartExtendedDto.md) |             |

#### get_part.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_part.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_part.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_part.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_part.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_part.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_part.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_part.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_part.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_part.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_part.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_parts_workflow_step**

<a id="get_parts_workflow_step"></a>

> ProjectWorkflowStepDto get_parts_workflow_step(project_uidjob_uid)

Get job's workflowStep

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.project_workflow_step_dto import ProjectWorkflowStepDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get job's workflowStep
        api_response = api_instance.get_parts_workflow_step(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_parts_workflow_step: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                           | Description                                                 |
| ---- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                    | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_parts_workflow_step.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_parts_workflow_step.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_parts_workflow_step.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_parts_workflow_step.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_parts_workflow_step.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_parts_workflow_step.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_parts_workflow_step.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_parts_workflow_step.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_parts_workflow_step.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_parts_workflow_step.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_parts_workflow_step.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_parts_workflow_step.ApiResponseFor501) | Not implemented                                             |

#### get_parts_workflow_step.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**ProjectWorkflowStepDto**](../../models/ProjectWorkflowStepDto.md) |             |

#### get_parts_workflow_step.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_parts_workflow_step.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_parts_workflow_step.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_parts_workflow_step.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_parts_workflow_step.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_parts_workflow_step.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_parts_workflow_step.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_parts_workflow_step.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_parts_workflow_step.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_parts_workflow_step.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_parts_workflow_step.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_segments_count**

<a id="get_segments_count"></a>

> SegmentsCountsResponseListDto get_segments_count(project_uid)

Get segments count

Provides segments count (progress data)

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_ready_references import JobPartReadyReferences
from phrasetms_client.model.segments_counts_response_list_dto import SegmentsCountsResponseListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get segments count
        api_response = api_instance.get_segments_count(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_segments_count: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = JobPartReadyReferences(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        get_parts=dict(),
    )
    try:
        # Get segments count
        api_response = api_instance.get_segments_count(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_segments_count: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**JobPartReadyReferences**](../../models/JobPartReadyReferences.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_segments_count.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_segments_count.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_segments_count.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_segments_count.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_segments_count.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_segments_count.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_segments_count.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_segments_count.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_segments_count.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_segments_count.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_segments_count.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_segments_count.ApiResponseFor501) | Not implemented                                             |

#### get_segments_count.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**SegmentsCountsResponseListDto**](../../models/SegmentsCountsResponseListDto.md) |             |

#### get_segments_count.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segments_count.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segments_count.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segments_count.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segments_count.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segments_count.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segments_count.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segments_count.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segments_count.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segments_count.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segments_count.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_translation_resources**

<a id="get_translation_resources"></a>

> TranslationResourcesDto get_translation_resources(project_uidjob_uid)

Get translation resources

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.translation_resources_dto import TranslationResourcesDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get translation resources
        api_response = api_instance.get_translation_resources(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->get_translation_resources: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                             | Description                                                 |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_translation_resources.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_translation_resources.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_translation_resources.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_translation_resources.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_translation_resources.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_translation_resources.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_translation_resources.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_translation_resources.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_translation_resources.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_translation_resources.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_translation_resources.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_translation_resources.ApiResponseFor501) | Not implemented                                             |

#### get_translation_resources.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationResourcesDto**](../../models/TranslationResourcesDto.md) |             |

#### get_translation_resources.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_part_analyse_v3**

<a id="list_part_analyse_v3"></a>

> PageDtoAnalyseReference list_part_analyse_v3(project_uidjob_uid)

List analyses

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.page_dto_analyse_reference import PageDtoAnalyseReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    query_params = {
    }
    try:
        # List analyses
        api_response = api_instance.list_part_analyse_v3(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->list_part_analyse_v3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List analyses
        api_response = api_instance.list_part_analyse_v3(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->list_part_analyse_v3: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name       | Type             | Description | Notes    |
| ---------- | ---------------- | ----------- | -------- |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |

# PageNumberSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 0value must be a 32 bit integer |

# PageSizeSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                                |
| --------------------- | ---------------- | ----------- | ------------------------------------------------------------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 50value must be a 32 bit integer |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_part_analyse_v3.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_part_analyse_v3.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_part_analyse_v3.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_part_analyse_v3.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_part_analyse_v3.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_part_analyse_v3.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_part_analyse_v3.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_part_analyse_v3.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_part_analyse_v3.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_part_analyse_v3.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_part_analyse_v3.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_part_analyse_v3.ApiResponseFor501) | Not implemented                                             |

#### list_part_analyse_v3.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoAnalyseReference**](../../models/PageDtoAnalyseReference.md) |             |

#### list_part_analyse_v3.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_parts_v2**

<a id="list_parts_v2"></a>

> PageDtoJobPartReferenceV2 list_parts_v2(project_uid)

List jobs

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.page_dto_job_part_reference_v2 import PageDtoJobPartReferenceV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # List jobs
        api_response = api_instance.list_parts_v2(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->list_parts_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
        'count': False,
        'workflowLevel': 1,
        'status': [
        "NEW"
    ],
        'assignedUser': 1,
        'dueInHours': 1,
        'filename': "filename_example",
        'targetLang': "targetLang_example",
        'assignedVendor': 1,
    }
    try:
        # List jobs
        api_response = api_instance.list_parts_v2(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->list_parts_v2: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name           | Type                 | Description | Notes    |
| -------------- | -------------------- | ----------- | -------- |
| pageNumber     | PageNumberSchema     |             | optional |
| pageSize       | PageSizeSchema       |             | optional |
| count          | CountSchema          |             | optional |
| workflowLevel  | WorkflowLevelSchema  |             | optional |
| status         | StatusSchema         |             | optional |
| assignedUser   | AssignedUserSchema   |             | optional |
| dueInHours     | DueInHoursSchema     |             | optional |
| filename       | FilenameSchema       |             | optional |
| targetLang     | TargetLangSchema     |             | optional |
| assignedVendor | AssignedVendorSchema |             | optional |

# PageNumberSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 0value must be a 32 bit integer |

# PageSizeSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                                |
| --------------------- | ---------------- | ----------- | ------------------------------------------------------------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 50value must be a 32 bit integer |

# CountSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

# WorkflowLevelSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 1value must be a 32 bit integer |

# StatusSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                                                          |
| ---------- | ---------- | ------------- | ----------- | -------------------------------------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["NEW", "ACCEPTED", "DECLINED", "REJECTED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] |

# AssignedUserSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 64 bit integer |

# DueInHoursSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 32 bit integer |

# FilenameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# TargetLangSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# AssignedVendorSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 64 bit integer |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_parts_v2.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_parts_v2.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_parts_v2.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_parts_v2.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_parts_v2.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_parts_v2.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_parts_v2.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_parts_v2.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_parts_v2.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_parts_v2.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_parts_v2.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_parts_v2.ApiResponseFor501) | Not implemented                                             |

#### list_parts_v2.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoJobPartReferenceV2**](../../models/PageDtoJobPartReferenceV2.md) |             |

#### list_parts_v2.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_parts_v2.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_parts_v2.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_parts_v2.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_parts_v2.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_parts_v2.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_parts_v2.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_parts_v2.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_parts_v2.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_parts_v2.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_parts_v2.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_providers4**

<a id="list_providers4"></a>

> ProviderListDtoV2 list_providers4(project_uidjob_uid)

Get suggested providers

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.provider_list_dto_v2 import ProviderListDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get suggested providers
        api_response = api_instance.list_providers4(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->list_providers4: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description          | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                      |
| accept_content_types | typing.Tuple[str]                                | default is ('_/_', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False     | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None      | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False     | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_providers4.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_providers4.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_providers4.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_providers4.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_providers4.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_providers4.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_providers4.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_providers4.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_providers4.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_providers4.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_providers4.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_providers4.ApiResponseFor501) | Not implemented                                             |

#### list_providers4.ApiResponseFor200

| Name     | Type                                     | Description              | Notes |
| -------- | ---------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                     | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBody, ] |                          |
| headers  | Unset                                    | headers were not defined |

# SchemaFor200ResponseBody

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**ProviderListDtoV2**](../../models/ProviderListDtoV2.md) |             |

#### list_providers4.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_segments**

<a id="list_segments"></a>

> SegmentListDto list_segments(project_uidjob_uid)

Get segments

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.segment_list_dto import SegmentListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    query_params = {
    }
    try:
        # Get segments
        api_response = api_instance.list_segments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->list_segments: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    query_params = {
        'beginIndex': 0,
        'endIndex': 0,
    }
    try:
        # Get segments
        api_response = api_instance.list_segments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->list_segments: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name       | Type             | Description | Notes    |
| ---------- | ---------------- | ----------- | -------- |
| beginIndex | BeginIndexSchema |             | optional |
| endIndex   | EndIndexSchema   |             | optional |

# BeginIndexSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 0value must be a 32 bit integer |

# EndIndexSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 0value must be a 32 bit integer |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_segments.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_segments.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_segments.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_segments.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_segments.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_segments.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_segments.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_segments.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_segments.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_segments.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_segments.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_segments.ApiResponseFor501) | Not implemented                                             |

#### list_segments.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                 | Description | Notes |
| ---------------------------------------------------- | ----------- | ----- |
| [**SegmentListDto**](../../models/SegmentListDto.md) |             |

#### list_segments.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_segments.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_segments.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_segments.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_segments.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_segments.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_segments.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_segments.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_segments.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_segments.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_segments.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **notify_assigned**

<a id="notify_assigned"></a>

> notify_assigned(project_uid)

Notify assigned users

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.notify_job_parts_request_dto import NotifyJobPartsRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Notify assigned users
        api_response = api_instance.notify_assigned(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->notify_assigned: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = NotifyJobPartsRequestDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        email_template=IdReference(
            id="id_example",
        ),
        cc=[
            "cc_example"
        ],
,
    )
    try:
        # Notify assigned users
        api_response = api_instance.notify_assigned(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->notify_assigned: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**NotifyJobPartsRequestDto**](../../models/NotifyJobPartsRequestDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#notify_assigned.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#notify_assigned.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#notify_assigned.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#notify_assigned.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#notify_assigned.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#notify_assigned.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#notify_assigned.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#notify_assigned.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#notify_assigned.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#notify_assigned.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#notify_assigned.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#notify_assigned.ApiResponseFor501) | Not implemented                                             |

#### notify_assigned.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### notify_assigned.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_part**

<a id="patch_part"></a>

> JobPartExtendedDto patch_part(project_uidjob_uid)

Patch job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_extended_dto import JobPartExtendedDto
from phrasetms_client.model.job_part_patch_single_dto import JobPartPatchSingleDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Patch job
        api_response = api_instance.patch_part(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->patch_part: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = JobPartPatchSingleDto(
        status="NEW",
        date_due="1970-01-01T00:00:00.00Z",
        providers=[
            ProviderReference()
        ],
    )
    try:
        # Patch job
        api_response = api_instance.patch_part(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->patch_part: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**JobPartPatchSingleDto**](../../models/JobPartPatchSingleDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                              | Description                                                 |
| ---- | -------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization       | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#patch_part.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#patch_part.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#patch_part.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#patch_part.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#patch_part.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#patch_part.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#patch_part.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#patch_part.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#patch_part.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#patch_part.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#patch_part.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#patch_part.ApiResponseFor501) | Not implemented                                             |

#### patch_part.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**JobPartExtendedDto**](../../models/JobPartExtendedDto.md) |             |

#### patch_part.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_part.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_part.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_part.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_part.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_part.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_part.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_part.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_part.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_part.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_part.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_update_job_parts**

<a id="patch_update_job_parts"></a>

> JobPartPatchResultDto patch_update_job_parts()

Edit jobs (with possible partial updates)

Allows partial update, not breaking whole batch if single job fails and returns list of errors

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_patch_result_dto import JobPartPatchResultDto
from phrasetms_client.model.job_part_patch_batch_dto import JobPartPatchBatchDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only optional values
    body = JobPartPatchBatchDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        status="NEW",
        date_due="1970-01-01T00:00:00.00Z",
        clear_date_due=True,
        providers=[
            ProviderReference()
        ],
    )
    try:
        # Edit jobs (with possible partial updates)
        api_response = api_instance.patch_update_job_parts(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->patch_update_job_parts: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**JobPartPatchBatchDto**](../../models/JobPartPatchBatchDto.md) |             |

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#patch_update_job_parts.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#patch_update_job_parts.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#patch_update_job_parts.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#patch_update_job_parts.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#patch_update_job_parts.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#patch_update_job_parts.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#patch_update_job_parts.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#patch_update_job_parts.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#patch_update_job_parts.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#patch_update_job_parts.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#patch_update_job_parts.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#patch_update_job_parts.ApiResponseFor501) | Not implemented                                             |

#### patch_update_job_parts.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**JobPartPatchResultDto**](../../models/JobPartPatchResultDto.md) |             |

#### patch_update_job_parts.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_update_job_parts.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_update_job_parts.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_update_job_parts.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_update_job_parts.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_update_job_parts.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_update_job_parts.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_update_job_parts.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_update_job_parts.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_update_job_parts.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### patch_update_job_parts.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **preview_urls**

<a id="preview_urls"></a>

> PreviewUrlsDto preview_urls(project_uidjob_uid)

Get PDF preview

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.preview_urls_dto import PreviewUrlsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    query_params = {
    }
    try:
        # Get PDF preview
        api_response = api_instance.preview_urls(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->preview_urls: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    query_params = {
        'workflowLevel': 1,
    }
    try:
        # Get PDF preview
        api_response = api_instance.preview_urls(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->preview_urls: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name          | Type                | Description | Notes    |
| ------------- | ------------------- | ----------- | -------- |
| workflowLevel | WorkflowLevelSchema |             | optional |

# WorkflowLevelSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 1value must be a 32 bit integer |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#preview_urls.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#preview_urls.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#preview_urls.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#preview_urls.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#preview_urls.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#preview_urls.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#preview_urls.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#preview_urls.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#preview_urls.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#preview_urls.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#preview_urls.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#preview_urls.ApiResponseFor501) | Not implemented                                             |

#### preview_urls.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                 | Description | Notes |
| ---------------------------------------------------- | ----------- | ----- |
| [**PreviewUrlsDto**](../../models/PreviewUrlsDto.md) |             |

#### preview_urls.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### preview_urls.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### preview_urls.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### preview_urls.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### preview_urls.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### preview_urls.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### preview_urls.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### preview_urls.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### preview_urls.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### preview_urls.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### preview_urls.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **pseudo_translate1**

<a id="pseudo_translate1"></a>

> pseudo_translate1(project_uid)

Pseudo-translate job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.pseudo_translate_wrapper_dto import PseudoTranslateWrapperDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Pseudo-translate job
        api_response = api_instance.pseudo_translate1(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->pseudo_translate1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = PseudoTranslateWrapperDto(
        job_parts=JobPartReadyReferences(
            jobs=[
                UidReference(
                    uid="uid_example",
                )
            ],
            get_parts=dict(),
        ),
        pseudo_translate=PseudoTranslateActionDtoV2(
            replacement="replacement_example",
            prefix="prefix_example",
            suffix="suffix_example",
            length=3.14,
            key_hash_prefix_len=0,
            substitution=[
                SubstituteDtoV2(
                    source="source_example",
                    target="target_example",
                )
            ],
        ),
    )
    try:
        # Pseudo-translate job
        api_response = api_instance.pseudo_translate1(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->pseudo_translate1: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBody, Unset]        | optional, default is unset |
| path_params          | RequestPathParams                                |                            |
| content_type         | str                                              | optional, default is '_/_' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                             | default is False           | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None            | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False           | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBody

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**PseudoTranslateWrapperDto**](../../models/PseudoTranslateWrapperDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#pseudo_translate1.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#pseudo_translate1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#pseudo_translate1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#pseudo_translate1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#pseudo_translate1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#pseudo_translate1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#pseudo_translate1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#pseudo_translate1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#pseudo_translate1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#pseudo_translate1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#pseudo_translate1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#pseudo_translate1.ApiResponseFor501) | Not implemented                                             |

#### pseudo_translate1.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **pseudo_translate_job_part**

<a id="pseudo_translate_job_part"></a>

> pseudo_translate_job_part(project_uidjob_uid)

Pseudo-translates job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.pseudo_translate_action_dto import PseudoTranslateActionDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Pseudo-translates job
        api_response = api_instance.pseudo_translate_job_part(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->pseudo_translate_job_part: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = PseudoTranslateActionDto(
        replacement="replacement_example",
        prefix="prefix_example",
        suffix="suffix_example",
        length=3.14,
        key_hash_prefix_len=0,
        substitution=[
            SubstituteDto(
                source="source_example",
                target="target_example",
            )
        ],
    )
    try:
        # Pseudo-translates job
        api_response = api_instance.pseudo_translate_job_part(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->pseudo_translate_job_part: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**PseudoTranslateActionDto**](../../models/PseudoTranslateActionDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                             | Description                                                 |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#pseudo_translate_job_part.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#pseudo_translate_job_part.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#pseudo_translate_job_part.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#pseudo_translate_job_part.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#pseudo_translate_job_part.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#pseudo_translate_job_part.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#pseudo_translate_job_part.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#pseudo_translate_job_part.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#pseudo_translate_job_part.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#pseudo_translate_job_part.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#pseudo_translate_job_part.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#pseudo_translate_job_part.ApiResponseFor501) | Not implemented                                             |

#### pseudo_translate_job_part.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### pseudo_translate_job_part.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_by_job3**

<a id="search_by_job3"></a>

> SearchResponseListTmDtoV3 search_by_job3(project_uidjob_uid)

Search job's translation memories

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.search_response_list_tm_dto_v3 import SearchResponseListTmDtoV3
from phrasetms_client.model.search_tmby_job_request_dto_v3 import SearchTMByJobRequestDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Search job's translation memories
        api_response = api_instance.search_by_job3(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->search_by_job3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = SearchTMByJobRequestDtoV3(
        query="query_example",
        reverse=True,
        score_threshold=0,
        max_results=1,
    )
    try:
        # Search job's translation memories
        api_response = api_instance.search_by_job3(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->search_by_job3: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBody, Unset]        | optional, default is unset        |
| path_params          | RequestPathParams                                |                                   |
| content_type         | str                                              | optional, default is '_/_'        | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBody

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SearchTMByJobRequestDtoV3**](../../models/SearchTMByJobRequestDtoV3.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#search_by_job3.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#search_by_job3.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#search_by_job3.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#search_by_job3.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#search_by_job3.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#search_by_job3.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#search_by_job3.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#search_by_job3.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#search_by_job3.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#search_by_job3.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#search_by_job3.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#search_by_job3.ApiResponseFor501) | Not implemented                                             |

#### search_by_job3.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SearchResponseListTmDtoV3**](../../models/SearchResponseListTmDtoV3.md) |             |

#### search_by_job3.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_by_job3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_by_job3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_by_job3.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_by_job3.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_by_job3.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_by_job3.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_by_job3.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_by_job3.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_by_job3.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_by_job3.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_parts_in_project**

<a id="search_parts_in_project"></a>

> SearchJobsDto search_parts_in_project(project_uid)

Search jobs in project

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.search_jobs_dto import SearchJobsDto
from phrasetms_client.model.search_jobs_request_dto import SearchJobsRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Search jobs in project
        api_response = api_instance.search_parts_in_project(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->search_parts_in_project: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = SearchJobsRequestDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
    )
    try:
        # Search jobs in project
        api_response = api_instance.search_parts_in_project(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->search_parts_in_project: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**SearchJobsRequestDto**](../../models/SearchJobsRequestDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                           | Description                                                 |
| ---- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                    | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#search_parts_in_project.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#search_parts_in_project.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#search_parts_in_project.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#search_parts_in_project.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#search_parts_in_project.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#search_parts_in_project.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#search_parts_in_project.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#search_parts_in_project.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#search_parts_in_project.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#search_parts_in_project.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#search_parts_in_project.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#search_parts_in_project.ApiResponseFor501) | Not implemented                                             |

#### search_parts_in_project.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                               | Description | Notes |
| -------------------------------------------------- | ----------- | ----- |
| [**SearchJobsDto**](../../models/SearchJobsDto.md) |             |

#### search_parts_in_project.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_parts_in_project.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_parts_in_project.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_parts_in_project.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_parts_in_project.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_parts_in_project.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_parts_in_project.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_parts_in_project.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_parts_in_project.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_parts_in_project.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_parts_in_project.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_segment_by_job**

<a id="search_segment_by_job"></a>

> SearchResponseListTmDto search_segment_by_job(project_uidjob_uid)

Search translation memory for segment by job

Returns at most <i>maxSegments</i> records with <i>score >= scoreThreshold</i> and at most <i>maxSubsegments</i> records which are subsegment, i.e. the source text is substring of the query text.

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.search_tmby_job_request_dto import SearchTMByJobRequestDto
from phrasetms_client.model.search_response_list_tm_dto import SearchResponseListTmDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Search translation memory for segment by job
        api_response = api_instance.search_segment_by_job(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->search_segment_by_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = SearchTMByJobRequestDto(
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
    )
    try:
        # Search translation memory for segment by job
        api_response = api_instance.search_segment_by_job(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->search_segment_by_job: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**SearchTMByJobRequestDto**](../../models/SearchTMByJobRequestDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                         | Description                                                 |
| ---- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                  | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#search_segment_by_job.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#search_segment_by_job.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#search_segment_by_job.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#search_segment_by_job.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#search_segment_by_job.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#search_segment_by_job.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#search_segment_by_job.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#search_segment_by_job.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#search_segment_by_job.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#search_segment_by_job.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#search_segment_by_job.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#search_segment_by_job.ApiResponseFor501) | Not implemented                                             |

#### search_segment_by_job.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**SearchResponseListTmDto**](../../models/SearchResponseListTmDto.md) |             |

#### search_segment_by_job.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_segment_by_job.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_segment_by_job.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_segment_by_job.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_segment_by_job.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_segment_by_job.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_segment_by_job.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_segment_by_job.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_segment_by_job.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_segment_by_job.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_segment_by_job.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_terms_by_job1**

<a id="search_terms_by_job1"></a>

> SearchTbResponseListDto search_terms_by_job1(job_uidproject_uid)

Search job's term bases

Search all read term bases assigned to the job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.search_tb_by_job_request_dto import SearchTbByJobRequestDto
from phrasetms_client.model.search_tb_response_list_dto import SearchTbResponseListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'projectUid': "projectUid_example",
    }
    try:
        # Search job's term bases
        api_response = api_instance.search_terms_by_job1(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->search_terms_by_job1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
        'projectUid': "projectUid_example",
    }
    body = SearchTbByJobRequestDto(
        query="query_example",
        count=1,
        offset=1,
        reverse=True,
    )
    try:
        # Search job's term bases
        api_response = api_instance.search_terms_by_job1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->search_terms_by_job1: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**SearchTbByJobRequestDto**](../../models/SearchTbByJobRequestDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| jobUid     | JobUidSchema     |             |
| projectUid | ProjectUidSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#search_terms_by_job1.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#search_terms_by_job1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#search_terms_by_job1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#search_terms_by_job1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#search_terms_by_job1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#search_terms_by_job1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#search_terms_by_job1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#search_terms_by_job1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#search_terms_by_job1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#search_terms_by_job1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#search_terms_by_job1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#search_terms_by_job1.ApiResponseFor501) | Not implemented                                             |

#### search_terms_by_job1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**SearchTbResponseListDto**](../../models/SearchTbResponseListDto.md) |             |

#### search_terms_by_job1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_by_job1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_by_job1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_by_job1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_by_job1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_by_job1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_by_job1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_by_job1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_by_job1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_by_job1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_by_job1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_terms_in_text_by_job_v2**

<a id="search_terms_in_text_by_job_v2"></a>

> SearchInTextResponseList2Dto search_terms_in_text_by_job_v2(job_uidproject_uid)

Search terms in text

Search in text in all read term bases assigned to the job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.search_tb_in_text_by_job_request_dto import SearchTbInTextByJobRequestDto
from phrasetms_client.model.search_in_text_response_list2_dto import SearchInTextResponseList2Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'projectUid': "projectUid_example",
    }
    try:
        # Search terms in text
        api_response = api_instance.search_terms_in_text_by_job_v2(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->search_terms_in_text_by_job_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
        'projectUid': "projectUid_example",
    }
    body = SearchTbInTextByJobRequestDto(
        text="text_example",
        reverse=True,
        zero_length_separator="zero_length_separator_example",
    )
    try:
        # Search terms in text
        api_response = api_instance.search_terms_in_text_by_job_v2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->search_terms_in_text_by_job_v2: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**SearchTbInTextByJobRequestDto**](../../models/SearchTbInTextByJobRequestDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| jobUid     | JobUidSchema     |             |
| projectUid | ProjectUidSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                                  | Description                                                 |
| ---- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#search_terms_in_text_by_job_v2.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#search_terms_in_text_by_job_v2.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#search_terms_in_text_by_job_v2.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#search_terms_in_text_by_job_v2.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#search_terms_in_text_by_job_v2.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#search_terms_in_text_by_job_v2.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#search_terms_in_text_by_job_v2.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#search_terms_in_text_by_job_v2.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#search_terms_in_text_by_job_v2.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#search_terms_in_text_by_job_v2.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#search_terms_in_text_by_job_v2.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#search_terms_in_text_by_job_v2.ApiResponseFor501) | Not implemented                                             |

#### search_terms_in_text_by_job_v2.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**SearchInTextResponseList2Dto**](../../models/SearchInTextResponseList2Dto.md) |             |

#### search_terms_in_text_by_job_v2.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_status**

<a id="set_status"></a>

> set_status(project_uidjob_uid)

Edit job status

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_status_change_action_dto import JobStatusChangeActionDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Edit job status
        api_response = api_instance.set_status(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->set_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = JobStatusChangeActionDto(
        requested_status="NEW",
        notify_owner=True,
        propagate_status=True,
    )
    try:
        # Edit job status
        api_response = api_instance.set_status(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->set_status: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**JobStatusChangeActionDto**](../../models/JobStatusChangeActionDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                              | Description                                                 |
| ---- | -------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization       | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#set_status.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#set_status.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#set_status.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#set_status.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#set_status.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#set_status.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#set_status.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#set_status.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#set_status.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#set_status.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#set_status.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#set_status.ApiResponseFor501) | Not implemented                                             |

#### set_status.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_status.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **split**

<a id="split"></a>

> JobPartsDto split(project_uidjob_uid)

Split job

Splits job by one of the following methods: _ **After specific segments** - fill in `segmentOrdinals` _ **Into X parts** - fill in `partCount` _ **Into parts with specific size** - fill in `partSize`. partSize represents segment count in each part. _ **Into parts with specific word count** - fill in `wordCount` \* **By document parts** - fill in `byDocumentParts`, works only with **PowerPoint** files Only one option at a time is allowed.

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.split_job_action_dto import SplitJobActionDto
from phrasetms_client.model.job_parts_dto import JobPartsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Split job
        api_response = api_instance.split(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->split: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = SplitJobActionDto(
        segment_ordinals=[
            1
        ],
        part_count=1,
        part_size=1,
        word_count=1,
        by_document_part=True,
    )
    try:
        # Split job
        api_response = api_instance.split(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->split: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**SplitJobActionDto**](../../models/SplitJobActionDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                         | Description                                                 |
| ---- | --------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization  | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#split.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#split.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#split.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#split.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#split.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#split.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#split.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#split.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#split.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#split.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#split.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#split.ApiResponseFor501) | Not implemented                                             |

#### split.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**JobPartsDto**](../../models/JobPartsDto.md) |             |

#### split.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### split.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### split.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### split.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### split.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### split.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### split.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### split.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### split.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### split.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### split.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **status_changes**

<a id="status_changes"></a>

> JobPartStatusChangesDto status_changes(project_uidjob_uid)

Get status changes

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_part_status_changes_dto import JobPartStatusChangesDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get status changes
        api_response = api_instance.status_changes(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->status_changes: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#status_changes.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#status_changes.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#status_changes.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#status_changes.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#status_changes.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#status_changes.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#status_changes.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#status_changes.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#status_changes.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#status_changes.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#status_changes.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#status_changes.ApiResponseFor501) | Not implemented                                             |

#### status_changes.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**JobPartStatusChangesDto**](../../models/JobPartStatusChangesDto.md) |             |

#### status_changes.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### status_changes.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### status_changes.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### status_changes.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### status_changes.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### status_changes.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### status_changes.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### status_changes.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### status_changes.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### status_changes.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### status_changes.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_source**

<a id="update_source"></a>

> JobUpdateSourceResponseDto update_source(project_uid)

Update source

API updated source file for specified job Job file can be provided directly in the message body. Please supply jobs in `Memsource` header. For file in the request body provide also the filename in `Content-Disposition` header. If a job from a multilingual file is updated, all jobs from the same file are update too even if their UIDs aren't listed in the jobs field. Accepted metadata: - `jobs` - **required** - list of jobs UID reference (maximum size `100`) - `preTranslate` - pre translate flag (default `false`) - `allowAutomaticPostAnalysis` - if automatic post editing analysis should be created. If not specified then value is taken from the analyse settings of the project - `callbackUrl` - consumer callback Job restrictions: - job must belong to project specified in path (`projectUid`) - job `UID` must be from the first workflow step - job cannot be split - job cannot be continuous - job cannot originate in a connector - status in any of the job's workflow steps cannot be a final status (`COMPLETED_BY_LINGUIST`, `COMPLETED`, `CANCELLED`) - job UIDs must be from the same multilingual file if a multilingual file is updated - multiple multilingual files or a mixture of multilingual and other jobs cannot be updated in one call File restrictions: - file cannot be a `.zip` file Example: `{   \"jobs\": [     {         \"uid\": \"jobIn1stWfStepAndNonFinalStatusUid\"     }   ],   \"preTranslate\": false,   \"allowAutomaticPostAnalysis\": false   \"callbackUrl\": \"https://my-shiny-service.com/consumeCallback\" }`

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_update_source_response_dto import JobUpdateSourceResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    header_params = {
    }
    try:
        # Update source
        api_response = api_instance.update_source(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->update_source: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    header_params = {
        'Memsource': "Memsource_example",
        'Content-Disposition': "Content-Disposition_example",
    }
    body = dict()
    try:
        # Update source
        api_response = api_instance.update_source(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->update_source: %s\n" % e)
```

### Parameters

| Name                 | Type                                                            | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset                      |
| header_params        | RequestHeaderParams                                             |                                                 |
| path_params          | RequestPathParams                                               |                                                 |
| content_type         | str                                                             | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                               | default is ('application/json', )               | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                            | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                            | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### header_params

#### RequestHeaderParams

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Memsource           | MemsourceSchema          |             | optional |
| Content-Disposition | ContentDispositionSchema |             | optional |

# MemsourceSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#update_source.ApiResponseFor200) | Updated                                                     |
| 400  | [ApiResponseFor400](#update_source.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_source.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_source.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_source.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_source.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_source.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_source.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_source.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_source.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_source.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_source.ApiResponseFor501) | Not implemented                                             |

#### update_source.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**JobUpdateSourceResponseDto**](../../models/JobUpdateSourceResponseDto.md) |             |

#### update_source.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_source.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_source.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_source.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_source.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_source.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_source.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_source.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_source.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_source.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_source.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_target**

<a id="update_target"></a>

> JobUpdateSourceResponseDto update_target(project_uid)

Update target

API update target file for specified job Job file can be provided directly in the message body. Please supply jobs in `Memsource` header. For file in the request body provide also the filename in `Content-Disposition` header. Accepted metadata: - `jobs` - **required** - list of jobs UID reference (maximum size `1`) - `propagateConfirmedToTm` - sets if confirmed segments should be stored in TM (default value: true) - `callbackUrl` - consumer callback - `targetSegmentationRule` - ID reference to segmentation rule of organization to use for update target - `unconfirmChangedSegments` - sets if segments should stay unconfirmed Job restrictions: - job must belong to project specified in path (`projectUid`) - job cannot be split - job cannot be continuous - job cannot be multilingual - job cannot originate in a connector - job cannot have different file extension than original file File restrictions: - file cannot be a `.zip` file - update target is not allowed for jobs with file extensions: xliff, po, tbx, tmx, ttx, ts Example: `{   \"jobs\": [     {         \"uid\": \"jobUid\"     }   ],   \"propagateConfirmedToTm\": true,   \"targetSegmentationRule\": {         \"id\": \"1\"    },   \"callbackUrl\": \"https://my-shiny-service.com/consumeCallback\" }`

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_update_source_response_dto import JobUpdateSourceResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    header_params = {
    }
    try:
        # Update target
        api_response = api_instance.update_target(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->update_target: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    header_params = {
        'Memsource': "Memsource_example",
        'Content-Disposition': "Content-Disposition_example",
    }
    body = dict()
    try:
        # Update target
        api_response = api_instance.update_target(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->update_target: %s\n" % e)
```

### Parameters

| Name                 | Type                                                            | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset                      |
| header_params        | RequestHeaderParams                                             |                                                 |
| path_params          | RequestPathParams                                               |                                                 |
| content_type         | str                                                             | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                               | default is ('application/json', )               | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                            | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                            | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### header_params

#### RequestHeaderParams

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Memsource           | MemsourceSchema          |             | optional |
| Content-Disposition | ContentDispositionSchema |             | optional |

# MemsourceSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 202  | [ApiResponseFor202](#update_target.ApiResponseFor202) | Updated                                                     |
| 400  | [ApiResponseFor400](#update_target.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_target.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_target.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_target.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_target.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_target.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_target.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_target.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_target.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_target.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_target.ApiResponseFor501) | Not implemented                                             |

#### update_target.ApiResponseFor202

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**JobUpdateSourceResponseDto**](../../models/JobUpdateSourceResponseDto.md) |             |

#### update_target.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_target.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_target.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_target.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_target.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_target.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_target.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_target.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_target.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_target.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_target.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_bilingual_file**

<a id="upload_bilingual_file"></a>

> JobPartsDto upload_bilingual_file()

Upload bilingual file

Returns updated job parts

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.job_parts_dto import JobPartsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only optional values
    query_params = {
        'format': "MXLF",
        'saveToTransMemory': "Confirmed",
        'setCompleted': False,
    }
    body = dict()
    try:
        # Upload bilingual file
        api_response = api_instance.upload_bilingual_file(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->upload_bilingual_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                                            | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset                      |
| query_params         | RequestQueryParams                                              |                                                 |
| content_type         | str                                                             | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                               | default is ('application/json', )               | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                            | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                            | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### query_params

#### RequestQueryParams

| Name              | Type                    | Description | Notes    |
| ----------------- | ----------------------- | ----------- | -------- |
| format            | FormatSchema            |             | optional |
| saveToTransMemory | SaveToTransMemorySchema |             | optional |
| setCompleted      | SetCompletedSchema      |             | optional |

# FormatSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                                 |
| ---------- | ------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| str,       | str,          |             | must be one of ["MXLF", "DOCX", "XLIFF", ] if omitted the server will use the default value of "MXLF" |

# SaveToTransMemorySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                                         |
| ---------- | ------------- | ----------- | ------------------------------------------------------------------------------------------------------------- |
| str,       | str,          |             | must be one of ["All", "Confirmed", "None", ] if omitted the server will use the default value of "Confirmed" |

# SetCompletedSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

### Return Types, Responses

| Code | Class                                                         | Description                                                 |
| ---- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                  | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#upload_bilingual_file.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#upload_bilingual_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#upload_bilingual_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#upload_bilingual_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#upload_bilingual_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#upload_bilingual_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#upload_bilingual_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#upload_bilingual_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#upload_bilingual_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#upload_bilingual_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#upload_bilingual_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#upload_bilingual_file.ApiResponseFor501) | Not implemented                                             |

#### upload_bilingual_file.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**JobPartsDto**](../../models/JobPartsDto.md) |             |

#### upload_bilingual_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_handover_file**

<a id="upload_handover_file"></a>

> FileHandoverDto upload_handover_file(project_uidmemsourcecontent_disposition)

Upload handover file

For following jobs the handover file is not supported: _ Continuous jobs _ Jobs from connectors _ Split jobs _ Multilingual jobs

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.file_handover_dto import FileHandoverDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    header_params = {
        'Memsource': "{\"jobs\":[{\"uid\":\"8kMckeDcgWWF4Fe4Szqjb1\"}]}",
        'Content-Disposition': "Content-Disposition_example",
    }
    try:
        # Upload handover file
        api_response = api_instance.upload_handover_file(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->upload_handover_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    header_params = {
        'Memsource': "{\"jobs\":[{\"uid\":\"8kMckeDcgWWF4Fe4Szqjb1\"}]}",
        'Content-Disposition': "Content-Disposition_example",
        'Content-Length': 1,
    }
    body = dict()
    try:
        # Upload handover file
        api_response = api_instance.upload_handover_file(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->upload_handover_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                                            | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset                      |
| header_params        | RequestHeaderParams                                             |                                                 |
| path_params          | RequestPathParams                                               |                                                 |
| content_type         | str                                                             | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                               | default is ('application/json', )               | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                            | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                            | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### header_params

#### RequestHeaderParams

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Memsource           | MemsourceSchema          |             |
| Content-Disposition | ContentDispositionSchema |             |
| Content-Length      | ContentLengthSchema      |             | optional |

# MemsourceSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

# ContentLengthSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 64 bit integer |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#upload_handover_file.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#upload_handover_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#upload_handover_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#upload_handover_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#upload_handover_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#upload_handover_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#upload_handover_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#upload_handover_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#upload_handover_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#upload_handover_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#upload_handover_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#upload_handover_file.ApiResponseFor501) | Not implemented                                             |

#### upload_handover_file.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                   | Description | Notes |
| ------------------------------------------------------ | ----------- | ----- |
| [**FileHandoverDto**](../../models/FileHandoverDto.md) |             |

#### upload_handover_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_handover_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_handover_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_handover_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_handover_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_handover_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_handover_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_handover_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_handover_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_handover_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_handover_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **web_editor_link_v2**

<a id="web_editor_link_v2"></a>

> WebEditorLinkDtoV2 web_editor_link_v2(project_uid)

Get Web Editor URL

Possible warning codes are: - `NOT_ACCEPTED_BY_LINGUIST` - Job is not accepted by linguist - `NOT_ASSIGNED_TO_LINGUIST` - Job is not assigned to linguist - `PDF` - One of requested jobs is PDF - `PREVIOUS_WORKFLOW_NOT_COMPLETED` - Previous workflow step is not completed - `PREVIOUS_WORKFLOW_NOT_COMPLETED_STRICT` - Previous workflow step is not completed and project has strictWorkflowFinish set to true - `IN_DELIVERED_STATE` - Jobs in DELIVERED state - `IN_COMPLETED_STATE` - Jobs in COMPLETED state - `IN_REJECTED_STATE` - Jobs in REJECTED state Possible error codes are: - `ASSIGNED_TO_OTHER_USER` - Job is accepted by other user - `NOT_UNIQUE_TARGET_LANG` - Requested jobs contains different target locales - `TOO_MANY_SEGMENTS` - Count of requested job's segments is higher than **40000** - `TOO_MANY_JOBS` - Count of requested jobs is higher than **290** - `COMPLETED_JOINED_WITH_OTHER` - Jobs in COMPLETED state cannot be joined with jobs in other states - `DELIVERED_JOINED_WITH_OTHER` - Jobs in DELIVERED state cannot be joined with jobs in other states - `REJECTED_JOINED_WITH_OTHER` - Jobs in REJECTED state cannot be joined with jobs in other states Warning response example: `{     \"warnings\": [         {             \"message\": \"Not accepted by linguist\",             \"args\": {                 \"jobs\": [                     \"abcd1234\"                 ]             },             \"code\": \"NOT_ACCEPTED_BY_LINGUIST\"         },         {             \"message\": \"Previous workflow step not completed\",             \"args\": {                 \"jobs\": [                     \"abcd1234\"                 ]             },             \"code\": \"PREVIOUS_WORKFLOW_NOT_COMPLETED\"         }     ],     \"url\": \"/web/job/abcd1234-efgh5678/translate\" }` Error response example: Status: `400 Bad Request` `{     \"errorCode\": \"NOT_UNIQUE_TARGET_LANG\",     \"errorDescription\": \"Only files with identical target languages can be joined\",     \"errorDetails\": [         {             \"code\": \"NOT_UNIQUE_TARGET_LANG\",             \"args\": {                 \"targetLocales\": [                     \"de\",                     \"en\"                 ]             },             \"message\": \"Only files with identical target languages can be joined\"         },         {             \"code\": \"TOO_MANY_SEGMENTS\",             \"args\": {                 \"maxSegments\": 40000,                 \"segments\": 400009             },             \"message\": \"Up to 40000 segments can be opened in the Memsource Web Editor, job has 400009 segments\"         }     ] }`

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.create_web_editor_link_dto_v2 import CreateWebEditorLinkDtoV2
from phrasetms_client.model.web_editor_link_dto_v2 import WebEditorLinkDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get Web Editor URL
        api_response = api_instance.web_editor_link_v2(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->web_editor_link_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = CreateWebEditorLinkDtoV2(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
    )
    try:
        # Get Web Editor URL
        api_response = api_instance.web_editor_link_v2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->web_editor_link_v2: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBody, Unset]        | optional, default is unset |
| path_params          | RequestPathParams                                |                            |
| content_type         | str                                              | optional, default is '_/_' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                | default is ('_/_', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False           | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None            | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False           | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBody

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**CreateWebEditorLinkDtoV2**](../../models/CreateWebEditorLinkDtoV2.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#web_editor_link_v2.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#web_editor_link_v2.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#web_editor_link_v2.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#web_editor_link_v2.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#web_editor_link_v2.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#web_editor_link_v2.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#web_editor_link_v2.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#web_editor_link_v2.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#web_editor_link_v2.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#web_editor_link_v2.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#web_editor_link_v2.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#web_editor_link_v2.ApiResponseFor501) | Not implemented                                             |

#### web_editor_link_v2.ApiResponseFor200

| Name     | Type                                     | Description              | Notes |
| -------- | ---------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                     | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBody, ] |                          |
| headers  | Unset                                    | headers were not defined |

# SchemaFor200ResponseBody

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**WebEditorLinkDtoV2**](../../models/WebEditorLinkDtoV2.md) |             |

#### web_editor_link_v2.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### web_editor_link_v2.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### web_editor_link_v2.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### web_editor_link_v2.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### web_editor_link_v2.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### web_editor_link_v2.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### web_editor_link_v2.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### web_editor_link_v2.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### web_editor_link_v2.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### web_editor_link_v2.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### web_editor_link_v2.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wild_card_search_by_job3**

<a id="wild_card_search_by_job3"></a>

> SearchResponseListTmDtoV3 wild_card_search_by_job3(project_uidjob_uid)

Wildcard search job's translation memories

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import job_api
from phrasetms_client.model.search_response_list_tm_dto_v3 import SearchResponseListTmDtoV3
from phrasetms_client.model.wild_card_search_by_job_request_dto_v3 import WildCardSearchByJobRequestDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Wildcard search job's translation memories
        api_response = api_instance.wild_card_search_by_job3(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->wild_card_search_by_job3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = WildCardSearchByJobRequestDtoV3(
        query="query_example",
        reverse=True,
        count=1,
        offset=1,
    )
    try:
        # Wildcard search job's translation memories
        api_response = api_instance.wild_card_search_by_job3(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling JobApi->wild_card_search_by_job3: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**WildCardSearchByJobRequestDtoV3**](../../models/WildCardSearchByJobRequestDtoV3.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                            | Description                                                 |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                     | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#wild_card_search_by_job3.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#wild_card_search_by_job3.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#wild_card_search_by_job3.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#wild_card_search_by_job3.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#wild_card_search_by_job3.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#wild_card_search_by_job3.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#wild_card_search_by_job3.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#wild_card_search_by_job3.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#wild_card_search_by_job3.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#wild_card_search_by_job3.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#wild_card_search_by_job3.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#wild_card_search_by_job3.ApiResponseFor501) | Not implemented                                             |

#### wild_card_search_by_job3.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**SearchResponseListTmDtoV3**](../../models/SearchResponseListTmDtoV3.md) |             |

#### wild_card_search_by_job3.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
