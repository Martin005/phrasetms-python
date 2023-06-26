# phrasetms_client.CostCenterApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cost_center**](CostCenterApi.md#create_cost_center) | **POST** /api2/v1/costCenters | Create cost center
[**delete_cost_center**](CostCenterApi.md#delete_cost_center) | **DELETE** /api2/v1/costCenters/{costCenterUid} | Delete cost center
[**get_cost_center**](CostCenterApi.md#get_cost_center) | **GET** /api2/v1/costCenters/{costCenterUid} | Get cost center
[**list_cost_centers**](CostCenterApi.md#list_cost_centers) | **GET** /api2/v1/costCenters | List of cost centers
[**update_cost_center**](CostCenterApi.md#update_cost_center) | **PUT** /api2/v1/costCenters/{costCenterUid} | Edit cost center


# **create_cost_center**
> CostCenterDto create_cost_center(body)

Create cost center

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.cost_center_dto import CostCenterDto
from phrasetms_client.models.cost_center_edit_dto import CostCenterEditDto
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
    api_instance = phrasetms_client.CostCenterApi(api_client)
    body = phrasetms_client.CostCenterEditDto() # CostCenterEditDto | 

    try:
        # Create cost center
        api_response = api_instance.create_cost_center(body)
        print("The response of CostCenterApi->create_cost_center:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCenterApi->create_cost_center: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CostCenterEditDto**](CostCenterEditDto.md)|  | 

### Return type

[**CostCenterDto**](CostCenterDto.md)

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

# **delete_cost_center**
> delete_cost_center(cost_center_uid)

Delete cost center

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
    api_instance = phrasetms_client.CostCenterApi(api_client)
    cost_center_uid = 'cost_center_uid_example' # str | 

    try:
        # Delete cost center
        api_instance.delete_cost_center(cost_center_uid)
    except Exception as e:
        print("Exception when calling CostCenterApi->delete_cost_center: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_center_uid** | **str**|  | 

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

# **get_cost_center**
> CostCenterDto get_cost_center(cost_center_uid)

Get cost center

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.cost_center_dto import CostCenterDto
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
    api_instance = phrasetms_client.CostCenterApi(api_client)
    cost_center_uid = 'cost_center_uid_example' # str | 

    try:
        # Get cost center
        api_response = api_instance.get_cost_center(cost_center_uid)
        print("The response of CostCenterApi->get_cost_center:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCenterApi->get_cost_center: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_center_uid** | **str**|  | 

### Return type

[**CostCenterDto**](CostCenterDto.md)

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

# **list_cost_centers**
> PageDtoCostCenterDto list_cost_centers(name=name, created_by=created_by, sort=sort, order=order, page_number=page_number, page_size=page_size)

List of cost centers

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_cost_center_dto import PageDtoCostCenterDto
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
    api_instance = phrasetms_client.CostCenterApi(api_client)
    name = 'name_example' # str |  (optional)
    created_by = 'created_by_example' # str | Uid of user (optional)
    sort = 'NAME' # str |  (optional) (default to 'NAME')
    order = 'ASC' # str |  (optional) (default to 'ASC')
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List of cost centers
        api_response = api_instance.list_cost_centers(name=name, created_by=created_by, sort=sort, order=order, page_number=page_number, page_size=page_size)
        print("The response of CostCenterApi->list_cost_centers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCenterApi->list_cost_centers: %s\n" % e)
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

[**PageDtoCostCenterDto**](PageDtoCostCenterDto.md)

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

# **update_cost_center**
> CostCenterDto update_cost_center(cost_center_uid, body=body)

Edit cost center

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.cost_center_dto import CostCenterDto
from phrasetms_client.models.cost_center_edit_dto import CostCenterEditDto
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
    api_instance = phrasetms_client.CostCenterApi(api_client)
    cost_center_uid = 'cost_center_uid_example' # str | 
    body = phrasetms_client.CostCenterEditDto() # CostCenterEditDto |  (optional)

    try:
        # Edit cost center
        api_response = api_instance.update_cost_center(cost_center_uid, body=body)
        print("The response of CostCenterApi->update_cost_center:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostCenterApi->update_cost_center: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_center_uid** | **str**|  | 
 **body** | [**CostCenterEditDto**](CostCenterEditDto.md)|  | [optional] 

### Return type

[**CostCenterDto**](CostCenterDto.md)

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

