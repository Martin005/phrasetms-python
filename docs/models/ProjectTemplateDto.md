# phrasetms_client.model.project_template_dto.ProjectTemplateDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                               |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| **id**                                    | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **uid**                                   | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **templateName**                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **name**                                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **sourceLang**                            | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **[targetLangs](#targetLangs)**           | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **note**                                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **useDynamicTitle**                       | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional]                                          |
| **dynamicTitle**                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional]                                          |
| **owner**                                 | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                          |
| **client**                                | [**ClientReference**](ClientReference.md)                                                                                                   | [**ClientReference**](ClientReference.md)                                               |                                                                    | [optional]                                          |
| **domain**                                | [**DomainReference**](DomainReference.md)                                                                                                   | [**DomainReference**](DomainReference.md)                                               |                                                                    | [optional]                                          |
| **subDomain**                             | [**SubDomainReference**](SubDomainReference.md)                                                                                             | [**SubDomainReference**](SubDomainReference.md)                                         |                                                                    | [optional]                                          |
| **vendor**                                | [**VendorReference**](VendorReference.md)                                                                                                   | [**VendorReference**](VendorReference.md)                                               |                                                                    | [optional]                                          |
| **createdBy**                             | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                          |
| **dateCreated**                           | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **modifiedBy**                            | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional]                                          |
| **dateModified**                          | str, datetime,                                                                                                                              | str,                                                                                    | Deprecated - use dateTimeModified field instead                    | [optional] value must conform to RFC-3339 date-time |
| **dateTimeModified**                      | str, datetime,                                                                                                                              | str,                                                                                    |                                                                    | [optional] value must conform to RFC-3339 date-time |
| **[workflowSteps](#workflowSteps)**       | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **[workflowSettings](#workflowSettings)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **businessUnit**                          | [**BusinessUnitReference**](BusinessUnitReference.md)                                                                                       | [**BusinessUnitReference**](BusinessUnitReference.md)                                   |                                                                    | [optional]                                          |
| **notifyProviders**                       | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md)                                                                 | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md)             |                                                                    | [optional]                                          |
| **[assignedTo](#assignedTo)**             | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional]                                          |
| **importSettings**                        | [**UidReference**](UidReference.md)                                                                                                         | [**UidReference**](UidReference.md)                                                     |                                                                    | [optional]                                          |
| **any_string_name**                       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                                          |

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

| Class Name                                | Input Type                                | Accessed Type                             | Description | Notes |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------- | ----- |
| [**WorkflowStepDto**](WorkflowStepDto.md) | [**WorkflowStepDto**](WorkflowStepDto.md) | [**WorkflowStepDto**](WorkflowStepDto.md) |             |

# workflowSettings

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                | Input Type                                                | Accessed Type                                             | Description | Notes |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | ----------- | ----- |
| [**WorkflowStepSettingsDto**](WorkflowStepSettingsDto.md) | [**WorkflowStepSettingsDto**](WorkflowStepSettingsDto.md) | [**WorkflowStepSettingsDto**](WorkflowStepSettingsDto.md) |             |

# assignedTo

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                      | Input Type                                                      | Accessed Type                                                   | Description | Notes |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | ----------- | ----- |
| [**AssignmentPerTargetLangDto**](AssignmentPerTargetLangDto.md) | [**AssignmentPerTargetLangDto**](AssignmentPerTargetLangDto.md) | [**AssignmentPerTargetLangDto**](AssignmentPerTargetLangDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
