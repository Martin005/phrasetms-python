# TranslationDto

## Properties

| Name     | Type    | Description | Notes |
| -------- | ------- | ----------- | ----- |
| **lang** | **str** |             |
| **text** | **str** |             |

## Example

```python
from phrasetms_client.models.translation_dto import TranslationDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationDto from a JSON string
translation_dto_instance = TranslationDto.from_json(json)
# print the JSON string representation of the object
print TranslationDto.to_json()

# convert the object into a dict
translation_dto_dict = translation_dto_instance.to_dict()
# create an instance of TranslationDto from a dict
translation_dto_from_dict = TranslationDto.from_dict(translation_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
