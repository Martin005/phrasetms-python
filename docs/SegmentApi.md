# phrasetms_client.SegmentApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_segments_count**](SegmentApi.md#get_segments_count) | **POST** /api2/v1/projects/{projectUid}/jobs/segmentsCount | Get segments count
[**list_segments**](SegmentApi.md#list_segments) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/segments | Get segments


# **get_segments_count**
> SegmentsCountsResponseListDto get_segments_count(project_uid, body=body)

Get segments count

Provides segments count (progress data)

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.job_part_ready_references import JobPartReadyReferences
from phrasetms_client.models.segments_counts_response_list_dto import SegmentsCountsResponseListDto
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
    api_instance = phrasetms_client.SegmentApi(api_client)
    project_uid = 'project_uid_example' # str | 
    body = phrasetms_client.JobPartReadyReferences() # JobPartReadyReferences |  (optional)

    try:
        # Get segments count
        api_response = api_instance.get_segments_count(project_uid, body=body)
        print("The response of SegmentApi->get_segments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentApi->get_segments_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**JobPartReadyReferences**](JobPartReadyReferences.md)|  | [optional] 

### Return type

[**SegmentsCountsResponseListDto**](SegmentsCountsResponseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**401** | Not authorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**405** | Method not allowed |  -  |
**408** | Timeout |  -  |
**410** | Gone |  -  |
**415** | Unsupported media type |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**501** | Not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_segments**
> SegmentListDto list_segments(project_uid, job_uid, begin_index=begin_index, end_index=end_index)

Get segments

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.segment_list_dto import SegmentListDto
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
    api_instance = phrasetms_client.SegmentApi(api_client)
    project_uid = 'project_uid_example' # str | 
    job_uid = 'job_uid_example' # str | 
    begin_index = 0 # int |  (optional) (default to 0)
    end_index = 0 # int |  (optional) (default to 0)

    try:
        # Get segments
        api_response = api_instance.list_segments(project_uid, job_uid, begin_index=begin_index, end_index=end_index)
        print("The response of SegmentApi->list_segments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentApi->list_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **begin_index** | **int**|  | [optional] [default to 0]
 **end_index** | **int**|  | [optional] [default to 0]

### Return type

[**SegmentListDto**](SegmentListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**401** | Not authorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**405** | Method not allowed |  -  |
**408** | Timeout |  -  |
**410** | Gone |  -  |
**415** | Unsupported media type |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**501** | Not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

