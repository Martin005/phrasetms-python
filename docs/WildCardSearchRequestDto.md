# WildCardSearchRequestDto

## Properties

| Name             | Type          | Description | Notes      |
| ---------------- | ------------- | ----------- | ---------- |
| **query**        | **str**       |             | [optional] |
| **source_lang**  | **str**       |             |
| **target_langs** | **List[str]** |             | [optional] |
| **count**        | **int**       |             | [optional] |
| **offset**       | **int**       |             | [optional] |
| **source_langs** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.wild_card_search_request_dto import WildCardSearchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of WildCardSearchRequestDto from a JSON string
wild_card_search_request_dto_instance = WildCardSearchRequestDto.from_json(json)
# print the JSON string representation of the object
print WildCardSearchRequestDto.to_json()

# convert the object into a dict
wild_card_search_request_dto_dict = wild_card_search_request_dto_instance.to_dict()
# create an instance of WildCardSearchRequestDto from a dict
wild_card_search_request_dto_from_dict = WildCardSearchRequestDto.from_dict(wild_card_search_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
