# SearchInTextResponse2Dto

## Properties

| Name                  | Type                                          | Description | Notes      |
| --------------------- | --------------------------------------------- | ----------- | ---------- |
| **term_base**         | [**TermBaseReference**](TermBaseReference.md) |             | [optional] |
| **source_term**       | [**TermV2Dto**](TermV2Dto.md)                 |             | [optional] |
| **concept**           | [**ConceptDtov2**](ConceptDtov2.md)           |             | [optional] |
| **translation_terms** | [**List[TermV2Dto]**](TermV2Dto.md)           |             | [optional] |
| **sub_term**          | **bool**                                      |             | [optional] |
| **matches**           | [**List[Match]**](Match.md)                   |             | [optional] |

## Example

```python
from phrasetms_client.models.search_in_text_response2_dto import SearchInTextResponse2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchInTextResponse2Dto from a JSON string
search_in_text_response2_dto_instance = SearchInTextResponse2Dto.from_json(json)
# print the JSON string representation of the object
print SearchInTextResponse2Dto.to_json()

# convert the object into a dict
search_in_text_response2_dto_dict = search_in_text_response2_dto_instance.to_dict()
# create an instance of SearchInTextResponse2Dto from a dict
search_in_text_response2_dto_from_dict = SearchInTextResponse2Dto.from_dict(search_in_text_response2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
