# TranslationPriceDto

connection between language pair and workflow steps, contains price

## Properties

| Name              | Type                                      | Description | Notes      |
| ----------------- | ----------------------------------------- | ----------- | ---------- |
| **workflow_step** | [**WorkflowStepDto**](WorkflowStepDto.md) |             | [optional] |
| **price**         | **float**                                 |             | [optional] |

## Example

```python
from phrasetms_client.models.translation_price_dto import TranslationPriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationPriceDto from a JSON string
translation_price_dto_instance = TranslationPriceDto.from_json(json)
# print the JSON string representation of the object
print TranslationPriceDto.to_json()

# convert the object into a dict
translation_price_dto_dict = translation_price_dto_instance.to_dict()
# create an instance of TranslationPriceDto from a dict
translation_price_dto_from_dict = TranslationPriceDto.from_dict(translation_price_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
