# phrasetms_client.LanguageQualityAssessmentApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_lqa_reports**](LanguageQualityAssessmentApi.md#download_lqa_reports) | **GET** /api2/v1/lqa/assessments/reports | Download LQA Assessment XLSX reports


# **download_lqa_reports**
> download_lqa_reports(job_parts)

Download LQA Assessment XLSX reports

Returns a single xlsx report or ZIP archive with multiple reports. If any given jobPart is not from LQA workflow step, reports from successive workflow steps may be returned If none were found returns 404 error, otherwise returns those that were found.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)


# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrasetms_client.LanguageQualityAssessmentApi(api_client)
    job_parts = 'job_parts_example' # str | Comma separated list of JobPart UIDs

    try:
        # Download LQA Assessment XLSX reports
        api_instance.download_lqa_reports(job_parts)
    except Exception as e:
        print("Exception when calling LanguageQualityAssessmentApi->download_lqa_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_parts** | **str**| Comma separated list of JobPart UIDs | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/octet-stream |  -  |
**400** | Invalid request |  -  |
**401** | Not authorized |  -  |
**403** | Forbidden |  -  |
**404** | No reports found |  -  |
**405** | Method not allowed |  -  |
**408** | Timeout |  -  |
**410** | Gone |  -  |
**415** | Unsupported media type |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**501** | Not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

