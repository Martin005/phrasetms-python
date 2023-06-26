# MTSettingsPerLanguageReference

## Properties

| Name                           | Type                                                                          | Description                                                         | Notes      |
| ------------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------- |
| **target_lang**                | **str**                                                                       | mtSettings is set for whole project if targetLang &#x3D;&#x3D; null |
| **machine_translate_settings** | [**MachineTranslateSettingsReference**](MachineTranslateSettingsReference.md) |                                                                     | [optional] |

## Example

```python
from phrasetms_client.models.mt_settings_per_language_reference import MTSettingsPerLanguageReference

# TODO update the JSON string below
json = "{}"
# create an instance of MTSettingsPerLanguageReference from a JSON string
mt_settings_per_language_reference_instance = MTSettingsPerLanguageReference.from_json(json)
# print the JSON string representation of the object
print MTSettingsPerLanguageReference.to_json()

# convert the object into a dict
mt_settings_per_language_reference_dict = mt_settings_per_language_reference_instance.to_dict()
# create an instance of MTSettingsPerLanguageReference from a dict
mt_settings_per_language_reference_from_dict = MTSettingsPerLanguageReference.from_dict(mt_settings_per_language_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
