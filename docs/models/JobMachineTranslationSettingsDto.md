# phrasetms_client.model.job_machine_translation_settings_dto.JobMachineTranslationSettingsDto

Machine translation related settings

## Model Type Info

| Input Type                   | Accessed Type          | Description                          | Notes |
| ---------------------------- | ---------------------- | ------------------------------------ | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, | Machine translation related settings |

### Dictionary Keys

| Key                          | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                            | Notes      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------- |
| **useMachineTranslation**    | bool,                                                                                                                                       | BoolClass,                                                                              | Pre-translate from machine translation. Default: true                                                  | [optional] |
| **lock100PercentMatches**    | bool,                                                                                                                                       | BoolClass,                                                                              | Lock section: 100% machine translation matches. Default: false                                         | [optional] |
| **confirm100PercentMatches** | bool,                                                                                                                                       | BoolClass,                                                                              | Set segment status to confirmed for: 100% translation machine matches. Default: false                  | [optional] |
| **useAltTransOnly**          | bool,                                                                                                                                       | BoolClass,                                                                              | Do not put machine translations to target and use alt-trans fields (alt-trans in mxlf). Default: false | [optional] |
| **any_string_name**          | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                                     | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
