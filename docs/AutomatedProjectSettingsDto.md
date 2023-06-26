# AutomatedProjectSettingsDto

## Properties

| Name              | Type                      | Description | Notes      |
| ----------------- | ------------------------- | ----------- | ---------- |
| **id**            | **str**                   |             | [optional] |
| **name**          | **str**                   |             | [optional] |
| **organization**  | [**NameDto**](NameDto.md) |             | [optional] |
| **active**        | **bool**                  |             | [optional] |
| **source_lang**   | **str**                   |             | [optional] |
| **target_langs**  | **List[str]**             |             | [optional] |
| **connector**     | [**NameDto**](NameDto.md) |             | [optional] |
| **remote_folder** | **str**                   |             | [optional] |

## Example

```python
from phrasetms_client.models.automated_project_settings_dto import AutomatedProjectSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AutomatedProjectSettingsDto from a JSON string
automated_project_settings_dto_instance = AutomatedProjectSettingsDto.from_json(json)
# print the JSON string representation of the object
print AutomatedProjectSettingsDto.to_json()

# convert the object into a dict
automated_project_settings_dto_dict = automated_project_settings_dto_instance.to_dict()
# create an instance of AutomatedProjectSettingsDto from a dict
automated_project_settings_dto_from_dict = AutomatedProjectSettingsDto.from_dict(automated_project_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
