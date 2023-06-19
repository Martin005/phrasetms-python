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
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WebhookApi()
body = phrasetms_client.CreateWebHookDto() # CreateWebHookDto |  (optional)

try:
    # Create webhook
    api_response = api_instance.create_web_hook1(body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_web_hook1**
> delete_web_hook1(web_hook_uid)

Delete webhook

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WebhookApi()
web_hook_uid = 'web_hook_uid_example' # str | 

try:
    # Delete webhook
    api_instance.delete_web_hook1(web_hook_uid)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_hook1**
> WebHookDtoV2 get_web_hook1(web_hook_uid)

Get webhook

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WebhookApi()
web_hook_uid = 'web_hook_uid_example' # str | 

try:
    # Get webhook
    api_response = api_instance.get_web_hook1(web_hook_uid)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_hook_list1**
> PageDtoWebHookDtoV2 get_web_hook_list1(page_number=page_number, page_size=page_size, name=name, status=status, url=url, events=events, created_by=created_by, modified_by=modified_by, sort_field=sort_field, sort_trend=sort_trend)

Lists webhooks

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WebhookApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
name = 'name_example' # str | Filter by webhook name (optional)
status = 'status_example' # str | Filter by enabled/disabled status (optional)
url = 'url_example' # str | Filter by webhook URL (optional)
events = ['events_example'] # list[str] | Filter by webhook events (optional)
created_by = ['created_by_example'] # list[str] | Filter by webhook creators UIDs (optional)
modified_by = ['modified_by_example'] # list[str] | Filter by webhook updaters UIDs (optional)
sort_field = 'sort_field_example' # str | Sort by this field (optional)
sort_trend = 'ASC' # str | Sort direction (optional) (default to ASC)

try:
    # Lists webhooks
    api_response = api_instance.get_web_hook_list1(page_number=page_number, page_size=page_size, name=name, status=status, url=url, events=events, created_by=created_by, modified_by=modified_by, sort_field=sort_field, sort_trend=sort_trend)
    pprint(api_response)
except ApiException as e:
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
 **events** | [**list[str]**](str.md)| Filter by webhook events | [optional] 
 **created_by** | [**list[str]**](str.md)| Filter by webhook creators UIDs | [optional] 
 **modified_by** | [**list[str]**](str.md)| Filter by webhook updaters UIDs | [optional] 
 **sort_field** | **str**| Sort by this field | [optional] 
 **sort_trend** | **str**| Sort direction | [optional] [default to ASC]

### Return type

[**PageDtoWebHookDtoV2**](PageDtoWebHookDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_calls_list**
> PageDtoWebhookCallDto get_webhook_calls_list(page_number=page_number, page_size=page_size, events=events, status=status, webhook_uid=webhook_uid, parent_uid=parent_uid)

Lists webhook calls

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WebhookApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
events = ['events_example'] # list[str] | List of Webhook events to filter by (optional)
status = 'status_example' # str | Status of Webhook calls to filter by (optional)
webhook_uid = 'webhook_uid_example' # str | UID of Webhook to filter by (optional)
parent_uid = 'parent_uid_example' # str | UID of parent webhook call to filter by (optional)

try:
    # Lists webhook calls
    api_response = api_instance.get_webhook_calls_list(page_number=page_number, page_size=page_size, events=events, status=status, webhook_uid=webhook_uid, parent_uid=parent_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_webhook_calls_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **events** | [**list[str]**](str.md)| List of Webhook events to filter by | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_previews**
> WebhookPreviewsDto get_webhook_previews(events=events)

Get webhook body previews

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WebhookApi()
events = ['events_example'] # list[str] | Filter by webhook events, example for multiple: ?events=JOB_CREATED&events=JOB_UPDATED (optional)

try:
    # Get webhook body previews
    api_response = api_instance.get_webhook_previews(events=events)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_webhook_previews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events** | [**list[str]**](str.md)| Filter by webhook events, example for multiple: ?events&#x3D;JOB_CREATED&amp;events&#x3D;JOB_UPDATED | [optional] 

### Return type

[**WebhookPreviewsDto**](WebhookPreviewsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replay_last**
> replay_last(number_of_calls=number_of_calls, events=events, status=status)

Replay last webhook calls

 Replays specified number of last Webhook calls from oldest to the newest one 

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WebhookApi()
number_of_calls = 5 # int | Number of calls to be replayed (optional) (default to 5)
events = ['events_example'] # list[str] | List of Webhook events to filter by (optional)
status = 'status_example' # str | Status of Webhook calls to filter by (optional)

try:
    # Replay last webhook calls
    api_instance.replay_last(number_of_calls=number_of_calls, events=events, status=status)
except ApiException as e:
    print("Exception when calling WebhookApi->replay_last: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number_of_calls** | **int**| Number of calls to be replayed | [optional] [default to 5]
 **events** | [**list[str]**](str.md)| List of Webhook events to filter by | [optional] 
 **status** | **str**| Status of Webhook calls to filter by | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replay_webhook_calls**
> replay_webhook_calls(body=body)

Replay webhook calls

 Replays given list of Webhook Calls in specified order in the request 

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WebhookApi()
body = phrasetms_client.ReplayRequestDto() # ReplayRequestDto |  (optional)

try:
    # Replay webhook calls
    api_instance.replay_webhook_calls(body=body)
except ApiException as e:
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

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_webhook**
> send_test_webhook(webhook_uid, event)

Send test webhook

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WebhookApi()
webhook_uid = 'webhook_uid_example' # str | UID of the webhook
event = 'event_example' # str | Event of test webhook

try:
    # Send test webhook
    api_instance.send_test_webhook(webhook_uid, event)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web_hook1**
> WebHookDtoV2 update_web_hook1(web_hook_uid, body=body)

Edit webhook

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.WebhookApi()
web_hook_uid = 'web_hook_uid_example' # str | 
body = phrasetms_client.CreateWebHookDto() # CreateWebHookDto |  (optional)

try:
    # Edit webhook
    api_response = api_instance.update_web_hook1(web_hook_uid, body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

