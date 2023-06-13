<a id="__pageTop"></a>
# openapi_client.apis.tags.machine_translation_api.MachineTranslationApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**machine_translation**](#machine_translation) | **post** /api2/v1/machineTranslations/{mtSettingsUid}/translate | Translate with MT

# **machine_translation**
<a id="machine_translation"></a>
> MachineTranslateResponse machine_translation(mt_settings_uid)

Translate with MT

### Example

```python
import openapi_client
from openapi_client.apis.tags import machine_translation_api
from openapi_client.model.translation_request_extended_dto import TranslationRequestExtendedDto
from openapi_client.model.machine_translate_response import MachineTranslateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = machine_translation_api.MachineTranslationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'mtSettingsUid': "mtSettingsUid_example",
    }
    try:
        # Translate with MT
        api_response = api_instance.machine_translation(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MachineTranslationApi->machine_translation: %s\n" % e)

    # example passing only optional values
    path_params = {
        'mtSettingsUid': "mtSettingsUid_example",
    }
    body = TranslationRequestExtendedDto(
        source_texts=[
            "source_texts_example"
        ],
        _from="_from_example",
        to="to_example",
        filename="filename_example",
    )
    try:
        # Translate with MT
        api_response = api_instance.machine_translation(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MachineTranslationApi->machine_translation: %s\n" % e)
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
[**TranslationRequestExtendedDto**](../../models/TranslationRequestExtendedDto.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
mtSettingsUid | MtSettingsUidSchema | | 

# MtSettingsUidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#machine_translation.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#machine_translation.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#machine_translation.ApiResponseFor401) | Not authorized
403 | [ApiResponseFor403](#machine_translation.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#machine_translation.ApiResponseFor404) | Resource not found
405 | [ApiResponseFor405](#machine_translation.ApiResponseFor405) | Method not allowed
408 | [ApiResponseFor408](#machine_translation.ApiResponseFor408) | Timeout
410 | [ApiResponseFor410](#machine_translation.ApiResponseFor410) | Gone
415 | [ApiResponseFor415](#machine_translation.ApiResponseFor415) | Unsupported media type
429 | [ApiResponseFor429](#machine_translation.ApiResponseFor429) | Too many requests
500 | [ApiResponseFor500](#machine_translation.ApiResponseFor500) | Internal server error
501 | [ApiResponseFor501](#machine_translation.ApiResponseFor501) | Not implemented

#### machine_translation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MachineTranslateResponse**](../../models/MachineTranslateResponse.md) |  | 


#### machine_translation.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### machine_translation.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

