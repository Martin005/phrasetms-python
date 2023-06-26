# phrasetms_client.SubDomainApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sub_domain**](SubDomainApi.md#create_sub_domain) | **POST** /api2/v1/subDomains | Create subdomain
[**delete_sub_domain**](SubDomainApi.md#delete_sub_domain) | **DELETE** /api2/v1/subDomains/{subDomainUid} | Delete subdomain
[**get_sub_domain**](SubDomainApi.md#get_sub_domain) | **GET** /api2/v1/subDomains/{subDomainUid} | Get subdomain
[**list_sub_domains**](SubDomainApi.md#list_sub_domains) | **GET** /api2/v1/subDomains | List subdomains
[**update_sub_domain**](SubDomainApi.md#update_sub_domain) | **PUT** /api2/v1/subDomains/{subDomainUid} | Edit subdomain


# **create_sub_domain**
> SubDomainDto create_sub_domain(body=body)

Create subdomain

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.sub_domain_dto import SubDomainDto
from phrasetms_client.models.sub_domain_edit_dto import SubDomainEditDto
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
    api_instance = phrasetms_client.SubDomainApi(api_client)
    body = phrasetms_client.SubDomainEditDto() # SubDomainEditDto |  (optional)

    try:
        # Create subdomain
        api_response = api_instance.create_sub_domain(body=body)
        print("The response of SubDomainApi->create_sub_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubDomainApi->create_sub_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubDomainEditDto**](SubDomainEditDto.md)|  | [optional] 

### Return type

[**SubDomainDto**](SubDomainDto.md)

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

# **delete_sub_domain**
> delete_sub_domain(sub_domain_uid)

Delete subdomain

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
    api_instance = phrasetms_client.SubDomainApi(api_client)
    sub_domain_uid = 'sub_domain_uid_example' # str | 

    try:
        # Delete subdomain
        api_instance.delete_sub_domain(sub_domain_uid)
    except Exception as e:
        print("Exception when calling SubDomainApi->delete_sub_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_domain_uid** | **str**|  | 

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

# **get_sub_domain**
> SubDomainDto get_sub_domain(sub_domain_uid)

Get subdomain

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.sub_domain_dto import SubDomainDto
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
    api_instance = phrasetms_client.SubDomainApi(api_client)
    sub_domain_uid = 'sub_domain_uid_example' # str | 

    try:
        # Get subdomain
        api_response = api_instance.get_sub_domain(sub_domain_uid)
        print("The response of SubDomainApi->get_sub_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubDomainApi->get_sub_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_domain_uid** | **str**|  | 

### Return type

[**SubDomainDto**](SubDomainDto.md)

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

# **list_sub_domains**
> PageDtoSubDomainDto list_sub_domains(name=name, created_by=created_by, sort=sort, order=order, page_number=page_number, page_size=page_size)

List subdomains

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_sub_domain_dto import PageDtoSubDomainDto
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
    api_instance = phrasetms_client.SubDomainApi(api_client)
    name = 'name_example' # str |  (optional)
    created_by = 'created_by_example' # str | Uid of user (optional)
    sort = 'NAME' # str |  (optional) (default to 'NAME')
    order = 'ASC' # str |  (optional) (default to 'ASC')
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List subdomains
        api_response = api_instance.list_sub_domains(name=name, created_by=created_by, sort=sort, order=order, page_number=page_number, page_size=page_size)
        print("The response of SubDomainApi->list_sub_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubDomainApi->list_sub_domains: %s\n" % e)
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

[**PageDtoSubDomainDto**](PageDtoSubDomainDto.md)

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

# **update_sub_domain**
> SubDomainDto update_sub_domain(sub_domain_uid, body=body)

Edit subdomain

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.sub_domain_dto import SubDomainDto
from phrasetms_client.models.sub_domain_edit_dto import SubDomainEditDto
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
    api_instance = phrasetms_client.SubDomainApi(api_client)
    sub_domain_uid = 'sub_domain_uid_example' # str | 
    body = phrasetms_client.SubDomainEditDto() # SubDomainEditDto |  (optional)

    try:
        # Edit subdomain
        api_response = api_instance.update_sub_domain(sub_domain_uid, body=body)
        print("The response of SubDomainApi->update_sub_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubDomainApi->update_sub_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_domain_uid** | **str**|  | 
 **body** | [**SubDomainEditDto**](SubDomainEditDto.md)|  | [optional] 

### Return type

[**SubDomainDto**](SubDomainDto.md)

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

