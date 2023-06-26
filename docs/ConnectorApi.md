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
> ConnectorCreateResponseDto edit_connector(connector_id, connection_test=connection_test, body=body)

Edit connector

Edit selected connector

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.abstract_connector_dto import AbstractConnectorDto
from phrasetms_client.models.connector_create_response_dto import ConnectorCreateResponseDto
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
    api_instance = phrasetms_client.ConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | 
    connection_test = True # bool | For running connection test (optional)
    body = phrasetms_client.AbstractConnectorDto() # AbstractConnectorDto |  (optional)

    try:
        # Edit connector
        api_response = api_instance.edit_connector(connector_id, connection_test=connection_test, body=body)
        print("The response of ConnectorApi->edit_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->edit_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **connection_test** | **bool**| For running connection test | [optional] 
 **body** | [**AbstractConnectorDto**](AbstractConnectorDto.md)|  | [optional] 

### Return type

[**ConnectorCreateResponseDto**](ConnectorCreateResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edited |  -  |
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

# **get_connector**
> ConnectorDto get_connector(connector_id)

Get a connector

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.connector_dto import ConnectorDto
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
    api_instance = phrasetms_client.ConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | 

    try:
        # Get a connector
        api_response = api_instance.get_connector(connector_id)
        print("The response of ConnectorApi->get_connector:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_connector_list**
> ConnectorListDto get_connector_list(type=type)

List connectors

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.connector_list_dto import ConnectorListDto
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
    api_instance = phrasetms_client.ConnectorApi(api_client)
    type = 'type_example' # str |  (optional)

    try:
        # List connectors
        api_response = api_instance.get_connector_list(type=type)
        print("The response of ConnectorApi->get_connector_list:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_file**
> InputStreamLength get_file(connector_id, folder, file)

Download file

Download a file from a subfolder of the selected connector

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.input_stream_length import InputStreamLength
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
    api_instance = phrasetms_client.ConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | 
    folder = 'folder_example' # str | 
    file = 'file_example' # str | 

    try:
        # Download file
        api_response = api_instance.get_file(connector_id, folder, file)
        print("The response of ConnectorApi->get_file:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_file1**
> AsyncFileOpResponseDto get_file1(connector_id, folder, file, body=body)

Download file (async)

 Create an asynchronous request to download a file from a (sub)folder of the selected connector.  After a callback with successful response is received, prepared file can be downloaded by [Download prepared file](#operation/getPreparedFile)  or [Create job from connector asynchronous download task](#operation/createJobFromAsyncDownloadTask). 

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_file_op_response_dto import AsyncFileOpResponseDto
from phrasetms_client.models.get_file_request_params_dto import GetFileRequestParamsDto
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
    api_instance = phrasetms_client.ConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | 
    folder = 'folder_example' # str | 
    file = 'file_example' # str | 
    body = phrasetms_client.GetFileRequestParamsDto() # GetFileRequestParamsDto |  (optional)

    try:
        # Download file (async)
        api_response = api_instance.get_file1(connector_id, folder, file, body=body)
        print("The response of ConnectorApi->get_file1:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_folder**
> FileListDto get_folder(connector_id, folder, project_uid=project_uid, file_type=file_type, sort=sort, direction=direction)

List files in a subfolder

List files in a subfolder of the selected connector

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.file_list_dto import FileListDto
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
    api_instance = phrasetms_client.ConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | 
    folder = 'folder_example' # str | 
    project_uid = 'project_uid_example' # str |  (optional)
    file_type = 'ALL' # str |  (optional) (default to 'ALL')
    sort = 'NAME' # str |  (optional) (default to 'NAME')
    direction = 'ASCENDING' # str |  (optional) (default to 'ASCENDING')

    try:
        # List files in a subfolder
        api_response = api_instance.get_folder(connector_id, folder, project_uid=project_uid, file_type=file_type, sort=sort, direction=direction)
        print("The response of ConnectorApi->get_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->get_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **project_uid** | **str**|  | [optional] 
 **file_type** | **str**|  | [optional] [default to &#39;ALL&#39;]
 **sort** | **str**|  | [optional] [default to &#39;NAME&#39;]
 **direction** | **str**|  | [optional] [default to &#39;ASCENDING&#39;]

### Return type

[**FileListDto**](FileListDto.md)

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

# **get_prepared_file**
> InputStreamLength get_prepared_file(connector_id, folder, file, task_id)

Download prepared file

Download the file by referencing successfully finished async download request [Connector - Download file (async)](#operation/getFile_1).

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.input_stream_length import InputStreamLength
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
    api_instance = phrasetms_client.ConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | 
    folder = 'folder_example' # str | 
    file = 'file_example' # str | 
    task_id = 'task_id_example' # str | 

    try:
        # Download prepared file
        api_response = api_instance.get_prepared_file(connector_id, folder, file, task_id)
        print("The response of ConnectorApi->get_prepared_file:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_root_folder**
> FileListDto get_root_folder(connector_id, file_type=file_type, sort=sort, direction=direction)

List files in root

List files in a root folder of the selected connector

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.file_list_dto import FileListDto
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
    api_instance = phrasetms_client.ConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | 
    file_type = 'ALL' # str |  (optional) (default to 'ALL')
    sort = 'NAME' # str |  (optional) (default to 'NAME')
    direction = 'ASCENDING' # str |  (optional) (default to 'ASCENDING')

    try:
        # List files in root
        api_response = api_instance.get_root_folder(connector_id, file_type=file_type, sort=sort, direction=direction)
        print("The response of ConnectorApi->get_root_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->get_root_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **file_type** | **str**|  | [optional] [default to &#39;ALL&#39;]
 **sort** | **str**|  | [optional] [default to &#39;NAME&#39;]
 **direction** | **str**|  | [optional] [default to &#39;ASCENDING&#39;]

### Return type

[**FileListDto**](FileListDto.md)

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

# **upload_file**
> UploadResultDto upload_file(connector_id, folder, content_type, file, source_file_name=source_file_name, subfolder_name=subfolder_name, mime_type=mime_type, commit_message=commit_message)

Upload a file to a subfolder of the selected connector

Upload a file to a subfolder of the selected connector

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.upload_result_dto import UploadResultDto
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
    api_instance = phrasetms_client.ConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | 
    folder = 'folder_example' # str | 
    content_type = 'content_type_example' # str | 
    file = None # bytearray | Translated file to upload
    source_file_name = 'source_file_name_example' # str | Name or ID of the original file (optional)
    subfolder_name = 'subfolder_name_example' # str | Optional subfolder to upload the file to (optional)
    mime_type = 'mime_type_example' # str | Mime type of the file to upload (optional)
    commit_message = 'commit_message_example' # str | Commit message for upload to Git, etc. (optional)

    try:
        # Upload a file to a subfolder of the selected connector
        api_response = api_instance.upload_file(connector_id, folder, content_type, file, source_file_name=source_file_name, subfolder_name=subfolder_name, mime_type=mime_type, commit_message=commit_message)
        print("The response of ConnectorApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->upload_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **content_type** | **str**|  | 
 **file** | **bytearray**| Translated file to upload | 
 **source_file_name** | **str**| Name or ID of the original file | [optional] 
 **subfolder_name** | **str**| Optional subfolder to upload the file to | [optional] 
 **mime_type** | **str**| Mime type of the file to upload | [optional] 
 **commit_message** | **str**| Commit message for upload to Git, etc. | [optional] 

### Return type

[**UploadResultDto**](UploadResultDto.md)

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

# **upload_file1**
> AsyncFileOpResponseDto upload_file1(connector_id, folder, file_name, memsource, content_type, file, mime_type=mime_type)

Upload file (async)

Upload a file to a subfolder of the selected connector

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.async_file_op_response_dto import AsyncFileOpResponseDto
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
    api_instance = phrasetms_client.ConnectorApi(api_client)
    connector_id = 'connector_id_example' # str | 
    folder = 'folder_example' # str | 
    file_name = 'file_name_example' # str | 
    memsource = '{\"subfolderName\":\"myFolder\",\"commitMessage\":\"add translation\",\"callbackUrl\":\"https://webhook.site/83b222a1-5cf2-48ec-b8b9-7f79bb2a25e4\"}' # str | 
    content_type = 'content_type_example' # str | 
    file = None # bytearray | Translated file to upload
    mime_type = 'mime_type_example' # str | Mime type of the file to upload (optional)

    try:
        # Upload file (async)
        api_response = api_instance.upload_file1(connector_id, folder, file_name, memsource, content_type, file, mime_type=mime_type)
        print("The response of ConnectorApi->upload_file1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->upload_file1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **file_name** | **str**|  | 
 **memsource** | **str**|  | 
 **content_type** | **str**|  | 
 **file** | **bytearray**| Translated file to upload | 
 **mime_type** | **str**| Mime type of the file to upload | [optional] 

### Return type

[**AsyncFileOpResponseDto**](AsyncFileOpResponseDto.md)

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

