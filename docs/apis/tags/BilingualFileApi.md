<a id="__pageTop"></a>

# phrasetms_client.apis.tags.bilingual_file_api.BilingualFileApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                | HTTP request                                               | Description             |
| ----------------------------------------------------- | ---------------------------------------------------------- | ----------------------- |
| [**compare_bilingual_file**](#compare_bilingual_file) | **post** /api2/v1/bilingualFiles/compare                   | Compare bilingual file  |
| [**convert_bilingual_file**](#convert_bilingual_file) | **post** /api2/v1/bilingualFiles/convert                   | Convert bilingual file  |
| [**get_bilingual_file**](#get_bilingual_file)         | **post** /api2/v1/projects/{projectUid}/jobs/bilingualFile | Download bilingual file |
| [**get_preview_file**](#get_preview_file)             | **post** /api2/v1/bilingualFiles/preview                   | Download preview        |
| [**upload_bilingual_file**](#upload_bilingual_file)   | **put** /api2/v1/bilingualFiles                            | Upload bilingual file   |

# **compare_bilingual_file**

<a id="compare_bilingual_file"></a>

> ComparedSegmentsDto compare_bilingual_file()

Compare bilingual file

Compares bilingual file to job state. Returns list of compared segments.

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import bilingual_file_api
from phrasetms_client.model.compared_segments_dto import ComparedSegmentsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bilingual_file_api.BilingualFileApi(api_client)

    # example passing only optional values
    query_params = {
        'workflowLevel': 1,
    }
    body = dict()
    try:
        # Compare bilingual file
        api_response = api_instance.compare_bilingual_file(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling BilingualFileApi->compare_bilingual_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                                            | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset                      |
| query_params         | RequestQueryParams                                              |                                                 |
| content_type         | str                                                             | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                               | default is ('application/json', )               | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                            | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                            | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

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

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#compare_bilingual_file.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#compare_bilingual_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#compare_bilingual_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#compare_bilingual_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#compare_bilingual_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#compare_bilingual_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#compare_bilingual_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#compare_bilingual_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#compare_bilingual_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#compare_bilingual_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#compare_bilingual_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#compare_bilingual_file.ApiResponseFor501) | Not implemented                                             |

#### compare_bilingual_file.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**ComparedSegmentsDto**](../../models/ComparedSegmentsDto.md) |             |

#### compare_bilingual_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_bilingual_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_bilingual_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_bilingual_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_bilingual_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_bilingual_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_bilingual_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_bilingual_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_bilingual_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_bilingual_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### compare_bilingual_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **convert_bilingual_file**

<a id="convert_bilingual_file"></a>

> convert_bilingual_file(\_fromto)

Convert bilingual file

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import bilingual_file_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bilingual_file_api.BilingualFileApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'from': "MXLF",
        'to': "MXLF",
    }
    try:
        # Convert bilingual file
        api_response = api_instance.convert_bilingual_file(
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling BilingualFileApi->convert_bilingual_file: %s\n" % e)

    # example passing only optional values
    query_params = {
        'from': "MXLF",
        'to': "MXLF",
    }
    body = dict()
    try:
        # Convert bilingual file
        api_response = api_instance.convert_bilingual_file(
            query_params=query_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling BilingualFileApi->convert_bilingual_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                                            | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset                      |
| query_params         | RequestQueryParams                                              |                                                 |
| content_type         | str                                                             | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                            | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                            | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### query_params

#### RequestQueryParams

| Name | Type            | Description | Notes |
| ---- | --------------- | ----------- | ----- |
| from | ModelFromSchema |             |
| to   | ToSchema        |             |

# ModelFromSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                             |
| ---------- | ------------- | ----------- | --------------------------------- |
| str,       | str,          |             | must be one of ["MXLF", "DOCX", ] |

# ToSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                             |
| ---------- | ------------- | ----------- | --------------------------------- |
| str,       | str,          |             | must be one of ["MXLF", "DOCX", ] |

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#convert_bilingual_file.ApiResponseFor200) | application/octet-stream                                    |
| 400  | [ApiResponseFor400](#convert_bilingual_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#convert_bilingual_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#convert_bilingual_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#convert_bilingual_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#convert_bilingual_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#convert_bilingual_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#convert_bilingual_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#convert_bilingual_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#convert_bilingual_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#convert_bilingual_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#convert_bilingual_file.ApiResponseFor501) | Not implemented                                             |

#### convert_bilingual_file.ApiResponseFor200

| Name     | Type                  | Description  | Notes |
| -------- | --------------------- | ------------ | ----- |
| response | urllib3.HTTPResponse  | Raw response |
| body     | typing.Union[]        |              |
| headers  | ResponseHeadersFor200 |              |

#### ResponseHeadersFor200

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Content-Disposition | ContentDispositionSchema |             | optional |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

#### convert_bilingual_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_bilingual_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_bilingual_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_bilingual_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_bilingual_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_bilingual_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_bilingual_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_bilingual_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_bilingual_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_bilingual_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### convert_bilingual_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_bilingual_file**

<a id="get_bilingual_file"></a>

> get_bilingual_file(project_uid)

Download bilingual file

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import bilingual_file_api
from phrasetms_client.model.get_bilingual_file_dto import GetBilingualFileDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bilingual_file_api.BilingualFileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
    }
    try:
        # Download bilingual file
        api_response = api_instance.get_bilingual_file(
            path_params=path_params,
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling BilingualFileApi->get_bilingual_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUid': "projectUid_example",
    }
    query_params = {
        'format': "MXLF",
        'preview': True,
    }
    body = GetBilingualFileDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
    )
    try:
        # Download bilingual file
        api_response = api_instance.get_bilingual_file(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling BilingualFileApi->get_bilingual_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| query_params         | RequestQueryParams                                       |                                         |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**GetBilingualFileDto**](../../models/GetBilingualFileDto.md) |             |

### query_params

#### RequestQueryParams

| Name    | Type          | Description | Notes    |
| ------- | ------------- | ----------- | -------- |
| format  | FormatSchema  |             | optional |
| preview | PreviewSchema |             | optional |

# FormatSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                                        |
| ---------- | ------------- | ----------- | ------------------------------------------------------------------------------------------------------------ |
| str,       | str,          |             | must be one of ["MXLF", "DOCX", "XLIFF", "TMX", ] if omitted the server will use the default value of "MXLF" |

# PreviewSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                    |
| ---------- | ------------- | ----------- | -------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of True |

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

| Code | Class                                                      | Description                                                         |
| ---- | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned         |
| 200  | [ApiResponseFor200](#get_bilingual_file.ApiResponseFor200) | application/octet-stream, application/mxliff, application/xliff+xml |
| 400  | [ApiResponseFor400](#get_bilingual_file.ApiResponseFor400) | Bad request                                                         |
| 401  | [ApiResponseFor401](#get_bilingual_file.ApiResponseFor401) | Not authorized                                                      |
| 403  | [ApiResponseFor403](#get_bilingual_file.ApiResponseFor403) | Forbidden                                                           |
| 404  | [ApiResponseFor404](#get_bilingual_file.ApiResponseFor404) | Resource not found                                                  |
| 405  | [ApiResponseFor405](#get_bilingual_file.ApiResponseFor405) | Method not allowed                                                  |
| 408  | [ApiResponseFor408](#get_bilingual_file.ApiResponseFor408) | Timeout                                                             |
| 410  | [ApiResponseFor410](#get_bilingual_file.ApiResponseFor410) | Gone                                                                |
| 415  | [ApiResponseFor415](#get_bilingual_file.ApiResponseFor415) | Unsupported media type                                              |
| 429  | [ApiResponseFor429](#get_bilingual_file.ApiResponseFor429) | Too many requests                                                   |
| 500  | [ApiResponseFor500](#get_bilingual_file.ApiResponseFor500) | Internal server error                                               |
| 501  | [ApiResponseFor501](#get_bilingual_file.ApiResponseFor501) | Not implemented                                                     |

#### get_bilingual_file.ApiResponseFor200

| Name     | Type                  | Description  | Notes |
| -------- | --------------------- | ------------ | ----- |
| response | urllib3.HTTPResponse  | Raw response |
| body     | typing.Union[]        |              |
| headers  | ResponseHeadersFor200 |              |

#### ResponseHeadersFor200

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Content-Disposition | ContentDispositionSchema |             | optional |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

#### get_bilingual_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_bilingual_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_preview_file**

<a id="get_preview_file"></a>

> get_preview_file()

Download preview

Supports mxliff format

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import bilingual_file_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bilingual_file_api.BilingualFileApi(api_client)

    # example passing only optional values
    body = dict()
    try:
        # Download preview
        api_response = api_instance.get_preview_file(
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling BilingualFileApi->get_preview_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                                            | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset                      |
| content_type         | str                                                             | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                            | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                            | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_preview_file.ApiResponseFor200) | application/octet-stream                                    |
| 400  | [ApiResponseFor400](#get_preview_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_preview_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_preview_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_preview_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_preview_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_preview_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_preview_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_preview_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_preview_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_preview_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_preview_file.ApiResponseFor501) | Not implemented                                             |

#### get_preview_file.ApiResponseFor200

| Name     | Type                  | Description  | Notes |
| -------- | --------------------- | ------------ | ----- |
| response | urllib3.HTTPResponse  | Raw response |
| body     | typing.Union[]        |              |
| headers  | ResponseHeadersFor200 |              |

#### ResponseHeadersFor200

| Name                | Type                     | Description | Notes    |
| ------------------- | ------------------------ | ----------- | -------- |
| Content-Disposition | ContentDispositionSchema |             | optional |

# ContentDispositionSchema

Contains filename (UTF-8 encoded). `filename*=UTF-8''ExampleFileName.md`

## Model Type Info

| Input Type | Accessed Type | Description                                                                                        | Notes |
| ---------- | ------------- | -------------------------------------------------------------------------------------------------- | ----- |
| str,       | str,          | Contains filename (UTF-8 encoded). &#x60;filename\*&#x3D;UTF-8&#x27;&#x27;ExampleFileName.md&#x60; |

#### get_preview_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_preview_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_preview_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_preview_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_preview_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_preview_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_preview_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_preview_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_preview_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_preview_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_preview_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_bilingual_file**

<a id="upload_bilingual_file"></a>

> JobPartsDto upload_bilingual_file()

Upload bilingual file

Returns updated job parts

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import bilingual_file_api
from phrasetms_client.model.job_parts_dto import JobPartsDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bilingual_file_api.BilingualFileApi(api_client)

    # example passing only optional values
    query_params = {
        'format': "MXLF",
        'saveToTransMemory': "Confirmed",
        'setCompleted': False,
    }
    body = dict()
    try:
        # Upload bilingual file
        api_response = api_instance.upload_bilingual_file(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling BilingualFileApi->upload_bilingual_file: %s\n" % e)
```

### Parameters

| Name                 | Type                                                            | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset                      |
| query_params         | RequestQueryParams                                              |                                                 |
| content_type         | str                                                             | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                               | default is ('application/json', )               | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                            | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]                | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                            | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### query_params

#### RequestQueryParams

| Name              | Type                    | Description | Notes    |
| ----------------- | ----------------------- | ----------- | -------- |
| format            | FormatSchema            |             | optional |
| saveToTransMemory | SaveToTransMemorySchema |             | optional |
| setCompleted      | SetCompletedSchema      |             | optional |

# FormatSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                                 |
| ---------- | ------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| str,       | str,          |             | must be one of ["MXLF", "DOCX", "XLIFF", ] if omitted the server will use the default value of "MXLF" |

# SaveToTransMemorySchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                                         |
| ---------- | ------------- | ----------- | ------------------------------------------------------------------------------------------------------------- |
| str,       | str,          |             | must be one of ["All", "Confirmed", "None", ] if omitted the server will use the default value of "Confirmed" |

# SetCompletedSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

### Return Types, Responses

| Code | Class                                                         | Description                                                 |
| ---- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                  | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#upload_bilingual_file.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#upload_bilingual_file.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#upload_bilingual_file.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#upload_bilingual_file.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#upload_bilingual_file.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#upload_bilingual_file.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#upload_bilingual_file.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#upload_bilingual_file.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#upload_bilingual_file.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#upload_bilingual_file.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#upload_bilingual_file.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#upload_bilingual_file.ApiResponseFor501) | Not implemented                                             |

#### upload_bilingual_file.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                           | Description | Notes |
| ---------------------------------------------- | ----------- | ----- |
| [**JobPartsDto**](../../models/JobPartsDto.md) |             |

#### upload_bilingual_file.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### upload_bilingual_file.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
