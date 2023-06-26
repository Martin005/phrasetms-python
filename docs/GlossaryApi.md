# phrasetms_client.GlossaryApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_glossary**](GlossaryApi.md#activate_glossary) | **PUT** /api2/v1/glossaries/{glossaryUid}/activate | Activate/Deactivate glossary
[**create_glossary**](GlossaryApi.md#create_glossary) | **POST** /api2/v1/glossaries | Create glossary
[**delete_glossary**](GlossaryApi.md#delete_glossary) | **DELETE** /api2/v1/glossaries/{glossaryUid} | Delete glossary
[**get_glossary**](GlossaryApi.md#get_glossary) | **GET** /api2/v1/glossaries/{glossaryUid} | Get glossary
[**list_glossaries**](GlossaryApi.md#list_glossaries) | **GET** /api2/v1/glossaries | List glossaries
[**update_glossary**](GlossaryApi.md#update_glossary) | **PUT** /api2/v1/glossaries/{glossaryUid} | Edit glossary


# **activate_glossary**
> GlossaryDto activate_glossary(glossary_uid, body=body)

Activate/Deactivate glossary

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.glossary_activation_dto import GlossaryActivationDto
from phrasetms_client.models.glossary_dto import GlossaryDto
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
    api_instance = phrasetms_client.GlossaryApi(api_client)
    glossary_uid = 'glossary_uid_example' # str | 
    body = phrasetms_client.GlossaryActivationDto() # GlossaryActivationDto |  (optional)

    try:
        # Activate/Deactivate glossary
        api_response = api_instance.activate_glossary(glossary_uid, body=body)
        print("The response of GlossaryApi->activate_glossary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlossaryApi->activate_glossary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **glossary_uid** | **str**|  | 
 **body** | [**GlossaryActivationDto**](GlossaryActivationDto.md)|  | [optional] 

### Return type

[**GlossaryDto**](GlossaryDto.md)

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

# **create_glossary**
> GlossaryDto create_glossary(body=body)

Create glossary

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.glossary_dto import GlossaryDto
from phrasetms_client.models.glossary_edit_dto import GlossaryEditDto
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
    api_instance = phrasetms_client.GlossaryApi(api_client)
    body = phrasetms_client.GlossaryEditDto() # GlossaryEditDto |  (optional)

    try:
        # Create glossary
        api_response = api_instance.create_glossary(body=body)
        print("The response of GlossaryApi->create_glossary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlossaryApi->create_glossary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GlossaryEditDto**](GlossaryEditDto.md)|  | [optional] 

### Return type

[**GlossaryDto**](GlossaryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
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

# **delete_glossary**
> delete_glossary(glossary_uid, purge=purge)

Delete glossary

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
    api_instance = phrasetms_client.GlossaryApi(api_client)
    glossary_uid = 'glossary_uid_example' # str | 
    purge = False # bool | purge=false - the Glossary can later be restored,                     'purge=true - the Glossary is completely deleted and cannot be restored (optional) (default to False)

    try:
        # Delete glossary
        api_instance.delete_glossary(glossary_uid, purge=purge)
    except Exception as e:
        print("Exception when calling GlossaryApi->delete_glossary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **glossary_uid** | **str**|  | 
 **purge** | **bool**| purge&#x3D;false - the Glossary can later be restored,                     &#39;purge&#x3D;true - the Glossary is completely deleted and cannot be restored | [optional] [default to False]

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
**204** | No Content |  -  |
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

# **get_glossary**
> GlossaryDto get_glossary(glossary_uid)

Get glossary

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.glossary_dto import GlossaryDto
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
    api_instance = phrasetms_client.GlossaryApi(api_client)
    glossary_uid = 'glossary_uid_example' # str | 

    try:
        # Get glossary
        api_response = api_instance.get_glossary(glossary_uid)
        print("The response of GlossaryApi->get_glossary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlossaryApi->get_glossary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **glossary_uid** | **str**|  | 

### Return type

[**GlossaryDto**](GlossaryDto.md)

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

# **list_glossaries**
> PageDtoGlossaryDto list_glossaries(name=name, lang=lang, page_number=page_number, page_size=page_size)

List glossaries

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_glossary_dto import PageDtoGlossaryDto
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
    api_instance = phrasetms_client.GlossaryApi(api_client)
    name = 'name_example' # str |  (optional)
    lang = ['lang_example'] # List[str] | Language of the glossary (optional)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List glossaries
        api_response = api_instance.list_glossaries(name=name, lang=lang, page_number=page_number, page_size=page_size)
        print("The response of GlossaryApi->list_glossaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlossaryApi->list_glossaries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **lang** | [**List[str]**](str.md)| Language of the glossary | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoGlossaryDto**](PageDtoGlossaryDto.md)

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

# **update_glossary**
> GlossaryDto update_glossary(glossary_uid, body=body)

Edit glossary

Languages can only be added, their removal is not supported

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.glossary_dto import GlossaryDto
from phrasetms_client.models.glossary_edit_dto import GlossaryEditDto
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
    api_instance = phrasetms_client.GlossaryApi(api_client)
    glossary_uid = 'glossary_uid_example' # str | 
    body = phrasetms_client.GlossaryEditDto() # GlossaryEditDto |  (optional)

    try:
        # Edit glossary
        api_response = api_instance.update_glossary(glossary_uid, body=body)
        print("The response of GlossaryApi->update_glossary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlossaryApi->update_glossary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **glossary_uid** | **str**|  | 
 **body** | [**GlossaryEditDto**](GlossaryEditDto.md)|  | [optional] 

### Return type

[**GlossaryDto**](GlossaryDto.md)

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

