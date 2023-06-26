# phrasetms_client.ClientApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](ClientApi.md#create_client) | **POST** /api2/v1/clients | Create client
[**delete_client**](ClientApi.md#delete_client) | **DELETE** /api2/v1/clients/{clientUid} | Delete client
[**get_client**](ClientApi.md#get_client) | **GET** /api2/v1/clients/{clientUid} | Get client
[**list_clients**](ClientApi.md#list_clients) | **GET** /api2/v1/clients | List clients
[**update_client**](ClientApi.md#update_client) | **PUT** /api2/v1/clients/{clientUid} | Edit client


# **create_client**
> ClientDto create_client(body)

Create client

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.client_dto import ClientDto
from phrasetms_client.models.client_edit_dto import ClientEditDto
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
    api_instance = phrasetms_client.ClientApi(api_client)
    body = phrasetms_client.ClientEditDto() # ClientEditDto | 

    try:
        # Create client
        api_response = api_instance.create_client(body)
        print("The response of ClientApi->create_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->create_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientEditDto**](ClientEditDto.md)|  | 

### Return type

[**ClientDto**](ClientDto.md)

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

# **delete_client**
> delete_client(client_uid)

Delete client

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
    api_instance = phrasetms_client.ClientApi(api_client)
    client_uid = 'client_uid_example' # str | 

    try:
        # Delete client
        api_instance.delete_client(client_uid)
    except Exception as e:
        print("Exception when calling ClientApi->delete_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_uid** | **str**|  | 

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

# **get_client**
> ClientDto get_client(client_uid)

Get client

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.client_dto import ClientDto
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
    api_instance = phrasetms_client.ClientApi(api_client)
    client_uid = 'client_uid_example' # str | 

    try:
        # Get client
        api_response = api_instance.get_client(client_uid)
        print("The response of ClientApi->get_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->get_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_uid** | **str**|  | 

### Return type

[**ClientDto**](ClientDto.md)

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

# **list_clients**
> PageDtoClientDto list_clients(name=name, created_by=created_by, sort=sort, order=order, page_number=page_number, page_size=page_size)

List clients

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_client_dto import PageDtoClientDto
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
    api_instance = phrasetms_client.ClientApi(api_client)
    name = 'name_example' # str | Unique name of the Client (optional)
    created_by = 'created_by_example' # str | Uid of user (optional)
    sort = 'NAME' # str |  (optional) (default to 'NAME')
    order = 'ASC' # str |  (optional) (default to 'ASC')
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List clients
        api_response = api_instance.list_clients(name=name, created_by=created_by, sort=sort, order=order, page_number=page_number, page_size=page_size)
        print("The response of ClientApi->list_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->list_clients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Unique name of the Client | [optional] 
 **created_by** | **str**| Uid of user | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;NAME&#39;]
 **order** | **str**|  | [optional] [default to &#39;ASC&#39;]
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoClientDto**](PageDtoClientDto.md)

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

# **update_client**
> ClientDto update_client(client_uid, body)

Edit client

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.client_dto import ClientDto
from phrasetms_client.models.client_edit_dto import ClientEditDto
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
    api_instance = phrasetms_client.ClientApi(api_client)
    client_uid = 'client_uid_example' # str | 
    body = phrasetms_client.ClientEditDto() # ClientEditDto | 

    try:
        # Edit client
        api_response = api_instance.update_client(client_uid, body)
        print("The response of ClientApi->update_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->update_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_uid** | **str**|  | 
 **body** | [**ClientEditDto**](ClientEditDto.md)|  | 

### Return type

[**ClientDto**](ClientDto.md)

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

