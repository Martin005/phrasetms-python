# phrasetms_client.QualityAssuranceApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ignored_warnings**](QualityAssuranceApi.md#add_ignored_warnings) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/ignoredWarnings | Add ignored warnings
[**add_ignored_warnings1**](QualityAssuranceApi.md#add_ignored_warnings1) | **POST** /api2/v2/projects/{projectUid}/jobs/qualityAssurances/ignoredWarnings | Add ignored warnings
[**create_lqa_profile**](QualityAssuranceApi.md#create_lqa_profile) | **POST** /api2/v1/lqa/profiles | Create LQA profile
[**delete_ignored_warnings**](QualityAssuranceApi.md#delete_ignored_warnings) | **DELETE** /api2/v1/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/ignoredWarnings | Delete ignored warnings
[**delete_ignored_warnings1**](QualityAssuranceApi.md#delete_ignored_warnings1) | **DELETE** /api2/v2/projects/{projectUid}/jobs/qualityAssurances/ignoredWarnings | Delete ignored warnings
[**delete_lqa_profile**](QualityAssuranceApi.md#delete_lqa_profile) | **DELETE** /api2/v1/lqa/profiles/{profileUid} | Delete LQA profile
[**duplicate_profile**](QualityAssuranceApi.md#duplicate_profile) | **POST** /api2/v1/lqa/profiles/{profileUid}/duplicate | Duplicate LQA profile
[**enabled_quality_checks_for_job**](QualityAssuranceApi.md#enabled_quality_checks_for_job) | **GET** /api2/v2/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/settings | Get QA settings for job
[**enabled_quality_checks_for_job1**](QualityAssuranceApi.md#enabled_quality_checks_for_job1) | **GET** /api2/v2/projects/{projectUid}/jobs/qualityAssurances/settings | Get QA settings
[**get_lqa_profile**](QualityAssuranceApi.md#get_lqa_profile) | **GET** /api2/v1/lqa/profiles/{profileUid} | Get LQA profile details
[**get_lqa_profile_authors**](QualityAssuranceApi.md#get_lqa_profile_authors) | **GET** /api2/v1/lqa/profiles/authors | Get list of LQA profile authors
[**get_lqa_profiles**](QualityAssuranceApi.md#get_lqa_profiles) | **GET** /api2/v1/lqa/profiles | GET list LQA profiles
[**make_default**](QualityAssuranceApi.md#make_default) | **POST** /api2/v1/lqa/profiles/{profileUid}/default | Make LQA profile default
[**run_qa_for_job_part_v3**](QualityAssuranceApi.md#run_qa_for_job_part_v3) | **POST** /api2/v3/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/run | Run quality assurance
[**run_qa_for_job_parts_v3**](QualityAssuranceApi.md#run_qa_for_job_parts_v3) | **POST** /api2/v3/projects/{projectUid}/jobs/qualityAssurances/run | Run quality assurance (batch)
[**run_qa_for_segments_v3**](QualityAssuranceApi.md#run_qa_for_segments_v3) | **POST** /api2/v3/projects/{projectUid}/jobs/qualityAssurances/segments/run | Run quality assurance on selected segments
[**update_ignored_checks**](QualityAssuranceApi.md#update_ignored_checks) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/ignoreChecks | Edit ignored checks
[**update_lqa_profile**](QualityAssuranceApi.md#update_lqa_profile) | **PUT** /api2/v1/lqa/profiles/{profileUid} | Update LQA profile


# **add_ignored_warnings**
> UpdateIgnoredWarningsDto add_ignored_warnings(project_uid, job_uid, body=body)

Add ignored warnings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.update_ignored_warnings_dto import UpdateIgnoredWarningsDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.UpdateIgnoredWarningsDto() # UpdateIgnoredWarningsDto |  (optional)

    try:
        # Add ignored warnings
        api_response = api_instance.add_ignored_warnings(project_uid, job_uid, body=body)
        print("The response of QualityAssuranceApi->add_ignored_warnings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->add_ignored_warnings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**UpdateIgnoredWarningsDto**](UpdateIgnoredWarningsDto.md)|  | [optional] 

### Return type

[**UpdateIgnoredWarningsDto**](UpdateIgnoredWarningsDto.md)

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

# **add_ignored_warnings1**
> UpdateIgnoredWarningsDto add_ignored_warnings1(project_uid, body=body)

Add ignored warnings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.update_ignored_warnings_dto import UpdateIgnoredWarningsDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.UpdateIgnoredWarningsDto() # UpdateIgnoredWarningsDto |  (optional)

    try:
        # Add ignored warnings
        api_response = api_instance.add_ignored_warnings1(project_uid, body=body)
        print("The response of QualityAssuranceApi->add_ignored_warnings1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->add_ignored_warnings1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**UpdateIgnoredWarningsDto**](UpdateIgnoredWarningsDto.md)|  | [optional] 

### Return type

[**UpdateIgnoredWarningsDto**](UpdateIgnoredWarningsDto.md)

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

# **create_lqa_profile**
> LqaProfileDetailDto create_lqa_profile(body=body)

Create LQA profile

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.create_lqa_profile_dto import CreateLqaProfileDto
from phrasetms_client.models.lqa_profile_detail_dto import LqaProfileDetailDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    body = phrasetms_client.CreateLqaProfileDto() # CreateLqaProfileDto |  (optional)

    try:
        # Create LQA profile
        api_response = api_instance.create_lqa_profile(body=body)
        print("The response of QualityAssuranceApi->create_lqa_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->create_lqa_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLqaProfileDto**](CreateLqaProfileDto.md)|  | [optional] 

### Return type

[**LqaProfileDetailDto**](LqaProfileDetailDto.md)

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

# **delete_ignored_warnings**
> delete_ignored_warnings(project_uid, job_uid, body=body)

Delete ignored warnings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.update_ignored_warnings_dto import UpdateIgnoredWarningsDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.UpdateIgnoredWarningsDto() # UpdateIgnoredWarningsDto |  (optional)

    try:
        # Delete ignored warnings
        api_instance.delete_ignored_warnings(project_uid, job_uid, body=body)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->delete_ignored_warnings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**UpdateIgnoredWarningsDto**](UpdateIgnoredWarningsDto.md)|  | [optional] 

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

# **delete_ignored_warnings1**
> delete_ignored_warnings1(project_uid, body=body)

Delete ignored warnings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.update_ignored_warnings_dto import UpdateIgnoredWarningsDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.UpdateIgnoredWarningsDto() # UpdateIgnoredWarningsDto |  (optional)

    try:
        # Delete ignored warnings
        api_instance.delete_ignored_warnings1(project_uid, body=body)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->delete_ignored_warnings1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**UpdateIgnoredWarningsDto**](UpdateIgnoredWarningsDto.md)|  | [optional] 

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

# **delete_lqa_profile**
> delete_lqa_profile(profile_uid)

Delete LQA profile

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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    profile_uid = 'profile_uid_example' # str | 

    try:
        # Delete LQA profile
        api_instance.delete_lqa_profile(profile_uid)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->delete_lqa_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uid** | **str**|  | 

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

# **duplicate_profile**
> LqaProfileReferenceDto duplicate_profile(profile_uid)

Duplicate LQA profile

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.lqa_profile_reference_dto import LqaProfileReferenceDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    profile_uid = 'profile_uid_example' # str | 

    try:
        # Duplicate LQA profile
        api_response = api_instance.duplicate_profile(profile_uid)
        print("The response of QualityAssuranceApi->duplicate_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->duplicate_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uid** | **str**|  | 

### Return type

[**LqaProfileReferenceDto**](LqaProfileReferenceDto.md)

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

# **enabled_quality_checks_for_job**
> QualityAssuranceChecksDtoV2 enabled_quality_checks_for_job(project_uid, job_uid)

Get QA settings for job

Returns enabled quality assurance checks and settings for job.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.quality_assurance_checks_dto_v2 import QualityAssuranceChecksDtoV2
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get QA settings for job
        api_response = api_instance.enabled_quality_checks_for_job(project_uid, job_uid)
        print("The response of QualityAssuranceApi->enabled_quality_checks_for_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->enabled_quality_checks_for_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**QualityAssuranceChecksDtoV2**](QualityAssuranceChecksDtoV2.md)

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

# **enabled_quality_checks_for_job1**
> QualityAssuranceChecksDtoV2 enabled_quality_checks_for_job1(project_uid)

Get QA settings

Returns enabled quality assurance checks and settings.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.quality_assurance_checks_dto_v2 import QualityAssuranceChecksDtoV2
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    project_uid = 'project_uid_example' # str | 

    try:
        # Get QA settings
        api_response = api_instance.enabled_quality_checks_for_job1(project_uid)
        print("The response of QualityAssuranceApi->enabled_quality_checks_for_job1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->enabled_quality_checks_for_job1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**QualityAssuranceChecksDtoV2**](QualityAssuranceChecksDtoV2.md)

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

# **get_lqa_profile**
> LqaProfileDetailDto get_lqa_profile(profile_uid)

Get LQA profile details

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.lqa_profile_detail_dto import LqaProfileDetailDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    profile_uid = 'profile_uid_example' # str | 

    try:
        # Get LQA profile details
        api_response = api_instance.get_lqa_profile(profile_uid)
        print("The response of QualityAssuranceApi->get_lqa_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->get_lqa_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uid** | **str**|  | 

### Return type

[**LqaProfileDetailDto**](LqaProfileDetailDto.md)

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

# **get_lqa_profile_authors**
> List[UserReference] get_lqa_profile_authors()

Get list of LQA profile authors

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.user_reference import UserReference
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)

    try:
        # Get list of LQA profile authors
        api_response = api_instance.get_lqa_profile_authors()
        print("The response of QualityAssuranceApi->get_lqa_profile_authors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->get_lqa_profile_authors: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[UserReference]**](UserReference.md)

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

# **get_lqa_profiles**
> PageDtoLqaProfileReferenceDto get_lqa_profiles(name=name, created_by=created_by, date_created=date_created, page_number=page_number, page_size=page_size, sort=sort, order=order)

GET list LQA profiles

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_lqa_profile_reference_dto import PageDtoLqaProfileReferenceDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    name = 'name_example' # str | Name of LQA profiles, it is used for filter the list by name (optional)
    created_by = 'created_by_example' # str | It is used for filter the list by who created the profile (optional)
    date_created = 'date_created_example' # str | It is used for filter the list by date created (optional)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 20 # int | Page size, accepts values between 1 and 50, default 20 (optional) (default to 20)
    sort = ['sort_example'] # List[str] |  (optional)
    order = ['order_example'] # List[str] |  (optional)

    try:
        # GET list LQA profiles
        api_response = api_instance.get_lqa_profiles(name=name, created_by=created_by, date_created=date_created, page_number=page_number, page_size=page_size, sort=sort, order=order)
        print("The response of QualityAssuranceApi->get_lqa_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->get_lqa_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of LQA profiles, it is used for filter the list by name | [optional] 
 **created_by** | **str**| It is used for filter the list by who created the profile | [optional] 
 **date_created** | **str**| It is used for filter the list by date created | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 20 | [optional] [default to 20]
 **sort** | [**List[str]**](str.md)|  | [optional] 
 **order** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PageDtoLqaProfileReferenceDto**](PageDtoLqaProfileReferenceDto.md)

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

# **make_default**
> LqaProfileReferenceDto make_default(profile_uid)

Make LQA profile default

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.lqa_profile_reference_dto import LqaProfileReferenceDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    profile_uid = 'profile_uid_example' # str | 

    try:
        # Make LQA profile default
        api_response = api_instance.make_default(profile_uid)
        print("The response of QualityAssuranceApi->make_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->make_default: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uid** | **str**|  | 

### Return type

[**LqaProfileReferenceDto**](LqaProfileReferenceDto.md)

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

# **run_qa_for_job_part_v3**
> QualityAssuranceResponseDto run_qa_for_job_part_v3(project_uid, job_uid, body=body)

Run quality assurance

Call \"Get QA settings\" endpoint to get the list of enabled QA checks

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.quality_assurance_response_dto import QualityAssuranceResponseDto
from phrasetms_client.models.quality_assurance_run_dto_v3 import QualityAssuranceRunDtoV3
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.QualityAssuranceRunDtoV3() # QualityAssuranceRunDtoV3 |  (optional)

    try:
        # Run quality assurance
        api_response = api_instance.run_qa_for_job_part_v3(project_uid, job_uid, body=body)
        print("The response of QualityAssuranceApi->run_qa_for_job_part_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->run_qa_for_job_part_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**QualityAssuranceRunDtoV3**](QualityAssuranceRunDtoV3.md)|  | [optional] 

### Return type

[**QualityAssuranceResponseDto**](QualityAssuranceResponseDto.md)

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

# **run_qa_for_job_parts_v3**
> QualityAssuranceResponseDto run_qa_for_job_parts_v3(project_uid, body=body)

Run quality assurance (batch)

Call \"Get QA settings\" endpoint to get the list of enabled QA checks

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.quality_assurance_batch_run_dto_v3 import QualityAssuranceBatchRunDtoV3
from phrasetms_client.models.quality_assurance_response_dto import QualityAssuranceResponseDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.QualityAssuranceBatchRunDtoV3() # QualityAssuranceBatchRunDtoV3 |  (optional)

    try:
        # Run quality assurance (batch)
        api_response = api_instance.run_qa_for_job_parts_v3(project_uid, body=body)
        print("The response of QualityAssuranceApi->run_qa_for_job_parts_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->run_qa_for_job_parts_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**QualityAssuranceBatchRunDtoV3**](QualityAssuranceBatchRunDtoV3.md)|  | [optional] 

### Return type

[**QualityAssuranceResponseDto**](QualityAssuranceResponseDto.md)

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

# **run_qa_for_segments_v3**
> QualityAssuranceResponseDto run_qa_for_segments_v3(project_uid, body=body)

Run quality assurance on selected segments

By default runs only fast running checks. Source and target language of jobs have to match.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.quality_assurance_response_dto import QualityAssuranceResponseDto
from phrasetms_client.models.quality_assurance_segments_run_dto_v3 import QualityAssuranceSegmentsRunDtoV3
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.QualityAssuranceSegmentsRunDtoV3() # QualityAssuranceSegmentsRunDtoV3 |  (optional)

    try:
        # Run quality assurance on selected segments
        api_response = api_instance.run_qa_for_segments_v3(project_uid, body=body)
        print("The response of QualityAssuranceApi->run_qa_for_segments_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->run_qa_for_segments_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**QualityAssuranceSegmentsRunDtoV3**](QualityAssuranceSegmentsRunDtoV3.md)|  | [optional] 

### Return type

[**QualityAssuranceResponseDto**](QualityAssuranceResponseDto.md)

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

# **update_ignored_checks**
> update_ignored_checks(project_uid, job_uid, body=body)

Edit ignored checks

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.update_ignored_checks_dto import UpdateIgnoredChecksDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.UpdateIgnoredChecksDto() # UpdateIgnoredChecksDto |  (optional)

    try:
        # Edit ignored checks
        api_instance.update_ignored_checks(project_uid, job_uid, body=body)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->update_ignored_checks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**UpdateIgnoredChecksDto**](UpdateIgnoredChecksDto.md)|  | [optional] 

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

# **update_lqa_profile**
> LqaProfileDetailDto update_lqa_profile(profile_uid, body=body)

Update LQA profile

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.lqa_profile_detail_dto import LqaProfileDetailDto
from phrasetms_client.models.update_lqa_profile_dto import UpdateLqaProfileDto
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
    api_instance = phrasetms_client.QualityAssuranceApi(api_client)
    profile_uid = 'profile_uid_example' # str | 
    body = phrasetms_client.UpdateLqaProfileDto() # UpdateLqaProfileDto |  (optional)

    try:
        # Update LQA profile
        api_response = api_instance.update_lqa_profile(profile_uid, body=body)
        print("The response of QualityAssuranceApi->update_lqa_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAssuranceApi->update_lqa_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uid** | **str**|  | 
 **body** | [**UpdateLqaProfileDto**](UpdateLqaProfileDto.md)|  | [optional] 

### Return type

[**LqaProfileDetailDto**](LqaProfileDetailDto.md)

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

