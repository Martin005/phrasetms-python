# EditProjectMTSettPerLangDto

## Properties

| Name                           | Type                              | Description | Notes      |
| ------------------------------ | --------------------------------- | ----------- | ---------- |
| **target_lang**                | **str**                           |             |
| **machine_translate_settings** | [**IdReference**](IdReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.edit_project_mt_sett_per_lang_dto import EditProjectMTSettPerLangDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditProjectMTSettPerLangDto from a JSON string
edit_project_mt_sett_per_lang_dto_instance = EditProjectMTSettPerLangDto.from_json(json)
# print the JSON string representation of the object
print EditProjectMTSettPerLangDto.to_json()

# convert the object into a dict
edit_project_mt_sett_per_lang_dto_dict = edit_project_mt_sett_per_lang_dto_instance.to_dict()
# create an instance of EditProjectMTSettPerLangDto from a dict
edit_project_mt_sett_per_lang_dto_from_dict = EditProjectMTSettPerLangDto.from_dict(edit_project_mt_sett_per_lang_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
