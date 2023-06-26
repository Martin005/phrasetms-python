# phrasetms_client.WebhookApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web_hook1**](WebhookApi.md#create_web_hook1) | **POST** /api2/v2/webhooks | Create webhook
[**delete_web_hook1**](WebhookApi.md#delete_web_hook1) | **DELETE** /api2/v2/webhooks/{webHookUid} | Delete webhook
[**get_web_hook1**](WebhookApi.md#get_web_hook1) | **GET** /api2/v2/webhooks/{webHookUid} | Get webhook
[**get_web_hook_list1**](WebhookApi.md#get_web_hook_list1) | **GET** /api2/v2/webhooks | Lists webhooks
[**get_webhook_calls_list**](WebhookApi.md#get_webhook_calls_list) | **GET** /api2/v1/webhooksCalls | Lists webhook calls
[**get_webhook_previews**](WebhookApi.md#get_webhook_previews) | **GET** /api2/v2/webhooks/previews | Get webhook body previews
[**replay_last**](WebhookApi.md#replay_last) | **POST** /api2/v1/webhooksCalls/replay/latest | Replay last webhook calls
[**replay_webhook_calls**](WebhookApi.md#replay_webhook_calls) | **POST** /api2/v1/webhooksCalls/replay | Replay webhook calls
[**send_test_webhook**](WebhookApi.md#send_test_webhook) | **POST** /api2/v2/webhooks/{webhookUid}/test | Send test webhook
[**update_web_hook1**](WebhookApi.md#update_web_hook1) | **PUT** /api2/v2/webhooks/{webHookUid} | Edit webhook


# **create_web_hook1**
> WebHookDtoV2 create_web_hook1(body=body)

Create webhook

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.create_web_hook_dto import CreateWebHookDto
from phrasetms_client.models.web_hook_dto_v2 import WebHookDtoV2
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
    api_instance = phrasetms_client.WebhookApi(api_client)
    body = phrasetms_client.CreateWebHookDto() # CreateWebHookDto |  (optional)

    try:
        # Create webhook
        api_response = api_instance.create_web_hook1(body=body)
        print("The response of WebhookApi->create_web_hook1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->create_web_hook1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWebHookDto**](CreateWebHookDto.md)|  | [optional] 

### Return type

[**WebHookDtoV2**](WebHookDtoV2.md)

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

# **delete_web_hook1**
> delete_web_hook1(web_hook_uid)

Delete webhook

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
    api_instance = phrasetms_client.WebhookApi(api_client)
    web_hook_uid = 'web_hook_uid_example' # str | 

    try:
        # Delete webhook
        api_instance.delete_web_hook1(web_hook_uid)
    except Exception as e:
        print("Exception when calling WebhookApi->delete_web_hook1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_uid** | **str**|  | 

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

# **get_web_hook1**
> WebHookDtoV2 get_web_hook1(web_hook_uid)

Get webhook

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.web_hook_dto_v2 import WebHookDtoV2
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
    api_instance = phrasetms_client.WebhookApi(api_client)
    web_hook_uid = 'web_hook_uid_example' # str | 

    try:
        # Get webhook
        api_response = api_instance.get_web_hook1(web_hook_uid)
        print("The response of WebhookApi->get_web_hook1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_web_hook1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_uid** | **str**|  | 

### Return type

[**WebHookDtoV2**](WebHookDtoV2.md)

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

# **get_web_hook_list1**
> PageDtoWebHookDtoV2 get_web_hook_list1(page_number=page_number, page_size=page_size, name=name, status=status, url=url, events=events, created_by=created_by, modified_by=modified_by, sort_field=sort_field, sort_trend=sort_trend)

Lists webhooks

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_web_hook_dto_v2 import PageDtoWebHookDtoV2
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
    api_instance = phrasetms_client.WebhookApi(api_client)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    name = 'name_example' # str | Filter by webhook name (optional)
    status = 'status_example' # str | Filter by enabled/disabled status (optional)
    url = 'url_example' # str | Filter by webhook URL (optional)
    events = ['events_example'] # List[str] | Filter by webhook events (optional)
    created_by = ['created_by_example'] # List[str] | Filter by webhook creators UIDs (optional)
    modified_by = ['modified_by_example'] # List[str] | Filter by webhook updaters UIDs (optional)
    sort_field = 'sort_field_example' # str | Sort by this field (optional)
    sort_trend = 'ASC' # str | Sort direction (optional) (default to 'ASC')

    try:
        # Lists webhooks
        api_response = api_instance.get_web_hook_list1(page_number=page_number, page_size=page_size, name=name, status=status, url=url, events=events, created_by=created_by, modified_by=modified_by, sort_field=sort_field, sort_trend=sort_trend)
        print("The response of WebhookApi->get_web_hook_list1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_web_hook_list1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **name** | **str**| Filter by webhook name | [optional] 
 **status** | **str**| Filter by enabled/disabled status | [optional] 
 **url** | **str**| Filter by webhook URL | [optional] 
 **events** | [**List[str]**](str.md)| Filter by webhook events | [optional] 
 **created_by** | [**List[str]**](str.md)| Filter by webhook creators UIDs | [optional] 
 **modified_by** | [**List[str]**](str.md)| Filter by webhook updaters UIDs | [optional] 
 **sort_field** | **str**| Sort by this field | [optional] 
 **sort_trend** | **str**| Sort direction | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageDtoWebHookDtoV2**](PageDtoWebHookDtoV2.md)

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

# **get_webhook_calls_list**
> PageDtoWebhookCallDto get_webhook_calls_list(page_number=page_number, page_size=page_size, events=events, status=status, webhook_uid=webhook_uid, parent_uid=parent_uid)

Lists webhook calls

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_webhook_call_dto import PageDtoWebhookCallDto
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
    api_instance = phrasetms_client.WebhookApi(api_client)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
    events = ['events_example'] # List[str] | List of Webhook events to filter by (optional)
    status = 'status_example' # str | Status of Webhook calls to filter by (optional)
    webhook_uid = 'webhook_uid_example' # str | UID of Webhook to filter by (optional)
    parent_uid = 'parent_uid_example' # str | UID of parent webhook call to filter by (optional)

    try:
        # Lists webhook calls
        api_response = api_instance.get_webhook_calls_list(page_number=page_number, page_size=page_size, events=events, status=status, webhook_uid=webhook_uid, parent_uid=parent_uid)
        print("The response of WebhookApi->get_webhook_calls_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_webhook_calls_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **events** | [**List[str]**](str.md)| List of Webhook events to filter by | [optional] 
 **status** | **str**| Status of Webhook calls to filter by | [optional] 
 **webhook_uid** | **str**| UID of Webhook to filter by | [optional] 
 **parent_uid** | **str**| UID of parent webhook call to filter by | [optional] 

### Return type

[**PageDtoWebhookCallDto**](PageDtoWebhookCallDto.md)

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

# **get_webhook_previews**
> WebhookPreviewsDto get_webhook_previews(events=events)

Get webhook body previews

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.webhook_previews_dto import WebhookPreviewsDto
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
    api_instance = phrasetms_client.WebhookApi(api_client)
    events = ['events_example'] # List[str] | Filter by webhook events, example for multiple: ?events=JOB_CREATED&events=JOB_UPDATED (optional)

    try:
        # Get webhook body previews
        api_response = api_instance.get_webhook_previews(events=events)
        print("The response of WebhookApi->get_webhook_previews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_webhook_previews: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events** | [**List[str]**](str.md)| Filter by webhook events, example for multiple: ?events&#x3D;JOB_CREATED&amp;events&#x3D;JOB_UPDATED | [optional] 

### Return type

[**WebhookPreviewsDto**](WebhookPreviewsDto.md)

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

# **replay_last**
> replay_last(number_of_calls=number_of_calls, events=events, status=status)

Replay last webhook calls

 Replays specified number of last Webhook calls from oldest to the newest one 

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
    api_instance = phrasetms_client.WebhookApi(api_client)
    number_of_calls = 5 # int | Number of calls to be replayed (optional) (default to 5)
    events = ['events_example'] # List[str] | List of Webhook events to filter by (optional)
    status = 'status_example' # str | Status of Webhook calls to filter by (optional)

    try:
        # Replay last webhook calls
        api_instance.replay_last(number_of_calls=number_of_calls, events=events, status=status)
    except Exception as e:
        print("Exception when calling WebhookApi->replay_last: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number_of_calls** | **int**| Number of calls to be replayed | [optional] [default to 5]
 **events** | [**List[str]**](str.md)| List of Webhook events to filter by | [optional] 
 **status** | **str**| Status of Webhook calls to filter by | [optional] 

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
**202** | Accepted |  -  |
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

# **replay_webhook_calls**
> replay_webhook_calls(body=body)

Replay webhook calls

 Replays given list of Webhook Calls in specified order in the request 

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.replay_request_dto import ReplayRequestDto
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
    api_instance = phrasetms_client.WebhookApi(api_client)
    body = phrasetms_client.ReplayRequestDto() # ReplayRequestDto |  (optional)

    try:
        # Replay webhook calls
        api_instance.replay_webhook_calls(body=body)
    except Exception as e:
        print("Exception when calling WebhookApi->replay_webhook_calls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplayRequestDto**](ReplayRequestDto.md)|  | [optional] 

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
**202** | Accepted |  -  |
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

# **send_test_webhook**
> send_test_webhook(webhook_uid, event)

Send test webhook

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
    api_instance = phrasetms_client.WebhookApi(api_client)
    webhook_uid = 'webhook_uid_example' # str | UID of the webhook
    event = 'event_example' # str | Event of test webhook

    try:
        # Send test webhook
        api_instance.send_test_webhook(webhook_uid, event)
    except Exception as e:
        print("Exception when calling WebhookApi->send_test_webhook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_uid** | **str**| UID of the webhook | 
 **event** | **str**| Event of test webhook | 

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
**201** | Test webhook sent |  -  |
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

# **update_web_hook1**
> WebHookDtoV2 update_web_hook1(web_hook_uid, body=body)

Edit webhook

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.create_web_hook_dto import CreateWebHookDto
from phrasetms_client.models.web_hook_dto_v2 import WebHookDtoV2
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
    api_instance = phrasetms_client.WebhookApi(api_client)
    web_hook_uid = 'web_hook_uid_example' # str | 
    body = phrasetms_client.CreateWebHookDto() # CreateWebHookDto |  (optional)

    try:
        # Edit webhook
        api_response = api_instance.update_web_hook1(web_hook_uid, body=body)
        print("The response of WebhookApi->update_web_hook1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->update_web_hook1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_uid** | **str**|  | 
 **body** | [**CreateWebHookDto**](CreateWebHookDto.md)|  | [optional] 

### Return type

[**WebHookDtoV2**](WebHookDtoV2.md)

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

