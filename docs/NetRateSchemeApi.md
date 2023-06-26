# phrasetms_client.NetRateSchemeApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_discount_scheme**](NetRateSchemeApi.md#create_discount_scheme) | **POST** /api2/v1/netRateSchemes | Create net rate scheme
[**edit_discount_scheme_workflow_step**](NetRateSchemeApi.md#edit_discount_scheme_workflow_step) | **PUT** /api2/v1/netRateSchemes/{netRateSchemeUid}/workflowStepNetSchemes/{netRateSchemeWorkflowStepId} | Edit scheme for workflow step
[**get_discount_scheme**](NetRateSchemeApi.md#get_discount_scheme) | **GET** /api2/v1/netRateSchemes/{netRateSchemeUid} | Get net rate scheme
[**get_discount_scheme_workflow_step**](NetRateSchemeApi.md#get_discount_scheme_workflow_step) | **GET** /api2/v1/netRateSchemes/{netRateSchemeUid}/workflowStepNetSchemes/{netRateSchemeWorkflowStepId} | Get scheme for workflow step
[**get_discount_scheme_workflow_steps**](NetRateSchemeApi.md#get_discount_scheme_workflow_steps) | **GET** /api2/v1/netRateSchemes/{netRateSchemeUid}/workflowStepNetSchemes | List schemes for workflow step
[**get_discount_schemes**](NetRateSchemeApi.md#get_discount_schemes) | **GET** /api2/v1/netRateSchemes | List net rate schemes
[**update_discount_scheme**](NetRateSchemeApi.md#update_discount_scheme) | **PUT** /api2/v1/netRateSchemes/{netRateSchemeUid} | Edit net rate scheme


# **create_discount_scheme**
> NetRateScheme create_discount_scheme(body=body)

Create net rate scheme

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.discount_scheme_create_dto import DiscountSchemeCreateDto
from phrasetms_client.models.net_rate_scheme import NetRateScheme
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
    api_instance = phrasetms_client.NetRateSchemeApi(api_client)
    body = phrasetms_client.DiscountSchemeCreateDto() # DiscountSchemeCreateDto |  (optional)

    try:
        # Create net rate scheme
        api_response = api_instance.create_discount_scheme(body=body)
        print("The response of NetRateSchemeApi->create_discount_scheme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetRateSchemeApi->create_discount_scheme: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiscountSchemeCreateDto**](DiscountSchemeCreateDto.md)|  | [optional] 

### Return type

[**NetRateScheme**](NetRateScheme.md)

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

# **edit_discount_scheme_workflow_step**
> NetRateSchemeWorkflowStep edit_discount_scheme_workflow_step(net_rate_scheme_uid, net_rate_scheme_workflow_step_id, body=body)

Edit scheme for workflow step

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.net_rate_scheme_workflow_step import NetRateSchemeWorkflowStep
from phrasetms_client.models.net_rate_scheme_workflow_step_edit import NetRateSchemeWorkflowStepEdit
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
    api_instance = phrasetms_client.NetRateSchemeApi(api_client)
    net_rate_scheme_uid = 'net_rate_scheme_uid_example' # str | 
    net_rate_scheme_workflow_step_id = 56 # int | 
    body = phrasetms_client.NetRateSchemeWorkflowStepEdit() # NetRateSchemeWorkflowStepEdit |  (optional)

    try:
        # Edit scheme for workflow step
        api_response = api_instance.edit_discount_scheme_workflow_step(net_rate_scheme_uid, net_rate_scheme_workflow_step_id, body=body)
        print("The response of NetRateSchemeApi->edit_discount_scheme_workflow_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetRateSchemeApi->edit_discount_scheme_workflow_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_rate_scheme_uid** | **str**|  | 
 **net_rate_scheme_workflow_step_id** | **int**|  | 
 **body** | [**NetRateSchemeWorkflowStepEdit**](NetRateSchemeWorkflowStepEdit.md)|  | [optional] 

### Return type

[**NetRateSchemeWorkflowStep**](NetRateSchemeWorkflowStep.md)

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

# **get_discount_scheme**
> NetRateScheme get_discount_scheme(net_rate_scheme_uid)

Get net rate scheme

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.net_rate_scheme import NetRateScheme
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
    api_instance = phrasetms_client.NetRateSchemeApi(api_client)
    net_rate_scheme_uid = 'net_rate_scheme_uid_example' # str | 

    try:
        # Get net rate scheme
        api_response = api_instance.get_discount_scheme(net_rate_scheme_uid)
        print("The response of NetRateSchemeApi->get_discount_scheme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetRateSchemeApi->get_discount_scheme: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_rate_scheme_uid** | **str**|  | 

### Return type

[**NetRateScheme**](NetRateScheme.md)

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

# **get_discount_scheme_workflow_step**
> NetRateSchemeWorkflowStep get_discount_scheme_workflow_step(net_rate_scheme_uid, net_rate_scheme_workflow_step_id)

Get scheme for workflow step

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.net_rate_scheme_workflow_step import NetRateSchemeWorkflowStep
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
    api_instance = phrasetms_client.NetRateSchemeApi(api_client)
    net_rate_scheme_uid = 'net_rate_scheme_uid_example' # str | 
    net_rate_scheme_workflow_step_id = 56 # int | 

    try:
        # Get scheme for workflow step
        api_response = api_instance.get_discount_scheme_workflow_step(net_rate_scheme_uid, net_rate_scheme_workflow_step_id)
        print("The response of NetRateSchemeApi->get_discount_scheme_workflow_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetRateSchemeApi->get_discount_scheme_workflow_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_rate_scheme_uid** | **str**|  | 
 **net_rate_scheme_workflow_step_id** | **int**|  | 

### Return type

[**NetRateSchemeWorkflowStep**](NetRateSchemeWorkflowStep.md)

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

# **get_discount_scheme_workflow_steps**
> PageDtoNetRateSchemeWorkflowStepReference get_discount_scheme_workflow_steps(net_rate_scheme_uid, page_number=page_number, page_size=page_size)

List schemes for workflow step

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_net_rate_scheme_workflow_step_reference import PageDtoNetRateSchemeWorkflowStepReference
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
    api_instance = phrasetms_client.NetRateSchemeApi(api_client)
    net_rate_scheme_uid = 'net_rate_scheme_uid_example' # str | 
    page_number = 0 # int |  (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List schemes for workflow step
        api_response = api_instance.get_discount_scheme_workflow_steps(net_rate_scheme_uid, page_number=page_number, page_size=page_size)
        print("The response of NetRateSchemeApi->get_discount_scheme_workflow_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetRateSchemeApi->get_discount_scheme_workflow_steps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_rate_scheme_uid** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoNetRateSchemeWorkflowStepReference**](PageDtoNetRateSchemeWorkflowStepReference.md)

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

# **get_discount_schemes**
> PageDtoNetRateSchemeReference get_discount_schemes(page_number=page_number, page_size=page_size)

List net rate schemes

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_net_rate_scheme_reference import PageDtoNetRateSchemeReference
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
    api_instance = phrasetms_client.NetRateSchemeApi(api_client)
    page_number = 0 # int |  (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List net rate schemes
        api_response = api_instance.get_discount_schemes(page_number=page_number, page_size=page_size)
        print("The response of NetRateSchemeApi->get_discount_schemes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetRateSchemeApi->get_discount_schemes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoNetRateSchemeReference**](PageDtoNetRateSchemeReference.md)

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

# **update_discount_scheme**
> NetRateScheme update_discount_scheme(net_rate_scheme_uid, body=body)

Edit net rate scheme

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.net_rate_scheme import NetRateScheme
from phrasetms_client.models.net_rate_scheme_edit import NetRateSchemeEdit
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
    api_instance = phrasetms_client.NetRateSchemeApi(api_client)
    net_rate_scheme_uid = 'net_rate_scheme_uid_example' # str | 
    body = phrasetms_client.NetRateSchemeEdit() # NetRateSchemeEdit |  (optional)

    try:
        # Edit net rate scheme
        api_response = api_instance.update_discount_scheme(net_rate_scheme_uid, body=body)
        print("The response of NetRateSchemeApi->update_discount_scheme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetRateSchemeApi->update_discount_scheme: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_rate_scheme_uid** | **str**|  | 
 **body** | [**NetRateSchemeEdit**](NetRateSchemeEdit.md)|  | [optional] 

### Return type

[**NetRateScheme**](NetRateScheme.md)

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

