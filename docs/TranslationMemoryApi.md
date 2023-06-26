# phrasetms_client.TranslationMemoryApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_target_lang_to_trans_memory**](TranslationMemoryApi.md#add_target_lang_to_trans_memory) | **POST** /api2/v1/transMemories/{transMemoryUid}/targetLanguages | Add target language to translation memory
[**clear_trans_memory**](TranslationMemoryApi.md#clear_trans_memory) | **DELETE** /api2/v1/transMemories/{transMemoryUid}/segments | Delete all segments
[**clear_trans_memory_v2**](TranslationMemoryApi.md#clear_trans_memory_v2) | **DELETE** /api2/v2/transMemories/{transMemoryUid}/segments | Delete all segments.
[**create_trans_memory**](TranslationMemoryApi.md#create_trans_memory) | **POST** /api2/v1/transMemories | Create translation memory
[**delete_source_and_translations**](TranslationMemoryApi.md#delete_source_and_translations) | **DELETE** /api2/v1/transMemories/{transMemoryUid}/segments/{segmentId} | Delete both source and translation
[**delete_trans_memory**](TranslationMemoryApi.md#delete_trans_memory) | **DELETE** /api2/v1/transMemories/{transMemoryUid} | Delete translation memory
[**delete_translation**](TranslationMemoryApi.md#delete_translation) | **DELETE** /api2/v1/transMemories/{transMemoryUid}/segments/{segmentId}/lang/{lang} | Delete segment of given language
[**download_cleaned_tm**](TranslationMemoryApi.md#download_cleaned_tm) | **GET** /api2/v1/transMemories/downloadCleaned/{asyncRequestId} | Download cleaned TM
[**download_search_result**](TranslationMemoryApi.md#download_search_result) | **GET** /api2/v1/transMemories/downloadExport/{asyncRequestId} | Download export
[**edit_trans_memory**](TranslationMemoryApi.md#edit_trans_memory) | **PUT** /api2/v1/transMemories/{transMemoryUid} | Edit translation memory
[**export_by_query_async**](TranslationMemoryApi.md#export_by_query_async) | **POST** /api2/v1/transMemories/{transMemoryUid}/exportByQueryAsync | Search translation memory
[**export_cleaned_tms**](TranslationMemoryApi.md#export_cleaned_tms) | **POST** /api2/v1/transMemories/extractCleaned | Extract cleaned translation memory
[**export_v2**](TranslationMemoryApi.md#export_v2) | **POST** /api2/v2/transMemories/{transMemoryUid}/export | Export translation memory
[**get_background_tasks1**](TranslationMemoryApi.md#get_background_tasks1) | **GET** /api2/v1/transMemories/{transMemoryUid}/lastBackgroundTask | Get last task information
[**get_metadata**](TranslationMemoryApi.md#get_metadata) | **GET** /api2/v1/transMemories/{transMemoryUid}/metadata | Get translation memory metadata
[**get_project_template_trans_memories2**](TranslationMemoryApi.md#get_project_template_trans_memories2) | **GET** /api2/v3/projectTemplates/{projectTemplateUid}/transMemories | Get translation memories
[**get_related_projects**](TranslationMemoryApi.md#get_related_projects) | **GET** /api2/v1/transMemories/{transMemoryUid}/relatedProjects | List related projects
[**get_trans_memory**](TranslationMemoryApi.md#get_trans_memory) | **GET** /api2/v1/transMemories/{transMemoryUid} | Get translation memory
[**get_translation_resources**](TranslationMemoryApi.md#get_translation_resources) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources | Get translation resources
[**import_trans_memory_v2**](TranslationMemoryApi.md#import_trans_memory_v2) | **POST** /api2/v2/transMemories/{transMemoryUid}/import | Import TMX
[**insert_to_trans_memory**](TranslationMemoryApi.md#insert_to_trans_memory) | **POST** /api2/v1/transMemories/{transMemoryUid}/segments | Insert segment
[**list_trans_memories**](TranslationMemoryApi.md#list_trans_memories) | **GET** /api2/v1/transMemories | List translation memories
[**relevant_trans_memories**](TranslationMemoryApi.md#relevant_trans_memories) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/transMemories/relevant | List project template relevant translation memories
[**relevant_trans_memories1**](TranslationMemoryApi.md#relevant_trans_memories1) | **GET** /api2/v1/projects/{projectUid}/transMemories/relevant | List project relevant translation memories
[**search**](TranslationMemoryApi.md#search) | **POST** /api2/v1/transMemories/{transMemoryUid}/search | Search translation memory (sync)
[**search_by_job3**](TranslationMemoryApi.md#search_by_job3) | **POST** /api2/v3/projects/{projectUid}/jobs/{jobUid}/transMemories/search | Search job&#39;s translation memories
[**search_segment1**](TranslationMemoryApi.md#search_segment1) | **POST** /api2/v1/projects/{projectUid}/transMemories/searchSegmentInProject | Search translation memory for segment in the project
[**search_segment_by_job**](TranslationMemoryApi.md#search_segment_by_job) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/transMemories/searchSegment | Search translation memory for segment by job
[**update_translation**](TranslationMemoryApi.md#update_translation) | **PUT** /api2/v1/transMemories/{transMemoryUid}/segments/{segmentId} | Edit segment
[**wild_card_search_by_job3**](TranslationMemoryApi.md#wild_card_search_by_job3) | **POST** /api2/v3/projects/{projectUid}/jobs/{jobUid}/transMemories/wildCardSearch | Wildcard search job&#39;s translation memories
[**wildcard_search**](TranslationMemoryApi.md#wildcard_search) | **POST** /api2/v1/transMemories/{transMemoryUid}/wildCardSearch | Wildcard search


# **add_target_lang_to_trans_memory**
> TransMemoryDto add_target_lang_to_trans_memory(trans_memory_uid, body=body)

Add target language to translation memory

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.target_language_dto import TargetLanguageDto
from phrasetms_client.models.trans_memory_dto import TransMemoryDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    body = phrasetms_client.TargetLanguageDto() # TargetLanguageDto |  (optional)

    try:
        # Add target language to translation memory
        api_response = api_instance.add_target_lang_to_trans_memory(trans_memory_uid, body=body)
        print("The response of TranslationMemoryApi->add_target_lang_to_trans_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->add_target_lang_to_trans_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **body** | [**TargetLanguageDto**](TargetLanguageDto.md)|  | [optional] 

### Return type

[**TransMemoryDto**](TransMemoryDto.md)

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

# **clear_trans_memory**
> clear_trans_memory(trans_memory_uid)

Delete all segments

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 

    try:
        # Delete all segments
        api_instance.clear_trans_memory(trans_memory_uid)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->clear_trans_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 

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

# **clear_trans_memory_v2**
> clear_trans_memory_v2(trans_memory_uid)

Delete all segments.

This call is **asynchronous**, use [this API](#operation/getAsyncRequest) to check the result

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 

    try:
        # Delete all segments.
        api_instance.clear_trans_memory_v2(trans_memory_uid)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->clear_trans_memory_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 

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

# **create_trans_memory**
> TransMemoryDto create_trans_memory(body=body)

Create translation memory

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.trans_memory_create_dto import TransMemoryCreateDto
from phrasetms_client.models.trans_memory_dto import TransMemoryDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    body = phrasetms_client.TransMemoryCreateDto() # TransMemoryCreateDto |  (optional)

    try:
        # Create translation memory
        api_response = api_instance.create_trans_memory(body=body)
        print("The response of TranslationMemoryApi->create_trans_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->create_trans_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransMemoryCreateDto**](TransMemoryCreateDto.md)|  | [optional] 

### Return type

[**TransMemoryDto**](TransMemoryDto.md)

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

# **delete_source_and_translations**
> delete_source_and_translations(trans_memory_uid, segment_id)

Delete both source and translation

Not recommended for bulk removal of segments

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    segment_id = 'segment_id_example' # str | 

    try:
        # Delete both source and translation
        api_instance.delete_source_and_translations(trans_memory_uid, segment_id)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->delete_source_and_translations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **segment_id** | **str**|  | 

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

# **delete_trans_memory**
> delete_trans_memory(trans_memory_uid, purge=purge)

Delete translation memory

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    purge = False # bool |  (optional) (default to False)

    try:
        # Delete translation memory
        api_instance.delete_trans_memory(trans_memory_uid, purge=purge)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->delete_trans_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **purge** | **bool**|  | [optional] [default to False]

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

# **delete_translation**
> delete_translation(trans_memory_uid, segment_id, lang)

Delete segment of given language

Not recommended for bulk removal of segments

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    segment_id = 'segment_id_example' # str | 
    lang = 'lang_example' # str | 

    try:
        # Delete segment of given language
        api_instance.delete_translation(trans_memory_uid, segment_id, lang)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->delete_translation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **segment_id** | **str**|  | 
 **lang** | **str**|  | 

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

# **download_cleaned_tm**
> download_cleaned_tm(async_request_id)

Download cleaned TM

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    async_request_id = 'async_request_id_example' # str | Request ID

    try:
        # Download cleaned TM
        api_instance.download_cleaned_tm(async_request_id)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->download_cleaned_tm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_request_id** | **str**| Request ID | 

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
**200** | application/octet-stream |  -  |
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

# **download_search_result**
> download_search_result(async_request_id, format=format, fields=fields)

Download export

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    async_request_id = 'async_request_id_example' # str | Request ID
    format = 'TMX' # str |  (optional) (default to 'TMX')
    fields = ['fields_example'] # List[str] | Fields to include in exported XLSX (optional)

    try:
        # Download export
        api_instance.download_search_result(async_request_id, format=format, fields=fields)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->download_search_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_request_id** | **str**| Request ID | 
 **format** | **str**|  | [optional] [default to &#39;TMX&#39;]
 **fields** | [**List[str]**](str.md)| Fields to include in exported XLSX | [optional] 

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
**200** | application/octet-stream |  -  |
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

# **edit_trans_memory**
> TransMemoryDto edit_trans_memory(trans_memory_uid, body=body)

Edit translation memory

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.trans_memory_dto import TransMemoryDto
from phrasetms_client.models.trans_memory_edit_dto import TransMemoryEditDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    body = phrasetms_client.TransMemoryEditDto() # TransMemoryEditDto |  (optional)

    try:
        # Edit translation memory
        api_response = api_instance.edit_trans_memory(trans_memory_uid, body=body)
        print("The response of TranslationMemoryApi->edit_trans_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->edit_trans_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **body** | [**TransMemoryEditDto**](TransMemoryEditDto.md)|  | [optional] 

### Return type

[**TransMemoryDto**](TransMemoryDto.md)

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

# **export_by_query_async**
> AsyncExportTMByQueryResponseDto export_by_query_async(trans_memory_uid, body=body)

Search translation memory

Use [this API](#operation/downloadSearchResult) to download result

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_export_tmby_query_response_dto import AsyncExportTMByQueryResponseDto
from phrasetms_client.models.export_by_query_dto import ExportByQueryDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    body = phrasetms_client.ExportByQueryDto() # ExportByQueryDto |  (optional)

    try:
        # Search translation memory
        api_response = api_instance.export_by_query_async(trans_memory_uid, body=body)
        print("The response of TranslationMemoryApi->export_by_query_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->export_by_query_async: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **body** | [**ExportByQueryDto**](ExportByQueryDto.md)|  | [optional] 

### Return type

[**AsyncExportTMByQueryResponseDto**](AsyncExportTMByQueryResponseDto.md)

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

# **export_cleaned_tms**
> AsyncRequestWrapperDto export_cleaned_tms(body=body)

Extract cleaned translation memory

Returns a ZIP file containing the cleaned translation memories in the specified outputFormat.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_request_wrapper_dto import AsyncRequestWrapperDto
from phrasetms_client.models.cleaned_trans_memories_dto import CleanedTransMemoriesDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    body = phrasetms_client.CleanedTransMemoriesDto() # CleanedTransMemoriesDto |  (optional)

    try:
        # Extract cleaned translation memory
        api_response = api_instance.export_cleaned_tms(body=body)
        print("The response of TranslationMemoryApi->export_cleaned_tms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->export_cleaned_tms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CleanedTransMemoriesDto**](CleanedTransMemoriesDto.md)|  | [optional] 

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
**202** | successful operation |  -  |
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

# **export_v2**
> AsyncExportTMResponseDto export_v2(trans_memory_uid, body=body)

Export translation memory

Use [this API](#operation/downloadSearchResult) to download result

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_export_tm_response_dto import AsyncExportTMResponseDto
from phrasetms_client.models.export_tm_dto import ExportTMDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    body = phrasetms_client.ExportTMDto() # ExportTMDto |  (optional)

    try:
        # Export translation memory
        api_response = api_instance.export_v2(trans_memory_uid, body=body)
        print("The response of TranslationMemoryApi->export_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->export_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **body** | [**ExportTMDto**](ExportTMDto.md)|  | [optional] 

### Return type

[**AsyncExportTMResponseDto**](AsyncExportTMResponseDto.md)

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

# **get_background_tasks1**
> BackgroundTasksTmDto get_background_tasks1(trans_memory_uid)

Get last task information

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.background_tasks_tm_dto import BackgroundTasksTmDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 

    try:
        # Get last task information
        api_response = api_instance.get_background_tasks1(trans_memory_uid)
        print("The response of TranslationMemoryApi->get_background_tasks1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->get_background_tasks1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 

### Return type

[**BackgroundTasksTmDto**](BackgroundTasksTmDto.md)

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

# **get_metadata**
> MetadataResponse get_metadata(trans_memory_uid, by_language=by_language)

Get translation memory metadata

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.metadata_response import MetadataResponse
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    by_language = False # bool |  (optional) (default to False)

    try:
        # Get translation memory metadata
        api_response = api_instance.get_metadata(trans_memory_uid, by_language=by_language)
        print("The response of TranslationMemoryApi->get_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->get_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **by_language** | **bool**|  | [optional] [default to False]

### Return type

[**MetadataResponse**](MetadataResponse.md)

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    target_lang = 'target_lang_example' # str | Filter project translation memories by target language (optional)
    wf_step_uid = 'wf_step_uid_example' # str | Filter project translation memories by workflow step (optional)

    try:
        # Get translation memories
        api_response = api_instance.get_project_template_trans_memories2(project_template_uid, target_lang=target_lang, wf_step_uid=wf_step_uid)
        print("The response of TranslationMemoryApi->get_project_template_trans_memories2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->get_project_template_trans_memories2: %s\n" % e)
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

# **get_related_projects**
> PageDtoAbstractProjectDto get_related_projects(trans_memory_uid, page_number=page_number, page_size=page_size)

List related projects

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_abstract_project_dto import PageDtoAbstractProjectDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List related projects
        api_response = api_instance.get_related_projects(trans_memory_uid, page_number=page_number, page_size=page_size)
        print("The response of TranslationMemoryApi->get_related_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->get_related_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoAbstractProjectDto**](PageDtoAbstractProjectDto.md)

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

# **get_trans_memory**
> TransMemoryDto get_trans_memory(trans_memory_uid)

Get translation memory

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.trans_memory_dto import TransMemoryDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 

    try:
        # Get translation memory
        api_response = api_instance.get_trans_memory(trans_memory_uid)
        print("The response of TranslationMemoryApi->get_trans_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->get_trans_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 

### Return type

[**TransMemoryDto**](TransMemoryDto.md)

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get translation resources
        api_response = api_instance.get_translation_resources(project_uid, job_uid)
        print("The response of TranslationMemoryApi->get_translation_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->get_translation_resources: %s\n" % e)
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

# **import_trans_memory_v2**
> AsyncRequestWrapperV2Dto import_trans_memory_v2(trans_memory_uid, content_disposition, content_length=content_length, strict_lang_matching=strict_lang_matching, strip_native_codes=strip_native_codes, body=body)

Import TMX

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_request_wrapper_v2_dto import AsyncRequestWrapperV2Dto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    content_disposition = 'content_disposition_example' # str | must match pattern `((inline|attachment); )?filename\\*=UTF-8''(.+)`
    content_length = 56 # int |  (optional)
    strict_lang_matching = False # bool |  (optional) (default to False)
    strip_native_codes = True # bool |  (optional) (default to True)
    body = None # object |  (optional)

    try:
        # Import TMX
        api_response = api_instance.import_trans_memory_v2(trans_memory_uid, content_disposition, content_length=content_length, strict_lang_matching=strict_lang_matching, strip_native_codes=strip_native_codes, body=body)
        print("The response of TranslationMemoryApi->import_trans_memory_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->import_trans_memory_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **content_disposition** | **str**| must match pattern &#x60;((inline|attachment); )?filename\\*&#x3D;UTF-8&#39;&#39;(.+)&#x60; | 
 **content_length** | **int**|  | [optional] 
 **strict_lang_matching** | **bool**|  | [optional] [default to False]
 **strip_native_codes** | **bool**|  | [optional] [default to True]
 **body** | **object**|  | [optional] 

### Return type

[**AsyncRequestWrapperV2Dto**](AsyncRequestWrapperV2Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successful operation |  -  |
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

# **insert_to_trans_memory**
> insert_to_trans_memory(trans_memory_uid, body=body)

Insert segment

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.segment_dto import SegmentDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    body = phrasetms_client.SegmentDto() # SegmentDto |  (optional)

    try:
        # Insert segment
        api_instance.insert_to_trans_memory(trans_memory_uid, body=body)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->insert_to_trans_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **body** | [**SegmentDto**](SegmentDto.md)|  | [optional] 

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

# **list_trans_memories**
> PageDtoTransMemoryDto list_trans_memories(name=name, source_lang=source_lang, target_lang=target_lang, client_id=client_id, domain_id=domain_id, sub_domain_id=sub_domain_id, business_unit_id=business_unit_id, page_number=page_number, page_size=page_size)

List translation memories

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    name = 'name_example' # str |  (optional)
    source_lang = 'source_lang_example' # str |  (optional)
    target_lang = 'target_lang_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)
    domain_id = 'domain_id_example' # str |  (optional)
    sub_domain_id = 'sub_domain_id_example' # str |  (optional)
    business_unit_id = 'business_unit_id_example' # str |  (optional)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List translation memories
        api_response = api_instance.list_trans_memories(name=name, source_lang=source_lang, target_lang=target_lang, client_id=client_id, domain_id=domain_id, sub_domain_id=sub_domain_id, business_unit_id=business_unit_id, page_number=page_number, page_size=page_size)
        print("The response of TranslationMemoryApi->list_trans_memories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->list_trans_memories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **source_lang** | **str**|  | [optional] 
 **target_lang** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **domain_id** | **str**|  | [optional] 
 **sub_domain_id** | **str**|  | [optional] 
 **business_unit_id** | **str**|  | [optional] 
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
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
        print("The response of TranslationMemoryApi->relevant_trans_memories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->relevant_trans_memories: %s\n" % e)
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

# **relevant_trans_memories1**
> PageDtoTransMemoryDto relevant_trans_memories1(project_uid, name=name, domain_name=domain_name, client_name=client_name, sub_domain_name=sub_domain_name, target_langs=target_langs, strict_lang_matching=strict_lang_matching, page_number=page_number, page_size=page_size)

List project relevant translation memories

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    project_uid = 'project_uid_example' # str | 
    name = 'name_example' # str |  (optional)
    domain_name = 'domain_name_example' # str |  (optional)
    client_name = 'client_name_example' # str |  (optional)
    sub_domain_name = 'sub_domain_name_example' # str |  (optional)
    target_langs = ['target_langs_example'] # List[str] |  (optional)
    strict_lang_matching = False # bool |  (optional) (default to False)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List project relevant translation memories
        api_response = api_instance.relevant_trans_memories1(project_uid, name=name, domain_name=domain_name, client_name=client_name, sub_domain_name=sub_domain_name, target_langs=target_langs, strict_lang_matching=strict_lang_matching, page_number=page_number, page_size=page_size)
        print("The response of TranslationMemoryApi->relevant_trans_memories1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->relevant_trans_memories1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
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

# **search**
> SearchResponseListTmDto search(trans_memory_uid, body=body)

Search translation memory (sync)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.search_request_dto import SearchRequestDto
from phrasetms_client.models.search_response_list_tm_dto import SearchResponseListTmDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    body = phrasetms_client.SearchRequestDto() # SearchRequestDto |  (optional)

    try:
        # Search translation memory (sync)
        api_response = api_instance.search(trans_memory_uid, body=body)
        print("The response of TranslationMemoryApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **body** | [**SearchRequestDto**](SearchRequestDto.md)|  | [optional] 

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.SearchTMByJobRequestDtoV3() # SearchTMByJobRequestDtoV3 |  (optional)

    try:
        # Search job's translation memories
        api_response = api_instance.search_by_job3(project_uid, job_uid, body=body)
        print("The response of TranslationMemoryApi->search_by_job3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->search_by_job3: %s\n" % e)
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

# **search_segment1**
> SearchResponseListTmDto search_segment1(project_uid, body=body)

Search translation memory for segment in the project

Returns at most <i>maxSegments</i>             records with <i>score >= scoreThreshold</i> and at most <i>maxSubsegments</i> records which are subsegment,             i.e. the source text is substring of the query text.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.search_response_list_tm_dto import SearchResponseListTmDto
from phrasetms_client.models.search_tm_request_dto import SearchTMRequestDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.SearchTMRequestDto() # SearchTMRequestDto |  (optional)

    try:
        # Search translation memory for segment in the project
        api_response = api_instance.search_segment1(project_uid, body=body)
        print("The response of TranslationMemoryApi->search_segment1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->search_segment1: %s\n" % e)
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.SearchTMByJobRequestDto() # SearchTMByJobRequestDto |  (optional)

    try:
        # Search translation memory for segment by job
        api_response = api_instance.search_segment_by_job(project_uid, job_uid, body=body)
        print("The response of TranslationMemoryApi->search_segment_by_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->search_segment_by_job: %s\n" % e)
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

# **update_translation**
> update_translation(trans_memory_uid, segment_id, body=body)

Edit segment

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.translation_dto import TranslationDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    segment_id = 'segment_id_example' # str | 
    body = phrasetms_client.TranslationDto() # TranslationDto |  (optional)

    try:
        # Edit segment
        api_instance.update_translation(trans_memory_uid, segment_id, body=body)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->update_translation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **segment_id** | **str**|  | 
 **body** | [**TranslationDto**](TranslationDto.md)|  | [optional] 

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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.WildCardSearchByJobRequestDtoV3() # WildCardSearchByJobRequestDtoV3 |  (optional)

    try:
        # Wildcard search job's translation memories
        api_response = api_instance.wild_card_search_by_job3(project_uid, job_uid, body=body)
        print("The response of TranslationMemoryApi->wild_card_search_by_job3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->wild_card_search_by_job3: %s\n" % e)
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

# **wildcard_search**
> SearchResponseListTmDto wildcard_search(trans_memory_uid, body=body)

Wildcard search

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.search_response_list_tm_dto import SearchResponseListTmDto
from phrasetms_client.models.wild_card_search_request_dto import WildCardSearchRequestDto
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
    api_instance = phrasetms_client.TranslationMemoryApi(api_client)
    trans_memory_uid = 'trans_memory_uid_example' # str | 
    body = phrasetms_client.WildCardSearchRequestDto() # WildCardSearchRequestDto |  (optional)

    try:
        # Wildcard search
        api_response = api_instance.wildcard_search(trans_memory_uid, body=body)
        print("The response of TranslationMemoryApi->wildcard_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationMemoryApi->wildcard_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_uid** | **str**|  | 
 **body** | [**WildCardSearchRequestDto**](WildCardSearchRequestDto.md)|  | [optional] 

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

