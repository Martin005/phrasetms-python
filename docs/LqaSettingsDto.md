# LqaSettingsDto

## Properties

| Name           | Type                                                    | Description | Notes      |
| -------------- | ------------------------------------------------------- | ----------- | ---------- |
| **enabled**    | **bool**                                                |             | [optional] |
| **severities** | [**List[LqaSeverityDto]**](LqaSeverityDto.md)           |             | [optional] |
| **categories** | [**List[LqaErrorCategoryDto]**](LqaErrorCategoryDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.lqa_settings_dto import LqaSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of LqaSettingsDto from a JSON string
lqa_settings_dto_instance = LqaSettingsDto.from_json(json)
# print the JSON string representation of the object
print LqaSettingsDto.to_json()

# convert the object into a dict
lqa_settings_dto_dict = lqa_settings_dto_instance.to_dict()
# create an instance of LqaSettingsDto from a dict
lqa_settings_dto_from_dict = LqaSettingsDto.from_dict(lqa_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
