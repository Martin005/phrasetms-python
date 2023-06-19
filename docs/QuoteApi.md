# phrasetms_client.QuoteApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quote_v2**](QuoteApi.md#create_quote_v2) | **POST** /api2/v2/quotes | Create quote
[**delete_quote**](QuoteApi.md#delete_quote) | **DELETE** /api2/v1/quotes/{quoteUid} | Delete quote
[**email_quotes**](QuoteApi.md#email_quotes) | **POST** /api2/v1/quotes/email | Email quotes
[**get2**](QuoteApi.md#get2) | **GET** /api2/v1/quotes/{quoteUid} | Get quote

# **create_quote_v2**
> QuoteV2Dto create_quote_v2(body=body)

Create quote

Either WorkflowSettings or Units must be sent for billingUnit \"Hour\".

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.QuoteApi()
body = phrasetms_client.QuoteCreateV2Dto() # QuoteCreateV2Dto |  (optional)

try:
    # Create quote
    api_response = api_instance.create_quote_v2(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteApi->create_quote_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuoteCreateV2Dto**](QuoteCreateV2Dto.md)|  | [optional] 

### Return type

[**QuoteV2Dto**](QuoteV2Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quote**
> delete_quote(quote_uid)

Delete quote

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.QuoteApi()
quote_uid = 'quote_uid_example' # str | 

try:
    # Delete quote
    api_instance.delete_quote(quote_uid)
except ApiException as e:
    print("Exception when calling QuoteApi->delete_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_quotes**
> EmailQuotesResponseDto email_quotes(body=body)

Email quotes

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.QuoteApi()
body = phrasetms_client.EmailQuotesRequestDto() # EmailQuotesRequestDto |  (optional)

try:
    # Email quotes
    api_response = api_instance.email_quotes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteApi->email_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailQuotesRequestDto**](EmailQuotesRequestDto.md)|  | [optional] 

### Return type

[**EmailQuotesResponseDto**](EmailQuotesResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get2**
> QuoteDto get2(quote_uid)

Get quote

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.QuoteApi()
quote_uid = 'quote_uid_example' # str | 

try:
    # Get quote
    api_response = api_instance.get2(quote_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteApi->get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_uid** | **str**|  | 

### Return type

[**QuoteDto**](QuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

