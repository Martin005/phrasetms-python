# phrasetms_client.model.create_project_v3_dto.CreateProjectV3Dto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                               |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| **sourceLang**                      | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **name**                            | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **[targetLangs](#targetLangs)**     | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    |
| **client**                          | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **businessUnit**                    | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **domain**                          | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **subDomain**                       | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **costCenter**                      | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **purchaseOrder**                   | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **[workflowSteps](#workflowSteps)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **dateDue**                         | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **note**                            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **[lqaProfiles](#lqaProfiles)**     | list, tuple,                                                                                                                                | tuple,                                                                                  | Lqa profiles that will be added to workflow steps                  | [optional]                                          |
| **[customFields](#customFields)**   | list, tuple,                                                                                                                                | tuple,                                                                                  | Custom fields for project                                          | [optional]                                          |
| **fileHandover**                    | bool,                                                                                                                                       | BoolClass,                                                                              | Default: false                                                     | [optional]                                          |
| **any_string_name**                 | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                          |

# targetLangs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# workflowSteps

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                        | Input Type                        | Accessed Type                     | Description | Notes |
| --------------------------------- | --------------------------------- | --------------------------------- | ----------- | ----- |
| [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |             |

# lqaProfiles

Lqa profiles that will be added to workflow steps

## Model Type Info

| Input Type   | Accessed Type | Description                                       | Notes |
| ------------ | ------------- | ------------------------------------------------- | ----- |
| list, tuple, | tuple,        | Lqa profiles that will be added to workflow steps |

### Tuple Items

| Class Name                                            | Input Type                                            | Accessed Type                                         | Description | Notes |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------- | ----- |
| [**LqaProfilesForWsV2Dto**](LqaProfilesForWsV2Dto.md) | [**LqaProfilesForWsV2Dto**](LqaProfilesForWsV2Dto.md) | [**LqaProfilesForWsV2Dto**](LqaProfilesForWsV2Dto.md) |             |

# customFields

Custom fields for project

## Model Type Info

| Input Type   | Accessed Type | Description               | Notes |
| ------------ | ------------- | ------------------------- | ----- |
| list, tuple, | tuple,        | Custom fields for project |

### Tuple Items

| Class Name                                                    | Input Type                                                    | Accessed Type                                                 | Description | Notes |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ----------- | ----- |
| [**CustomFieldInstanceApiDto**](CustomFieldInstanceApiDto.md) | [**CustomFieldInstanceApiDto**](CustomFieldInstanceApiDto.md) | [**CustomFieldInstanceApiDto**](CustomFieldInstanceApiDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
