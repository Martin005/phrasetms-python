<a id="__pageTop"></a>

# phrasetms_client.apis.tags.project_reference_file_api.ProjectReferenceFileApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                                | HTTP request                                                        | Description                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------- |
| [**batch_delete_reference_files**](#batch_delete_reference_files)     | **delete** /api2/v1/projects/{projectUid}/references                | Delete project reference files (batch)   |
| [**batch_download_reference_files**](#batch_download_reference_files) | **post** /api2/v1/projects/{projectUid}/references/download         | Download project reference files (batch) |
| [**create_note_ref**](#create_note_ref)                               | **post** /api2/v1/projects/{projectUid}/references                  | Create project reference file            |
| [**download_reference**](#download_reference)                         | **get** /api2/v1/projects/{projectUid}/references/{referenceFileId} | Download project reference file          |
| [**list_reference_file_creators**](#list_reference_file_creators)     | **get** /api2/v1/projects/{projectUid}/references/creators          | List project reference file creators     |
| [**list_reference_files**](#list_reference_files)                     | **get** /api2/v1/projects/{projectUid}/references                   | List project reference files             |

# **batch_delete_reference_files**

<a id="batch_delete_reference_files"></a>

> batch_delete_reference_files(project_uid)

Delete project reference files (batch)

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import project_reference_file_api
from phrasetms_client.model.project_reference_files_request_dto import ProjectReferenceFilesRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_reference_file_api.ProjectReferenceFileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Delete project reference files (batch)
        api_response = api_instance.batch_delete_reference_files(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->batch_delete_reference_files: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = ProjectReferenceFilesRequestDto(
        reference_files=[
            IdReference(
                id="id_example",
            )
        ],
    )
    try:
        # Delete project reference files (batch)
        api_response = api_instance.batch_delete_reference_files(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->batch_delete_reference_files: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**ProjectReferenceFilesRequestDto**](../../models/ProjectReferenceFilesRequestDto.md) |             |

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

| Code | Class                                                                | Description                                                 |
| ---- | -------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                         | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#batch_delete_reference_files.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#batch_delete_reference_files.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#batch_delete_reference_files.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#batch_delete_reference_files.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#batch_delete_reference_files.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#batch_delete_reference_files.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#batch_delete_reference_files.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#batch_delete_reference_files.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#batch_delete_reference_files.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#batch_delete_reference_files.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#batch_delete_reference_files.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#batch_delete_reference_files.ApiResponseFor501) | Not implemented                                             |

#### batch_delete_reference_files.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_delete_reference_files.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **batch_download_reference_files**

<a id="batch_download_reference_files"></a>

> batch_download_reference_files(project_uid)

Download project reference files (batch)

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import project_reference_file_api
from phrasetms_client.model.project_reference_files_request_dto import ProjectReferenceFilesRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_reference_file_api.ProjectReferenceFileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    try:
        # Download project reference files (batch)
        api_response = api_instance.batch_download_reference_files(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->batch_download_reference_files: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    body = ProjectReferenceFilesRequestDto(
        reference_files=[
            IdReference(
                id="id_example",
            )
        ],
    )
    try:
        # Download project reference files (batch)
        api_response = api_instance.batch_download_reference_files(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->batch_download_reference_files: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                   | Description | Notes |
| -------------------------------------------------------------------------------------- | ----------- | ----- |
| [**ProjectReferenceFilesRequestDto**](../../models/ProjectReferenceFilesRequestDto.md) |             |

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

| Code | Class                                                                  | Description                                                 |
| ---- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#batch_download_reference_files.ApiResponseFor200) | application/octet-stream                                    |
| 400  | [ApiResponseFor400](#batch_download_reference_files.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#batch_download_reference_files.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#batch_download_reference_files.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#batch_download_reference_files.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#batch_download_reference_files.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#batch_download_reference_files.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#batch_download_reference_files.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#batch_download_reference_files.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#batch_download_reference_files.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#batch_download_reference_files.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#batch_download_reference_files.ApiResponseFor501) | Not implemented                                             |

#### batch_download_reference_files.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### batch_download_reference_files.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_note_ref**

<a id="create_note_ref"></a>

> ReferenceFileReference create_note_ref(project_uid)

Create project reference file

Accepts `application/octet-stream` or `application/json`.<br> - `application/json` - `note` field will be converted to .txt.<br> - `application/octet-stream` - `Content-Disposition` header is required

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import project_reference_file_api
from phrasetms_client.model.create_reference_file_note_dto import CreateReferenceFileNoteDto
from phrasetms_client.model.reference_file_reference import ReferenceFileReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_reference_file_api.ProjectReferenceFileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    header_params = {
    }
    try:
        # Create project reference file
        api_response = api_instance.create_note_ref(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->create_note_ref: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    header_params = {
        'Content-Disposition': "Content-Disposition_example",
        'X-Memsource-Note': "X-Memsource-Note_example",
    }
    body = CreateReferenceFileNoteDto(
        note="note_example",
    )
    try:
        # Create project reference file
        api_response = api_instance.create_note_ref(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->create_note_ref: %s\n" % e)
```

### Parameters

| Name                 | Type                                                                                                 | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset              |
| header_params        | RequestHeaderParams                                                                                  |                                         |
| path_params          | RequestPathParams                                                                                    |                                         |
| content_type         | str                                                                                                  | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                                                                    | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                                                                 | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                                                     | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                                                                 | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**CreateReferenceFileNoteDto**](../../models/CreateReferenceFileNoteDto.md) |             |

# SchemaForRequestBodyApplicationOctetStream

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**CreateReferenceFileNoteDto**](../../models/CreateReferenceFileNoteDto.md) |             |

### header_params

#### RequestHeaderParams

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Content-Disposition | ContentDispositionSchema |             | optional |
| X-Memsource-Note    | XMemsourceNoteSchema     |             | optional |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

# XMemsourceNoteSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

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
| 201  | [ApiResponseFor201](#create_note_ref.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_note_ref.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_note_ref.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_note_ref.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_note_ref.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_note_ref.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_note_ref.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_note_ref.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_note_ref.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_note_ref.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_note_ref.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_note_ref.ApiResponseFor501) | Not implemented                                             |

#### create_note_ref.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**ReferenceFileReference**](../../models/ReferenceFileReference.md) |             |

#### create_note_ref.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_note_ref.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_note_ref.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_note_ref.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_note_ref.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_note_ref.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_note_ref.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_note_ref.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_note_ref.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_note_ref.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_note_ref.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_reference**

<a id="download_reference"></a>

> download_reference(project_uidreference_file_id)

Download project reference file

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import project_reference_file_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_reference_file_api.ProjectReferenceFileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'referenceFileId': "referenceFileId_example",
    }
    try:
        # Download project reference file
        api_response = api_instance.download_reference(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->download_reference: %s\n" % e)
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

| Name            | Type                  | Description | Notes |
| --------------- | --------------------- | ----------- | ----- |
| projectUid      | ProjectUidSchema      |             |
| referenceFileId | ReferenceFileIdSchema |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ReferenceFileIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#download_reference.ApiResponseFor200) | application/octet-stream                                    |
| 400  | [ApiResponseFor400](#download_reference.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#download_reference.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#download_reference.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#download_reference.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#download_reference.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#download_reference.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#download_reference.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#download_reference.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#download_reference.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#download_reference.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#download_reference.ApiResponseFor501) | Not implemented                                             |

#### download_reference.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_reference.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_reference_file_creators**

<a id="list_reference_file_creators"></a>

> UserReferencesDto list_reference_file_creators(project_uid)

List project reference file creators

The result is not paged and returns up to 50 users. If the requested user is not included, the search can be narrowed down with the `userName` parameter.

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import project_reference_file_api
from phrasetms_client.model.user_references_dto import UserReferencesDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_reference_file_api.ProjectReferenceFileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # List project reference file creators
        api_response = api_instance.list_reference_file_creators(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->list_reference_file_creators: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'userName': "userName_example",
    }
    try:
        # List project reference file creators
        api_response = api_instance.list_reference_file_creators(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->list_reference_file_creators: %s\n" % e)
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

| Name     | Type           | Description | Notes    |
| -------- | -------------- | ----------- | -------- |
| userName | UserNameSchema |             | optional |

# UserNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

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

| Code | Class                                                                | Description                                                 |
| ---- | -------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_reference_file_creators.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_reference_file_creators.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_reference_file_creators.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_reference_file_creators.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_reference_file_creators.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_reference_file_creators.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_reference_file_creators.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_reference_file_creators.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_reference_file_creators.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_reference_file_creators.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_reference_file_creators.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_reference_file_creators.ApiResponseFor501) | Not implemented                                             |

#### list_reference_file_creators.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**UserReferencesDto**](../../models/UserReferencesDto.md) |             |

#### list_reference_file_creators.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_file_creators.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_file_creators.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_file_creators.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_file_creators.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_file_creators.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_file_creators.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_file_creators.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_file_creators.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_file_creators.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_file_creators.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_reference_files**

<a id="list_reference_files"></a>

> ReferenceFilePageDto list_reference_files(project_uid)

List project reference files

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import project_reference_file_api
from phrasetms_client.model.reference_file_page_dto import ReferenceFilePageDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_reference_file_api.ProjectReferenceFileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # List project reference files
        api_response = api_instance.list_reference_files(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->list_reference_files: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'filename': "filename_example",
        'dateCreatedSince': "dateCreatedSince_example",
        'createdBy': "createdBy_example",
        'pageNumber': 0,
        'pageSize': 50,
        'sort': "DATE_CREATED",
        'order': "DESC",
    }
    try:
        # List project reference files
        api_response = api_instance.list_reference_files(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ProjectReferenceFileApi->list_reference_files: %s\n" % e)
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

| Name             | Type                   | Description | Notes    |
| ---------------- | ---------------------- | ----------- | -------- |
| filename         | FilenameSchema         |             | optional |
| dateCreatedSince | DateCreatedSinceSchema |             | optional |
| createdBy        | CreatedBySchema        |             | optional |
| pageNumber       | PageNumberSchema       |             | optional |
| pageSize         | PageSizeSchema         |             | optional |
| sort             | SortSchema             |             | optional |
| order            | OrderSchema            |             | optional |

# FilenameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# DateCreatedSinceSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# CreatedBySchema

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

# SortSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                                                          |
| ---------- | ------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------ |
| str,       | str,          |             | must be one of ["FILENAME", "DATE_CREATED", "CREATED_BY", ] if omitted the server will use the default value of "DATE_CREATED" |

# OrderSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                       |
| ---------- | ------------- | ----------- | ------------------------------------------------------------------------------------------- |
| str,       | str,          |             | must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "DESC" |

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

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_reference_files.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_reference_files.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_reference_files.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_reference_files.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_reference_files.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_reference_files.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_reference_files.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_reference_files.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_reference_files.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_reference_files.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_reference_files.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_reference_files.ApiResponseFor501) | Not implemented                                             |

#### list_reference_files.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**ReferenceFilePageDto**](../../models/ReferenceFilePageDto.md) |             |

#### list_reference_files.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_files.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_files.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_files.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_files.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_files.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_files.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_files.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_files.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_files.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_reference_files.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
