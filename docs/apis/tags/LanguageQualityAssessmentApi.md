<a id="__pageTop"></a>

# phrasetms_client.apis.tags.language_quality_assessment_api.LanguageQualityAssessmentApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                            | HTTP request                             | Description                          |
| ------------------------------------------------- | ---------------------------------------- | ------------------------------------ |
| [**download_lqa_reports**](#download_lqa_reports) | **get** /api2/v1/lqa/assessments/reports | Download LQA Assessment XLSX reports |

# **download_lqa_reports**

<a id="download_lqa_reports"></a>

> download_lqa_reports(job_parts)

Download LQA Assessment XLSX reports

Returns a single xlsx report or ZIP archive with multiple reports. If any given jobPart is not from LQA workflow step, reports from successive workflow steps may be returned If none were found returns 404 error, otherwise returns those that were found.

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import language_quality_assessment_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = language_quality_assessment_api.LanguageQualityAssessmentApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'jobParts': "jobParts_example",
    }
    try:
        # Download LQA Assessment XLSX reports
        api_response = api_instance.download_lqa_reports(
            query_params=query_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling LanguageQualityAssessmentApi->download_lqa_reports: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name     | Type           | Description | Notes |
| -------- | -------------- | ----------- | ----- |
| jobParts | JobPartsSchema |             |

# JobPartsSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#download_lqa_reports.ApiResponseFor200) | application/octet-stream                                    |
| 400  | [ApiResponseFor400](#download_lqa_reports.ApiResponseFor400) | Invalid request                                             |
| 401  | [ApiResponseFor401](#download_lqa_reports.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#download_lqa_reports.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#download_lqa_reports.ApiResponseFor404) | No reports found                                            |
| 405  | [ApiResponseFor405](#download_lqa_reports.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#download_lqa_reports.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#download_lqa_reports.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#download_lqa_reports.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#download_lqa_reports.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#download_lqa_reports.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#download_lqa_reports.ApiResponseFor501) | Not implemented                                             |

#### download_lqa_reports.ApiResponseFor200

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### download_lqa_reports.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
