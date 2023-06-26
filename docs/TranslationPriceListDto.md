# TranslationPriceListDto

Price list with set of prices for language pairs

## Properties

| Name              | Type                                                          | Description | Notes                 |
| ----------------- | ------------------------------------------------------------- | ----------- | --------------------- |
| **id**            | **str**                                                       |             | [optional] [readonly] |
| **uid**           | **str**                                                       |             | [optional]            |
| **date_created**  | **datetime**                                                  |             | [optional]            |
| **name**          | **str**                                                       |             |
| **currency_code** | **str**                                                       |             | [optional]            |
| **billing_unit**  | **str**                                                       |             | [optional]            |
| **price_sets**    | [**List[TranslationPriceSetDto]**](TranslationPriceSetDto.md) |             | [optional]            |

## Example

```python
from phrasetms_client.models.translation_price_list_dto import TranslationPriceListDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationPriceListDto from a JSON string
translation_price_list_dto_instance = TranslationPriceListDto.from_json(json)
# print the JSON string representation of the object
print TranslationPriceListDto.to_json()

# convert the object into a dict
translation_price_list_dto_dict = translation_price_list_dto_instance.to_dict()
# create an instance of TranslationPriceListDto from a dict
translation_price_list_dto_from_dict = TranslationPriceListDto.from_dict(translation_price_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
