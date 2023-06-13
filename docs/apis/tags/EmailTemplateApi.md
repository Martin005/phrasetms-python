<a id="__pageTop"></a>
# openapi_client.apis.tags.email_template_api.EmailTemplateApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_email_template**](#get_org_email_template) | **get** /api2/v1/emailTemplates/{templateUid} | Get email template
[**list_org_email_templates**](#list_org_email_templates) | **get** /api2/v1/emailTemplates | List email templates

# **get_org_email_template**
<a id="get_org_email_template"></a>
> OrganizationEmailTemplateDto get_org_email_template(template_uid)

Get email template

### Example

```python
import openapi_client
from openapi_client.apis.tags import email_template_api
from openapi_client.model.organization_email_template_dto import OrganizationEmailTemplateDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = email_template_api.EmailTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'templateUid': "templateUid_example",
    }
    try:
        # Get email template
        api_response = api_instance.get_org_email_template(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EmailTemplateApi->get_org_email_template: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
templateUid | TemplateUidSchema | | 

# TemplateUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_org_email_template.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_org_email_template.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_org_email_template.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_org_email_template.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_org_email_template.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_org_email_template.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_org_email_template.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_org_email_template.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_org_email_template.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_org_email_template.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_org_email_template.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_org_email_template.ApiResponseFor501) | Not implemented

#### get_org_email_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationEmailTemplateDto**](../../models/OrganizationEmailTemplateDto.md) |  | 


#### get_org_email_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_org_email_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_org_email_template.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_org_email_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_org_email_template.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_org_email_template.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_org_email_template.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_org_email_template.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_org_email_template.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_org_email_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_org_email_template.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_org_email_templates**
<a id="list_org_email_templates"></a>
> PageDtoOrganizationEmailTemplateDto list_org_email_templates()

List email templates

### Example

```python
import openapi_client
from openapi_client.apis.tags import email_template_api
from openapi_client.model.page_dto_organization_email_template_dto import PageDtoOrganizationEmailTemplateDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = email_template_api.EmailTemplateApi(api_client)

    # example passing only optional values
    query_params = {
        'type': "type_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List email templates
        api_response = api_instance.list_org_email_templates(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EmailTemplateApi->list_org_email_templates: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_org_email_templates.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#list_org_email_templates.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#list_org_email_templates.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#list_org_email_templates.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_org_email_templates.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#list_org_email_templates.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#list_org_email_templates.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#list_org_email_templates.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#list_org_email_templates.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#list_org_email_templates.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#list_org_email_templates.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#list_org_email_templates.ApiResponseFor501) | Not implemented

#### list_org_email_templates.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoOrganizationEmailTemplateDto**](../../models/PageDtoOrganizationEmailTemplateDto.md) |  | 


#### list_org_email_templates.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_org_email_templates.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_org_email_templates.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_org_email_templates.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_org_email_templates.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_org_email_templates.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_org_email_templates.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_org_email_templates.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_org_email_templates.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_org_email_templates.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### list_org_email_templates.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

