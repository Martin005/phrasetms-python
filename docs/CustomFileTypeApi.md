# phrasetms_client.CustomFileTypeApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_file_types**](CustomFileTypeApi.md#create_custom_file_types) | **POST** /api2/v1/customFileTypes | Create custom file type
[**delete_batch_custom_file_type**](CustomFileTypeApi.md#delete_batch_custom_file_type) | **DELETE** /api2/v1/customFileTypes | Delete multiple Custom file type
[**delete_custom_file_type**](CustomFileTypeApi.md#delete_custom_file_type) | **DELETE** /api2/v1/customFileTypes/{customFileTypeUid} | Delete Custom file type
[**get_all_custom_file_type**](CustomFileTypeApi.md#get_all_custom_file_type) | **GET** /api2/v1/customFileTypes | Get All Custom file type
[**get_custom_file_type**](CustomFileTypeApi.md#get_custom_file_type) | **GET** /api2/v1/customFileTypes/{customFileTypeUid} | Get Custom file type
[**update_custom_file_type**](CustomFileTypeApi.md#update_custom_file_type) | **PUT** /api2/v1/customFileTypes/{customFileTypeUid} | Update Custom file type

# **create_custom_file_types**
> CustomFileTypeDto create_custom_file_types(body=body)

Create custom file type

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.CustomFileTypeApi()
body = phrasetms_client.CreateCustomFileTypeDto() # CreateCustomFileTypeDto |  (optional)

try:
    # Create custom file type
    api_response = api_instance.create_custom_file_types(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFileTypeApi->create_custom_file_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomFileTypeDto**](CreateCustomFileTypeDto.md)|  | [optional] 

### Return type

[**CustomFileTypeDto**](CustomFileTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_batch_custom_file_type**
> delete_batch_custom_file_type(body=body)

Delete multiple Custom file type

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.CustomFileTypeApi()
body = phrasetms_client.DeleteCustomFileTypeDto() # DeleteCustomFileTypeDto |  (optional)

try:
    # Delete multiple Custom file type
    api_instance.delete_batch_custom_file_type(body=body)
except ApiException as e:
    print("Exception when calling CustomFileTypeApi->delete_batch_custom_file_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteCustomFileTypeDto**](DeleteCustomFileTypeDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_file_type**
> delete_custom_file_type(custom_file_type_uid)

Delete Custom file type

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.CustomFileTypeApi()
custom_file_type_uid = 'custom_file_type_uid_example' # str | 

try:
    # Delete Custom file type
    api_instance.delete_custom_file_type(custom_file_type_uid)
except ApiException as e:
    print("Exception when calling CustomFileTypeApi->delete_custom_file_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_file_type_uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_custom_file_type**
> PageDtoCustomFileTypeDto get_all_custom_file_type(page_number=page_number, page_size=page_size)

Get All Custom file type

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.CustomFileTypeApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # Get All Custom file type
    api_response = api_instance.get_all_custom_file_type(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFileTypeApi->get_all_custom_file_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoCustomFileTypeDto**](PageDtoCustomFileTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_file_type**
> CustomFileTypeDto get_custom_file_type(custom_file_type_uid)

Get Custom file type

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.CustomFileTypeApi()
custom_file_type_uid = 'custom_file_type_uid_example' # str | 

try:
    # Get Custom file type
    api_response = api_instance.get_custom_file_type(custom_file_type_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFileTypeApi->get_custom_file_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_file_type_uid** | **str**|  | 

### Return type

[**CustomFileTypeDto**](CustomFileTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_file_type**
> CustomFileTypeDto update_custom_file_type(custom_file_type_uid, body=body)

Update Custom file type

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.CustomFileTypeApi()
custom_file_type_uid = 'custom_file_type_uid_example' # str | 
body = phrasetms_client.UpdateCustomFileTypeDto() # UpdateCustomFileTypeDto |  (optional)

try:
    # Update Custom file type
    api_response = api_instance.update_custom_file_type(custom_file_type_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFileTypeApi->update_custom_file_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_file_type_uid** | **str**|  | 
 **body** | [**UpdateCustomFileTypeDto**](UpdateCustomFileTypeDto.md)|  | [optional] 

### Return type

[**CustomFileTypeDto**](CustomFileTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

