# DictionaryItemDto

## Properties

| Name     | Type    | Description | Notes |
| -------- | ------- | ----------- | ----- |
| **lang** | **str** |             |
| **word** | **str** |             |

## Example

```python
from phrasetms_client.models.dictionary_item_dto import DictionaryItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of DictionaryItemDto from a JSON string
dictionary_item_dto_instance = DictionaryItemDto.from_json(json)
# print the JSON string representation of the object
print DictionaryItemDto.to_json()

# convert the object into a dict
dictionary_item_dto_dict = dictionary_item_dto_instance.to_dict()
# create an instance of DictionaryItemDto from a dict
dictionary_item_dto_from_dict = DictionaryItemDto.from_dict(dictionary_item_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
