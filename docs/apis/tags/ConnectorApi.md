<a id="__pageTop"></a>

# phrasetms_client.apis.tags.connector_api.ConnectorApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                        | HTTP request                                                                           | Description                                            |
| --------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| [**edit_connector**](#edit_connector)         | **put** /api2/v1/connectors/{connectorId}                                              | Edit connector                                         |
| [**get_connector**](#get_connector)           | **get** /api2/v1/connectors/{connectorId}                                              | Get a connector                                        |
| [**get_connector_list**](#get_connector_list) | **get** /api2/v1/connectors                                                            | List connectors                                        |
| [**get_file**](#get_file)                     | **get** /api2/v1/connectors/{connectorId}/folders/{folder}/files/{file}                | Download file                                          |
| [**get_file1**](#get_file1)                   | **post** /api2/v2/connectors/{connectorId}/folders/{folder}/files/{file}               | Download file (async)                                  |
| [**get_folder**](#get_folder)                 | **get** /api2/v1/connectors/{connectorId}/folders/{folder}                             | List files in a subfolder                              |
| [**get_prepared_file**](#get_prepared_file)   | **get** /api2/v2/connectors/{connectorId}/folders/{folder}/files/{file}/tasks/{taskId} | Download prepared file                                 |
| [**get_root_folder**](#get_root_folder)       | **get** /api2/v1/connectors/{connectorId}/folders                                      | List files in root                                     |
| [**upload_file**](#upload_file)               | **post** /api2/v1/connectors/{connectorId}/folders/{folder}                            | Upload a file to a subfolder of the selected connector |
| [**upload_file1**](#upload_file1)             | **post** /api2/v2/connectors/{connectorId}/folders/{folder}/files/{fileName}/upload    | Upload file (async)                                    |

# **edit_connector**

<a id="edit_connector"></a>

> ConnectorCreateResponseDto edit_connector(connector_id)

Edit connector

Edit selected connector

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import connector_api
from phrasetms_client.model.connector_create_response_dto import ConnectorCreateResponseDto
from phrasetms_client.model.abstract_connector_dto import AbstractConnectorDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_api.ConnectorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectorId': "connectorId_example",
    }
    query_params = {
    }
    try:
        # Edit connector
        api_response = api_instance.edit_connector(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->edit_connector: %s\n" % e)

    # example passing only optional values
    path_params = {
        'connectorId': "connectorId_example",
    }
    query_params = {
        'connectionTest': True,
    }
    body = AbstractConnectorDto()
    try:
        # Edit connector
        api_response = api_instance.edit_connector(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->edit_connector: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| query_params         | RequestQueryParams                                       |                                         |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**AbstractConnectorDto**](../../models/AbstractConnectorDto.md) |             |

### query_params

#### RequestQueryParams

| Name           | Type                 | Description | Notes    |
| -------------- | -------------------- | ----------- | -------- |
| connectionTest | ConnectionTestSchema |             | optional |

# ConnectionTestSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| bool,      | BoolClass,    |             |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| connectorId | ConnectorIdSchema |             |

# ConnectorIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#edit_connector.ApiResponseFor200) | Edited                                                      |
| 400  | [ApiResponseFor400](#edit_connector.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#edit_connector.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#edit_connector.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#edit_connector.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#edit_connector.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#edit_connector.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#edit_connector.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#edit_connector.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#edit_connector.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#edit_connector.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#edit_connector.ApiResponseFor501) | Not implemented                                             |

#### edit_connector.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**ConnectorCreateResponseDto**](../../models/ConnectorCreateResponseDto.md) |             |

#### edit_connector.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_connector.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_connector.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_connector.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_connector.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_connector.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_connector.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_connector.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_connector.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_connector.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### edit_connector.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_connector**

<a id="get_connector"></a>

> ConnectorDto get_connector(connector_id)

Get a connector

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import connector_api
from phrasetms_client.model.connector_dto import ConnectorDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_api.ConnectorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectorId': "connectorId_example",
    }
    try:
        # Get a connector
        api_response = api_instance.get_connector(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->get_connector: %s\n" % e)
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

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| connectorId | ConnectorIdSchema |             |

# ConnectorIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                 | Description                                                 |
| ---- | ----------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization          | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_connector.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_connector.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_connector.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_connector.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_connector.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_connector.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_connector.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_connector.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_connector.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_connector.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_connector.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_connector.ApiResponseFor501) | Not implemented                                             |

#### get_connector.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                             | Description | Notes |
| ------------------------------------------------ | ----------- | ----- |
| [**ConnectorDto**](../../models/ConnectorDto.md) |             |

#### get_connector.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_connector_list**

<a id="get_connector_list"></a>

> ConnectorListDto get_connector_list()

List connectors

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import connector_api
from phrasetms_client.model.connector_list_dto import ConnectorListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_api.ConnectorApi(api_client)

    # example passing only optional values
    query_params = {
        'type': "type_example",
    }
    try:
        # List connectors
        api_response = api_instance.get_connector_list(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->get_connector_list: %s\n" % e)
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

| Name | Type       | Description | Notes    |
| ---- | ---------- | ----------- | -------- |
| type | TypeSchema |             | optional |

# TypeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_connector_list.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_connector_list.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_connector_list.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_connector_list.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_connector_list.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_connector_list.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_connector_list.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_connector_list.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_connector_list.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_connector_list.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_connector_list.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_connector_list.ApiResponseFor501) | Not implemented                                             |

#### get_connector_list.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**ConnectorListDto**](../../models/ConnectorListDto.md) |             |

#### get_connector_list.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector_list.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector_list.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector_list.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector_list.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector_list.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector_list.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector_list.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector_list.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector_list.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_connector_list.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_file**

<a id="get_file"></a>

> InputStreamLength get_file(connector_idfolderfile)

Download file

Download a file from a subfolder of the selected connector

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import connector_api
from phrasetms_client.model.input_stream_length import InputStreamLength
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_api.ConnectorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectorId': "connectorId_example",
        'folder': "folder_example",
        'file': "file_example",
    }
    try:
        # Download file
        api_response = api_instance.get_file(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->get_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                               | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                           |
| accept_content_types | typing.Tuple[str]                                | default is ('application/octet-stream', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                          | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                           | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                          | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| connectorId | ConnectorIdSchema |             |
| folder      | FolderSchema      |             |
| file        | FileSchema        |             |

# ConnectorIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FolderSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FileSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                            | Description                                                 |
| ---- | ------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization     | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_file.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_file.ApiResponseFor501) | Not implemented                                             |

#### get_file.ApiResponseFor200

| Name     | Type                                                           | Description              | Notes |
| -------- | -------------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                           | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |                          |
| headers  | Unset                                                          | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**InputStreamLength**](../../models/InputStreamLength.md) |             |

#### get_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_file1**

<a id="get_file1"></a>

> AsyncFileOpResponseDto get_file1(connector_idfolderfile)

Download file (async)

Create an asynchronous request to download a file from a (sub)folder of the selected connector. After a callback with successful response is received, prepared file can be downloaded by [Download prepared file](#operation/getPreparedFile) or [Create job from connector asynchronous download task](#operation/createJobFromAsyncDownloadTask).

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import connector_api
from phrasetms_client.model.get_file_request_params_dto import GetFileRequestParamsDto
from phrasetms_client.model.async_file_op_response_dto import AsyncFileOpResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_api.ConnectorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectorId': "connectorId_example",
        'folder': "folder_example",
        'file': "file_example",
    }
    try:
        # Download file (async)
        api_response = api_instance.get_file1(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->get_file1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'connectorId': "connectorId_example",
        'folder': "folder_example",
        'file': "file_example",
    }
    body = GetFileRequestParamsDto(
        source_lang="source_lang_example",
        target_lang="target_lang_example",
        callback_url="{\"callbackUrl\": \"https://www.yourdomain.com/callback_endpoint\"}",
    )
    try:
        # Download file (async)
        api_response = api_instance.get_file1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->get_file1: %s\n" % e)
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

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**GetFileRequestParamsDto**](../../models/GetFileRequestParamsDto.md) |             |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| connectorId | ConnectorIdSchema |             |
| folder      | FolderSchema      |             |
| file        | FileSchema        |             |

# ConnectorIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FolderSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FileSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                             | Description                                                 |
| ---- | ------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization      | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_file1.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_file1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_file1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_file1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_file1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_file1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_file1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_file1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_file1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_file1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_file1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_file1.ApiResponseFor501) | Not implemented                                             |

#### get_file1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**AsyncFileOpResponseDto**](../../models/AsyncFileOpResponseDto.md) |             |

#### get_file1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_file1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_folder**

<a id="get_folder"></a>

> FileListDto get_folder(connector_idfolder)

List files in a subfolder

List files in a subfolder of the selected connector

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import connector_api
from phrasetms_client.model.file_list_dto import FileListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_api.ConnectorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectorId': "connectorId_example",
        'folder': "folder_example",
    }
    query_params = {
    }
    try:
        # List files in a subfolder
        api_response = api_instance.get_folder(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->get_folder: %s\n" % e)

    # example passing only optional values
    path_params = {
        'connectorId': "connectorId_example",
        'folder': "folder_example",
    }
    query_params = {
        'projectUid': "projectUid_example",
        'fileType': "ALL",
        'sort': "NAME",
        'direction': "ASCENDING",
    }
    try:
        # List files in a subfolder
        api_response = api_instance.get_folder(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->get_folder: %s\n" % e)
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

| Name       | Type             | Description | Notes    |
| ---------- | ---------------- | ----------- | -------- |
| projectUid | ProjectUidSchema |             | optional |
| fileType   | FileTypeSchema   |             | optional |
| sort       | SortSchema       |             | optional |
| direction  | DirectionSchema  |             | optional |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FileTypeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| str,       | str,          |             | if omitted the server will use the default value of "ALL" |

# SortSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                      |
| ---------- | ------------- | ----------- | ---------------------------------------------------------- |
| str,       | str,          |             | if omitted the server will use the default value of "NAME" |

# DirectionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                           |
| ---------- | ------------- | ----------- | --------------------------------------------------------------- |
| str,       | str,          |             | if omitted the server will use the default value of "ASCENDING" |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| connectorId | ConnectorIdSchema |             |
| folder      | FolderSchema      |             |

# ConnectorIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FolderSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                              | Description                                                 |
| ---- | -------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization       | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_folder.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_folder.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_folder.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_folder.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_folder.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_folder.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_folder.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_folder.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_folder.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_folder.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_folder.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_folder.ApiResponseFor501) | Not implemented                                             |

#### get_folder.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**FileListDto**](../../models/FileListDto.md) |             |

#### get_folder.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_folder.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_folder.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_folder.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_folder.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_folder.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_folder.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_folder.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_folder.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_folder.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_folder.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_prepared_file**

<a id="get_prepared_file"></a>

> InputStreamLength get_prepared_file(connector_idfolderfiletask_id)

Download prepared file

Download the file by referencing successfully finished async download request [Connector - Download file (async)](#operation/getFile_1).

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import connector_api
from phrasetms_client.model.input_stream_length import InputStreamLength
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_api.ConnectorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectorId': "connectorId_example",
        'folder': "folder_example",
        'file': "file_example",
        'taskId': "taskId_example",
    }
    try:
        # Download prepared file
        api_response = api_instance.get_prepared_file(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->get_prepared_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                               | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                           |
| accept_content_types | typing.Tuple[str]                                | default is ('application/octet-stream', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                          | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                           | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                          | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| connectorId | ConnectorIdSchema |             |
| folder      | FolderSchema      |             |
| file        | FileSchema        |             |
| taskId      | TaskIdSchema      |             |

# ConnectorIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FolderSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FileSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# TaskIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_prepared_file.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_prepared_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_prepared_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_prepared_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_prepared_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_prepared_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_prepared_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_prepared_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_prepared_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_prepared_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_prepared_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_prepared_file.ApiResponseFor501) | Not implemented                                             |

#### get_prepared_file.ApiResponseFor200

| Name     | Type                                                           | Description              | Notes |
| -------- | -------------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                           | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |                          |
| headers  | Unset                                                          | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**InputStreamLength**](../../models/InputStreamLength.md) |             |

#### get_prepared_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prepared_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prepared_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prepared_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prepared_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prepared_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prepared_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prepared_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prepared_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prepared_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prepared_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_root_folder**

<a id="get_root_folder"></a>

> FileListDto get_root_folder(connector_id)

List files in root

List files in a root folder of the selected connector

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import connector_api
from phrasetms_client.model.file_list_dto import FileListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_api.ConnectorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectorId': "connectorId_example",
    }
    query_params = {
    }
    try:
        # List files in root
        api_response = api_instance.get_root_folder(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->get_root_folder: %s\n" % e)

    # example passing only optional values
    path_params = {
        'connectorId': "connectorId_example",
    }
    query_params = {
        'fileType': "ALL",
        'sort': "NAME",
        'direction': "ASCENDING",
    }
    try:
        # List files in root
        api_response = api_instance.get_root_folder(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->get_root_folder: %s\n" % e)
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

| Name      | Type            | Description | Notes    |
| --------- | --------------- | ----------- | -------- |
| fileType  | FileTypeSchema  |             | optional |
| sort      | SortSchema      |             | optional |
| direction | DirectionSchema |             | optional |

# FileTypeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| str,       | str,          |             | if omitted the server will use the default value of "ALL" |

# SortSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                      |
| ---------- | ------------- | ----------- | ---------------------------------------------------------- |
| str,       | str,          |             | if omitted the server will use the default value of "NAME" |

# DirectionSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                           |
| ---------- | ------------- | ----------- | --------------------------------------------------------------- |
| str,       | str,          |             | if omitted the server will use the default value of "ASCENDING" |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| connectorId | ConnectorIdSchema |             |

# ConnectorIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_root_folder.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_root_folder.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_root_folder.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_root_folder.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_root_folder.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_root_folder.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_root_folder.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_root_folder.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_root_folder.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_root_folder.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_root_folder.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_root_folder.ApiResponseFor501) | Not implemented                                             |

#### get_root_folder.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**FileListDto**](../../models/FileListDto.md) |             |

#### get_root_folder.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_root_folder.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_root_folder.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_root_folder.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_root_folder.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_root_folder.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_root_folder.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_root_folder.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_root_folder.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_root_folder.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_root_folder.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_file**

<a id="upload_file"></a>

> UploadResultDto upload_file(connector_idfoldercontent_type)

Upload a file to a subfolder of the selected connector

Upload a file to a subfolder of the selected connector

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import connector_api
from phrasetms_client.model.upload_result_dto import UploadResultDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_api.ConnectorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectorId': "connectorId_example",
        'folder': "folder_example",
    }
    header_params = {
        'Content-Type': "multipart/form-data",
    }
    try:
        # Upload a file to a subfolder of the selected connector
        api_response = api_instance.upload_file(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->upload_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'connectorId': "connectorId_example",
        'folder': "folder_example",
    }
    header_params = {
        'Content-Type': "multipart/form-data",
    }
    body = None
    try:
        # Upload a file to a subfolder of the selected connector
        api_response = api_instance.upload_file(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->upload_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                                       | Description                                | Notes                                                                                                                                                                                              |
| -------------------- | ---------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset                 |
| header_params        | RequestHeaderParams                                        |                                            |
| path_params          | RequestPathParams                                          |                                            |
| content_type         | str                                                        | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                          | default is ('application/json', )          | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                       | default is False                           | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]           | default is None                            | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                       | default is False                           | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info

| Input Type                                                                                                                                              | Accessed Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------- | ----- |
| dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **file**            | bytes, io.FileIO, io.BufferedReader,                                                                                                        | bytes, FileIO,                                                                          | Translated file to upload                                          |
| **sourceFileName**  | str,                                                                                                                                        | str,                                                                                    | Name or ID of the original file                                    | [optional] |
| **subfolderName**   | str,                                                                                                                                        | str,                                                                                    | Optional subfolder to upload the file to                           | [optional] |
| **mimeType**        | str,                                                                                                                                        | str,                                                                                    | Mime type of the file to upload                                    | [optional] |
| **commitMessage**   | str,                                                                                                                                        | str,                                                                                    | Commit message for upload to Git, etc.                             | [optional] |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

### header_params

#### RequestHeaderParams

| Name         | Type              | Description | Notes |
| ------------ | ----------------- | ----------- | ----- |
| Content-Type | ContentTypeSchema |             |

# ContentTypeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                    |
| ---------- | ------------- | ----------- | ---------------------------------------- |
| str,       | str,          |             | must be one of ["multipart/form-data", ] |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| connectorId | ConnectorIdSchema |             |
| folder      | FolderSchema      |             |

# ConnectorIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FolderSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                               | Description                                                 |
| ---- | --------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization        | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#upload_file.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#upload_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#upload_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#upload_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#upload_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#upload_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#upload_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#upload_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#upload_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#upload_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#upload_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#upload_file.ApiResponseFor501) | Not implemented                                             |

#### upload_file.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                   | Description | Notes |
| ------------------------------------------------------ | ----------- | ----- |
| [**UploadResultDto**](../../models/UploadResultDto.md) |             |

#### upload_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_file1**

<a id="upload_file1"></a>

> AsyncFileOpResponseDto upload_file1(connector_idfolderfile_namememsourcecontent_type)

Upload file (async)

Upload a file to a subfolder of the selected connector

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import connector_api
from phrasetms_client.model.async_file_op_response_dto import AsyncFileOpResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_api.ConnectorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'connectorId': "connectorId_example",
        'folder': "folder_example",
        'fileName': "fileName_example",
    }
    query_params = {
    }
    header_params = {
        'Memsource': "{\"subfolderName\":\"myFolder\",\"commitMessage\":\"add translation\",\"callbackUrl\":\"https://webhook.site/83b222a1-5cf2-48ec-b8b9-7f79bb2a25e4\"}",
        'Content-Type': "multipart/form-data",
    }
    try:
        # Upload file (async)
        api_response = api_instance.upload_file1(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->upload_file1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'connectorId': "connectorId_example",
        'folder': "folder_example",
        'fileName': "fileName_example",
    }
    query_params = {
        'mimeType': "mimeType_example",
    }
    header_params = {
        'Memsource': "{\"subfolderName\":\"myFolder\",\"commitMessage\":\"add translation\",\"callbackUrl\":\"https://webhook.site/83b222a1-5cf2-48ec-b8b9-7f79bb2a25e4\"}",
        'Content-Type': "multipart/form-data",
    }
    body = None
    try:
        # Upload file (async)
        api_response = api_instance.upload_file1(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConnectorApi->upload_file1: %s\n" % e)
```

### Parameters

| Name                 | Type                                                       | Description                                | Notes                                                                                                                                                                                              |
| -------------------- | ---------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset                 |
| query_params         | RequestQueryParams                                         |                                            |
| header_params        | RequestHeaderParams                                        |                                            |
| path_params          | RequestPathParams                                          |                                            |
| content_type         | str                                                        | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                          | default is ('application/json', )          | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                       | default is False                           | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]           | default is None                            | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                       | default is False                           | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info

| Input Type                                                                                                                                              | Accessed Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------- | ----- |
| dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |             |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **file**            | bytes, io.FileIO, io.BufferedReader,                                                                                                        | bytes, FileIO,                                                                          | Translated file to upload                                          |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

### query_params

#### RequestQueryParams

| Name     | Type           | Description | Notes    |
| -------- | -------------- | ----------- | -------- |
| mimeType | MimeTypeSchema |             | optional |

# MimeTypeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### header_params

#### RequestHeaderParams

| Name         | Type              | Description | Notes |
| ------------ | ----------------- | ----------- | ----- |
| Memsource    | MemsourceSchema   |             |
| Content-Type | ContentTypeSchema |             |

# MemsourceSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ContentTypeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                    |
| ---------- | ------------- | ----------- | ---------------------------------------- |
| str,       | str,          |             | must be one of ["multipart/form-data", ] |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| connectorId | ConnectorIdSchema |             |
| folder      | FolderSchema      |             |
| fileName    | FileNameSchema    |             |

# ConnectorIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FolderSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# FileNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#upload_file1.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#upload_file1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#upload_file1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#upload_file1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#upload_file1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#upload_file1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#upload_file1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#upload_file1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#upload_file1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#upload_file1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#upload_file1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#upload_file1.ApiResponseFor501) | Not implemented                                             |

#### upload_file1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**AsyncFileOpResponseDto**](../../models/AsyncFileOpResponseDto.md) |             |

#### upload_file1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_file1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
