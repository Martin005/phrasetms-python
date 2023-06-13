<a id="__pageTop"></a>

# phrasetms_client.apis.tags.additional_workflow_step_api.AdditionalWorkflowStepApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                  | HTTP request                                     | Description                     |
| --------------------------------------- | ------------------------------------------------ | ------------------------------- |
| [**create_awf_step**](#create_awf_step) | **post** /api2/v1/additionalWorkflowSteps        | Create additional workflow step |
| [**delete_awf_step**](#delete_awf_step) | **delete** /api2/v1/additionalWorkflowSteps/{id} | Delete additional workflow step |
| [**list_awf_steps**](#list_awf_steps)   | **get** /api2/v1/additionalWorkflowSteps         | List additional workflow steps  |

# **create_awf_step**

<a id="create_awf_step"></a>

> AdditionalWorkflowStepDto create_awf_step()

Create additional workflow step

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import additional_workflow_step_api
from phrasetms_client.model.additional_workflow_step_dto import AdditionalWorkflowStepDto
from phrasetms_client.model.additional_workflow_step_request_dto import AdditionalWorkflowStepRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = additional_workflow_step_api.AdditionalWorkflowStepApi(api_client)

    # example passing only optional values
    body = AdditionalWorkflowStepRequestDto(
        name="name_example",
    )
    try:
        # Create additional workflow step
        api_response = api_instance.create_awf_step(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AdditionalWorkflowStepApi->create_awf_step: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBody, Unset]        | optional, default is unset |
| content_type         | str                                              | optional, default is '_/_' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                | default is ('_/_', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False           | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None            | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False           | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBody

| Type                                                                                     | Description | Notes |
| ---------------------------------------------------------------------------------------- | ----------- | ----- |
| [**AdditionalWorkflowStepRequestDto**](../../models/AdditionalWorkflowStepRequestDto.md) |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_awf_step.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_awf_step.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_awf_step.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_awf_step.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_awf_step.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_awf_step.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_awf_step.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_awf_step.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_awf_step.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_awf_step.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_awf_step.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_awf_step.ApiResponseFor501) | Not implemented                                             |

#### create_awf_step.ApiResponseFor201

| Name     | Type                                     | Description              | Notes |
| -------- | ---------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                     | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBody, ] |                          |
| headers  | Unset                                    | headers were not defined |

# SchemaFor201ResponseBody

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**AdditionalWorkflowStepDto**](../../models/AdditionalWorkflowStepDto.md) |             |

#### create_awf_step.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_awf_step.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_awf_step.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_awf_step.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_awf_step.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_awf_step.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_awf_step.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_awf_step.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_awf_step.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_awf_step.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_awf_step.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_awf_step**

<a id="delete_awf_step"></a>

> delete_awf_step(id)

Delete additional workflow step

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import additional_workflow_step_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = additional_workflow_step_api.AdditionalWorkflowStepApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Delete additional workflow step
        api_response = api_instance.delete_awf_step(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling AdditionalWorkflowStepApi->delete_awf_step: %s\n" % e)
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

| Name | Type     | Description | Notes |
| ---- | -------- | ----------- | ----- |
| id   | IdSchema |             |

# IdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_awf_step.ApiResponseFor204) | Deleted                                                     |
| 400  | [ApiResponseFor400](#delete_awf_step.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_awf_step.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_awf_step.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_awf_step.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_awf_step.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_awf_step.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_awf_step.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_awf_step.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_awf_step.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_awf_step.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_awf_step.ApiResponseFor501) | Not implemented                                             |

#### delete_awf_step.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_awf_step.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_awf_steps**

<a id="list_awf_steps"></a>

> PageDtoAdditionalWorkflowStepDto list_awf_steps()

List additional workflow steps

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import additional_workflow_step_api
from phrasetms_client.model.page_dto_additional_workflow_step_dto import PageDtoAdditionalWorkflowStepDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = additional_workflow_step_api.AdditionalWorkflowStepApi(api_client)

    # example passing only optional values
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
        'name': "name_example",
    }
    try:
        # List additional workflow steps
        api_response = api_instance.list_awf_steps(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AdditionalWorkflowStepApi->list_awf_steps: %s\n" % e)
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

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_awf_steps.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_awf_steps.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_awf_steps.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_awf_steps.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_awf_steps.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_awf_steps.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_awf_steps.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_awf_steps.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_awf_steps.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_awf_steps.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_awf_steps.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_awf_steps.ApiResponseFor501) | Not implemented                                             |

#### list_awf_steps.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                                     | Description | Notes |
| ---------------------------------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoAdditionalWorkflowStepDto**](../../models/PageDtoAdditionalWorkflowStepDto.md) |             |

#### list_awf_steps.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_awf_steps.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_awf_steps.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_awf_steps.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_awf_steps.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_awf_steps.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_awf_steps.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_awf_steps.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_awf_steps.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_awf_steps.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_awf_steps.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
