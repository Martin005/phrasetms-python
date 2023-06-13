# phrasetms_client.model.set_project_template_term_base_dto.SetProjectTemplateTermBaseDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                                         | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **[readTermBases](#readTermBases)**                         | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **writeTermBase**                                           | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional] |
| **[qualityAssuranceTermBases](#qualityAssuranceTermBases)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **targetLang**                                              | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **workflowStep**                                            | [**IdReference**](IdReference.md)                                                                                                           | [**IdReference**](IdReference.md)                                                       |                                                                    | [optional] |
| **any_string_name**                                         | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# readTermBases

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                        | Input Type                        | Accessed Type                     | Description | Notes |
| --------------------------------- | --------------------------------- | --------------------------------- | ----------- | ----- |
| [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |             |

# qualityAssuranceTermBases

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                        | Input Type                        | Accessed Type                     | Description | Notes |
| --------------------------------- | --------------------------------- | --------------------------------- | ----------- | ----- |
| [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) | [**IdReference**](IdReference.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
