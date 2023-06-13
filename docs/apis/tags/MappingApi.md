<a id="__pageTop"></a>

# phrasetms_client.apis.tags.mapping_api.MappingApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                            | HTTP request                         | Description                         |
| ------------------------------------------------- | ------------------------------------ | ----------------------------------- |
| [**get_mapping_for_task**](#get_mapping_for_task) | **get** /api2/v1/mappings/tasks/{id} | Returns mapping for taskId (mxliff) |

# **get_mapping_for_task**

<a id="get_mapping_for_task"></a>

> TaskMappingDto get_mapping_for_task(id)

Returns mapping for taskId (mxliff)

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import mapping_api
from phrasetms_client.model.task_mapping_dto import TaskMappingDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mapping_api.MappingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    try:
        # Returns mapping for taskId (mxliff)
        api_response = api_instance.get_mapping_for_task(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling MappingApi->get_mapping_for_task: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'workflowLevel': 1,
    }
    try:
        # Returns mapping for taskId (mxliff)
        api_response = api_instance.get_mapping_for_task(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling MappingApi->get_mapping_for_task: %s\n" % e)
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

| Name          | Type                | Description | Notes    |
| ------------- | ------------------- | ----------- | -------- |
| workflowLevel | WorkflowLevelSchema |             | optional |

# WorkflowLevelSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 1value must be a 32 bit integer |

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

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_mapping_for_task.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_mapping_for_task.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_mapping_for_task.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_mapping_for_task.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_mapping_for_task.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_mapping_for_task.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_mapping_for_task.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_mapping_for_task.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_mapping_for_task.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_mapping_for_task.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_mapping_for_task.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_mapping_for_task.ApiResponseFor501) | Not implemented                                             |

#### get_mapping_for_task.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                 | Description | Notes |
| ---------------------------------------------------- | ----------- | ----- |
| [**TaskMappingDto**](../../models/TaskMappingDto.md) |             |

#### get_mapping_for_task.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mapping_for_task.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mapping_for_task.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mapping_for_task.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mapping_for_task.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mapping_for_task.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mapping_for_task.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mapping_for_task.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mapping_for_task.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mapping_for_task.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mapping_for_task.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
