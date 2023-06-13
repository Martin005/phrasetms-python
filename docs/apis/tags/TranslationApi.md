<a id="__pageTop"></a>
# openapi_client.apis.tags.translation_api.TranslationApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**human_translate**](#human_translate) | **post** /api2/v1/projects/{projectUid}/jobs/humanTranslate | Human translate (Gengo or Unbabel)
[**machine_translation_job**](#machine_translation_job) | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translations/translateWithMachineTranslation | Translate using machine translation
[**pre_translate1**](#pre_translate1) | **post** /api2/v2/projects/{projectUid}/jobs/preTranslate | Pre-translate job

# **human_translate**
<a id="human_translate"></a>
> AsyncRequestWrapperDto human_translate(project_uid)

Human translate (Gengo or Unbabel)

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_api
from openapi_client.model.human_translate_jobs_dto import HumanTranslateJobsDto
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
    api_instance = translation_api.TranslationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Human translate (Gengo or Unbabel)
        api_response = api_instance.human_translate(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationApi->human_translate: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = HumanTranslateJobsDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        human_translate_settings=IdReference(
            id="id_example",
        ),
        comment="comment_example",
        glossary_id="glossary_id_example",
        use_preferred_translators=True,
        level="STANDARD",
        callback_url="callback_url_example",
    )
    try:
        # Human translate (Gengo or Unbabel)
        api_response = api_instance.human_translate(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationApi->human_translate: %s\n" % e)
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
[**HumanTranslateJobsDto**](../../models/HumanTranslateJobsDto.md) |  | 


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
200 | [ApiResponseFor200](#human_translate.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#human_translate.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#human_translate.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#human_translate.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#human_translate.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#human_translate.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#human_translate.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#human_translate.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#human_translate.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#human_translate.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#human_translate.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#human_translate.ApiResponseFor501) | Not implemented

#### human_translate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsyncRequestWrapperDto**](../../models/AsyncRequestWrapperDto.md) |  | 


#### human_translate.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### human_translate.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### human_translate.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### human_translate.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### human_translate.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### human_translate.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### human_translate.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### human_translate.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### human_translate.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### human_translate.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### human_translate.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **machine_translation_job**
<a id="machine_translation_job"></a>
> MachineTranslateResponse machine_translation_job(project_uidjob_uid)

Translate using machine translation

Configured machine translate settings is used

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_api
from openapi_client.model.machine_translate_response import MachineTranslateResponse
from openapi_client.model.translation_request_dto import TranslationRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = translation_api.TranslationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Translate using machine translation
        api_response = api_instance.machine_translation_job(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationApi->machine_translation_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = TranslationRequestDto(
        source_texts=[
            "source_texts_example"
        ],
    )
    try:
        # Translate using machine translation
        api_response = api_instance.machine_translation_job(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationApi->machine_translation_job: %s\n" % e)
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
[**TranslationRequestDto**](../../models/TranslationRequestDto.md) |  | 


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
200 | [ApiResponseFor200](#machine_translation_job.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#machine_translation_job.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#machine_translation_job.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#machine_translation_job.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#machine_translation_job.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#machine_translation_job.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#machine_translation_job.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#machine_translation_job.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#machine_translation_job.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#machine_translation_job.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#machine_translation_job.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#machine_translation_job.ApiResponseFor501) | Not implemented

#### machine_translation_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MachineTranslateResponse**](../../models/MachineTranslateResponse.md) |  | 


#### machine_translation_job.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation_job.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation_job.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation_job.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation_job.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation_job.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation_job.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation_job.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation_job.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **pre_translate1**
<a id="pre_translate1"></a>
> AsyncRequestWrapperV2Dto pre_translate1(project_uid)

Pre-translate job

### Example

```python
import openapi_client
from openapi_client.apis.tags import translation_api
from openapi_client.model.pre_translate_jobs_v2_dto import PreTranslateJobsV2Dto
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
    api_instance = translation_api.TranslationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Pre-translate job
        api_response = api_instance.pre_translate1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationApi->pre_translate1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = PreTranslateJobsV2Dto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        segment_filters=[
            "LOCKED"
        ],
        use_project_pre_translate_settings=True,
        callback_url="callback_url_example",
        pre_translate_settings=PreTranslateJobSettingsDto(
            auto_propagate_repetitions=True,
            confirm_repetitions=True,
            set_job_status_completed=True,
            set_job_status_completed_when_confirmed=True,
            set_project_status_completed=True,
            overwrite_existing_translations=True,
            translation_memory_settings=JobTranslationMemorySettingsDto(
                use_translation_memory=True,
                translation_memory_threshold=0,
                confirm100_percent_matches=True,
                confirm101_percent_matches=True,
                lock100_percent_matches=True,
                lock101_percent_matches=True,
            ),
            machine_translation_settings=JobMachineTranslationSettingsDto(
                use_machine_translation=True,
                lock100_percent_matches=True,
                confirm100_percent_matches=True,
                use_alt_trans_only=True,
            ),
            non_translatable_settings=JobNonTranslatableSettingsDto(
                pre_translate_non_translatables=True,
                confirm100_percent_matches=True,
                lock100_percent_matches=True,
            ),
        ),
    )
    try:
        # Pre-translate job
        api_response = api_instance.pre_translate1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TranslationApi->pre_translate1: %s\n" % e)
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
[**PreTranslateJobsV2Dto**](../../models/PreTranslateJobsV2Dto.md) |  | 


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
202 | [ApiResponseFor202](#pre_translate1.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#pre_translate1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#pre_translate1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#pre_translate1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#pre_translate1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#pre_translate1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#pre_translate1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#pre_translate1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#pre_translate1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#pre_translate1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#pre_translate1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#pre_translate1.ApiResponseFor501) | Not implemented

#### pre_translate1.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AsyncRequestWrapperV2Dto**](../../models/AsyncRequestWrapperV2Dto.md) |  | 


#### pre_translate1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### pre_translate1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### pre_translate1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### pre_translate1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### pre_translate1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### pre_translate1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### pre_translate1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### pre_translate1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### pre_translate1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### pre_translate1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### pre_translate1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

