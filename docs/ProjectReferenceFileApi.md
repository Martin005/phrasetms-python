# phrasetms_client.ProjectReferenceFileApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_delete_reference_files**](ProjectReferenceFileApi.md#batch_delete_reference_files) | **DELETE** /api2/v1/projects/{projectUid}/references | Delete project reference files (batch)
[**batch_download_reference_files**](ProjectReferenceFileApi.md#batch_download_reference_files) | **POST** /api2/v1/projects/{projectUid}/references/download | Download project reference files (batch)
[**create_note_ref**](ProjectReferenceFileApi.md#create_note_ref) | **POST** /api2/v1/projects/{projectUid}/references | Create project reference file
[**download_reference**](ProjectReferenceFileApi.md#download_reference) | **GET** /api2/v1/projects/{projectUid}/references/{referenceFileId} | Download project reference file
[**list_reference_file_creators**](ProjectReferenceFileApi.md#list_reference_file_creators) | **GET** /api2/v1/projects/{projectUid}/references/creators | List project reference file creators
[**list_reference_files**](ProjectReferenceFileApi.md#list_reference_files) | **GET** /api2/v1/projects/{projectUid}/references | List project reference files

# **batch_delete_reference_files**
> batch_delete_reference_files(project_uid, body=body)

Delete project reference files (batch)

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectReferenceFileApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.ProjectReferenceFilesRequestDto() # ProjectReferenceFilesRequestDto |  (optional)

try:
    # Delete project reference files (batch)
    api_instance.batch_delete_reference_files(project_uid, body=body)
except ApiException as e:
    print("Exception when calling ProjectReferenceFileApi->batch_delete_reference_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**ProjectReferenceFilesRequestDto**](ProjectReferenceFilesRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_download_reference_files**
> batch_download_reference_files(project_uid, body=body)

Download project reference files (batch)

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectReferenceFileApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.ProjectReferenceFilesRequestDto() # ProjectReferenceFilesRequestDto |  (optional)

try:
    # Download project reference files (batch)
    api_instance.batch_download_reference_files(project_uid, body=body)
except ApiException as e:
    print("Exception when calling ProjectReferenceFileApi->batch_download_reference_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**ProjectReferenceFilesRequestDto**](ProjectReferenceFilesRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_note_ref**
> ReferenceFileReference create_note_ref(project_uid, body=body, content_disposition=content_disposition, x_memsource_note=x_memsource_note)

Create project reference file

Accepts `application/octet-stream` or `application/json`.<br>                        - `application/json` - `note` field will be converted to .txt.<br>                        - `application/octet-stream` - `Content-Disposition` header is required

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectReferenceFileApi()
project_uid = 'project_uid_example' # str | 
body = phrasetms_client.CreateReferenceFileNoteDto() # CreateReferenceFileNoteDto |  (optional)
content_disposition = 'content_disposition_example' # str | Required for `application/octet-stream`.<br> Example: `filename*=UTF-8''YourFileName.txt` (optional)
x_memsource_note = 'x_memsource_note_example' # str | For use with `application/octet-stream` (optional)

try:
    # Create project reference file
    api_response = api_instance.create_note_ref(project_uid, body=body, content_disposition=content_disposition, x_memsource_note=x_memsource_note)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectReferenceFileApi->create_note_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**CreateReferenceFileNoteDto**](CreateReferenceFileNoteDto.md)|  | [optional] 
 **content_disposition** | **str**| Required for &#x60;application/octet-stream&#x60;.&lt;br&gt; Example: &#x60;filename*&#x3D;UTF-8&#x27;&#x27;YourFileName.txt&#x60; | [optional] 
 **x_memsource_note** | **str**| For use with &#x60;application/octet-stream&#x60; | [optional] 

### Return type

[**ReferenceFileReference**](ReferenceFileReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_reference**
> download_reference(project_uid, reference_file_id)

Download project reference file

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectReferenceFileApi()
project_uid = 'project_uid_example' # str | 
reference_file_id = 'reference_file_id_example' # str | 

try:
    # Download project reference file
    api_instance.download_reference(project_uid, reference_file_id)
except ApiException as e:
    print("Exception when calling ProjectReferenceFileApi->download_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **reference_file_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reference_file_creators**
> UserReferencesDto list_reference_file_creators(project_uid, user_name=user_name)

List project reference file creators

The result is not paged and returns up to 50 users.                 If the requested user is not included, the search can be narrowed down with the `userName` parameter.             

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectReferenceFileApi()
project_uid = 'project_uid_example' # str | 
user_name = 'user_name_example' # str |  (optional)

try:
    # List project reference file creators
    api_response = api_instance.list_reference_file_creators(project_uid, user_name=user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectReferenceFileApi->list_reference_file_creators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **user_name** | **str**|  | [optional] 

### Return type

[**UserReferencesDto**](UserReferencesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reference_files**
> ReferenceFilePageDto list_reference_files(project_uid, filename=filename, date_created_since=date_created_since, created_by=created_by, page_number=page_number, page_size=page_size, sort=sort, order=order)

List project reference files

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ProjectReferenceFileApi()
project_uid = 'project_uid_example' # str | 
filename = 'filename_example' # str |  (optional)
date_created_since = 'date_created_since_example' # str | date time in ISO 8601 UTC format (optional)
created_by = 'created_by_example' # str | UID of user (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)
sort = 'DATE_CREATED' # str |  (optional) (default to DATE_CREATED)
order = 'DESC' # str |  (optional) (default to DESC)

try:
    # List project reference files
    api_response = api_instance.list_reference_files(project_uid, filename=filename, date_created_since=date_created_since, created_by=created_by, page_number=page_number, page_size=page_size, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectReferenceFileApi->list_reference_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **filename** | **str**|  | [optional] 
 **date_created_since** | **str**| date time in ISO 8601 UTC format | [optional] 
 **created_by** | **str**| UID of user | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]
 **sort** | **str**|  | [optional] [default to DATE_CREATED]
 **order** | **str**|  | [optional] [default to DESC]

### Return type

[**ReferenceFilePageDto**](ReferenceFilePageDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

