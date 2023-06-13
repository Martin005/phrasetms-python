<a id="__pageTop"></a>

# phrasetms_client.apis.tags.machine_translation_settings_api.MachineTranslationSettingsApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                            | HTTP request                                                              | Description                                 |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------- |
| [**get_list**](#get_list)                                         | **get** /api2/v1/machineTranslateSettings                                 | List machine translate settings             |
| [**get_mt_settings**](#get_mt_settings)                           | **get** /api2/v1/machineTranslateSettings/{mtsUid}                        | Get machine translate settings              |
| [**get_mt_types**](#get_mt_types)                                 | **get** /api2/v1/machineTranslateSettings/types                           | Get machine translate settings types        |
| [**get_status**](#get_status)                                     | **get** /api2/v1/machineTranslateSettings/{mtsUid}/status                 | Get status of machine translate engine      |
| [**get_third_party_engines_list**](#get_third_party_engines_list) | **get** /api2/v1/machineTranslateSettings/thirdPartyEngines               | List third party machine translate settings |
| [**get_translation_resources**](#get_translation_resources)       | **get** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources | Get translation resources                   |

# **get_list**

<a id="get_list"></a>

> PageDtoMachineTranslateSettingsPbmDto get_list()

List machine translate settings

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import machine_translation_settings_api
from phrasetms_client.model.page_dto_machine_translate_settings_pbm_dto import PageDtoMachineTranslateSettingsPbmDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = machine_translation_settings_api.MachineTranslationSettingsApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'pageNumber': 0,
        'pageSize': 50,
        'sort': "NAME",
        'order': "asc",
    }
    try:
        # List machine translate settings
        api_response = api_instance.get_list(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling MachineTranslationSettingsApi->get_list: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name       | Type             | Description | Notes    |
| ---------- | ---------------- | ----------- | -------- |
| name       | NameSchema       |             | optional |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |
| sort       | SortSchema       |             | optional |
| order      | OrderSchema      |             | optional |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PageNumberSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 0value must be a 32 bit integer |

# PageSizeSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                                |
| --------------------- | ---------------- | ----------- | ------------------------------------------------------------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 50value must be a 32 bit integer |

# SortSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                |
| ---------- | ------------- | ----------- | ------------------------------------------------------------------------------------ |
| str,       | str,          |             | must be one of ["NAME", ] if omitted the server will use the default value of "NAME" |

# OrderSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| str,       | str,          |             | if omitted the server will use the default value of "asc" |

### Return Types, Responses

| Code | Class                                            | Description                                                 |
| ---- | ------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization     | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_list.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_list.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_list.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_list.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_list.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_list.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_list.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_list.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_list.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_list.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_list.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_list.ApiResponseFor501) | Not implemented                                             |

#### get_list.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                                               | Description | Notes |
| -------------------------------------------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoMachineTranslateSettingsPbmDto**](../../models/PageDtoMachineTranslateSettingsPbmDto.md) |             |

#### get_list.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_mt_settings**

<a id="get_mt_settings"></a>

> MachineTranslateSettingsPbmDto get_mt_settings(mts_uid)

Get machine translate settings

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import machine_translation_settings_api
from phrasetms_client.model.machine_translate_settings_pbm_dto import MachineTranslateSettingsPbmDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = machine_translation_settings_api.MachineTranslationSettingsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'mtsUid': "mtsUid_example",
    }
    try:
        # Get machine translate settings
        api_response = api_instance.get_mt_settings(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling MachineTranslationSettingsApi->get_mt_settings: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name   | Type         | Description | Notes |
| ------ | ------------ | ----------- | ----- |
| mtsUid | MtsUidSchema |             |

# MtsUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_mt_settings.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_mt_settings.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_mt_settings.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_mt_settings.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_mt_settings.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_mt_settings.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_mt_settings.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_mt_settings.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_mt_settings.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_mt_settings.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_mt_settings.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_mt_settings.ApiResponseFor501) | Not implemented                                             |

#### get_mt_settings.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**MachineTranslateSettingsPbmDto**](../../models/MachineTranslateSettingsPbmDto.md) |             |

#### get_mt_settings.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_settings.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_settings.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_settings.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_settings.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_settings.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_settings.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_settings.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_settings.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_settings.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_settings.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_mt_types**

<a id="get_mt_types"></a>

> TypesDto get_mt_types()

Get machine translate settings types

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import machine_translation_settings_api
from phrasetms_client.model.types_dto import TypesDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = machine_translation_settings_api.MachineTranslationSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get machine translate settings types
        api_response = api_instance.get_mt_types()
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling MachineTranslationSettingsApi->get_mt_types: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_mt_types.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_mt_types.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_mt_types.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_mt_types.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_mt_types.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_mt_types.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_mt_types.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_mt_types.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_mt_types.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_mt_types.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_mt_types.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_mt_types.ApiResponseFor501) | Not implemented                                             |

#### get_mt_types.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                     | Description | Notes |
| ---------------------------------------- | ----------- | ----- |
| [**TypesDto**](../../models/TypesDto.md) |             |

#### get_mt_types.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_types.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_types.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_types.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_types.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_types.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_types.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_types.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_types.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_types.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_mt_types.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_status**

<a id="get_status"></a>

> MachineTranslateStatusDto get_status(mts_uid)

Get status of machine translate engine

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import machine_translation_settings_api
from phrasetms_client.model.machine_translate_status_dto import MachineTranslateStatusDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = machine_translation_settings_api.MachineTranslationSettingsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'mtsUid': "mtsUid_example",
    }
    try:
        # Get status of machine translate engine
        api_response = api_instance.get_status(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling MachineTranslationSettingsApi->get_status: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name   | Type         | Description | Notes |
| ------ | ------------ | ----------- | ----- |
| mtsUid | MtsUidSchema |             |

# MtsUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                              | Description                                                 |
| ---- | -------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization       | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_status.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_status.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_status.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_status.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_status.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_status.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_status.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_status.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_status.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_status.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_status.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_status.ApiResponseFor501) | Not implemented                                             |

#### get_status.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**MachineTranslateStatusDto**](../../models/MachineTranslateStatusDto.md) |             |

#### get_status.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_status.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_status.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_status.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_status.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_status.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_status.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_status.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_status.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_status.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_status.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_third_party_engines_list**

<a id="get_third_party_engines_list"></a>

> PageDtoMachineTranslateSettingsPbmDto get_third_party_engines_list()

List third party machine translate settings

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import machine_translation_settings_api
from phrasetms_client.model.page_dto_machine_translate_settings_pbm_dto import PageDtoMachineTranslateSettingsPbmDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = machine_translation_settings_api.MachineTranslationSettingsApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'pageNumber': 0,
        'pageSize': 50,
        'sort': "NAME",
        'order': "asc",
    }
    try:
        # List third party machine translate settings
        api_response = api_instance.get_third_party_engines_list(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling MachineTranslationSettingsApi->get_third_party_engines_list: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name       | Type             | Description | Notes    |
| ---------- | ---------------- | ----------- | -------- |
| name       | NameSchema       |             | optional |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |
| sort       | SortSchema       |             | optional |
| order      | OrderSchema      |             | optional |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# PageNumberSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 0value must be a 32 bit integer |

# PageSizeSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                                |
| --------------------- | ---------------- | ----------- | ------------------------------------------------------------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 50value must be a 32 bit integer |

# SortSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                                                |
| ---------- | ------------- | ----------- | ------------------------------------------------------------------------------------ |
| str,       | str,          |             | must be one of ["NAME", ] if omitted the server will use the default value of "NAME" |

# OrderSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| str,       | str,          |             | if omitted the server will use the default value of "asc" |

### Return Types, Responses

| Code | Class                                                                | Description                                                 |
| ---- | -------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_third_party_engines_list.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_third_party_engines_list.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_third_party_engines_list.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_third_party_engines_list.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_third_party_engines_list.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_third_party_engines_list.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_third_party_engines_list.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_third_party_engines_list.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_third_party_engines_list.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_third_party_engines_list.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_third_party_engines_list.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_third_party_engines_list.ApiResponseFor501) | Not implemented                                             |

#### get_third_party_engines_list.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                                               | Description | Notes |
| -------------------------------------------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoMachineTranslateSettingsPbmDto**](../../models/PageDtoMachineTranslateSettingsPbmDto.md) |             |

#### get_third_party_engines_list.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_third_party_engines_list.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_third_party_engines_list.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_third_party_engines_list.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_third_party_engines_list.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_third_party_engines_list.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_third_party_engines_list.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_third_party_engines_list.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_third_party_engines_list.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_third_party_engines_list.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_third_party_engines_list.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_translation_resources**

<a id="get_translation_resources"></a>

> TranslationResourcesDto get_translation_resources(project_uidjob_uid)

Get translation resources

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import machine_translation_settings_api
from phrasetms_client.model.translation_resources_dto import TranslationResourcesDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = machine_translation_settings_api.MachineTranslationSettingsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUid': "projectUid_example",
        'jobUid': "jobUid_example",
    }
    try:
        # Get translation resources
        api_response = api_instance.get_translation_resources(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling MachineTranslationSettingsApi->get_translation_resources: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name       | Type             | Description | Notes |
| ---------- | ---------------- | ----------- | ----- |
| projectUid | ProjectUidSchema |             |
| jobUid     | JobUidSchema     |             |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                             | Description                                                 |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_translation_resources.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_translation_resources.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_translation_resources.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_translation_resources.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_translation_resources.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_translation_resources.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_translation_resources.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_translation_resources.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_translation_resources.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_translation_resources.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_translation_resources.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_translation_resources.ApiResponseFor501) | Not implemented                                             |

#### get_translation_resources.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationResourcesDto**](../../models/TranslationResourcesDto.md) |             |

#### get_translation_resources.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_translation_resources.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
