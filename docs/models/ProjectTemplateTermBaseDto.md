# phrasetms_client.model.project_template_term_base_dto.ProjectTemplateTermBaseDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                  | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **targetLocale**     | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **workflowStep**     | [**WorkflowStepReference**](WorkflowStepReference.md)                                                                                       | [**WorkflowStepReference**](WorkflowStepReference.md)                                   |                                                                    | [optional] |
| **readMode**         | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **writeMode**        | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **termBase**         | [**TermBaseDto**](TermBaseDto.md)                                                                                                           | [**TermBaseDto**](TermBaseDto.md)                                                       |                                                                    | [optional] |
| **qualityAssurance** | bool,                                                                                                                                       | BoolClass,                                                                              |                                                                    | [optional] |
| **any_string_name**  | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
