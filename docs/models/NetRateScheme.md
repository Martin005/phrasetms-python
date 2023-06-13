# phrasetms_client.model.net_rate_scheme.NetRateScheme

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                                   | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                               |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| **id**                                                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **uid**                                               | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **name**                                              | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **organization**                                      | [**OrganizationReference**](OrganizationReference.md)                                                                                       | [**OrganizationReference**](OrganizationReference.md)                                   |                                                                    | [optional]                                          |
| **dateCreated**                                       | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **createdBy**                                         | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                          |
| **[workflowStepNetSchemes](#workflowStepNetSchemes)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **rates**                                             | [**DiscountSettingsDto**](DiscountSettingsDto.md)                                                                                           | [**DiscountSettingsDto**](DiscountSettingsDto.md)                                       |                                                                    | [optional]                                          |
| **any_string_name**                                   | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                          |

# workflowStepNetSchemes

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                                      | Input Type                                                                      | Accessed Type                                                                   | Description | Notes |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------- | ----- |
| [**NetRateSchemeWorkflowStepReference**](NetRateSchemeWorkflowStepReference.md) | [**NetRateSchemeWorkflowStepReference**](NetRateSchemeWorkflowStepReference.md) | [**NetRateSchemeWorkflowStepReference**](NetRateSchemeWorkflowStepReference.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
