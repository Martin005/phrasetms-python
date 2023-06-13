# phrasetms_client.model.quality_assurance_batch_run_dto_v3.QualityAssuranceBatchRunDtoV3

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                    | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                                                                                                                                                 | Notes                                     |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **[jobs](#jobs)**      | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                                                                                                                                             |
| **settings**           | [**QualityAssuranceRunDtoV3**](QualityAssuranceRunDtoV3.md)                                                                                 | [**QualityAssuranceRunDtoV3**](QualityAssuranceRunDtoV3.md)                             |                                                                                                                                                                                             | [optional]                                |
| **maxQaWarningsCount** | decimal.Decimal, int,                                                                                                                       | decimal.Decimal,                                                                        | Maximum number of QA warnings in result, default: 100. For efficiency reasons QA warnings are processed with minimum segments chunk size 10, therefore slightly more warnings are returned. | [optional] value must be a 32 bit integer |
| **any_string_name**    | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type                                                                                                                          | [optional]                                |

# jobs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
