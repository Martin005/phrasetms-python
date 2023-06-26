# QASettingsDtoV2

## Properties

| Name       | Type                                      | Description | Notes      |
| ---------- | ----------------------------------------- | ----------- | ---------- |
| **checks** | [**List[QACheckDtoV2]**](QACheckDtoV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.qa_settings_dto_v2 import QASettingsDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of QASettingsDtoV2 from a JSON string
qa_settings_dto_v2_instance = QASettingsDtoV2.from_json(json)
# print the JSON string representation of the object
print QASettingsDtoV2.to_json()

# convert the object into a dict
qa_settings_dto_v2_dict = qa_settings_dto_v2_instance.to_dict()
# create an instance of QASettingsDtoV2 from a dict
qa_settings_dto_v2_from_dict = QASettingsDtoV2.from_dict(qa_settings_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
