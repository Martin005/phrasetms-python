# phrasetms_client.EmailTemplateApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_email_template**](EmailTemplateApi.md#get_org_email_template) | **GET** /api2/v1/emailTemplates/{templateUid} | Get email template
[**list_org_email_templates**](EmailTemplateApi.md#list_org_email_templates) | **GET** /api2/v1/emailTemplates | List email templates


# **get_org_email_template**
> OrganizationEmailTemplateDto get_org_email_template(template_uid)

Get email template

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.organization_email_template_dto import OrganizationEmailTemplateDto
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
    api_instance = phrasetms_client.EmailTemplateApi(api_client)
    template_uid = 'template_uid_example' # str | 

    try:
        # Get email template
        api_response = api_instance.get_org_email_template(template_uid)
        print("The response of EmailTemplateApi->get_org_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->get_org_email_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_uid** | **str**|  | 

### Return type

[**OrganizationEmailTemplateDto**](OrganizationEmailTemplateDto.md)

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

# **list_org_email_templates**
> PageDtoOrganizationEmailTemplateDto list_org_email_templates(type=type, page_number=page_number, page_size=page_size)

List email templates

### Example

```python
import time
import os
import phrasetms_client
from phrasetms_client.models.page_dto_organization_email_template_dto import PageDtoOrganizationEmailTemplateDto
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
    api_instance = phrasetms_client.EmailTemplateApi(api_client)
    type = 'type_example' # str |  (optional)
    page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
    page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

    try:
        # List email templates
        api_response = api_instance.list_org_email_templates(type=type, page_number=page_number, page_size=page_size)
        print("The response of EmailTemplateApi->list_org_email_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->list_org_email_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoOrganizationEmailTemplateDto**](PageDtoOrganizationEmailTemplateDto.md)

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

