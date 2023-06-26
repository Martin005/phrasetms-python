# phrasetms_client.CustomFieldsApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_field**](CustomFieldsApi.md#create_custom_field) | **POST** /api2/v1/customFields | Create custom field
[**get_custom_field**](CustomFieldsApi.md#get_custom_field) | **GET** /api2/v1/customFields/{fieldUid} | Get custom field
[**get_custom_field_list**](CustomFieldsApi.md#get_custom_field_list) | **GET** /api2/v1/customFields | Lists custom fields
[**get_custom_field_option_list**](CustomFieldsApi.md#get_custom_field_option_list) | **GET** /api2/v1/customFields/{fieldUid}/options | Lists options of custom field


# **create_custom_field**
> CustomFieldDto create_custom_field(body=body)

Create custom field

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.create_custom_field_dto import CreateCustomFieldDto
from phrasetms_client.models.custom_field_dto import CustomFieldDto
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
    api_instance = phrasetms_client.CustomFieldsApi(api_client)
    body = phrasetms_client.CreateCustomFieldDto() # CreateCustomFieldDto |  (optional)

    try:
        # Create custom field
        api_response = api_instance.create_custom_field(body=body)
        print("The response of CustomFieldsApi->create_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->create_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomFieldDto**](CreateCustomFieldDto.md)|  | [optional] 

### Return type

[**CustomFieldDto**](CustomFieldDto.md)

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

# **get_custom_field**
> CustomFieldDto get_custom_field(field_uid)

Get custom field

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.custom_field_dto import CustomFieldDto
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
    api_instance = phrasetms_client.CustomFieldsApi(api_client)
    field_uid = 'field_uid_example' # str | 

    try:
        # Get custom field
        api_response = api_instance.get_custom_field(field_uid)
        print("The response of CustomFieldsApi->get_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->get_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_uid** | **str**|  | 

### Return type

[**CustomFieldDto**](CustomFieldDto.md)

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

# **get_custom_field_list**
> PageDtoCustomFieldDto get_custom_field_list(page_number=page_number, page_size=page_size, name=name, allowed_entities=allowed_entities, types=types, created_by=created_by, modified_by=modified_by, uids=uids, required=required, sort_field=sort_field, sort_trend=sort_trend)

Lists custom fields

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_custom_field_dto import PageDtoCustomFieldDto
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
    api_instance = phrasetms_client.CustomFieldsApi(api_client)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    name = 'name_example' # str | Filter by custom field name (optional)
    allowed_entities = ['allowed_entities_example'] # List[str] | Filter by custom field allowed entities (optional)
    types = ['types_example'] # List[str] | Filter by custom field types (optional)
    created_by = ['created_by_example'] # List[str] | Filter by custom field creators UIDs (optional)
    modified_by = ['modified_by_example'] # List[str] | Filter by custom field updaters UIDs (optional)
    uids = ['uids_example'] # List[str] | Filter by custom field UIDs (optional)
    required = True # bool | Filter by custom field required parameter (optional)
    sort_field = 'sort_field_example' # str | Sort by this field (optional)
    sort_trend = 'ASC' # str | Sort direction (optional) (default to 'ASC')

    try:
        # Lists custom fields
        api_response = api_instance.get_custom_field_list(page_number=page_number, page_size=page_size, name=name, allowed_entities=allowed_entities, types=types, created_by=created_by, modified_by=modified_by, uids=uids, required=required, sort_field=sort_field, sort_trend=sort_trend)
        print("The response of CustomFieldsApi->get_custom_field_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->get_custom_field_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **name** | **str**| Filter by custom field name | [optional] 
 **allowed_entities** | [**List[str]**](str.md)| Filter by custom field allowed entities | [optional] 
 **types** | [**List[str]**](str.md)| Filter by custom field types | [optional] 
 **created_by** | [**List[str]**](str.md)| Filter by custom field creators UIDs | [optional] 
 **modified_by** | [**List[str]**](str.md)| Filter by custom field updaters UIDs | [optional] 
 **uids** | [**List[str]**](str.md)| Filter by custom field UIDs | [optional] 
 **required** | **bool**| Filter by custom field required parameter | [optional] 
 **sort_field** | **str**| Sort by this field | [optional] 
 **sort_trend** | **str**| Sort direction | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageDtoCustomFieldDto**](PageDtoCustomFieldDto.md)

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

# **get_custom_field_option_list**
> PageDtoCustomFieldOptionDto get_custom_field_option_list(field_uid, page_number=page_number, page_size=page_size, name=name, sort_field=sort_field, sort_trend=sort_trend)

Lists options of custom field

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_custom_field_option_dto import PageDtoCustomFieldOptionDto
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
    api_instance = phrasetms_client.CustomFieldsApi(api_client)
    field_uid = 'field_uid_example' # str | 
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    name = 'name_example' # str | Filter by option name (optional)
    sort_field = 'sort_field_example' # str | Sort by this field (optional)
    sort_trend = 'ASC' # str | Sort direction (optional) (default to 'ASC')

    try:
        # Lists options of custom field
        api_response = api_instance.get_custom_field_option_list(field_uid, page_number=page_number, page_size=page_size, name=name, sort_field=sort_field, sort_trend=sort_trend)
        print("The response of CustomFieldsApi->get_custom_field_option_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->get_custom_field_option_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_uid** | **str**|  | 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **name** | **str**| Filter by option name | [optional] 
 **sort_field** | **str**| Sort by this field | [optional] 
 **sort_trend** | **str**| Sort direction | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageDtoCustomFieldOptionDto**](PageDtoCustomFieldOptionDto.md)

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

