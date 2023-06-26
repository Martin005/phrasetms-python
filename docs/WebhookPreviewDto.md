# WebhookPreviewDto

## Properties

| Name        | Type    | Description | Notes      |
| ----------- | ------- | ----------- | ---------- |
| **event**   | **str** |             | [optional] |
| **preview** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.webhook_preview_dto import WebhookPreviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPreviewDto from a JSON string
webhook_preview_dto_instance = WebhookPreviewDto.from_json(json)
# print the JSON string representation of the object
print WebhookPreviewDto.to_json()

# convert the object into a dict
webhook_preview_dto_dict = webhook_preview_dto_instance.to_dict()
# create an instance of WebhookPreviewDto from a dict
webhook_preview_dto_from_dict = WebhookPreviewDto.from_dict(webhook_preview_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
