# TranslationPriceSetDto

Language pair for translation price list, owns minimalPrice

## Properties

| Name              | Type                                                    | Description | Notes      |
| ----------------- | ------------------------------------------------------- | ----------- | ---------- |
| **source_lang**   | **str**                                                 |             | [optional] |
| **target_lang**   | **str**                                                 |             | [optional] |
| **minimum_price** | **float**                                               |             | [optional] |
| **prices**        | [**List[TranslationPriceDto]**](TranslationPriceDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.translation_price_set_dto import TranslationPriceSetDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationPriceSetDto from a JSON string
translation_price_set_dto_instance = TranslationPriceSetDto.from_json(json)
# print the JSON string representation of the object
print TranslationPriceSetDto.to_json()

# convert the object into a dict
translation_price_set_dto_dict = translation_price_set_dto_instance.to_dict()
# create an instance of TranslationPriceSetDto from a dict
translation_price_set_dto_from_dict = TranslationPriceSetDto.from_dict(translation_price_set_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
