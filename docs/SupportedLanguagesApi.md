# phrasetms_client.SupportedLanguagesApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_of_languages**](SupportedLanguagesApi.md#list_of_languages) | **GET** /api2/v1/languages | List supported languages


# **list_of_languages**
> LanguageListDto list_of_languages(active=active)

List supported languages

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.language_list_dto import LanguageListDto
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
    api_instance = phrasetms_client.SupportedLanguagesApi(api_client)
    active = True # bool |  (optional)

    try:
        # List supported languages
        api_response = api_instance.list_of_languages(active=active)
        print("The response of SupportedLanguagesApi->list_of_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportedLanguagesApi->list_of_languages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**|  | [optional] 

### Return type

[**LanguageListDto**](LanguageListDto.md)

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

