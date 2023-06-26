# phrasetms_client.DomainApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain**](DomainApi.md#create_domain) | **POST** /api2/v1/domains | Create domain
[**delete_domain**](DomainApi.md#delete_domain) | **DELETE** /api2/v1/domains/{domainUid} | Delete domain
[**get_domain**](DomainApi.md#get_domain) | **GET** /api2/v1/domains/{domainUid} | Get domain
[**list_domains**](DomainApi.md#list_domains) | **GET** /api2/v1/domains | List of domains
[**update_domain**](DomainApi.md#update_domain) | **PUT** /api2/v1/domains/{domainUid} | Edit domain


# **create_domain**
> DomainDto create_domain(body=body)

Create domain

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.domain_dto import DomainDto
from phrasetms_client.models.domain_edit_dto import DomainEditDto
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
    api_instance = phrasetms_client.DomainApi(api_client)
    body = phrasetms_client.DomainEditDto() # DomainEditDto |  (optional)

    try:
        # Create domain
        api_response = api_instance.create_domain(body=body)
        print("The response of DomainApi->create_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->create_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainEditDto**](DomainEditDto.md)|  | [optional] 

### Return type

[**DomainDto**](DomainDto.md)

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

# **delete_domain**
> delete_domain(domain_uid)

Delete domain

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
    api_instance = phrasetms_client.DomainApi(api_client)
    domain_uid = 'domain_uid_example' # str | 

    try:
        # Delete domain
        api_instance.delete_domain(domain_uid)
    except Exception as e:
        print("Exception when calling DomainApi->delete_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uid** | **str**|  | 

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

# **get_domain**
> DomainDto get_domain(domain_uid)

Get domain

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.domain_dto import DomainDto
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
    api_instance = phrasetms_client.DomainApi(api_client)
    domain_uid = 'domain_uid_example' # str | 

    try:
        # Get domain
        api_response = api_instance.get_domain(domain_uid)
        print("The response of DomainApi->get_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->get_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uid** | **str**|  | 

### Return type

[**DomainDto**](DomainDto.md)

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

# **list_domains**
> PageDtoDomainDto list_domains(name=name, created_by=created_by, sort=sort, order=order, page_number=page_number, page_size=page_size)

List of domains

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_domain_dto import PageDtoDomainDto
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
    api_instance = phrasetms_client.DomainApi(api_client)
    name = 'name_example' # str |  (optional)
    created_by = 'created_by_example' # str | Uid of user (optional)
    sort = 'NAME' # str |  (optional) (default to 'NAME')
    order = 'ASC' # str |  (optional) (default to 'ASC')
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List of domains
        api_response = api_instance.list_domains(name=name, created_by=created_by, sort=sort, order=order, page_number=page_number, page_size=page_size)
        print("The response of DomainApi->list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->list_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **created_by** | **str**| Uid of user | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;NAME&#39;]
 **order** | **str**|  | [optional] [default to &#39;ASC&#39;]
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoDomainDto**](PageDtoDomainDto.md)

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

# **update_domain**
> DomainDto update_domain(domain_uid, body=body)

Edit domain

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.domain_dto import DomainDto
from phrasetms_client.models.domain_edit_dto import DomainEditDto
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
    api_instance = phrasetms_client.DomainApi(api_client)
    domain_uid = 'domain_uid_example' # str | 
    body = phrasetms_client.DomainEditDto() # DomainEditDto |  (optional)

    try:
        # Edit domain
        api_response = api_instance.update_domain(domain_uid, body=body)
        print("The response of DomainApi->update_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->update_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uid** | **str**|  | 
 **body** | [**DomainEditDto**](DomainEditDto.md)|  | [optional] 

### Return type

[**DomainDto**](DomainDto.md)

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

