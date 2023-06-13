<a id="__pageTop"></a>

# phrasetms_client.apis.tags.glossary_api.GlossaryApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                      | HTTP request                                       | Description                  |
| ------------------------------------------- | -------------------------------------------------- | ---------------------------- |
| [**activate_glossary**](#activate_glossary) | **put** /api2/v1/glossaries/{glossaryUid}/activate | Activate/Deactivate glossary |
| [**create_glossary**](#create_glossary)     | **post** /api2/v1/glossaries                       | Create glossary              |
| [**delete_glossary**](#delete_glossary)     | **delete** /api2/v1/glossaries/{glossaryUid}       | Delete glossary              |
| [**get_glossary**](#get_glossary)           | **get** /api2/v1/glossaries/{glossaryUid}          | Get glossary                 |
| [**list_glossaries**](#list_glossaries)     | **get** /api2/v1/glossaries                        | List glossaries              |
| [**update_glossary**](#update_glossary)     | **put** /api2/v1/glossaries/{glossaryUid}          | Edit glossary                |

# **activate_glossary**

<a id="activate_glossary"></a>

> GlossaryDto activate_glossary(glossary_uid)

Activate/Deactivate glossary

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import glossary_api
from phrasetms_client.model.glossary_dto import GlossaryDto
from phrasetms_client.model.glossary_activation_dto import GlossaryActivationDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = glossary_api.GlossaryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'glossaryUid': "glossaryUid_example",
    }
    try:
        # Activate/Deactivate glossary
        api_response = api_instance.activate_glossary(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling GlossaryApi->activate_glossary: %s\n" % e)

    # example passing only optional values
    path_params = {
        'glossaryUid': "glossaryUid_example",
    }
    body = GlossaryActivationDto(
        active=True,
    )
    try:
        # Activate/Deactivate glossary
        api_response = api_instance.activate_glossary(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling GlossaryApi->activate_glossary: %s\n" % e)
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

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**GlossaryActivationDto**](../../models/GlossaryActivationDto.md) |             |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| glossaryUid | GlossaryUidSchema |             |

# GlossaryUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#activate_glossary.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#activate_glossary.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#activate_glossary.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#activate_glossary.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#activate_glossary.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#activate_glossary.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#activate_glossary.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#activate_glossary.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#activate_glossary.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#activate_glossary.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#activate_glossary.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#activate_glossary.ApiResponseFor501) | Not implemented                                             |

#### activate_glossary.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**GlossaryDto**](../../models/GlossaryDto.md) |             |

#### activate_glossary.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### activate_glossary.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### activate_glossary.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### activate_glossary.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### activate_glossary.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### activate_glossary.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### activate_glossary.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### activate_glossary.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### activate_glossary.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### activate_glossary.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### activate_glossary.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_glossary**

<a id="create_glossary"></a>

> GlossaryDto create_glossary()

Create glossary

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import glossary_api
from phrasetms_client.model.glossary_dto import GlossaryDto
from phrasetms_client.model.glossary_edit_dto import GlossaryEditDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = glossary_api.GlossaryApi(api_client)

    # example passing only optional values
    body = GlossaryEditDto(
        name="name_example",
        langs=[
            "langs_example"
        ],
        owner=IdReference(
            id="id_example",
        ),
    )
    try:
        # Create glossary
        api_response = api_instance.create_glossary(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling GlossaryApi->create_glossary: %s\n" % e)
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

| Type                                                   | Description | Notes |
| ------------------------------------------------------ | ----------- | ----- |
| [**GlossaryEditDto**](../../models/GlossaryEditDto.md) |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#create_glossary.ApiResponseFor200) | Created                                                     |
| 400  | [ApiResponseFor400](#create_glossary.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_glossary.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_glossary.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_glossary.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_glossary.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_glossary.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_glossary.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_glossary.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_glossary.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_glossary.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_glossary.ApiResponseFor501) | Not implemented                                             |

#### create_glossary.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**GlossaryDto**](../../models/GlossaryDto.md) |             |

#### create_glossary.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_glossary.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_glossary.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_glossary.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_glossary.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_glossary.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_glossary.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_glossary.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_glossary.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_glossary.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_glossary.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_glossary**

<a id="delete_glossary"></a>

> delete_glossary(glossary_uid)

Delete glossary

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import glossary_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = glossary_api.GlossaryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'glossaryUid': "glossaryUid_example",
    }
    query_params = {
    }
    try:
        # Delete glossary
        api_response = api_instance.delete_glossary(
            path_params=path_params,
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling GlossaryApi->delete_glossary: %s\n" % e)

    # example passing only optional values
    path_params = {
        'glossaryUid': "glossaryUid_example",
    }
    query_params = {
        'purge': False,
    }
    try:
        # Delete glossary
        api_response = api_instance.delete_glossary(
            path_params=path_params,
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling GlossaryApi->delete_glossary: %s\n" % e)
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

| Name  | Type        | Description | Notes    |
| ----- | ----------- | ----------- | -------- |
| purge | PurgeSchema |             | optional |

# PurgeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| glossaryUid | GlossaryUidSchema |             |

# GlossaryUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_glossary.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_glossary.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_glossary.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_glossary.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_glossary.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_glossary.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_glossary.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_glossary.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_glossary.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_glossary.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_glossary.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_glossary.ApiResponseFor501) | Not implemented                                             |

#### delete_glossary.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_glossary.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_glossary**

<a id="get_glossary"></a>

> GlossaryDto get_glossary(glossary_uid)

Get glossary

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import glossary_api
from phrasetms_client.model.glossary_dto import GlossaryDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = glossary_api.GlossaryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'glossaryUid': "glossaryUid_example",
    }
    try:
        # Get glossary
        api_response = api_instance.get_glossary(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling GlossaryApi->get_glossary: %s\n" % e)
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
| glossaryUid | GlossaryUidSchema |             |

# GlossaryUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_glossary.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_glossary.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_glossary.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_glossary.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_glossary.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_glossary.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_glossary.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_glossary.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_glossary.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_glossary.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_glossary.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_glossary.ApiResponseFor501) | Not implemented                                             |

#### get_glossary.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**GlossaryDto**](../../models/GlossaryDto.md) |             |

#### get_glossary.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_glossary.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_glossary.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_glossary.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_glossary.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_glossary.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_glossary.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_glossary.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_glossary.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_glossary.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_glossary.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_glossaries**

<a id="list_glossaries"></a>

> PageDtoGlossaryDto list_glossaries()

List glossaries

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import glossary_api
from phrasetms_client.model.page_dto_glossary_dto import PageDtoGlossaryDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = glossary_api.GlossaryApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'lang': [
        "lang_example"
    ],
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List glossaries
        api_response = api_instance.list_glossaries(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling GlossaryApi->list_glossaries: %s\n" % e)
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
| lang       | LangSchema       |             | optional |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# LangSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

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

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_glossaries.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_glossaries.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_glossaries.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_glossaries.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_glossaries.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_glossaries.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_glossaries.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_glossaries.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_glossaries.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_glossaries.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_glossaries.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_glossaries.ApiResponseFor501) | Not implemented                                             |

#### list_glossaries.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**PageDtoGlossaryDto**](../../models/PageDtoGlossaryDto.md) |             |

#### list_glossaries.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_glossaries.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_glossaries.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_glossaries.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_glossaries.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_glossaries.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_glossaries.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_glossaries.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_glossaries.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_glossaries.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_glossaries.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_glossary**

<a id="update_glossary"></a>

> GlossaryDto update_glossary(glossary_uid)

Edit glossary

Languages can only be added, their removal is not supported

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import glossary_api
from phrasetms_client.model.glossary_dto import GlossaryDto
from phrasetms_client.model.glossary_edit_dto import GlossaryEditDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = glossary_api.GlossaryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'glossaryUid': "glossaryUid_example",
    }
    try:
        # Edit glossary
        api_response = api_instance.update_glossary(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling GlossaryApi->update_glossary: %s\n" % e)

    # example passing only optional values
    path_params = {
        'glossaryUid': "glossaryUid_example",
    }
    body = GlossaryEditDto(
        name="name_example",
        langs=[
            "langs_example"
        ],
        owner=IdReference(
            id="id_example",
        ),
    )
    try:
        # Edit glossary
        api_response = api_instance.update_glossary(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling GlossaryApi->update_glossary: %s\n" % e)
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

| Type                                                   | Description | Notes |
| ------------------------------------------------------ | ----------- | ----- |
| [**GlossaryEditDto**](../../models/GlossaryEditDto.md) |             |

### path_params

#### RequestPathParams

| Name        | Type              | Description | Notes |
| ----------- | ----------------- | ----------- | ----- |
| glossaryUid | GlossaryUidSchema |             |

# GlossaryUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#update_glossary.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#update_glossary.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_glossary.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_glossary.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_glossary.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_glossary.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_glossary.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_glossary.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_glossary.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_glossary.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_glossary.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_glossary.ApiResponseFor501) | Not implemented                                             |

#### update_glossary.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**GlossaryDto**](../../models/GlossaryDto.md) |             |

#### update_glossary.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_glossary.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_glossary.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_glossary.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_glossary.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_glossary.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_glossary.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_glossary.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_glossary.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_glossary.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_glossary.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
