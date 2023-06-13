<a id="__pageTop"></a>

# phrasetms_client.apis.tags.conversations_api.ConversationsApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                                          | HTTP request                                                                                 | Description               |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------- |
| [**add_lqa_comment1**](#add_lqa_comment1)                                       | **post** /api2/v2/jobs/{jobUid}/conversations/lqas/{conversationId}/comments                 | Add LQA comment           |
| [**add_plain_comment2**](#add_plain_comment2)                                   | **post** /api2/v3/jobs/{jobUid}/conversations/plains/{conversationId}/comments               | Add plain comment         |
| [**create_lqa_conversation1**](#create_lqa_conversation1)                       | **post** /api2/v2/jobs/{jobUid}/conversations/lqas                                           | Create LQA conversation   |
| [**create_segment_target_conversation1**](#create_segment_target_conversation1) | **post** /api2/v3/jobs/{jobUid}/conversations/plains                                         | Create plain conversation |
| [**delete_lqa_comment**](#delete_lqa_comment)                                   | **delete** /api2/v1/jobs/{jobUid}/conversations/lqas/{conversationId}/comments/{commentId}   | Delete LQA comment        |
| [**delete_lqa_conversation**](#delete_lqa_conversation)                         | **delete** /api2/v1/jobs/{jobUid}/conversations/lqas/{conversationId}                        | Delete LQA conversation   |
| [**delete_plain_comment**](#delete_plain_comment)                               | **delete** /api2/v1/jobs/{jobUid}/conversations/plains/{conversationId}/comments/{commentId} | Delete plain comment      |
| [**delete_plain_conversation**](#delete_plain_conversation)                     | **delete** /api2/v1/jobs/{jobUid}/conversations/plains/{conversationId}                      | Delete plain conversation |
| [**find_conversations**](#find_conversations)                                   | **post** /api2/v1/jobs/conversations/find                                                    | Find all conversation     |
| [**get_lqa_conversation**](#get_lqa_conversation)                               | **get** /api2/v1/jobs/{jobUid}/conversations/lqas/{conversationId}                           | Get LQA conversation      |
| [**get_plain_conversation**](#get_plain_conversation)                           | **get** /api2/v1/jobs/{jobUid}/conversations/plains/{conversationId}                         | Get plain conversation    |
| [**list_all_conversations**](#list_all_conversations)                           | **get** /api2/v1/jobs/{jobUid}/conversations                                                 | List all conversations    |
| [**list_lqa_conversations**](#list_lqa_conversations)                           | **get** /api2/v1/jobs/{jobUid}/conversations/lqas                                            | List LQA conversations    |
| [**list_plain_conversations**](#list_plain_conversations)                       | **get** /api2/v1/jobs/{jobUid}/conversations/plains                                          | List plain conversations  |
| [**update_lqa_comment1**](#update_lqa_comment1)                                 | **put** /api2/v2/jobs/{jobUid}/conversations/lqas/{conversationId}/comments/{commentId}      | Edit LQA comment          |
| [**update_lqa_conversation1**](#update_lqa_conversation1)                       | **put** /api2/v2/jobs/{jobUid}/conversations/lqas/{conversationId}                           | Update LQA conversation   |
| [**update_plain_comment1**](#update_plain_comment1)                             | **put** /api2/v3/jobs/{jobUid}/conversations/plains/{conversationId}/comments/{commentId}    | Edit plain comment        |
| [**update_plain_conversation**](#update_plain_conversation)                     | **put** /api2/v1/jobs/{jobUid}/conversations/plains/{conversationId}                         | Edit plain conversation   |

# **add_lqa_comment1**

<a id="add_lqa_comment1"></a>

> AddLqaCommentResultDto add_lqa_comment1(job_uidconversation_id)

Add LQA comment

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.add_lqa_comment_result_dto import AddLqaCommentResultDto
from phrasetms_client.model.add_comment_dto import AddCommentDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    try:
        # Add LQA comment
        api_response = api_instance.add_lqa_comment1(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->add_lqa_comment1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    body = AddCommentDto(
        text="text_example",
    )
    try:
        # Add LQA comment
        api_response = api_instance.add_lqa_comment1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->add_lqa_comment1: %s\n" % e)
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

| Type                                               | Description | Notes |
| -------------------------------------------------- | ----------- | ----- |
| [**AddCommentDto**](../../models/AddCommentDto.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                    | Description                                                 |
| ---- | -------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization             | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#add_lqa_comment1.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#add_lqa_comment1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#add_lqa_comment1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#add_lqa_comment1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#add_lqa_comment1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#add_lqa_comment1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#add_lqa_comment1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#add_lqa_comment1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#add_lqa_comment1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#add_lqa_comment1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#add_lqa_comment1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#add_lqa_comment1.ApiResponseFor501) | Not implemented                                             |

#### add_lqa_comment1.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**AddLqaCommentResultDto**](../../models/AddLqaCommentResultDto.md) |             |

#### add_lqa_comment1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_lqa_comment1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_lqa_comment1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_lqa_comment1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_lqa_comment1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_lqa_comment1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_lqa_comment1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_lqa_comment1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_lqa_comment1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_lqa_comment1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_lqa_comment1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **add_plain_comment2**

<a id="add_plain_comment2"></a>

> AddPlainCommentResultDto add_plain_comment2(job_uidconversation_id)

Add plain comment

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.add_comment_dto import AddCommentDto
from phrasetms_client.model.add_plain_comment_result_dto import AddPlainCommentResultDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    try:
        # Add plain comment
        api_response = api_instance.add_plain_comment2(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->add_plain_comment2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    body = AddCommentDto(
        text="text_example",
    )
    try:
        # Add plain comment
        api_response = api_instance.add_plain_comment2(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->add_plain_comment2: %s\n" % e)
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

| Type                                               | Description | Notes |
| -------------------------------------------------- | ----------- | ----- |
| [**AddCommentDto**](../../models/AddCommentDto.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#add_plain_comment2.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#add_plain_comment2.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#add_plain_comment2.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#add_plain_comment2.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#add_plain_comment2.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#add_plain_comment2.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#add_plain_comment2.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#add_plain_comment2.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#add_plain_comment2.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#add_plain_comment2.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#add_plain_comment2.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#add_plain_comment2.ApiResponseFor501) | Not implemented                                             |

#### add_plain_comment2.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**AddPlainCommentResultDto**](../../models/AddPlainCommentResultDto.md) |             |

#### add_plain_comment2.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_plain_comment2.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_plain_comment2.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_plain_comment2.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_plain_comment2.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_plain_comment2.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_plain_comment2.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_plain_comment2.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_plain_comment2.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_plain_comment2.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### add_plain_comment2.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_lqa_conversation1**

<a id="create_lqa_conversation1"></a>

> LQAConversationDto create_lqa_conversation1(job_uid)

Create LQA conversation

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.create_lqa_conversation_dto import CreateLqaConversationDto
from phrasetms_client.model.lqa_conversation_dto import LQAConversationDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
    }
    try:
        # Create LQA conversation
        api_response = api_instance.create_lqa_conversation1(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->create_lqa_conversation1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
    }
    body = CreateLqaConversationDto(
        lqa_description="lqa_description_example",
        references=LQAReferences(
            task_id="task_id_example",
            job_part_uid="job_part_uid_example",
            trans_group_id=0,
            segment_id="segment_id_example",
            conversation_title="conversation_title_example",
            conversation_title_offset=0,
            commented_text="commented_text_example",
            correlation=ReferenceCorrelation(
                uid="uid_example",
                role="PARENT",
            ),
            lqa=[
                LQAReference(
                    error_category_id=1,
                    severity_id=1,
                    user=IdReference(
                        id="id_example",
                    ),
                    repeated="REPEATED",
                )
            ],
        ),
    )
    try:
        # Create LQA conversation
        api_response = api_instance.create_lqa_conversation1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->create_lqa_conversation1: %s\n" % e)
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

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**CreateLqaConversationDto**](../../models/CreateLqaConversationDto.md) |             |

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

| Code | Class                                                            | Description                                                 |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                     | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_lqa_conversation1.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_lqa_conversation1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_lqa_conversation1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_lqa_conversation1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_lqa_conversation1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_lqa_conversation1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_lqa_conversation1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_lqa_conversation1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_lqa_conversation1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_lqa_conversation1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_lqa_conversation1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_lqa_conversation1.ApiResponseFor501) | Not implemented                                             |

#### create_lqa_conversation1.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**LQAConversationDto**](../../models/LQAConversationDto.md) |             |

#### create_lqa_conversation1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_lqa_conversation1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_lqa_conversation1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_lqa_conversation1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_lqa_conversation1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_lqa_conversation1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_lqa_conversation1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_lqa_conversation1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_lqa_conversation1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_lqa_conversation1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_lqa_conversation1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_segment_target_conversation1**

<a id="create_segment_target_conversation1"></a>

> PlainConversationDto create_segment_target_conversation1(job_uid)

Create plain conversation

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.plain_conversation_dto import PlainConversationDto
from phrasetms_client.model.create_plain_conversation_dto import CreatePlainConversationDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
    }
    try:
        # Create plain conversation
        api_response = api_instance.create_segment_target_conversation1(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->create_segment_target_conversation1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
    }
    body = CreatePlainConversationDto(
        comment=AddCommentDto(
            text="text_example",
        ),
        references=PlainReferences(
            task_id="task_id_example",
            job_part_uid="job_part_uid_example",
            trans_group_id=0,
            segment_id="segment_id_example",
            conversation_title="conversation_title_example",
            conversation_title_offset=0,
            commented_text="commented_text_example",
            correlation=ReferenceCorrelation(
                uid="uid_example",
                role="PARENT",
            ),
        ),
    )
    try:
        # Create plain conversation
        api_response = api_instance.create_segment_target_conversation1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->create_segment_target_conversation1: %s\n" % e)
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

| Type                                                                         | Description | Notes |
| ---------------------------------------------------------------------------- | ----------- | ----- |
| [**CreatePlainConversationDto**](../../models/CreatePlainConversationDto.md) |             |

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

| Code | Class                                                                       | Description                                                 |
| ---- | --------------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                                | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_segment_target_conversation1.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_segment_target_conversation1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_segment_target_conversation1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_segment_target_conversation1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_segment_target_conversation1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_segment_target_conversation1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_segment_target_conversation1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_segment_target_conversation1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_segment_target_conversation1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_segment_target_conversation1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_segment_target_conversation1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_segment_target_conversation1.ApiResponseFor501) | Not implemented                                             |

#### create_segment_target_conversation1.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**PlainConversationDto**](../../models/PlainConversationDto.md) |             |

#### create_segment_target_conversation1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segment_target_conversation1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segment_target_conversation1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segment_target_conversation1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segment_target_conversation1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segment_target_conversation1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segment_target_conversation1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segment_target_conversation1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segment_target_conversation1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segment_target_conversation1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segment_target_conversation1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_lqa_comment**

<a id="delete_lqa_comment"></a>

> delete_lqa_comment(job_uidconversation_idcomment_id)

Delete LQA comment

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
        'commentId': "commentId_example",
    }
    try:
        # Delete LQA comment
        api_response = api_instance.delete_lqa_comment(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->delete_lqa_comment: %s\n" % e)
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
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |
| commentId      | CommentIdSchema      |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# CommentIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_lqa_comment.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_lqa_comment.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_lqa_comment.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_lqa_comment.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_lqa_comment.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_lqa_comment.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_lqa_comment.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_lqa_comment.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_lqa_comment.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_lqa_comment.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_lqa_comment.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_lqa_comment.ApiResponseFor501) | Not implemented                                             |

#### delete_lqa_comment.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_comment.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_lqa_conversation**

<a id="delete_lqa_conversation"></a>

> delete_lqa_conversation(job_uidconversation_id)

Delete LQA conversation

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    try:
        # Delete LQA conversation
        api_response = api_instance.delete_lqa_conversation(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->delete_lqa_conversation: %s\n" % e)
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
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                           | Description                                                 |
| ---- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                    | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_lqa_conversation.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_lqa_conversation.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_lqa_conversation.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_lqa_conversation.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_lqa_conversation.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_lqa_conversation.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_lqa_conversation.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_lqa_conversation.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_lqa_conversation.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_lqa_conversation.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_lqa_conversation.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_lqa_conversation.ApiResponseFor501) | Not implemented                                             |

#### delete_lqa_conversation.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_lqa_conversation.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_plain_comment**

<a id="delete_plain_comment"></a>

> delete_plain_comment(job_uidconversation_idcomment_id)

Delete plain comment

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
        'commentId': "commentId_example",
    }
    try:
        # Delete plain comment
        api_response = api_instance.delete_plain_comment(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->delete_plain_comment: %s\n" % e)
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
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |
| commentId      | CommentIdSchema      |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# CommentIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_plain_comment.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_plain_comment.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_plain_comment.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_plain_comment.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_plain_comment.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_plain_comment.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_plain_comment.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_plain_comment.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_plain_comment.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_plain_comment.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_plain_comment.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_plain_comment.ApiResponseFor501) | Not implemented                                             |

#### delete_plain_comment.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_comment.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_plain_conversation**

<a id="delete_plain_conversation"></a>

> delete_plain_conversation(job_uidconversation_id)

Delete plain conversation

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    try:
        # Delete plain conversation
        api_response = api_instance.delete_plain_conversation(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->delete_plain_conversation: %s\n" % e)
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
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                             | Description                                                 |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#delete_plain_conversation.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#delete_plain_conversation.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#delete_plain_conversation.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#delete_plain_conversation.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#delete_plain_conversation.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#delete_plain_conversation.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#delete_plain_conversation.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#delete_plain_conversation.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#delete_plain_conversation.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#delete_plain_conversation.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#delete_plain_conversation.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#delete_plain_conversation.ApiResponseFor501) | Not implemented                                             |

#### delete_plain_conversation.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### delete_plain_conversation.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_conversations**

<a id="find_conversations"></a>

> ConversationListDto find_conversations()

Find all conversation

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.find_conversations_dto import FindConversationsDto
from phrasetms_client.model.conversation_list_dto import ConversationListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only optional values
    body = FindConversationsDto(
        jobs=[
            UidReference(
                uid="uid_example",
            )
        ],
        since="since_example",
        include_deleted=True,
    )
    try:
        # Find all conversation
        api_response = api_instance.find_conversations(
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->find_conversations: %s\n" % e)
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
| [**FindConversationsDto**](../../models/FindConversationsDto.md) |             |

### Return Types, Responses

| Code | Class                                                      | Description                                                 |
| ---- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization               | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#find_conversations.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#find_conversations.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#find_conversations.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#find_conversations.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#find_conversations.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#find_conversations.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#find_conversations.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#find_conversations.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#find_conversations.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#find_conversations.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#find_conversations.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#find_conversations.ApiResponseFor501) | Not implemented                                             |

#### find_conversations.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**ConversationListDto**](../../models/ConversationListDto.md) |             |

#### find_conversations.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### find_conversations.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### find_conversations.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### find_conversations.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### find_conversations.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### find_conversations.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### find_conversations.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### find_conversations.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### find_conversations.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### find_conversations.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### find_conversations.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_lqa_conversation**

<a id="get_lqa_conversation"></a>

> LQAConversationDto get_lqa_conversation(job_uidconversation_id)

Get LQA conversation

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.lqa_conversation_dto import LQAConversationDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    try:
        # Get LQA conversation
        api_response = api_instance.get_lqa_conversation(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->get_lqa_conversation: %s\n" % e)
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

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                        | Description                                                 |
| ---- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                 | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_lqa_conversation.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_lqa_conversation.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_lqa_conversation.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_lqa_conversation.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_lqa_conversation.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_lqa_conversation.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_lqa_conversation.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_lqa_conversation.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_lqa_conversation.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_lqa_conversation.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_lqa_conversation.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_lqa_conversation.ApiResponseFor501) | Not implemented                                             |

#### get_lqa_conversation.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**LQAConversationDto**](../../models/LQAConversationDto.md) |             |

#### get_lqa_conversation.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_lqa_conversation.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_lqa_conversation.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_lqa_conversation.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_lqa_conversation.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_lqa_conversation.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_lqa_conversation.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_lqa_conversation.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_lqa_conversation.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_lqa_conversation.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_lqa_conversation.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_plain_conversation**

<a id="get_plain_conversation"></a>

> PlainConversationDto get_plain_conversation(job_uidconversation_id)

Get plain conversation

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.plain_conversation_dto import PlainConversationDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    try:
        # Get plain conversation
        api_response = api_instance.get_plain_conversation(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->get_plain_conversation: %s\n" % e)
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

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_plain_conversation.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_plain_conversation.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_plain_conversation.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_plain_conversation.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_plain_conversation.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_plain_conversation.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_plain_conversation.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_plain_conversation.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_plain_conversation.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_plain_conversation.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_plain_conversation.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_plain_conversation.ApiResponseFor501) | Not implemented                                             |

#### get_plain_conversation.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**PlainConversationDto**](../../models/PlainConversationDto.md) |             |

#### get_plain_conversation.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_plain_conversation.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_plain_conversation.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_plain_conversation.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_plain_conversation.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_plain_conversation.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_plain_conversation.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_plain_conversation.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_plain_conversation.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_plain_conversation.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_plain_conversation.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_all_conversations**

<a id="list_all_conversations"></a>

> ConversationListDto list_all_conversations(job_uid)

List all conversations

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.conversation_list_dto import ConversationListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
    }
    query_params = {
    }
    try:
        # List all conversations
        api_response = api_instance.list_all_conversations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->list_all_conversations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
    }
    query_params = {
        'includeDeleted': False,
        'since': "since_example",
    }
    try:
        # List all conversations
        api_response = api_instance.list_all_conversations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->list_all_conversations: %s\n" % e)
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
| includeDeleted | IncludeDeletedSchema |             | optional |
| since          | SinceSchema          |             | optional |

# IncludeDeletedSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

# SinceSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

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

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_all_conversations.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_all_conversations.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_all_conversations.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_all_conversations.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_all_conversations.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_all_conversations.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_all_conversations.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_all_conversations.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_all_conversations.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_all_conversations.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_all_conversations.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_all_conversations.ApiResponseFor501) | Not implemented                                             |

#### list_all_conversations.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**ConversationListDto**](../../models/ConversationListDto.md) |             |

#### list_all_conversations.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_all_conversations.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_all_conversations.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_all_conversations.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_all_conversations.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_all_conversations.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_all_conversations.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_all_conversations.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_all_conversations.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_all_conversations.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_all_conversations.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_lqa_conversations**

<a id="list_lqa_conversations"></a>

> LQAConversationsListDto list_lqa_conversations(job_uid)

List LQA conversations

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.lqa_conversations_list_dto import LQAConversationsListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
    }
    query_params = {
    }
    try:
        # List LQA conversations
        api_response = api_instance.list_lqa_conversations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->list_lqa_conversations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
    }
    query_params = {
        'includeDeleted': False,
        'since': "since_example",
    }
    try:
        # List LQA conversations
        api_response = api_instance.list_lqa_conversations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->list_lqa_conversations: %s\n" % e)
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
| includeDeleted | IncludeDeletedSchema |             | optional |
| since          | SinceSchema          |             | optional |

# IncludeDeletedSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

# SinceSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

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

| Code | Class                                                          | Description                                                 |
| ---- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                   | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_lqa_conversations.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_lqa_conversations.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_lqa_conversations.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_lqa_conversations.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_lqa_conversations.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_lqa_conversations.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_lqa_conversations.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_lqa_conversations.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_lqa_conversations.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_lqa_conversations.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_lqa_conversations.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_lqa_conversations.ApiResponseFor501) | Not implemented                                             |

#### list_lqa_conversations.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**LQAConversationsListDto**](../../models/LQAConversationsListDto.md) |             |

#### list_lqa_conversations.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_lqa_conversations.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_lqa_conversations.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_lqa_conversations.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_lqa_conversations.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_lqa_conversations.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_lqa_conversations.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_lqa_conversations.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_lqa_conversations.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_lqa_conversations.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_lqa_conversations.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_plain_conversations**

<a id="list_plain_conversations"></a>

> PlainConversationsListDto list_plain_conversations(job_uid)

List plain conversations

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.plain_conversations_list_dto import PlainConversationsListDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
    }
    query_params = {
    }
    try:
        # List plain conversations
        api_response = api_instance.list_plain_conversations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->list_plain_conversations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
    }
    query_params = {
        'includeDeleted': False,
        'since': "since_example",
    }
    try:
        # List plain conversations
        api_response = api_instance.list_plain_conversations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->list_plain_conversations: %s\n" % e)
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
| includeDeleted | IncludeDeletedSchema |             | optional |
| since          | SinceSchema          |             | optional |

# IncludeDeletedSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes                                                     |
| ---------- | ------------- | ----------- | --------------------------------------------------------- |
| bool,      | BoolClass,    |             | if omitted the server will use the default value of False |

# SinceSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

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

| Code | Class                                                            | Description                                                 |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                     | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#list_plain_conversations.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#list_plain_conversations.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#list_plain_conversations.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#list_plain_conversations.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#list_plain_conversations.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#list_plain_conversations.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#list_plain_conversations.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#list_plain_conversations.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#list_plain_conversations.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#list_plain_conversations.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#list_plain_conversations.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#list_plain_conversations.ApiResponseFor501) | Not implemented                                             |

#### list_plain_conversations.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                       | Description | Notes |
| -------------------------------------------------------------------------- | ----------- | ----- |
| [**PlainConversationsListDto**](../../models/PlainConversationsListDto.md) |             |

#### list_plain_conversations.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_plain_conversations.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_plain_conversations.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_plain_conversations.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_plain_conversations.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_plain_conversations.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_plain_conversations.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_plain_conversations.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_plain_conversations.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_plain_conversations.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### list_plain_conversations.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_lqa_comment1**

<a id="update_lqa_comment1"></a>

> LQAConversationDto update_lqa_comment1(job_uidconversation_idcomment_id)

Edit LQA comment

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.add_comment_dto import AddCommentDto
from phrasetms_client.model.lqa_conversation_dto import LQAConversationDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
        'commentId': "commentId_example",
    }
    try:
        # Edit LQA comment
        api_response = api_instance.update_lqa_comment1(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->update_lqa_comment1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
        'commentId': "commentId_example",
    }
    body = AddCommentDto(
        text="text_example",
    )
    try:
        # Edit LQA comment
        api_response = api_instance.update_lqa_comment1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->update_lqa_comment1: %s\n" % e)
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

| Type                                               | Description | Notes |
| -------------------------------------------------- | ----------- | ----- |
| [**AddCommentDto**](../../models/AddCommentDto.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |
| commentId      | CommentIdSchema      |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# CommentIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                       | Description                                                 |
| ---- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                | When skip_deserialization is True this response is returned |
| 202  | [ApiResponseFor202](#update_lqa_comment1.ApiResponseFor202) | Updated                                                     |
| 400  | [ApiResponseFor400](#update_lqa_comment1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_lqa_comment1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_lqa_comment1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_lqa_comment1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_lqa_comment1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_lqa_comment1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_lqa_comment1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_lqa_comment1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_lqa_comment1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_lqa_comment1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_lqa_comment1.ApiResponseFor501) | Not implemented                                             |

#### update_lqa_comment1.ApiResponseFor202

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**LQAConversationDto**](../../models/LQAConversationDto.md) |             |

#### update_lqa_comment1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_comment1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_comment1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_comment1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_comment1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_comment1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_comment1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_comment1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_comment1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_comment1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_comment1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_lqa_conversation1**

<a id="update_lqa_conversation1"></a>

> LQAConversationDto update_lqa_conversation1(job_uidconversation_id)

Update LQA conversation

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.edit_lqa_conversation_dto import EditLqaConversationDto
from phrasetms_client.model.lqa_conversation_dto import LQAConversationDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    try:
        # Update LQA conversation
        api_response = api_instance.update_lqa_conversation1(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->update_lqa_conversation1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    body = EditLqaConversationDto(
        lqa_description="lqa_description_example",
        lqa=[
            LQAReference(
                error_category_id=1,
                severity_id=1,
                user=IdReference(
                    id="id_example",
                ),
                repeated="REPEATED",
            )
        ],
        status="resolved",
        correlation=ReferenceCorrelation(
            uid="uid_example",
            role="PARENT",
        ),
    )
    try:
        # Update LQA conversation
        api_response = api_instance.update_lqa_conversation1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->update_lqa_conversation1: %s\n" % e)
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

| Type                                                                 | Description | Notes |
| -------------------------------------------------------------------- | ----------- | ----- |
| [**EditLqaConversationDto**](../../models/EditLqaConversationDto.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                            | Description                                                 |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                     | When skip_deserialization is True this response is returned |
| 202  | [ApiResponseFor202](#update_lqa_conversation1.ApiResponseFor202) | Updated                                                     |
| 400  | [ApiResponseFor400](#update_lqa_conversation1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_lqa_conversation1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_lqa_conversation1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_lqa_conversation1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_lqa_conversation1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_lqa_conversation1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_lqa_conversation1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_lqa_conversation1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_lqa_conversation1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_lqa_conversation1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_lqa_conversation1.ApiResponseFor501) | Not implemented                                             |

#### update_lqa_conversation1.ApiResponseFor202

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson

| Type                                                         | Description | Notes |
| ------------------------------------------------------------ | ----------- | ----- |
| [**LQAConversationDto**](../../models/LQAConversationDto.md) |             |

#### update_lqa_conversation1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_conversation1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_conversation1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_conversation1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_conversation1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_conversation1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_conversation1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_conversation1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_conversation1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_conversation1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_lqa_conversation1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_plain_comment1**

<a id="update_plain_comment1"></a>

> PlainConversationDto update_plain_comment1(job_uidconversation_idcomment_id)

Edit plain comment

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.plain_conversation_dto import PlainConversationDto
from phrasetms_client.model.add_comment_dto import AddCommentDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
        'commentId': "commentId_example",
    }
    try:
        # Edit plain comment
        api_response = api_instance.update_plain_comment1(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->update_plain_comment1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
        'commentId': "commentId_example",
    }
    body = AddCommentDto(
        text="text_example",
    )
    try:
        # Edit plain comment
        api_response = api_instance.update_plain_comment1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->update_plain_comment1: %s\n" % e)
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

| Type                                               | Description | Notes |
| -------------------------------------------------- | ----------- | ----- |
| [**AddCommentDto**](../../models/AddCommentDto.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |
| commentId      | CommentIdSchema      |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# CommentIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                         | Description                                                 |
| ---- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                  | When skip_deserialization is True this response is returned |
| 202  | [ApiResponseFor202](#update_plain_comment1.ApiResponseFor202) | Updated                                                     |
| 400  | [ApiResponseFor400](#update_plain_comment1.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_plain_comment1.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_plain_comment1.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_plain_comment1.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_plain_comment1.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_plain_comment1.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_plain_comment1.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_plain_comment1.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_plain_comment1.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_plain_comment1.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_plain_comment1.ApiResponseFor501) | Not implemented                                             |

#### update_plain_comment1.ApiResponseFor202

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**PlainConversationDto**](../../models/PlainConversationDto.md) |             |

#### update_plain_comment1.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_comment1.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_comment1.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_comment1.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_comment1.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_comment1.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_comment1.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_comment1.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_comment1.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_comment1.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_comment1.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_plain_conversation**

<a id="update_plain_conversation"></a>

> PlainConversationDto update_plain_conversation(job_uidconversation_id)

Edit plain conversation

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import conversations_api
from phrasetms_client.model.plain_conversation_dto import PlainConversationDto
from phrasetms_client.model.edit_plain_conversation_dto import EditPlainConversationDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    try:
        # Edit plain conversation
        api_response = api_instance.update_plain_conversation(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->update_plain_conversation: %s\n" % e)

    # example passing only optional values
    path_params = {
        'jobUid': "jobUid_example",
        'conversationId': "conversationId_example",
    }
    body = EditPlainConversationDto(
        status="resolved",
        correlation=ReferenceCorrelation(
            uid="uid_example",
            role="PARENT",
        ),
    )
    try:
        # Edit plain conversation
        api_response = api_instance.update_plain_conversation(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling ConversationsApi->update_plain_conversation: %s\n" % e)
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

| Type                                                                     | Description | Notes |
| ------------------------------------------------------------------------ | ----------- | ----- |
| [**EditPlainConversationDto**](../../models/EditPlainConversationDto.md) |             |

### path_params

#### RequestPathParams

| Name           | Type                 | Description | Notes |
| -------------- | -------------------- | ----------- | ----- |
| jobUid         | JobUidSchema         |             |
| conversationId | ConversationIdSchema |             |

# JobUidSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

# ConversationIdSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                             | Description                                                 |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#update_plain_conversation.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#update_plain_conversation.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#update_plain_conversation.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#update_plain_conversation.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#update_plain_conversation.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#update_plain_conversation.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#update_plain_conversation.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#update_plain_conversation.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#update_plain_conversation.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#update_plain_conversation.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#update_plain_conversation.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#update_plain_conversation.ApiResponseFor501) | Not implemented                                             |

#### update_plain_conversation.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                             | Description | Notes |
| ---------------------------------------------------------------- | ----------- | ----- |
| [**PlainConversationDto**](../../models/PlainConversationDto.md) |             |

#### update_plain_conversation.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_conversation.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_conversation.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_conversation.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_conversation.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_conversation.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_conversation.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_conversation.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_conversation.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_conversation.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### update_plain_conversation.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
