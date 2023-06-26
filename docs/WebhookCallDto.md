# WebhookCallDto

## Properties

| Name                 | Type                                | Description | Notes      |
| -------------------- | ----------------------------------- | ----------- | ---------- |
| **uid**              | **str**                             |             | [optional] |
| **parent_uid**       | **str**                             |             | [optional] |
| **event_uid**        | **str**                             |             | [optional] |
| **webhook_settings** | [**UidReference**](UidReference.md) |             | [optional] |
| **created_at**       | **datetime**                        |             | [optional] |
| **url**              | **str**                             |             | [optional] |
| **forced**           | **bool**                            |             | [optional] |
| **last_forced_at**   | **datetime**                        |             | [optional] |
| **body**             | **str**                             |             | [optional] |
| **trigger_event**    | **str**                             |             | [optional] |
| **retry_attempt**    | **int**                             |             | [optional] |
| **status_code**      | **int**                             |             | [optional] |
| **error_message**    | **str**                             |             | [optional] |

## Example

```python
from phrasetms_client.models.webhook_call_dto import WebhookCallDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCallDto from a JSON string
webhook_call_dto_instance = WebhookCallDto.from_json(json)
# print the JSON string representation of the object
print WebhookCallDto.to_json()

# convert the object into a dict
webhook_call_dto_dict = webhook_call_dto_instance.to_dict()
# create an instance of WebhookCallDto from a dict
webhook_call_dto_from_dict = WebhookCallDto.from_dict(webhook_call_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
