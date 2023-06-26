# TranslationPriceSetBulkPricesDto

## Properties

| Name                 | Type                                    | Description | Notes      |
| -------------------- | --------------------------------------- | ----------- | ---------- |
| **source_languages** | **List[str]**                           |             | [optional] |
| **target_languages** | **List[str]**                           |             | [optional] |
| **price**            | **float**                               |             | [optional] |
| **workflow_steps**   | [**List[IdReference]**](IdReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.translation_price_set_bulk_prices_dto import TranslationPriceSetBulkPricesDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationPriceSetBulkPricesDto from a JSON string
translation_price_set_bulk_prices_dto_instance = TranslationPriceSetBulkPricesDto.from_json(json)
# print the JSON string representation of the object
print TranslationPriceSetBulkPricesDto.to_json()

# convert the object into a dict
translation_price_set_bulk_prices_dto_dict = translation_price_set_bulk_prices_dto_instance.to_dict()
# create an instance of TranslationPriceSetBulkPricesDto from a dict
translation_price_set_bulk_prices_dto_from_dict = TranslationPriceSetBulkPricesDto.from_dict(translation_price_set_bulk_prices_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
