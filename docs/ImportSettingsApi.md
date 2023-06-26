# phrasetms_client.ImportSettingsApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_import_settings**](ImportSettingsApi.md#create_import_settings) | **POST** /api2/v1/importSettings | Create import settings
[**delete_import_settings**](ImportSettingsApi.md#delete_import_settings) | **DELETE** /api2/v1/importSettings/{uid} | Delete import settings
[**edit_import_settings**](ImportSettingsApi.md#edit_import_settings) | **PUT** /api2/v1/importSettings | Edit import settings
[**get_import_settings**](ImportSettingsApi.md#get_import_settings) | **GET** /api2/v1/importSettings/{uid} | Get import settings
[**get_import_settings1**](ImportSettingsApi.md#get_import_settings1) | **GET** /api2/v1/importSettings/default | Get organization&#39;s default import settings
[**list_import_settings**](ImportSettingsApi.md#list_import_settings) | **GET** /api2/v1/importSettings | List import settings


# **create_import_settings**
> ImportSettingsDto create_import_settings(body=body)

Create import settings

Pre-defined import settings is handy for [Create Job](#operation/createJob).                   See [supported file types](https://wiki.memsource.com/wiki/API_File_Type_List)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.import_settings_create_dto import ImportSettingsCreateDto
from phrasetms_client.models.import_settings_dto import ImportSettingsDto
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
    api_instance = phrasetms_client.ImportSettingsApi(api_client)
    body = phrasetms_client.ImportSettingsCreateDto() # ImportSettingsCreateDto |  (optional)

    try:
        # Create import settings
        api_response = api_instance.create_import_settings(body=body)
        print("The response of ImportSettingsApi->create_import_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportSettingsApi->create_import_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportSettingsCreateDto**](ImportSettingsCreateDto.md)|  | [optional] 

### Return type

[**ImportSettingsDto**](ImportSettingsDto.md)

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

# **delete_import_settings**
> delete_import_settings(uid)

Delete import settings

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
    api_instance = phrasetms_client.ImportSettingsApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Delete import settings
        api_instance.delete_import_settings(uid)
    except Exception as e:
        print("Exception when calling ImportSettingsApi->delete_import_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

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

# **edit_import_settings**
> ImportSettingsDto edit_import_settings(body=body)

Edit import settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.import_settings_dto import ImportSettingsDto
from phrasetms_client.models.import_settings_edit_dto import ImportSettingsEditDto
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
    api_instance = phrasetms_client.ImportSettingsApi(api_client)
    body = phrasetms_client.ImportSettingsEditDto() # ImportSettingsEditDto |  (optional)

    try:
        # Edit import settings
        api_response = api_instance.edit_import_settings(body=body)
        print("The response of ImportSettingsApi->edit_import_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportSettingsApi->edit_import_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportSettingsEditDto**](ImportSettingsEditDto.md)|  | [optional] 

### Return type

[**ImportSettingsDto**](ImportSettingsDto.md)

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

# **get_import_settings**
> ImportSettingsDto get_import_settings(uid)

Get import settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.import_settings_dto import ImportSettingsDto
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
    api_instance = phrasetms_client.ImportSettingsApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Get import settings
        api_response = api_instance.get_import_settings(uid)
        print("The response of ImportSettingsApi->get_import_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportSettingsApi->get_import_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**ImportSettingsDto**](ImportSettingsDto.md)

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

# **get_import_settings1**
> ImportSettingsDto get_import_settings1()

Get organization's default import settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.import_settings_dto import ImportSettingsDto
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
    api_instance = phrasetms_client.ImportSettingsApi(api_client)

    try:
        # Get organization's default import settings
        api_response = api_instance.get_import_settings1()
        print("The response of ImportSettingsApi->get_import_settings1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportSettingsApi->get_import_settings1: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ImportSettingsDto**](ImportSettingsDto.md)

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

# **list_import_settings**
> PageDtoImportSettingsReference list_import_settings(name=name, page_number=page_number, page_size=page_size)

List import settings

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_import_settings_reference import PageDtoImportSettingsReference
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
    api_instance = phrasetms_client.ImportSettingsApi(api_client)
    name = 'name_example' # str |  (optional)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List import settings
        api_response = api_instance.list_import_settings(name=name, page_number=page_number, page_size=page_size)
        print("The response of ImportSettingsApi->list_import_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportSettingsApi->list_import_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoImportSettingsReference**](PageDtoImportSettingsReference.md)

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

