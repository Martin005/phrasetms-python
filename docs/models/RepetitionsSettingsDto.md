# phrasetms_client.model.repetitions_settings_dto.RepetitionsSettingsDto

Repetitions related settings

## Model Type Info

| Input Type                   | Accessed Type          | Description                  | Notes |
| ---------------------------- | ---------------------- | ---------------------------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, | Repetitions related settings |

### Dictionary Keys

| Key                                  | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                              | Notes      |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------- |
| **autoPropagateRepetitions**         | bool,                                                                                                                                       | BoolClass,                                                                              | Propagate repetitions. Default: false                                                                    | [optional] |
| **confirmRepetitions**               | bool,                                                                                                                                       | BoolClass,                                                                              | Set segment status to confirmed for: Repetitions. Default: false                                         | [optional] |
| **autoPropagateToLockedRepetitions** | bool,                                                                                                                                       | BoolClass,                                                                              | Changes in 1st repetition propagate upon confirmation into subsequent locked repetitions. Default: false | [optional] |
| **lockSubsequentRepetitions**        | bool,                                                                                                                                       | BoolClass,                                                                              | If auto-propagated subsequent repetitions should be locked. Default: false                               | [optional] |
| **any_string_name**                  | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                                       | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
