# InconsistentTranslationWarningDto

## Properties

| Name           | Type    | Description | Notes      |
| -------------- | ------- | ----------- | ---------- |
| **segment_id** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.inconsistent_translation_warning_dto import InconsistentTranslationWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of InconsistentTranslationWarningDto from a JSON string
inconsistent_translation_warning_dto_instance = InconsistentTranslationWarningDto.from_json(json)
# print the JSON string representation of the object
print InconsistentTranslationWarningDto.to_json()

# convert the object into a dict
inconsistent_translation_warning_dto_dict = inconsistent_translation_warning_dto_instance.to_dict()
# create an instance of InconsistentTranslationWarningDto from a dict
inconsistent_translation_warning_dto_from_dict = InconsistentTranslationWarningDto.from_dict(inconsistent_translation_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
