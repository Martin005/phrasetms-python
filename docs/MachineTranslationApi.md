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
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.MachineTranslationApi()
mt_settings_uid = 'mt_settings_uid_example' # str | 
body = phrasetms_client.TranslationRequestExtendedDto() # TranslationRequestExtendedDto |  (optional)

try:
    # Translate with MT
    api_response = api_instance.machine_translation(mt_settings_uid, body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

