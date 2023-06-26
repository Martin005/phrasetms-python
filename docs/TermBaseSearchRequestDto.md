# TermBaseSearchRequestDto

## Properties

| Name             | Type          | Description | Notes      |
| ---------------- | ------------- | ----------- | ---------- |
| **target_langs** | **List[str]** |             |
| **source_lang**  | **str**       |             |
| **query**        | **str**       |             |
| **status**       | **str**       |             | [optional] |

## Example

```python
from phrasetms_client.models.term_base_search_request_dto import TermBaseSearchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TermBaseSearchRequestDto from a JSON string
term_base_search_request_dto_instance = TermBaseSearchRequestDto.from_json(json)
# print the JSON string representation of the object
print TermBaseSearchRequestDto.to_json()

# convert the object into a dict
term_base_search_request_dto_dict = term_base_search_request_dto_instance.to_dict()
# create an instance of TermBaseSearchRequestDto from a dict
term_base_search_request_dto_from_dict = TermBaseSearchRequestDto.from_dict(term_base_search_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
