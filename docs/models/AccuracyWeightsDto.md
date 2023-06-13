# phrasetms_client.model.accuracy_weights_dto.AccuracyWeightsDto

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                  | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **accuracy**         | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                                                                           | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                       |                                                                    | [optional] |
| **addition**         | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                                                                           | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                       |                                                                    | [optional] |
| **omission**         | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                                                                           | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                       |                                                                    | [optional] |
| **mistranslation**   | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                                                                           | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                       |                                                                    | [optional] |
| **underTranslation** | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                                                                           | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                       |                                                                    | [optional] |
| **untranslated**     | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                                                                           | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                       |                                                                    | [optional] |
| **improperTmMatch**  | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                                                                           | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                       |                                                                    | [optional] |
| **overTranslation**  | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                                                                           | [**ToggleableWeightDto**](ToggleableWeightDto.md)                                       |                                                                    | [optional] |
| **any_string_name**  | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
