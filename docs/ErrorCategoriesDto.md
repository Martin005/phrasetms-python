# ErrorCategoriesDto

Error categories and their importance weight. If not provided, defaults will be created.

## Properties

| Name                  | Type                                                            | Description | Notes      |
| --------------------- | --------------------------------------------------------------- | ----------- | ---------- |
| **accuracy**          | [**AccuracyWeightsDto**](AccuracyWeightsDto.md)                 |             | [optional] |
| **fluency**           | [**FluencyWeightsDto**](FluencyWeightsDto.md)                   |             | [optional] |
| **terminology**       | [**TerminologyWeightsDto**](TerminologyWeightsDto.md)           |             | [optional] |
| **style**             | [**StyleWeightsDto**](StyleWeightsDto.md)                       |             | [optional] |
| **locale_convention** | [**LocaleConventionWeightsDto**](LocaleConventionWeightsDto.md) |             | [optional] |
| **verity**            | [**VerityWeightsDto**](VerityWeightsDto.md)                     |             | [optional] |
| **design**            | [**DesignWeightsDto**](DesignWeightsDto.md)                     |             | [optional] |
| **other**             | [**OtherWeightsDto**](OtherWeightsDto.md)                       |             | [optional] |

## Example

```python
from phrasetms_client.models.error_categories_dto import ErrorCategoriesDto

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorCategoriesDto from a JSON string
error_categories_dto_instance = ErrorCategoriesDto.from_json(json)
# print the JSON string representation of the object
print ErrorCategoriesDto.to_json()

# convert the object into a dict
error_categories_dto_dict = error_categories_dto_instance.to_dict()
# create an instance of ErrorCategoriesDto from a dict
error_categories_dto_from_dict = ErrorCategoriesDto.from_dict(error_categories_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
