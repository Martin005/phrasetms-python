# PageDtoMachineTranslateSettingsPbmDto

## Properties

| Name                   | Type                                                                          | Description | Notes      |
| ---------------------- | ----------------------------------------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                                                       |             | [optional] |
| **total_pages**        | **int**                                                                       |             | [optional] |
| **page_size**          | **int**                                                                       |             | [optional] |
| **page_number**        | **int**                                                                       |             | [optional] |
| **number_of_elements** | **int**                                                                       |             | [optional] |
| **content**            | [**List[MachineTranslateSettingsPbmDto]**](MachineTranslateSettingsPbmDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_machine_translate_settings_pbm_dto import PageDtoMachineTranslateSettingsPbmDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoMachineTranslateSettingsPbmDto from a JSON string
page_dto_machine_translate_settings_pbm_dto_instance = PageDtoMachineTranslateSettingsPbmDto.from_json(json)
# print the JSON string representation of the object
print PageDtoMachineTranslateSettingsPbmDto.to_json()

# convert the object into a dict
page_dto_machine_translate_settings_pbm_dto_dict = page_dto_machine_translate_settings_pbm_dto_instance.to_dict()
# create an instance of PageDtoMachineTranslateSettingsPbmDto from a dict
page_dto_machine_translate_settings_pbm_dto_from_dict = PageDtoMachineTranslateSettingsPbmDto.from_dict(page_dto_machine_translate_settings_pbm_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
