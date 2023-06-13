<a id="__pageTop"></a>

# phrasetms_client.apis.tags.async_request_api.AsyncRequestApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                    | HTTP request                            | Description              |
| --------------------------------------------------------- | --------------------------------------- | ------------------------ |
| [**get_async_request**](#get_async_request)               | **get** /api2/v1/async/{asyncRequestId} | Get asynchronous request |
| [**get_current_limit_status**](#get_current_limit_status) | **get** /api2/v1/async/status           | Get current limits       |
| [**list_pending_requests**](#list_pending_requests)       | **get** /api2/v1/async                  | List pending requests    |

# **get_async_request**

<a id="get_async_request"></a>

> AsyncRequestDto get_async_request(async_request_id)

Get asynchronous request

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import async_request_api
from phrasetms_client.model.async_request_dto import AsyncRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = async_request_api.AsyncRequestApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'asyncRequestId': 1,
    }
    try:
        # Get asynchronous request
        api_response = api_instance.get_async_request(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AsyncRequestApi->get_async_request: %s\n" % e)
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

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| asyncRequestId | AsyncRequestIdSchema |             |

# AsyncRequestIdSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 64 bit integer |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_async_request.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_async_request.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_async_request.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_async_request.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_async_request.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_async_request.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_async_request.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_async_request.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_async_request.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_async_request.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_async_request.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_async_request.ApiResponseFor501) | Not implemented                                             |

#### get_async_request.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                   | Description | Notes |
| ------------------------------------------------------ | ----------- | ----- |
| [**AsyncRequestDto**](../../models/AsyncRequestDto.md) |             |

#### get_async_request.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_async_request.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_async_request.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_async_request.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_async_request.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_async_request.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_async_request.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_async_request.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_async_request.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_async_request.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_async_request.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_current_limit_status**

<a id="get_current_limit_status"></a>

> AsyncRequestStatusDto get_current_limit_status()

Get current limits

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import async_request_api
from phrasetms_client.model.async_request_status_dto import AsyncRequestStatusDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = async_request_api.AsyncRequestApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current limits
        api_response = api_instance.get_current_limit_status()
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AsyncRequestApi->get_current_limit_status: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                            | Description                                                 |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                     | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_current_limit_status.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_current_limit_status.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_current_limit_status.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_current_limit_status.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_current_limit_status.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_current_limit_status.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_current_limit_status.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_current_limit_status.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_current_limit_status.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_current_limit_status.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_current_limit_status.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_current_limit_status.ApiResponseFor501) | Not implemented                                             |

#### get_current_limit_status.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**AsyncRequestStatusDto**](../../models/AsyncRequestStatusDto.md) |             |

#### get_current_limit_status.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_current_limit_status.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_current_limit_status.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_current_limit_status.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_current_limit_status.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_current_limit_status.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_current_limit_status.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_current_limit_status.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_current_limit_status.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_current_limit_status.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_current_limit_status.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_pending_requests**

<a id="list_pending_requests"></a>

> PageDtoAsyncRequestDto list_pending_requests()

List pending requests

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import async_request_api
from phrasetms_client.model.page_dto_async_request_dto import PageDtoAsyncRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = async_request_api.AsyncRequestApi(api_client)

    # example passing only optional values
    query_params = {
        'all': False,
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List pending requests
        api_response = api_instance.list_pending_requests(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AsyncRequestApi->list_pending_requests: %s\n" % e)
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
| all        | AllSchema        |             | optional |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |

# AllSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

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

### Return Types, Responses

| Code | Class                                                         | Description                                                 |
| ---- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                  | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_pending_requests.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_pending_requests.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_pending_requests.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_pending_requests.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_pending_requests.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_pending_requests.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_pending_requests.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_pending_requests.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_pending_requests.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_pending_requests.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_pending_requests.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_pending_requests.ApiResponseFor501) | Not implemented                                             |

#### list_pending_requests.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoAsyncRequestDto**](../../models/PageDtoAsyncRequestDto.md) |             |

#### list_pending_requests.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_pending_requests.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_pending_requests.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_pending_requests.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_pending_requests.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_pending_requests.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_pending_requests.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_pending_requests.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_pending_requests.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_pending_requests.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_pending_requests.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
