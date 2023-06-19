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
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.LanguageQualityAssessmentApi()
job_parts = 'job_parts_example' # str | Comma separated list of JobPart UIDs

try:
    # Download LQA Assessment XLSX reports
    api_instance.download_lqa_reports(job_parts)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

