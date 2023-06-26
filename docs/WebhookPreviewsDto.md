# WebhookPreviewsDto

## Properties

| Name         | Type                                                | Description | Notes      |
| ------------ | --------------------------------------------------- | ----------- | ---------- |
| **previews** | [**List[WebhookPreviewDto]**](WebhookPreviewDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.webhook_previews_dto import WebhookPreviewsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPreviewsDto from a JSON string
webhook_previews_dto_instance = WebhookPreviewsDto.from_json(json)
# print the JSON string representation of the object
print WebhookPreviewsDto.to_json()

# convert the object into a dict
webhook_previews_dto_dict = webhook_previews_dto_instance.to_dict()
# create an instance of WebhookPreviewsDto from a dict
webhook_previews_dto_from_dict = WebhookPreviewsDto.from_dict(webhook_previews_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
