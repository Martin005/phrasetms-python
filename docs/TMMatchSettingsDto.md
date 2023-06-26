# TMMatchSettingsDto

## Properties

| Name                             | Type                                                              | Description                    | Notes      |
| -------------------------------- | ----------------------------------------------------------------- | ------------------------------ | ---------- |
| **context_type**                 | **str**                                                           | Default: PREV_AND_NEXT_SEGMENT | [optional] |
| **prev_or_next_segment**         | **bool**                                                          | Default: false                 | [optional] |
| **penalize_multi_context_match** | **bool**                                                          | Default: false                 | [optional] |
| **ignore_tag_metadata**          | **bool**                                                          | Default: true                  | [optional] |
| **metadata_priority**            | [**MetadataPrioritySettingsDto**](MetadataPrioritySettingsDto.md) |                                | [optional] |

## Example

```python
from phrasetms_client.models.tm_match_settings_dto import TMMatchSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TMMatchSettingsDto from a JSON string
tm_match_settings_dto_instance = TMMatchSettingsDto.from_json(json)
# print the JSON string representation of the object
print TMMatchSettingsDto.to_json()

# convert the object into a dict
tm_match_settings_dto_dict = tm_match_settings_dto_instance.to_dict()
# create an instance of TMMatchSettingsDto from a dict
tm_match_settings_dto_from_dict = TMMatchSettingsDto.from_dict(tm_match_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
