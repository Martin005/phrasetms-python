# phrasetms_client.model.create_project_from_template_v2_dto.CreateProjectFromTemplateV2Dto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                               |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| **name**                            | str,                                                                                                                                        | str,                                                                                    |                                                                    |
| **sourceLang**                      | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **[targetLangs](#targetLangs)**     | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **[workflowSteps](#workflowSteps)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **dateDue**                         | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **note**                            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **client**                          | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **businessUnit**                    | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **domain**                          | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **subDomain**                       | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
| **costCenter**                      | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional]                                          |
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
