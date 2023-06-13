<a id="__pageTop"></a>
# openapi_client.apis.tags.quality_assurance_api.QualityAssuranceApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ignored_warnings**](#add_ignored_warnings) | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/ignoredWarnings | Add ignored warnings
[**add_ignored_warnings1**](#add_ignored_warnings1) | **post** /api2/v2/projects/{projectUid}/jobs/qualityAssurances/ignoredWarnings | Add ignored warnings
[**create_lqa_profile**](#create_lqa_profile) | **post** /api2/v1/lqa/profiles | Create LQA profile
[**delete_ignored_warnings**](#delete_ignored_warnings) | **delete** /api2/v1/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/ignoredWarnings | Delete ignored warnings
[**delete_ignored_warnings1**](#delete_ignored_warnings1) | **delete** /api2/v2/projects/{projectUid}/jobs/qualityAssurances/ignoredWarnings | Delete ignored warnings
[**delete_lqa_profile**](#delete_lqa_profile) | **delete** /api2/v1/lqa/profiles/{profileUid} | Delete LQA profile
[**duplicate_profile**](#duplicate_profile) | **post** /api2/v1/lqa/profiles/{profileUid}/duplicate | Duplicate LQA profile
[**enabled_quality_checks_for_job**](#enabled_quality_checks_for_job) | **get** /api2/v2/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/settings | Get QA settings for job
[**enabled_quality_checks_for_job1**](#enabled_quality_checks_for_job1) | **get** /api2/v2/projects/{projectUid}/jobs/qualityAssurances/settings | Get QA settings
[**get_lqa_profile**](#get_lqa_profile) | **get** /api2/v1/lqa/profiles/{profileUid} | Get LQA profile details
[**get_lqa_profile_authors**](#get_lqa_profile_authors) | **get** /api2/v1/lqa/profiles/authors | Get list of LQA profile authors
[**get_lqa_profiles**](#get_lqa_profiles) | **get** /api2/v1/lqa/profiles | GET list LQA profiles
[**make_default**](#make_default) | **post** /api2/v1/lqa/profiles/{profileUid}/default | Make LQA profile default
[**run_qa_for_job_part_v3**](#run_qa_for_job_part_v3) | **post** /api2/v3/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/run | Run quality assurance
[**run_qa_for_job_parts_v3**](#run_qa_for_job_parts_v3) | **post** /api2/v3/projects/{projectUid}/jobs/qualityAssurances/run | Run quality assurance (batch)
[**run_qa_for_segments_v3**](#run_qa_for_segments_v3) | **post** /api2/v3/projects/{projectUid}/jobs/qualityAssurances/segments/run | Run quality assurance on selected segments
[**update_ignored_checks**](#update_ignored_checks) | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/ignoreChecks | Edit ignored checks
[**update_lqa_profile**](#update_lqa_profile) | **put** /api2/v1/lqa/profiles/{profileUid} | Update LQA profile

# **add_ignored_warnings**
<a id="add_ignored_warnings"></a>
> UpdateIgnoredWarningsDto add_ignored_warnings(project_uidjob_uid)

Add ignored warnings

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.update_ignored_warnings_dto import UpdateIgnoredWarningsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Add ignored warnings
        api_response = api_instance.add_ignored_warnings(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->add_ignored_warnings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = UpdateIgnoredWarningsDto(
        job_parts=[
            UpdateIgnoredJobPartSegment(
                job_part_uid="job_part_uid_example",
                segments=[
                    UpdateIgnoredSegment(
                        uid="uid_example",
                        warnings=[
                            UpdateIgnoredWarning(
                                id="id_example",
                            )
                        ],
                    )
                ],
            )
        ],
    )
    try:
        # Add ignored warnings
        api_response = api_instance.add_ignored_warnings(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->add_ignored_warnings: %s\n" % e)
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
[**UpdateIgnoredWarningsDto**](../../models/UpdateIgnoredWarningsDto.md) |  | 


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
200 | [ApiResponseFor200](#add_ignored_warnings.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#add_ignored_warnings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#add_ignored_warnings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#add_ignored_warnings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#add_ignored_warnings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#add_ignored_warnings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#add_ignored_warnings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#add_ignored_warnings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#add_ignored_warnings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#add_ignored_warnings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#add_ignored_warnings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#add_ignored_warnings.ApiResponseFor501) | Not implemented

#### add_ignored_warnings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateIgnoredWarningsDto**](../../models/UpdateIgnoredWarningsDto.md) |  | 


#### add_ignored_warnings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **add_ignored_warnings1**
<a id="add_ignored_warnings1"></a>
> UpdateIgnoredWarningsDto add_ignored_warnings1(project_uid)

Add ignored warnings

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.update_ignored_warnings_dto import UpdateIgnoredWarningsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Add ignored warnings
        api_response = api_instance.add_ignored_warnings1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->add_ignored_warnings1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = UpdateIgnoredWarningsDto(
        job_parts=[
            UpdateIgnoredJobPartSegment(
                job_part_uid="job_part_uid_example",
                segments=[
                    UpdateIgnoredSegment(
                        uid="uid_example",
                        warnings=[
                            UpdateIgnoredWarning(
                                id="id_example",
                            )
                        ],
                    )
                ],
            )
        ],
    )
    try:
        # Add ignored warnings
        api_response = api_instance.add_ignored_warnings1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->add_ignored_warnings1: %s\n" % e)
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
[**UpdateIgnoredWarningsDto**](../../models/UpdateIgnoredWarningsDto.md) |  | 


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
200 | [ApiResponseFor200](#add_ignored_warnings1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#add_ignored_warnings1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#add_ignored_warnings1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#add_ignored_warnings1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#add_ignored_warnings1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#add_ignored_warnings1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#add_ignored_warnings1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#add_ignored_warnings1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#add_ignored_warnings1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#add_ignored_warnings1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#add_ignored_warnings1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#add_ignored_warnings1.ApiResponseFor501) | Not implemented

#### add_ignored_warnings1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateIgnoredWarningsDto**](../../models/UpdateIgnoredWarningsDto.md) |  | 


#### add_ignored_warnings1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_ignored_warnings1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_lqa_profile**
<a id="create_lqa_profile"></a>
> LqaProfileDetailDto create_lqa_profile()

Create LQA profile

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.create_lqa_profile_dto import CreateLqaProfileDto
from openapi_client.model.lqa_profile_detail_dto import LqaProfileDetailDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only optional values
    body = CreateLqaProfileDto(
        name="name_example",
        error_categories=ErrorCategoriesDto(
            accuracy=AccuracyWeightsDto(
                accuracy=ToggleableWeightDto(
                    enabled=True,
                    weight=1,
                    code=1,
                ),
,
,
,
,
,
,
,
            ),
            fluency=FluencyWeightsDto(
                fluency=ToggleableWeightDto(),
                punctuation=ToggleableWeightDto(),
                spelling=ToggleableWeightDto(),
                grammar=ToggleableWeightDto(),
                grammatical_register=ToggleableWeightDto(),
                inconsistency=ToggleableWeightDto(),
                cross_reference=ToggleableWeightDto(),
                character_encoding=ToggleableWeightDto(),
            ),
            terminology=TerminologyWeightsDto(
                terminology=ToggleableWeightDto(),
                inconsistent_with_tb=ToggleableWeightDto(),
                inconsistent_use_of_terminology=ToggleableWeightDto(),
            ),
            style=StyleWeightsDto(
                style=ToggleableWeightDto(),
                awkward=ToggleableWeightDto(),
                company_style=ToggleableWeightDto(),
                inconsistent_style=ToggleableWeightDto(),
                third_party_style=ToggleableWeightDto(),
                unidiomatic=ToggleableWeightDto(),
            ),
            locale_convention=LocaleConventionWeightsDto(
                locale_convention=ToggleableWeightDto(),
                address_format=ToggleableWeightDto(),
                date_format=ToggleableWeightDto(),
                currency_format=ToggleableWeightDto(),
                measurement_format=ToggleableWeightDto(),
                shortcut_key=ToggleableWeightDto(),
                telephone_format=ToggleableWeightDto(),
            ),
            verity=VerityWeightsDto(
                verity=ToggleableWeightDto(),
                culture_specific_reference=ToggleableWeightDto(),
            ),
            design=DesignWeightsDto(
                design=ToggleableWeightDto(),
                length=ToggleableWeightDto(),
                local_formatting=ToggleableWeightDto(),
                markup=ToggleableWeightDto(),
                missing_text=ToggleableWeightDto(),
                truncation=ToggleableWeightDto(),
            ),
            other=OtherWeightsDto(
                other=ToggleableWeightDto(),
            ),
        ),
        penalty_points=PenaltyPointsDto(
            neutral=SeverityDto(
                code=1,
                value=3.14,
            ),
,
,
,
        ),
        pass_fail_threshold=PassFailThresholdDto(
            min_score_percentage=99,
        ),
    )
    try:
        # Create LQA profile
        api_response = api_instance.create_lqa_profile(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->create_lqa_profile: %s\n" % e)
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
[**CreateLqaProfileDto**](../../models/CreateLqaProfileDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_lqa_profile.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_lqa_profile.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_lqa_profile.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_lqa_profile.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_lqa_profile.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_lqa_profile.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_lqa_profile.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_lqa_profile.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_lqa_profile.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_lqa_profile.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_lqa_profile.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_lqa_profile.ApiResponseFor501) | Not implemented

#### create_lqa_profile.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LqaProfileDetailDto**](../../models/LqaProfileDetailDto.md) |  | 


#### create_lqa_profile.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_lqa_profile.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_lqa_profile.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_lqa_profile.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_lqa_profile.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_lqa_profile.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_lqa_profile.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_lqa_profile.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_lqa_profile.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_lqa_profile.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_lqa_profile.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_ignored_warnings**
<a id="delete_ignored_warnings"></a>
> delete_ignored_warnings(project_uidjob_uid)

Delete ignored warnings

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.update_ignored_warnings_dto import UpdateIgnoredWarningsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Delete ignored warnings
        api_response = api_instance.delete_ignored_warnings(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->delete_ignored_warnings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = UpdateIgnoredWarningsDto(
        job_parts=[
            UpdateIgnoredJobPartSegment(
                job_part_uid="job_part_uid_example",
                segments=[
                    UpdateIgnoredSegment(
                        uid="uid_example",
                        warnings=[
                            UpdateIgnoredWarning(
                                id="id_example",
                            )
                        ],
                    )
                ],
            )
        ],
    )
    try:
        # Delete ignored warnings
        api_response = api_instance.delete_ignored_warnings(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->delete_ignored_warnings: %s\n" % e)
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
[**UpdateIgnoredWarningsDto**](../../models/UpdateIgnoredWarningsDto.md) |  | 


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
204 | [ApiResponseFor204](#delete_ignored_warnings.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_ignored_warnings.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_ignored_warnings.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_ignored_warnings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_ignored_warnings.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_ignored_warnings.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_ignored_warnings.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_ignored_warnings.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_ignored_warnings.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_ignored_warnings.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_ignored_warnings.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_ignored_warnings.ApiResponseFor501) | Not implemented

#### delete_ignored_warnings.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_ignored_warnings1**
<a id="delete_ignored_warnings1"></a>
> delete_ignored_warnings1(project_uid)

Delete ignored warnings

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.update_ignored_warnings_dto import UpdateIgnoredWarningsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Delete ignored warnings
        api_response = api_instance.delete_ignored_warnings1(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->delete_ignored_warnings1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = UpdateIgnoredWarningsDto(
        job_parts=[
            UpdateIgnoredJobPartSegment(
                job_part_uid="job_part_uid_example",
                segments=[
                    UpdateIgnoredSegment(
                        uid="uid_example",
                        warnings=[
                            UpdateIgnoredWarning(
                                id="id_example",
                            )
                        ],
                    )
                ],
            )
        ],
    )
    try:
        # Delete ignored warnings
        api_response = api_instance.delete_ignored_warnings1(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->delete_ignored_warnings1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateIgnoredWarningsDto**](../../models/UpdateIgnoredWarningsDto.md) |  | 


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
204 | [ApiResponseFor204](#delete_ignored_warnings1.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_ignored_warnings1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_ignored_warnings1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_ignored_warnings1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_ignored_warnings1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_ignored_warnings1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_ignored_warnings1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_ignored_warnings1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_ignored_warnings1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_ignored_warnings1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_ignored_warnings1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_ignored_warnings1.ApiResponseFor501) | Not implemented

#### delete_ignored_warnings1.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_ignored_warnings1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_lqa_profile**
<a id="delete_lqa_profile"></a>
> delete_lqa_profile(profile_uid)

Delete LQA profile

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'profileUid': "profileUid_example",
    }
    try:
        # Delete LQA profile
        api_response = api_instance.delete_lqa_profile(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->delete_lqa_profile: %s\n" % e)
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
profileUid | ProfileUidSchema | | 

# ProfileUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_lqa_profile.ApiResponseFor204) | Deleted
400 | [ApiResponseFor400](#delete_lqa_profile.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_lqa_profile.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_lqa_profile.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_lqa_profile.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_lqa_profile.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_lqa_profile.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_lqa_profile.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_lqa_profile.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_lqa_profile.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_lqa_profile.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_lqa_profile.ApiResponseFor501) | Not implemented

#### delete_lqa_profile.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_lqa_profile.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **duplicate_profile**
<a id="duplicate_profile"></a>
> LqaProfileReferenceDto duplicate_profile(profile_uid)

Duplicate LQA profile

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.lqa_profile_reference_dto import LqaProfileReferenceDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'profileUid': "profileUid_example",
    }
    try:
        # Duplicate LQA profile
        api_response = api_instance.duplicate_profile(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->duplicate_profile: %s\n" % e)
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
profileUid | ProfileUidSchema | | 

# ProfileUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#duplicate_profile.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#duplicate_profile.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#duplicate_profile.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#duplicate_profile.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#duplicate_profile.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#duplicate_profile.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#duplicate_profile.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#duplicate_profile.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#duplicate_profile.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#duplicate_profile.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#duplicate_profile.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#duplicate_profile.ApiResponseFor501) | Not implemented

#### duplicate_profile.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LqaProfileReferenceDto**](../../models/LqaProfileReferenceDto.md) |  | 


#### duplicate_profile.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### duplicate_profile.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### duplicate_profile.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### duplicate_profile.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### duplicate_profile.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### duplicate_profile.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### duplicate_profile.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### duplicate_profile.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### duplicate_profile.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### duplicate_profile.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### duplicate_profile.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enabled_quality_checks_for_job**
<a id="enabled_quality_checks_for_job"></a>
> QualityAssuranceChecksDtoV2 enabled_quality_checks_for_job(project_uidjob_uid)

Get QA settings for job

Returns enabled quality assurance checks and settings for job.

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.quality_assurance_checks_dto_v2 import QualityAssuranceChecksDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get QA settings for job
        api_response = api_instance.enabled_quality_checks_for_job(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->enabled_quality_checks_for_job: %s\n" % e)
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
200 | [ApiResponseFor200](#enabled_quality_checks_for_job.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#enabled_quality_checks_for_job.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#enabled_quality_checks_for_job.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#enabled_quality_checks_for_job.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#enabled_quality_checks_for_job.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#enabled_quality_checks_for_job.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#enabled_quality_checks_for_job.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#enabled_quality_checks_for_job.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#enabled_quality_checks_for_job.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#enabled_quality_checks_for_job.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#enabled_quality_checks_for_job.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#enabled_quality_checks_for_job.ApiResponseFor501) | Not implemented

#### enabled_quality_checks_for_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**QualityAssuranceChecksDtoV2**](../../models/QualityAssuranceChecksDtoV2.md) |  | 


#### enabled_quality_checks_for_job.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enabled_quality_checks_for_job1**
<a id="enabled_quality_checks_for_job1"></a>
> QualityAssuranceChecksDtoV2 enabled_quality_checks_for_job1(project_uid)

Get QA settings

Returns enabled quality assurance checks and settings.

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.quality_assurance_checks_dto_v2 import QualityAssuranceChecksDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get QA settings
        api_response = api_instance.enabled_quality_checks_for_job1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->enabled_quality_checks_for_job1: %s\n" % e)
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
200 | [ApiResponseFor200](#enabled_quality_checks_for_job1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#enabled_quality_checks_for_job1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#enabled_quality_checks_for_job1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#enabled_quality_checks_for_job1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#enabled_quality_checks_for_job1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#enabled_quality_checks_for_job1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#enabled_quality_checks_for_job1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#enabled_quality_checks_for_job1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#enabled_quality_checks_for_job1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#enabled_quality_checks_for_job1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#enabled_quality_checks_for_job1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#enabled_quality_checks_for_job1.ApiResponseFor501) | Not implemented

#### enabled_quality_checks_for_job1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**QualityAssuranceChecksDtoV2**](../../models/QualityAssuranceChecksDtoV2.md) |  | 


#### enabled_quality_checks_for_job1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### enabled_quality_checks_for_job1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_lqa_profile**
<a id="get_lqa_profile"></a>
> LqaProfileDetailDto get_lqa_profile(profile_uid)

Get LQA profile details

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.lqa_profile_detail_dto import LqaProfileDetailDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'profileUid': "profileUid_example",
    }
    try:
        # Get LQA profile details
        api_response = api_instance.get_lqa_profile(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->get_lqa_profile: %s\n" % e)
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
profileUid | ProfileUidSchema | | 

# ProfileUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_lqa_profile.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_lqa_profile.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_lqa_profile.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_lqa_profile.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_lqa_profile.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_lqa_profile.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_lqa_profile.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_lqa_profile.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_lqa_profile.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_lqa_profile.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_lqa_profile.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_lqa_profile.ApiResponseFor501) | Not implemented

#### get_lqa_profile.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LqaProfileDetailDto**](../../models/LqaProfileDetailDto.md) |  | 


#### get_lqa_profile.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_lqa_profile_authors**
<a id="get_lqa_profile_authors"></a>
> [UserReference] get_lqa_profile_authors()

Get list of LQA profile authors

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.user_reference import UserReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get list of LQA profile authors
        api_response = api_instance.get_lqa_profile_authors()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->get_lqa_profile_authors: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_lqa_profile_authors.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_lqa_profile_authors.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_lqa_profile_authors.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_lqa_profile_authors.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_lqa_profile_authors.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_lqa_profile_authors.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_lqa_profile_authors.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_lqa_profile_authors.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_lqa_profile_authors.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_lqa_profile_authors.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_lqa_profile_authors.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_lqa_profile_authors.ApiResponseFor501) | Not implemented

#### get_lqa_profile_authors.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UserReference**]({{complexTypePrefix}}UserReference.md) | [**UserReference**]({{complexTypePrefix}}UserReference.md) | [**UserReference**]({{complexTypePrefix}}UserReference.md) |  | 

#### get_lqa_profile_authors.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile_authors.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile_authors.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile_authors.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile_authors.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile_authors.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile_authors.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile_authors.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile_authors.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile_authors.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profile_authors.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_lqa_profiles**
<a id="get_lqa_profiles"></a>
> PageDtoLqaProfileReferenceDto get_lqa_profiles()

GET list LQA profiles

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.page_dto_lqa_profile_reference_dto import PageDtoLqaProfileReferenceDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'createdBy': "createdBy_example",
        'dateCreated': "dateCreated_example",
        'pageNumber': 0,
        'pageSize': 20,
        'sort': [
        "NAME"
    ],
        'order': [
        "ASC"
    ],
    }
    try:
        # GET list LQA profiles
        api_response = api_instance.get_lqa_profiles(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->get_lqa_profiles: %s\n" % e)
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
createdBy | CreatedBySchema | | optional
dateCreated | DateCreatedSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional
sort | SortSchema | | optional
order | OrderSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CreatedBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DateCreatedSchema

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
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20value must be a 32 bit integer

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["NAME", "CREATED_BY", "DATE_CREATED", ] 

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["ASC", "DESC", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_lqa_profiles.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_lqa_profiles.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_lqa_profiles.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_lqa_profiles.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_lqa_profiles.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_lqa_profiles.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_lqa_profiles.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_lqa_profiles.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_lqa_profiles.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_lqa_profiles.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_lqa_profiles.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_lqa_profiles.ApiResponseFor501) | Not implemented

#### get_lqa_profiles.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoLqaProfileReferenceDto**](../../models/PageDtoLqaProfileReferenceDto.md) |  | 


#### get_lqa_profiles.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profiles.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profiles.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profiles.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profiles.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profiles.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profiles.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profiles.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profiles.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profiles.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_lqa_profiles.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **make_default**
<a id="make_default"></a>
> LqaProfileReferenceDto make_default(profile_uid)

Make LQA profile default

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.lqa_profile_reference_dto import LqaProfileReferenceDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'profileUid': "profileUid_example",
    }
    try:
        # Make LQA profile default
        api_response = api_instance.make_default(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->make_default: %s\n" % e)
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
profileUid | ProfileUidSchema | | 

# ProfileUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#make_default.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#make_default.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#make_default.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#make_default.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#make_default.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#make_default.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#make_default.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#make_default.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#make_default.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#make_default.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#make_default.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#make_default.ApiResponseFor501) | Not implemented

#### make_default.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LqaProfileReferenceDto**](../../models/LqaProfileReferenceDto.md) |  | 


#### make_default.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### make_default.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### make_default.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### make_default.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### make_default.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### make_default.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### make_default.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### make_default.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### make_default.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### make_default.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### make_default.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **run_qa_for_job_part_v3**
<a id="run_qa_for_job_part_v3"></a>
> QualityAssuranceResponseDto run_qa_for_job_part_v3(project_uidjob_uid)

Run quality assurance

Call \"Get QA settings\" endpoint to get the list of enabled QA checks

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.quality_assurance_response_dto import QualityAssuranceResponseDto
from openapi_client.model.quality_assurance_run_dto_v3 import QualityAssuranceRunDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Run quality assurance
        api_response = api_instance.run_qa_for_job_part_v3(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->run_qa_for_job_part_v3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = QualityAssuranceRunDtoV3(
        initial_segment=SegmentReference(
            uid="uid_example",
        ),
        max_qa_warnings_count=1,
        warning_types=[
            "EmptyTranslation"
        ],
    )
    try:
        # Run quality assurance
        api_response = api_instance.run_qa_for_job_part_v3(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->run_qa_for_job_part_v3: %s\n" % e)
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
[**QualityAssuranceRunDtoV3**](../../models/QualityAssuranceRunDtoV3.md) |  | 


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
200 | [ApiResponseFor200](#run_qa_for_job_part_v3.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#run_qa_for_job_part_v3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#run_qa_for_job_part_v3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#run_qa_for_job_part_v3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#run_qa_for_job_part_v3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#run_qa_for_job_part_v3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#run_qa_for_job_part_v3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#run_qa_for_job_part_v3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#run_qa_for_job_part_v3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#run_qa_for_job_part_v3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#run_qa_for_job_part_v3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#run_qa_for_job_part_v3.ApiResponseFor501) | Not implemented

#### run_qa_for_job_part_v3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**QualityAssuranceResponseDto**](../../models/QualityAssuranceResponseDto.md) |  | 


#### run_qa_for_job_part_v3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_part_v3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_part_v3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_part_v3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_part_v3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_part_v3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_part_v3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_part_v3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_part_v3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_part_v3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_part_v3.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **run_qa_for_job_parts_v3**
<a id="run_qa_for_job_parts_v3"></a>
> QualityAssuranceResponseDto run_qa_for_job_parts_v3(project_uid)

Run quality assurance (batch)

Call \"Get QA settings\" endpoint to get the list of enabled QA checks

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.quality_assurance_response_dto import QualityAssuranceResponseDto
from openapi_client.model.quality_assurance_batch_run_dto_v3 import QualityAssuranceBatchRunDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Run quality assurance (batch)
        api_response = api_instance.run_qa_for_job_parts_v3(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->run_qa_for_job_parts_v3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = QualityAssuranceBatchRunDtoV3(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        settings=QualityAssuranceRunDtoV3(
            initial_segment=SegmentReference(
                uid="uid_example",
            ),
            max_qa_warnings_count=1,
            warning_types=[
                "EmptyTranslation"
            ],
        ),
        max_qa_warnings_count=1,
    )
    try:
        # Run quality assurance (batch)
        api_response = api_instance.run_qa_for_job_parts_v3(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->run_qa_for_job_parts_v3: %s\n" % e)
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
[**QualityAssuranceBatchRunDtoV3**](../../models/QualityAssuranceBatchRunDtoV3.md) |  | 


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
200 | [ApiResponseFor200](#run_qa_for_job_parts_v3.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#run_qa_for_job_parts_v3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#run_qa_for_job_parts_v3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#run_qa_for_job_parts_v3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#run_qa_for_job_parts_v3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#run_qa_for_job_parts_v3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#run_qa_for_job_parts_v3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#run_qa_for_job_parts_v3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#run_qa_for_job_parts_v3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#run_qa_for_job_parts_v3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#run_qa_for_job_parts_v3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#run_qa_for_job_parts_v3.ApiResponseFor501) | Not implemented

#### run_qa_for_job_parts_v3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**QualityAssuranceResponseDto**](../../models/QualityAssuranceResponseDto.md) |  | 


#### run_qa_for_job_parts_v3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_parts_v3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_parts_v3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_parts_v3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_parts_v3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_parts_v3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_parts_v3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_parts_v3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_parts_v3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_parts_v3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_job_parts_v3.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **run_qa_for_segments_v3**
<a id="run_qa_for_segments_v3"></a>
> QualityAssuranceResponseDto run_qa_for_segments_v3(project_uid)

Run quality assurance on selected segments

By default runs only fast running checks. Source and target language of jobs have to match.

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.quality_assurance_segments_run_dto_v3 import QualityAssuranceSegmentsRunDtoV3
from openapi_client.model.quality_assurance_response_dto import QualityAssuranceResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Run quality assurance on selected segments
        api_response = api_instance.run_qa_for_segments_v3(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->run_qa_for_segments_v3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = QualityAssuranceSegmentsRunDtoV3(
        jobs_and_segments=[
            JobPartSegmentsDtoV3(
                job=UidReference(
                    uid="uid_example",
                ),
                segments=[
                    "segments_example"
                ],
            )
        ],
        warning_types=[
            "EmptyTranslation"
        ],
        max_qa_warnings_count=1,
    )
    try:
        # Run quality assurance on selected segments
        api_response = api_instance.run_qa_for_segments_v3(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->run_qa_for_segments_v3: %s\n" % e)
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
[**QualityAssuranceSegmentsRunDtoV3**](../../models/QualityAssuranceSegmentsRunDtoV3.md) |  | 


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
200 | [ApiResponseFor200](#run_qa_for_segments_v3.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#run_qa_for_segments_v3.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#run_qa_for_segments_v3.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#run_qa_for_segments_v3.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#run_qa_for_segments_v3.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#run_qa_for_segments_v3.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#run_qa_for_segments_v3.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#run_qa_for_segments_v3.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#run_qa_for_segments_v3.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#run_qa_for_segments_v3.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#run_qa_for_segments_v3.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#run_qa_for_segments_v3.ApiResponseFor501) | Not implemented

#### run_qa_for_segments_v3.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**QualityAssuranceResponseDto**](../../models/QualityAssuranceResponseDto.md) |  | 


#### run_qa_for_segments_v3.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_segments_v3.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_segments_v3.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_segments_v3.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_segments_v3.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_segments_v3.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_segments_v3.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_segments_v3.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_segments_v3.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_segments_v3.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### run_qa_for_segments_v3.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_ignored_checks**
<a id="update_ignored_checks"></a>
> update_ignored_checks(project_uidjob_uid)

Edit ignored checks

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.update_ignored_checks_dto import UpdateIgnoredChecksDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Edit ignored checks
        api_response = api_instance.update_ignored_checks(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->update_ignored_checks: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    body = UpdateIgnoredChecksDto(
        segment=SegmentReference(
            uid="uid_example",
        ),
        warning_types=[
            "EmptyTranslation"
        ],
    )
    try:
        # Edit ignored checks
        api_response = api_instance.update_ignored_checks(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->update_ignored_checks: %s\n" % e)
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
[**UpdateIgnoredChecksDto**](../../models/UpdateIgnoredChecksDto.md) |  | 


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
204 | [ApiResponseFor204](#update_ignored_checks.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#update_ignored_checks.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_ignored_checks.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_ignored_checks.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_ignored_checks.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_ignored_checks.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_ignored_checks.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_ignored_checks.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_ignored_checks.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_ignored_checks.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_ignored_checks.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_ignored_checks.ApiResponseFor501) | Not implemented

#### update_ignored_checks.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_ignored_checks.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_lqa_profile**
<a id="update_lqa_profile"></a>
> LqaProfileDetailDto update_lqa_profile(profile_uid)

Update LQA profile

### Example

```python
import openapi_client
from openapi_client.apis.tags import quality_assurance_api
from openapi_client.model.update_lqa_profile_dto import UpdateLqaProfileDto
from openapi_client.model.lqa_profile_detail_dto import LqaProfileDetailDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quality_assurance_api.QualityAssuranceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'profileUid': "profileUid_example",
    }
    try:
        # Update LQA profile
        api_response = api_instance.update_lqa_profile(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->update_lqa_profile: %s\n" % e)

    # example passing only optional values
    path_params = {
        'profileUid': "profileUid_example",
    }
    body = UpdateLqaProfileDto(
        name="name_example",
        error_categories=ErrorCategoriesDto(
            accuracy=AccuracyWeightsDto(
                accuracy=ToggleableWeightDto(
                    enabled=True,
                    weight=1,
                    code=1,
                ),
,
,
,
,
,
,
,
            ),
            fluency=FluencyWeightsDto(
                fluency=ToggleableWeightDto(),
                punctuation=ToggleableWeightDto(),
                spelling=ToggleableWeightDto(),
                grammar=ToggleableWeightDto(),
                grammatical_register=ToggleableWeightDto(),
                inconsistency=ToggleableWeightDto(),
                cross_reference=ToggleableWeightDto(),
                character_encoding=ToggleableWeightDto(),
            ),
            terminology=TerminologyWeightsDto(
                terminology=ToggleableWeightDto(),
                inconsistent_with_tb=ToggleableWeightDto(),
                inconsistent_use_of_terminology=ToggleableWeightDto(),
            ),
            style=StyleWeightsDto(
                style=ToggleableWeightDto(),
                awkward=ToggleableWeightDto(),
                company_style=ToggleableWeightDto(),
                inconsistent_style=ToggleableWeightDto(),
                third_party_style=ToggleableWeightDto(),
                unidiomatic=ToggleableWeightDto(),
            ),
            locale_convention=LocaleConventionWeightsDto(
                locale_convention=ToggleableWeightDto(),
                address_format=ToggleableWeightDto(),
                date_format=ToggleableWeightDto(),
                currency_format=ToggleableWeightDto(),
                measurement_format=ToggleableWeightDto(),
                shortcut_key=ToggleableWeightDto(),
                telephone_format=ToggleableWeightDto(),
            ),
            verity=VerityWeightsDto(
                verity=ToggleableWeightDto(),
                culture_specific_reference=ToggleableWeightDto(),
            ),
            design=DesignWeightsDto(
                design=ToggleableWeightDto(),
                length=ToggleableWeightDto(),
                local_formatting=ToggleableWeightDto(),
                markup=ToggleableWeightDto(),
                missing_text=ToggleableWeightDto(),
                truncation=ToggleableWeightDto(),
            ),
            other=OtherWeightsDto(
                other=ToggleableWeightDto(),
            ),
        ),
        penalty_points=PenaltyPointsDto(
            neutral=SeverityDto(
                code=1,
                value=3.14,
            ),
,
,
,
        ),
        pass_fail_threshold=PassFailThresholdDto(
            min_score_percentage=99,
        ),
    )
    try:
        # Update LQA profile
        api_response = api_instance.update_lqa_profile(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling QualityAssuranceApi->update_lqa_profile: %s\n" % e)
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
[**UpdateLqaProfileDto**](../../models/UpdateLqaProfileDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
profileUid | ProfileUidSchema | | 

# ProfileUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_lqa_profile.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#update_lqa_profile.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_lqa_profile.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_lqa_profile.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_lqa_profile.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_lqa_profile.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_lqa_profile.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_lqa_profile.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_lqa_profile.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_lqa_profile.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_lqa_profile.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_lqa_profile.ApiResponseFor501) | Not implemented

#### update_lqa_profile.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LqaProfileDetailDto**](../../models/LqaProfileDetailDto.md) |  | 


#### update_lqa_profile.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_lqa_profile.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_lqa_profile.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_lqa_profile.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_lqa_profile.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_lqa_profile.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_lqa_profile.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_lqa_profile.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_lqa_profile.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_lqa_profile.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_lqa_profile.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

