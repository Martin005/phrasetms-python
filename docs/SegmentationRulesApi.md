# phrasetms_client.SegmentationRulesApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segmentation_rule**](SegmentationRulesApi.md#create_segmentation_rule) | **POST** /api2/v1/segmentationRules | Create segmentation rule
[**deletes_segmentation_rule**](SegmentationRulesApi.md#deletes_segmentation_rule) | **DELETE** /api2/v1/segmentationRules/{segRuleId} | Delete segmentation rule
[**get_list_of_segmentation_rules**](SegmentationRulesApi.md#get_list_of_segmentation_rules) | **GET** /api2/v1/segmentationRules | List segmentation rules
[**get_segmentation_rule**](SegmentationRulesApi.md#get_segmentation_rule) | **GET** /api2/v1/segmentationRules/{segRuleId} | Get segmentation rule
[**updates_segmentation_rule**](SegmentationRulesApi.md#updates_segmentation_rule) | **PUT** /api2/v1/segmentationRules/{segRuleId} | Edit segmentation rule


# **create_segmentation_rule**
> SegmentationRuleDto create_segmentation_rule(seg_rule, body)

Create segmentation rule

Creates new Segmentation Rule with file and segRule JSON Object as header parameter. The same object is used for GET action.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.segmentation_rule_dto import SegmentationRuleDto
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
    api_instance = phrasetms_client.SegmentationRulesApi(api_client)
    seg_rule = '{name:'name', locale:'en', primary:'false', filename:'extra_file.xml'}' # str | 
    body = None # object | streamed file

    try:
        # Create segmentation rule
        api_response = api_instance.create_segmentation_rule(seg_rule, body)
        print("The response of SegmentationRulesApi->create_segmentation_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentationRulesApi->create_segmentation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seg_rule** | **str**|  | 
 **body** | **object**| streamed file | 

### Return type

[**SegmentationRuleDto**](SegmentationRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
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

# **deletes_segmentation_rule**
> deletes_segmentation_rule(seg_rule_id)

Delete segmentation rule

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
    api_instance = phrasetms_client.SegmentationRulesApi(api_client)
    seg_rule_id = 56 # int | 

    try:
        # Delete segmentation rule
        api_instance.deletes_segmentation_rule(seg_rule_id)
    except Exception as e:
        print("Exception when calling SegmentationRulesApi->deletes_segmentation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seg_rule_id** | **int**|  | 

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

# **get_list_of_segmentation_rules**
> PageDtoSegmentationRuleReference get_list_of_segmentation_rules(locales=locales, page_number=page_number, page_size=page_size)

List segmentation rules

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_segmentation_rule_reference import PageDtoSegmentationRuleReference
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
    api_instance = phrasetms_client.SegmentationRulesApi(api_client)
    locales = ['locales_example'] # List[str] |  (optional)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List segmentation rules
        api_response = api_instance.get_list_of_segmentation_rules(locales=locales, page_number=page_number, page_size=page_size)
        print("The response of SegmentationRulesApi->get_list_of_segmentation_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentationRulesApi->get_list_of_segmentation_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locales** | [**List[str]**](str.md)|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoSegmentationRuleReference**](PageDtoSegmentationRuleReference.md)

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

# **get_segmentation_rule**
> SegmentationRuleDto get_segmentation_rule(seg_rule_id)

Get segmentation rule

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.segmentation_rule_dto import SegmentationRuleDto
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
    api_instance = phrasetms_client.SegmentationRulesApi(api_client)
    seg_rule_id = 56 # int | 

    try:
        # Get segmentation rule
        api_response = api_instance.get_segmentation_rule(seg_rule_id)
        print("The response of SegmentationRulesApi->get_segmentation_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentationRulesApi->get_segmentation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seg_rule_id** | **int**|  | 

### Return type

[**SegmentationRuleDto**](SegmentationRuleDto.md)

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

# **updates_segmentation_rule**
> SegmentationRuleDto updates_segmentation_rule(seg_rule_id, body=body)

Edit segmentation rule

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.edit_segmentation_rule_dto import EditSegmentationRuleDto
from phrasetms_client.models.segmentation_rule_dto import SegmentationRuleDto
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
    api_instance = phrasetms_client.SegmentationRulesApi(api_client)
    seg_rule_id = 56 # int | 
    body = phrasetms_client.EditSegmentationRuleDto() # EditSegmentationRuleDto |  (optional)

    try:
        # Edit segmentation rule
        api_response = api_instance.updates_segmentation_rule(seg_rule_id, body=body)
        print("The response of SegmentationRulesApi->updates_segmentation_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentationRulesApi->updates_segmentation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seg_rule_id** | **int**|  | 
 **body** | [**EditSegmentationRuleDto**](EditSegmentationRuleDto.md)|  | [optional] 

### Return type

[**SegmentationRuleDto**](SegmentationRuleDto.md)

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

