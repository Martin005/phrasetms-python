<a id="__pageTop"></a>

# phrasetms_client.apis.tags.authentication_api.AuthenticationApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                                      | HTTP request                                       | Description                    |
| --------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------ |
| [**login**](#login)                                                         | **post** /api2/v1/auth/login                       | Login                          |
| [**login1**](#login1)                                                       | **post** /api2/v3/auth/login                       | Login                          |
| [**login_by_apple_with_code**](#login_by_apple_with_code)                   | **post** /api2/v1/auth/loginWithApple/code         | Login with Apple with code     |
| [**login_by_apple_with_refresh_token**](#login_by_apple_with_refresh_token) | **post** /api2/v1/auth/loginWithApple/refreshToken | Login with Apple refresh token |
| [**login_by_google**](#login_by_google)                                     | **post** /api2/v1/auth/loginWithGoogle             | Login with Google              |
| [**login_other**](#login_other)                                             | **post** /api2/v1/auth/loginOther                  | Login as another user          |
| [**login_other1**](#login_other1)                                           | **post** /api2/v3/auth/loginOther                  | Login as another user          |
| [**login_to_session**](#login_to_session)                                   | **post** /api2/v1/auth/loginToSession              | Login to session               |
| [**login_to_session2**](#login_to_session2)                                 | **post** /api2/v3/auth/loginToSession              | Login to session               |
| [**logout**](#logout)                                                       | **post** /api2/v1/auth/logout                      | Logout                         |
| [**refresh_apple_token**](#refresh_apple_token)                             | **get** /api2/v1/auth/refreshAppleToken            | refresh apple token            |
| [**who_am_i**](#who_am_i)                                                   | **get** /api2/v1/auth/whoAmI                       | Who am I                       |

# **login**

<a id="login"></a>

> LoginResponseDto login()

Login

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.login_response_dto import LoginResponseDto
from phrasetms_client.model.login_dto import LoginDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    body = LoginDto(
        user_name="user_name_example",
        password="password_example",
        code="code_example",
    )
    try:
        # Login
        api_response = api_instance.login(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
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

| Type                                     | Description | Notes |
| ---------------------------------------- | ----------- | ----- |
| [**LoginDto**](../../models/LoginDto.md) |             |

### Return Types, Responses

| Code | Class                                         | Description                                                 |
| ---- | --------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization  | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#login.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#login.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#login.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#login.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#login.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#login.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#login.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#login.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#login.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#login.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#login.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#login.ApiResponseFor501) | Not implemented                                             |

#### login.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**LoginResponseDto**](../../models/LoginResponseDto.md) |             |

#### login.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **login1**

<a id="login1"></a>

> LoginResponseV3Dto login1()

Login

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.login_response_v3_dto import LoginResponseV3Dto
from phrasetms_client.model.login_v3_dto import LoginV3Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    body = LoginV3Dto(
        user_uid="user_uid_example",
        user_name="user_name_example",
        password="password_example",
        code="code_example",
    )
    try:
        # Login
        api_response = api_instance.login1(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->login1: %s\n" % e)
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

| Type                                         | Description | Notes |
| -------------------------------------------- | ----------- | ----- |
| [**LoginV3Dto**](../../models/LoginV3Dto.md) |             |

### Return Types, Responses

| Code | Class                                          | Description                                                 |
| ---- | ---------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#login1.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#login1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#login1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#login1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#login1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#login1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#login1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#login1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#login1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#login1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#login1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#login1.ApiResponseFor501) | Not implemented                                             |

#### login1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**LoginResponseV3Dto**](../../models/LoginResponseV3Dto.md) |             |

#### login1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **login_by_apple_with_code**

<a id="login_by_apple_with_code"></a>

> LoginResponseDto login_by_apple_with_code()

Login with Apple with code

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.login_response_dto import LoginResponseDto
from phrasetms_client.model.login_with_apple_dto import LoginWithAppleDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    query_params = {
        'native': True,
    }
    body = LoginWithAppleDto(
        code_or_refresh_token="code_or_refresh_token_example",
    )
    try:
        # Login with Apple with code
        api_response = api_instance.login_by_apple_with_code(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->login_by_apple_with_code: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                             | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset              |
| query_params         | RequestQueryParams                                       |                                         |
| content_type         | str                                                      | optional, default is 'application/json' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )       | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                        | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                         | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                        | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationJson

| Type                                                       | Description | Notes |
| ---------------------------------------------------------- | ----------- | ----- |
| [**LoginWithAppleDto**](../../models/LoginWithAppleDto.md) |             |

### query_params

#### RequestQueryParams

| Name   | Type         | Description | Notes    |
| ------ | ------------ | ----------- | -------- |
| native | NativeSchema |             | optional |

# NativeSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| bool,      | BoolClass,    |             |

### Return Types, Responses

| Code | Class                                                            | Description                                                 |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                     | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#login_by_apple_with_code.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#login_by_apple_with_code.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#login_by_apple_with_code.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#login_by_apple_with_code.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#login_by_apple_with_code.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#login_by_apple_with_code.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#login_by_apple_with_code.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#login_by_apple_with_code.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#login_by_apple_with_code.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#login_by_apple_with_code.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#login_by_apple_with_code.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#login_by_apple_with_code.ApiResponseFor501) | Not implemented                                             |

#### login_by_apple_with_code.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**LoginResponseDto**](../../models/LoginResponseDto.md) |             |

#### login_by_apple_with_code.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_code.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_code.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_code.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_code.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_code.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_code.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_code.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_code.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_code.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_code.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **login_by_apple_with_refresh_token**

<a id="login_by_apple_with_refresh_token"></a>

> LoginResponseDto login_by_apple_with_refresh_token()

Login with Apple refresh token

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.login_response_dto import LoginResponseDto
from phrasetms_client.model.login_with_apple_dto import LoginWithAppleDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    body = LoginWithAppleDto(
        code_or_refresh_token="code_or_refresh_token_example",
    )
    try:
        # Login with Apple refresh token
        api_response = api_instance.login_by_apple_with_refresh_token(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->login_by_apple_with_refresh_token: %s\n" % e)
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
| [**LoginWithAppleDto**](../../models/LoginWithAppleDto.md) |             |

### Return Types, Responses

| Code | Class                                                                     | Description                                                 |
| ---- | ------------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#login_by_apple_with_refresh_token.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#login_by_apple_with_refresh_token.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#login_by_apple_with_refresh_token.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#login_by_apple_with_refresh_token.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#login_by_apple_with_refresh_token.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#login_by_apple_with_refresh_token.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#login_by_apple_with_refresh_token.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#login_by_apple_with_refresh_token.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#login_by_apple_with_refresh_token.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#login_by_apple_with_refresh_token.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#login_by_apple_with_refresh_token.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#login_by_apple_with_refresh_token.ApiResponseFor501) | Not implemented                                             |

#### login_by_apple_with_refresh_token.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**LoginResponseDto**](../../models/LoginResponseDto.md) |             |

#### login_by_apple_with_refresh_token.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_refresh_token.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_refresh_token.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_refresh_token.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_refresh_token.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_refresh_token.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_refresh_token.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_refresh_token.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_refresh_token.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_refresh_token.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_apple_with_refresh_token.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **login_by_google**

<a id="login_by_google"></a>

> LoginResponseDto login_by_google()

Login with Google

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.login_response_dto import LoginResponseDto
from phrasetms_client.model.login_with_google_dto import LoginWithGoogleDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    body = LoginWithGoogleDto(
        id_token="id_token_example",
    )
    try:
        # Login with Google
        api_response = api_instance.login_by_google(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->login_by_google: %s\n" % e)
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

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**LoginWithGoogleDto**](../../models/LoginWithGoogleDto.md) |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#login_by_google.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#login_by_google.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#login_by_google.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#login_by_google.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#login_by_google.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#login_by_google.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#login_by_google.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#login_by_google.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#login_by_google.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#login_by_google.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#login_by_google.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#login_by_google.ApiResponseFor501) | Not implemented                                             |

#### login_by_google.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**LoginResponseDto**](../../models/LoginResponseDto.md) |             |

#### login_by_google.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_google.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_google.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_google.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_google.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_google.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_google.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_google.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_google.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_google.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_by_google.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **login_other**

<a id="login_other"></a>

> LoginResponseDto login_other()

Login as another user

Available only for admin

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.login_other_dto import LoginOtherDto
from phrasetms_client.model.login_response_dto import LoginResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    body = LoginOtherDto(
        user_name="user_name_example",
    )
    try:
        # Login as another user
        api_response = api_instance.login_other(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->login_other: %s\n" % e)
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

| Type                                               | Description | Notes |
| -------------------------------------------------- | ----------- | ----- |
| [**LoginOtherDto**](../../models/LoginOtherDto.md) |             |

### Return Types, Responses

| Code | Class                                               | Description                                                 |
| ---- | --------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization        | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#login_other.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#login_other.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#login_other.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#login_other.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#login_other.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#login_other.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#login_other.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#login_other.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#login_other.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#login_other.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#login_other.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#login_other.ApiResponseFor501) | Not implemented                                             |

#### login_other.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**LoginResponseDto**](../../models/LoginResponseDto.md) |             |

#### login_other.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **login_other1**

<a id="login_other1"></a>

> LoginResponseV3Dto login_other1()

Login as another user

Available only for admin

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.login_response_v3_dto import LoginResponseV3Dto
from phrasetms_client.model.login_other_v3_dto import LoginOtherV3Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    body = LoginOtherV3Dto(
        user_uid="user_uid_example",
        user_name="user_name_example",
    )
    try:
        # Login as another user
        api_response = api_instance.login_other1(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->login_other1: %s\n" % e)
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

| Type                                                   | Description | Notes |
| ------------------------------------------------------ | ----------- | ----- |
| [**LoginOtherV3Dto**](../../models/LoginOtherV3Dto.md) |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#login_other1.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#login_other1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#login_other1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#login_other1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#login_other1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#login_other1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#login_other1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#login_other1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#login_other1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#login_other1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#login_other1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#login_other1.ApiResponseFor501) | Not implemented                                             |

#### login_other1.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**LoginResponseV3Dto**](../../models/LoginResponseV3Dto.md) |             |

#### login_other1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_other1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **login_to_session**

<a id="login_to_session"></a>

> LoginToSessionResponseDto login_to_session()

Login to session

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.login_to_session_response_dto import LoginToSessionResponseDto
from phrasetms_client.model.login_to_session_dto import LoginToSessionDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    body = LoginToSessionDto(
        user_name="user_name_example",
        password="password_example",
        remember_me=True,
    )
    try:
        # Login to session
        api_response = api_instance.login_to_session(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->login_to_session: %s\n" % e)
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
| [**LoginToSessionDto**](../../models/LoginToSessionDto.md) |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#login_to_session.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#login_to_session.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#login_to_session.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#login_to_session.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#login_to_session.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#login_to_session.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#login_to_session.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#login_to_session.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#login_to_session.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#login_to_session.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#login_to_session.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#login_to_session.ApiResponseFor501) | Not implemented                                             |

#### login_to_session.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**LoginToSessionResponseDto**](../../models/LoginToSessionResponseDto.md) |             |

#### login_to_session.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **login_to_session2**

<a id="login_to_session2"></a>

> LoginToSessionResponseV3Dto login_to_session2()

Login to session

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.login_to_session_response_v3_dto import LoginToSessionResponseV3Dto
from phrasetms_client.model.login_to_session_v3_dto import LoginToSessionV3Dto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    body = LoginToSessionV3Dto(
        user_uid="user_uid_example",
        user_name="user_name_example",
        password="password_example",
        remember_me=True,
        two_factor_code=1,
        captcha_code="captcha_code_example",
    )
    try:
        # Login to session
        api_response = api_instance.login_to_session2(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->login_to_session2: %s\n" % e)
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

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**LoginToSessionV3Dto**](../../models/LoginToSessionV3Dto.md) |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#login_to_session2.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#login_to_session2.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#login_to_session2.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#login_to_session2.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#login_to_session2.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#login_to_session2.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#login_to_session2.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#login_to_session2.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#login_to_session2.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#login_to_session2.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#login_to_session2.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#login_to_session2.ApiResponseFor501) | Not implemented                                             |

#### login_to_session2.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------ | ----------- | ----- |
| [**LoginToSessionResponseV3Dto**](../../models/LoginToSessionResponseV3Dto.md) |             |

#### login_to_session2.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session2.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session2.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session2.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session2.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session2.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session2.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session2.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session2.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session2.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_to_session2.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **logout**

<a id="logout"></a>

> logout()

Logout

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    query_params = {
        'token': "token_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Logout
        api_response = api_instance.logout(
            query_params=query_params,
            header_params=header_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```

### Parameters

| Name                 | Type                                             | Description      | Notes                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query_params         | RequestQueryParams                               |                  |
| header_params        | RequestHeaderParams                              |                  |
| stream               | bool                                             | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]] | default is None  | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                             | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### query_params

#### RequestQueryParams

| Name  | Type        | Description | Notes    |
| ----- | ----------- | ----------- | -------- |
| token | TokenSchema |             | optional |

# TokenSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### header_params

#### RequestHeaderParams

| Name          | Type                | Description | Notes    |
| ------------- | ------------------- | ----------- | -------- |
| Authorization | AuthorizationSchema |             | optional |

# AuthorizationSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                          | Description                                                 |
| ---- | ---------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization   | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#logout.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#logout.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#logout.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#logout.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#logout.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#logout.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#logout.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#logout.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#logout.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#logout.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#logout.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#logout.ApiResponseFor501) | Not implemented                                             |

#### logout.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### logout.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **refresh_apple_token**

<a id="refresh_apple_token"></a>

> AppleTokenResponseDto refresh_apple_token()

refresh apple token

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.apple_token_response_dto import AppleTokenResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example passing only optional values
    query_params = {
        'token': "token_example",
    }
    try:
        # refresh apple token
        api_response = api_instance.refresh_apple_token(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->refresh_apple_token: %s\n" % e)
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

| Name  | Type        | Description | Notes    |
| ----- | ----------- | ----------- | -------- |
| token | TokenSchema |             | optional |

# TokenSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#refresh_apple_token.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#refresh_apple_token.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#refresh_apple_token.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#refresh_apple_token.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#refresh_apple_token.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#refresh_apple_token.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#refresh_apple_token.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#refresh_apple_token.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#refresh_apple_token.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#refresh_apple_token.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#refresh_apple_token.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#refresh_apple_token.ApiResponseFor501) | Not implemented                                             |

#### refresh_apple_token.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**AppleTokenResponseDto**](../../models/AppleTokenResponseDto.md) |             |

#### refresh_apple_token.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### refresh_apple_token.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### refresh_apple_token.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### refresh_apple_token.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### refresh_apple_token.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### refresh_apple_token.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### refresh_apple_token.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### refresh_apple_token.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### refresh_apple_token.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### refresh_apple_token.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### refresh_apple_token.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **who_am_i**

<a id="who_am_i"></a>

> LoginUserDto who_am_i()

Who am I

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import authentication_api
from phrasetms_client.model.login_user_dto import LoginUserDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Who am I
        api_response = api_instance.who_am_i()
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling AuthenticationApi->who_am_i: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return Types, Responses

| Code | Class                                            | Description                                                 |
| ---- | ------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization     | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#who_am_i.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#who_am_i.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#who_am_i.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#who_am_i.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#who_am_i.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#who_am_i.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#who_am_i.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#who_am_i.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#who_am_i.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#who_am_i.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#who_am_i.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#who_am_i.ApiResponseFor501) | Not implemented                                             |

#### who_am_i.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                             | Description | Notes |
| ------------------------------------------------ | ----------- | ----- |
| [**LoginUserDto**](../../models/LoginUserDto.md) |             |

#### who_am_i.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### who_am_i.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### who_am_i.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### who_am_i.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### who_am_i.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### who_am_i.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### who_am_i.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### who_am_i.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### who_am_i.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### who_am_i.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### who_am_i.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
