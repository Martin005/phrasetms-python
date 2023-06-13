<a id="__pageTop"></a>

# phrasetms_client.apis.tags.webhook_api.WebhookApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                | HTTP request                                  | Description               |
| ----------------------------------------------------- | --------------------------------------------- | ------------------------- |
| [**create_web_hook1**](#create_web_hook1)             | **post** /api2/v2/webhooks                    | Create webhook            |
| [**delete_web_hook1**](#delete_web_hook1)             | **delete** /api2/v2/webhooks/{webHookUid}     | Delete webhook            |
| [**get_web_hook1**](#get_web_hook1)                   | **get** /api2/v2/webhooks/{webHookUid}        | Get webhook               |
| [**get_web_hook_list1**](#get_web_hook_list1)         | **get** /api2/v2/webhooks                     | Lists webhooks            |
| [**get_webhook_calls_list**](#get_webhook_calls_list) | **get** /api2/v1/webhooksCalls                | Lists webhook calls       |
| [**get_webhook_previews**](#get_webhook_previews)     | **get** /api2/v2/webhooks/previews            | Get webhook body previews |
| [**replay_last**](#replay_last)                       | **post** /api2/v1/webhooksCalls/replay/latest | Replay last webhook calls |
| [**replay_webhook_calls**](#replay_webhook_calls)     | **post** /api2/v1/webhooksCalls/replay        | Replay webhook calls      |
| [**send_test_webhook**](#send_test_webhook)           | **post** /api2/v2/webhooks/{webhookUid}/test  | Send test webhook         |
| [**update_web_hook1**](#update_web_hook1)             | **put** /api2/v2/webhooks/{webHookUid}        | Edit webhook              |

# **create_web_hook1**

<a id="create_web_hook1"></a>

> WebHookDtoV2 create_web_hook1()

Create webhook

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import webhook_api
from phrasetms_client.model.web_hook_dto_v2 import WebHookDtoV2
from phrasetms_client.model.create_web_hook_dto import CreateWebHookDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)

    # example passing only optional values
    body = CreateWebHookDto(
        name="name_example",
        url="url_example",
        events=[
            "JOB_STATUS_CHANGED"
        ],
        secret_token="secret_token_example",
        hidden=True,
        status="ENABLED",
    )
    try:
        # Create webhook
        api_response = api_instance.create_web_hook1(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->create_web_hook1: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**CreateWebHookDto**](../../models/CreateWebHookDto.md) |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_web_hook1.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_web_hook1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_web_hook1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_web_hook1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_web_hook1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_web_hook1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_web_hook1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_web_hook1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_web_hook1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_web_hook1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_web_hook1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_web_hook1.ApiResponseFor501) | Not implemented                                             |

#### create_web_hook1.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                             | Description | Notes |
| ------------------------------------------------ | ----------- | ----- |
| [**WebHookDtoV2**](../../models/WebHookDtoV2.md) |             |

#### create_web_hook1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_web_hook1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_web_hook1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_web_hook1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_web_hook1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_web_hook1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_web_hook1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_web_hook1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_web_hook1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_web_hook1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_web_hook1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_web_hook1**

<a id="delete_web_hook1"></a>

> delete_web_hook1(web_hook_uid)

Delete webhook

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import webhook_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'webHookUid': "webHookUid_example",
    }
    try:
        # Delete webhook
        api_response = api_instance.delete_web_hook1(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->delete_web_hook1: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| webHookUid | WebHookUidSchema |             |

# WebHookUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_web_hook1.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_web_hook1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_web_hook1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_web_hook1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_web_hook1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_web_hook1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_web_hook1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_web_hook1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_web_hook1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_web_hook1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_web_hook1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_web_hook1.ApiResponseFor501) | Not implemented                                             |

#### delete_web_hook1.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_web_hook1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_web_hook1**

<a id="get_web_hook1"></a>

> WebHookDtoV2 get_web_hook1(web_hook_uid)

Get webhook

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import webhook_api
from phrasetms_client.model.web_hook_dto_v2 import WebHookDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'webHookUid': "webHookUid_example",
    }
    try:
        # Get webhook
        api_response = api_instance.get_web_hook1(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->get_web_hook1: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| webHookUid | WebHookUidSchema |             |

# WebHookUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_web_hook1.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_web_hook1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_web_hook1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_web_hook1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_web_hook1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_web_hook1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_web_hook1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_web_hook1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_web_hook1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_web_hook1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_web_hook1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_web_hook1.ApiResponseFor501) | Not implemented                                             |

#### get_web_hook1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                             | Description | Notes |
| ------------------------------------------------ | ----------- | ----- |
| [**WebHookDtoV2**](../../models/WebHookDtoV2.md) |             |

#### get_web_hook1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_web_hook_list1**

<a id="get_web_hook_list1"></a>

> PageDtoWebHookDtoV2 get_web_hook_list1()

Lists webhooks

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import webhook_api
from phrasetms_client.model.page_dto_web_hook_dto_v2 import PageDtoWebHookDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)

    # example passing only optional values
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
        'name': "name_example",
        'status': "ENABLED",
        'url': "url_example",
        'events': [
        "JOB_STATUS_CHANGED"
    ],
        'createdBy': [
        "createdBy_example"
    ],
        'modifiedBy': [
        "modifiedBy_example"
    ],
        'sortField': "NAME",
        'sortTrend': "ASC",
    }
    try:
        # Lists webhooks
        api_response = api_instance.get_web_hook_list1(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->get_web_hook_list1: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name       | Type             | Description | Notes    |
| ---------- | ---------------- | ----------- | -------- |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |
| name       | NameSchema       |             | optional |
| status     | StatusSchema     |             | optional |
| url        | UrlSchema        |             | optional |
| events     | EventsSchema     |             | optional |
| createdBy  | CreatedBySchema  |             | optional |
| modifiedBy | ModifiedBySchema |             | optional |
| sortField  | SortFieldSchema  |             | optional |
| sortTrend  | SortTrendSchema  |             | optional |

# PageNumberSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 0value must be a 32 bit integer |

# PageSizeSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                                |
| --------------------- | ---------------- | ----------- | ------------------------------------------------------------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 50value must be a 32 bit integer |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# StatusSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                    |
| ---------- | ------------- | ----------- | ---------------------------------------- |
| str,       | str,          |             | must be one of ["ENABLED", "DISABLED", ] |

# UrlSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# EventsSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ---------- | ------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["JOB_STATUS_CHANGED", "JOB_CREATED", "JOB_DELETED", "JOB_ASSIGNED", "JOB_DUE_DATE_CHANGED", "JOB_UPDATED", "JOB_TARGET_UPDATED", "JOB_EXPORTED", "JOB_UNEXPORTED", "PROJECT_CREATED", "PROJECT_DELETED", "PROJECT_STATUS_CHANGED", "PROJECT_DUE_DATE_CHANGED", "SHARED_PROJECT_ASSIGNED", "PROJECT_METADATA_UPDATED", "PRE_TRANSLATION_FINISHED", "ANALYSIS_CREATED", "CONTINUOUS_JOB_UPDATED", "PROJECT_TEMPLATE_CREATED", "PROJECT_TEMPLATE_UPDATED", "PROJECT_TEMPLATE_DELETED", ] |

# CreatedBySchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# ModifiedBySchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# SortFieldSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                           |
| ---------- | ------------- | ----------- | --------------------------------------------------------------- |
| str,       | str,          |             | must be one of ["NAME", "STATUS", "CREATED", "LAST_MODIFIED", ] |

# SortTrendSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                      |
| ---------- | ------------- | ----------- | ------------------------------------------------------------------------------------------ |
| str,       | str,          |             | must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "ASC" |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_web_hook_list1.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_web_hook_list1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_web_hook_list1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_web_hook_list1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_web_hook_list1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_web_hook_list1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_web_hook_list1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_web_hook_list1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_web_hook_list1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_web_hook_list1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_web_hook_list1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_web_hook_list1.ApiResponseFor501) | Not implemented                                             |

#### get_web_hook_list1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoWebHookDtoV2**](../../models/PageDtoWebHookDtoV2.md) |             |

#### get_web_hook_list1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook_list1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook_list1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook_list1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook_list1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook_list1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook_list1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook_list1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook_list1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook_list1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_web_hook_list1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_webhook_calls_list**

<a id="get_webhook_calls_list"></a>

> PageDtoWebhookCallDto get_webhook_calls_list()

Lists webhook calls

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import webhook_api
from phrasetms_client.model.page_dto_webhook_call_dto import PageDtoWebhookCallDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)

    # example passing only optional values
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
        'events': [
        "JOB_STATUS_CHANGED"
    ],
        'status': "SUCCESS",
        'webhookUid': "webhookUid_example",
        'parentUid': "parentUid_example",
    }
    try:
        # Lists webhook calls
        api_response = api_instance.get_webhook_calls_list(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->get_webhook_calls_list: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name       | Type             | Description | Notes    |
| ---------- | ---------------- | ----------- | -------- |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |
| events     | EventsSchema     |             | optional |
| status     | StatusSchema     |             | optional |
| webhookUid | WebhookUidSchema |             | optional |
| parentUid  | ParentUidSchema  |             | optional |

# PageNumberSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 0value must be a 32 bit integer |

# PageSizeSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                                |
| --------------------- | ---------------- | ----------- | ------------------------------------------------------------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 50value must be a 32 bit integer |

# EventsSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ---------- | ------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["JOB_STATUS_CHANGED", "JOB_CREATED", "JOB_DELETED", "JOB_ASSIGNED", "JOB_DUE_DATE_CHANGED", "JOB_UPDATED", "JOB_TARGET_UPDATED", "JOB_EXPORTED", "JOB_UNEXPORTED", "PROJECT_CREATED", "PROJECT_DELETED", "PROJECT_STATUS_CHANGED", "PROJECT_DUE_DATE_CHANGED", "SHARED_PROJECT_ASSIGNED", "PROJECT_METADATA_UPDATED", "PRE_TRANSLATION_FINISHED", "ANALYSIS_CREATED", "CONTINUOUS_JOB_UPDATED", "PROJECT_TEMPLATE_CREATED", "PROJECT_TEMPLATE_UPDATED", "PROJECT_TEMPLATE_DELETED", ] |

# StatusSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                |
| ---------- | ------------- | ----------- | ------------------------------------ |
| str,       | str,          |             | must be one of ["SUCCESS", "FAIL", ] |

# WebhookUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ParentUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_webhook_calls_list.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_webhook_calls_list.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_webhook_calls_list.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_webhook_calls_list.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_webhook_calls_list.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_webhook_calls_list.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_webhook_calls_list.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_webhook_calls_list.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_webhook_calls_list.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_webhook_calls_list.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_webhook_calls_list.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_webhook_calls_list.ApiResponseFor501) | Not implemented                                             |

#### get_webhook_calls_list.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**PageDtoWebhookCallDto**](../../models/PageDtoWebhookCallDto.md) |             |

#### get_webhook_calls_list.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_calls_list.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_calls_list.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_calls_list.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_calls_list.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_calls_list.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_calls_list.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_calls_list.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_calls_list.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_calls_list.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_calls_list.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_webhook_previews**

<a id="get_webhook_previews"></a>

> WebhookPreviewsDto get_webhook_previews()

Get webhook body previews

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import webhook_api
from phrasetms_client.model.webhook_previews_dto import WebhookPreviewsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)

    # example passing only optional values
    query_params = {
        'events': [
        "JOB_STATUS_CHANGED"
    ],
    }
    try:
        # Get webhook body previews
        api_response = api_instance.get_webhook_previews(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->get_webhook_previews: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name   | Type         | Description | Notes    |
| ------ | ------------ | ----------- | -------- |
| events | EventsSchema |             | optional |

# EventsSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ---------- | ------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["JOB_STATUS_CHANGED", "JOB_CREATED", "JOB_ASSIGNED", "JOB_DUE_DATE_CHANGED", "JOB_DELETED", "JOB_UPDATED", "JOB_TARGET_UPDATED", "JOB_EXPORTED", "JOB_UNEXPORTED", "PROJECT_CREATED", "PROJECT_STATUS_CHANGED", "PROJECT_DUE_DATE_CHANGED", "SHARED_PROJECT_ASSIGNED", "PROJECT_METADATA_UPDATED", "PROJECT_DELETED", "PRE_TRANSLATION_FINISHED", "ANALYSIS_CREATED", "CONTINUOUS_JOB_UPDATED", "PROJECT_TEMPLATE_CREATED", "PROJECT_TEMPLATE_UPDATED", "PROJECT_TEMPLATE_DELETED", ] |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_webhook_previews.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_webhook_previews.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_webhook_previews.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_webhook_previews.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_webhook_previews.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_webhook_previews.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_webhook_previews.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_webhook_previews.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_webhook_previews.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_webhook_previews.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_webhook_previews.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_webhook_previews.ApiResponseFor501) | Not implemented                                             |

#### get_webhook_previews.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**WebhookPreviewsDto**](../../models/WebhookPreviewsDto.md) |             |

#### get_webhook_previews.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_previews.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_previews.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_previews.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_previews.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_previews.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_previews.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_previews.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_previews.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_previews.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_webhook_previews.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replay_last**

<a id="replay_last"></a>

> replay_last()

Replay last webhook calls

Replays specified number of last Webhook calls from oldest to the newest one

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import webhook_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)

    # example passing only optional values
    query_params = {
        'numberOfCalls': 5,
        'events': [
        "JOB_STATUS_CHANGED"
    ],
        'status': "SUCCESS",
    }
    try:
        # Replay last webhook calls
        api_response = api_instance.replay_last(
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->replay_last: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name          | Type                | Description | Notes    |
| ------------- | ------------------- | ----------- | -------- |
| numberOfCalls | NumberOfCallsSchema |             | optional |
| events        | EventsSchema        |             | optional |
| status        | StatusSchema        |             | optional |

# NumberOfCallsSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 5value must be a 32 bit integer |

# EventsSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ---------- | ------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["JOB_STATUS_CHANGED", "JOB_CREATED", "JOB_DELETED", "JOB_ASSIGNED", "JOB_DUE_DATE_CHANGED", "JOB_UPDATED", "JOB_TARGET_UPDATED", "JOB_EXPORTED", "JOB_UNEXPORTED", "PROJECT_CREATED", "PROJECT_DELETED", "PROJECT_STATUS_CHANGED", "PROJECT_DUE_DATE_CHANGED", "SHARED_PROJECT_ASSIGNED", "PROJECT_METADATA_UPDATED", "PRE_TRANSLATION_FINISHED", "ANALYSIS_CREATED", "CONTINUOUS_JOB_UPDATED", "PROJECT_TEMPLATE_CREATED", "PROJECT_TEMPLATE_UPDATED", "PROJECT_TEMPLATE_DELETED", ] |

# StatusSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                |
| ---------- | ------------- | ----------- | ------------------------------------ |
| str,       | str,          |             | must be one of ["SUCCESS", "FAIL", ] |

### Return Types, Responses

| Code | Class                                               | Description                                                 |
| ---- | --------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization        | When skip_deserialization is True this response is returned |
| 202  | [ApiResponseFor202](#replay_last.ApiResponseFor202) | Accepted                                                    |
| 400  | [ApiResponseFor400](#replay_last.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#replay_last.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#replay_last.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#replay_last.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#replay_last.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#replay_last.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#replay_last.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#replay_last.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#replay_last.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#replay_last.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#replay_last.ApiResponseFor501) | Not implemented                                             |

#### replay_last.ApiResponseFor202

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_last.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replay_webhook_calls**

<a id="replay_webhook_calls"></a>

> replay_webhook_calls()

Replay webhook calls

Replays given list of Webhook Calls in specified order in the request

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import webhook_api
from phrasetms_client.model.replay_request_dto import ReplayRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)

    # example passing only optional values
    body = ReplayRequestDto(
        webhook_calls=[
            UidReference(
                uid="uid_example",
            )
        ],
    )
    try:
        # Replay webhook calls
        api_response = api_instance.replay_webhook_calls(
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->replay_webhook_calls: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBody, Unset]        | optional, default is unset |
| content_type         | str                                              | optional, default is '_/_' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                             | default is False           | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None            | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False           | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBody

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**ReplayRequestDto**](../../models/ReplayRequestDto.md) |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 202  | [ApiResponseFor202](#replay_webhook_calls.ApiResponseFor202) | Accepted                                                    |
| 400  | [ApiResponseFor400](#replay_webhook_calls.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#replay_webhook_calls.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#replay_webhook_calls.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#replay_webhook_calls.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#replay_webhook_calls.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#replay_webhook_calls.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#replay_webhook_calls.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#replay_webhook_calls.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#replay_webhook_calls.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#replay_webhook_calls.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#replay_webhook_calls.ApiResponseFor501) | Not implemented                                             |

#### replay_webhook_calls.ApiResponseFor202

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### replay_webhook_calls.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **send_test_webhook**

<a id="send_test_webhook"></a>

> send_test_webhook(webhook_uidevent)

Send test webhook

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import webhook_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'webhookUid': "webhookUid_example",
    }
    query_params = {
        'event': "JOB_STATUS_CHANGED",
    }
    try:
        # Send test webhook
        api_response = api_instance.send_test_webhook(
            path_params=path_params,
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->send_test_webhook: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                  |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name  | Type        | Description | Notes |
| ----- | ----------- | ----------- | ----- |
| event | EventSchema |             |

# EventSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| str,       | str,          |             | must be one of ["JOB_STATUS_CHANGED", "JOB_CREATED", "JOB_DELETED", "JOB_ASSIGNED", "JOB_DUE_DATE_CHANGED", "JOB_UPDATED", "JOB_TARGET_UPDATED", "JOB_EXPORTED", "JOB_UNEXPORTED", "PROJECT_CREATED", "PROJECT_DELETED", "PROJECT_STATUS_CHANGED", "PROJECT_DUE_DATE_CHANGED", "SHARED_PROJECT_ASSIGNED", "PROJECT_METADATA_UPDATED", "PRE_TRANSLATION_FINISHED", "ANALYSIS_CREATED", "CONTINUOUS_JOB_UPDATED", "PROJECT_TEMPLATE_CREATED", "PROJECT_TEMPLATE_UPDATED", "PROJECT_TEMPLATE_DELETED", ] |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| webhookUid | WebhookUidSchema |             |

# WebhookUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#send_test_webhook.ApiResponseFor201) | Test webhook sent                                           |
| 400  | [ApiResponseFor400](#send_test_webhook.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#send_test_webhook.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#send_test_webhook.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#send_test_webhook.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#send_test_webhook.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#send_test_webhook.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#send_test_webhook.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#send_test_webhook.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#send_test_webhook.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#send_test_webhook.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#send_test_webhook.ApiResponseFor501) | Not implemented                                             |

#### send_test_webhook.ApiResponseFor201

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_test_webhook.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_web_hook1**

<a id="update_web_hook1"></a>

> WebHookDtoV2 update_web_hook1(web_hook_uid)

Edit webhook

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import webhook_api
from phrasetms_client.model.web_hook_dto_v2 import WebHookDtoV2
from phrasetms_client.model.create_web_hook_dto import CreateWebHookDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_api.WebhookApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'webHookUid': "webHookUid_example",
    }
    try:
        # Edit webhook
        api_response = api_instance.update_web_hook1(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->update_web_hook1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'webHookUid': "webHookUid_example",
    }
    body = CreateWebHookDto(
        name="name_example",
        url="url_example",
        events=[
            "JOB_STATUS_CHANGED"
        ],
        secret_token="secret_token_example",
        hidden=True,
        status="ENABLED",
    )
    try:
        # Edit webhook
        api_response = api_instance.update_web_hook1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling WebhookApi->update_web_hook1: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**CreateWebHookDto**](../../models/CreateWebHookDto.md) |             |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| webHookUid | WebHookUidSchema |             |

# WebHookUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#update_web_hook1.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#update_web_hook1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_web_hook1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_web_hook1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_web_hook1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_web_hook1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_web_hook1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_web_hook1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_web_hook1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_web_hook1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_web_hook1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_web_hook1.ApiResponseFor501) | Not implemented                                             |

#### update_web_hook1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                             | Description | Notes |
| ------------------------------------------------ | ----------- | ----- |
| [**WebHookDtoV2**](../../models/WebHookDtoV2.md) |             |

#### update_web_hook1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_web_hook1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_web_hook1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_web_hook1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_web_hook1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_web_hook1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_web_hook1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_web_hook1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_web_hook1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_web_hook1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_web_hook1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
