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
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.NetRateSchemeApi()
body = phrasetms_client.DiscountSchemeCreateDto() # DiscountSchemeCreateDto |  (optional)

try:
    # Create net rate scheme
    api_response = api_instance.create_discount_scheme(body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_discount_scheme_workflow_step**
> NetRateSchemeWorkflowStep edit_discount_scheme_workflow_step(net_rate_scheme_uid, net_rate_scheme_workflow_step_id, body=body)

Edit scheme for workflow step

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.NetRateSchemeApi()
net_rate_scheme_uid = 'net_rate_scheme_uid_example' # str | 
net_rate_scheme_workflow_step_id = 789 # int | 
body = phrasetms_client.NetRateSchemeWorkflowStepEdit() # NetRateSchemeWorkflowStepEdit |  (optional)

try:
    # Edit scheme for workflow step
    api_response = api_instance.edit_discount_scheme_workflow_step(net_rate_scheme_uid, net_rate_scheme_workflow_step_id, body=body)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_scheme**
> NetRateScheme get_discount_scheme(net_rate_scheme_uid)

Get net rate scheme

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.NetRateSchemeApi()
net_rate_scheme_uid = 'net_rate_scheme_uid_example' # str | 

try:
    # Get net rate scheme
    api_response = api_instance.get_discount_scheme(net_rate_scheme_uid)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_scheme_workflow_step**
> NetRateSchemeWorkflowStep get_discount_scheme_workflow_step(net_rate_scheme_uid, net_rate_scheme_workflow_step_id)

Get scheme for workflow step

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.NetRateSchemeApi()
net_rate_scheme_uid = 'net_rate_scheme_uid_example' # str | 
net_rate_scheme_workflow_step_id = 789 # int | 

try:
    # Get scheme for workflow step
    api_response = api_instance.get_discount_scheme_workflow_step(net_rate_scheme_uid, net_rate_scheme_workflow_step_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_scheme_workflow_steps**
> PageDtoNetRateSchemeWorkflowStepReference get_discount_scheme_workflow_steps(net_rate_scheme_uid, page_number=page_number, page_size=page_size)

List schemes for workflow step

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.NetRateSchemeApi()
net_rate_scheme_uid = 'net_rate_scheme_uid_example' # str | 
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List schemes for workflow step
    api_response = api_instance.get_discount_scheme_workflow_steps(net_rate_scheme_uid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discount_schemes**
> PageDtoNetRateSchemeReference get_discount_schemes(page_number=page_number, page_size=page_size)

List net rate schemes

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.NetRateSchemeApi()
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List net rate schemes
    api_response = api_instance.get_discount_schemes(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_discount_scheme**
> NetRateScheme update_discount_scheme(net_rate_scheme_uid, body=body)

Edit net rate scheme

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.NetRateSchemeApi()
net_rate_scheme_uid = 'net_rate_scheme_uid_example' # str | 
body = phrasetms_client.NetRateSchemeEdit() # NetRateSchemeEdit |  (optional)

try:
    # Edit net rate scheme
    api_response = api_instance.update_discount_scheme(net_rate_scheme_uid, body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

