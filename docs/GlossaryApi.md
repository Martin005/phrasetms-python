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
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.GlossaryApi()
glossary_uid = 'glossary_uid_example' # str | 
body = phrasetms_client.GlossaryActivationDto() # GlossaryActivationDto |  (optional)

try:
    # Activate/Deactivate glossary
    api_response = api_instance.activate_glossary(glossary_uid, body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_glossary**
> GlossaryDto create_glossary(body=body)

Create glossary

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.GlossaryApi()
body = phrasetms_client.GlossaryEditDto() # GlossaryEditDto |  (optional)

try:
    # Create glossary
    api_response = api_instance.create_glossary(body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_glossary**
> delete_glossary(glossary_uid, purge=purge)

Delete glossary

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.GlossaryApi()
glossary_uid = 'glossary_uid_example' # str | 
purge = false # bool | purge=false - the Glossary can later be restored,                     'purge=true - the Glossary is completely deleted and cannot be restored (optional) (default to false)

try:
    # Delete glossary
    api_instance.delete_glossary(glossary_uid, purge=purge)
except ApiException as e:
    print("Exception when calling GlossaryApi->delete_glossary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **glossary_uid** | **str**|  | 
 **purge** | **bool**| purge&#x3D;false - the Glossary can later be restored,                     &#x27;purge&#x3D;true - the Glossary is completely deleted and cannot be restored | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_glossary**
> GlossaryDto get_glossary(glossary_uid)

Get glossary

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.GlossaryApi()
glossary_uid = 'glossary_uid_example' # str | 

try:
    # Get glossary
    api_response = api_instance.get_glossary(glossary_uid)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_glossaries**
> PageDtoGlossaryDto list_glossaries(name=name, lang=lang, page_number=page_number, page_size=page_size)

List glossaries

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.GlossaryApi()
name = 'name_example' # str |  (optional)
lang = ['lang_example'] # list[str] | Language of the glossary (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List glossaries
    api_response = api_instance.list_glossaries(name=name, lang=lang, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->list_glossaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **lang** | [**list[str]**](str.md)| Language of the glossary | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoGlossaryDto**](PageDtoGlossaryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_glossary**
> GlossaryDto update_glossary(glossary_uid, body=body)

Edit glossary

Languages can only be added, their removal is not supported

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.GlossaryApi()
glossary_uid = 'glossary_uid_example' # str | 
body = phrasetms_client.GlossaryEditDto() # GlossaryEditDto |  (optional)

try:
    # Edit glossary
    api_response = api_instance.update_glossary(glossary_uid, body=body)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

