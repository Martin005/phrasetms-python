# phrasetms_client.model.mt_settings_per_language_reference.MTSettingsPerLanguageReference

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                          | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                         | Notes      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------- |
| **targetLang**               | str,                                                                                                                                        | str,                                                                                    | mtSettings is set for whole project if targetLang &#x3D;&#x3D; null |
| **machineTranslateSettings** | [**MachineTranslateSettingsReference**](MachineTranslateSettingsReference.md)                                                               | [**MachineTranslateSettingsReference**](MachineTranslateSettingsReference.md)           |                                                                     | [optional] |
| **any_string_name**          | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type  | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
