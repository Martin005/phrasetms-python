# TranslationPriceSetCreateDto

## Properties

| Name                 | Type          | Description | Notes |
| -------------------- | ------------- | ----------- | ----- |
| **source_languages** | **List[str]** |             |
| **target_languages** | **List[str]** |             |

## Example

```python
from phrasetms_client.models.translation_price_set_create_dto import TranslationPriceSetCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationPriceSetCreateDto from a JSON string
translation_price_set_create_dto_instance = TranslationPriceSetCreateDto.from_json(json)
# print the JSON string representation of the object
print TranslationPriceSetCreateDto.to_json()

# convert the object into a dict
translation_price_set_create_dto_dict = translation_price_set_create_dto_instance.to_dict()
# create an instance of TranslationPriceSetCreateDto from a dict
translation_price_set_create_dto_from_dict = TranslationPriceSetCreateDto.from_dict(translation_price_set_create_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
