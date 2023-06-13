<a id="__pageTop"></a>

# phrasetms_client.apis.tags.spell_check_api.SpellCheckApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                            | HTTP request                                | Description            |
| --------------------------------- | ------------------------------------------- | ---------------------- |
| [**add_word**](#add_word)         | **post** /api2/v1/spellCheck/words          | Add word to dictionary |
| [**check**](#check)               | **post** /api2/v1/spellCheck/check          | Spell check            |
| [**check_by_job**](#check_by_job) | **post** /api2/v1/spellCheck/check/{jobUid} | Spell check for job    |
| [**suggest**](#suggest)           | **post** /api2/v1/spellCheck/suggest        | Suggest a word         |

# **add_word**

<a id="add_word"></a>

> add_word()

Add word to dictionary

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import spell_check_api
from phrasetms_client.model.dictionary_item_dto import DictionaryItemDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spell_check_api.SpellCheckApi(api_client)

    # example passing only optional values
    body = DictionaryItemDto(
        lang="lang_example",
        word="word_example",
    )
    try:
        # Add word to dictionary
        api_response = api_instance.add_word(
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling SpellCheckApi->add_word: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**DictionaryItemDto**](../../models/DictionaryItemDto.md) |             |

### Return Types, Responses

| Code | Class                                            | Description                                                 |
| ---- | ------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization     | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#add_word.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#add_word.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#add_word.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#add_word.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#add_word.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#add_word.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#add_word.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#add_word.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#add_word.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#add_word.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#add_word.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#add_word.ApiResponseFor501) | Not implemented                                             |

#### add_word.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_word.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **check**

<a id="check"></a>

> SpellCheckResponseDto check()

Spell check

Spell check using the settings of the user's organization

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import spell_check_api
from phrasetms_client.model.spell_check_response_dto import SpellCheckResponseDto
from phrasetms_client.model.spell_check_request_dto import SpellCheckRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spell_check_api.SpellCheckApi(api_client)

    # example passing only optional values
    body = SpellCheckRequestDto(
        lang="lang_example",
        texts=[
            "texts_example"
        ],
,
        zero_length_separator="zero_length_separator_example",
    )
    try:
        # Spell check
        api_response = api_instance.check(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SpellCheckApi->check: %s\n" % e)
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

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**SpellCheckRequestDto**](../../models/SpellCheckRequestDto.md) |             |

### Return Types, Responses

| Code | Class                                         | Description                                                 |
| ---- | --------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization  | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#check.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#check.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#check.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#check.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#check.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#check.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#check.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#check.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#check.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#check.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#check.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#check.ApiResponseFor501) | Not implemented                                             |

#### check.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**SpellCheckResponseDto**](../../models/SpellCheckResponseDto.md) |             |

#### check.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **check_by_job**

<a id="check_by_job"></a>

> SpellCheckResponseDto check_by_job(job_uid)

Spell check for job

Spell check using the settings from the project of the job

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import spell_check_api
from phrasetms_client.model.spell_check_response_dto import SpellCheckResponseDto
from phrasetms_client.model.spell_check_request_dto import SpellCheckRequestDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spell_check_api.SpellCheckApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
    }
    try:
        # Spell check for job
        api_response = api_instance.check_by_job(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SpellCheckApi->check_by_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
    }
    body = SpellCheckRequestDto(
        lang="lang_example",
        texts=[
            "texts_example"
        ],
,
        zero_length_separator="zero_length_separator_example",
    )
    try:
        # Spell check for job
        api_response = api_instance.check_by_job(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SpellCheckApi->check_by_job: %s\n" % e)
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

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**SpellCheckRequestDto**](../../models/SpellCheckRequestDto.md) |             |

### path_params

#### RequestPathParams

| Name   | Type         | Description | Notes |
| ------ | ------------ | ----------- | ----- |
| jobUid | JobUidSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#check_by_job.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#check_by_job.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#check_by_job.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#check_by_job.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#check_by_job.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#check_by_job.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#check_by_job.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#check_by_job.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#check_by_job.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#check_by_job.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#check_by_job.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#check_by_job.ApiResponseFor501) | Not implemented                                             |

#### check_by_job.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**SpellCheckResponseDto**](../../models/SpellCheckResponseDto.md) |             |

#### check_by_job.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check_by_job.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check_by_job.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check_by_job.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check_by_job.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check_by_job.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check_by_job.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check_by_job.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check_by_job.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check_by_job.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### check_by_job.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **suggest**

<a id="suggest"></a>

> SuggestResponseDto suggest()

Suggest a word

Spell check suggest using the users's spell check dictionary

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import spell_check_api
from phrasetms_client.model.suggest_request_dto import SuggestRequestDto
from phrasetms_client.model.suggest_response_dto import SuggestResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spell_check_api.SpellCheckApi(api_client)

    # example passing only optional values
    body = SuggestRequestDto(
        lang="lang_example",
        words=[
            "words_example"
        ],
,
    )
    try:
        # Suggest a word
        api_response = api_instance.suggest(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SpellCheckApi->suggest: %s\n" % e)
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

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**SuggestRequestDto**](../../models/SuggestRequestDto.md) |             |

### Return Types, Responses

| Code | Class                                           | Description                                                 |
| ---- | ----------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization    | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#suggest.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#suggest.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#suggest.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#suggest.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#suggest.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#suggest.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#suggest.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#suggest.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#suggest.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#suggest.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#suggest.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#suggest.ApiResponseFor501) | Not implemented                                             |

#### suggest.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**SuggestResponseDto**](../../models/SuggestResponseDto.md) |             |

#### suggest.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### suggest.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### suggest.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### suggest.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### suggest.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### suggest.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### suggest.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### suggest.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### suggest.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### suggest.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### suggest.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
