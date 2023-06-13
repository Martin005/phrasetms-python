<a id="__pageTop"></a>
# openapi_client.apis.tags.term_base_api.TermBaseApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browse_terms**](#browse_terms) | **post** /api2/v1/termBases/{termBaseUid}/browse | Browse term base
[**clear_term_base**](#clear_term_base) | **delete** /api2/v1/termBases/{termBaseUid}/terms | Clear term base
[**create_concept**](#create_concept) | **post** /api2/v1/termBases/{termBaseUid}/concepts | Create concept
[**create_term**](#create_term) | **post** /api2/v1/termBases/{termBaseUid}/terms | Create term
[**create_term_base**](#create_term_base) | **post** /api2/v1/termBases | Create term base
[**create_term_by_job**](#create_term_by_job) | **post** /api2/v1/projects/{projectUid}/jobs/{jobUid}/termBases/createByJob | Create term in job&#x27;s term bases
[**delete_concept**](#delete_concept) | **delete** /api2/v1/termBases/{termBaseUid}/concepts/{conceptId} | Delete concept
[**delete_concepts**](#delete_concepts) | **delete** /api2/v1/termBases/{termBaseUid}/concepts | Delete concepts
[**delete_term**](#delete_term) | **delete** /api2/v1/termBases/{termBaseUid}/terms/{termId} | Delete term
[**delete_term_base**](#delete_term_base) | **delete** /api2/v1/termBases/{termBaseUid} | Delete term base
[**export_term_base**](#export_term_base) | **get** /api2/v1/termBases/{termBaseUid}/export | Export term base
[**get_concept**](#get_concept) | **get** /api2/v1/termBases/{termBaseUid}/concepts/{conceptUid} | Get concept
[**get_last_background_task**](#get_last_background_task) | **get** /api2/v1/termBases/{termBaseUid}/lastBackgroundTask | Last import status
[**get_project_template_term_bases**](#get_project_template_term_bases) | **get** /api2/v1/projectTemplates/{projectTemplateUid}/termBases | Get term bases
[**get_project_term_bases**](#get_project_term_bases) | **get** /api2/v1/projects/{projectUid}/termBases | Get term bases
[**get_term**](#get_term) | **get** /api2/v1/termBases/{termBaseUid}/terms/{termId} | Get term
[**get_term_base**](#get_term_base) | **get** /api2/v1/termBases/{termBaseUid} | Get term base
[**get_term_base_metadata**](#get_term_base_metadata) | **get** /api2/v1/termBases/{termBaseUid}/metadata | Get term base metadata
[**get_translation_resources**](#get_translation_resources) | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources | Get translation resources
[**import_term_base**](#import_term_base) | **post** /api2/v1/termBases/{termBaseUid}/upload | Upload term base
[**list_concepts**](#list_concepts) | **get** /api2/v1/termBases/{termBaseUid}/concepts | List concepts
[**list_term_bases**](#list_term_bases) | **get** /api2/v1/termBases | List term bases
[**list_terms_of_concept**](#list_terms_of_concept) | **get** /api2/v1/termBases/{termBaseUid}/concepts/{conceptId}/terms | Get terms of concept
[**relevant_term_bases**](#relevant_term_bases) | **get** /api2/v1/projects/{projectUid}/termBases/relevant | List project relevant term bases
[**search_terms**](#search_terms) | **post** /api2/v1/termBases/{termBaseUid}/search | Search term base
[**search_terms_by_job1**](#search_terms_by_job1) | **post** /api2/v2/projects/{projectUid}/jobs/{jobUid}/termBases/searchByJob | Search job&#x27;s term bases
[**search_terms_in_text_by_job_v2**](#search_terms_in_text_by_job_v2) | **post** /api2/v2/projects/{projectUid}/jobs/{jobUid}/termBases/searchInTextByJob | Search terms in text
[**set_project_template_term_bases**](#set_project_template_term_bases) | **put** /api2/v1/projectTemplates/{projectTemplateUid}/termBases | Edit term bases in project template
[**set_project_term_bases**](#set_project_term_bases) | **put** /api2/v1/projects/{projectUid}/termBases | Edit term bases
[**update_concept**](#update_concept) | **put** /api2/v1/termBases/{termBaseUid}/concepts/{conceptUid} | Update concept
[**update_term**](#update_term) | **put** /api2/v1/termBases/{termBaseUid}/terms/{termId} | Edit term
[**update_term_base**](#update_term_base) | **put** /api2/v1/termBases/{termBaseUid} | Edit term base

# **browse_terms**
<a id="browse_terms"></a>
> BrowseResponseListDto browse_terms(term_base_uid)

Browse term base

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.browse_response_list_dto import BrowseResponseListDto
from openapi_client.model.browse_request_dto import BrowseRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    try:
        # Browse term base
        api_response = api_instance.browse_terms(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->browse_terms: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    body = BrowseRequestDto(
        query_lang="query_lang_example",
        query="query_example",
        status="status_example",
        page_number=1,
        page_size=1,
    )
    try:
        # Browse term base
        api_response = api_instance.browse_terms(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->browse_terms: %s\n" % e)
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
[**BrowseRequestDto**](../../models/BrowseRequestDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#browse_terms.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#browse_terms.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#browse_terms.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#browse_terms.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#browse_terms.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#browse_terms.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#browse_terms.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#browse_terms.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#browse_terms.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#browse_terms.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#browse_terms.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#browse_terms.ApiResponseFor501) | Not implemented

#### browse_terms.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BrowseResponseListDto**](../../models/BrowseResponseListDto.md) |  | 


#### browse_terms.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### browse_terms.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### browse_terms.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### browse_terms.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### browse_terms.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### browse_terms.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### browse_terms.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### browse_terms.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### browse_terms.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### browse_terms.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### browse_terms.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **clear_term_base**
<a id="clear_term_base"></a>
> clear_term_base(term_base_uid)

Clear term base

Deletes all terms

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    try:
        # Clear term base
        api_response = api_instance.clear_term_base(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->clear_term_base: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#clear_term_base.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#clear_term_base.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#clear_term_base.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#clear_term_base.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#clear_term_base.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#clear_term_base.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#clear_term_base.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#clear_term_base.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#clear_term_base.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#clear_term_base.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#clear_term_base.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#clear_term_base.ApiResponseFor501) | Not implemented

#### clear_term_base.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### clear_term_base.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_concept**
<a id="create_concept"></a>
> ConceptWithMetadataDto create_concept(term_base_uid)

Create concept

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.concept_with_metadata_dto import ConceptWithMetadataDto
from openapi_client.model.concept_edit_dto import ConceptEditDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    try:
        # Create concept
        api_response = api_instance.create_concept(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->create_concept: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    body = ConceptEditDto(
        domain=UidReference(
            uid="uid_example",
        ),
        subdomains=[
            UidReference()
        ],
        definition="definition_example",
        url="url_example",
        concept_note="concept_note_example",
    )
    try:
        # Create concept
        api_response = api_instance.create_concept(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->create_concept: %s\n" % e)
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
[**ConceptEditDto**](../../models/ConceptEditDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_concept.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_concept.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_concept.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_concept.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_concept.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_concept.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_concept.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_concept.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_concept.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_concept.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_concept.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_concept.ApiResponseFor501) | Not implemented

#### create_concept.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConceptWithMetadataDto**](../../models/ConceptWithMetadataDto.md) |  | 


#### create_concept.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_concept.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_concept.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_concept.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_concept.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_concept.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_concept.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_concept.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_concept.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_concept.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_concept.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_term**
<a id="create_term"></a>
> TermDto create_term(term_base_uid)

Create term

Set conceptId to assign the term to an existing concept, otherwise a new concept will be created.

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.term_dto import TermDto
from openapi_client.model.term_create_dto import TermCreateDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    try:
        # Create term
        api_response = api_instance.create_term(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->create_term: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    body = TermCreateDto(
        text="text_example",
        lang="lang_example",
        case_sensitive=True,
        exact_match=True,
        forbidden=True,
        preferred=True,
        status="New",
        concept_id="concept_id_example",
        usage="usage_example",
        note="note_example",
        short_translation="short_translation_example",
        term_type="FULL_FORM",
        part_of_speech="ADJECTIVE",
        gender="MASCULINE",
        number="SINGULAR",
    )
    try:
        # Create term
        api_response = api_instance.create_term(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->create_term: %s\n" % e)
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
[**TermCreateDto**](../../models/TermCreateDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_term.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_term.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_term.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_term.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_term.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_term.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_term.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_term.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_term.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_term.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_term.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_term.ApiResponseFor501) | Not implemented

#### create_term.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TermDto**](../../models/TermDto.md) |  | 


#### create_term.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_term_base**
<a id="create_term_base"></a>
> TermBaseDto create_term_base()

Create term base

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.term_base_edit_dto import TermBaseEditDto
from openapi_client.model.term_base_dto import TermBaseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only optional values
    body = TermBaseEditDto(
        name="name_example",
        langs=[
            "langs_example"
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
        # Create term base
        api_response = api_instance.create_term_base(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->create_term_base: %s\n" % e)
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
[**TermBaseEditDto**](../../models/TermBaseEditDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_term_base.ApiResponseFor200) | Created
400 | [ApiResponseFor400](#create_term_base.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_term_base.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_term_base.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_term_base.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_term_base.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_term_base.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_term_base.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_term_base.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_term_base.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_term_base.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_term_base.ApiResponseFor501) | Not implemented

#### create_term_base.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TermBaseDto**](../../models/TermBaseDto.md) |  | 


#### create_term_base.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_base.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_base.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_base.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_base.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_base.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_base.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_base.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_base.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_base.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_base.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_term_by_job**
<a id="create_term_by_job"></a>
> TermPairDto create_term_by_job(job_uidproject_uid)

Create term in job's term bases

Create new term in the write term base assigned to the job

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.create_terms_dto import CreateTermsDto
from openapi_client.model.term_pair_dto import TermPairDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->create_term_by_job: %s\n" % e)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->create_term_by_job: %s\n" % e)
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
[**CreateTermsDto**](../../models/CreateTermsDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
jobUid | JobUidSchema | | 
projectUid | ProjectUidSchema | | 

# JobUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_term_by_job.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#create_term_by_job.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_term_by_job.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_term_by_job.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_term_by_job.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_term_by_job.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_term_by_job.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_term_by_job.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_term_by_job.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_term_by_job.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_term_by_job.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_term_by_job.ApiResponseFor501) | Not implemented

#### create_term_by_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TermPairDto**](../../models/TermPairDto.md) |  | 


#### create_term_by_job.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_by_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_by_job.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_by_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_by_job.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_by_job.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_by_job.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_by_job.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_by_job.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_by_job.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_term_by_job.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_concept**
<a id="delete_concept"></a>
> delete_concept(term_base_uidconcept_id)

Delete concept

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
        'conceptId': "conceptId_example",
    }
    try:
        # Delete concept
        api_response = api_instance.delete_concept(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->delete_concept: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 
conceptId | ConceptIdSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConceptIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_concept.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_concept.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_concept.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_concept.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_concept.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_concept.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_concept.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_concept.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_concept.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_concept.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_concept.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_concept.ApiResponseFor501) | Not implemented

#### delete_concept.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concept.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_concepts**
<a id="delete_concepts"></a>
> delete_concepts(term_base_uid)

Delete concepts

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.concept_list_reference import ConceptListReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    try:
        # Delete concepts
        api_response = api_instance.delete_concepts(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->delete_concepts: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    body = ConceptListReference(
        concepts=[
            IdReference(
                id="id_example",
            )
        ],
    )
    try:
        # Delete concepts
        api_response = api_instance.delete_concepts(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->delete_concepts: %s\n" % e)
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
[**ConceptListReference**](../../models/ConceptListReference.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_concepts.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_concepts.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_concepts.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_concepts.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_concepts.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_concepts.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_concepts.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_concepts.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_concepts.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_concepts.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_concepts.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_concepts.ApiResponseFor501) | Not implemented

#### delete_concepts.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_concepts.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_term**
<a id="delete_term"></a>
> delete_term(term_base_uidterm_id)

Delete term

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
        'termId': "termId_example",
    }
    try:
        # Delete term
        api_response = api_instance.delete_term(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->delete_term: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 
termId | TermIdSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TermIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_term.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_term.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_term.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_term.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_term.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_term.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_term.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_term.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_term.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_term.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_term.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_term.ApiResponseFor501) | Not implemented

#### delete_term.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_term_base**
<a id="delete_term_base"></a>
> delete_term_base(term_base_uid)

Delete term base

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    query_params = {
    }
    try:
        # Delete term base
        api_response = api_instance.delete_term_base(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->delete_term_base: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    query_params = {
        'purge': False,
    }
    try:
        # Delete term base
        api_response = api_instance.delete_term_base(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->delete_term_base: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_term_base.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_term_base.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#delete_term_base.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#delete_term_base.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_term_base.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#delete_term_base.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#delete_term_base.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#delete_term_base.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#delete_term_base.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#delete_term_base.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#delete_term_base.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#delete_term_base.ApiResponseFor501) | Not implemented

#### delete_term_base.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### delete_term_base.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_term_base**
<a id="export_term_base"></a>
> export_term_base(term_base_uid)

Export term base

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    query_params = {
    }
    try:
        # Export term base
        api_response = api_instance.export_term_base(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->export_term_base: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    query_params = {
        'format': "Tbx",
        'charset': "UTF-8",
        'termStatus': "NEW",
    }
    try:
        # Export term base
        api_response = api_instance.export_term_base(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->export_term_base: %s\n" % e)
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
charset | CharsetSchema | | optional
termStatus | TermStatusSchema | | optional


# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["Tbx", "Xlsx", ] if omitted the server will use the default value of "Tbx"

# CharsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "UTF-8"

# TermStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NEW", "APPROVED", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_term_base.ApiResponseFor200) | application/octet-stream
400 | [ApiResponseFor400](#export_term_base.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#export_term_base.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#export_term_base.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#export_term_base.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#export_term_base.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#export_term_base.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#export_term_base.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#export_term_base.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#export_term_base.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#export_term_base.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#export_term_base.ApiResponseFor501) | Not implemented

#### export_term_base.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### export_term_base.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_concept**
<a id="get_concept"></a>
> ConceptWithMetadataDto get_concept(term_base_uidconcept_uid)

Get concept

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.concept_with_metadata_dto import ConceptWithMetadataDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
        'conceptUid': "conceptUid_example",
    }
    try:
        # Get concept
        api_response = api_instance.get_concept(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->get_concept: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 
conceptUid | ConceptUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConceptUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_concept.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_concept.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_concept.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_concept.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_concept.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_concept.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_concept.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_concept.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_concept.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_concept.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_concept.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_concept.ApiResponseFor501) | Not implemented

#### get_concept.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConceptWithMetadataDto**](../../models/ConceptWithMetadataDto.md) |  | 


#### get_concept.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_concept.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_concept.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_concept.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_concept.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_concept.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_concept.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_concept.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_concept.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_concept.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_concept.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_last_background_task**
<a id="get_last_background_task"></a>
> BackgroundTasksTbDto get_last_background_task(term_base_uid)

Last import status

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.background_tasks_tb_dto import BackgroundTasksTbDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    try:
        # Last import status
        api_response = api_instance.get_last_background_task(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->get_last_background_task: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_last_background_task.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_last_background_task.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_last_background_task.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_last_background_task.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_last_background_task.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_last_background_task.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_last_background_task.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_last_background_task.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_last_background_task.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_last_background_task.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_last_background_task.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_last_background_task.ApiResponseFor501) | Not implemented

#### get_last_background_task.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BackgroundTasksTbDto**](../../models/BackgroundTasksTbDto.md) |  | 


#### get_last_background_task.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_last_background_task.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_last_background_task.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_last_background_task.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_last_background_task.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_last_background_task.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_last_background_task.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_last_background_task.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_last_background_task.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_last_background_task.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_last_background_task.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_template_term_bases**
<a id="get_project_template_term_bases"></a>
> ProjectTemplateTermBaseListDto get_project_template_term_bases(project_template_uid)

Get term bases

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.project_template_term_base_list_dto import ProjectTemplateTermBaseListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Get term bases
        api_response = api_instance.get_project_template_term_bases(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->get_project_template_term_bases: %s\n" % e)
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
200 | [ApiResponseFor200](#get_project_template_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_template_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_template_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_template_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_template_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_template_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_template_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_template_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_template_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_template_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_template_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_template_term_bases.ApiResponseFor501) | Not implemented

#### get_project_template_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTemplateTermBaseListDto**](../../models/ProjectTemplateTermBaseListDto.md) |  | 


#### get_project_template_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_template_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_term_bases**
<a id="get_project_term_bases"></a>
> ProjectTermBaseListDto get_project_term_bases(project_uid)

Get term bases

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.project_term_base_list_dto import ProjectTermBaseListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get term bases
        api_response = api_instance.get_project_term_bases(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->get_project_term_bases: %s\n" % e)
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
200 | [ApiResponseFor200](#get_project_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_project_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_project_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_project_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_project_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_project_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_project_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_project_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_project_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_project_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_project_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_project_term_bases.ApiResponseFor501) | Not implemented

#### get_project_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTermBaseListDto**](../../models/ProjectTermBaseListDto.md) |  | 


#### get_project_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_project_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_term**
<a id="get_term"></a>
> TermDto get_term(term_base_uidterm_id)

Get term

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.term_dto import TermDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
        'termId': "termId_example",
    }
    try:
        # Get term
        api_response = api_instance.get_term(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->get_term: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 
termId | TermIdSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TermIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_term.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_term.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_term.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_term.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_term.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_term.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_term.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_term.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_term.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_term.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_term.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_term.ApiResponseFor501) | Not implemented

#### get_term.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TermDto**](../../models/TermDto.md) |  | 


#### get_term.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_term_base**
<a id="get_term_base"></a>
> TermBaseDto get_term_base(term_base_uid)

Get term base

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.term_base_dto import TermBaseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    try:
        # Get term base
        api_response = api_instance.get_term_base(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->get_term_base: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_term_base.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_term_base.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_term_base.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_term_base.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_term_base.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_term_base.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_term_base.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_term_base.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_term_base.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_term_base.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_term_base.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_term_base.ApiResponseFor501) | Not implemented

#### get_term_base.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TermBaseDto**](../../models/TermBaseDto.md) |  | 


#### get_term_base.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_term_base_metadata**
<a id="get_term_base_metadata"></a>
> MetadataTbDto get_term_base_metadata(term_base_uid)

Get term base metadata

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.metadata_tb_dto import MetadataTbDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    try:
        # Get term base metadata
        api_response = api_instance.get_term_base_metadata(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->get_term_base_metadata: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_term_base_metadata.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_term_base_metadata.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_term_base_metadata.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_term_base_metadata.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_term_base_metadata.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_term_base_metadata.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_term_base_metadata.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_term_base_metadata.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_term_base_metadata.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_term_base_metadata.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_term_base_metadata.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_term_base_metadata.ApiResponseFor501) | Not implemented

#### get_term_base_metadata.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MetadataTbDto**](../../models/MetadataTbDto.md) |  | 


#### get_term_base_metadata.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base_metadata.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base_metadata.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base_metadata.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base_metadata.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base_metadata.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base_metadata.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base_metadata.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base_metadata.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base_metadata.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_term_base_metadata.ApiResponseFor501
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
from openapi_client.apis.tags import term_base_api
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
    api_instance = term_base_api.TermBaseApi(api_client)

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
        print("Exception when calling TermBaseApi->get_translation_resources: %s\n" % e)
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

# **import_term_base**
<a id="import_term_base"></a>
> ImportTermBaseResponseDto import_term_base(content_dispositionterm_base_uid)

Upload term base

 Terms can be imported from XLS/XLSX and TBX file formats into a term base. See <a target=\"_blank\" href=\"https://support.phrase.com/hc/en-us/articles/5709733372188\">Phrase Help Center</a> 

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.import_term_base_response_dto import ImportTermBaseResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    query_params = {
    }
    header_params = {
        'Content-Disposition': "Content-Disposition_example",
    }
    try:
        # Upload term base
        api_response = api_instance.import_term_base(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->import_term_base: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    query_params = {
        'charset': "UTF-8",
        'strictLangMatching': False,
        'updateTerms': True,
    }
    header_params = {
        'Content-Disposition': "Content-Disposition_example",
    }
    body = dict()
    try:
        # Upload term base
        api_response = api_instance.import_term_base(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->import_term_base: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset |
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

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
charset | CharsetSchema | | optional
strictLangMatching | StrictLangMatchingSchema | | optional
updateTerms | UpdateTermsSchema | | optional


# CharsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "UTF-8"

# StrictLangMatchingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# UpdateTermsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Disposition | ContentDispositionSchema | | 

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
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#import_term_base.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#import_term_base.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#import_term_base.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#import_term_base.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#import_term_base.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#import_term_base.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#import_term_base.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#import_term_base.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#import_term_base.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#import_term_base.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#import_term_base.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#import_term_base.ApiResponseFor501) | Not implemented

#### import_term_base.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImportTermBaseResponseDto**](../../models/ImportTermBaseResponseDto.md) |  | 


#### import_term_base.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_term_base.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_term_base.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_term_base.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_term_base.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_term_base.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_term_base.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_term_base.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_term_base.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_term_base.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### import_term_base.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_concepts**
<a id="list_concepts"></a>
> ConceptListResponseDto list_concepts(term_base_uid)

List concepts

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.concept_list_response_dto import ConceptListResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    query_params = {
    }
    try:
        # List concepts
        api_response = api_instance.list_concepts(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->list_concepts: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List concepts
        api_response = api_instance.list_concepts(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->list_concepts: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_concepts.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_concepts.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_concepts.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_concepts.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_concepts.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_concepts.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_concepts.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_concepts.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_concepts.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_concepts.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_concepts.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_concepts.ApiResponseFor501) | Not implemented

#### list_concepts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConceptListResponseDto**](../../models/ConceptListResponseDto.md) |  | 


#### list_concepts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_concepts.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_concepts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_concepts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_concepts.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_concepts.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_concepts.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_concepts.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_concepts.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_concepts.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_concepts.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_term_bases**
<a id="list_term_bases"></a>
> PageDtoTermBaseDto list_term_bases()

List term bases

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.page_dto_term_base_dto import PageDtoTermBaseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'lang': [
        "lang_example"
    ],
        'clientId': "clientId_example",
        'domainId': "domainId_example",
        'subDomainId': "subDomainId_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List term bases
        api_response = api_instance.list_term_bases(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->list_term_bases: %s\n" % e)
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
lang | LangSchema | | optional
clientId | ClientIdSchema | | optional
domainId | DomainIdSchema | | optional
subDomainId | SubDomainIdSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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
200 | [ApiResponseFor200](#list_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_term_bases.ApiResponseFor501) | Not implemented

#### list_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoTermBaseDto**](../../models/PageDtoTermBaseDto.md) |  | 


#### list_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_terms_of_concept**
<a id="list_terms_of_concept"></a>
> ConceptDto list_terms_of_concept(term_base_uidconcept_id)

Get terms of concept

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.concept_dto import ConceptDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
        'conceptId': "conceptId_example",
    }
    try:
        # Get terms of concept
        api_response = api_instance.list_terms_of_concept(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->list_terms_of_concept: %s\n" % e)
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
termBaseUid | TermBaseUidSchema | | 
conceptId | ConceptIdSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConceptIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_terms_of_concept.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_terms_of_concept.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_terms_of_concept.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_terms_of_concept.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_terms_of_concept.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_terms_of_concept.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_terms_of_concept.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_terms_of_concept.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_terms_of_concept.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_terms_of_concept.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_terms_of_concept.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_terms_of_concept.ApiResponseFor501) | Not implemented

#### list_terms_of_concept.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConceptDto**](../../models/ConceptDto.md) |  | 


#### list_terms_of_concept.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_terms_of_concept.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_terms_of_concept.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_terms_of_concept.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_terms_of_concept.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_terms_of_concept.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_terms_of_concept.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_terms_of_concept.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_terms_of_concept.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_terms_of_concept.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_terms_of_concept.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **relevant_term_bases**
<a id="relevant_term_bases"></a>
> PageDtoTermBaseDto relevant_term_bases(project_uid)

List project relevant term bases

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.page_dto_term_base_dto import PageDtoTermBaseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # List project relevant term bases
        api_response = api_instance.relevant_term_bases(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->relevant_term_bases: %s\n" % e)

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
        # List project relevant term bases
        api_response = api_instance.relevant_term_bases(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->relevant_term_bases: %s\n" % e)
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
200 | [ApiResponseFor200](#relevant_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#relevant_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#relevant_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#relevant_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#relevant_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#relevant_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#relevant_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#relevant_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#relevant_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#relevant_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#relevant_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#relevant_term_bases.ApiResponseFor501) | Not implemented

#### relevant_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoTermBaseDto**](../../models/PageDtoTermBaseDto.md) |  | 


#### relevant_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### relevant_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_terms**
<a id="search_terms"></a>
> SearchResponseListTbDto search_terms(term_base_uid)

Search term base

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.search_response_list_tb_dto import SearchResponseListTbDto
from openapi_client.model.term_base_search_request_dto import TermBaseSearchRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    try:
        # Search term base
        api_response = api_instance.search_terms(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->search_terms: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    body = TermBaseSearchRequestDto(
        target_langs=[
            "target_langs_example"
        ],
        source_lang="source_lang_example",
        query="query_example",
        status="New",
    )
    try:
        # Search term base
        api_response = api_instance.search_terms(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->search_terms: %s\n" % e)
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
[**TermBaseSearchRequestDto**](../../models/TermBaseSearchRequestDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_terms.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#search_terms.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#search_terms.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#search_terms.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_terms.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#search_terms.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#search_terms.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#search_terms.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#search_terms.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#search_terms.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#search_terms.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#search_terms.ApiResponseFor501) | Not implemented

#### search_terms.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchResponseListTbDto**](../../models/SearchResponseListTbDto.md) |  | 


#### search_terms.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_terms_by_job1**
<a id="search_terms_by_job1"></a>
> SearchTbResponseListDto search_terms_by_job1(job_uidproject_uid)

Search job's term bases

Search all read term bases assigned to the job

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.search_tb_by_job_request_dto import SearchTbByJobRequestDto
from openapi_client.model.search_tb_response_list_dto import SearchTbResponseListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->search_terms_by_job1: %s\n" % e)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->search_terms_by_job1: %s\n" % e)
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
[**SearchTbByJobRequestDto**](../../models/SearchTbByJobRequestDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
jobUid | JobUidSchema | | 
projectUid | ProjectUidSchema | | 

# JobUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_terms_by_job1.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#search_terms_by_job1.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#search_terms_by_job1.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#search_terms_by_job1.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_terms_by_job1.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#search_terms_by_job1.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#search_terms_by_job1.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#search_terms_by_job1.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#search_terms_by_job1.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#search_terms_by_job1.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#search_terms_by_job1.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#search_terms_by_job1.ApiResponseFor501) | Not implemented

#### search_terms_by_job1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchTbResponseListDto**](../../models/SearchTbResponseListDto.md) |  | 


#### search_terms_by_job1.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_by_job1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_by_job1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_by_job1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_by_job1.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_by_job1.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_by_job1.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_by_job1.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_by_job1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_by_job1.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_by_job1.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_terms_in_text_by_job_v2**
<a id="search_terms_in_text_by_job_v2"></a>
> SearchInTextResponseList2Dto search_terms_in_text_by_job_v2(job_uidproject_uid)

Search terms in text

Search in text in all read term bases assigned to the job

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.search_tb_in_text_by_job_request_dto import SearchTbInTextByJobRequestDto
from openapi_client.model.search_in_text_response_list2_dto import SearchInTextResponseList2Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->search_terms_in_text_by_job_v2: %s\n" % e)

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
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->search_terms_in_text_by_job_v2: %s\n" % e)
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
[**SearchTbInTextByJobRequestDto**](../../models/SearchTbInTextByJobRequestDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
jobUid | JobUidSchema | | 
projectUid | ProjectUidSchema | | 

# JobUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_terms_in_text_by_job_v2.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#search_terms_in_text_by_job_v2.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#search_terms_in_text_by_job_v2.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#search_terms_in_text_by_job_v2.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#search_terms_in_text_by_job_v2.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#search_terms_in_text_by_job_v2.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#search_terms_in_text_by_job_v2.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#search_terms_in_text_by_job_v2.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#search_terms_in_text_by_job_v2.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#search_terms_in_text_by_job_v2.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#search_terms_in_text_by_job_v2.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#search_terms_in_text_by_job_v2.ApiResponseFor501) | Not implemented

#### search_terms_in_text_by_job_v2.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchInTextResponseList2Dto**](../../models/SearchInTextResponseList2Dto.md) |  | 


#### search_terms_in_text_by_job_v2.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### search_terms_in_text_by_job_v2.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_project_template_term_bases**
<a id="set_project_template_term_bases"></a>
> ProjectTemplateTermBaseListDto set_project_template_term_bases(project_template_uid)

Edit term bases in project template

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.project_template_term_base_list_dto import ProjectTemplateTermBaseListDto
from openapi_client.model.set_project_template_term_base_dto import SetProjectTemplateTermBaseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    try:
        # Edit term bases in project template
        api_response = api_instance.set_project_template_term_bases(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->set_project_template_term_bases: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectTemplateUid': "projectTemplateUid_example",
    }
    body = SetProjectTemplateTermBaseDto(
        read_term_bases=[
            IdReference(
                id="id_example",
            )
        ],
,
,
        target_lang="target_lang_example",
,
    )
    try:
        # Edit term bases in project template
        api_response = api_instance.set_project_template_term_bases(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->set_project_template_term_bases: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetProjectTemplateTermBaseDto**](../../models/SetProjectTemplateTermBaseDto.md) |  | 


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
200 | [ApiResponseFor200](#set_project_template_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#set_project_template_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_project_template_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_project_template_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_project_template_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_project_template_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_project_template_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_project_template_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_project_template_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_project_template_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_project_template_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_project_template_term_bases.ApiResponseFor501) | Not implemented

#### set_project_template_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTemplateTermBaseListDto**](../../models/ProjectTemplateTermBaseListDto.md) |  | 


#### set_project_template_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_template_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_project_term_bases**
<a id="set_project_term_bases"></a>
> ProjectTermBaseListDto set_project_term_bases(project_uid)

Edit term bases

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.set_term_base_dto import SetTermBaseDto
from openapi_client.model.project_term_base_list_dto import ProjectTermBaseListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Edit term bases
        api_response = api_instance.set_project_term_bases(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->set_project_term_bases: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = SetTermBaseDto(
        read_term_bases=[
            IdReference(
                id="id_example",
            )
        ],
,
,
        target_lang="target_lang_example",
    )
    try:
        # Edit term bases
        api_response = api_instance.set_project_term_bases(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->set_project_term_bases: %s\n" % e)
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
[**SetTermBaseDto**](../../models/SetTermBaseDto.md) |  | 


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
200 | [ApiResponseFor200](#set_project_term_bases.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#set_project_term_bases.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#set_project_term_bases.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#set_project_term_bases.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#set_project_term_bases.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#set_project_term_bases.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#set_project_term_bases.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#set_project_term_bases.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#set_project_term_bases.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#set_project_term_bases.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#set_project_term_bases.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#set_project_term_bases.ApiResponseFor501) | Not implemented

#### set_project_term_bases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectTermBaseListDto**](../../models/ProjectTermBaseListDto.md) |  | 


#### set_project_term_bases.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### set_project_term_bases.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_concept**
<a id="update_concept"></a>
> ConceptWithMetadataDto update_concept(term_base_uidconcept_uid)

Update concept

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.concept_with_metadata_dto import ConceptWithMetadataDto
from openapi_client.model.concept_edit_dto import ConceptEditDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
        'conceptUid': "conceptUid_example",
    }
    try:
        # Update concept
        api_response = api_instance.update_concept(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->update_concept: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
        'conceptUid': "conceptUid_example",
    }
    body = ConceptEditDto(
        domain=UidReference(
            uid="uid_example",
        ),
        subdomains=[
            UidReference()
        ],
        definition="definition_example",
        url="url_example",
        concept_note="concept_note_example",
    )
    try:
        # Update concept
        api_response = api_instance.update_concept(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->update_concept: %s\n" % e)
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
[**ConceptEditDto**](../../models/ConceptEditDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
termBaseUid | TermBaseUidSchema | | 
conceptUid | ConceptUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConceptUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_concept.ApiResponseFor200) | Ok
400 | [ApiResponseFor400](#update_concept.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_concept.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_concept.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_concept.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_concept.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_concept.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_concept.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_concept.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_concept.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_concept.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_concept.ApiResponseFor501) | Not implemented

#### update_concept.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConceptWithMetadataDto**](../../models/ConceptWithMetadataDto.md) |  | 


#### update_concept.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_concept.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_concept.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_concept.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_concept.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_concept.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_concept.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_concept.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_concept.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_concept.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_concept.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_term**
<a id="update_term"></a>
> TermDto update_term(term_base_uidterm_id)

Edit term

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.term_dto import TermDto
from openapi_client.model.term_edit_dto import TermEditDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
        'termId': "termId_example",
    }
    try:
        # Edit term
        api_response = api_instance.update_term(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->update_term: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
        'termId': "termId_example",
    }
    body = TermEditDto(
        text="text_example",
        lang="lang_example",
        case_sensitive=True,
        exact_match=True,
        forbidden=True,
        preferred=True,
        status="New",
        usage="usage_example",
        note="note_example",
        short_translation="short_translation_example",
        term_type="FULL_FORM",
        part_of_speech="ADJECTIVE",
        gender="MASCULINE",
        number="SINGULAR",
    )
    try:
        # Edit term
        api_response = api_instance.update_term(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->update_term: %s\n" % e)
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
[**TermEditDto**](../../models/TermEditDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
termBaseUid | TermBaseUidSchema | | 
termId | TermIdSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TermIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_term.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#update_term.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_term.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_term.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_term.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_term.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_term.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_term.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_term.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_term.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_term.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_term.ApiResponseFor501) | Not implemented

#### update_term.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TermDto**](../../models/TermDto.md) |  | 


#### update_term.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_term_base**
<a id="update_term_base"></a>
> TermBaseDto update_term_base(term_base_uid)

Edit term base

It is possible to add new languages only

### Example

```python
import openapi_client
from openapi_client.apis.tags import term_base_api
from openapi_client.model.term_base_edit_dto import TermBaseEditDto
from openapi_client.model.term_base_dto import TermBaseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = term_base_api.TermBaseApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    try:
        # Edit term base
        api_response = api_instance.update_term_base(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->update_term_base: %s\n" % e)

    # example passing only optional values
    path_params = {
        'termBaseUid': "termBaseUid_example",
    }
    body = TermBaseEditDto(
        name="name_example",
        langs=[
            "langs_example"
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
        # Edit term base
        api_response = api_instance.update_term_base(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TermBaseApi->update_term_base: %s\n" % e)
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
[**TermBaseEditDto**](../../models/TermBaseEditDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
termBaseUid | TermBaseUidSchema | | 

# TermBaseUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_term_base.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#update_term_base.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_term_base.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_term_base.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_term_base.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_term_base.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_term_base.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_term_base.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_term_base.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_term_base.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_term_base.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_term_base.ApiResponseFor501) | Not implemented

#### update_term_base.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TermBaseDto**](../../models/TermBaseDto.md) |  | 


#### update_term_base.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term_base.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term_base.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term_base.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term_base.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term_base.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term_base.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term_base.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term_base.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term_base.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_term_base.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

