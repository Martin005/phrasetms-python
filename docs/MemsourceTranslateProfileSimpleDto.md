# MemsourceTranslateProfileSimpleDto

## Properties

| Name                    | Type                                                                              | Description | Notes      |
| ----------------------- | --------------------------------------------------------------------------------- | ----------- | ---------- |
| **uid**                 | **str**                                                                           |             | [optional] |
| **name**                | **str**                                                                           |             | [optional] |
| **date_created**        | **datetime**                                                                      |             | [optional] |
| **created_by**          | [**UserReference**](UserReference.md)                                             |             | [optional] |
| **memsource_translate** | [**MemTransMachineTranslateSettingsDto**](MemTransMachineTranslateSettingsDto.md) |             | [optional] |
| **locked**              | **bool**                                                                          |             | [optional] |

## Example

```python
from phrasetms_client.models.memsource_translate_profile_simple_dto import MemsourceTranslateProfileSimpleDto

# TODO update the JSON string below
json = "{}"
# create an instance of MemsourceTranslateProfileSimpleDto from a JSON string
memsource_translate_profile_simple_dto_instance = MemsourceTranslateProfileSimpleDto.from_json(json)
# print the JSON string representation of the object
print MemsourceTranslateProfileSimpleDto.to_json()

# convert the object into a dict
memsource_translate_profile_simple_dto_dict = memsource_translate_profile_simple_dto_instance.to_dict()
# create an instance of MemsourceTranslateProfileSimpleDto from a dict
memsource_translate_profile_simple_dto_from_dict = MemsourceTranslateProfileSimpleDto.from_dict(memsource_translate_profile_simple_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
