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
import time
import os
import phrasetms_client
from phrasetms_client.models.quote_create_v2_dto import QuoteCreateV2Dto
from phrasetms_client.models.quote_v2_dto import QuoteV2Dto
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
    api_instance = phrasetms_client.QuoteApi(api_client)
    body = phrasetms_client.QuoteCreateV2Dto() # QuoteCreateV2Dto |  (optional)

    try:
        # Create quote
        api_response = api_instance.create_quote_v2(body=body)
        print("The response of QuoteApi->create_quote_v2:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  -  |
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

# **delete_quote**
> delete_quote(quote_uid)

Delete quote

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
    api_instance = phrasetms_client.QuoteApi(api_client)
    quote_uid = 'quote_uid_example' # str | 

    try:
        # Delete quote
        api_instance.delete_quote(quote_uid)
    except Exception as e:
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

# **email_quotes**
> EmailQuotesResponseDto email_quotes(body=body)

Email quotes

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.email_quotes_request_dto import EmailQuotesRequestDto
from phrasetms_client.models.email_quotes_response_dto import EmailQuotesResponseDto
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
    api_instance = phrasetms_client.QuoteApi(api_client)
    body = phrasetms_client.EmailQuotesRequestDto() # EmailQuotesRequestDto |  (optional)

    try:
        # Email quotes
        api_response = api_instance.email_quotes(body=body)
        print("The response of QuoteApi->email_quotes:\n")
        pprint(api_response)
    except Exception as e:
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

# **get2**
> QuoteDto get2(quote_uid)

Get quote

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.quote_dto import QuoteDto
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
    api_instance = phrasetms_client.QuoteApi(api_client)
    quote_uid = 'quote_uid_example' # str | 

    try:
        # Get quote
        api_response = api_instance.get2(quote_uid)
        print("The response of QuoteApi->get2:\n")
        pprint(api_response)
    except Exception as e:
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

