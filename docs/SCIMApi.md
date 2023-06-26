# phrasetms_client.SCIMApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_scim**](SCIMApi.md#create_user_scim) | **POST** /api2/v1/scim/Users | Create user using SCIM
[**delete_user**](SCIMApi.md#delete_user) | **DELETE** /api2/v1/scim/Users/{userId} | Delete user using SCIM
[**edit_user**](SCIMApi.md#edit_user) | **PUT** /api2/v1/scim/Users/{userId} | Edit user using SCIM
[**get_resource_types**](SCIMApi.md#get_resource_types) | **GET** /api2/v1/scim/ResourceTypes | List the types of SCIM Resources available
[**get_schema_by_urn**](SCIMApi.md#get_schema_by_urn) | **GET** /api2/v1/scim/Schemas/{schemaUrn} | Get supported SCIM Schema by urn
[**get_schemas**](SCIMApi.md#get_schemas) | **GET** /api2/v1/scim/Schemas | Get supported SCIM Schemas
[**get_scim_user**](SCIMApi.md#get_scim_user) | **GET** /api2/v1/scim/Users/{userId} | Get user
[**get_service_provider_config_dto**](SCIMApi.md#get_service_provider_config_dto) | **GET** /api2/v1/scim/ServiceProviderConfig | Retrieve the Service Provider&#39;s Configuration
[**patch_user**](SCIMApi.md#patch_user) | **PATCH** /api2/v1/scim/Users/{userId} | Patch user using SCIM
[**search_users**](SCIMApi.md#search_users) | **GET** /api2/v1/scim/Users | Search users


# **create_user_scim**
> ScimUserCoreDto create_user_scim(authorization=authorization, body=body)

Create user using SCIM

 Supported schema: `\"urn:ietf:params:scim:schemas:core:2.0:User\"`  Create active user: ``` {     \"schemas\": [         \"urn:ietf:params:scim:schemas:core:2.0:User\"     ],     \"active\": true,     \"userName\": \"john.doe\",     \"emails\": [         {             \"primary\": true,             \"value\": \"john.doe@example.com\",             \"type\": \"work\"         }     ],     \"name\": {         \"givenName\": \"John\",         \"familyName\": \"Doe\"     } } ``` 

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.scim_user_core_dto import ScimUserCoreDto
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
    api_instance = phrasetms_client.SCIMApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    body = phrasetms_client.ScimUserCoreDto() # ScimUserCoreDto |  (optional)

    try:
        # Create user using SCIM
        api_response = api_instance.create_user_scim(authorization=authorization, body=body)
        print("The response of SCIMApi->create_user_scim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMApi->create_user_scim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **body** | [**ScimUserCoreDto**](ScimUserCoreDto.md)|  | [optional] 

### Return type

[**ScimUserCoreDto**](ScimUserCoreDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json
 - **Accept**: application/json, application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
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

# **delete_user**
> delete_user(user_id, authorization=authorization)

Delete user using SCIM

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
    api_instance = phrasetms_client.SCIMApi(api_client)
    user_id = 56 # int | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Delete user using SCIM
        api_instance.delete_user(user_id, authorization=authorization)
    except Exception as e:
        print("Exception when calling SCIMApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 

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
**200** | No Content |  -  |
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

# **edit_user**
> ScimUserCoreDto edit_user(user_id, authorization=authorization, body=body)

Edit user using SCIM

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.scim_user_core_dto import ScimUserCoreDto
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
    api_instance = phrasetms_client.SCIMApi(api_client)
    user_id = 56 # int | 
    authorization = 'authorization_example' # str |  (optional)
    body = phrasetms_client.ScimUserCoreDto() # ScimUserCoreDto |  (optional)

    try:
        # Edit user using SCIM
        api_response = api_instance.edit_user(user_id, authorization=authorization, body=body)
        print("The response of SCIMApi->edit_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMApi->edit_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **body** | [**ScimUserCoreDto**](ScimUserCoreDto.md)|  | [optional] 

### Return type

[**ScimUserCoreDto**](ScimUserCoreDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json
 - **Accept**: application/json, application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
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

# **get_resource_types**
> List[ScimResourceTypeSchema] get_resource_types()

List the types of SCIM Resources available

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.scim_resource_type_schema import ScimResourceTypeSchema
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
    api_instance = phrasetms_client.SCIMApi(api_client)

    try:
        # List the types of SCIM Resources available
        api_response = api_instance.get_resource_types()
        print("The response of SCIMApi->get_resource_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMApi->get_resource_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ScimResourceTypeSchema]**](ScimResourceTypeSchema.md)

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

# **get_schema_by_urn**
> ScimResourceSchema get_schema_by_urn(schema_urn)

Get supported SCIM Schema by urn

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.scim_resource_schema import ScimResourceSchema
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
    api_instance = phrasetms_client.SCIMApi(api_client)
    schema_urn = 'schema_urn_example' # str | 

    try:
        # Get supported SCIM Schema by urn
        api_response = api_instance.get_schema_by_urn(schema_urn)
        print("The response of SCIMApi->get_schema_by_urn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMApi->get_schema_by_urn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_urn** | **str**|  | 

### Return type

[**ScimResourceSchema**](ScimResourceSchema.md)

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

# **get_schemas**
> List[ScimResourceSchema] get_schemas()

Get supported SCIM Schemas

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.scim_resource_schema import ScimResourceSchema
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
    api_instance = phrasetms_client.SCIMApi(api_client)

    try:
        # Get supported SCIM Schemas
        api_response = api_instance.get_schemas()
        print("The response of SCIMApi->get_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMApi->get_schemas: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ScimResourceSchema]**](ScimResourceSchema.md)

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

# **get_scim_user**
> ScimUserCoreDto get_scim_user(user_id, authorization=authorization)

Get user

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.scim_user_core_dto import ScimUserCoreDto
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
    api_instance = phrasetms_client.SCIMApi(api_client)
    user_id = 56 # int | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get user
        api_response = api_instance.get_scim_user(user_id, authorization=authorization)
        print("The response of SCIMApi->get_scim_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMApi->get_scim_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ScimUserCoreDto**](ScimUserCoreDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

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

# **get_service_provider_config_dto**
> ServiceProviderConfigDto get_service_provider_config_dto()

Retrieve the Service Provider's Configuration

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.service_provider_config_dto import ServiceProviderConfigDto
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
    api_instance = phrasetms_client.SCIMApi(api_client)

    try:
        # Retrieve the Service Provider's Configuration
        api_response = api_instance.get_service_provider_config_dto()
        print("The response of SCIMApi->get_service_provider_config_dto:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMApi->get_service_provider_config_dto: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceProviderConfigDto**](ServiceProviderConfigDto.md)

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

# **patch_user**
> ScimUserCoreDto patch_user(user_id, authorization=authorization, body=body)

Patch user using SCIM

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.scim_user_core_dto import ScimUserCoreDto
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
    api_instance = phrasetms_client.SCIMApi(api_client)
    user_id = 56 # int | 
    authorization = 'authorization_example' # str |  (optional)
    body = None # Dict[str, object] |  (optional)

    try:
        # Patch user using SCIM
        api_response = api_instance.patch_user(user_id, authorization=authorization, body=body)
        print("The response of SCIMApi->patch_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCIMApi->patch_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 
 **body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

[**ScimUserCoreDto**](ScimUserCoreDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Patched |  -  |
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

# **search_users**
> search_users(authorization=authorization, filter=filter, attributes=attributes, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)

Search users

 This operation supports <a href=\"http://ldapwiki.com/wiki/SCIM%20Filtering\" target=\"_blank\">SCIM Filter</a>,  <a href=\"http://ldapwiki.com/wiki/SCIM%20Search%20Request\" target=\"_blank\">SCIM attributes</a> and  <a href=\"http://ldapwiki.com/wiki/SCIM%20Sorting\" target=\"_blank\">SCIM sort</a>  Supported attributes:   - `id`   - `active`   - `userName`   - `name.givenName`   - `name.familyName`   - `emails.value`   - `meta.created` 

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
    api_instance = phrasetms_client.SCIMApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    filter = 'filter_example' # str | See method description (optional)
    attributes = 'attributes_example' # str | See method description (optional)
    sort_by = 'sort_by_example' # str | See method description (optional)
    sort_order = 'ascending' # str | See method description (optional) (default to 'ascending')
    start_index = 1 # int | The 1-based index of the first search result. Default 1 (optional) (default to 1)
    count = 50 # int | Non-negative Integer. Specifies the desired maximum number of search results per page; e.g., 10. (optional) (default to 50)

    try:
        # Search users
        api_instance.search_users(authorization=authorization, filter=filter, attributes=attributes, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)
    except Exception as e:
        print("Exception when calling SCIMApi->search_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **filter** | **str**| See method description | [optional] 
 **attributes** | **str**| See method description | [optional] 
 **sort_by** | **str**| See method description | [optional] 
 **sort_order** | **str**| See method description | [optional] [default to &#39;ascending&#39;]
 **start_index** | **int**| The 1-based index of the first search result. Default 1 | [optional] [default to 1]
 **count** | **int**| Non-negative Integer. Specifies the desired maximum number of search results per page; e.g., 10. | [optional] [default to 50]

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

