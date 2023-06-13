<a id="__pageTop"></a>

# phrasetms_client.apis.tags.sub_domain_api.SubDomainApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                      | HTTP request                                  | Description      |
| ------------------------------------------- | --------------------------------------------- | ---------------- |
| [**create_sub_domain**](#create_sub_domain) | **post** /api2/v1/subDomains                  | Create subdomain |
| [**delete_sub_domain**](#delete_sub_domain) | **delete** /api2/v1/subDomains/{subDomainUid} | Delete subdomain |
| [**get_sub_domain**](#get_sub_domain)       | **get** /api2/v1/subDomains/{subDomainUid}    | Get subdomain    |
| [**list_sub_domains**](#list_sub_domains)   | **get** /api2/v1/subDomains                   | List subdomains  |
| [**update_sub_domain**](#update_sub_domain) | **put** /api2/v1/subDomains/{subDomainUid}    | Edit subdomain   |

# **create_sub_domain**

<a id="create_sub_domain"></a>

> SubDomainDto create_sub_domain()

Create subdomain

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import sub_domain_api
from phrasetms_client.model.sub_domain_edit_dto import SubDomainEditDto
from phrasetms_client.model.sub_domain_dto import SubDomainDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sub_domain_api.SubDomainApi(api_client)

    # example passing only optional values
    body = SubDomainEditDto(
        name="name_example",
    )
    try:
        # Create subdomain
        api_response = api_instance.create_sub_domain(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SubDomainApi->create_sub_domain: %s\n" % e)
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
| [**SubDomainEditDto**](../../models/SubDomainEditDto.md) |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_sub_domain.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_sub_domain.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_sub_domain.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_sub_domain.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_sub_domain.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_sub_domain.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_sub_domain.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_sub_domain.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_sub_domain.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_sub_domain.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_sub_domain.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_sub_domain.ApiResponseFor501) | Not implemented                                             |

#### create_sub_domain.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                             | Description | Notes |
| ------------------------------------------------ | ----------- | ----- |
| [**SubDomainDto**](../../models/SubDomainDto.md) |             |

#### create_sub_domain.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_sub_domain.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_sub_domain.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_sub_domain.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_sub_domain.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_sub_domain.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_sub_domain.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_sub_domain.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_sub_domain.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_sub_domain.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_sub_domain.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_sub_domain**

<a id="delete_sub_domain"></a>

> delete_sub_domain(sub_domain_uid)

Delete subdomain

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import sub_domain_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sub_domain_api.SubDomainApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subDomainUid': "subDomainUid_example",
    }
    try:
        # Delete subdomain
        api_response = api_instance.delete_sub_domain(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling SubDomainApi->delete_sub_domain: %s\n" % e)
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

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| subDomainUid | SubDomainUidSchema |             |

# SubDomainUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_sub_domain.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_sub_domain.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_sub_domain.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_sub_domain.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_sub_domain.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_sub_domain.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_sub_domain.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_sub_domain.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_sub_domain.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_sub_domain.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_sub_domain.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_sub_domain.ApiResponseFor501) | Not implemented                                             |

#### delete_sub_domain.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_sub_domain.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sub_domain**

<a id="get_sub_domain"></a>

> SubDomainDto get_sub_domain(sub_domain_uid)

Get subdomain

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import sub_domain_api
from phrasetms_client.model.sub_domain_dto import SubDomainDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sub_domain_api.SubDomainApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subDomainUid': "subDomainUid_example",
    }
    try:
        # Get subdomain
        api_response = api_instance.get_sub_domain(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SubDomainApi->get_sub_domain: %s\n" % e)
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

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| subDomainUid | SubDomainUidSchema |             |

# SubDomainUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_sub_domain.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_sub_domain.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_sub_domain.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_sub_domain.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_sub_domain.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_sub_domain.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_sub_domain.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_sub_domain.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_sub_domain.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_sub_domain.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_sub_domain.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_sub_domain.ApiResponseFor501) | Not implemented                                             |

#### get_sub_domain.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                             | Description | Notes |
| ------------------------------------------------ | ----------- | ----- |
| [**SubDomainDto**](../../models/SubDomainDto.md) |             |

#### get_sub_domain.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_sub_domain.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_sub_domain.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_sub_domain.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_sub_domain.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_sub_domain.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_sub_domain.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_sub_domain.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_sub_domain.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_sub_domain.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_sub_domain.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_sub_domains**

<a id="list_sub_domains"></a>

> PageDtoSubDomainDto list_sub_domains()

List subdomains

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import sub_domain_api
from phrasetms_client.model.page_dto_sub_domain_dto import PageDtoSubDomainDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sub_domain_api.SubDomainApi(api_client)

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
        # List subdomains
        api_response = api_instance.list_sub_domains(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SubDomainApi->list_sub_domains: %s\n" % e)
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

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_sub_domains.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_sub_domains.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_sub_domains.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_sub_domains.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_sub_domains.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_sub_domains.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_sub_domains.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_sub_domains.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_sub_domains.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_sub_domains.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_sub_domains.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_sub_domains.ApiResponseFor501) | Not implemented                                             |

#### list_sub_domains.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoSubDomainDto**](../../models/PageDtoSubDomainDto.md) |             |

#### list_sub_domains.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_sub_domains.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_sub_domains.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_sub_domains.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_sub_domains.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_sub_domains.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_sub_domains.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_sub_domains.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_sub_domains.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_sub_domains.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_sub_domains.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_sub_domain**

<a id="update_sub_domain"></a>

> SubDomainDto update_sub_domain(sub_domain_uid)

Edit subdomain

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import sub_domain_api
from phrasetms_client.model.sub_domain_edit_dto import SubDomainEditDto
from phrasetms_client.model.sub_domain_dto import SubDomainDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sub_domain_api.SubDomainApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'subDomainUid': "subDomainUid_example",
    }
    try:
        # Edit subdomain
        api_response = api_instance.update_sub_domain(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SubDomainApi->update_sub_domain: %s\n" % e)

    # example passing only optional values
    path_params = {
        'subDomainUid': "subDomainUid_example",
    }
    body = SubDomainEditDto(
        name="name_example",
    )
    try:
        # Edit subdomain
        api_response = api_instance.update_sub_domain(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SubDomainApi->update_sub_domain: %s\n" % e)
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
| [**SubDomainEditDto**](../../models/SubDomainEditDto.md) |             |

### path_params

#### RequestPathParams

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| subDomainUid | SubDomainUidSchema |             |

# SubDomainUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#update_sub_domain.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#update_sub_domain.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_sub_domain.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_sub_domain.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_sub_domain.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_sub_domain.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_sub_domain.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_sub_domain.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_sub_domain.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_sub_domain.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_sub_domain.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_sub_domain.ApiResponseFor501) | Not implemented                                             |

#### update_sub_domain.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                             | Description | Notes |
| ------------------------------------------------ | ----------- | ----- |
| [**SubDomainDto**](../../models/SubDomainDto.md) |             |

#### update_sub_domain.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_sub_domain.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_sub_domain.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_sub_domain.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_sub_domain.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_sub_domain.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_sub_domain.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_sub_domain.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_sub_domain.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_sub_domain.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_sub_domain.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
