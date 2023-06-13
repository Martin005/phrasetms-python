# phrasetms_client.model.project_translation_memory_reference.ProjectTranslationMemoryReference

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                               | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------- |
| **id**                            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                              |
| **[transMem](#transMem)**         | dict, frozendict.frozendict,                                                                                                                | frozendict.frozendict,                                                                  |                                                                    | [optional]                              |
| **name**                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                              |
| **[workflowStep](#workflowStep)** | dict, frozendict.frozendict,                                                                                                                | frozendict.frozendict,                                                                  |                                                                    | [optional]                              |
| **targetLang**                    | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                              |
| **penalty**                       | decimal.Decimal, int, float,                                                                                                                | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 64 bit float |
| **readMode**                      | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                              |
| **any_string_name**               | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                              |

# transMem

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

# workflowStep

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
