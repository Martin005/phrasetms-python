<a id="__pageTop"></a>

# phrasetms_client.apis.tags.quote_api.QuoteApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                  | HTTP request                          | Description  |
| --------------------------------------- | ------------------------------------- | ------------ |
| [**create_quote_v2**](#create_quote_v2) | **post** /api2/v2/quotes              | Create quote |
| [**delete_quote**](#delete_quote)       | **delete** /api2/v1/quotes/{quoteUid} | Delete quote |
| [**email_quotes**](#email_quotes)       | **post** /api2/v1/quotes/email        | Email quotes |
| [**get2**](#get2)                       | **get** /api2/v1/quotes/{quoteUid}    | Get quote    |

# **create_quote_v2**

<a id="create_quote_v2"></a>

> QuoteV2Dto create_quote_v2()

Create quote

Either WorkflowSettings or Units must be sent for billingUnit \"Hour\".

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import quote_api
from phrasetms_client.model.quote_create_v2_dto import QuoteCreateV2Dto
from phrasetms_client.model.quote_v2_dto import QuoteV2Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quote_api.QuoteApi(api_client)

    # example passing only optional values
    body = QuoteCreateV2Dto(
        name="name_example",
        project=UidReference(
            uid="uid_example",
        ),
        analyse=IdReference(
            id="id_example",
        ),
,
,
        provider=ProviderReference(),
        workflow_settings=[
            QuoteWorkflowSettingDto(
                workflow_step=IdReference(),
                units=[
                    QuoteUnitsDto(
                        analyse_language_part=IdReference(),
                        value=0,
                    )
                ],
            )
        ],
        units=[
            QuoteUnitsDto()
        ],
        additional_steps=[
            "additional_steps_example"
        ],
    )
    try:
        # Create quote
        api_response = api_instance.create_quote_v2(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling QuoteApi->create_quote_v2: %s\n" % e)
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

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**QuoteCreateV2Dto**](../../models/QuoteCreateV2Dto.md) |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_quote_v2.ApiResponseFor201) | successful operation                                        |
| 400  | [ApiResponseFor400](#create_quote_v2.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_quote_v2.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_quote_v2.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_quote_v2.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_quote_v2.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_quote_v2.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_quote_v2.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_quote_v2.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_quote_v2.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_quote_v2.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_quote_v2.ApiResponseFor501) | Not implemented                                             |

#### create_quote_v2.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                         | Description | Notes |
| -------------------------------------------- | ----------- | ----- |
| [**QuoteV2Dto**](../../models/QuoteV2Dto.md) |             |

#### create_quote_v2.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_quote_v2.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_quote_v2.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_quote_v2.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_quote_v2.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_quote_v2.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_quote_v2.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_quote_v2.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_quote_v2.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_quote_v2.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_quote_v2.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_quote**

<a id="delete_quote"></a>

> delete_quote(quote_uid)

Delete quote

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import quote_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quote_api.QuoteApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'quoteUid': "quoteUid_example",
    }
    try:
        # Delete quote
        api_response = api_instance.delete_quote(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling QuoteApi->delete_quote: %s\n" % e)
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

| Name     | Type           | Description | Notes |
| -------- | -------------- | ----------- | ----- |
| quoteUid | QuoteUidSchema |             |

# QuoteUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_quote.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_quote.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_quote.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_quote.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_quote.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_quote.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_quote.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_quote.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_quote.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_quote.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_quote.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_quote.ApiResponseFor501) | Not implemented                                             |

#### delete_quote.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_quote.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **email_quotes**

<a id="email_quotes"></a>

> EmailQuotesResponseDto email_quotes()

Email quotes

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import quote_api
from phrasetms_client.model.email_quotes_request_dto import EmailQuotesRequestDto
from phrasetms_client.model.email_quotes_response_dto import EmailQuotesResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quote_api.QuoteApi(api_client)

    # example passing only optional values
    body = EmailQuotesRequestDto(
        quotes=[
            UidReference(
                uid="uid_example",
            )
        ],
        subject="subject_example",
        body="body_example",
        cc="cc_example",
        bcc="bcc_example",
    )
    try:
        # Email quotes
        api_response = api_instance.email_quotes(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling QuoteApi->email_quotes: %s\n" % e)
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

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**EmailQuotesRequestDto**](../../models/EmailQuotesRequestDto.md) |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#email_quotes.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#email_quotes.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#email_quotes.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#email_quotes.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#email_quotes.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#email_quotes.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#email_quotes.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#email_quotes.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#email_quotes.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#email_quotes.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#email_quotes.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#email_quotes.ApiResponseFor501) | Not implemented                                             |

#### email_quotes.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**EmailQuotesResponseDto**](../../models/EmailQuotesResponseDto.md) |             |

#### email_quotes.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### email_quotes.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### email_quotes.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### email_quotes.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### email_quotes.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### email_quotes.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### email_quotes.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### email_quotes.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### email_quotes.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### email_quotes.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### email_quotes.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get2**

<a id="get2"></a>

> QuoteDto get2(quote_uid)

Get quote

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import quote_api
from phrasetms_client.model.quote_dto import QuoteDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quote_api.QuoteApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'quoteUid': "quoteUid_example",
    }
    try:
        # Get quote
        api_response = api_instance.get2(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling QuoteApi->get2: %s\n" % e)
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

| Name     | Type           | Description | Notes |
| -------- | -------------- | ----------- | ----- |
| quoteUid | QuoteUidSchema |             |

# QuoteUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                        | Description                                                 |
| ---- | -------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get2.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get2.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get2.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get2.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get2.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get2.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get2.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get2.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get2.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get2.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get2.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get2.ApiResponseFor501) | Not implemented                                             |

#### get2.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                     | Description | Notes |
| ---------------------------------------- | ----------- | ----- |
| [**QuoteDto**](../../models/QuoteDto.md) |             |

#### get2.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get2.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get2.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get2.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get2.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get2.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get2.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get2.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get2.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get2.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get2.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
