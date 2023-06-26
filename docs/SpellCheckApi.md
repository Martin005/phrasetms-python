# phrasetms_client.SpellCheckApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_word**](SpellCheckApi.md#add_word) | **POST** /api2/v1/spellCheck/words | Add word to dictionary
[**check**](SpellCheckApi.md#check) | **POST** /api2/v1/spellCheck/check | Spell check
[**check_by_job**](SpellCheckApi.md#check_by_job) | **POST** /api2/v1/spellCheck/check/{jobUid} | Spell check for job
[**suggest**](SpellCheckApi.md#suggest) | **POST** /api2/v1/spellCheck/suggest | Suggest a word


# **add_word**
> add_word(body=body)

Add word to dictionary

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.dictionary_item_dto import DictionaryItemDto
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
    api_instance = phrasetms_client.SpellCheckApi(api_client)
    body = phrasetms_client.DictionaryItemDto() # DictionaryItemDto |  (optional)

    try:
        # Add word to dictionary
        api_instance.add_word(body=body)
    except Exception as e:
        print("Exception when calling SpellCheckApi->add_word: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryItemDto**](DictionaryItemDto.md)|  | [optional] 

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

# **check**
> SpellCheckResponseDto check(body=body)

Spell check

Spell check using the settings of the user's organization

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.spell_check_request_dto import SpellCheckRequestDto
from phrasetms_client.models.spell_check_response_dto import SpellCheckResponseDto
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
    api_instance = phrasetms_client.SpellCheckApi(api_client)
    body = phrasetms_client.SpellCheckRequestDto() # SpellCheckRequestDto |  (optional)

    try:
        # Spell check
        api_response = api_instance.check(body=body)
        print("The response of SpellCheckApi->check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpellCheckApi->check: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpellCheckRequestDto**](SpellCheckRequestDto.md)|  | [optional] 

### Return type

[**SpellCheckResponseDto**](SpellCheckResponseDto.md)

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

# **check_by_job**
> SpellCheckResponseDto check_by_job(job_uid, body=body)

Spell check for job

Spell check using the settings from the project of the job

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.spell_check_request_dto import SpellCheckRequestDto
from phrasetms_client.models.spell_check_response_dto import SpellCheckResponseDto
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
    api_instance = phrasetms_client.SpellCheckApi(api_client)
    job_uid = 'job_uid_example' # str | 
    body = phrasetms_client.SpellCheckRequestDto() # SpellCheckRequestDto |  (optional)

    try:
        # Spell check for job
        api_response = api_instance.check_by_job(job_uid, body=body)
        print("The response of SpellCheckApi->check_by_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpellCheckApi->check_by_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **body** | [**SpellCheckRequestDto**](SpellCheckRequestDto.md)|  | [optional] 

### Return type

[**SpellCheckResponseDto**](SpellCheckResponseDto.md)

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

# **suggest**
> SuggestResponseDto suggest(body=body)

Suggest a word

Spell check suggest using the users's spell check dictionary

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.suggest_request_dto import SuggestRequestDto
from phrasetms_client.models.suggest_response_dto import SuggestResponseDto
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
    api_instance = phrasetms_client.SpellCheckApi(api_client)
    body = phrasetms_client.SuggestRequestDto() # SuggestRequestDto |  (optional)

    try:
        # Suggest a word
        api_response = api_instance.suggest(body=body)
        print("The response of SpellCheckApi->suggest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpellCheckApi->suggest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SuggestRequestDto**](SuggestRequestDto.md)|  | [optional] 

### Return type

[**SuggestResponseDto**](SuggestResponseDto.md)

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

