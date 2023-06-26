# SearchTbResponseDto

## Properties

| Name                  | Type                                          | Description | Notes      |
| --------------------- | --------------------------------------------- | ----------- | ---------- |
| **term_base**         | [**TermBaseReference**](TermBaseReference.md) |             | [optional] |
| **concept**           | [**ConceptDtov2**](ConceptDtov2.md)           |             | [optional] |
| **source_term**       | [**TermV2Dto**](TermV2Dto.md)                 |             | [optional] |
| **translation_terms** | [**List[TermV2Dto]**](TermV2Dto.md)           |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tb_response_dto import SearchTbResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTbResponseDto from a JSON string
search_tb_response_dto_instance = SearchTbResponseDto.from_json(json)
# print the JSON string representation of the object
print SearchTbResponseDto.to_json()

# convert the object into a dict
search_tb_response_dto_dict = search_tb_response_dto_instance.to_dict()
# create an instance of SearchTbResponseDto from a dict
search_tb_response_dto_from_dict = SearchTbResponseDto.from_dict(search_tb_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
