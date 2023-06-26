# phrasetms_client.AnalysisApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyses_batch_edit_v2**](AnalysisApi.md#analyses_batch_edit_v2) | **PUT** /api2/v2/analyses/bulk | Edit analyses (batch)
[**bulk_delete_analyses**](AnalysisApi.md#bulk_delete_analyses) | **DELETE** /api2/v1/analyses/bulk | Delete analyses (batch)
[**create_analyse_async1**](AnalysisApi.md#create_analyse_async1) | **POST** /api2/v2/analyses | Create analysis
[**create_analyses_for_langs**](AnalysisApi.md#create_analyses_for_langs) | **POST** /api2/v1/analyses/byLanguages | Create analyses by languages
[**create_analyses_for_providers**](AnalysisApi.md#create_analyses_for_providers) | **POST** /api2/v1/analyses/byProviders | Create analyses by providers
[**delete**](AnalysisApi.md#delete) | **DELETE** /api2/v1/analyses/{analyseUid} | Delete analysis
[**download_analyse**](AnalysisApi.md#download_analyse) | **GET** /api2/v1/analyses/{analyseUid}/download | Download analysis
[**edit_analysis**](AnalysisApi.md#edit_analysis) | **PUT** /api2/v2/analyses/{analyseUid} | Edit analysis
[**get_analyse_language_part**](AnalysisApi.md#get_analyse_language_part) | **GET** /api2/v1/analyses/{analyseUid}/analyseLanguageParts/{analyseLanguagePartId} | Get analysis language part
[**get_analyse_v3**](AnalysisApi.md#get_analyse_v3) | **GET** /api2/v3/analyses/{analyseUid} | Get analysis
[**get_job_part_analyse**](AnalysisApi.md#get_job_part_analyse) | **GET** /api2/v1/analyses/{analyseUid}/jobs/{jobUid} | Get jobs analysis
[**list_by_project_v3**](AnalysisApi.md#list_by_project_v3) | **GET** /api2/v3/projects/{projectUid}/analyses | List analyses by project
[**list_job_parts**](AnalysisApi.md#list_job_parts) | **GET** /api2/v1/analyses/{analyseUid}/analyseLanguageParts/{analyseLanguagePartId}/jobs | List jobs of analyses
[**list_part_analyse_v3**](AnalysisApi.md#list_part_analyse_v3) | **GET** /api2/v3/projects/{projectUid}/jobs/{jobUid}/analyses | List analyses
[**recalculate**](AnalysisApi.md#recalculate) | **POST** /api2/v1/analyses/recalculate | Recalculate analysis


# **analyses_batch_edit_v2**
> AnalysesV2Dto analyses_batch_edit_v2(body=body)

Edit analyses (batch)

If no netRateScheme is provided in request, then netRateScheme associated with provider will be used if it exists, otherwise it will remain the same as it was.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.analyses_v2_dto import AnalysesV2Dto
from phrasetms_client.models.bulk_edit_analyse_v2_dto import BulkEditAnalyseV2Dto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    body = phrasetms_client.BulkEditAnalyseV2Dto() # BulkEditAnalyseV2Dto |  (optional)

    try:
        # Edit analyses (batch)
        api_response = api_instance.analyses_batch_edit_v2(body=body)
        print("The response of AnalysisApi->analyses_batch_edit_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->analyses_batch_edit_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkEditAnalyseV2Dto**](BulkEditAnalyseV2Dto.md)|  | [optional] 

### Return type

[**AnalysesV2Dto**](AnalysesV2Dto.md)

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

# **bulk_delete_analyses**
> bulk_delete_analyses(body=body)

Delete analyses (batch)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.bulk_delete_analyse_dto import BulkDeleteAnalyseDto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    body = phrasetms_client.BulkDeleteAnalyseDto() # BulkDeleteAnalyseDto |  (optional)

    try:
        # Delete analyses (batch)
        api_instance.bulk_delete_analyses(body=body)
    except Exception as e:
        print("Exception when calling AnalysisApi->bulk_delete_analyses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkDeleteAnalyseDto**](BulkDeleteAnalyseDto.md)|  | [optional] 

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

# **create_analyse_async1**
> AsyncAnalyseListResponseV2Dto create_analyse_async1(body=body)

Create analysis

Returns created analyses - batching analyses by number of segments (api.segment.count.approximation, default 100000), in case request contains more segments than maximum (api.segment.max.count, default 300000), returns 400 bad request.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_analyse_list_response_v2_dto import AsyncAnalyseListResponseV2Dto
from phrasetms_client.models.create_analyse_async_v2_dto import CreateAnalyseAsyncV2Dto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    body = phrasetms_client.CreateAnalyseAsyncV2Dto() # CreateAnalyseAsyncV2Dto |  (optional)

    try:
        # Create analysis
        api_response = api_instance.create_analyse_async1(body=body)
        print("The response of AnalysisApi->create_analyse_async1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->create_analyse_async1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAnalyseAsyncV2Dto**](CreateAnalyseAsyncV2Dto.md)|  | [optional] 

### Return type

[**AsyncAnalyseListResponseV2Dto**](AsyncAnalyseListResponseV2Dto.md)

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

# **create_analyses_for_langs**
> AsyncAnalyseListResponseDto create_analyses_for_langs(body=body)

Create analyses by languages

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_analyse_list_response_dto import AsyncAnalyseListResponseDto
from phrasetms_client.models.create_analyse_list_async_dto import CreateAnalyseListAsyncDto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    body = phrasetms_client.CreateAnalyseListAsyncDto() # CreateAnalyseListAsyncDto |  (optional)

    try:
        # Create analyses by languages
        api_response = api_instance.create_analyses_for_langs(body=body)
        print("The response of AnalysisApi->create_analyses_for_langs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->create_analyses_for_langs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAnalyseListAsyncDto**](CreateAnalyseListAsyncDto.md)|  | [optional] 

### Return type

[**AsyncAnalyseListResponseDto**](AsyncAnalyseListResponseDto.md)

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

# **create_analyses_for_providers**
> AsyncAnalyseListResponseDto create_analyses_for_providers(body=body)

Create analyses by providers

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_analyse_list_response_dto import AsyncAnalyseListResponseDto
from phrasetms_client.models.create_analyse_list_async_dto import CreateAnalyseListAsyncDto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    body = phrasetms_client.CreateAnalyseListAsyncDto() # CreateAnalyseListAsyncDto |  (optional)

    try:
        # Create analyses by providers
        api_response = api_instance.create_analyses_for_providers(body=body)
        print("The response of AnalysisApi->create_analyses_for_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->create_analyses_for_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAnalyseListAsyncDto**](CreateAnalyseListAsyncDto.md)|  | [optional] 

### Return type

[**AsyncAnalyseListResponseDto**](AsyncAnalyseListResponseDto.md)

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

# **delete**
> delete(analyse_uid, purge=purge)

Delete analysis

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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    analyse_uid = 'analyse_uid_example' # str | 
    purge = True # bool |  (optional)

    try:
        # Delete analysis
        api_instance.delete(analyse_uid, purge=purge)
    except Exception as e:
        print("Exception when calling AnalysisApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_uid** | **str**|  | 
 **purge** | **bool**|  | [optional] 

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

# **download_analyse**
> download_analyse(analyse_uid, format)

Download analysis

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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    analyse_uid = 'analyse_uid_example' # str | 
    format = 'format_example' # str | 

    try:
        # Download analysis
        api_instance.download_analyse(analyse_uid, format)
    except Exception as e:
        print("Exception when calling AnalysisApi->download_analyse: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_uid** | **str**|  | 
 **format** | **str**|  | 

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

# **edit_analysis**
> AnalyseV2Dto edit_analysis(analyse_uid, body=body)

Edit analysis

If no netRateScheme is provided in request, then netRateScheme associated with provider will be used if it exists, otherwise it will remain the same as it was.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.analyse_v2_dto import AnalyseV2Dto
from phrasetms_client.models.edit_analyse_v2_dto import EditAnalyseV2Dto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    analyse_uid = 'analyse_uid_example' # str | 
    body = phrasetms_client.EditAnalyseV2Dto() # EditAnalyseV2Dto |  (optional)

    try:
        # Edit analysis
        api_response = api_instance.edit_analysis(analyse_uid, body=body)
        print("The response of AnalysisApi->edit_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->edit_analysis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_uid** | **str**|  | 
 **body** | [**EditAnalyseV2Dto**](EditAnalyseV2Dto.md)|  | [optional] 

### Return type

[**AnalyseV2Dto**](AnalyseV2Dto.md)

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

# **get_analyse_language_part**
> AnalyseLanguagePartDto get_analyse_language_part(analyse_uid, analyse_language_part_id)

Get analysis language part

Returns analysis language pair

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.analyse_language_part_dto import AnalyseLanguagePartDto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    analyse_uid = 'analyse_uid_example' # str | 
    analyse_language_part_id = 56 # int | 

    try:
        # Get analysis language part
        api_response = api_instance.get_analyse_language_part(analyse_uid, analyse_language_part_id)
        print("The response of AnalysisApi->get_analyse_language_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->get_analyse_language_part: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_uid** | **str**|  | 
 **analyse_language_part_id** | **int**|  | 

### Return type

[**AnalyseLanguagePartDto**](AnalyseLanguagePartDto.md)

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

# **get_analyse_v3**
> AnalyseV3Dto get_analyse_v3(analyse_uid)

Get analysis

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.analyse_v3_dto import AnalyseV3Dto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    analyse_uid = 'analyse_uid_example' # str | 

    try:
        # Get analysis
        api_response = api_instance.get_analyse_v3(analyse_uid)
        print("The response of AnalysisApi->get_analyse_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->get_analyse_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_uid** | **str**|  | 

### Return type

[**AnalyseV3Dto**](AnalyseV3Dto.md)

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

# **get_job_part_analyse**
> AnalyseJobDto get_job_part_analyse(analyse_uid, job_uid)

Get jobs analysis

Returns job's analyse

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.analyse_job_dto import AnalyseJobDto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    analyse_uid = 'analyse_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get jobs analysis
        api_response = api_instance.get_job_part_analyse(analyse_uid, job_uid)
        print("The response of AnalysisApi->get_job_part_analyse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->get_job_part_analyse: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**AnalyseJobDto**](AnalyseJobDto.md)

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

# **list_by_project_v3**
> PageDtoAnalyseReference list_by_project_v3(project_uid, name=name, uid=uid, page_number=page_number, page_size=page_size, sort=sort, order=order, only_owner_org=only_owner_org)

List analyses by project

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_analyse_reference import PageDtoAnalyseReference
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    project_uid = 'project_uid_example' # str | 
    name = 'name_example' # str | Name to search by (optional)
    uid = 'uid_example' # str | Uid to search by (optional)
    page_number = 0 # int |  (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    sort = 'DATE_CREATED' # str | Sorting field (optional) (default to 'DATE_CREATED')
    order = 'desc' # str | Sorting order (optional) (default to 'desc')
    only_owner_org = True # bool |  (optional)

    try:
        # List analyses by project
        api_response = api_instance.list_by_project_v3(project_uid, name=name, uid=uid, page_number=page_number, page_size=page_size, sort=sort, order=order, only_owner_org=only_owner_org)
        print("The response of AnalysisApi->list_by_project_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->list_by_project_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **name** | **str**| Name to search by | [optional] 
 **uid** | **str**| Uid to search by | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **sort** | **str**| Sorting field | [optional] [default to &#39;DATE_CREATED&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;desc&#39;]
 **only_owner_org** | **bool**|  | [optional] 

### Return type

[**PageDtoAnalyseReference**](PageDtoAnalyseReference.md)

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

# **list_job_parts**
> PageDtoAnalyseJobDto list_job_parts(analyse_uid, analyse_language_part_id, page_number=page_number, page_size=page_size)

List jobs of analyses

Returns list of job's analyses

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_analyse_job_dto import PageDtoAnalyseJobDto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    analyse_uid = 'analyse_uid_example' # str | 
    analyse_language_part_id = 56 # int | 
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List jobs of analyses
        api_response = api_instance.list_job_parts(analyse_uid, analyse_language_part_id, page_number=page_number, page_size=page_size)
        print("The response of AnalysisApi->list_job_parts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->list_job_parts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_uid** | **str**|  | 
 **analyse_language_part_id** | **int**|  | 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoAnalyseJobDto**](PageDtoAnalyseJobDto.md)

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

# **list_part_analyse_v3**
> PageDtoAnalyseReference list_part_analyse_v3(project_uid, job_uid, page_number=page_number, page_size=page_size)

List analyses

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_analyse_reference import PageDtoAnalyseReference
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    page_number = 0 # int |  (optional) (default to 0)
    page_size = 50 # int |  (optional) (default to 50)

    try:
        # List analyses
        api_response = api_instance.list_part_analyse_v3(project_uid, job_uid, page_number=page_number, page_size=page_size)
        print("The response of AnalysisApi->list_part_analyse_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->list_part_analyse_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoAnalyseReference**](PageDtoAnalyseReference.md)

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

# **recalculate**
> AnalyseRecalculateResponseDto recalculate(body=body)

Recalculate analysis

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.analyse_recalculate_request_dto import AnalyseRecalculateRequestDto
from phrasetms_client.models.analyse_recalculate_response_dto import AnalyseRecalculateResponseDto
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
    api_instance = phrasetms_client.AnalysisApi(api_client)
    body = phrasetms_client.AnalyseRecalculateRequestDto() # AnalyseRecalculateRequestDto |  (optional)

    try:
        # Recalculate analysis
        api_response = api_instance.recalculate(body=body)
        print("The response of AnalysisApi->recalculate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->recalculate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyseRecalculateRequestDto**](AnalyseRecalculateRequestDto.md)|  | [optional] 

### Return type

[**AnalyseRecalculateResponseDto**](AnalyseRecalculateResponseDto.md)

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

