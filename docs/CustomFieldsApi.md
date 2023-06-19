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
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.CustomFieldsApi()
body = phrasetms_client.CreateCustomFieldDto() # CreateCustomFieldDto |  (optional)

try:
    # Create custom field
    api_response = api_instance.create_custom_field(body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> CustomFieldDto get_custom_field(field_uid)

Get custom field

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.CustomFieldsApi()
field_uid = 'field_uid_example' # str | 

try:
    # Get custom field
    api_response = api_instance.get_custom_field(field_uid)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field_list**
> PageDtoCustomFieldDto get_custom_field_list(page_number=page_number, page_size=page_size, name=name, allowed_entities=allowed_entities, types=types, created_by=created_by, modified_by=modified_by, uids=uids, required=required, sort_field=sort_field, sort_trend=sort_trend)

Lists custom fields

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.CustomFieldsApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
name = 'name_example' # str | Filter by custom field name (optional)
allowed_entities = ['allowed_entities_example'] # list[str] | Filter by custom field allowed entities (optional)
types = ['types_example'] # list[str] | Filter by custom field types (optional)
created_by = ['created_by_example'] # list[str] | Filter by custom field creators UIDs (optional)
modified_by = ['modified_by_example'] # list[str] | Filter by custom field updaters UIDs (optional)
uids = ['uids_example'] # list[str] | Filter by custom field UIDs (optional)
required = true # bool | Filter by custom field required parameter (optional)
sort_field = 'sort_field_example' # str | Sort by this field (optional)
sort_trend = 'ASC' # str | Sort direction (optional) (default to ASC)

try:
    # Lists custom fields
    api_response = api_instance.get_custom_field_list(page_number=page_number, page_size=page_size, name=name, allowed_entities=allowed_entities, types=types, created_by=created_by, modified_by=modified_by, uids=uids, required=required, sort_field=sort_field, sort_trend=sort_trend)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->get_custom_field_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **name** | **str**| Filter by custom field name | [optional] 
 **allowed_entities** | [**list[str]**](str.md)| Filter by custom field allowed entities | [optional] 
 **types** | [**list[str]**](str.md)| Filter by custom field types | [optional] 
 **created_by** | [**list[str]**](str.md)| Filter by custom field creators UIDs | [optional] 
 **modified_by** | [**list[str]**](str.md)| Filter by custom field updaters UIDs | [optional] 
 **uids** | [**list[str]**](str.md)| Filter by custom field UIDs | [optional] 
 **required** | **bool**| Filter by custom field required parameter | [optional] 
 **sort_field** | **str**| Sort by this field | [optional] 
 **sort_trend** | **str**| Sort direction | [optional] [default to ASC]

### Return type

[**PageDtoCustomFieldDto**](PageDtoCustomFieldDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field_option_list**
> PageDtoCustomFieldOptionDto get_custom_field_option_list(field_uid, page_number=page_number, page_size=page_size, name=name, sort_field=sort_field, sort_trend=sort_trend)

Lists options of custom field

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.CustomFieldsApi()
field_uid = 'field_uid_example' # str | 
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
name = 'name_example' # str | Filter by option name (optional)
sort_field = 'sort_field_example' # str | Sort by this field (optional)
sort_trend = 'ASC' # str | Sort direction (optional) (default to ASC)

try:
    # Lists options of custom field
    api_response = api_instance.get_custom_field_option_list(field_uid, page_number=page_number, page_size=page_size, name=name, sort_field=sort_field, sort_trend=sort_trend)
    pprint(api_response)
except ApiException as e:
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
 **sort_trend** | **str**| Sort direction | [optional] [default to ASC]

### Return type

[**PageDtoCustomFieldOptionDto**](PageDtoCustomFieldOptionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

