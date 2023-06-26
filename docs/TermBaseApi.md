# phrasetms_client.TermBaseApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browse_terms**](TermBaseApi.md#browse_terms) | **POST** /api2/v1/termBases/{termBaseUid}/browse | Browse term base
[**clear_term_base**](TermBaseApi.md#clear_term_base) | **DELETE** /api2/v1/termBases/{termBaseUid}/terms | Clear term base
[**create_concept**](TermBaseApi.md#create_concept) | **POST** /api2/v1/termBases/{termBaseUid}/concepts | Create concept
[**create_term**](TermBaseApi.md#create_term) | **POST** /api2/v1/termBases/{termBaseUid}/terms | Create term
[**create_term_base**](TermBaseApi.md#create_term_base) | **POST** /api2/v1/termBases | Create term base
[**create_term_by_job**](TermBaseApi.md#create_term_by_job) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/termBases/createByJob | Create term in job&#39;s term bases
[**delete_concept**](TermBaseApi.md#delete_concept) | **DELETE** /api2/v1/termBases/{termBaseUid}/concepts/{conceptId} | Delete concept
[**delete_concepts**](TermBaseApi.md#delete_concepts) | **DELETE** /api2/v1/termBases/{termBaseUid}/concepts | Delete concepts
[**delete_term**](TermBaseApi.md#delete_term) | **DELETE** /api2/v1/termBases/{termBaseUid}/terms/{termId} | Delete term
[**delete_term_base**](TermBaseApi.md#delete_term_base) | **DELETE** /api2/v1/termBases/{termBaseUid} | Delete term base
[**export_term_base**](TermBaseApi.md#export_term_base) | **GET** /api2/v1/termBases/{termBaseUid}/export | Export term base
[**get_concept**](TermBaseApi.md#get_concept) | **GET** /api2/v1/termBases/{termBaseUid}/concepts/{conceptUid} | Get concept
[**get_last_background_task**](TermBaseApi.md#get_last_background_task) | **GET** /api2/v1/termBases/{termBaseUid}/lastBackgroundTask | Last import status
[**get_project_template_term_bases**](TermBaseApi.md#get_project_template_term_bases) | **GET** /api2/v1/projectTemplates/{projectTemplateUid}/termBases | Get term bases
[**get_project_term_bases**](TermBaseApi.md#get_project_term_bases) | **GET** /api2/v1/projects/{projectUid}/termBases | Get term bases
[**get_term**](TermBaseApi.md#get_term) | **GET** /api2/v1/termBases/{termBaseUid}/terms/{termId} | Get term
[**get_term_base**](TermBaseApi.md#get_term_base) | **GET** /api2/v1/termBases/{termBaseUid} | Get term base
[**get_term_base_metadata**](TermBaseApi.md#get_term_base_metadata) | **GET** /api2/v1/termBases/{termBaseUid}/metadata | Get term base metadata
[**get_translation_resources**](TermBaseApi.md#get_translation_resources) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources | Get translation resources
[**import_term_base**](TermBaseApi.md#import_term_base) | **POST** /api2/v1/termBases/{termBaseUid}/upload | Upload term base
[**list_concepts**](TermBaseApi.md#list_concepts) | **GET** /api2/v1/termBases/{termBaseUid}/concepts | List concepts
[**list_term_bases**](TermBaseApi.md#list_term_bases) | **GET** /api2/v1/termBases | List term bases
[**list_terms_of_concept**](TermBaseApi.md#list_terms_of_concept) | **GET** /api2/v1/termBases/{termBaseUid}/concepts/{conceptId}/terms | Get terms of concept
[**relevant_term_bases**](TermBaseApi.md#relevant_term_bases) | **GET** /api2/v1/projects/{projectUid}/termBases/relevant | List project relevant term bases
[**search_terms**](TermBaseApi.md#search_terms) | **POST** /api2/v1/termBases/{termBaseUid}/search | Search term base
[**search_terms_by_job1**](TermBaseApi.md#search_terms_by_job1) | **POST** /api2/v2/projects/{projectUid}/jobs/{jobUid}/termBases/searchByJob | Search job&#39;s term bases
[**search_terms_in_text_by_job_v2**](TermBaseApi.md#search_terms_in_text_by_job_v2) | **POST** /api2/v2/projects/{projectUid}/jobs/{jobUid}/termBases/searchInTextByJob | Search terms in text
[**set_project_template_term_bases**](TermBaseApi.md#set_project_template_term_bases) | **PUT** /api2/v1/projectTemplates/{projectTemplateUid}/termBases | Edit term bases in project template
[**set_project_term_bases**](TermBaseApi.md#set_project_term_bases) | **PUT** /api2/v1/projects/{projectUid}/termBases | Edit term bases
[**update_concept**](TermBaseApi.md#update_concept) | **PUT** /api2/v1/termBases/{termBaseUid}/concepts/{conceptUid} | Update concept
[**update_term**](TermBaseApi.md#update_term) | **PUT** /api2/v1/termBases/{termBaseUid}/terms/{termId} | Edit term
[**update_term_base**](TermBaseApi.md#update_term_base) | **PUT** /api2/v1/termBases/{termBaseUid} | Edit term base


# **browse_terms**
> BrowseResponseListDto browse_terms(term_base_uid, body=body)

Browse term base

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.browse_request_dto import BrowseRequestDto
from phrasetms_client.models.browse_response_list_dto import BrowseResponseListDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    body = phrasetms_client.BrowseRequestDto() # BrowseRequestDto |  (optional)

    try:
        # Browse term base
        api_response = api_instance.browse_terms(term_base_uid, body=body)
        print("The response of TermBaseApi->browse_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->browse_terms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **body** | [**BrowseRequestDto**](BrowseRequestDto.md)|  | [optional] 

### Return type

[**BrowseResponseListDto**](BrowseResponseListDto.md)

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

# **clear_term_base**
> clear_term_base(term_base_uid)

Clear term base

Deletes all terms

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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 

    try:
        # Clear term base
        api_instance.clear_term_base(term_base_uid)
    except Exception as e:
        print("Exception when calling TermBaseApi->clear_term_base: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 

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

# **create_concept**
> ConceptWithMetadataDto create_concept(term_base_uid, body=body)

Create concept

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.concept_edit_dto import ConceptEditDto
from phrasetms_client.models.concept_with_metadata_dto import ConceptWithMetadataDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    body = phrasetms_client.ConceptEditDto() # ConceptEditDto |  (optional)

    try:
        # Create concept
        api_response = api_instance.create_concept(term_base_uid, body=body)
        print("The response of TermBaseApi->create_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->create_concept: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **body** | [**ConceptEditDto**](ConceptEditDto.md)|  | [optional] 

### Return type

[**ConceptWithMetadataDto**](ConceptWithMetadataDto.md)

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

# **create_term**
> TermDto create_term(term_base_uid, body=body)

Create term

Set conceptId to assign the term to an existing concept, otherwise a new concept will be created.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.term_create_dto import TermCreateDto
from phrasetms_client.models.term_dto import TermDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    body = phrasetms_client.TermCreateDto() # TermCreateDto |  (optional)

    try:
        # Create term
        api_response = api_instance.create_term(term_base_uid, body=body)
        print("The response of TermBaseApi->create_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->create_term: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **body** | [**TermCreateDto**](TermCreateDto.md)|  | [optional] 

### Return type

[**TermDto**](TermDto.md)

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

# **create_term_base**
> TermBaseDto create_term_base(body=body)

Create term base

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.term_base_dto import TermBaseDto
from phrasetms_client.models.term_base_edit_dto import TermBaseEditDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    body = phrasetms_client.TermBaseEditDto() # TermBaseEditDto |  (optional)

    try:
        # Create term base
        api_response = api_instance.create_term_base(body=body)
        print("The response of TermBaseApi->create_term_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->create_term_base: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TermBaseEditDto**](TermBaseEditDto.md)|  | [optional] 

### Return type

[**TermBaseDto**](TermBaseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    job_uid = 'job_uid_example' # str | 
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.CreateTermsDto() # CreateTermsDto |  (optional)

    try:
        # Create term in job's term bases
        api_response = api_instance.create_term_by_job(job_uid, project_uid, body=body)
        print("The response of TermBaseApi->create_term_by_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->create_term_by_job: %s\n" % e)
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

# **delete_concept**
> delete_concept(term_base_uid, concept_id)

Delete concept

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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    concept_id = 'concept_id_example' # str | 

    try:
        # Delete concept
        api_instance.delete_concept(term_base_uid, concept_id)
    except Exception as e:
        print("Exception when calling TermBaseApi->delete_concept: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **concept_id** | **str**|  | 

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

# **delete_concepts**
> delete_concepts(term_base_uid, body=body)

Delete concepts

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.concept_list_reference import ConceptListReference
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    body = phrasetms_client.ConceptListReference() # ConceptListReference |  (optional)

    try:
        # Delete concepts
        api_instance.delete_concepts(term_base_uid, body=body)
    except Exception as e:
        print("Exception when calling TermBaseApi->delete_concepts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **body** | [**ConceptListReference**](ConceptListReference.md)|  | [optional] 

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

# **delete_term**
> delete_term(term_base_uid, term_id)

Delete term

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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    term_id = 'term_id_example' # str | 

    try:
        # Delete term
        api_instance.delete_term(term_base_uid, term_id)
    except Exception as e:
        print("Exception when calling TermBaseApi->delete_term: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **term_id** | **str**|  | 

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

# **delete_term_base**
> delete_term_base(term_base_uid, purge=purge)

Delete term base

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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    purge = False # bool | purge=false - the Termbase is can later be restored,                      \"purge=true - the Termbase is completely deleted and cannot be restored (optional) (default to False)

    try:
        # Delete term base
        api_instance.delete_term_base(term_base_uid, purge=purge)
    except Exception as e:
        print("Exception when calling TermBaseApi->delete_term_base: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **purge** | **bool**| purge&#x3D;false - the Termbase is can later be restored,                      \&quot;purge&#x3D;true - the Termbase is completely deleted and cannot be restored | [optional] [default to False]

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

# **export_term_base**
> export_term_base(term_base_uid, format=format, charset=charset, term_status=term_status)

Export term base

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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    format = 'Tbx' # str |  (optional) (default to 'Tbx')
    charset = 'UTF-8' # str |  (optional) (default to 'UTF-8')
    term_status = 'term_status_example' # str |  (optional)

    try:
        # Export term base
        api_instance.export_term_base(term_base_uid, format=format, charset=charset, term_status=term_status)
    except Exception as e:
        print("Exception when calling TermBaseApi->export_term_base: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **format** | **str**|  | [optional] [default to &#39;Tbx&#39;]
 **charset** | **str**|  | [optional] [default to &#39;UTF-8&#39;]
 **term_status** | **str**|  | [optional] 

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

# **get_concept**
> ConceptWithMetadataDto get_concept(term_base_uid, concept_uid)

Get concept

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.concept_with_metadata_dto import ConceptWithMetadataDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    concept_uid = 'concept_uid_example' # str | 

    try:
        # Get concept
        api_response = api_instance.get_concept(term_base_uid, concept_uid)
        print("The response of TermBaseApi->get_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->get_concept: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **concept_uid** | **str**|  | 

### Return type

[**ConceptWithMetadataDto**](ConceptWithMetadataDto.md)

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

# **get_last_background_task**
> BackgroundTasksTbDto get_last_background_task(term_base_uid)

Last import status

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.background_tasks_tb_dto import BackgroundTasksTbDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 

    try:
        # Last import status
        api_response = api_instance.get_last_background_task(term_base_uid)
        print("The response of TermBaseApi->get_last_background_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->get_last_background_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 

### Return type

[**BackgroundTasksTbDto**](BackgroundTasksTbDto.md)

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

# **get_project_template_term_bases**
> ProjectTemplateTermBaseListDto get_project_template_term_bases(project_template_uid)

Get term bases

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_template_term_base_list_dto import ProjectTemplateTermBaseListDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 

    try:
        # Get term bases
        api_response = api_instance.get_project_template_term_bases(project_template_uid)
        print("The response of TermBaseApi->get_project_template_term_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->get_project_template_term_bases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 

### Return type

[**ProjectTemplateTermBaseListDto**](ProjectTemplateTermBaseListDto.md)

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

# **get_project_term_bases**
> ProjectTermBaseListDto get_project_term_bases(project_uid)

Get term bases

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_term_base_list_dto import ProjectTermBaseListDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    project_uid = 'project_uid_example' # str | 

    try:
        # Get term bases
        api_response = api_instance.get_project_term_bases(project_uid)
        print("The response of TermBaseApi->get_project_term_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->get_project_term_bases: %s\n" % e)
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

# **get_term**
> TermDto get_term(term_base_uid, term_id)

Get term

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.term_dto import TermDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    term_id = 'term_id_example' # str | 

    try:
        # Get term
        api_response = api_instance.get_term(term_base_uid, term_id)
        print("The response of TermBaseApi->get_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->get_term: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **term_id** | **str**|  | 

### Return type

[**TermDto**](TermDto.md)

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

# **get_term_base**
> TermBaseDto get_term_base(term_base_uid)

Get term base

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.term_base_dto import TermBaseDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 

    try:
        # Get term base
        api_response = api_instance.get_term_base(term_base_uid)
        print("The response of TermBaseApi->get_term_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->get_term_base: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 

### Return type

[**TermBaseDto**](TermBaseDto.md)

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

# **get_term_base_metadata**
> MetadataTbDto get_term_base_metadata(term_base_uid)

Get term base metadata

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.metadata_tb_dto import MetadataTbDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 

    try:
        # Get term base metadata
        api_response = api_instance.get_term_base_metadata(term_base_uid)
        print("The response of TermBaseApi->get_term_base_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->get_term_base_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 

### Return type

[**MetadataTbDto**](MetadataTbDto.md)

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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get translation resources
        api_response = api_instance.get_translation_resources(project_uid, job_uid)
        print("The response of TermBaseApi->get_translation_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->get_translation_resources: %s\n" % e)
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

# **import_term_base**
> ImportTermBaseResponseDto import_term_base(content_disposition, term_base_uid, charset=charset, strict_lang_matching=strict_lang_matching, update_terms=update_terms, body=body)

Upload term base

 Terms can be imported from XLS/XLSX and TBX file formats into a term base. See <a target=\"_blank\" href=\"https://support.phrase.com/hc/en-us/articles/5709733372188\">Phrase Help Center</a> 

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.import_term_base_response_dto import ImportTermBaseResponseDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    content_disposition = 'content_disposition_example' # str | must match pattern `((inline|attachment); )?filename\\*=UTF-8''(.+)`
    term_base_uid = 'term_base_uid_example' # str | 
    charset = 'UTF-8' # str |  (optional) (default to 'UTF-8')
    strict_lang_matching = False # bool |  (optional) (default to False)
    update_terms = True # bool |  (optional) (default to True)
    body = None # object |  (optional)

    try:
        # Upload term base
        api_response = api_instance.import_term_base(content_disposition, term_base_uid, charset=charset, strict_lang_matching=strict_lang_matching, update_terms=update_terms, body=body)
        print("The response of TermBaseApi->import_term_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->import_term_base: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_disposition** | **str**| must match pattern &#x60;((inline|attachment); )?filename\\*&#x3D;UTF-8&#39;&#39;(.+)&#x60; | 
 **term_base_uid** | **str**|  | 
 **charset** | **str**|  | [optional] [default to &#39;UTF-8&#39;]
 **strict_lang_matching** | **bool**|  | [optional] [default to False]
 **update_terms** | **bool**|  | [optional] [default to True]
 **body** | **object**|  | [optional] 

### Return type

[**ImportTermBaseResponseDto**](ImportTermBaseResponseDto.md)

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

# **list_concepts**
> ConceptListResponseDto list_concepts(term_base_uid, page_number=page_number, page_size=page_size)

List concepts

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.concept_list_response_dto import ConceptListResponseDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List concepts
        api_response = api_instance.list_concepts(term_base_uid, page_number=page_number, page_size=page_size)
        print("The response of TermBaseApi->list_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->list_concepts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**ConceptListResponseDto**](ConceptListResponseDto.md)

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

# **list_term_bases**
> PageDtoTermBaseDto list_term_bases(name=name, lang=lang, client_id=client_id, domain_id=domain_id, sub_domain_id=sub_domain_id, page_number=page_number, page_size=page_size)

List term bases

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_term_base_dto import PageDtoTermBaseDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    name = 'name_example' # str |  (optional)
    lang = ['lang_example'] # List[str] | Language of the term base (optional)
    client_id = 'client_id_example' # str |  (optional)
    domain_id = 'domain_id_example' # str |  (optional)
    sub_domain_id = 'sub_domain_id_example' # str |  (optional)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List term bases
        api_response = api_instance.list_term_bases(name=name, lang=lang, client_id=client_id, domain_id=domain_id, sub_domain_id=sub_domain_id, page_number=page_number, page_size=page_size)
        print("The response of TermBaseApi->list_term_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->list_term_bases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **lang** | [**List[str]**](str.md)| Language of the term base | [optional] 
 **client_id** | **str**|  | [optional] 
 **domain_id** | **str**|  | [optional] 
 **sub_domain_id** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoTermBaseDto**](PageDtoTermBaseDto.md)

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

# **list_terms_of_concept**
> ConceptDto list_terms_of_concept(term_base_uid, concept_id)

Get terms of concept

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.concept_dto import ConceptDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    concept_id = 'concept_id_example' # str | 

    try:
        # Get terms of concept
        api_response = api_instance.list_terms_of_concept(term_base_uid, concept_id)
        print("The response of TermBaseApi->list_terms_of_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->list_terms_of_concept: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **concept_id** | **str**|  | 

### Return type

[**ConceptDto**](ConceptDto.md)

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

# **relevant_term_bases**
> PageDtoTermBaseDto relevant_term_bases(project_uid, name=name, domain_name=domain_name, client_name=client_name, sub_domain_name=sub_domain_name, target_langs=target_langs, strict_lang_matching=strict_lang_matching, page_number=page_number, page_size=page_size)

List project relevant term bases

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_term_base_dto import PageDtoTermBaseDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
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
        # List project relevant term bases
        api_response = api_instance.relevant_term_bases(project_uid, name=name, domain_name=domain_name, client_name=client_name, sub_domain_name=sub_domain_name, target_langs=target_langs, strict_lang_matching=strict_lang_matching, page_number=page_number, page_size=page_size)
        print("The response of TermBaseApi->relevant_term_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->relevant_term_bases: %s\n" % e)
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

[**PageDtoTermBaseDto**](PageDtoTermBaseDto.md)

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

# **search_terms**
> SearchResponseListTbDto search_terms(term_base_uid, body=body)

Search term base

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.search_response_list_tb_dto import SearchResponseListTbDto
from phrasetms_client.models.term_base_search_request_dto import TermBaseSearchRequestDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    body = phrasetms_client.TermBaseSearchRequestDto() # TermBaseSearchRequestDto |  (optional)

    try:
        # Search term base
        api_response = api_instance.search_terms(term_base_uid, body=body)
        print("The response of TermBaseApi->search_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->search_terms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **body** | [**TermBaseSearchRequestDto**](TermBaseSearchRequestDto.md)|  | [optional] 

### Return type

[**SearchResponseListTbDto**](SearchResponseListTbDto.md)

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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    job_uid = 'job_uid_example' # str | 
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.SearchTbByJobRequestDto() # SearchTbByJobRequestDto |  (optional)

    try:
        # Search job's term bases
        api_response = api_instance.search_terms_by_job1(job_uid, project_uid, body=body)
        print("The response of TermBaseApi->search_terms_by_job1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->search_terms_by_job1: %s\n" % e)
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    job_uid = 'job_uid_example' # str | 
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.SearchTbInTextByJobRequestDto() # SearchTbInTextByJobRequestDto |  (optional)

    try:
        # Search terms in text
        api_response = api_instance.search_terms_in_text_by_job_v2(job_uid, project_uid, body=body)
        print("The response of TermBaseApi->search_terms_in_text_by_job_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->search_terms_in_text_by_job_v2: %s\n" % e)
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

# **set_project_template_term_bases**
> ProjectTemplateTermBaseListDto set_project_template_term_bases(project_template_uid, body=body)

Edit term bases in project template

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_template_term_base_list_dto import ProjectTemplateTermBaseListDto
from phrasetms_client.models.set_project_template_term_base_dto import SetProjectTemplateTermBaseDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    project_template_uid = 'project_template_uid_example' # str | 
    body = phrasetms_client.SetProjectTemplateTermBaseDto() # SetProjectTemplateTermBaseDto |  (optional)

    try:
        # Edit term bases in project template
        api_response = api_instance.set_project_template_term_bases(project_template_uid, body=body)
        print("The response of TermBaseApi->set_project_template_term_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->set_project_template_term_bases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_uid** | **str**|  | 
 **body** | [**SetProjectTemplateTermBaseDto**](SetProjectTemplateTermBaseDto.md)|  | [optional] 

### Return type

[**ProjectTemplateTermBaseListDto**](ProjectTemplateTermBaseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **set_project_term_bases**
> ProjectTermBaseListDto set_project_term_bases(project_uid, body=body)

Edit term bases

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.project_term_base_list_dto import ProjectTermBaseListDto
from phrasetms_client.models.set_term_base_dto import SetTermBaseDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.SetTermBaseDto() # SetTermBaseDto |  (optional)

    try:
        # Edit term bases
        api_response = api_instance.set_project_term_bases(project_uid, body=body)
        print("The response of TermBaseApi->set_project_term_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->set_project_term_bases: %s\n" % e)
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

# **update_concept**
> ConceptWithMetadataDto update_concept(term_base_uid, concept_uid, body=body)

Update concept

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.concept_edit_dto import ConceptEditDto
from phrasetms_client.models.concept_with_metadata_dto import ConceptWithMetadataDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    concept_uid = 'concept_uid_example' # str | 
    body = phrasetms_client.ConceptEditDto() # ConceptEditDto |  (optional)

    try:
        # Update concept
        api_response = api_instance.update_concept(term_base_uid, concept_uid, body=body)
        print("The response of TermBaseApi->update_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->update_concept: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **concept_uid** | **str**|  | 
 **body** | [**ConceptEditDto**](ConceptEditDto.md)|  | [optional] 

### Return type

[**ConceptWithMetadataDto**](ConceptWithMetadataDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
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

# **update_term**
> TermDto update_term(term_base_uid, term_id, body=body)

Edit term

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.term_dto import TermDto
from phrasetms_client.models.term_edit_dto import TermEditDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    term_id = 'term_id_example' # str | 
    body = phrasetms_client.TermEditDto() # TermEditDto |  (optional)

    try:
        # Edit term
        api_response = api_instance.update_term(term_base_uid, term_id, body=body)
        print("The response of TermBaseApi->update_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->update_term: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **term_id** | **str**|  | 
 **body** | [**TermEditDto**](TermEditDto.md)|  | [optional] 

### Return type

[**TermDto**](TermDto.md)

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

# **update_term_base**
> TermBaseDto update_term_base(term_base_uid, body=body)

Edit term base

It is possible to add new languages only

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.term_base_dto import TermBaseDto
from phrasetms_client.models.term_base_edit_dto import TermBaseEditDto
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
    api_instance = phrasetms_client.TermBaseApi(api_client)
    term_base_uid = 'term_base_uid_example' # str | 
    body = phrasetms_client.TermBaseEditDto() # TermBaseEditDto |  (optional)

    try:
        # Edit term base
        api_response = api_instance.update_term_base(term_base_uid, body=body)
        print("The response of TermBaseApi->update_term_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermBaseApi->update_term_base: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_uid** | **str**|  | 
 **body** | [**TermBaseEditDto**](TermBaseEditDto.md)|  | [optional] 

### Return type

[**TermBaseDto**](TermBaseDto.md)

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

