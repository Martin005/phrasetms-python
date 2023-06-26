# MifSettingsDto

## Properties

| Name                                | Type     | Description    | Notes      |
| ----------------------------------- | -------- | -------------- | ---------- |
| **extract_body_pages**              | **bool** | Default: true  | [optional] |
| **extract_reference_pages**         | **bool** | Default: false | [optional] |
| **extract_master_pages**            | **bool** | Default: true  | [optional] |
| **extract_hidden_pages**            | **bool** | Default: false | [optional] |
| **extract_variables**               | **bool** | Default: false | [optional] |
| **extract_index_markers**           | **bool** | Default: true  | [optional] |
| **extract_links**                   | **bool** | Default: false | [optional] |
| **extract_x_ref_def**               | **bool** | Default: false | [optional] |
| **extract_pgf_num_format**          | **bool** | Default: true  | [optional] |
| **extract_custom_reference_pages**  | **bool** | Default: true  | [optional] |
| **extract_default_reference_pages** | **bool** | Default: false | [optional] |
| **extract_used_variables**          | **bool** | Default: true  | [optional] |
| **extract_hidden_cond_text**        | **bool** | Default: false | [optional] |
| **extract_used_x_ref_def**          | **bool** | Default: true  | [optional] |
| **extract_used_pgf_num_format**     | **bool** | Default: true  | [optional] |
| **tag_regexp**                      | **str**  |                | [optional] |

## Example

```python
from phrasetms_client.models.mif_settings_dto import MifSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MifSettingsDto from a JSON string
mif_settings_dto_instance = MifSettingsDto.from_json(json)
# print the JSON string representation of the object
print MifSettingsDto.to_json()

# convert the object into a dict
mif_settings_dto_dict = mif_settings_dto_instance.to_dict()
# create an instance of MifSettingsDto from a dict
mif_settings_dto_from_dict = MifSettingsDto.from_dict(mif_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
