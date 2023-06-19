# phrasetms_client.VendorApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vendor**](VendorApi.md#create_vendor) | **POST** /api2/v1/vendors | Create vendor
[**get_vendor**](VendorApi.md#get_vendor) | **GET** /api2/v1/vendors/{vendorUid} | Get vendor
[**list_vendors**](VendorApi.md#list_vendors) | **GET** /api2/v1/vendors | List vendors

# **create_vendor**
> VendorDto create_vendor(body=body)

Create vendor

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.VendorApi()
body = phrasetms_client.CreateVendorDto() # CreateVendorDto |  (optional)

try:
    # Create vendor
    api_response = api_instance.create_vendor(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->create_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVendorDto**](CreateVendorDto.md)|  | [optional] 

### Return type

[**VendorDto**](VendorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor**
> VendorDto get_vendor(vendor_uid)

Get vendor

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.VendorApi()
vendor_uid = 'vendor_uid_example' # str | 

try:
    # Get vendor
    api_response = api_instance.get_vendor(vendor_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->get_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_uid** | **str**|  | 

### Return type

[**VendorDto**](VendorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vendors**
> PageDtoVendorDto list_vendors(page_number=page_number, page_size=page_size, name=name)

List vendors

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.VendorApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
name = 'name_example' # str | Name or the vendor, for filtering (optional)

try:
    # List vendors
    api_response = api_instance.list_vendors(page_number=page_number, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->list_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **name** | **str**| Name or the vendor, for filtering | [optional] 

### Return type

[**PageDtoVendorDto**](PageDtoVendorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

