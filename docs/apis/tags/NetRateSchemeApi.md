<a id="__pageTop"></a>
# openapi_client.apis.tags.net_rate_scheme_api.NetRateSchemeApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_discount_scheme**](#create_discount_scheme) | **post** /api2/v1/netRateSchemes | Create net rate scheme
[**edit_discount_scheme_workflow_step**](#edit_discount_scheme_workflow_step) | **put** /api2/v1/netRateSchemes/{netRateSchemeUid}/workflowStepNetSchemes/{netRateSchemeWorkflowStepId} | Edit scheme for workflow step
[**get_discount_scheme**](#get_discount_scheme) | **get** /api2/v1/netRateSchemes/{netRateSchemeUid} | Get net rate scheme
[**get_discount_scheme_workflow_step**](#get_discount_scheme_workflow_step) | **get** /api2/v1/netRateSchemes/{netRateSchemeUid}/workflowStepNetSchemes/{netRateSchemeWorkflowStepId} | Get scheme for workflow step
[**get_discount_scheme_workflow_steps**](#get_discount_scheme_workflow_steps) | **get** /api2/v1/netRateSchemes/{netRateSchemeUid}/workflowStepNetSchemes | List schemes for workflow step
[**get_discount_schemes**](#get_discount_schemes) | **get** /api2/v1/netRateSchemes | List net rate schemes
[**update_discount_scheme**](#update_discount_scheme) | **put** /api2/v1/netRateSchemes/{netRateSchemeUid} | Edit net rate scheme

# **create_discount_scheme**
<a id="create_discount_scheme"></a>
> NetRateScheme create_discount_scheme()

Create net rate scheme

### Example

```python
import openapi_client
from openapi_client.apis.tags import net_rate_scheme_api
from openapi_client.model.discount_scheme_create_dto import DiscountSchemeCreateDto
from openapi_client.model.net_rate_scheme import NetRateScheme
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = net_rate_scheme_api.NetRateSchemeApi(api_client)

    # example passing only optional values
    body = DiscountSchemeCreateDto(
        name="name_example",
        rates=DiscountSettingsDto(
            repetition=3.14,
            tm101=3.14,
            tm100=3.14,
            tm95=3.14,
            tm85=3.14,
            tm75=3.14,
            tm50=3.14,
            tm0=3.14,
            mt100=3.14,
            mt95=3.14,
            mt85=3.14,
            mt75=3.14,
            mt50=3.14,
            mt0=3.14,
            nt100=3.14,
            nt99=3.14,
            nt85=3.14,
            nt75=3.14,
            nt50=3.14,
            nt0=3.14,
            if100=3.14,
            if95=3.14,
            if85=3.14,
            if75=3.14,
            if50=3.14,
            if0=3.14,
        ),
        workflow_step_net_schemes=[
            NetRateSchemeWorkflowStepCreate(
                workflow_step=IdReference(
                    id="id_example",
                ),
                rates=DiscountSettingsDto(),
            )
        ],
    )
    try:
        # Create net rate scheme
        api_response = api_instance.create_discount_scheme(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetRateSchemeApi->create_discount_scheme: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DiscountSchemeCreateDto**](../../models/DiscountSchemeCreateDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_discount_scheme.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_discount_scheme.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_discount_scheme.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#create_discount_scheme.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_discount_scheme.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#create_discount_scheme.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#create_discount_scheme.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#create_discount_scheme.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#create_discount_scheme.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#create_discount_scheme.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#create_discount_scheme.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#create_discount_scheme.ApiResponseFor501) | Not implemented

#### create_discount_scheme.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetRateScheme**](../../models/NetRateScheme.md) |  | 


#### create_discount_scheme.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_discount_scheme.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_discount_scheme.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_discount_scheme.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_discount_scheme.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_discount_scheme.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_discount_scheme.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_discount_scheme.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_discount_scheme.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_discount_scheme.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### create_discount_scheme.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_discount_scheme_workflow_step**
<a id="edit_discount_scheme_workflow_step"></a>
> NetRateSchemeWorkflowStep edit_discount_scheme_workflow_step(net_rate_scheme_uidnet_rate_scheme_workflow_step_id)

Edit scheme for workflow step

### Example

```python
import openapi_client
from openapi_client.apis.tags import net_rate_scheme_api
from openapi_client.model.net_rate_scheme_workflow_step import NetRateSchemeWorkflowStep
from openapi_client.model.net_rate_scheme_workflow_step_edit import NetRateSchemeWorkflowStepEdit
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = net_rate_scheme_api.NetRateSchemeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'netRateSchemeUid': "netRateSchemeUid_example",
        'netRateSchemeWorkflowStepId': 1,
    }
    try:
        # Edit scheme for workflow step
        api_response = api_instance.edit_discount_scheme_workflow_step(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetRateSchemeApi->edit_discount_scheme_workflow_step: %s\n" % e)

    # example passing only optional values
    path_params = {
        'netRateSchemeUid': "netRateSchemeUid_example",
        'netRateSchemeWorkflowStepId': 1,
    }
    body = NetRateSchemeWorkflowStepEdit(
        rates=DiscountSettingsDto(
            repetition=3.14,
            tm101=3.14,
            tm100=3.14,
            tm95=3.14,
            tm85=3.14,
            tm75=3.14,
            tm50=3.14,
            tm0=3.14,
            mt100=3.14,
            mt95=3.14,
            mt85=3.14,
            mt75=3.14,
            mt50=3.14,
            mt0=3.14,
            nt100=3.14,
            nt99=3.14,
            nt85=3.14,
            nt75=3.14,
            nt50=3.14,
            nt0=3.14,
            if100=3.14,
            if95=3.14,
            if85=3.14,
            if75=3.14,
            if50=3.14,
            if0=3.14,
        ),
    )
    try:
        # Edit scheme for workflow step
        api_response = api_instance.edit_discount_scheme_workflow_step(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetRateSchemeApi->edit_discount_scheme_workflow_step: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**NetRateSchemeWorkflowStepEdit**](../../models/NetRateSchemeWorkflowStepEdit.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
netRateSchemeUid | NetRateSchemeUidSchema | | 
netRateSchemeWorkflowStepId | NetRateSchemeWorkflowStepIdSchema | | 

# NetRateSchemeUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NetRateSchemeWorkflowStepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_discount_scheme_workflow_step.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#edit_discount_scheme_workflow_step.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#edit_discount_scheme_workflow_step.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#edit_discount_scheme_workflow_step.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_discount_scheme_workflow_step.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#edit_discount_scheme_workflow_step.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#edit_discount_scheme_workflow_step.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#edit_discount_scheme_workflow_step.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#edit_discount_scheme_workflow_step.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#edit_discount_scheme_workflow_step.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#edit_discount_scheme_workflow_step.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#edit_discount_scheme_workflow_step.ApiResponseFor501) | Not implemented

#### edit_discount_scheme_workflow_step.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetRateSchemeWorkflowStep**](../../models/NetRateSchemeWorkflowStep.md) |  | 


#### edit_discount_scheme_workflow_step.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_discount_scheme_workflow_step.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_discount_scheme_workflow_step.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_discount_scheme_workflow_step.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_discount_scheme_workflow_step.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_discount_scheme_workflow_step.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_discount_scheme_workflow_step.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_discount_scheme_workflow_step.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_discount_scheme_workflow_step.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_discount_scheme_workflow_step.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### edit_discount_scheme_workflow_step.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_discount_scheme**
<a id="get_discount_scheme"></a>
> NetRateScheme get_discount_scheme(net_rate_scheme_uid)

Get net rate scheme

### Example

```python
import openapi_client
from openapi_client.apis.tags import net_rate_scheme_api
from openapi_client.model.net_rate_scheme import NetRateScheme
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = net_rate_scheme_api.NetRateSchemeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'netRateSchemeUid': "netRateSchemeUid_example",
    }
    try:
        # Get net rate scheme
        api_response = api_instance.get_discount_scheme(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetRateSchemeApi->get_discount_scheme: %s\n" % e)
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
netRateSchemeUid | NetRateSchemeUidSchema | | 

# NetRateSchemeUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_discount_scheme.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_discount_scheme.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_discount_scheme.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_discount_scheme.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_discount_scheme.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_discount_scheme.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_discount_scheme.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_discount_scheme.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_discount_scheme.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_discount_scheme.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_discount_scheme.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_discount_scheme.ApiResponseFor501) | Not implemented

#### get_discount_scheme.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetRateScheme**](../../models/NetRateScheme.md) |  | 


#### get_discount_scheme.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_discount_scheme_workflow_step**
<a id="get_discount_scheme_workflow_step"></a>
> NetRateSchemeWorkflowStep get_discount_scheme_workflow_step(net_rate_scheme_uidnet_rate_scheme_workflow_step_id)

Get scheme for workflow step

### Example

```python
import openapi_client
from openapi_client.apis.tags import net_rate_scheme_api
from openapi_client.model.net_rate_scheme_workflow_step import NetRateSchemeWorkflowStep
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = net_rate_scheme_api.NetRateSchemeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'netRateSchemeUid': "netRateSchemeUid_example",
        'netRateSchemeWorkflowStepId': 1,
    }
    try:
        # Get scheme for workflow step
        api_response = api_instance.get_discount_scheme_workflow_step(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetRateSchemeApi->get_discount_scheme_workflow_step: %s\n" % e)
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
netRateSchemeUid | NetRateSchemeUidSchema | | 
netRateSchemeWorkflowStepId | NetRateSchemeWorkflowStepIdSchema | | 

# NetRateSchemeUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NetRateSchemeWorkflowStepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_discount_scheme_workflow_step.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_discount_scheme_workflow_step.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_discount_scheme_workflow_step.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_discount_scheme_workflow_step.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_discount_scheme_workflow_step.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_discount_scheme_workflow_step.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_discount_scheme_workflow_step.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_discount_scheme_workflow_step.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_discount_scheme_workflow_step.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_discount_scheme_workflow_step.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_discount_scheme_workflow_step.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_discount_scheme_workflow_step.ApiResponseFor501) | Not implemented

#### get_discount_scheme_workflow_step.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetRateSchemeWorkflowStep**](../../models/NetRateSchemeWorkflowStep.md) |  | 


#### get_discount_scheme_workflow_step.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_step.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_step.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_step.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_step.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_step.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_step.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_step.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_step.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_step.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_step.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_discount_scheme_workflow_steps**
<a id="get_discount_scheme_workflow_steps"></a>
> PageDtoNetRateSchemeWorkflowStepReference get_discount_scheme_workflow_steps(net_rate_scheme_uid)

List schemes for workflow step

### Example

```python
import openapi_client
from openapi_client.apis.tags import net_rate_scheme_api
from openapi_client.model.page_dto_net_rate_scheme_workflow_step_reference import PageDtoNetRateSchemeWorkflowStepReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = net_rate_scheme_api.NetRateSchemeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'netRateSchemeUid': "netRateSchemeUid_example",
    }
    query_params = {
    }
    try:
        # List schemes for workflow step
        api_response = api_instance.get_discount_scheme_workflow_steps(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetRateSchemeApi->get_discount_scheme_workflow_steps: %s\n" % e)

    # example passing only optional values
    path_params = {
        'netRateSchemeUid': "netRateSchemeUid_example",
    }
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List schemes for workflow step
        api_response = api_instance.get_discount_scheme_workflow_steps(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetRateSchemeApi->get_discount_scheme_workflow_steps: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
netRateSchemeUid | NetRateSchemeUidSchema | | 

# NetRateSchemeUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_discount_scheme_workflow_steps.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_discount_scheme_workflow_steps.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_discount_scheme_workflow_steps.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_discount_scheme_workflow_steps.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_discount_scheme_workflow_steps.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_discount_scheme_workflow_steps.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_discount_scheme_workflow_steps.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_discount_scheme_workflow_steps.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_discount_scheme_workflow_steps.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_discount_scheme_workflow_steps.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_discount_scheme_workflow_steps.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_discount_scheme_workflow_steps.ApiResponseFor501) | Not implemented

#### get_discount_scheme_workflow_steps.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoNetRateSchemeWorkflowStepReference**](../../models/PageDtoNetRateSchemeWorkflowStepReference.md) |  | 


#### get_discount_scheme_workflow_steps.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_steps.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_steps.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_steps.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_steps.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_steps.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_steps.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_steps.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_steps.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_steps.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_scheme_workflow_steps.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_discount_schemes**
<a id="get_discount_schemes"></a>
> PageDtoNetRateSchemeReference get_discount_schemes()

List net rate schemes

### Example

```python
import openapi_client
from openapi_client.apis.tags import net_rate_scheme_api
from openapi_client.model.page_dto_net_rate_scheme_reference import PageDtoNetRateSchemeReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = net_rate_scheme_api.NetRateSchemeApi(api_client)

    # example passing only optional values
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List net rate schemes
        api_response = api_instance.get_discount_schemes(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetRateSchemeApi->get_discount_schemes: %s\n" % e)
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
pageNumber | PageNumberSchema | | optional
pageSize | PageSizeSchema | | optional


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
200 | [ApiResponseFor200](#get_discount_schemes.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_discount_schemes.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_discount_schemes.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#get_discount_schemes.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_discount_schemes.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#get_discount_schemes.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#get_discount_schemes.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#get_discount_schemes.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#get_discount_schemes.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#get_discount_schemes.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#get_discount_schemes.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#get_discount_schemes.ApiResponseFor501) | Not implemented

#### get_discount_schemes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageDtoNetRateSchemeReference**](../../models/PageDtoNetRateSchemeReference.md) |  | 


#### get_discount_schemes.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_schemes.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_schemes.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_schemes.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_schemes.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_schemes.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_schemes.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_schemes.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_schemes.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_schemes.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### get_discount_schemes.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_discount_scheme**
<a id="update_discount_scheme"></a>
> NetRateScheme update_discount_scheme(net_rate_scheme_uid)

Edit net rate scheme

### Example

```python
import openapi_client
from openapi_client.apis.tags import net_rate_scheme_api
from openapi_client.model.net_rate_scheme_edit import NetRateSchemeEdit
from openapi_client.model.net_rate_scheme import NetRateScheme
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = net_rate_scheme_api.NetRateSchemeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'netRateSchemeUid': "netRateSchemeUid_example",
    }
    try:
        # Edit net rate scheme
        api_response = api_instance.update_discount_scheme(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetRateSchemeApi->update_discount_scheme: %s\n" % e)

    # example passing only optional values
    path_params = {
        'netRateSchemeUid': "netRateSchemeUid_example",
    }
    body = NetRateSchemeEdit(
        name="name_example",
        rates=DiscountSettingsDto(
            repetition=3.14,
            tm101=3.14,
            tm100=3.14,
            tm95=3.14,
            tm85=3.14,
            tm75=3.14,
            tm50=3.14,
            tm0=3.14,
            mt100=3.14,
            mt95=3.14,
            mt85=3.14,
            mt75=3.14,
            mt50=3.14,
            mt0=3.14,
            nt100=3.14,
            nt99=3.14,
            nt85=3.14,
            nt75=3.14,
            nt50=3.14,
            nt0=3.14,
            if100=3.14,
            if95=3.14,
            if85=3.14,
            if75=3.14,
            if50=3.14,
            if0=3.14,
        ),
    )
    try:
        # Edit net rate scheme
        api_response = api_instance.update_discount_scheme(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetRateSchemeApi->update_discount_scheme: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetRateSchemeEdit**](../../models/NetRateSchemeEdit.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
netRateSchemeUid | NetRateSchemeUidSchema | | 

# NetRateSchemeUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_discount_scheme.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#update_discount_scheme.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#update_discount_scheme.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#update_discount_scheme.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_discount_scheme.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#update_discount_scheme.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#update_discount_scheme.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#update_discount_scheme.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#update_discount_scheme.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#update_discount_scheme.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#update_discount_scheme.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#update_discount_scheme.ApiResponseFor501) | Not implemented

#### update_discount_scheme.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetRateScheme**](../../models/NetRateScheme.md) |  | 


#### update_discount_scheme.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_discount_scheme.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_discount_scheme.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_discount_scheme.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_discount_scheme.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_discount_scheme.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_discount_scheme.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_discount_scheme.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_discount_scheme.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_discount_scheme.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### update_discount_scheme.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

