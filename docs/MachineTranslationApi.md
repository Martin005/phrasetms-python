# phrasetms_client.MachineTranslationApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**machine_translation**](MachineTranslationApi.md#machine_translation) | **POST** /api2/v1/machineTranslations/{mtSettingsUid}/translate | Translate with MT


# **machine_translation**
> MachineTranslateResponse machine_translation(mt_settings_uid, body=body)

Translate with MT

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.machine_translate_response import MachineTranslateResponse
from phrasetms_client.models.translation_request_extended_dto import TranslationRequestExtendedDto
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
    api_instance = phrasetms_client.MachineTranslationApi(api_client)
    mt_settings_uid = 'mt_settings_uid_example' # str | 
    body = phrasetms_client.TranslationRequestExtendedDto() # TranslationRequestExtendedDto |  (optional)

    try:
        # Translate with MT
        api_response = api_instance.machine_translation(mt_settings_uid, body=body)
        print("The response of MachineTranslationApi->machine_translation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineTranslationApi->machine_translation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mt_settings_uid** | **str**|  | 
 **body** | [**TranslationRequestExtendedDto**](TranslationRequestExtendedDto.md)|  | [optional] 

### Return type

[**MachineTranslateResponse**](MachineTranslateResponse.md)

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

