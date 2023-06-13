<a id="__pageTop"></a>
# openapi_client.apis.tags.analysis_api.AnalysisApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyses_batch_edit_v2**](#analyses_batch_edit_v2) | **put** /api2/v2/analyses/bulk | Edit analyses (batch)
[**bulk_delete_analyses**](#bulk_delete_analyses) | **delete** /api2/v1/analyses/bulk | Delete analyses (batch)
[**create_analyse_async1**](#create_analyse_async1) | **post** /api2/v2/analyses | Create analysis
[**create_analyses_for_langs**](#create_analyses_for_langs) | **post** /api2/v1/analyses/byLanguages | Create analyses by languages
[**create_analyses_for_providers**](#create_analyses_for_providers) | **post** /api2/v1/analyses/byProviders | Create analyses by providers
[**delete**](#delete) | **delete** /api2/v1/analyses/{analyseUid} | Delete analysis
[**download_analyse**](#download_analyse) | **get** /api2/v1/analyses/{analyseUid}/download | Download analysis
[**edit_analysis**](#edit_analysis) | **put** /api2/v2/analyses/{analyseUid} | Edit analysis
[**get_analyse_language_part**](#get_analyse_language_part) | **get** /api2/v1/analyses/{analyseUid}/analyseLanguageParts/{analyseLanguagePartId} | Get analysis language part
[**get_analyse_v3**](#get_analyse_v3) | **get** /api2/v3/analyses/{analyseUid} | Get analysis
[**get_job_part_analyse**](#get_job_part_analyse) | **get** /api2/v1/analyses/{analyseUid}/jobs/{jobUid} | Get jobs analysis
[**list_by_project_v3**](#list_by_project_v3) | **get** /api2/v3/projects/{projectUid}/analyses | List analyses by project
[**list_job_parts**](#list_job_parts) | **get** /api2/v1/analyses/{analyseUid}/analyseLanguageParts/{analyseLanguagePartId}/jobs | List jobs of analyses
[**list_part_analyse_v3**](#list_part_analyse_v3) | **get** /api2/v3/projects/{projectUid}/jobs/{jobUid}/analyses | List analyses
[**recalculate**](#recalculate) | **post** /api2/v1/analyses/recalculate | Recalculate analysis

# **analyses_batch_edit_v2**
<a id="analyses_batch_edit_v2"></a>
> AnalysesV2Dto analyses_batch_edit_v2()

Edit analyses (batch)

If no netRateScheme is provided in request, then netRateScheme associated with provider will be used if it exists, otherwise it will remain the same as it was.

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.bulk_edit_analyse_v2_dto import BulkEditAnalyseV2Dto
from openapi_client.model.analyses_v2_dto import AnalysesV2Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only optional values
    body = BulkEditAnalyseV2Dto(
        analyses=[
            IdReference(
                id="id_example",
            )
        ],
        name="name_example",
        provider=ProviderReference(),
        net_rate_scheme=UidReference(
            uid="uid_example",
        ),
    )
    try:
        # Edit analyses (batch)
        api_response = api_instance.analyses_batch_edit_v2(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->analyses_batch_edit_v2: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**BulkEditAnalyseV2Dto**](../../models/BulkEditAnalyseV2Dto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#analyses_batch_edit_v2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#analyses_batch_edit_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#analyses_batch_edit_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#analyses_batch_edit_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#analyses_batch_edit_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#analyses_batch_edit_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#analyses_batch_edit_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#analyses_batch_edit_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#analyses_batch_edit_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#analyses_batch_edit_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#analyses_batch_edit_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#analyses_batch_edit_v2.ApiResponseFor501) | Not implemented

#### analyses_batch_edit_v2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalysesV2Dto**](../../models/AnalysesV2Dto.md) |  | 


#### analyses_batch_edit_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### analyses_batch_edit_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### analyses_batch_edit_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### analyses_batch_edit_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### analyses_batch_edit_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### analyses_batch_edit_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### analyses_batch_edit_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### analyses_batch_edit_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### analyses_batch_edit_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### analyses_batch_edit_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### analyses_batch_edit_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **bulk_delete_analyses**
<a id="bulk_delete_analyses"></a>
> bulk_delete_analyses()

Delete analyses (batch)

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.bulk_delete_analyse_dto import BulkDeleteAnalyseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only optional values
    body = BulkDeleteAnalyseDto(
        analyses=[
            IdReference(
                id="id_example",
            )
        ],
        purge=True,
    )
    try:
        # Delete analyses (batch)
        api_response = api_instance.bulk_delete_analyses(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->bulk_delete_analyses: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BulkDeleteAnalyseDto**](../../models/BulkDeleteAnalyseDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#bulk_delete_analyses.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#bulk_delete_analyses.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#bulk_delete_analyses.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#bulk_delete_analyses.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#bulk_delete_analyses.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#bulk_delete_analyses.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#bulk_delete_analyses.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#bulk_delete_analyses.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#bulk_delete_analyses.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#bulk_delete_analyses.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#bulk_delete_analyses.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#bulk_delete_analyses.ApiResponseFor501) | Not implemented

#### bulk_delete_analyses.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### bulk_delete_analyses.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_analyse_async1**
<a id="create_analyse_async1"></a>
> AsyncAnalyseListResponseV2Dto create_analyse_async1()

Create analysis

Returns created analyses - batching analyses by number of segments (api.segment.count.approximation, default 100000), in case request contains more segments than maximum (api.segment.max.count, default 300000), returns 400 bad request.

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.create_analyse_async_v2_dto import CreateAnalyseAsyncV2Dto
from openapi_client.model.async_analyse_list_response_v2_dto import AsyncAnalyseListResponseV2Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only optional values
    body = CreateAnalyseAsyncV2Dto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        type="PreAnalyse",
        include_fuzzy_repetitions=True,
        separate_fuzzy_repetitions=True,
        include_confirmed_segments=True,
        include_numbers=True,
        include_locked_segments=True,
        count_source_units=True,
        include_trans_memory=True,
        include_non_translatables=True,
        include_machine_translation_matches=True,
        trans_memory_post_editing=True,
        non_translatable_post_editing=True,
        machine_translate_post_editing=True,
        name="name_example",
        net_rate_scheme=IdReference(
            id="id_example",
        ),
        compare_workflow_level=1,
        use_project_analysis_settings=True,
        callback_url="callback_url_example",
        provider=ProviderReference(),
    )
    try:
        # Create analysis
        api_response = api_instance.create_analyse_async1(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->create_analyse_async1: %s\n" % e)
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
[**CreateAnalyseAsyncV2Dto**](../../models/CreateAnalyseAsyncV2Dto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_analyse_async1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#create_analyse_async1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_analyse_async1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_analyse_async1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_analyse_async1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_analyse_async1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_analyse_async1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_analyse_async1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_analyse_async1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_analyse_async1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_analyse_async1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_analyse_async1.ApiResponseFor501) | Not implemented

#### create_analyse_async1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsyncAnalyseListResponseV2Dto**](../../models/AsyncAnalyseListResponseV2Dto.md) |  | 


#### create_analyse_async1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyse_async1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyse_async1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyse_async1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyse_async1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyse_async1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyse_async1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyse_async1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyse_async1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyse_async1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyse_async1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_analyses_for_langs**
<a id="create_analyses_for_langs"></a>
> AsyncAnalyseListResponseDto create_analyses_for_langs()

Create analyses by languages

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.async_analyse_list_response_dto import AsyncAnalyseListResponseDto
from openapi_client.model.create_analyse_list_async_dto import CreateAnalyseListAsyncDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only optional values
    body = CreateAnalyseListAsyncDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        type="PreAnalyse",
        include_fuzzy_repetitions=True,
        separate_fuzzy_repetitions=True,
        include_confirmed_segments=True,
        include_numbers=True,
        include_locked_segments=True,
        count_source_units=True,
        include_trans_memory=True,
        include_non_translatables=True,
        include_machine_translation_matches=True,
        trans_memory_post_editing=True,
        non_translatable_post_editing=True,
        machine_translate_post_editing=True,
        name="name_example",
        net_rate_scheme=IdReference(
            id="id_example",
        ),
        compare_workflow_level=1,
        use_project_analysis_settings=True,
        callback_url="callback_url_example",
    )
    try:
        # Create analyses by languages
        api_response = api_instance.create_analyses_for_langs(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->create_analyses_for_langs: %s\n" % e)
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
[**CreateAnalyseListAsyncDto**](../../models/CreateAnalyseListAsyncDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_analyses_for_langs.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#create_analyses_for_langs.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_analyses_for_langs.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_analyses_for_langs.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_analyses_for_langs.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_analyses_for_langs.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_analyses_for_langs.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_analyses_for_langs.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_analyses_for_langs.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_analyses_for_langs.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_analyses_for_langs.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_analyses_for_langs.ApiResponseFor501) | Not implemented

#### create_analyses_for_langs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsyncAnalyseListResponseDto**](../../models/AsyncAnalyseListResponseDto.md) |  | 


#### create_analyses_for_langs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_langs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_langs.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_langs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_langs.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_langs.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_langs.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_langs.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_langs.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_langs.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_langs.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_analyses_for_providers**
<a id="create_analyses_for_providers"></a>
> AsyncAnalyseListResponseDto create_analyses_for_providers()

Create analyses by providers

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.async_analyse_list_response_dto import AsyncAnalyseListResponseDto
from openapi_client.model.create_analyse_list_async_dto import CreateAnalyseListAsyncDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only optional values
    body = CreateAnalyseListAsyncDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        type="PreAnalyse",
        include_fuzzy_repetitions=True,
        separate_fuzzy_repetitions=True,
        include_confirmed_segments=True,
        include_numbers=True,
        include_locked_segments=True,
        count_source_units=True,
        include_trans_memory=True,
        include_non_translatables=True,
        include_machine_translation_matches=True,
        trans_memory_post_editing=True,
        non_translatable_post_editing=True,
        machine_translate_post_editing=True,
        name="name_example",
        net_rate_scheme=IdReference(
            id="id_example",
        ),
        compare_workflow_level=1,
        use_project_analysis_settings=True,
        callback_url="callback_url_example",
    )
    try:
        # Create analyses by providers
        api_response = api_instance.create_analyses_for_providers(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->create_analyses_for_providers: %s\n" % e)
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
[**CreateAnalyseListAsyncDto**](../../models/CreateAnalyseListAsyncDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_analyses_for_providers.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#create_analyses_for_providers.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_analyses_for_providers.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_analyses_for_providers.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_analyses_for_providers.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_analyses_for_providers.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_analyses_for_providers.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_analyses_for_providers.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_analyses_for_providers.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_analyses_for_providers.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_analyses_for_providers.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_analyses_for_providers.ApiResponseFor501) | Not implemented

#### create_analyses_for_providers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsyncAnalyseListResponseDto**](../../models/AsyncAnalyseListResponseDto.md) |  | 


#### create_analyses_for_providers.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_providers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_providers.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_providers.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_providers.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_providers.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_providers.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_providers.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_providers.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_providers.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_analyses_for_providers.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete**
<a id="delete"></a>
> delete(analyse_uid)

Delete analysis

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'analyseUid': "analyseUid_example",
    }
    query_params = {
    }
    try:
        # Delete analysis
        api_response = api_instance.delete(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'analyseUid': "analyseUid_example",
    }
    query_params = {
        'purge': True,
    }
    try:
        # Delete analysis
        api_response = api_instance.delete(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->delete: %s\n" % e)
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
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
analyseUid | AnalyseUidSchema | | 

# AnalyseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete.ApiResponseFor501) | Not implemented

#### delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_analyse**
<a id="download_analyse"></a>
> download_analyse(analyse_uidformat)

Download analysis

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'analyseUid': "analyseUid_example",
    }
    query_params = {
        'format': "CSV",
    }
    try:
        # Download analysis
        api_response = api_instance.download_analyse(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->download_analyse: %s\n" % e)
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
format | FormatSchema | | 


# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["CSV", "CSV_EXTENDED", "LOG", "JSON", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
analyseUid | AnalyseUidSchema | | 

# AnalyseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#download_analyse.ApiResponseFor200) | application/octet-stream
400 | [ApiResponseFor400](#download_analyse.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#download_analyse.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#download_analyse.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#download_analyse.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#download_analyse.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#download_analyse.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#download_analyse.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#download_analyse.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#download_analyse.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#download_analyse.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#download_analyse.ApiResponseFor501) | Not implemented

#### download_analyse.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### download_analyse.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_analysis**
<a id="edit_analysis"></a>
> AnalyseV2Dto edit_analysis(analyse_uid)

Edit analysis

If no netRateScheme is provided in request, then netRateScheme associated with provider will be used if it exists, otherwise it will remain the same as it was.

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.edit_analyse_v2_dto import EditAnalyseV2Dto
from openapi_client.model.analyse_v2_dto import AnalyseV2Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'analyseUid': "analyseUid_example",
    }
    try:
        # Edit analysis
        api_response = api_instance.edit_analysis(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->edit_analysis: %s\n" % e)

    # example passing only optional values
    path_params = {
        'analyseUid': "analyseUid_example",
    }
    body = EditAnalyseV2Dto(
        name="name_example",
        provider=ProviderReference(),
        net_rate_scheme=UidReference(
            uid="uid_example",
        ),
    )
    try:
        # Edit analysis
        api_response = api_instance.edit_analysis(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->edit_analysis: %s\n" % e)
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
[**EditAnalyseV2Dto**](../../models/EditAnalyseV2Dto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
analyseUid | AnalyseUidSchema | | 

# AnalyseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_analysis.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_analysis.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_analysis.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_analysis.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_analysis.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_analysis.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_analysis.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_analysis.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_analysis.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_analysis.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_analysis.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_analysis.ApiResponseFor501) | Not implemented

#### edit_analysis.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalyseV2Dto**](../../models/AnalyseV2Dto.md) |  | 


#### edit_analysis.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_analysis.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_analysis.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_analysis.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_analysis.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_analysis.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_analysis.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_analysis.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_analysis.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_analysis.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_analysis.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_analyse_language_part**
<a id="get_analyse_language_part"></a>
> AnalyseLanguagePartDto get_analyse_language_part(analyse_uidanalyse_language_part_id)

Get analysis language part

Returns analysis language pair

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.analyse_language_part_dto import AnalyseLanguagePartDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'analyseUid': "analyseUid_example",
        'analyseLanguagePartId': 1,
    }
    try:
        # Get analysis language part
        api_response = api_instance.get_analyse_language_part(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->get_analyse_language_part: %s\n" % e)
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
analyseUid | AnalyseUidSchema | | 
analyseLanguagePartId | AnalyseLanguagePartIdSchema | | 

# AnalyseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AnalyseLanguagePartIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_analyse_language_part.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_analyse_language_part.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_analyse_language_part.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_analyse_language_part.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_analyse_language_part.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_analyse_language_part.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_analyse_language_part.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_analyse_language_part.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_analyse_language_part.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_analyse_language_part.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_analyse_language_part.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_analyse_language_part.ApiResponseFor501) | Not implemented

#### get_analyse_language_part.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalyseLanguagePartDto**](../../models/AnalyseLanguagePartDto.md) |  | 


#### get_analyse_language_part.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_language_part.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_language_part.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_language_part.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_language_part.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_language_part.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_language_part.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_language_part.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_language_part.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_language_part.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_language_part.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_analyse_v3**
<a id="get_analyse_v3"></a>
> AnalyseV3Dto get_analyse_v3(analyse_uid)

Get analysis

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.analyse_v3_dto import AnalyseV3Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'analyseUid': "analyseUid_example",
    }
    try:
        # Get analysis
        api_response = api_instance.get_analyse_v3(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->get_analyse_v3: %s\n" % e)
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
analyseUid | AnalyseUidSchema | | 

# AnalyseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_analyse_v3.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_analyse_v3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_analyse_v3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_analyse_v3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_analyse_v3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_analyse_v3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_analyse_v3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_analyse_v3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_analyse_v3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_analyse_v3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_analyse_v3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_analyse_v3.ApiResponseFor501) | Not implemented

#### get_analyse_v3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalyseV3Dto**](../../models/AnalyseV3Dto.md) |  | 


#### get_analyse_v3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_v3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_v3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_v3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_v3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_v3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_v3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_v3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_v3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_v3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_analyse_v3.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_job_part_analyse**
<a id="get_job_part_analyse"></a>
> AnalyseJobDto get_job_part_analyse(analyse_uidjob_uid)

Get jobs analysis

Returns job's analyse

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.analyse_job_dto import AnalyseJobDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'analyseUid': "analyseUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get jobs analysis
        api_response = api_instance.get_job_part_analyse(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->get_job_part_analyse: %s\n" % e)
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
analyseUid | AnalyseUidSchema | | 
jobUid | JobUidSchema | | 

# AnalyseUidSchema

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
200 | [ApiResponseFor200](#get_job_part_analyse.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_job_part_analyse.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_job_part_analyse.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_job_part_analyse.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_job_part_analyse.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_job_part_analyse.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_job_part_analyse.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_job_part_analyse.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_job_part_analyse.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_job_part_analyse.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_job_part_analyse.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_job_part_analyse.ApiResponseFor501) | Not implemented

#### get_job_part_analyse.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalyseJobDto**](../../models/AnalyseJobDto.md) |  | 


#### get_job_part_analyse.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_job_part_analyse.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_job_part_analyse.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_job_part_analyse.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_job_part_analyse.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_job_part_analyse.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_job_part_analyse.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_job_part_analyse.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_job_part_analyse.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_job_part_analyse.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_job_part_analyse.ApiResponseFor501
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
from openapi_client.apis.tags import analysis_api
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
    api_instance = analysis_api.AnalysisApi(api_client)

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
        print("Exception when calling AnalysisApi->list_by_project_v3: %s\n" % e)

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
        print("Exception when calling AnalysisApi->list_by_project_v3: %s\n" % e)
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

# **list_job_parts**
<a id="list_job_parts"></a>
> PageDtoAnalyseJobDto list_job_parts(analyse_uidanalyse_language_part_id)

List jobs of analyses

Returns list of job's analyses

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.page_dto_analyse_job_dto import PageDtoAnalyseJobDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'analyseUid': "analyseUid_example",
        'analyseLanguagePartId': 1,
    }
    query_params = {
    }
    try:
        # List jobs of analyses
        api_response = api_instance.list_job_parts(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->list_job_parts: %s\n" % e)

    # example passing only optional values
    path_params = {
        'analyseUid': "analyseUid_example",
        'analyseLanguagePartId': 1,
    }
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List jobs of analyses
        api_response = api_instance.list_job_parts(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->list_job_parts: %s\n" % e)
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
analyseUid | AnalyseUidSchema | | 
analyseLanguagePartId | AnalyseLanguagePartIdSchema | | 

# AnalyseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AnalyseLanguagePartIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_job_parts.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_job_parts.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_job_parts.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_job_parts.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_job_parts.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_job_parts.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_job_parts.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_job_parts.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_job_parts.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_job_parts.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_job_parts.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_job_parts.ApiResponseFor501) | Not implemented

#### list_job_parts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoAnalyseJobDto**](../../models/PageDtoAnalyseJobDto.md) |  | 


#### list_job_parts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_job_parts.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_job_parts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_job_parts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_job_parts.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_job_parts.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_job_parts.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_job_parts.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_job_parts.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_job_parts.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_job_parts.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_part_analyse_v3**
<a id="list_part_analyse_v3"></a>
> PageDtoAnalyseReference list_part_analyse_v3(project_uidjob_uid)

List analyses

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
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
    api_instance = analysis_api.AnalysisApi(api_client)

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
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->list_part_analyse_v3: %s\n" % e)

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
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->list_part_analyse_v3: %s\n" % e)
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
200 | [ApiResponseFor200](#list_part_analyse_v3.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_part_analyse_v3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_part_analyse_v3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_part_analyse_v3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_part_analyse_v3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_part_analyse_v3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_part_analyse_v3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_part_analyse_v3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_part_analyse_v3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_part_analyse_v3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_part_analyse_v3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_part_analyse_v3.ApiResponseFor501) | Not implemented

#### list_part_analyse_v3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoAnalyseReference**](../../models/PageDtoAnalyseReference.md) |  | 


#### list_part_analyse_v3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_part_analyse_v3.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **recalculate**
<a id="recalculate"></a>
> AnalyseRecalculateResponseDto recalculate()

Recalculate analysis

### Example

```python
import openapi_client
from openapi_client.apis.tags import analysis_api
from openapi_client.model.analyse_recalculate_response_dto import AnalyseRecalculateResponseDto
from openapi_client.model.analyse_recalculate_request_dto import AnalyseRecalculateRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_api.AnalysisApi(api_client)

    # example passing only optional values
    body = AnalyseRecalculateRequestDto(
        analyses=[
            IdReference(
                id="id_example",
            )
        ],
        callback_url="callback_url_example",
    )
    try:
        # Recalculate analysis
        api_response = api_instance.recalculate(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalysisApi->recalculate: %s\n" % e)
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
[**AnalyseRecalculateRequestDto**](../../models/AnalyseRecalculateRequestDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#recalculate.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#recalculate.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#recalculate.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#recalculate.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#recalculate.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#recalculate.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#recalculate.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#recalculate.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#recalculate.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#recalculate.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#recalculate.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#recalculate.ApiResponseFor501) | Not implemented

#### recalculate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalyseRecalculateResponseDto**](../../models/AnalyseRecalculateResponseDto.md) |  | 


#### recalculate.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### recalculate.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### recalculate.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### recalculate.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### recalculate.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### recalculate.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### recalculate.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### recalculate.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### recalculate.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### recalculate.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### recalculate.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

