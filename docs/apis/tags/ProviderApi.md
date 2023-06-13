<a id="__pageTop"></a>

# phrasetms_client.apis.tags.provider_api.ProviderApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                  | HTTP request                                                            | Description             |
| ------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------- |
| [**get_project_assignments**](#get_project_assignments) | **get** /api2/v1/projects/{projectUid}/providers                        | List project providers  |
| [**list_providers3**](#list_providers3)                 | **post** /api2/v2/projects/{projectUid}/providers/suggest               | Get suggested providers |
| [**list_providers4**](#list_providers4)                 | **post** /api2/v2/projects/{projectUid}/jobs/{jobUid}/providers/suggest | Get suggested providers |

# **get_project_assignments**

<a id="get_project_assignments"></a>

> PageDtoProviderReference get_project_assignments(project_uid)

List project providers

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import provider_api
from phrasetms_client.model.page_dto_provider_reference import PageDtoProviderReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = provider_api.ProviderApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # List project providers
        api_response = api_instance.get_project_assignments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProviderApi->get_project_assignments: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'providerName': "providerName_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List project providers
        api_response = api_instance.get_project_assignments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProviderApi->get_project_assignments: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name         | Type               | Description | Notes    |
| ------------ | ------------------ | ----------- | -------- |
| providerName | ProviderNameSchema |             | optional |
| pageNumber   | PageNumberSchema   |             | optional |
| pageSize     | PageSizeSchema     |             | optional |

# ProviderNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

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

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                           | Description                                                 |
| ---- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                    | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_project_assignments.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_project_assignments.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_project_assignments.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_project_assignments.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_project_assignments.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_project_assignments.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_project_assignments.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_project_assignments.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_project_assignments.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_project_assignments.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_project_assignments.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_project_assignments.ApiResponseFor501) | Not implemented                                             |

#### get_project_assignments.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**PageDtoProviderReference**](../../models/PageDtoProviderReference.md) |             |

#### get_project_assignments.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_project_assignments.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_project_assignments.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_project_assignments.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_project_assignments.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_project_assignments.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_project_assignments.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_project_assignments.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_project_assignments.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_project_assignments.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_project_assignments.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_providers3**

<a id="list_providers3"></a>

> ProviderListDtoV2 list_providers3(project_uid)

Get suggested providers

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import provider_api
from phrasetms_client.model.provider_list_dto_v2 import ProviderListDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = provider_api.ProviderApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Get suggested providers
        api_response = api_instance.list_providers3(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProviderApi->list_providers3: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description          | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                      |
| accept_content_types | typing.Tuple[str]                                | default is ('_/_', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False     | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None      | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False     | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_providers3.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_providers3.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_providers3.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_providers3.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_providers3.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_providers3.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_providers3.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_providers3.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_providers3.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_providers3.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_providers3.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_providers3.ApiResponseFor501) | Not implemented                                             |

#### list_providers3.ApiResponseFor200

| Name     | Type                                     | Description              | Notes |
| -------- | ---------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                     | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBody, ] |                          |
| headers  | Unset                                    | headers were not defined |

# SchemaFor200ResponseBody

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**ProviderListDtoV2**](../../models/ProviderListDtoV2.md) |             |

#### list_providers3.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers3.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers3.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers3.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers3.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers3.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers3.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers3.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers3.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_providers4**

<a id="list_providers4"></a>

> ProviderListDtoV2 list_providers4(project_uidjob_uid)

Get suggested providers

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import provider_api
from phrasetms_client.model.provider_list_dto_v2 import ProviderListDtoV2
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = provider_api.ProviderApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get suggested providers
        api_response = api_instance.list_providers4(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProviderApi->list_providers4: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description          | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                      |
| accept_content_types | typing.Tuple[str]                                | default is ('_/_', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False     | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None      | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False     | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_providers4.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_providers4.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_providers4.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_providers4.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_providers4.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_providers4.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_providers4.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_providers4.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_providers4.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_providers4.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_providers4.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_providers4.ApiResponseFor501) | Not implemented                                             |

#### list_providers4.ApiResponseFor200

| Name     | Type                                     | Description              | Notes |
| -------- | ---------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                     | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBody, ] |                          |
| headers  | Unset                                    | headers were not defined |

# SchemaFor200ResponseBody

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**ProviderListDtoV2**](../../models/ProviderListDtoV2.md) |             |

#### list_providers4.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_providers4.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
