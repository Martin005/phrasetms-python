# phrasetms_client.TranslationApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**human_translate**](TranslationApi.md#human_translate) | **POST** /api2/v1/projects/{projectUid}/jobs/humanTranslate | Human translate (Gengo or Unbabel)
[**machine_translation_job**](TranslationApi.md#machine_translation_job) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translations/translateWithMachineTranslation | Translate using machine translation
[**pre_translate1**](TranslationApi.md#pre_translate1) | **POST** /api2/v2/projects/{projectUid}/jobs/preTranslate | Pre-translate job


# **human_translate**
> AsyncRequestWrapperDto human_translate(project_uid, body=body)

Human translate (Gengo or Unbabel)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_request_wrapper_dto import AsyncRequestWrapperDto
from phrasetms_client.models.human_translate_jobs_dto import HumanTranslateJobsDto
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
    api_instance = phrasetms_client.TranslationApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.HumanTranslateJobsDto() # HumanTranslateJobsDto |  (optional)

    try:
        # Human translate (Gengo or Unbabel)
        api_response = api_instance.human_translate(project_uid, body=body)
        print("The response of TranslationApi->human_translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->human_translate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**HumanTranslateJobsDto**](HumanTranslateJobsDto.md)|  | [optional] 

### Return type

[**AsyncRequestWrapperDto**](AsyncRequestWrapperDto.md)

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

# **machine_translation_job**
> MachineTranslateResponse machine_translation_job(project_uid, job_uid, body=body)

Translate using machine translation

Configured machine translate settings is used

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.machine_translate_response import MachineTranslateResponse
from phrasetms_client.models.translation_request_dto import TranslationRequestDto
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
    api_instance = phrasetms_client.TranslationApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.TranslationRequestDto() # TranslationRequestDto |  (optional)

    try:
        # Translate using machine translation
        api_response = api_instance.machine_translation_job(project_uid, job_uid, body=body)
        print("The response of TranslationApi->machine_translation_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->machine_translation_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**TranslationRequestDto**](TranslationRequestDto.md)|  | [optional] 

### Return type

[**MachineTranslateResponse**](MachineTranslateResponse.md)

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

# **pre_translate1**
> AsyncRequestWrapperV2Dto pre_translate1(project_uid, body=body)

Pre-translate job

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_request_wrapper_v2_dto import AsyncRequestWrapperV2Dto
from phrasetms_client.models.pre_translate_jobs_v2_dto import PreTranslateJobsV2Dto
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
    api_instance = phrasetms_client.TranslationApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.PreTranslateJobsV2Dto() # PreTranslateJobsV2Dto |  (optional)

    try:
        # Pre-translate job
        api_response = api_instance.pre_translate1(project_uid, body=body)
        print("The response of TranslationApi->pre_translate1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->pre_translate1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**PreTranslateJobsV2Dto**](PreTranslateJobsV2Dto.md)|  | [optional] 

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

