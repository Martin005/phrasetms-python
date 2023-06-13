<a id="__pageTop"></a>

# phrasetms_client.apis.tags.price_list_api.PriceListApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                                | HTTP request                                                                              | Description           |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------- |
| [**create_language_pair**](#create_language_pair)                     | **post** /api2/v1/priceLists/{priceListUid}/priceSets                                     | Add language pairs    |
| [**create_price_list**](#create_price_list)                           | **post** /api2/v1/priceLists                                                              | Create price list     |
| [**delete_language_pair**](#delete_language_pair)                     | **delete** /api2/v1/priceLists/{priceListUid}/priceSets/{sourceLanguage}/{targetLanguage} | Remove language pair  |
| [**delete_language_pairs**](#delete_language_pairs)                   | **delete** /api2/v1/priceLists/{priceListUid}/priceSets                                   | Remove language pairs |
| [**delete_price_list**](#delete_price_list)                           | **delete** /api2/v1/priceLists/{priceListUid}                                             | Delete price list     |
| [**get_list_of_price_list**](#get_list_of_price_list)                 | **get** /api2/v1/priceLists                                                               | List price lists      |
| [**get_price_list**](#get_price_list)                                 | **get** /api2/v1/priceLists/{priceListUid}                                                | Get price list        |
| [**get_prices_with_workflow_steps**](#get_prices_with_workflow_steps) | **get** /api2/v1/priceLists/{priceListUid}/priceSets                                      | List price sets       |
| [**set_minimum_price_for_set**](#set_minimum_price_for_set)           | **post** /api2/v1/priceLists/{priceListUid}/priceSets/minimumPrices                       | Edit minimum prices   |
| [**set_prices**](#set_prices)                                         | **post** /api2/v1/priceLists/{priceListUid}/priceSets/prices                              | Edit prices           |
| [**update_price_list**](#update_price_list)                           | **put** /api2/v1/priceLists/{priceListUid}                                                | Update price list     |

# **create_language_pair**

<a id="create_language_pair"></a>

> TranslationPriceSetListDto create_language_pair(price_list_uid)

Add language pairs

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from phrasetms_client.model.translation_price_set_list_dto import TranslationPriceSetListDto
from phrasetms_client.model.translation_price_set_create_dto import TranslationPriceSetCreateDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    try:
        # Add language pairs
        api_response = api_instance.create_language_pair(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->create_language_pair: %s\n" % e)

    # example passing only optional values
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    body = TranslationPriceSetCreateDto(
        source_languages=[
            "source_languages_example"
        ],
,
    )
    try:
        # Add language pairs
        api_response = api_instance.create_language_pair(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->create_language_pair: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceSetCreateDto**](../../models/TranslationPriceSetCreateDto.md) |             |

### path_params

#### RequestPathParams

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| priceListUid | PriceListUidSchema |             |

# PriceListUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_language_pair.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_language_pair.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_language_pair.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_language_pair.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_language_pair.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_language_pair.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_language_pair.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_language_pair.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_language_pair.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_language_pair.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_language_pair.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_language_pair.ApiResponseFor501) | Not implemented                                             |

#### create_language_pair.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceSetListDto**](../../models/TranslationPriceSetListDto.md) |             |

#### create_language_pair.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_language_pair.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_language_pair.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_language_pair.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_language_pair.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_language_pair.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_language_pair.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_language_pair.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_language_pair.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_language_pair.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_language_pair.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_price_list**

<a id="create_price_list"></a>

> TranslationPriceListDto create_price_list()

Create price list

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from phrasetms_client.model.translation_price_list_create_dto import TranslationPriceListCreateDto
from phrasetms_client.model.translation_price_list_dto import TranslationPriceListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only optional values
    body = TranslationPriceListCreateDto(
        name="name_example",
        currency_code="currency_code_example",
        billing_unit="Word",
    )
    try:
        # Create price list
        api_response = api_instance.create_price_list(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->create_price_list: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceListCreateDto**](../../models/TranslationPriceListCreateDto.md) |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_price_list.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_price_list.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_price_list.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_price_list.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_price_list.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_price_list.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_price_list.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_price_list.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_price_list.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_price_list.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_price_list.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_price_list.ApiResponseFor501) | Not implemented                                             |

#### create_price_list.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceListDto**](../../models/TranslationPriceListDto.md) |             |

#### create_price_list.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_price_list.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_price_list.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_price_list.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_price_list.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_price_list.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_price_list.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_price_list.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_price_list.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_price_list.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_price_list.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_language_pair**

<a id="delete_language_pair"></a>

> delete_language_pair(price_list_uidsource_languagetarget_language)

Remove language pair

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'priceListUid': "priceListUid_example",
        'sourceLanguage': "sourceLanguage_example",
        'targetLanguage': "targetLanguage_example",
    }
    try:
        # Remove language pair
        api_response = api_instance.delete_language_pair(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->delete_language_pair: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| priceListUid   | PriceListUidSchema   |             |
| sourceLanguage | SourceLanguageSchema |             |
| targetLanguage | TargetLanguageSchema |             |

# PriceListUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# SourceLanguageSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# TargetLanguageSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_language_pair.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_language_pair.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_language_pair.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_language_pair.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_language_pair.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_language_pair.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_language_pair.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_language_pair.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_language_pair.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_language_pair.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_language_pair.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_language_pair.ApiResponseFor501) | Not implemented                                             |

#### delete_language_pair.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pair.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_language_pairs**

<a id="delete_language_pairs"></a>

> delete_language_pairs(price_list_uid)

Remove language pairs

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from phrasetms_client.model.translation_price_set_bulk_delete_dto import TranslationPriceSetBulkDeleteDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    try:
        # Remove language pairs
        api_response = api_instance.delete_language_pairs(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->delete_language_pairs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    body = TranslationPriceSetBulkDeleteDto(
        source_languages=[
            "source_languages_example"
        ],
,
    )
    try:
        # Remove language pairs
        api_response = api_instance.delete_language_pairs(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->delete_language_pairs: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                     | Description | Notes |
| ---------------------------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceSetBulkDeleteDto**](../../models/TranslationPriceSetBulkDeleteDto.md) |             |

### path_params

#### RequestPathParams

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| priceListUid | PriceListUidSchema |             |

# PriceListUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                         | Description                                                 |
| ---- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                  | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_language_pairs.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_language_pairs.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_language_pairs.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_language_pairs.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_language_pairs.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_language_pairs.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_language_pairs.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_language_pairs.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_language_pairs.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_language_pairs.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_language_pairs.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_language_pairs.ApiResponseFor501) | Not implemented                                             |

#### delete_language_pairs.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_language_pairs.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_price_list**

<a id="delete_price_list"></a>

> delete_price_list(price_list_uid)

Delete price list

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    try:
        # Delete price list
        api_response = api_instance.delete_price_list(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->delete_price_list: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path_params          | RequestPathParams                                |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### path_params

#### RequestPathParams

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| priceListUid | PriceListUidSchema |             |

# PriceListUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_price_list.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_price_list.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_price_list.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_price_list.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_price_list.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_price_list.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_price_list.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_price_list.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_price_list.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_price_list.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_price_list.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_price_list.ApiResponseFor501) | Not implemented                                             |

#### delete_price_list.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_price_list.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_list_of_price_list**

<a id="get_list_of_price_list"></a>

> PageDtoTranslationPriceListDto get_list_of_price_list()

List price lists

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from phrasetms_client.model.page_dto_translation_price_list_dto import PageDtoTranslationPriceListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only optional values
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List price lists
        api_response = api_instance.get_list_of_price_list(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->get_list_of_price_list: %s\n" % e)
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
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |

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

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_list_of_price_list.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_list_of_price_list.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_list_of_price_list.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_list_of_price_list.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_list_of_price_list.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_list_of_price_list.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_list_of_price_list.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_list_of_price_list.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_list_of_price_list.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_list_of_price_list.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_list_of_price_list.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_list_of_price_list.ApiResponseFor501) | Not implemented                                             |

#### get_list_of_price_list.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                                 | Description | Notes |
| ------------------------------------------------------------------------------------ | ----------- | ----- |
| [**PageDtoTranslationPriceListDto**](../../models/PageDtoTranslationPriceListDto.md) |             |

#### get_list_of_price_list.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_price_list.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_price_list.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_price_list.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_price_list.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_price_list.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_price_list.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_price_list.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_price_list.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_price_list.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_price_list.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_price_list**

<a id="get_price_list"></a>

> TranslationPriceListDto get_price_list(price_list_uid)

Get price list

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from phrasetms_client.model.translation_price_list_dto import TranslationPriceListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    try:
        # Get price list
        api_response = api_instance.get_price_list(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->get_price_list: %s\n" % e)
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

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| priceListUid | PriceListUidSchema |             |

# PriceListUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_price_list.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_price_list.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_price_list.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_price_list.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_price_list.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_price_list.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_price_list.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_price_list.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_price_list.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_price_list.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_price_list.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_price_list.ApiResponseFor501) | Not implemented                                             |

#### get_price_list.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceListDto**](../../models/TranslationPriceListDto.md) |             |

#### get_price_list.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_price_list.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_price_list.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_price_list.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_price_list.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_price_list.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_price_list.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_price_list.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_price_list.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_price_list.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_price_list.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_prices_with_workflow_steps**

<a id="get_prices_with_workflow_steps"></a>

> PageDtoTranslationPriceSetDto get_prices_with_workflow_steps(price_list_uid)

List price sets

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from phrasetms_client.model.page_dto_translation_price_set_dto import PageDtoTranslationPriceSetDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    query_params = {
    }
    try:
        # List price sets
        api_response = api_instance.get_prices_with_workflow_steps(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->get_prices_with_workflow_steps: %s\n" % e)

    # example passing only optional values
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    query_params = {
        'pageNumber': 0,
        'pageSize': 50,
        'sourceLanguages': [
        "sourceLanguages_example"
    ],
        'targetLanguages': [
        "targetLanguages_example"
    ],
    }
    try:
        # List price sets
        api_response = api_instance.get_prices_with_workflow_steps(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->get_prices_with_workflow_steps: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description                       | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                                   |
| path_params          | RequestPathParams                                |                                   |
| accept_content_types | typing.Tuple[str]                                | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                             | default is False                  | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None                   | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False                  | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name            | Type                  | Description | Notes    |
| --------------- | --------------------- | ----------- | -------- |
| pageNumber      | PageNumberSchema      |             | optional |
| pageSize        | PageSizeSchema        |             | optional |
| sourceLanguages | SourceLanguagesSchema |             | optional |
| targetLanguages | TargetLanguagesSchema |             | optional |

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

# SourceLanguagesSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# TargetLanguagesSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

### path_params

#### RequestPathParams

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| priceListUid | PriceListUidSchema |             |

# PriceListUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                                  | Description                                                 |
| ---- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_prices_with_workflow_steps.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_prices_with_workflow_steps.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_prices_with_workflow_steps.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_prices_with_workflow_steps.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_prices_with_workflow_steps.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_prices_with_workflow_steps.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_prices_with_workflow_steps.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_prices_with_workflow_steps.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_prices_with_workflow_steps.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_prices_with_workflow_steps.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_prices_with_workflow_steps.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_prices_with_workflow_steps.ApiResponseFor501) | Not implemented                                             |

#### get_prices_with_workflow_steps.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoTranslationPriceSetDto**](../../models/PageDtoTranslationPriceSetDto.md) |             |

#### get_prices_with_workflow_steps.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prices_with_workflow_steps.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prices_with_workflow_steps.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prices_with_workflow_steps.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prices_with_workflow_steps.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prices_with_workflow_steps.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prices_with_workflow_steps.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prices_with_workflow_steps.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prices_with_workflow_steps.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prices_with_workflow_steps.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_prices_with_workflow_steps.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_minimum_price_for_set**

<a id="set_minimum_price_for_set"></a>

> TranslationPriceListDto set_minimum_price_for_set(price_list_uid)

Edit minimum prices

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from phrasetms_client.model.translation_price_list_dto import TranslationPriceListDto
from phrasetms_client.model.translation_price_set_bulk_minimum_prices_dto import TranslationPriceSetBulkMinimumPricesDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    try:
        # Edit minimum prices
        api_response = api_instance.set_minimum_price_for_set(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->set_minimum_price_for_set: %s\n" % e)

    # example passing only optional values
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    body = TranslationPriceSetBulkMinimumPricesDto(
        source_languages=[
            "source_languages_example"
        ],
,
        minimum_price=3.14,
    )
    try:
        # Edit minimum prices
        api_response = api_instance.set_minimum_price_for_set(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->set_minimum_price_for_set: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                                   | Description | Notes |
| ------------------------------------------------------------------------------------------------------ | ----------- | ----- |
| [**TranslationPriceSetBulkMinimumPricesDto**](../../models/TranslationPriceSetBulkMinimumPricesDto.md) |             |

### path_params

#### RequestPathParams

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| priceListUid | PriceListUidSchema |             |

# PriceListUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                             | Description                                                 |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#set_minimum_price_for_set.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#set_minimum_price_for_set.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#set_minimum_price_for_set.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#set_minimum_price_for_set.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#set_minimum_price_for_set.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#set_minimum_price_for_set.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#set_minimum_price_for_set.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#set_minimum_price_for_set.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#set_minimum_price_for_set.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#set_minimum_price_for_set.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#set_minimum_price_for_set.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#set_minimum_price_for_set.ApiResponseFor501) | Not implemented                                             |

#### set_minimum_price_for_set.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceListDto**](../../models/TranslationPriceListDto.md) |             |

#### set_minimum_price_for_set.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_minimum_price_for_set.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_minimum_price_for_set.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_minimum_price_for_set.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_minimum_price_for_set.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_minimum_price_for_set.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_minimum_price_for_set.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_minimum_price_for_set.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_minimum_price_for_set.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_minimum_price_for_set.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_minimum_price_for_set.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_prices**

<a id="set_prices"></a>

> TranslationPriceListDto set_prices(price_list_uid)

Edit prices

If object contains only price, all languages and workflow steps will be updated

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from phrasetms_client.model.translation_price_set_bulk_prices_dto import TranslationPriceSetBulkPricesDto
from phrasetms_client.model.translation_price_list_dto import TranslationPriceListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    try:
        # Edit prices
        api_response = api_instance.set_prices(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->set_prices: %s\n" % e)

    # example passing only optional values
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    body = TranslationPriceSetBulkPricesDto(
        source_languages=[
            "source_languages_example"
        ],
,
        price=3.14,
        workflow_steps=[
            IdReference(
                id="id_example",
            )
        ],
    )
    try:
        # Edit prices
        api_response = api_instance.set_prices(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->set_prices: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                                     | Description | Notes |
| ---------------------------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceSetBulkPricesDto**](../../models/TranslationPriceSetBulkPricesDto.md) |             |

### path_params

#### RequestPathParams

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| priceListUid | PriceListUidSchema |             |

# PriceListUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                              | Description                                                 |
| ---- | -------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization       | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#set_prices.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#set_prices.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#set_prices.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#set_prices.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#set_prices.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#set_prices.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#set_prices.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#set_prices.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#set_prices.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#set_prices.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#set_prices.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#set_prices.ApiResponseFor501) | Not implemented                                             |

#### set_prices.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceListDto**](../../models/TranslationPriceListDto.md) |             |

#### set_prices.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_prices.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_prices.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_prices.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_prices.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_prices.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_prices.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_prices.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_prices.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_prices.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### set_prices.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_price_list**

<a id="update_price_list"></a>

> TranslationPriceListDto update_price_list(price_list_uid)

Update price list

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import price_list_api
from phrasetms_client.model.translation_price_list_create_dto import TranslationPriceListCreateDto
from phrasetms_client.model.translation_price_list_dto import TranslationPriceListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    try:
        # Update price list
        api_response = api_instance.update_price_list(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->update_price_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'priceListUid': "priceListUid_example",
    }
    body = TranslationPriceListCreateDto(
        name="name_example",
        currency_code="currency_code_example",
        billing_unit="Word",
    )
    try:
        # Update price list
        api_response = api_instance.update_price_list(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling PriceListApi->update_price_list: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| path_params          | RequestPathParams                                        |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                                               | Description | Notes |
| ---------------------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceListCreateDto**](../../models/TranslationPriceListCreateDto.md) |             |

### path_params

#### RequestPathParams

| Name         | Type               | Description | Notes |
| ------------ | ------------------ | ----------- | ----- |
| priceListUid | PriceListUidSchema |             |

# PriceListUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#update_price_list.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#update_price_list.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_price_list.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_price_list.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_price_list.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_price_list.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_price_list.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_price_list.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_price_list.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_price_list.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_price_list.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_price_list.ApiResponseFor501) | Not implemented                                             |

#### update_price_list.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**TranslationPriceListDto**](../../models/TranslationPriceListDto.md) |             |

#### update_price_list.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_price_list.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_price_list.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_price_list.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_price_list.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_price_list.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_price_list.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_price_list.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_price_list.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_price_list.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_price_list.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
