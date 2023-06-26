# TranslationPriceSetListDto

## Properties

| Name           | Type                                                          | Description | Notes      |
| -------------- | ------------------------------------------------------------- | ----------- | ---------- |
| **price_sets** | [**List[TranslationPriceSetDto]**](TranslationPriceSetDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.translation_price_set_list_dto import TranslationPriceSetListDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationPriceSetListDto from a JSON string
translation_price_set_list_dto_instance = TranslationPriceSetListDto.from_json(json)
# print the JSON string representation of the object
print TranslationPriceSetListDto.to_json()

# convert the object into a dict
translation_price_set_list_dto_dict = translation_price_set_list_dto_instance.to_dict()
# create an instance of TranslationPriceSetListDto from a dict
translation_price_set_list_dto_from_dict = TranslationPriceSetListDto.from_dict(translation_price_set_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
