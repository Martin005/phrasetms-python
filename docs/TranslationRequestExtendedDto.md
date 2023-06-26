# TranslationRequestExtendedDto

## Properties

| Name             | Type          | Description | Notes      |
| ---------------- | ------------- | ----------- | ---------- |
| **source_texts** | **List[str]** |             |
| **var_from**     | **str**       |             |
| **to**           | **str**       |             |
| **filename**     | **str**       |             | [optional] |

## Example

```python
from phrasetms_client.models.translation_request_extended_dto import TranslationRequestExtendedDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationRequestExtendedDto from a JSON string
translation_request_extended_dto_instance = TranslationRequestExtendedDto.from_json(json)
# print the JSON string representation of the object
print TranslationRequestExtendedDto.to_json()

# convert the object into a dict
translation_request_extended_dto_dict = translation_request_extended_dto_instance.to_dict()
# create an instance of TranslationRequestExtendedDto from a dict
translation_request_extended_dto_from_dict = TranslationRequestExtendedDto.from_dict(translation_request_extended_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
