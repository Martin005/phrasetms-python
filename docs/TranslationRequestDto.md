# TranslationRequestDto

## Properties

| Name             | Type          | Description | Notes |
| ---------------- | ------------- | ----------- | ----- |
| **source_texts** | **List[str]** |             |

## Example

```python
from phrasetms_client.models.translation_request_dto import TranslationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationRequestDto from a JSON string
translation_request_dto_instance = TranslationRequestDto.from_json(json)
# print the JSON string representation of the object
print TranslationRequestDto.to_json()

# convert the object into a dict
translation_request_dto_dict = translation_request_dto_instance.to_dict()
# create an instance of TranslationRequestDto from a dict
translation_request_dto_from_dict = TranslationRequestDto.from_dict(translation_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
