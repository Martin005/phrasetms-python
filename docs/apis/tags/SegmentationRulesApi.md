<a id="__pageTop"></a>

# phrasetms_client.apis.tags.segmentation_rules_api.SegmentationRulesApi

All URIs are relative to *https://cloud.memsource.com/web*

| Method                                                                | HTTP request                                      | Description              |
| --------------------------------------------------------------------- | ------------------------------------------------- | ------------------------ |
| [**create_segmentation_rule**](#create_segmentation_rule)             | **post** /api2/v1/segmentationRules               | Create segmentation rule |
| [**deletes_segmentation_rule**](#deletes_segmentation_rule)           | **delete** /api2/v1/segmentationRules/{segRuleId} | Delete segmentation rule |
| [**get_list_of_segmentation_rules**](#get_list_of_segmentation_rules) | **get** /api2/v1/segmentationRules                | List segmentation rules  |
| [**get_segmentation_rule**](#get_segmentation_rule)                   | **get** /api2/v1/segmentationRules/{segRuleId}    | Get segmentation rule    |
| [**updates_segmentation_rule**](#updates_segmentation_rule)           | **put** /api2/v1/segmentationRules/{segRuleId}    | Edit segmentation rule   |

# **create_segmentation_rule**

<a id="create_segmentation_rule"></a>

> SegmentationRuleDto create_segmentation_rule(seg_rulebody)

Create segmentation rule

Creates new Segmentation Rule with file and segRule JSON Object as header parameter. The same object is used for GET action.

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import segmentation_rules_api
from phrasetms_client.model.segmentation_rule_dto import SegmentationRuleDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segmentation_rules_api.SegmentationRulesApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'segRule': "{name:'name', locale:'en', primary:'false', filename:'extra_file.xml'}",
    }
    body = dict()
    try:
        # Create segmentation rule
        api_response = api_instance.create_segmentation_rule(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SegmentationRulesApi->create_segmentation_rule: %s\n" % e)
```

### Parameters

| Name                 | Type                                                     | Description                                     | Notes                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body                 | typing.Union[SchemaForRequestBodyApplicationOctetStream] | required                                        |
| header_params        | RequestHeaderParams                                      |                                                 |
| content_type         | str                                                      | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body                                                                                                                                           |
| accept_content_types | typing.Tuple[str]                                        | default is ('application/json', )               | Tells the server the content type(s) that are accepted by the client                                                                                                                               |
| stream               | bool                                                     | default is False                                | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file |
| timeout              | typing.Optional[typing.Union[int, typing.Tuple]]         | default is None                                 | the timeout used by the rest client                                                                                                                                                                |
| skip_deserialization | bool                                                     | default is False                                | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned                                                                         |

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### header_params

#### RequestHeaderParams

| Name    | Type          | Description | Notes |
| ------- | ------------- | ----------- | ----- |
| segRule | SegRuleSchema |             |

# SegRuleSchema

## Model Type Info

| Input Type | Accessed Type | Description | Notes |
| ---------- | ------------- | ----------- | ----- |
| str,       | str,          |             |

### Return Types, Responses

| Code | Class                                                            | Description                                                 |
| ---- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                     | When skip_deserialization is True this response is returned |
| 201  | [ApiResponseFor201](#create_segmentation_rule.ApiResponseFor201) | Created                                                     |
| 400  | [ApiResponseFor400](#create_segmentation_rule.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#create_segmentation_rule.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#create_segmentation_rule.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#create_segmentation_rule.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#create_segmentation_rule.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#create_segmentation_rule.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#create_segmentation_rule.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#create_segmentation_rule.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#create_segmentation_rule.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#create_segmentation_rule.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#create_segmentation_rule.ApiResponseFor501) | Not implemented                                             |

#### create_segmentation_rule.ApiResponseFor201

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**SegmentationRuleDto**](../../models/SegmentationRuleDto.md) |             |

#### create_segmentation_rule.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segmentation_rule.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segmentation_rule.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segmentation_rule.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segmentation_rule.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segmentation_rule.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segmentation_rule.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segmentation_rule.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segmentation_rule.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segmentation_rule.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### create_segmentation_rule.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **deletes_segmentation_rule**

<a id="deletes_segmentation_rule"></a>

> deletes_segmentation_rule(seg_rule_id)

Delete segmentation rule

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import segmentation_rules_api
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segmentation_rules_api.SegmentationRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'segRuleId': 1,
    }
    try:
        # Delete segmentation rule
        api_response = api_instance.deletes_segmentation_rule(
            path_params=path_params,
        )
    except phrasetms_client.ApiException as e:
        print("Exception when calling SegmentationRulesApi->deletes_segmentation_rule: %s\n" % e)
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

| Name      | Type            | Description | Notes |
| --------- | --------------- | ----------- | ----- |
| segRuleId | SegRuleIdSchema |             |

# SegRuleIdSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 64 bit integer |

### Return Types, Responses

| Code | Class                                                             | Description                                                 |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| 204  | [ApiResponseFor204](#deletes_segmentation_rule.ApiResponseFor204) | No Content                                                  |
| 400  | [ApiResponseFor400](#deletes_segmentation_rule.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#deletes_segmentation_rule.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#deletes_segmentation_rule.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#deletes_segmentation_rule.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#deletes_segmentation_rule.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#deletes_segmentation_rule.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#deletes_segmentation_rule.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#deletes_segmentation_rule.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#deletes_segmentation_rule.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#deletes_segmentation_rule.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#deletes_segmentation_rule.ApiResponseFor501) | Not implemented                                             |

#### deletes_segmentation_rule.ApiResponseFor204

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### deletes_segmentation_rule.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_list_of_segmentation_rules**

<a id="get_list_of_segmentation_rules"></a>

> PageDtoSegmentationRuleReference get_list_of_segmentation_rules()

List segmentation rules

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import segmentation_rules_api
from phrasetms_client.model.page_dto_segmentation_rule_reference import PageDtoSegmentationRuleReference
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segmentation_rules_api.SegmentationRulesApi(api_client)

    # example passing only optional values
    query_params = {
        'locales': [
        "locales_example"
    ],
        'pageNumber': 0,
        'pageSize': 50,
    }
    try:
        # List segmentation rules
        api_response = api_instance.get_list_of_segmentation_rules(
            query_params=query_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SegmentationRulesApi->get_list_of_segmentation_rules: %s\n" % e)
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
| locales    | LocalesSchema    |             | optional |
| pageNumber | PageNumberSchema |             | optional |
| pageSize   | PageSizeSchema   |             | optional |

# LocalesSchema

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

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

| Code | Class                                                                  | Description                                                 |
| ---- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                           | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_list_of_segmentation_rules.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_list_of_segmentation_rules.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_list_of_segmentation_rules.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_list_of_segmentation_rules.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_list_of_segmentation_rules.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_list_of_segmentation_rules.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_list_of_segmentation_rules.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_list_of_segmentation_rules.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_list_of_segmentation_rules.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_list_of_segmentation_rules.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_list_of_segmentation_rules.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_list_of_segmentation_rules.ApiResponseFor501) | Not implemented                                             |

#### get_list_of_segmentation_rules.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                                                     | Description | Notes |
| ---------------------------------------------------------------------------------------- | ----------- | ----- |
| [**PageDtoSegmentationRuleReference**](../../models/PageDtoSegmentationRuleReference.md) |             |

#### get_list_of_segmentation_rules.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_segmentation_rules.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_segmentation_rules.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_segmentation_rules.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_segmentation_rules.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_segmentation_rules.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_segmentation_rules.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_segmentation_rules.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_segmentation_rules.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_segmentation_rules.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_list_of_segmentation_rules.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_segmentation_rule**

<a id="get_segmentation_rule"></a>

> SegmentationRuleDto get_segmentation_rule(seg_rule_id)

Get segmentation rule

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import segmentation_rules_api
from phrasetms_client.model.segmentation_rule_dto import SegmentationRuleDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segmentation_rules_api.SegmentationRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'segRuleId': 1,
    }
    try:
        # Get segmentation rule
        api_response = api_instance.get_segmentation_rule(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SegmentationRulesApi->get_segmentation_rule: %s\n" % e)
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

| Name      | Type            | Description | Notes |
| --------- | --------------- | ----------- | ----- |
| segRuleId | SegRuleIdSchema |             |

# SegRuleIdSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 64 bit integer |

### Return Types, Responses

| Code | Class                                                         | Description                                                 |
| ---- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                  | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#get_segmentation_rule.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#get_segmentation_rule.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#get_segmentation_rule.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#get_segmentation_rule.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#get_segmentation_rule.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#get_segmentation_rule.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#get_segmentation_rule.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#get_segmentation_rule.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#get_segmentation_rule.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#get_segmentation_rule.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#get_segmentation_rule.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#get_segmentation_rule.ApiResponseFor501) | Not implemented                                             |

#### get_segmentation_rule.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**SegmentationRuleDto**](../../models/SegmentationRuleDto.md) |             |

#### get_segmentation_rule.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segmentation_rule.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segmentation_rule.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segmentation_rule.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segmentation_rule.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segmentation_rule.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segmentation_rule.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segmentation_rule.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segmentation_rule.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segmentation_rule.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### get_segmentation_rule.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **updates_segmentation_rule**

<a id="updates_segmentation_rule"></a>

> SegmentationRuleDto updates_segmentation_rule(seg_rule_id)

Edit segmentation rule

### Example

```python
import phrasetms_client
from phrasetms_client.apis.tags import segmentation_rules_api
from phrasetms_client.model.segmentation_rule_dto import SegmentationRuleDto
from phrasetms_client.model.edit_segmentation_rule_dto import EditSegmentationRuleDto
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.memsource.com/web
# See configuration.py for a list of all supported configuration parameters.
configuration = phrasetms_client.Configuration(
    host = "https://cloud.memsource.com/web"
)

# Enter a context with an instance of the API client
with phrasetms_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segmentation_rules_api.SegmentationRulesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'segRuleId': 1,
    }
    try:
        # Edit segmentation rule
        api_response = api_instance.updates_segmentation_rule(
            path_params=path_params,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SegmentationRulesApi->updates_segmentation_rule: %s\n" % e)

    # example passing only optional values
    path_params = {
        'segRuleId': 1,
    }
    body = EditSegmentationRuleDto(
        name="name_example",
        primary=True,
    )
    try:
        # Edit segmentation rule
        api_response = api_instance.updates_segmentation_rule(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phrasetms_client.ApiException as e:
        print("Exception when calling SegmentationRulesApi->updates_segmentation_rule: %s\n" % e)
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

| Type                                                                   | Description | Notes |
| ---------------------------------------------------------------------- | ----------- | ----- |
| [**EditSegmentationRuleDto**](../../models/EditSegmentationRuleDto.md) |             |

### path_params

#### RequestPathParams

| Name      | Type            | Description | Notes |
| --------- | --------------- | ----------- | ----- |
| segRuleId | SegRuleIdSchema |             |

# SegRuleIdSchema

## Model Type Info

| Input Type            | Accessed Type    | Description | Notes                          |
| --------------------- | ---------------- | ----------- | ------------------------------ |
| decimal.Decimal, int, | decimal.Decimal, |             | value must be a 64 bit integer |

### Return Types, Responses

| Code | Class                                                             | Description                                                 |
| ---- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| n/a  | api_client.ApiResponseWithoutDeserialization                      | When skip_deserialization is True this response is returned |
| 200  | [ApiResponseFor200](#updates_segmentation_rule.ApiResponseFor200) | successful operation                                        |
| 400  | [ApiResponseFor400](#updates_segmentation_rule.ApiResponseFor400) | Bad request                                                 |
| 401  | [ApiResponseFor401](#updates_segmentation_rule.ApiResponseFor401) | Not authorized                                              |
| 403  | [ApiResponseFor403](#updates_segmentation_rule.ApiResponseFor403) | Forbidden                                                   |
| 404  | [ApiResponseFor404](#updates_segmentation_rule.ApiResponseFor404) | Resource not found                                          |
| 405  | [ApiResponseFor405](#updates_segmentation_rule.ApiResponseFor405) | Method not allowed                                          |
| 408  | [ApiResponseFor408](#updates_segmentation_rule.ApiResponseFor408) | Timeout                                                     |
| 410  | [ApiResponseFor410](#updates_segmentation_rule.ApiResponseFor410) | Gone                                                        |
| 415  | [ApiResponseFor415](#updates_segmentation_rule.ApiResponseFor415) | Unsupported media type                                      |
| 429  | [ApiResponseFor429](#updates_segmentation_rule.ApiResponseFor429) | Too many requests                                           |
| 500  | [ApiResponseFor500](#updates_segmentation_rule.ApiResponseFor500) | Internal server error                                       |
| 501  | [ApiResponseFor501](#updates_segmentation_rule.ApiResponseFor501) | Not implemented                                             |

#### updates_segmentation_rule.ApiResponseFor200

| Name     | Type                                                    | Description              | Notes |
| -------- | ------------------------------------------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse                                    | Raw response             |
| body     | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |                          |
| headers  | Unset                                                   | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

| Type                                                           | Description | Notes |
| -------------------------------------------------------------- | ----------- | ----- |
| [**SegmentationRuleDto**](../../models/SegmentationRuleDto.md) |             |

#### updates_segmentation_rule.ApiResponseFor400

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### updates_segmentation_rule.ApiResponseFor401

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### updates_segmentation_rule.ApiResponseFor403

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### updates_segmentation_rule.ApiResponseFor404

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### updates_segmentation_rule.ApiResponseFor405

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### updates_segmentation_rule.ApiResponseFor408

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### updates_segmentation_rule.ApiResponseFor410

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### updates_segmentation_rule.ApiResponseFor415

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### updates_segmentation_rule.ApiResponseFor429

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### updates_segmentation_rule.ApiResponseFor500

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

#### updates_segmentation_rule.ApiResponseFor501

| Name     | Type                 | Description              | Notes |
| -------- | -------------------- | ------------------------ | ----- |
| response | urllib3.HTTPResponse | Raw response             |
| body     | typing.Union[]       |                          |
| headers  | Unset                | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#\_\_pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
