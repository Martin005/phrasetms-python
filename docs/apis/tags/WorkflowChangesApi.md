<a id="__pageTop"></a>

# phrasetms_client.apis.tags.workflow_changes_api.WorkflowChangesApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                      | HTTP request                           | Description                      |
| ----------------------------------------------------------- | -------------------------------------- | -------------------------------- |
| [**download_workflow_changes**](#download_workflow_changes) | **post** /api2/v2/jobs/workflowChanges | Download workflow changes report |

# **download_workflow_changes**

<a id="download_workflow_changes"></a>

> Response download_workflow_changes()

Download workflow changes report

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import workflow_changes_api
from phrasetms_client.model.workflow_changes_dto import WorkflowChangesDto
from phrasetms_client.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_changes_api.WorkflowChangesApi(api_client)

    # example passing only optional values
    body = WorkflowChangesDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
    )
    try:
        # Download workflow changes report
        api_response = api_instance.download_workflow_changes(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling WorkflowChangesApi->download_workflow_changes: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBody, Unset]        | optional, default is unset |
| content_type         | str                                              | optional, default is '_/_' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                | default is ('text/html', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False           | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None            | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False           | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBody

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**WorkflowChangesDto**](../../models/WorkflowChangesDto.md) |             |

### Return Types, Responses

| Code | Class                                                             | Description                                                 |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#download_workflow_changes.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#download_workflow_changes.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#download_workflow_changes.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#download_workflow_changes.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#download_workflow_changes.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#download_workflow_changes.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#download_workflow_changes.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#download_workflow_changes.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#download_workflow_changes.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#download_workflow_changes.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#download_workflow_changes.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#download_workflow_changes.ApiResponseFor501) | Not implemented                                             |

#### download_workflow_changes.ApiResponseFor200

| Name     | Type                                             | Description              | Notes |
| -------- | ------------------------------------------------ | ------------------------ | ----- |
| response | urllib3.HTTPResponse                             | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyTextHtml, ] |                          |
| headers  | Unset                                            | headers were not defined |

# SchemaFor200ResponseBodyTextHtml

| Type                                     | Description | Notes |
| ---------------------------------------- | ----------- | ----- |
| [**Response**](../../models/Response.md) |             |

#### download_workflow_changes.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_workflow_changes.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_workflow_changes.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_workflow_changes.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_workflow_changes.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_workflow_changes.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_workflow_changes.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_workflow_changes.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_workflow_changes.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_workflow_changes.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_workflow_changes.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
