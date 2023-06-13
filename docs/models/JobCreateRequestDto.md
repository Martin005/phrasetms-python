# phrasetms_client.model.job_create_request_dto.JobCreateRequestDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                                          | Notes                                               |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **[targetLangs](#targetLangs)**           | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                                                                      |
| **due**                                   | str, datetime,                                                                                                                              | str,                                                                                    | only use for projects without workflows; otherwise specify in the workflowSettings object. Use ISO 8601 date format. | [optional] value must conform to RFC-3339 date-time |
| **[workflowSettings](#workflowSettings)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                                                                      | [optional]                                          |
| **[assignments](#assignments)**           | list, tuple,                                                                                                                                | tuple,                                                                                  | only use for projects without workflows; otherwise specify in the workflowSettings object                            | [optional]                                          |
| **importSettings**                        | [**UidReference**](UidReference.md)                                                                                                         | [**UidReference**](UidReference.md)                                                     |                                                                                                                      | [optional]                                          |
| **useProjectFileImportSettings**          | bool,                                                                                                                                       | BoolClass,                                                                              | Default: false                                                                                                       | [optional]                                          |
| **preTranslate**                          | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                                                                      | [optional]                                          |
| **notifyProvider**                        | [**NotifyProviderDto**](NotifyProviderDto.md)                                                                                               | [**NotifyProviderDto**](NotifyProviderDto.md)                                           |                                                                                                                      | [optional]                                          |
| **callbackUrl**                           | str,                                                                                                                                        | str,                                                                                    |                                                                                                                      | [optional]                                          |
| **path**                                  | str,                                                                                                                                        | str,                                                                                    |                                                                                                                      | [optional]                                          |
| **remoteFile**                            | [**JobCreateRemoteFileDto**](JobCreateRemoteFileDto.md)                                                                                     | [**JobCreateRemoteFileDto**](JobCreateRemoteFileDto.md)                                 |                                                                                                                      | [optional]                                          |
| **any_string_name**                       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                                                   | [optional]                                          |

# targetLangs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# workflowSettings

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                    | Input Type                                                    | Accessed Type                                                 | Description | Notes |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ----------- | ----- |
| [**WorkflowStepConfiguration**](WorkflowStepConfiguration.md) | [**WorkflowStepConfiguration**](WorkflowStepConfiguration.md) | [**WorkflowStepConfiguration**](WorkflowStepConfiguration.md) |             |

# assignments

only use for projects without workflows; otherwise specify in the workflowSettings object

## Model Type Info

| Input Type   | Accessed Type | Description                                                                               | Notes |
| ------------ | ------------- | ----------------------------------------------------------------------------------------- | ----- |
| list, tuple, | tuple,        | only use for projects without workflows; otherwise specify in the workflowSettings object |

### Tuple Items

| Class Name                                          | Input Type                                          | Accessed Type                                       | Description | Notes |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | ----------- | ----- |
| [**ProvidersPerLanguage**](ProvidersPerLanguage.md) | [**ProvidersPerLanguage**](ProvidersPerLanguage.md) | [**ProvidersPerLanguage**](ProvidersPerLanguage.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
