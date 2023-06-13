# phrasetms_client.model.machine_translate_settings_pbm_dto.MachineTranslateSettingsPbmDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                     | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------- |
| **id**                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **uid**                 | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **baseName**            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **name**                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **type**                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                |
| **default\_**           | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                |
| **includeTags**         | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                |
| **mtQualityEstimation** | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                |
| **[args](#args)**       | dict, frozendict.frozendict,                                                                                                                | frozendict.frozendict,                                                                  |                                                                    | [optional]                                |
| **payForMtPossible**    | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                |
| **payForMtActive**      | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                |
| **charCount**           | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 32 bit integer |
| **sharingSettings**     | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 32 bit integer |
| **langs**               | [**MachineTranslateSettingsLangsDto**](MachineTranslateSettingsLangsDto.md)                                                                 | [**MachineTranslateSettingsLangsDto**](MachineTranslateSettingsLangsDto.md)             |                                                                    | [optional]                                |
| **any_string_name**     | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                |

# args

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                 | Input Type | Accessed Type | Description                                                        | Notes      |
| ------------------- | ---------- | ------------- | ------------------------------------------------------------------ | ---------- |
| **any_string_name** | str,       | str,          | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
