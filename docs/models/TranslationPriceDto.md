# phrasetms_client.model.translation_price_dto.TranslationPriceDto

connection between language pair and workflow steps, contains price

## Model Type Info

| Input Type                   | Accessed Type          | Description                                                         | Notes |
| ---------------------------- | ---------------------- | ------------------------------------------------------------------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, | connection between language pair and workflow steps, contains price |

### Dictionary Keys

| Key                 | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------- |
| **workflowStep**    | [**WorkflowStepDto**](WorkflowStepDto.md)                                                                                                   | [**WorkflowStepDto**](WorkflowStepDto.md)                                               |                                                                    | [optional]                              |
| **price**           | decimal.Decimal, int, float,                                                                                                                | decimal.Decimal,                                                                        |                                                                    | [optional] value must be a 64 bit float |
| **any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]                              |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
