# EditProjectMTSettPerLangListDto

## Properties

| Name                          | Type                                                                    | Description | Notes      |
| ----------------------------- | ----------------------------------------------------------------------- | ----------- | ---------- |
| **mt_settings_per_lang_list** | [**List[EditProjectMTSettPerLangDto]**](EditProjectMTSettPerLangDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.edit_project_mt_sett_per_lang_list_dto import EditProjectMTSettPerLangListDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditProjectMTSettPerLangListDto from a JSON string
edit_project_mt_sett_per_lang_list_dto_instance = EditProjectMTSettPerLangListDto.from_json(json)
# print the JSON string representation of the object
print EditProjectMTSettPerLangListDto.to_json()

# convert the object into a dict
edit_project_mt_sett_per_lang_list_dto_dict = edit_project_mt_sett_per_lang_list_dto_instance.to_dict()
# create an instance of EditProjectMTSettPerLangListDto from a dict
edit_project_mt_sett_per_lang_list_dto_from_dict = EditProjectMTSettPerLangListDto.from_dict(edit_project_mt_sett_per_lang_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
