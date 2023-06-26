# TranslationResourcesDto

## Properties

| Name                           | Type                                                                                | Description | Notes      |
| ------------------------------ | ----------------------------------------------------------------------------------- | ----------- | ---------- |
| **machine_translate_settings** | [**MachineTranslateSettingsReference**](MachineTranslateSettingsReference.md)       |             | [optional] |
| **translation_memories**       | [**List[ProjectTranslationMemoryReference]**](ProjectTranslationMemoryReference.md) |             | [optional] |
| **term_bases**                 | [**List[ProjectTermBaseReference]**](ProjectTermBaseReference.md)                   |             | [optional] |

## Example

```python
from phrasetms_client.models.translation_resources_dto import TranslationResourcesDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationResourcesDto from a JSON string
translation_resources_dto_instance = TranslationResourcesDto.from_json(json)
# print the JSON string representation of the object
print TranslationResourcesDto.to_json()

# convert the object into a dict
translation_resources_dto_dict = translation_resources_dto_instance.to_dict()
# create an instance of TranslationResourcesDto from a dict
translation_resources_dto_from_dict = TranslationResourcesDto.from_dict(translation_resources_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
