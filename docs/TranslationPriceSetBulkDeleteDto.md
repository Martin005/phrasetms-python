# TranslationPriceSetBulkDeleteDto

## Properties

| Name                 | Type          | Description | Notes      |
| -------------------- | ------------- | ----------- | ---------- |
| **source_languages** | **List[str]** |             | [optional] |
| **target_languages** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.translation_price_set_bulk_delete_dto import TranslationPriceSetBulkDeleteDto

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationPriceSetBulkDeleteDto from a JSON string
translation_price_set_bulk_delete_dto_instance = TranslationPriceSetBulkDeleteDto.from_json(json)
# print the JSON string representation of the object
print TranslationPriceSetBulkDeleteDto.to_json()

# convert the object into a dict
translation_price_set_bulk_delete_dto_dict = translation_price_set_bulk_delete_dto_instance.to_dict()
# create an instance of TranslationPriceSetBulkDeleteDto from a dict
translation_price_set_bulk_delete_dto_from_dict = TranslationPriceSetBulkDeleteDto.from_dict(translation_price_set_bulk_delete_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
