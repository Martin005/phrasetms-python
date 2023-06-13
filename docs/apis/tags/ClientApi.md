<a id="__pageTop"></a>

# phrasetms_client.apis.tags.client_api.ClientApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                              | HTTP request                            | Description   |
| ----------------------------------- | --------------------------------------- | ------------- |
| [**create_client**](#create_client) | **post** /api2/v1/clients               | Create client |
| [**delete_client**](#delete_client) | **delete** /api2/v1/clients/{clientUid} | Delete client |
| [**get_client**](#get_client)       | **get** /api2/v1/clients/{clientUid}    | Get client    |
| [**list_clients**](#list_clients)   | **get** /api2/v1/clients                | List clients  |
| [**update_client**](#update_client) | **put** /api2/v1/clients/{clientUid}    | Edit client   |

# **create_client**

<a id="create_client"></a>

> ClientDto create_client(body)

Create client

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import client_api
from phrasetms_client.model.client_edit_dto import ClientEditDto
from phrasetms_client.model.client_dto import ClientDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client_api.ClientApi(api_client)

    # example passing only required values which don't have defaults set
    body = ClientEditDto(
        name="name_example",
        external_id="external_id_example",
        note="note_example",
        display_note_in_project=True,
        price_list=IdReference(
            id="id_example",
        ),
,
    )
    try:
        # Create client
        api_response = api_instance.create_client(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ClientApi->create_client: %s\n" % e)
```

### Parameters

| Name                 | Type                                              | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson] | required                                |
| content_type         | str                                               | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                 | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                              | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]  | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                              | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                               | Description | Notes |
| -------------------------------------------------- | ----------- | ----- |
| [**ClientEditDto**](../../models/ClientEditDto.md) |             |

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_client.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_client.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_client.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_client.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_client.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_client.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_client.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_client.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_client.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_client.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_client.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_client.ApiResponseFor501) | Not implemented                                             |

#### create_client.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                       | Description | Notes |
| ------------------------------------------ | ----------- | ----- |
| [**ClientDto**](../../models/ClientDto.md) |             |

#### create_client.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_client.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_client.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_client.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_client.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_client.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_client.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_client.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_client.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_client.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_client.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_client**

<a id="delete_client"></a>

> delete_client(client_uid)

Delete client

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import client_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client_api.ClientApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clientUid': "clientUid_example",
    }
    try:
        # Delete client
        api_response = api_instance.delete_client(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ClientApi->delete_client: %s\n" % e)
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

| Name      | Type            | Description | Notes |
| --------- | --------------- | ----------- | ----- |
| clientUid | ClientUidSchema |             |

# ClientUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_client.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_client.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_client.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_client.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_client.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_client.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_client.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_client.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_client.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_client.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_client.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_client.ApiResponseFor501) | Not implemented                                             |

#### delete_client.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_client.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_client**

<a id="get_client"></a>

> ClientDto get_client(client_uid)

Get client

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import client_api
from phrasetms_client.model.client_dto import ClientDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client_api.ClientApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clientUid': "clientUid_example",
    }
    try:
        # Get client
        api_response = api_instance.get_client(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ClientApi->get_client: %s\n" % e)
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

| Name      | Type            | Description | Notes |
| --------- | --------------- | ----------- | ----- |
| clientUid | ClientUidSchema |             |

# ClientUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                              | Description                                                 |
| ---- | -------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization       | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_client.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_client.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_client.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_client.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_client.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_client.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_client.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_client.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_client.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_client.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_client.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_client.ApiResponseFor501) | Not implemented                                             |

#### get_client.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                       | Description | Notes |
| ------------------------------------------ | ----------- | ----- |
| [**ClientDto**](../../models/ClientDto.md) |             |

#### get_client.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_client.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_client.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_client.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_client.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_client.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_client.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_client.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_client.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_client.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_client.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_clients**

<a id="list_clients"></a>

> PageDtoClientDto list_clients()

List clients

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import client_api
from phrasetms_client.model.page_dto_client_dto import PageDtoClientDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client_api.ClientApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'createdBy': "createdBy_example",
        'sort': "NAME",
        'order': "ASC",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List clients
        api_response = api_instance.list_clients(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ClientApi->list_clients: %s\n" % e)
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
| name       | NameSchema       |             | optional |
| createdBy  | CreatedBySchema  |             | optional |
| sort       | SortSchema       |             | optional |
| order      | OrderSchema      |             | optional |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# CreatedBySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# SortSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                                |
| ---------- | ------------- | ----------- | ---------------------------------------------------------------------------------------------------- |
| str,       | str,          |             | must be one of ["NAME", "DATE_CREATED", ] if omitted the server will use the default value of "NAME" |

# OrderSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                      |
| ---------- | ------------- | ----------- | ------------------------------------------------------------------------------------------ |
| str,       | str,          |             | must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "ASC" |

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

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_clients.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_clients.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_clients.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_clients.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_clients.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_clients.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_clients.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_clients.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_clients.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_clients.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_clients.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_clients.ApiResponseFor501) | Not implemented                                             |

#### list_clients.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**PageDtoClientDto**](../../models/PageDtoClientDto.md) |             |

#### list_clients.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_clients.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_clients.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_clients.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_clients.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_clients.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_clients.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_clients.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_clients.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_clients.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_clients.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_client**

<a id="update_client"></a>

> ClientDto update_client(client_uidbody)

Edit client

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import client_api
from phrasetms_client.model.client_edit_dto import ClientEditDto
from phrasetms_client.model.client_dto import ClientDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client_api.ClientApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clientUid': "clientUid_example",
    }
    body = ClientEditDto(
        name="name_example",
        external_id="external_id_example",
        note="note_example",
        display_note_in_project=True,
        price_list=IdReference(
            id="id_example",
        ),
,
    )
    try:
        # Edit client
        api_response = api_instance.update_client(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ClientApi->update_client: %s\n" % e)
```

### Parameters

| Name                 | Type                                              | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson] | required                                |
| path_params          | RequestPathParams                                 |                                         |
| content_type         | str                                               | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                 | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                              | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]  | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                              | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                               | Description | Notes |
| -------------------------------------------------- | ----------- | ----- |
| [**ClientEditDto**](../../models/ClientEditDto.md) |             |

### path_params

#### RequestPathParams

| Name      | Type            | Description | Notes |
| --------- | --------------- | ----------- | ----- |
| clientUid | ClientUidSchema |             |

# ClientUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#update_client.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#update_client.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_client.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_client.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_client.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_client.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_client.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_client.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_client.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_client.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_client.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_client.ApiResponseFor501) | Not implemented                                             |

#### update_client.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                       | Description | Notes |
| ------------------------------------------ | ----------- | ----- |
| [**ClientDto**](../../models/ClientDto.md) |             |

#### update_client.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_client.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_client.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_client.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_client.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_client.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_client.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_client.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_client.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_client.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_client.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
