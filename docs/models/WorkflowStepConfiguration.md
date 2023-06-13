# phrasetms_client.model.workflow_step_configuration.WorkflowStepConfiguration

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                             | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| **[assignments](#assignments)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    |
| **id**                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **due**                         | str, datetime,                                                                                                                              | str,                                                                                    | Use ISO 8601 date format.                                          | [optional] value must conform to RFC-3339 date-time |
| **notifyProvider**              | [**NotifyProviderDto**](NotifyProviderDto.md)                                                                                               | [**NotifyProviderDto**](NotifyProviderDto.md)                                           |                                                                    | [optional]                                          |
| **any_string_name**             | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                          |

# assignments

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                          | Input Type                                          | Accessed Type                                       | Description | Notes |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | ----------- | ----- |
| [**ProvidersPerLanguage**](ProvidersPerLanguage.md) | [**ProvidersPerLanguage**](ProvidersPerLanguage.md) | [**ProvidersPerLanguage**](ProvidersPerLanguage.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
