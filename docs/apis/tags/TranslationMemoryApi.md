<a id="__pageTop"></a>
# openapi_client.apis.tags.translation_memory_api.TranslationMemoryApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_target_lang_to_trans_memory**](#add_target_lang_to_trans_memory) | **post** /api2/v1/transMemories/{transMemoryUid}/targetLanguages | Add target language to translation memory
[**clear_trans_memory**](#clear_trans_memory) | **delete** /api2/v1/transMemories/{transMemoryUid}/segments | Delete all segments
[**clear_trans_memory_v2**](#clear_trans_memory_v2) | **delete** /api2/v2/transMemories/{transMemoryUid}/segments | Delete all segments.
[**create_trans_memory**](#create_trans_memory) | **post** /api2/v1/transMemories | Create translation memory
[**delete_source_and_translations**](#delete_source_and_translations) | **delete** /api2/v1/transMemories/{transMemoryUid}/segments/{segmentId} | Delete both source and translation
[**delete_trans_memory**](#delete_trans_memory) | **delete** /api2/v1/transMemories/{transMemoryUid} | Delete translation memory
[**delete_translation**](#delete_translation) | **delete** /api2/v1/transMemories/{transMemoryUid}/segments/{segmentId}/lang/{lang} | Delete segment of given language
[**download_cleaned_tm**](#download_cleaned_tm) | **get** /api2/v1/transMemories/downloadCleaned/{asyncRequestId} | Download cleaned TM
[**download_search_result**](#download_search_result) | **get** /api2/v1/transMemories/downloadExport/{asyncRequestId} | Download export
[**edit_trans_memory**](#edit_trans_memory) | **put** /api2/v1/transMemories/{transMemoryUid} | Edit translation memory
[**export_by_query_async**](#export_by_query_async) | **post** /api2/v1/transMemories/{transMemoryUid}/exportByQueryAsync | Search translation memory
[**export_cleaned_tms**](#export_cleaned_tms) | **post** /api2/v1/transMemories/extractCleaned | Extract cleaned translation memory
[**export_v2**](#export_v2) | **post** /api2/v2/transMemories/{transMemoryUid}/export | Export translation memory
[**get_background_tasks1**](#get_background_tasks1) | **get** /api2/v1/transMemories/{transMemoryUid}/lastBackgroundTask | Get last task information
[**get_metadata**](#get_metadata) | **get** /api2/v1/transMemories/{transMemoryUid}/metadata | Get translation memory metadata
[**get_project_template_trans_memories2**](#get_project_template_trans_memories2) | **get** /api2/v3/projectTemplates/{projectTemplateUid}/transMemories | Get translation memories
[**get_related_projects**](#get_related_projects) | **get** /api2/v1/transMemories/{transMemoryUid}/relatedProjects | List related projects
[**get_trans_memory**](#get_trans_memory) | **get** /api2/v1/transMemories/{transMemoryUid} | Get translation memory
[**get_translation_resources**](#get_translation_resources) | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources | Get translation resources
[**import_trans_memory_v2**](#import_trans_memory_v2) | **post** /api2/v2/transMemories/{transMemoryUid}/import | Import TMX
[**insert_to_trans_memory**](#insert_to_trans_memory) | **post** /api2/v1/transMemories/{transMemoryUid}/segments | Insert segment
[**list_trans_memories**](#list_trans_memories) | **get** /api2/v1/transMemories | List translation memories
[**relevant_trans_memories**](#relevant_trans_memories) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/transMemories/relevant | List project template relevant translation memories
[**relevant_trans_memories1**](#relevant_trans_memories1) | **get** /api2/v1/projects/{projectUid}/transMemories/relevant | List project relevant translation memories
[**search**](#search) | **post** /api2/v1/transMemories/{transMemoryUid}/search | Search translation memory (sync)
[**search_by_job3**](#search_by_job3) | **post** /api2/v3/projects/{projectUid}/jobs/{jobUid}/transMemories/search | Search job&#x27;s translation memories
[**search_segment1**](#search_segment1) | **post** /api2/v1/projects/{projectUid}/transMemories/searchSegmentInProject | Search translation memory for segment in the project
[**search_segment_by_job**](#search_segment_by_job) | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/transMemories/searchSegment | Search translation memory for segment by job
[**update_translation**](#update_translation) | **put** /api2/v1/transMemories/{transMemoryUid}/segments/{segmentId} | Edit segment
[**wild_card_search_by_job3**](#wild_card_search_by_job3) | **post** /api2/v3/projects/{projectUid}/jobs/{jobUid}/transMemories/wildCardSearch | Wildcard search job&#x27;s translation memories
[**wildcard_search**](#wildcard_search) | **post** /api2/v1/transMemories/{transMemoryUid}/wildCardSearch | Wildcard search

# **add_target_lang_to_trans_memory**
<a id="add_target_lang_to_trans_memory"></a>
> TransMemoryDto add_target_lang_to_trans_memory(trans_memory_uid)

Add target language to translation memory

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.target_language_dto import TargetLanguageDto
from openapi_client.model.trans_memory_dto import TransMemoryDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Add target language to translation memory
        api_response = api_instance.add_target_lang_to_trans_memory(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->add_target_lang_to_trans_memory: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    body = TargetLanguageDto(
        language="language_example",
    )
    try:
        # Add target language to translation memory
        api_response = api_instance.add_target_lang_to_trans_memory(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->add_target_lang_to_trans_memory: %s\n" % e)
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
[**TargetLanguageDto**](../../models/TargetLanguageDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#add_target_lang_to_trans_memory.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#add_target_lang_to_trans_memory.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#add_target_lang_to_trans_memory.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#add_target_lang_to_trans_memory.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#add_target_lang_to_trans_memory.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#add_target_lang_to_trans_memory.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#add_target_lang_to_trans_memory.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#add_target_lang_to_trans_memory.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#add_target_lang_to_trans_memory.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#add_target_lang_to_trans_memory.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#add_target_lang_to_trans_memory.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#add_target_lang_to_trans_memory.ApiResponseFor501) | Not implemented

#### add_target_lang_to_trans_memory.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransMemoryDto**](../../models/TransMemoryDto.md) |  | 


#### add_target_lang_to_trans_memory.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_lang_to_trans_memory.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_lang_to_trans_memory.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_lang_to_trans_memory.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_lang_to_trans_memory.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_lang_to_trans_memory.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_lang_to_trans_memory.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_lang_to_trans_memory.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_lang_to_trans_memory.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_lang_to_trans_memory.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_target_lang_to_trans_memory.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **clear_trans_memory**
<a id="clear_trans_memory"></a>
> clear_trans_memory(trans_memory_uid)

Delete all segments

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Delete all segments
        api_response = api_instance.clear_trans_memory(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->clear_trans_memory: %s\n" % e)
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
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#clear_trans_memory.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#clear_trans_memory.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#clear_trans_memory.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#clear_trans_memory.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#clear_trans_memory.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#clear_trans_memory.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#clear_trans_memory.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#clear_trans_memory.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#clear_trans_memory.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#clear_trans_memory.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#clear_trans_memory.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#clear_trans_memory.ApiResponseFor501) | Not implemented

#### clear_trans_memory.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **clear_trans_memory_v2**
<a id="clear_trans_memory_v2"></a>
> clear_trans_memory_v2(trans_memory_uid)

Delete all segments.

This call is **asynchronous**, use [this API](#operation/getAsyncRequest) to check the result

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Delete all segments.
        api_response = api_instance.clear_trans_memory_v2(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->clear_trans_memory_v2: %s\n" % e)
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
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#clear_trans_memory_v2.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#clear_trans_memory_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#clear_trans_memory_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#clear_trans_memory_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#clear_trans_memory_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#clear_trans_memory_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#clear_trans_memory_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#clear_trans_memory_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#clear_trans_memory_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#clear_trans_memory_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#clear_trans_memory_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#clear_trans_memory_v2.ApiResponseFor501) | Not implemented

#### clear_trans_memory_v2.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_trans_memory_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_trans_memory**
<a id="create_trans_memory"></a>
> TransMemoryDto create_trans_memory()

Create translation memory

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.trans_memory_dto import TransMemoryDto
from openapi_client.model.trans_memory_create_dto import TransMemoryCreateDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only optional values
    body = TransMemoryCreateDto(
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
        note="note_example",
    )
    try:
        # Create translation memory
        api_response = api_instance.create_trans_memory(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->create_trans_memory: %s\n" % e)
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
[**TransMemoryCreateDto**](../../models/TransMemoryCreateDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_trans_memory.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_trans_memory.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_trans_memory.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_trans_memory.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_trans_memory.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_trans_memory.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_trans_memory.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_trans_memory.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_trans_memory.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_trans_memory.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_trans_memory.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_trans_memory.ApiResponseFor501) | Not implemented

#### create_trans_memory.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransMemoryDto**](../../models/TransMemoryDto.md) |  | 


#### create_trans_memory.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_trans_memory.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_trans_memory.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_trans_memory.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_trans_memory.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_trans_memory.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_trans_memory.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_trans_memory.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_trans_memory.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_trans_memory.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_trans_memory.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_source_and_translations**
<a id="delete_source_and_translations"></a>
> delete_source_and_translations(trans_memory_uidsegment_id)

Delete both source and translation

Not recommended for bulk removal of segments

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
        'segmentId': "segmentId_example",
    }
    try:
        # Delete both source and translation
        api_response = api_instance.delete_source_and_translations(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->delete_source_and_translations: %s\n" % e)
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
transMemoryUid | TransMemoryUidSchema | | 
segmentId | SegmentIdSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SegmentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_source_and_translations.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_source_and_translations.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_source_and_translations.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_source_and_translations.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_source_and_translations.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_source_and_translations.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_source_and_translations.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_source_and_translations.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_source_and_translations.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_source_and_translations.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_source_and_translations.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_source_and_translations.ApiResponseFor501) | Not implemented

#### delete_source_and_translations.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_source_and_translations.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_trans_memory**
<a id="delete_trans_memory"></a>
> delete_trans_memory(trans_memory_uid)

Delete translation memory

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    query_params = {
    }
    try:
        # Delete translation memory
        api_response = api_instance.delete_trans_memory(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->delete_trans_memory: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    query_params = {
        'purge': False,
    }
    try:
        # Delete translation memory
        api_response = api_instance.delete_trans_memory(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->delete_trans_memory: %s\n" % e)
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
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_trans_memory.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_trans_memory.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_trans_memory.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_trans_memory.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_trans_memory.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_trans_memory.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_trans_memory.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_trans_memory.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_trans_memory.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_trans_memory.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_trans_memory.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_trans_memory.ApiResponseFor501) | Not implemented

#### delete_trans_memory.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_trans_memory.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_translation**
<a id="delete_translation"></a>
> delete_translation(trans_memory_uidsegment_idlang)

Delete segment of given language

Not recommended for bulk removal of segments

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
        'segmentId': "segmentId_example",
        'lang': "lang_example",
    }
    try:
        # Delete segment of given language
        api_response = api_instance.delete_translation(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->delete_translation: %s\n" % e)
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
transMemoryUid | TransMemoryUidSchema | | 
segmentId | SegmentIdSchema | | 
lang | LangSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SegmentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_translation.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_translation.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_translation.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_translation.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_translation.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_translation.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_translation.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_translation.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_translation.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_translation.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_translation.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_translation.ApiResponseFor501) | Not implemented

#### delete_translation.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_translation.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_cleaned_tm**
<a id="download_cleaned_tm"></a>
> download_cleaned_tm(async_request_id)

Download cleaned TM

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'asyncRequestId': "asyncRequestId_example",
    }
    try:
        # Download cleaned TM
        api_response = api_instance.download_cleaned_tm(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->download_cleaned_tm: %s\n" % e)
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
asyncRequestId | AsyncRequestIdSchema | | 

# AsyncRequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#download_cleaned_tm.ApiResponseFor200) | application/octet-stream
400 | [ApiResponseFor400](#download_cleaned_tm.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#download_cleaned_tm.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#download_cleaned_tm.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#download_cleaned_tm.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#download_cleaned_tm.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#download_cleaned_tm.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#download_cleaned_tm.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#download_cleaned_tm.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#download_cleaned_tm.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#download_cleaned_tm.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#download_cleaned_tm.ApiResponseFor501) | Not implemented

#### download_cleaned_tm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_cleaned_tm.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_search_result**
<a id="download_search_result"></a>
> download_search_result(async_request_id)

Download export

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'asyncRequestId': "asyncRequestId_example",
    }
    query_params = {
    }
    try:
        # Download export
        api_response = api_instance.download_search_result(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->download_search_result: %s\n" % e)

    # example passing only optional values
    path_params = {
        'asyncRequestId': "asyncRequestId_example",
    }
    query_params = {
        'format': "TMX",
        'fields': [
        "ID"
    ],
    }
    try:
        # Download export
        api_response = api_instance.download_search_result(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->download_search_result: %s\n" % e)
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
format | FormatSchema | | optional
fields | FieldsSchema | | optional


# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["TMX", "XLSX", ] if omitted the server will use the default value of "TMX"

# FieldsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["ID", "TEXT", "PREVIOUS_SEGMENT", "NEXT_SEGMENT", "CONTEXT_KEY", "CREATED_BY", "CREATED_AT", "MODIFIED_BY", "MODIFIED_AT", "CLIENT", "PROJECT", "DOMAIN", "SUBDOMAIN", "NOTE", "REVIEWED", "ALIGNED", "FILENAME", "METADATA", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asyncRequestId | AsyncRequestIdSchema | | 

# AsyncRequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#download_search_result.ApiResponseFor200) | application/octet-stream
400 | [ApiResponseFor400](#download_search_result.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#download_search_result.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#download_search_result.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#download_search_result.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#download_search_result.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#download_search_result.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#download_search_result.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#download_search_result.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#download_search_result.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#download_search_result.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#download_search_result.ApiResponseFor501) | Not implemented

#### download_search_result.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_search_result.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_trans_memory**
<a id="edit_trans_memory"></a>
> TransMemoryDto edit_trans_memory(trans_memory_uid)

Edit translation memory

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.trans_memory_dto import TransMemoryDto
from openapi_client.model.trans_memory_edit_dto import TransMemoryEditDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Edit translation memory
        api_response = api_instance.edit_trans_memory(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->edit_trans_memory: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    body = TransMemoryEditDto(
        name="name_example",
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
        note="note_example",
    )
    try:
        # Edit translation memory
        api_response = api_instance.edit_trans_memory(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->edit_trans_memory: %s\n" % e)
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
[**TransMemoryEditDto**](../../models/TransMemoryEditDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_trans_memory.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_trans_memory.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_trans_memory.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_trans_memory.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_trans_memory.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_trans_memory.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_trans_memory.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_trans_memory.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_trans_memory.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_trans_memory.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_trans_memory.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_trans_memory.ApiResponseFor501) | Not implemented

#### edit_trans_memory.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransMemoryDto**](../../models/TransMemoryDto.md) |  | 


#### edit_trans_memory.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_trans_memory.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_trans_memory.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_trans_memory.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_trans_memory.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_trans_memory.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_trans_memory.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_trans_memory.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_trans_memory.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_trans_memory.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_trans_memory.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_by_query_async**
<a id="export_by_query_async"></a>
> AsyncExportTMByQueryResponseDto export_by_query_async(trans_memory_uid)

Search translation memory

Use [this API](#operation/downloadSearchResult) to download result

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.export_by_query_dto import ExportByQueryDto
from openapi_client.model.async_export_tmby_query_response_dto import AsyncExportTMByQueryResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Search translation memory
        api_response = api_instance.export_by_query_async(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->export_by_query_async: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    body = ExportByQueryDto(
        export_target_langs=[
            "export_target_langs_example"
        ],
,
,
        created_at_min="1970-01-01T00:00:00.00Z",
        created_at_max="1970-01-01T00:00:00.00Z",
        modified_at_min="1970-01-01T00:00:00.00Z",
        modified_at_max="1970-01-01T00:00:00.00Z",
        created_by=IdReference(
            id="id_example",
        ),
,
        filename="filename_example",
        project=UidReference(
            uid="uid_example",
        ),
        callback_url="callback_url_example",
    )
    try:
        # Search translation memory
        api_response = api_instance.export_by_query_async(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->export_by_query_async: %s\n" % e)
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
[**ExportByQueryDto**](../../models/ExportByQueryDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_by_query_async.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#export_by_query_async.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_by_query_async.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#export_by_query_async.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#export_by_query_async.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#export_by_query_async.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#export_by_query_async.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#export_by_query_async.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#export_by_query_async.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#export_by_query_async.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#export_by_query_async.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#export_by_query_async.ApiResponseFor501) | Not implemented

#### export_by_query_async.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsyncExportTMByQueryResponseDto**](../../models/AsyncExportTMByQueryResponseDto.md) |  | 


#### export_by_query_async.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_by_query_async.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_by_query_async.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_by_query_async.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_by_query_async.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_by_query_async.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_by_query_async.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_by_query_async.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_by_query_async.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_by_query_async.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_by_query_async.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_cleaned_tms**
<a id="export_cleaned_tms"></a>
> AsyncRequestWrapperDto export_cleaned_tms()

Extract cleaned translation memory

Returns a ZIP file containing the cleaned translation memories in the specified outputFormat.

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.cleaned_trans_memories_dto import CleanedTransMemoriesDto
from openapi_client.model.async_request_wrapper_dto import AsyncRequestWrapperDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only optional values
    body = CleanedTransMemoriesDto(
        uids=[
            "uids_example"
        ],
        output_format="TXT",
        preserve_ratio=0,
,
    )
    try:
        # Extract cleaned translation memory
        api_response = api_instance.export_cleaned_tms(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->export_cleaned_tms: %s\n" % e)
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
[**CleanedTransMemoriesDto**](../../models/CleanedTransMemoriesDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#export_cleaned_tms.ApiResponseFor202) | successful operation
400 | [ApiResponseFor400](#export_cleaned_tms.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_cleaned_tms.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#export_cleaned_tms.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#export_cleaned_tms.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#export_cleaned_tms.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#export_cleaned_tms.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#export_cleaned_tms.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#export_cleaned_tms.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#export_cleaned_tms.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#export_cleaned_tms.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#export_cleaned_tms.ApiResponseFor501) | Not implemented

#### export_cleaned_tms.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsyncRequestWrapperDto**](../../models/AsyncRequestWrapperDto.md) |  | 


#### export_cleaned_tms.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_cleaned_tms.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_cleaned_tms.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_cleaned_tms.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_cleaned_tms.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_cleaned_tms.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_cleaned_tms.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_cleaned_tms.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_cleaned_tms.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_cleaned_tms.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_cleaned_tms.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_v2**
<a id="export_v2"></a>
> AsyncExportTMResponseDto export_v2(trans_memory_uid)

Export translation memory

Use [this API](#operation/downloadSearchResult) to download result

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.async_export_tm_response_dto import AsyncExportTMResponseDto
from openapi_client.model.export_tm_dto import ExportTMDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Export translation memory
        api_response = api_instance.export_v2(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->export_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    body = ExportTMDto(
        export_target_langs=[
            "export_target_langs_example"
        ],
        callback_url="callback_url_example",
    )
    try:
        # Export translation memory
        api_response = api_instance.export_v2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->export_v2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportTMDto**](../../models/ExportTMDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_v2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#export_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#export_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#export_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#export_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#export_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#export_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#export_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#export_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#export_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#export_v2.ApiResponseFor501) | Not implemented

#### export_v2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsyncExportTMResponseDto**](../../models/AsyncExportTMResponseDto.md) |  | 


#### export_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_background_tasks1**
<a id="get_background_tasks1"></a>
> BackgroundTasksTmDto get_background_tasks1(trans_memory_uid)

Get last task information

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.background_tasks_tm_dto import BackgroundTasksTmDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Get last task information
        api_response = api_instance.get_background_tasks1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->get_background_tasks1: %s\n" % e)
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
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_background_tasks1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_background_tasks1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_background_tasks1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_background_tasks1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_background_tasks1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_background_tasks1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_background_tasks1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_background_tasks1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_background_tasks1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_background_tasks1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_background_tasks1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_background_tasks1.ApiResponseFor501) | Not implemented

#### get_background_tasks1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BackgroundTasksTmDto**](../../models/BackgroundTasksTmDto.md) |  | 


#### get_background_tasks1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_background_tasks1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_background_tasks1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_background_tasks1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_background_tasks1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_background_tasks1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_background_tasks1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_background_tasks1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_background_tasks1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_background_tasks1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_background_tasks1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_metadata**
<a id="get_metadata"></a>
> MetadataResponse get_metadata(trans_memory_uid)

Get translation memory metadata

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.metadata_response import MetadataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    query_params = {
    }
    try:
        # Get translation memory metadata
        api_response = api_instance.get_metadata(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->get_metadata: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    query_params = {
        'byLanguage': False,
    }
    try:
        # Get translation memory metadata
        api_response = api_instance.get_metadata(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->get_metadata: %s\n" % e)
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
byLanguage | ByLanguageSchema | | optional


# ByLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_metadata.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_metadata.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_metadata.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_metadata.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_metadata.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_metadata.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_metadata.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_metadata.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_metadata.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_metadata.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_metadata.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_metadata.ApiResponseFor501) | Not implemented

#### get_metadata.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MetadataResponse**](../../models/MetadataResponse.md) |  | 


#### get_metadata.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_metadata.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_metadata.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_metadata.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_metadata.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_metadata.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_metadata.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_metadata.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_metadata.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_metadata.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_metadata.ApiResponseFor501
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
from openapi_client.apis.tags import translation_memory_api
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
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

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
        print("Exception when calling TranslationMemoryApi->get_project_template_trans_memories2: %s\n" % e)

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
        print("Exception when calling TranslationMemoryApi->get_project_template_trans_memories2: %s\n" % e)
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

# **get_related_projects**
<a id="get_related_projects"></a>
> PageDtoAbstractProjectDto get_related_projects(trans_memory_uid)

List related projects

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
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
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    query_params = {
    }
    try:
        # List related projects
        api_response = api_instance.get_related_projects(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->get_related_projects: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List related projects
        api_response = api_instance.get_related_projects(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->get_related_projects: %s\n" % e)
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
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_related_projects.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_related_projects.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_related_projects.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_related_projects.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_related_projects.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_related_projects.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_related_projects.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_related_projects.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_related_projects.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_related_projects.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_related_projects.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_related_projects.ApiResponseFor501) | Not implemented

#### get_related_projects.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoAbstractProjectDto**](../../models/PageDtoAbstractProjectDto.md) |  | 


#### get_related_projects.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_related_projects.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_related_projects.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_related_projects.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_related_projects.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_related_projects.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_related_projects.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_related_projects.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_related_projects.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_related_projects.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_related_projects.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_trans_memory**
<a id="get_trans_memory"></a>
> TransMemoryDto get_trans_memory(trans_memory_uid)

Get translation memory

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.trans_memory_dto import TransMemoryDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Get translation memory
        api_response = api_instance.get_trans_memory(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->get_trans_memory: %s\n" % e)
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
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_trans_memory.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_trans_memory.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_trans_memory.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_trans_memory.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_trans_memory.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_trans_memory.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_trans_memory.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_trans_memory.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_trans_memory.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_trans_memory.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_trans_memory.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_trans_memory.ApiResponseFor501) | Not implemented

#### get_trans_memory.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransMemoryDto**](../../models/TransMemoryDto.md) |  | 


#### get_trans_memory.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_trans_memory.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_trans_memory.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_trans_memory.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_trans_memory.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_trans_memory.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_trans_memory.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_trans_memory.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_trans_memory.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_trans_memory.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_trans_memory.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_translation_resources**
<a id="get_translation_resources"></a>
> TranslationResourcesDto get_translation_resources(project_uidjob_uid)

Get translation resources

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.translation_resources_dto import TranslationResourcesDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->get_translation_resources: %s\n" % e)
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
jobUid | JobUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_translation_resources.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_translation_resources.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_translation_resources.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_translation_resources.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_translation_resources.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_translation_resources.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_translation_resources.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_translation_resources.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_translation_resources.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_translation_resources.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_translation_resources.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_translation_resources.ApiResponseFor501) | Not implemented

#### get_translation_resources.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TranslationResourcesDto**](../../models/TranslationResourcesDto.md) |  | 


#### get_translation_resources.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_translation_resources.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_translation_resources.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_translation_resources.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_translation_resources.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_translation_resources.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_translation_resources.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_translation_resources.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_translation_resources.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_translation_resources.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_translation_resources.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **import_trans_memory_v2**
<a id="import_trans_memory_v2"></a>
> AsyncRequestWrapperV2Dto import_trans_memory_v2(trans_memory_uidcontent_disposition)

Import TMX

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
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
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    query_params = {
    }
    header_params = {
        'Content-Disposition': "Content-Disposition_example",
    }
    try:
        # Import TMX
        api_response = api_instance.import_trans_memory_v2(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->import_trans_memory_v2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    query_params = {
        'strictLangMatching': False,
        'stripNativeCodes': True,
    }
    header_params = {
        'Content-Length': 1,
        'Content-Disposition': "Content-Disposition_example",
    }
    body = dict()
    try:
        # Import TMX
        api_response = api_instance.import_trans_memory_v2(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->import_trans_memory_v2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationOctetStream, SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# SchemaForRequestBodyMultipartFormData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
strictLangMatching | StrictLangMatchingSchema | | optional
stripNativeCodes | StripNativeCodesSchema | | optional


# StrictLangMatchingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# StripNativeCodesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Length | ContentLengthSchema | | optional
Content-Disposition | ContentDispositionSchema | | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# ContentDispositionSchema

Contains filename (UTF-8 encoded).    `filename*=UTF-8''ExampleFileName.md`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Contains filename (UTF-8 encoded).    &#x60;filename*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#import_trans_memory_v2.ApiResponseFor202) | successful operation
400 | [ApiResponseFor400](#import_trans_memory_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#import_trans_memory_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#import_trans_memory_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#import_trans_memory_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#import_trans_memory_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#import_trans_memory_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#import_trans_memory_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#import_trans_memory_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#import_trans_memory_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#import_trans_memory_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#import_trans_memory_v2.ApiResponseFor501) | Not implemented

#### import_trans_memory_v2.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsyncRequestWrapperV2Dto**](../../models/AsyncRequestWrapperV2Dto.md) |  | 


#### import_trans_memory_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_trans_memory_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_trans_memory_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_trans_memory_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_trans_memory_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_trans_memory_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_trans_memory_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_trans_memory_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_trans_memory_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_trans_memory_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_trans_memory_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **insert_to_trans_memory**
<a id="insert_to_trans_memory"></a>
> insert_to_trans_memory(trans_memory_uid)

Insert segment

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.segment_dto import SegmentDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Insert segment
        api_response = api_instance.insert_to_trans_memory(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->insert_to_trans_memory: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    body = SegmentDto(
        target_lang="target_lang_example",
        source_segment="source_segment_example",
        target_segment="target_segment_example",
        previous_source_segment="previous_source_segment_example",
        next_source_segment="next_source_segment_example",
        source_tag_metadata=[
            TagMetadataDto(
                id="id_example",
                type="type_example",
                content="content_example",
                trans_attributes="trans_attributes_example",
            )
        ],
,
    )
    try:
        # Insert segment
        api_response = api_instance.insert_to_trans_memory(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->insert_to_trans_memory: %s\n" % e)
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
[**SegmentDto**](../../models/SegmentDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#insert_to_trans_memory.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#insert_to_trans_memory.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#insert_to_trans_memory.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#insert_to_trans_memory.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#insert_to_trans_memory.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#insert_to_trans_memory.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#insert_to_trans_memory.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#insert_to_trans_memory.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#insert_to_trans_memory.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#insert_to_trans_memory.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#insert_to_trans_memory.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#insert_to_trans_memory.ApiResponseFor501) | Not implemented

#### insert_to_trans_memory.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### insert_to_trans_memory.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_trans_memories**
<a id="list_trans_memories"></a>
> PageDtoTransMemoryDto list_trans_memories()

List translation memories

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
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
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'sourceLang': "sourceLang_example",
        'targetLang': "targetLang_example",
        'clientId': "clientId_example",
        'domainId': "domainId_example",
        'subDomainId': "subDomainId_example",
        'businessUnitId': "businessUnitId_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List translation memories
        api_response = api_instance.list_trans_memories(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->list_trans_memories: %s\n" % e)
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
sourceLang | SourceLangSchema | | optional
targetLang | TargetLangSchema | | optional
clientId | ClientIdSchema | | optional
domainId | DomainIdSchema | | optional
subDomainId | SubDomainIdSchema | | optional
businessUnitId | BusinessUnitIdSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SourceLangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TargetLangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClientIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DomainIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubDomainIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BusinessUnitIdSchema

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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_trans_memories.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_trans_memories.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_trans_memories.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_trans_memories.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_trans_memories.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_trans_memories.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_trans_memories.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_trans_memories.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_trans_memories.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_trans_memories.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_trans_memories.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_trans_memories.ApiResponseFor501) | Not implemented

#### list_trans_memories.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoTransMemoryDto**](../../models/PageDtoTransMemoryDto.md) |  | 


#### list_trans_memories.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_trans_memories.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_trans_memories.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_trans_memories.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_trans_memories.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_trans_memories.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_trans_memories.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_trans_memories.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_trans_memories.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_trans_memories.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_trans_memories.ApiResponseFor501
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
from openapi_client.apis.tags import translation_memory_api
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
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

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
        print("Exception when calling TranslationMemoryApi->relevant_trans_memories: %s\n" % e)

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
        print("Exception when calling TranslationMemoryApi->relevant_trans_memories: %s\n" % e)
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

# **relevant_trans_memories1**
<a id="relevant_trans_memories1"></a>
> PageDtoTransMemoryDto relevant_trans_memories1(project_uid)

List project relevant translation memories

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
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
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

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
        print("Exception when calling TranslationMemoryApi->relevant_trans_memories1: %s\n" % e)

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
        print("Exception when calling TranslationMemoryApi->relevant_trans_memories1: %s\n" % e)
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

# **search**
<a id="search"></a>
> SearchResponseListTmDto search(trans_memory_uid)

Search translation memory (sync)

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.search_request_dto import SearchRequestDto
from openapi_client.model.search_response_list_tm_dto import SearchResponseListTmDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Search translation memory (sync)
        api_response = api_instance.search(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->search: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    body = SearchRequestDto(
        query="query_example",
        source_lang="source_lang_example",
        target_langs=[
            "target_langs_example"
        ],
        previous_segment="previous_segment_example",
        next_segment="next_segment_example",
        tag_metadata=[
            TagMetadataDto(
                id="id_example",
                type="type_example",
                content="content_example",
                trans_attributes="trans_attributes_example",
            )
        ],
        trim_query=True,
        phrase_query=True,
    )
    try:
        # Search translation memory (sync)
        api_response = api_instance.search(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->search: %s\n" % e)
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
[**SearchRequestDto**](../../models/SearchRequestDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#search.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#search.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#search.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#search.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#search.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#search.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#search.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#search.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#search.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#search.ApiResponseFor501) | Not implemented

#### search.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchResponseListTmDto**](../../models/SearchResponseListTmDto.md) |  | 


#### search.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_by_job3**
<a id="search_by_job3"></a>
> SearchResponseListTmDtoV3 search_by_job3(project_uidjob_uid)

Search job's translation memories

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.search_response_list_tm_dto_v3 import SearchResponseListTmDtoV3
from openapi_client.model.search_tmby_job_request_dto_v3 import SearchTMByJobRequestDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->search_by_job3: %s\n" % e)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->search_by_job3: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchTMByJobRequestDtoV3**](../../models/SearchTMByJobRequestDtoV3.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 
jobUid | JobUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_by_job3.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#search_by_job3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#search_by_job3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#search_by_job3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_by_job3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#search_by_job3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#search_by_job3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#search_by_job3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#search_by_job3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#search_by_job3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#search_by_job3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#search_by_job3.ApiResponseFor501) | Not implemented

#### search_by_job3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchResponseListTmDtoV3**](../../models/SearchResponseListTmDtoV3.md) |  | 


#### search_by_job3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_by_job3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_by_job3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_by_job3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_by_job3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_by_job3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_by_job3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_by_job3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_by_job3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_by_job3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_by_job3.ApiResponseFor501
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
from openapi_client.apis.tags import translation_memory_api
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
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

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
        print("Exception when calling TranslationMemoryApi->search_segment1: %s\n" % e)

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
        print("Exception when calling TranslationMemoryApi->search_segment1: %s\n" % e)
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

# **search_segment_by_job**
<a id="search_segment_by_job"></a>
> SearchResponseListTmDto search_segment_by_job(project_uidjob_uid)

Search translation memory for segment by job

Returns at most <i>maxSegments</i>             records with <i>score >= scoreThreshold</i> and at most <i>maxSubsegments</i> records which are subsegment,             i.e. the source text is substring of the query text.

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.search_tmby_job_request_dto import SearchTMByJobRequestDto
from openapi_client.model.search_response_list_tm_dto import SearchResponseListTmDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->search_segment_by_job: %s\n" % e)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->search_segment_by_job: %s\n" % e)
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
[**SearchTMByJobRequestDto**](../../models/SearchTMByJobRequestDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 
jobUid | JobUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_segment_by_job.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#search_segment_by_job.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#search_segment_by_job.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#search_segment_by_job.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_segment_by_job.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#search_segment_by_job.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#search_segment_by_job.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#search_segment_by_job.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#search_segment_by_job.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#search_segment_by_job.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#search_segment_by_job.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#search_segment_by_job.ApiResponseFor501) | Not implemented

#### search_segment_by_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchResponseListTmDto**](../../models/SearchResponseListTmDto.md) |  | 


#### search_segment_by_job.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment_by_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment_by_job.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment_by_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment_by_job.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment_by_job.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment_by_job.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment_by_job.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment_by_job.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment_by_job.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_segment_by_job.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_translation**
<a id="update_translation"></a>
> update_translation(trans_memory_uidsegment_id)

Edit segment

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.translation_dto import TranslationDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
        'segmentId': "segmentId_example",
    }
    try:
        # Edit segment
        api_response = api_instance.update_translation(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->update_translation: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
        'segmentId': "segmentId_example",
    }
    body = TranslationDto(
        lang="lang_example",
        text="text_example",
    )
    try:
        # Edit segment
        api_response = api_instance.update_translation(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->update_translation: %s\n" % e)
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
[**TranslationDto**](../../models/TranslationDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transMemoryUid | TransMemoryUidSchema | | 
segmentId | SegmentIdSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SegmentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_translation.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#update_translation.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_translation.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_translation.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_translation.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_translation.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_translation.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_translation.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_translation.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_translation.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_translation.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_translation.ApiResponseFor501) | Not implemented

#### update_translation.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_translation.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wild_card_search_by_job3**
<a id="wild_card_search_by_job3"></a>
> SearchResponseListTmDtoV3 wild_card_search_by_job3(project_uidjob_uid)

Wildcard search job's translation memories

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.search_response_list_tm_dto_v3 import SearchResponseListTmDtoV3
from openapi_client.model.wild_card_search_by_job_request_dto_v3 import WildCardSearchByJobRequestDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->wild_card_search_by_job3: %s\n" % e)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->wild_card_search_by_job3: %s\n" % e)
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
[**WildCardSearchByJobRequestDtoV3**](../../models/WildCardSearchByJobRequestDtoV3.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUid | ProjectUidSchema | | 
jobUid | JobUidSchema | | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#wild_card_search_by_job3.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#wild_card_search_by_job3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#wild_card_search_by_job3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#wild_card_search_by_job3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#wild_card_search_by_job3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#wild_card_search_by_job3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#wild_card_search_by_job3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#wild_card_search_by_job3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#wild_card_search_by_job3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#wild_card_search_by_job3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#wild_card_search_by_job3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#wild_card_search_by_job3.ApiResponseFor501) | Not implemented

#### wild_card_search_by_job3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchResponseListTmDtoV3**](../../models/SearchResponseListTmDtoV3.md) |  | 


#### wild_card_search_by_job3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wild_card_search_by_job3.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **wildcard_search**
<a id="wildcard_search"></a>
> SearchResponseListTmDto wildcard_search(trans_memory_uid)

Wildcard search

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_memory_api
from openapi_client.model.search_response_list_tm_dto import SearchResponseListTmDto
from openapi_client.model.wild_card_search_request_dto import WildCardSearchRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_memory_api.TranslationMemoryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    try:
        # Wildcard search
        api_response = api_instance.wildcard_search(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->wildcard_search: %s\n" % e)

    # example passing only optional values
    path_params = {
        'transMemoryUid': "transMemoryUid_example",
    }
    body = WildCardSearchRequestDto(
        query="query_example",
        source_lang="source_lang_example",
        target_langs=[
            "target_langs_example"
        ],
        count=1,
        offset=1,
,
    )
    try:
        # Wildcard search
        api_response = api_instance.wildcard_search(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationMemoryApi->wildcard_search: %s\n" % e)
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
[**WildCardSearchRequestDto**](../../models/WildCardSearchRequestDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
transMemoryUid | TransMemoryUidSchema | | 

# TransMemoryUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#wildcard_search.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#wildcard_search.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#wildcard_search.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#wildcard_search.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#wildcard_search.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#wildcard_search.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#wildcard_search.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#wildcard_search.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#wildcard_search.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#wildcard_search.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#wildcard_search.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#wildcard_search.ApiResponseFor501) | Not implemented

#### wildcard_search.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchResponseListTmDto**](../../models/SearchResponseListTmDto.md) |  | 


#### wildcard_search.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wildcard_search.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wildcard_search.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wildcard_search.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wildcard_search.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wildcard_search.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wildcard_search.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wildcard_search.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wildcard_search.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wildcard_search.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### wildcard_search.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

