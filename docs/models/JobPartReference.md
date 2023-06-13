# phrasetms_client.model.job_part_reference.JobPartReference

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                                                                                                     |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **uid**                                                   | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **status**                                                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] must be one of ["NEW", "ACCEPTED", "DECLINED", "REJECTED", "DELIVERED", "EMAILED", "COMPLETED", "CANCELLED", ] |
| **[providers](#providers)**                               | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                                                                                                |
| **targetLang**                                            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **workflowLevel**                                         | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 32 bit integer                                                                                 |
| **workflowStep**                                          | [**WorkflowStepReference**](WorkflowStepReference.md)                                                                                       | [**WorkflowStepReference**](WorkflowStepReference.md)                                   |                                                                    | [optional]                                                                                                                |
| **filename**                                              | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **dateDue**                                               | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time                                                                       |
| **dateCreated**                                           | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time                                                                       |
| **updateSourceDate**                                      | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time                                                                       |
| **imported**                                              | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                                                                                                |
| **[jobAssignedEmailTemplate](#jobAssignedEmailTemplate)** | dict, frozendict.frozendict,                                                                                                                | frozendict.frozendict,                                                                  |                                                                    | [optional]                                                                                                                |
| **notificationIntervalInMinutes**                         | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 32 bit integer                                                                                 |
| **continuous**                                            | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                                                                                                |
| **sourceFileUid**                                         | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                                                                                                |
| **any_string_name**                                       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                                                                                                |

# providers

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                    | Input Type                                    | Accessed Type                                 | Description | Notes |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | ----------- | ----- |
| [**ProviderReference**](ProviderReference.md) | [**ProviderReference**](ProviderReference.md) | [**ProviderReference**](ProviderReference.md) |             |

# jobAssignedEmailTemplate

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
