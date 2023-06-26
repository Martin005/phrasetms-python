# phrasetms_client.PriceListApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_language_pair**](PriceListApi.md#create_language_pair) | **POST** /api2/v1/priceLists/{priceListUid}/priceSets | Add language pairs
[**create_price_list**](PriceListApi.md#create_price_list) | **POST** /api2/v1/priceLists | Create price list
[**delete_language_pair**](PriceListApi.md#delete_language_pair) | **DELETE** /api2/v1/priceLists/{priceListUid}/priceSets/{sourceLanguage}/{targetLanguage} | Remove language pair
[**delete_language_pairs**](PriceListApi.md#delete_language_pairs) | **DELETE** /api2/v1/priceLists/{priceListUid}/priceSets | Remove language pairs
[**delete_price_list**](PriceListApi.md#delete_price_list) | **DELETE** /api2/v1/priceLists/{priceListUid} | Delete price list
[**get_list_of_price_list**](PriceListApi.md#get_list_of_price_list) | **GET** /api2/v1/priceLists | List price lists
[**get_price_list**](PriceListApi.md#get_price_list) | **GET** /api2/v1/priceLists/{priceListUid} | Get price list
[**get_prices_with_workflow_steps**](PriceListApi.md#get_prices_with_workflow_steps) | **GET** /api2/v1/priceLists/{priceListUid}/priceSets | List price sets
[**set_minimum_price_for_set**](PriceListApi.md#set_minimum_price_for_set) | **POST** /api2/v1/priceLists/{priceListUid}/priceSets/minimumPrices | Edit minimum prices
[**set_prices**](PriceListApi.md#set_prices) | **POST** /api2/v1/priceLists/{priceListUid}/priceSets/prices | Edit prices
[**update_price_list**](PriceListApi.md#update_price_list) | **PUT** /api2/v1/priceLists/{priceListUid} | Update price list


# **create_language_pair**
> TranslationPriceSetListDto create_language_pair(price_list_uid, body=body)

Add language pairs

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.translation_price_set_create_dto import TranslationPriceSetCreateDto
from phrasetms_client.models.translation_price_set_list_dto import TranslationPriceSetListDto
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
    api_instance = phrasetms_client.PriceListApi(api_client)
    price_list_uid = 'price_list_uid_example' # str | 
    body = phrasetms_client.TranslationPriceSetCreateDto() # TranslationPriceSetCreateDto |  (optional)

    try:
        # Add language pairs
        api_response = api_instance.create_language_pair(price_list_uid, body=body)
        print("The response of PriceListApi->create_language_pair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->create_language_pair: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_list_uid** | **str**|  | 
 **body** | [**TranslationPriceSetCreateDto**](TranslationPriceSetCreateDto.md)|  | [optional] 

### Return type

[**TranslationPriceSetListDto**](TranslationPriceSetListDto.md)

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

# **create_price_list**
> TranslationPriceListDto create_price_list(body=body)

Create price list

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.translation_price_list_create_dto import TranslationPriceListCreateDto
from phrasetms_client.models.translation_price_list_dto import TranslationPriceListDto
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
    api_instance = phrasetms_client.PriceListApi(api_client)
    body = phrasetms_client.TranslationPriceListCreateDto() # TranslationPriceListCreateDto |  (optional)

    try:
        # Create price list
        api_response = api_instance.create_price_list(body=body)
        print("The response of PriceListApi->create_price_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->create_price_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TranslationPriceListCreateDto**](TranslationPriceListCreateDto.md)|  | [optional] 

### Return type

[**TranslationPriceListDto**](TranslationPriceListDto.md)

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

# **delete_language_pair**
> delete_language_pair(price_list_uid, source_language, target_language)

Remove language pair

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
    api_instance = phrasetms_client.PriceListApi(api_client)
    price_list_uid = 'price_list_uid_example' # str | 
    source_language = 'source_language_example' # str | 
    target_language = 'target_language_example' # str | 

    try:
        # Remove language pair
        api_instance.delete_language_pair(price_list_uid, source_language, target_language)
    except Exception as e:
        print("Exception when calling PriceListApi->delete_language_pair: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_list_uid** | **str**|  | 
 **source_language** | **str**|  | 
 **target_language** | **str**|  | 

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

# **delete_language_pairs**
> delete_language_pairs(price_list_uid, body=body)

Remove language pairs

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.translation_price_set_bulk_delete_dto import TranslationPriceSetBulkDeleteDto
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
    api_instance = phrasetms_client.PriceListApi(api_client)
    price_list_uid = 'price_list_uid_example' # str | 
    body = phrasetms_client.TranslationPriceSetBulkDeleteDto() # TranslationPriceSetBulkDeleteDto |  (optional)

    try:
        # Remove language pairs
        api_instance.delete_language_pairs(price_list_uid, body=body)
    except Exception as e:
        print("Exception when calling PriceListApi->delete_language_pairs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_list_uid** | **str**|  | 
 **body** | [**TranslationPriceSetBulkDeleteDto**](TranslationPriceSetBulkDeleteDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **delete_price_list**
> delete_price_list(price_list_uid)

Delete price list

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
    api_instance = phrasetms_client.PriceListApi(api_client)
    price_list_uid = 'price_list_uid_example' # str | 

    try:
        # Delete price list
        api_instance.delete_price_list(price_list_uid)
    except Exception as e:
        print("Exception when calling PriceListApi->delete_price_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_list_uid** | **str**|  | 

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

# **get_list_of_price_list**
> PageDtoTranslationPriceListDto get_list_of_price_list(page_number=page_number, page_size=page_size)

List price lists

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_translation_price_list_dto import PageDtoTranslationPriceListDto
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
    api_instance = phrasetms_client.PriceListApi(api_client)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List price lists
        api_response = api_instance.get_list_of_price_list(page_number=page_number, page_size=page_size)
        print("The response of PriceListApi->get_list_of_price_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->get_list_of_price_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoTranslationPriceListDto**](PageDtoTranslationPriceListDto.md)

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

# **get_price_list**
> TranslationPriceListDto get_price_list(price_list_uid)

Get price list

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.translation_price_list_dto import TranslationPriceListDto
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
    api_instance = phrasetms_client.PriceListApi(api_client)
    price_list_uid = 'price_list_uid_example' # str | 

    try:
        # Get price list
        api_response = api_instance.get_price_list(price_list_uid)
        print("The response of PriceListApi->get_price_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->get_price_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_list_uid** | **str**|  | 

### Return type

[**TranslationPriceListDto**](TranslationPriceListDto.md)

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

# **get_prices_with_workflow_steps**
> PageDtoTranslationPriceSetDto get_prices_with_workflow_steps(price_list_uid, page_number=page_number, page_size=page_size, source_languages=source_languages, target_languages=target_languages)

List price sets

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_translation_price_set_dto import PageDtoTranslationPriceSetDto
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
    api_instance = phrasetms_client.PriceListApi(api_client)
    price_list_uid = 'price_list_uid_example' # str | 
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    source_languages = ['source_languages_example'] # List[str] |  (optional)
    target_languages = ['target_languages_example'] # List[str] |  (optional)

    try:
        # List price sets
        api_response = api_instance.get_prices_with_workflow_steps(price_list_uid, page_number=page_number, page_size=page_size, source_languages=source_languages, target_languages=target_languages)
        print("The response of PriceListApi->get_prices_with_workflow_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->get_prices_with_workflow_steps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_list_uid** | **str**|  | 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **source_languages** | [**List[str]**](str.md)|  | [optional] 
 **target_languages** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PageDtoTranslationPriceSetDto**](PageDtoTranslationPriceSetDto.md)

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

# **set_minimum_price_for_set**
> TranslationPriceListDto set_minimum_price_for_set(price_list_uid, body=body)

Edit minimum prices

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.translation_price_list_dto import TranslationPriceListDto
from phrasetms_client.models.translation_price_set_bulk_minimum_prices_dto import TranslationPriceSetBulkMinimumPricesDto
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
    api_instance = phrasetms_client.PriceListApi(api_client)
    price_list_uid = 'price_list_uid_example' # str | 
    body = phrasetms_client.TranslationPriceSetBulkMinimumPricesDto() # TranslationPriceSetBulkMinimumPricesDto |  (optional)

    try:
        # Edit minimum prices
        api_response = api_instance.set_minimum_price_for_set(price_list_uid, body=body)
        print("The response of PriceListApi->set_minimum_price_for_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->set_minimum_price_for_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_list_uid** | **str**|  | 
 **body** | [**TranslationPriceSetBulkMinimumPricesDto**](TranslationPriceSetBulkMinimumPricesDto.md)|  | [optional] 

### Return type

[**TranslationPriceListDto**](TranslationPriceListDto.md)

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

# **set_prices**
> TranslationPriceListDto set_prices(price_list_uid, body=body)

Edit prices

If object contains only price, all languages and workflow steps will be updated

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.translation_price_list_dto import TranslationPriceListDto
from phrasetms_client.models.translation_price_set_bulk_prices_dto import TranslationPriceSetBulkPricesDto
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
    api_instance = phrasetms_client.PriceListApi(api_client)
    price_list_uid = 'price_list_uid_example' # str | 
    body = phrasetms_client.TranslationPriceSetBulkPricesDto() # TranslationPriceSetBulkPricesDto |  (optional)

    try:
        # Edit prices
        api_response = api_instance.set_prices(price_list_uid, body=body)
        print("The response of PriceListApi->set_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->set_prices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_list_uid** | **str**|  | 
 **body** | [**TranslationPriceSetBulkPricesDto**](TranslationPriceSetBulkPricesDto.md)|  | [optional] 

### Return type

[**TranslationPriceListDto**](TranslationPriceListDto.md)

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

# **update_price_list**
> TranslationPriceListDto update_price_list(price_list_uid, body=body)

Update price list

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.translation_price_list_create_dto import TranslationPriceListCreateDto
from phrasetms_client.models.translation_price_list_dto import TranslationPriceListDto
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
    api_instance = phrasetms_client.PriceListApi(api_client)
    price_list_uid = 'price_list_uid_example' # str | 
    body = phrasetms_client.TranslationPriceListCreateDto() # TranslationPriceListCreateDto |  (optional)

    try:
        # Update price list
        api_response = api_instance.update_price_list(price_list_uid, body=body)
        print("The response of PriceListApi->update_price_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->update_price_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_list_uid** | **str**|  | 
 **body** | [**TranslationPriceListCreateDto**](TranslationPriceListCreateDto.md)|  | [optional] 

### Return type

[**TranslationPriceListDto**](TranslationPriceListDto.md)

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

