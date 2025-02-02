# phrasetms_client.BilingualFileApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_bilingual_file**](BilingualFileApi.md#compare_bilingual_file) | **POST** /api2/v1/bilingualFiles/compare | Compare bilingual file
[**convert_bilingual_file**](BilingualFileApi.md#convert_bilingual_file) | **POST** /api2/v1/bilingualFiles/convert | Convert bilingual file
[**get_bilingual_file**](BilingualFileApi.md#get_bilingual_file) | **POST** /api2/v1/projects/{projectUid}/jobs/bilingualFile | Download bilingual file
[**get_preview_file**](BilingualFileApi.md#get_preview_file) | **POST** /api2/v1/bilingualFiles/preview | Download preview
[**upload_bilingual_file_v2**](BilingualFileApi.md#upload_bilingual_file_v2) | **POST** /api2/v2/bilingualFiles | Upload bilingual file


# **compare_bilingual_file**
> ComparedSegmentsDto compare_bilingual_file(workflow_level=workflow_level, body=body)

Compare bilingual file

Compares bilingual file to job state. Returns list of compared segments.

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.compared_segments_dto import ComparedSegmentsDto
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
    api_instance = phrasetms_client.BilingualFileApi(api_client)
    workflow_level = 1 # int |  (optional) (default to 1)
    body = None # object |  (optional)

    try:
        # Compare bilingual file
        api_response = api_instance.compare_bilingual_file(workflow_level=workflow_level, body=body)
        print("The response of BilingualFileApi->compare_bilingual_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BilingualFileApi->compare_bilingual_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_level** | **int**|  | [optional] [default to 1]
 **body** | **object**|  | [optional] 

### Return type

[**ComparedSegmentsDto**](ComparedSegmentsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
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

# **convert_bilingual_file**
> convert_bilingual_file(var_from, to, body=body)

Convert bilingual file

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
    api_instance = phrasetms_client.BilingualFileApi(api_client)
    var_from = 'var_from_example' # str | 
    to = 'to_example' # str | 
    body = None # object |  (optional)

    try:
        # Convert bilingual file
        api_instance.convert_bilingual_file(var_from, to, body=body)
    except Exception as e:
        print("Exception when calling BilingualFileApi->convert_bilingual_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**|  | 
 **to** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/octet-stream |  * Content-Disposition - Contains filename (UTF-8 encoded).    &#x60;filename*&#x3D;UTF-8&#39;&#39;ExampleFileName.md&#x60; <br>  |
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

# **get_bilingual_file**
> get_bilingual_file(project_uid, format=format, preview=preview, body=body)

Download bilingual file

 This API call generates a bilingual file in the chosen format by merging all submitted jobs together. Note that all submitted jobs must belong to the same project; it's not feasible to merge jobs from multiple projects.  When dealing with MXLIFF or DOCX files, modifications made externally can be imported back into the Phrase TMS project. Any changes will be synchronized into the editor, allowing actions like confirming or locking segments.  Unlike the user interface (UI), the APIs also support XLIFF as a bilingual format, intended primarily for export purposes. However, TMX and XLIFF files cannot be imported back into the project to reflect external changes.  While MXLIFF files are editable using various means, their primary intended use is with the [CAT Desktop Editor](https://support.phrase.com/hc/en-us/articles/5709683873052-CAT-Desktop-Editor-TMS-). It's crucial to note that alterations to the file incompatible with the CAT Desktop Editor's features may result in a corrupted file, leading to potential loss or duplication of work. 

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.get_bilingual_file_dto import GetBilingualFileDto
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
    api_instance = phrasetms_client.BilingualFileApi(api_client)
    project_uid = 'project_uid_example' # str | 
    format = 'MXLF' # str |  (optional) (default to 'MXLF')
    preview = True # bool |  (optional) (default to True)
    body = phrasetms_client.GetBilingualFileDto() # GetBilingualFileDto |  (optional)

    try:
        # Download bilingual file
        api_instance.get_bilingual_file(project_uid, format=format, preview=preview, body=body)
    except Exception as e:
        print("Exception when calling BilingualFileApi->get_bilingual_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **format** | **str**|  | [optional] [default to &#39;MXLF&#39;]
 **preview** | **bool**|  | [optional] [default to True]
 **body** | [**GetBilingualFileDto**](GetBilingualFileDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/octet-stream, application/mxliff, application/xliff+xml |  * Content-Disposition - Contains filename (UTF-8 encoded).    &#x60;filename*&#x3D;UTF-8&#39;&#39;ExampleFileName.md&#x60; <br>  |
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

# **get_preview_file**
> get_preview_file(body=body)

Download preview

Supports mxliff format

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
    api_instance = phrasetms_client.BilingualFileApi(api_client)
    body = None # object |  (optional)

    try:
        # Download preview
        api_instance.get_preview_file(body=body)
    except Exception as e:
        print("Exception when calling BilingualFileApi->get_preview_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/octet-stream |  * Content-Disposition - Contains filename (UTF-8 encoded).    &#x60;filename*&#x3D;UTF-8&#39;&#39;ExampleFileName.md&#x60; <br>  |
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

# **upload_bilingual_file_v2**
> ProjectJobPartsDto upload_bilingual_file_v2(file, save_to_trans_memory=save_to_trans_memory, set_completed=set_completed)

Upload bilingual file

Returns updated job parts and projects

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.multipart_file import MultipartFile
from phrasetms_client.models.project_job_parts_dto import ProjectJobPartsDto
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
    api_instance = phrasetms_client.BilingualFileApi(api_client)
    file = phrasetms_client.MultipartFile(local_path="output.mxliff") # MultipartFile | 
    save_to_trans_memory = 'Confirmed' # str |  (optional) (default to 'Confirmed')
    set_completed = False # bool |  (optional) (default to False)

    try:
        # Upload bilingual file
        api_response = api_instance.upload_bilingual_file_v2(file, save_to_trans_memory=save_to_trans_memory, set_completed=set_completed)
        print("The response of BilingualFileApi->upload_bilingual_file_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BilingualFileApi->upload_bilingual_file_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**MultipartFile**](MultipartFile.md)|  | 
 **save_to_trans_memory** | **str**|  | [optional] [default to &#39;Confirmed&#39;]
 **set_completed** | **bool**|  | [optional] [default to False]

### Return type

[**ProjectJobPartsDto**](ProjectJobPartsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

