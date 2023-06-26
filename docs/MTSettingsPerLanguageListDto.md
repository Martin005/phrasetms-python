# MTSettingsPerLanguageListDto

## Properties

| Name                          | Type                                                              | Description | Notes      |
| ----------------------------- | ----------------------------------------------------------------- | ----------- | ---------- |
| **mt_settings_per_lang_list** | [**List[MTSettingsPerLanguageDto]**](MTSettingsPerLanguageDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.mt_settings_per_language_list_dto import MTSettingsPerLanguageListDto

# TODO update the JSON string below
json = "{}"
# create an instance of MTSettingsPerLanguageListDto from a JSON string
mt_settings_per_language_list_dto_instance = MTSettingsPerLanguageListDto.from_json(json)
# print the JSON string representation of the object
print MTSettingsPerLanguageListDto.to_json()

# convert the object into a dict
mt_settings_per_language_list_dto_dict = mt_settings_per_language_list_dto_instance.to_dict()
# create an instance of MTSettingsPerLanguageListDto from a dict
mt_settings_per_language_list_dto_from_dict = MTSettingsPerLanguageListDto.from_dict(mt_settings_per_language_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
