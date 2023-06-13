# phrasetms_client.model.project_template_edit_dto.ProjectTemplateEditDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                       | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                               | Notes      |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ---------- |
| **templateName**                          | str,                                                                                                                                        | str,                                                                                    |                                                                                           |
| **name**                                  | str,                                                                                                                                        | str,                                                                                    |                                                                                           | [optional] |
| **sourceLang**                            | str,                                                                                                                                        | str,                                                                                    |                                                                                           | [optional] |
| **[targetLangs](#targetLangs)**           | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                                           | [optional] |
| **useDynamicTitle**                       | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                                           | [optional] |
| **dynamicTitle**                          | str,                                                                                                                                        | str,                                                                                    |                                                                                           | [optional] |
| **notifyProvider**                        | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md)                                                                 | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md)             |                                                                                           | [optional] |
| **[workFlowSettings](#workFlowSettings)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                                           | [optional] |
| **client**                                | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                                           | [optional] |
| **costCenter**                            | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                                           | [optional] |
| **businessUnit**                          | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                                           | [optional] |
| **domain**                                | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                                           | [optional] |
| **subDomain**                             | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                                           | [optional] |
| **vendor**                                | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                                           | [optional] |
| **importSettings**                        | [**UidReference**](UidReference.md)                                                                                                         | [**UidReference**](UidReference.md)                                                     |                                                                                           | [optional] |
| **note**                                  | str,                                                                                                                                        | str,                                                                                    |                                                                                           | [optional] |
| **fileHandover**                          | bool,                                                                                                                                       | BoolClass,                                                                              | Default: false                                                                            | [optional] |
| **[assignedTo](#assignedTo)**             | list, tuple,                                                                                                                                | tuple,                                                                                  | only use for projects without workflows; otherwise specify in the workflowSettings object | [optional] |
| **any_string_name**                       | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                        | [optional] |

# targetLangs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# workFlowSettings

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                                                        | Input Type                                                        | Accessed Type                                                     | Description | Notes |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------- | ----- |
| [**WorkflowStepSettingsEditDto**](WorkflowStepSettingsEditDto.md) | [**WorkflowStepSettingsEditDto**](WorkflowStepSettingsEditDto.md) | [**WorkflowStepSettingsEditDto**](WorkflowStepSettingsEditDto.md) |             |

# assignedTo

only use for projects without workflows; otherwise specify in the workflowSettings object

## Model Type Info

| Input Type   | Accessed Type | Description                                                                               | Notes |
| ------------ | ------------- | ----------------------------------------------------------------------------------------- | ----- |
| list, tuple, | tuple,        | only use for projects without workflows; otherwise specify in the workflowSettings object |

### Tuple Items

| Class Name                                                                                          | Input Type                                                                                          | Accessed Type                                                                                       | Description | Notes |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------- | ----- |
| [**ProjectTemplateWorkflowSettingsAssignedToDto**](ProjectTemplateWorkflowSettingsAssignedToDto.md) | [**ProjectTemplateWorkflowSettingsAssignedToDto**](ProjectTemplateWorkflowSettingsAssignedToDto.md) | [**ProjectTemplateWorkflowSettingsAssignedToDto**](ProjectTemplateWorkflowSettingsAssignedToDto.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
