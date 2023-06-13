<a id="__pageTop"></a>

# phrasetms_client.apis.tags.user_api.UserApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                        | HTTP request                                            | Description                       |
| ------------------------------------------------------------- | ------------------------------------------------------- | --------------------------------- |
| [**cancel_deletion**](#cancel_deletion)                       | **post** /api2/v1/users/{userUid}/undelete              | Restore user                      |
| [**create_user_v3**](#create_user_v3)                         | **post** /api2/v3/users                                 | Create user                       |
| [**delete_user1**](#delete_user1)                             | **delete** /api2/v1/users/{userUid}                     | Delete user                       |
| [**disable_two_factor_auth_v3**](#disable_two_factor_auth_v3) | **post** /api2/v3/users/{userUid}/disableTwoFactorAuth  | Disable two-factor authentication |
| [**get_list_of_users_filtered**](#get_list_of_users_filtered) | **get** /api2/v1/users                                  | List users                        |
| [**get_user_v3**](#get_user_v3)                               | **get** /api2/v3/users/{userUid}                        | Get user                          |
| [**list_assigned_projects**](#list_assigned_projects)         | **get** /api2/v1/users/{userUid}/projects               | List assigned projects            |
| [**list_jobs**](#list_jobs)                                   | **get** /api2/v1/users/{userUid}/jobs                   | List assigned jobs                |
| [**list_target_langs**](#list_target_langs)                   | **get** /api2/v1/users/{userUid}/targetLangs            | List assigned target languages    |
| [**list_workflow_steps**](#list_workflow_steps)               | **get** /api2/v1/users/{userUid}/workflowSteps          | List assigned workflow steps      |
| [**login_activity**](#login_activity)                         | **get** /api2/v1/users/{userUid}/loginStatistics        | Login statistics                  |
| [**send_login_info**](#send_login_info)                       | **post** /api2/v1/users/{userUid}/emailLoginInformation | Send login information            |
| [**update_password**](#update_password)                       | **post** /api2/v1/users/{userUid}/updatePassword        | Update password                   |
| [**update_user_v3**](#update_user_v3)                         | **put** /api2/v3/users/{userUid}                        | Edit user                         |
| [**user_last_logins**](#user_last_logins)                     | **get** /api2/v1/users/lastLogins                       | List last login dates             |

# **cancel_deletion**

<a id="cancel_deletion"></a>

> UserDto cancel_deletion(user_uid)

Restore user

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.user_dto import UserDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    try:
        # Restore user
        api_response = api_instance.cancel_deletion(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->cancel_deletion: %s\n" % e)
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

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#cancel_deletion.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#cancel_deletion.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#cancel_deletion.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#cancel_deletion.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#cancel_deletion.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#cancel_deletion.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#cancel_deletion.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#cancel_deletion.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#cancel_deletion.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#cancel_deletion.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#cancel_deletion.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#cancel_deletion.ApiResponseFor501) | Not implemented                                             |

#### cancel_deletion.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                   | Description | Notes |
| -------------------------------------- | ----------- | ----- |
| [**UserDto**](../../models/UserDto.md) |             |

#### cancel_deletion.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### cancel_deletion.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### cancel_deletion.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### cancel_deletion.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### cancel_deletion.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### cancel_deletion.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### cancel_deletion.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### cancel_deletion.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### cancel_deletion.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### cancel_deletion.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### cancel_deletion.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_user_v3**

<a id="create_user_v3"></a>

> UserDetailsDtoV3 create_user_v3()

Create user

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.user_details_dto_v3 import UserDetailsDtoV3
from phrasetms_client.model.abstract_user_create_dto import AbstractUserCreateDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only optional values
    body = AbstractUserCreateDto()
    try:
        # Create user
        api_response = api_instance.create_user_v3(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->create_user_v3: %s\n" % e)
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
| [**AbstractUserCreateDto**](../../models/AbstractUserCreateDto.md) |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_user_v3.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_user_v3.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_user_v3.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_user_v3.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_user_v3.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_user_v3.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_user_v3.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_user_v3.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_user_v3.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_user_v3.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_user_v3.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_user_v3.ApiResponseFor501) | Not implemented                                             |

#### create_user_v3.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**UserDetailsDtoV3**](../../models/UserDetailsDtoV3.md) |             |

#### create_user_v3.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_user_v3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_user_v3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_user_v3.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_user_v3.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_user_v3.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_user_v3.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_user_v3.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_user_v3.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_user_v3.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_user_v3.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_user1**

<a id="delete_user1"></a>

> delete_user1(user_uid)

Delete user

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    try:
        # Delete user
        api_response = api_instance.delete_user1(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->delete_user1: %s\n" % e)
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

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                | Description                                                 |
| ---- | ---------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization         | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_user1.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_user1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_user1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_user1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_user1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_user1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_user1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_user1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_user1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_user1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_user1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_user1.ApiResponseFor501) | Not implemented                                             |

#### delete_user1.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_user1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **disable_two_factor_auth_v3**

<a id="disable_two_factor_auth_v3"></a>

> UserDetailsDtoV3 disable_two_factor_auth_v3(user_uid)

Disable two-factor authentication

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.user_details_dto_v3 import UserDetailsDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    try:
        # Disable two-factor authentication
        api_response = api_instance.disable_two_factor_auth_v3(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->disable_two_factor_auth_v3: %s\n" % e)
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

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                              | Description                                                 |
| ---- | ------------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                       | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#disable_two_factor_auth_v3.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#disable_two_factor_auth_v3.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#disable_two_factor_auth_v3.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#disable_two_factor_auth_v3.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#disable_two_factor_auth_v3.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#disable_two_factor_auth_v3.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#disable_two_factor_auth_v3.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#disable_two_factor_auth_v3.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#disable_two_factor_auth_v3.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#disable_two_factor_auth_v3.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#disable_two_factor_auth_v3.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#disable_two_factor_auth_v3.ApiResponseFor501) | Not implemented                                             |

#### disable_two_factor_auth_v3.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**UserDetailsDtoV3**](../../models/UserDetailsDtoV3.md) |             |

#### disable_two_factor_auth_v3.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_two_factor_auth_v3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_two_factor_auth_v3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_two_factor_auth_v3.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_two_factor_auth_v3.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_two_factor_auth_v3.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_two_factor_auth_v3.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_two_factor_auth_v3.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_two_factor_auth_v3.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_two_factor_auth_v3.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### disable_two_factor_auth_v3.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_list_of_users_filtered**

<a id="get_list_of_users_filtered"></a>

> PageDtoUserDto get_list_of_users_filtered()

List users

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.page_dto_user_dto import PageDtoUserDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only optional values
    query_params = {
        'firstName': "firstName_example",
        'lastName': "lastName_example",
        'name': "name_example",
        'userName': "userName_example",
        'email': "email_example",
        'nameOrEmail': "nameOrEmail_example",
        'role': [
        "ADMIN"
    ],
        'includeDeleted': False,
        'pageNumber': 0,
        'pageSize': 50,
        'sort': [
        "ID"
    ],
        'order': [
        "ASC"
    ],
    }
    try:
        # List users
        api_response = api_instance.get_list_of_users_filtered(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->get_list_of_users_filtered: %s\n" % e)
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

| Name           | Type                 | Description | Notes    |
| -------------- | -------------------- | ----------- | -------- |
| firstName      | FirstNameSchema      |             | optional |
| lastName       | LastNameSchema       |             | optional |
| name           | NameSchema           |             | optional |
| userName       | UserNameSchema       |             | optional |
| email          | EmailSchema          |             | optional |
| nameOrEmail    | NameOrEmailSchema    |             | optional |
| role           | RoleSchema           |             | optional |
| includeDeleted | IncludeDeletedSchema |             | optional |
| pageNumber     | PageNumberSchema     |             | optional |
| pageSize       | PageSizeSchema       |             | optional |
| sort           | SortSchema           |             | optional |
| order          | OrderSchema          |             | optional |

# FirstNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# LastNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# UserNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# EmailSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# NameOrEmailSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RoleSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                           |
| ---------- | ---------- | ------------- | ----------- | ------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["ADMIN", "PROJECT_MANAGER", "LINGUIST", "GUEST", "SUBMITTER", ] |

# IncludeDeletedSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

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

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                              |
| ---------- | ---------- | ------------- | ----------- | -------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["ID", "LAST_NAME", "FIRST_NAME", ] |

# OrderSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                            |
| ---------- | ---------- | ------------- | ----------- | -------------------------------- |
| items      | str,       | str,          |             | must be one of ["ASC", "DESC", ] |

### Return Types, Responses

| Code | Class                                                              | Description                                                 |
| ---- | ------------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                       | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_list_of_users_filtered.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_list_of_users_filtered.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_list_of_users_filtered.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_list_of_users_filtered.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_list_of_users_filtered.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_list_of_users_filtered.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_list_of_users_filtered.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_list_of_users_filtered.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_list_of_users_filtered.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_list_of_users_filtered.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_list_of_users_filtered.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_list_of_users_filtered.ApiResponseFor501) | Not implemented                                             |

#### get_list_of_users_filtered.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                 | Description | Notes |
| ---------------------------------------------------- | ----------- | ----- |
| [**PageDtoUserDto**](../../models/PageDtoUserDto.md) |             |

#### get_list_of_users_filtered.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_users_filtered.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_users_filtered.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_users_filtered.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_users_filtered.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_users_filtered.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_users_filtered.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_users_filtered.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_users_filtered.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_users_filtered.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_users_filtered.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user_v3**

<a id="get_user_v3"></a>

> UserDetailsDtoV3 get_user_v3(user_uid)

Get user

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.user_details_dto_v3 import UserDetailsDtoV3
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    try:
        # Get user
        api_response = api_instance.get_user_v3(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->get_user_v3: %s\n" % e)
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

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                               | Description                                                 |
| ---- | --------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization        | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_user_v3.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_user_v3.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_user_v3.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_user_v3.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_user_v3.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_user_v3.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_user_v3.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_user_v3.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_user_v3.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_user_v3.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_user_v3.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_user_v3.ApiResponseFor501) | Not implemented                                             |

#### get_user_v3.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**UserDetailsDtoV3**](../../models/UserDetailsDtoV3.md) |             |

#### get_user_v3.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_user_v3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_user_v3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_user_v3.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_user_v3.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_user_v3.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_user_v3.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_user_v3.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_user_v3.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_user_v3.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_user_v3.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_assigned_projects**

<a id="list_assigned_projects"></a>

> PageDtoProjectReference list_assigned_projects(user_uid)

List assigned projects

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.page_dto_project_reference import PageDtoProjectReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
    }
    try:
        # List assigned projects
        api_response = api_instance.list_assigned_projects(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->list_assigned_projects: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
        'status': [
        "NEW"
    ],
        'targetLang': [
        "targetLang_example"
    ],
        'workflowStepId': 1,
        'dueInHours': -1,
        'filename': "filename_example",
        'projectName': "projectName_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List assigned projects
        api_response = api_instance.list_assigned_projects(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->list_assigned_projects: %s\n" % e)
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

| Name           | Type                 | Description | Notes    |
| -------------- | -------------------- | ----------- | -------- |
| status         | StatusSchema         |             | optional |
| targetLang     | TargetLangSchema     |             | optional |
| workflowStepId | WorkflowStepIdSchema |             | optional |
| dueInHours     | DueInHoursSchema     |             | optional |
| filename       | FilenameSchema       |             | optional |
| projectName    | ProjectNameSchema    |             | optional |
| pageNumber     | PageNumberSchema     |             | optional |
| pageSize       | PageSizeSchema       |             | optional |

# StatusSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                                              |
| ---------- | ---------- | ------------- | ----------- | -------------------------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["NEW", "ACCEPTED", "DECLINED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] |

# TargetLangSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# WorkflowStepIdSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 64 bit integer |

# DueInHoursSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 32 bit integer |

# FilenameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ProjectNameSchema

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

### path_params

#### RequestPathParams

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_assigned_projects.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_assigned_projects.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_assigned_projects.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_assigned_projects.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_assigned_projects.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_assigned_projects.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_assigned_projects.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_assigned_projects.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_assigned_projects.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_assigned_projects.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_assigned_projects.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_assigned_projects.ApiResponseFor501) | Not implemented                                             |

#### list_assigned_projects.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoProjectReference**](../../models/PageDtoProjectReference.md) |             |

#### list_assigned_projects.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_assigned_projects.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_assigned_projects.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_assigned_projects.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_assigned_projects.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_assigned_projects.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_assigned_projects.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_assigned_projects.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_assigned_projects.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_assigned_projects.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_assigned_projects.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_jobs**

<a id="list_jobs"></a>

> PageDtoAssignedJobDto list_jobs(user_uid)

List assigned jobs

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.page_dto_assigned_job_dto import PageDtoAssignedJobDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
    }
    try:
        # List assigned jobs
        api_response = api_instance.list_jobs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->list_jobs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
        'status': [
        "NEW"
    ],
        'projectUid': "projectUid_example",
        'targetLang': [
        "targetLang_example"
    ],
        'workflowStepId': 1,
        'dueInHours': -1,
        'filename': "filename_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List assigned jobs
        api_response = api_instance.list_jobs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->list_jobs: %s\n" % e)
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

| Name           | Type                 | Description | Notes    |
| -------------- | -------------------- | ----------- | -------- |
| status         | StatusSchema         |             | optional |
| projectUid     | ProjectUidSchema     |             | optional |
| targetLang     | TargetLangSchema     |             | optional |
| workflowStepId | WorkflowStepIdSchema |             | optional |
| dueInHours     | DueInHoursSchema     |             | optional |
| filename       | FilenameSchema       |             | optional |
| pageNumber     | PageNumberSchema     |             | optional |
| pageSize       | PageSizeSchema       |             | optional |

# StatusSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                                              |
| ---------- | ---------- | ------------- | ----------- | -------------------------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["NEW", "ACCEPTED", "DECLINED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# TargetLangSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# WorkflowStepIdSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 64 bit integer |

# DueInHoursSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 32 bit integer |

# FilenameSchema

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

### path_params

#### RequestPathParams

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                             | Description                                                 |
| ---- | ------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization      | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_jobs.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_jobs.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_jobs.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_jobs.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_jobs.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_jobs.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_jobs.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_jobs.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_jobs.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_jobs.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_jobs.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_jobs.ApiResponseFor501) | Not implemented                                             |

#### list_jobs.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**PageDtoAssignedJobDto**](../../models/PageDtoAssignedJobDto.md) |             |

#### list_jobs.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_jobs.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_jobs.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_jobs.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_jobs.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_jobs.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_jobs.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_jobs.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_jobs.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_jobs.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_jobs.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_target_langs**

<a id="list_target_langs"></a>

> PageDtoString list_target_langs(user_uid)

List assigned target languages

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.page_dto_string import PageDtoString
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
    }
    try:
        # List assigned target languages
        api_response = api_instance.list_target_langs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->list_target_langs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
        'status': [
        "NEW"
    ],
        'projectUid': "projectUid_example",
        'workflowStepId': 1,
        'dueInHours': -1,
        'filename': "filename_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List assigned target languages
        api_response = api_instance.list_target_langs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->list_target_langs: %s\n" % e)
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

| Name           | Type                 | Description | Notes    |
| -------------- | -------------------- | ----------- | -------- |
| status         | StatusSchema         |             | optional |
| projectUid     | ProjectUidSchema     |             | optional |
| workflowStepId | WorkflowStepIdSchema |             | optional |
| dueInHours     | DueInHoursSchema     |             | optional |
| filename       | FilenameSchema       |             | optional |
| pageNumber     | PageNumberSchema     |             | optional |
| pageSize       | PageSizeSchema       |             | optional |

# StatusSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                                              |
| ---------- | ---------- | ------------- | ----------- | -------------------------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["NEW", "ACCEPTED", "DECLINED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# WorkflowStepIdSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 64 bit integer |

# DueInHoursSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 32 bit integer |

# FilenameSchema

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

### path_params

#### RequestPathParams

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                     | Description                                                 |
| ---- | --------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization              | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_target_langs.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_target_langs.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_target_langs.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_target_langs.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_target_langs.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_target_langs.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_target_langs.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_target_langs.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_target_langs.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_target_langs.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_target_langs.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_target_langs.ApiResponseFor501) | Not implemented                                             |

#### list_target_langs.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                               | Description | Notes |
| -------------------------------------------------- | ----------- | ----- |
| [**PageDtoString**](../../models/PageDtoString.md) |             |

#### list_target_langs.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_target_langs.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_target_langs.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_target_langs.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_target_langs.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_target_langs.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_target_langs.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_target_langs.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_target_langs.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_target_langs.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_target_langs.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_workflow_steps**

<a id="list_workflow_steps"></a>

> PageDtoWorkflowStepReference list_workflow_steps(user_uid)

List assigned workflow steps

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.page_dto_workflow_step_reference import PageDtoWorkflowStepReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
    }
    try:
        # List assigned workflow steps
        api_response = api_instance.list_workflow_steps(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->list_workflow_steps: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userUid': "userUid_example",
    }
    query_params = {
        'status': [
        "NEW"
    ],
        'projectUid': "projectUid_example",
        'targetLang': [
        "targetLang_example"
    ],
        'dueInHours': -1,
        'filename': "filename_example",
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List assigned workflow steps
        api_response = api_instance.list_workflow_steps(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->list_workflow_steps: %s\n" % e)
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

| Name       | Type             | Description | Notes    |
| ---------- | ---------------- | ----------- | -------- |
| status     | StatusSchema     |             | optional |
| projectUid | ProjectUidSchema |             | optional |
| targetLang | TargetLangSchema |             | optional |
| dueInHours | DueInHoursSchema |             | optional |
| filename   | FilenameSchema   |             | optional |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |

# StatusSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                                              |
| ---------- | ---------- | ------------- | ----------- | -------------------------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["NEW", "ACCEPTED", "DECLINED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] |

# ProjectUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# TargetLangSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# DueInHoursSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 32 bit integer |

# FilenameSchema

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

### path_params

#### RequestPathParams

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_workflow_steps.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_workflow_steps.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_workflow_steps.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_workflow_steps.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_workflow_steps.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_workflow_steps.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_workflow_steps.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_workflow_steps.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_workflow_steps.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_workflow_steps.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_workflow_steps.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_workflow_steps.ApiResponseFor501) | Not implemented                                             |

#### list_workflow_steps.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                             | Description | Notes |
| -------------------------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoWorkflowStepReference**](../../models/PageDtoWorkflowStepReference.md) |             |

#### list_workflow_steps.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_workflow_steps.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_workflow_steps.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_workflow_steps.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_workflow_steps.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_workflow_steps.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_workflow_steps.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_workflow_steps.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_workflow_steps.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_workflow_steps.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_workflow_steps.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **login_activity**

<a id="login_activity"></a>

> UserStatisticsListDto login_activity(user_uid)

Login statistics

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.user_statistics_list_dto import UserStatisticsListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    try:
        # Login statistics
        api_response = api_instance.login_activity(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->login_activity: %s\n" % e)
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

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#login_activity.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#login_activity.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#login_activity.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#login_activity.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#login_activity.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#login_activity.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#login_activity.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#login_activity.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#login_activity.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#login_activity.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#login_activity.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#login_activity.ApiResponseFor501) | Not implemented                                             |

#### login_activity.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                               | Description | Notes |
| ------------------------------------------------------------------ | ----------- | ----- |
| [**UserStatisticsListDto**](../../models/UserStatisticsListDto.md) |             |

#### login_activity.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_activity.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_activity.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_activity.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_activity.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_activity.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_activity.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_activity.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_activity.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_activity.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### login_activity.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **send_login_info**

<a id="send_login_info"></a>

> send_login_info(user_uid)

Send login information

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    try:
        # Send login information
        api_response = api_instance.send_login_info(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->send_login_info: %s\n" % e)
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

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#send_login_info.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#send_login_info.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#send_login_info.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#send_login_info.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#send_login_info.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#send_login_info.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#send_login_info.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#send_login_info.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#send_login_info.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#send_login_info.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#send_login_info.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#send_login_info.ApiResponseFor501) | Not implemented                                             |

#### send_login_info.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### send_login_info.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_password**

<a id="update_password"></a>

> update_password(user_uid)

Update password

- Password length must be between 8 and 255 \* Password must not be same as the username

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.user_password_edit_dto import UserPasswordEditDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    try:
        # Update password
        api_response = api_instance.update_password(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->update_password: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userUid': "userUid_example",
    }
    body = UserPasswordEditDto(
        password="password_example",
    )
    try:
        # Update password
        api_response = api_instance.update_password(
            path_params=path_params,
            body=body,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->update_password: %s\n" % e)
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

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**UserPasswordEditDto**](../../models/UserPasswordEditDto.md) |             |

### path_params

#### RequestPathParams

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                   | Description                                                 |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization            | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#update_password.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#update_password.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_password.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_password.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_password.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_password.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_password.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_password.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_password.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_password.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_password.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_password.ApiResponseFor501) | Not implemented                                             |

#### update_password.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_password.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_user_v3**

<a id="update_user_v3"></a>

> UserDetailsDtoV3 update_user_v3(user_uid)

Edit user

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.user_details_dto_v3 import UserDetailsDtoV3
from phrasetms_client.model.abstract_user_edit_dto import AbstractUserEditDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userUid': "userUid_example",
    }
    try:
        # Edit user
        api_response = api_instance.update_user_v3(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->update_user_v3: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userUid': "userUid_example",
    }
    body = AbstractUserEditDto()
    try:
        # Edit user
        api_response = api_instance.update_user_v3(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->update_user_v3: %s\n" % e)
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

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**AbstractUserEditDto**](../../models/AbstractUserEditDto.md) |             |

### path_params

#### RequestPathParams

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| userUid | UserUidSchema |             |

# UserUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                  | Description                                                 |
| ---- | ------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#update_user_v3.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#update_user_v3.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_user_v3.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_user_v3.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_user_v3.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_user_v3.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_user_v3.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_user_v3.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_user_v3.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_user_v3.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_user_v3.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_user_v3.ApiResponseFor501) | Not implemented                                             |

#### update_user_v3.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                     | Description | Notes |
| -------------------------------------------------------- | ----------- | ----- |
| [**UserDetailsDtoV3**](../../models/UserDetailsDtoV3.md) |             |

#### update_user_v3.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_user_v3.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_user_v3.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_user_v3.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_user_v3.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_user_v3.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_user_v3.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_user_v3.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_user_v3.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_user_v3.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_user_v3.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_last_logins**

<a id="user_last_logins"></a>

> PageDtoLastLoginDto user_last_logins()

List last login dates

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import user_api
from phrasetms_client.model.page_dto_last_login_dto import PageDtoLastLoginDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only optional values
    query_params = {
        'userName': "userName_example",
        'role': [
        "ADMIN"
    ],
        'sort': [
        "ID"
    ],
        'order': [
        "ASC"
    ],
        'pageNumber': 0,
        'pageSize': 100,
    }
    try:
        # List last login dates
        api_response = api_instance.user_last_logins(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling UserApi->user_last_logins: %s\n" % e)
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
| userName   | UserNameSchema   |             | optional |
| role       | RoleSchema       |             | optional |
| sort       | SortSchema       |             | optional |
| order      | OrderSchema      |             | optional |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |

# UserNameSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# RoleSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                                                           |
| ---------- | ---------- | ------------- | ----------- | ------------------------------------------------------------------------------- |
| items      | str,       | str,          |             | must be one of ["ADMIN", "PROJECT_MANAGER", "LINGUIST", "GUEST", "SUBMITTER", ] |

# SortSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                                      |
| ---------- | ---------- | ------------- | ----------- | ------------------------------------------ |
| items      | str,       | str,          |             | must be one of ["ID", "LAST_LOGIN_DATE", ] |

# OrderSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes                            |
| ---------- | ---------- | ------------- | ----------- | -------------------------------- |
| items      | str,       | str,          |             | must be one of ["ASC", "DESC", ] |

# PageNumberSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                               |
| --------------------- | ---------------- | ----------- | ----------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 0value must be a 32 bit integer |

# PageSizeSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                                                                                 |
| --------------------- | ---------------- | ----------- | ------------------------------------------------------------------------------------- |
| decimal.Decimal, int, | decimal.Decimal, |             | if omitted the server will use the default value of 100value must be a 32 bit integer |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#user_last_logins.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#user_last_logins.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#user_last_logins.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#user_last_logins.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#user_last_logins.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#user_last_logins.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#user_last_logins.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#user_last_logins.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#user_last_logins.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#user_last_logins.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#user_last_logins.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#user_last_logins.ApiResponseFor501) | Not implemented                                             |

#### user_last_logins.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoLastLoginDto**](../../models/PageDtoLastLoginDto.md) |             |

#### user_last_logins.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### user_last_logins.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### user_last_logins.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### user_last_logins.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### user_last_logins.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### user_last_logins.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### user_last_logins.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### user_last_logins.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### user_last_logins.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### user_last_logins.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### user_last_logins.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
