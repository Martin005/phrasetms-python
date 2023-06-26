# ProjectMTSettingsPerLangDto

## Properties

| Name                           | Type                                | Description | Notes      |
| ------------------------------ | ----------------------------------- | ----------- | ---------- |
| **target_lang**                | **str**                             |             |
| **machine_translate_settings** | [**UidReference**](UidReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.project_mt_settings_per_lang_dto import ProjectMTSettingsPerLangDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMTSettingsPerLangDto from a JSON string
project_mt_settings_per_lang_dto_instance = ProjectMTSettingsPerLangDto.from_json(json)
# print the JSON string representation of the object
print ProjectMTSettingsPerLangDto.to_json()

# convert the object into a dict
project_mt_settings_per_lang_dto_dict = project_mt_settings_per_lang_dto_instance.to_dict()
# create an instance of ProjectMTSettingsPerLangDto from a dict
project_mt_settings_per_lang_dto_from_dict = ProjectMTSettingsPerLangDto.from_dict(project_mt_settings_per_lang_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
