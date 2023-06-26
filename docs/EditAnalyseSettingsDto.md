# EditAnalyseSettingsDto

## Properties

| Name                                    | Type     | Description                                               | Notes      |
| --------------------------------------- | -------- | --------------------------------------------------------- | ---------- |
| **type**                                | **str**  |                                                           | [optional] |
| **include_fuzzy_repetitions**           | **bool** | Default: false                                            | [optional] |
| **separate_fuzzy_repetitions**          | **bool** | Default: false                                            | [optional] |
| **include_non_translatables**           | **bool** | Default: false                                            | [optional] |
| **include_machine_translation_matches** | **bool** | Default: false                                            | [optional] |
| **include_confirmed_segments**          | **bool** | Default: false                                            | [optional] |
| **include_numbers**                     | **bool** | Default: false                                            | [optional] |
| **include_locked_segments**             | **bool** | Default: false                                            | [optional] |
| **trans_memory_post_editing**           | **bool** | Default: false                                            | [optional] |
| **non_translatable_post_editing**       | **bool** | Default: false                                            | [optional] |
| **machine_translate_post_editing**      | **bool** | Default: false                                            | [optional] |
| **count_source_units**                  | **bool** | Default: false                                            | [optional] |
| **include_trans_memory**                | **bool** | Default: false                                            | [optional] |
| **naming_pattern**                      | **str**  |                                                           | [optional] |
| **analyze_by_language**                 | **bool** | Mutually exclusive with analyzeByProvider. Default: false | [optional] |
| **analyze_by_provider**                 | **bool** | Mutually exclusive with analyzeByLanguage. Default: true  | [optional] |
| **allow_automatic_post_analysis**       | **bool** | Default: false                                            | [optional] |

## Example

```python
from phrasetms_client.models.edit_analyse_settings_dto import EditAnalyseSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditAnalyseSettingsDto from a JSON string
edit_analyse_settings_dto_instance = EditAnalyseSettingsDto.from_json(json)
# print the JSON string representation of the object
print EditAnalyseSettingsDto.to_json()

# convert the object into a dict
edit_analyse_settings_dto_dict = edit_analyse_settings_dto_instance.to_dict()
# create an instance of EditAnalyseSettingsDto from a dict
edit_analyse_settings_dto_from_dict = EditAnalyseSettingsDto.from_dict(edit_analyse_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
