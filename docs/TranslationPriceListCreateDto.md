# TranslationPriceListCreateDto

## Properties

| Name              | Type    | Description   | Notes      |
| ----------------- | ------- | ------------- | ---------- |
| **name**          | **str** |               |
| **currency_code** | **str** |               |
| **billing_unit**  | **str** | Default: Word | [optional] |

## Example

```python
from phrasetms_client.models.translation_price_list_create_dto import TranslationPriceListCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationPriceListCreateDto from a JSON string
translation_price_list_create_dto_instance = TranslationPriceListCreateDto.from_json(json)
# print the JSON string representation of the object
print TranslationPriceListCreateDto.to_json()

# convert the object into a dict
translation_price_list_create_dto_dict = translation_price_list_create_dto_instance.to_dict()
# create an instance of TranslationPriceListCreateDto from a dict
translation_price_list_create_dto_from_dict = TranslationPriceListCreateDto.from_dict(translation_price_list_create_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
