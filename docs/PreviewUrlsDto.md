# PreviewUrlsDto

## Properties

| Name         | Type                                        | Description | Notes      |
| ------------ | ------------------------------------------- | ----------- | ---------- |
| **previews** | [**List[PreviewUrlDto]**](PreviewUrlDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.preview_urls_dto import PreviewUrlsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewUrlsDto from a JSON string
preview_urls_dto_instance = PreviewUrlsDto.from_json(json)
# print the JSON string representation of the object
print PreviewUrlsDto.to_json()

# convert the object into a dict
preview_urls_dto_dict = preview_urls_dto_instance.to_dict()
# create an instance of PreviewUrlsDto from a dict
preview_urls_dto_from_dict = PreviewUrlsDto.from_dict(preview_urls_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
