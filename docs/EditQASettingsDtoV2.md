# EditQASettingsDtoV2

## Properties

| Name       | Type                        | Description | Notes      |
| ---------- | --------------------------- | ----------- | ---------- |
| **checks** | **List[Dict[str, object]]** | checks      | [optional] |

## Example

```python
from phrasetms_client.models.edit_qa_settings_dto_v2 import EditQASettingsDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of EditQASettingsDtoV2 from a JSON string
edit_qa_settings_dto_v2_instance = EditQASettingsDtoV2.from_json(json)
# print the JSON string representation of the object
print EditQASettingsDtoV2.to_json()

# convert the object into a dict
edit_qa_settings_dto_v2_dict = edit_qa_settings_dto_v2_instance.to_dict()
# create an instance of EditQASettingsDtoV2 from a dict
edit_qa_settings_dto_v2_from_dict = EditQASettingsDtoV2.from_dict(edit_qa_settings_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
