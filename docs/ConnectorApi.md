# phrasetms_client.ConnectorApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_connector**](ConnectorApi.md#edit_connector) | **PUT** /api2/v1/connectors/{connectorId} | Edit connector
[**get_connector**](ConnectorApi.md#get_connector) | **GET** /api2/v1/connectors/{connectorId} | Get a connector
[**get_connector_list**](ConnectorApi.md#get_connector_list) | **GET** /api2/v1/connectors | List connectors
[**get_file**](ConnectorApi.md#get_file) | **GET** /api2/v1/connectors/{connectorId}/folders/{folder}/files/{file} | Download file
[**get_file1**](ConnectorApi.md#get_file1) | **POST** /api2/v2/connectors/{connectorId}/folders/{folder}/files/{file} | Download file (async)
[**get_folder**](ConnectorApi.md#get_folder) | **GET** /api2/v1/connectors/{connectorId}/folders/{folder} | List files in a subfolder
[**get_prepared_file**](ConnectorApi.md#get_prepared_file) | **GET** /api2/v2/connectors/{connectorId}/folders/{folder}/files/{file}/tasks/{taskId} | Download prepared file
[**get_root_folder**](ConnectorApi.md#get_root_folder) | **GET** /api2/v1/connectors/{connectorId}/folders | List files in root
[**upload_file**](ConnectorApi.md#upload_file) | **POST** /api2/v1/connectors/{connectorId}/folders/{folder} | Upload a file to a subfolder of the selected connector
[**upload_file1**](ConnectorApi.md#upload_file1) | **POST** /api2/v2/connectors/{connectorId}/folders/{folder}/files/{fileName}/upload | Upload file (async)

# **edit_connector**
> ConnectorCreateResponseDto edit_connector(connector_id, body=body, connection_test=connection_test)

Edit connector

Edit selected connector

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ConnectorApi()
connector_id = 'connector_id_example' # str | 
body = phrasetms_client.AbstractConnectorDto() # AbstractConnectorDto |  (optional)
connection_test = true # bool | For running connection test (optional)

try:
    # Edit connector
    api_response = api_instance.edit_connector(connector_id, body=body, connection_test=connection_test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->edit_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **body** | [**AbstractConnectorDto**](AbstractConnectorDto.md)|  | [optional] 
 **connection_test** | **bool**| For running connection test | [optional] 

### Return type

[**ConnectorCreateResponseDto**](ConnectorCreateResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector**
> ConnectorDto get_connector(connector_id)

Get a connector

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ConnectorApi()
connector_id = 'connector_id_example' # str | 

try:
    # Get a connector
    api_response = api_instance.get_connector(connector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 

### Return type

[**ConnectorDto**](ConnectorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_list**
> ConnectorListDto get_connector_list(type=type)

List connectors

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ConnectorApi()
type = 'type_example' # str |  (optional)

try:
    # List connectors
    api_response = api_instance.get_connector_list(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_connector_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 

### Return type

[**ConnectorListDto**](ConnectorListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> InputStreamLength get_file(connector_id, folder, file)

Download file

Download a file from a subfolder of the selected connector

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ConnectorApi()
connector_id = 'connector_id_example' # str | 
folder = 'folder_example' # str | 
file = 'file_example' # str | 

try:
    # Download file
    api_response = api_instance.get_file(connector_id, folder, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **file** | **str**|  | 

### Return type

[**InputStreamLength**](InputStreamLength.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file1**
> AsyncFileOpResponseDto get_file1(connector_id, folder, file, body=body)

Download file (async)

 Create an asynchronous request to download a file from a (sub)folder of the selected connector.  After a callback with successful response is received, prepared file can be downloaded by [Download prepared file](#operation/getPreparedFile)  or [Create job from connector asynchronous download task](#operation/createJobFromAsyncDownloadTask). 

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ConnectorApi()
connector_id = 'connector_id_example' # str | 
folder = 'folder_example' # str | 
file = 'file_example' # str | 
body = phrasetms_client.GetFileRequestParamsDto() # GetFileRequestParamsDto |  (optional)

try:
    # Download file (async)
    api_response = api_instance.get_file1(connector_id, folder, file, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_file1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **file** | **str**|  | 
 **body** | [**GetFileRequestParamsDto**](GetFileRequestParamsDto.md)|  | [optional] 

### Return type

[**AsyncFileOpResponseDto**](AsyncFileOpResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> FileListDto get_folder(connector_id, folder, project_uid=project_uid, file_type=file_type, sort=sort, direction=direction)

List files in a subfolder

List files in a subfolder of the selected connector

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ConnectorApi()
connector_id = 'connector_id_example' # str | 
folder = 'folder_example' # str | 
project_uid = 'project_uid_example' # str |  (optional)
file_type = 'ALL' # str |  (optional) (default to ALL)
sort = 'NAME' # str |  (optional) (default to NAME)
direction = 'ASCENDING' # str |  (optional) (default to ASCENDING)

try:
    # List files in a subfolder
    api_response = api_instance.get_folder(connector_id, folder, project_uid=project_uid, file_type=file_type, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **project_uid** | **str**|  | [optional] 
 **file_type** | **str**|  | [optional] [default to ALL]
 **sort** | **str**|  | [optional] [default to NAME]
 **direction** | **str**|  | [optional] [default to ASCENDING]

### Return type

[**FileListDto**](FileListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prepared_file**
> InputStreamLength get_prepared_file(connector_id, folder, file, task_id)

Download prepared file

Download the file by referencing successfully finished async download request [Connector - Download file (async)](#operation/getFile_1).

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ConnectorApi()
connector_id = 'connector_id_example' # str | 
folder = 'folder_example' # str | 
file = 'file_example' # str | 
task_id = 'task_id_example' # str | 

try:
    # Download prepared file
    api_response = api_instance.get_prepared_file(connector_id, folder, file, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_prepared_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **file** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

[**InputStreamLength**](InputStreamLength.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_folder**
> FileListDto get_root_folder(connector_id, file_type=file_type, sort=sort, direction=direction)

List files in root

List files in a root folder of the selected connector

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ConnectorApi()
connector_id = 'connector_id_example' # str | 
file_type = 'ALL' # str |  (optional) (default to ALL)
sort = 'NAME' # str |  (optional) (default to NAME)
direction = 'ASCENDING' # str |  (optional) (default to ASCENDING)

try:
    # List files in root
    api_response = api_instance.get_root_folder(connector_id, file_type=file_type, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_root_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **file_type** | **str**|  | [optional] [default to ALL]
 **sort** | **str**|  | [optional] [default to NAME]
 **direction** | **str**|  | [optional] [default to ASCENDING]

### Return type

[**FileListDto**](FileListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> UploadResultDto upload_file(file, source_file_name, subfolder_name, mime_type, commit_message, content_type, connector_id, folder)

Upload a file to a subfolder of the selected connector

Upload a file to a subfolder of the selected connector

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ConnectorApi()
file = 'file_example' # str | 
source_file_name = 'source_file_name_example' # str | 
subfolder_name = 'subfolder_name_example' # str | 
mime_type = 'mime_type_example' # str | 
commit_message = 'commit_message_example' # str | 
content_type = 'content_type_example' # str | 
connector_id = 'connector_id_example' # str | 
folder = 'folder_example' # str | 

try:
    # Upload a file to a subfolder of the selected connector
    api_response = api_instance.upload_file(file, source_file_name, subfolder_name, mime_type, commit_message, content_type, connector_id, folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **source_file_name** | **str**|  | 
 **subfolder_name** | **str**|  | 
 **mime_type** | **str**|  | 
 **commit_message** | **str**|  | 
 **content_type** | **str**|  | 
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 

### Return type

[**UploadResultDto**](UploadResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file1**
> AsyncFileOpResponseDto upload_file1(file, memsource, content_type, connector_id, folder, file_name, mime_type=mime_type)

Upload file (async)

Upload a file to a subfolder of the selected connector

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.ConnectorApi()
file = 'file_example' # str | 
memsource = 'memsource_example' # str | 
content_type = 'content_type_example' # str | 
connector_id = 'connector_id_example' # str | 
folder = 'folder_example' # str | 
file_name = 'file_name_example' # str | 
mime_type = 'mime_type_example' # str | Mime type of the file to upload (optional)

try:
    # Upload file (async)
    api_response = api_instance.upload_file1(file, memsource, content_type, connector_id, folder, file_name, mime_type=mime_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->upload_file1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **memsource** | **str**|  | 
 **content_type** | **str**|  | 
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **file_name** | **str**|  | 
 **mime_type** | **str**| Mime type of the file to upload | [optional] 

### Return type

[**AsyncFileOpResponseDto**](AsyncFileOpResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

