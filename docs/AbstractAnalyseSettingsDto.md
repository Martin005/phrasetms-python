# AbstractAnalyseSettingsDto

Base analyseSettingsDto

## Properties

| Name                              | Type     | Description                                                                      | Notes      |
| --------------------------------- | -------- | -------------------------------------------------------------------------------- | ---------- |
| **type**                          | **str**  | Response differs based on analyse type                                           | [optional] |
| **include_confirmed_segments**    | **bool** | Default: false                                                                   | [optional] |
| **include_numbers**               | **bool** | Default: false                                                                   | [optional] |
| **include_locked_segments**       | **bool** | Default: false                                                                   | [optional] |
| **count_source_units**            | **bool** | Default: false                                                                   | [optional] |
| **include_trans_memory**          | **bool** | Default: false                                                                   | [optional] |
| **naming_pattern**                | **str**  |                                                                                  | [optional] |
| **analyze_by_language**           | **bool** | Default: false                                                                   | [optional] |
| **analyze_by_provider**           | **bool** | Default: false                                                                   | [optional] |
| **allow_automatic_post_analysis** | **bool** | If automatic post analysis should be created after update source. Default: false | [optional] |

## Example

```python
from phrasetms_client.models.abstract_analyse_settings_dto import AbstractAnalyseSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractAnalyseSettingsDto from a JSON string
abstract_analyse_settings_dto_instance = AbstractAnalyseSettingsDto.from_json(json)
# print the JSON string representation of the object
print AbstractAnalyseSettingsDto.to_json()

# convert the object into a dict
abstract_analyse_settings_dto_dict = abstract_analyse_settings_dto_instance.to_dict()
# create an instance of AbstractAnalyseSettingsDto from a dict
abstract_analyse_settings_dto_from_dict = AbstractAnalyseSettingsDto.from_dict(abstract_analyse_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
