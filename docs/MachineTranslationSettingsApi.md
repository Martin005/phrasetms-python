# phrasetms_client.MachineTranslationSettingsApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list**](MachineTranslationSettingsApi.md#get_list) | **GET** /api2/v1/machineTranslateSettings | List machine translate settings
[**get_mt_settings**](MachineTranslationSettingsApi.md#get_mt_settings) | **GET** /api2/v1/machineTranslateSettings/{mtsUid} | Get machine translate settings
[**get_mt_types**](MachineTranslationSettingsApi.md#get_mt_types) | **GET** /api2/v1/machineTranslateSettings/types | Get machine translate settings types
[**get_status**](MachineTranslationSettingsApi.md#get_status) | **GET** /api2/v1/machineTranslateSettings/{mtsUid}/status | Get status of machine translate engine
[**get_third_party_engines_list**](MachineTranslationSettingsApi.md#get_third_party_engines_list) | **GET** /api2/v1/machineTranslateSettings/thirdPartyEngines | List third party machine translate settings
[**get_translation_resources**](MachineTranslationSettingsApi.md#get_translation_resources) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources | Get translation resources


# **get_list**
> PageDtoMachineTranslateSettingsPbmDto get_list(name=name, page_number=page_number, page_size=page_size, sort=sort, order=order)

List machine translate settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_machine_translate_settings_pbm_dto import PageDtoMachineTranslateSettingsPbmDto
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
    api_instance = phrasetms_client.MachineTranslationSettingsApi(api_client)
    name = 'name_example' # str |  (optional)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    sort = 'NAME' # str | Sorting field (optional) (default to 'NAME')
    order = 'asc' # str |  (optional) (default to 'asc')

    try:
        # List machine translate settings
        api_response = api_instance.get_list(name=name, page_number=page_number, page_size=page_size, sort=sort, order=order)
        print("The response of MachineTranslationSettingsApi->get_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineTranslationSettingsApi->get_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **sort** | **str**| Sorting field | [optional] [default to &#39;NAME&#39;]
 **order** | **str**|  | [optional] [default to &#39;asc&#39;]

### Return type

[**PageDtoMachineTranslateSettingsPbmDto**](PageDtoMachineTranslateSettingsPbmDto.md)

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

# **get_mt_settings**
> MachineTranslateSettingsPbmDto get_mt_settings(mts_uid)

Get machine translate settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.machine_translate_settings_pbm_dto import MachineTranslateSettingsPbmDto
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
    api_instance = phrasetms_client.MachineTranslationSettingsApi(api_client)
    mts_uid = 'mts_uid_example' # str | 

    try:
        # Get machine translate settings
        api_response = api_instance.get_mt_settings(mts_uid)
        print("The response of MachineTranslationSettingsApi->get_mt_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineTranslationSettingsApi->get_mt_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mts_uid** | **str**|  | 

### Return type

[**MachineTranslateSettingsPbmDto**](MachineTranslateSettingsPbmDto.md)

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

# **get_mt_types**
> TypesDto get_mt_types()

Get machine translate settings types

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.types_dto import TypesDto
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
    api_instance = phrasetms_client.MachineTranslationSettingsApi(api_client)

    try:
        # Get machine translate settings types
        api_response = api_instance.get_mt_types()
        print("The response of MachineTranslationSettingsApi->get_mt_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineTranslationSettingsApi->get_mt_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesDto**](TypesDto.md)

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

# **get_status**
> MachineTranslateStatusDto get_status(mts_uid)

Get status of machine translate engine

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.machine_translate_status_dto import MachineTranslateStatusDto
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
    api_instance = phrasetms_client.MachineTranslationSettingsApi(api_client)
    mts_uid = 'mts_uid_example' # str | 

    try:
        # Get status of machine translate engine
        api_response = api_instance.get_status(mts_uid)
        print("The response of MachineTranslationSettingsApi->get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineTranslationSettingsApi->get_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mts_uid** | **str**|  | 

### Return type

[**MachineTranslateStatusDto**](MachineTranslateStatusDto.md)

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

# **get_third_party_engines_list**
> PageDtoMachineTranslateSettingsPbmDto get_third_party_engines_list(name=name, page_number=page_number, page_size=page_size, sort=sort, order=order)

List third party machine translate settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_machine_translate_settings_pbm_dto import PageDtoMachineTranslateSettingsPbmDto
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
    api_instance = phrasetms_client.MachineTranslationSettingsApi(api_client)
    name = 'name_example' # str |  (optional)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    sort = 'NAME' # str | Sorting field (optional) (default to 'NAME')
    order = 'asc' # str |  (optional) (default to 'asc')

    try:
        # List third party machine translate settings
        api_response = api_instance.get_third_party_engines_list(name=name, page_number=page_number, page_size=page_size, sort=sort, order=order)
        print("The response of MachineTranslationSettingsApi->get_third_party_engines_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineTranslationSettingsApi->get_third_party_engines_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **sort** | **str**| Sorting field | [optional] [default to &#39;NAME&#39;]
 **order** | **str**|  | [optional] [default to &#39;asc&#39;]

### Return type

[**PageDtoMachineTranslateSettingsPbmDto**](PageDtoMachineTranslateSettingsPbmDto.md)

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
    api_instance = phrasetms_client.MachineTranslationSettingsApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 

    try:
        # Get translation resources
        api_response = api_instance.get_translation_resources(project_uid, job_uid)
        print("The response of MachineTranslationSettingsApi->get_translation_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineTranslationSettingsApi->get_translation_resources: %s\n" % e)
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

