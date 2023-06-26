# PreviewUrlDto

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **type** | **str** |             | [optional] |
| **url**  | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.preview_url_dto import PreviewUrlDto

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewUrlDto from a JSON string
preview_url_dto_instance = PreviewUrlDto.from_json(json)
# print the JSON string representation of the object
print PreviewUrlDto.to_json()

# convert the object into a dict
preview_url_dto_dict = preview_url_dto_instance.to_dict()
# create an instance of PreviewUrlDto from a dict
preview_url_dto_from_dict = PreviewUrlDto.from_dict(preview_url_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
