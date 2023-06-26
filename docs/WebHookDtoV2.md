# WebHookDtoV2

## Properties

| Name                 | Type                                  | Description    | Notes      |
| -------------------- | ------------------------------------- | -------------- | ---------- |
| **name**             | **str**                               |                | [optional] |
| **id**               | **str**                               |                | [optional] |
| **uid**              | **str**                               |                | [optional] |
| **url**              | **str**                               |                |
| **events**           | **List[str]**                         |                | [optional] |
| **secret_token**     | **str**                               |                | [optional] |
| **hidden**           | **bool**                              | Default: false | [optional] |
| **status**           | **str**                               |                | [optional] |
| **failed_attempts**  | **int**                               |                | [optional] |
| **created**          | **datetime**                          |                | [optional] |
| **created_by**       | [**UserReference**](UserReference.md) |                | [optional] |
| **last_modified**    | **datetime**                          |                | [optional] |
| **last_modified_by** | [**UserReference**](UserReference.md) |                | [optional] |

## Example

```python
from phrasetms_client.models.web_hook_dto_v2 import WebHookDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookDtoV2 from a JSON string
web_hook_dto_v2_instance = WebHookDtoV2.from_json(json)
# print the JSON string representation of the object
print WebHookDtoV2.to_json()

# convert the object into a dict
web_hook_dto_v2_dict = web_hook_dto_v2_instance.to_dict()
# create an instance of WebHookDtoV2 from a dict
web_hook_dto_v2_from_dict = WebHookDtoV2.from_dict(web_hook_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
