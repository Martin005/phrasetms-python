# SearchResponseTbDto

## Properties

| Name                  | Type                              | Description | Notes      |
| --------------------- | --------------------------------- | ----------- | ---------- |
| **term_base**         | [**TermBaseDto**](TermBaseDto.md) |             | [optional] |
| **concept_id**        | **str**                           |             | [optional] |
| **source_term**       | [**TermDto**](TermDto.md)         |             | [optional] |
| **translation_terms** | [**List[TermDto]**](TermDto.md)   |             | [optional] |

## Example

```python
from phrasetms_client.models.search_response_tb_dto import SearchResponseTbDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseTbDto from a JSON string
search_response_tb_dto_instance = SearchResponseTbDto.from_json(json)
# print the JSON string representation of the object
print SearchResponseTbDto.to_json()

# convert the object into a dict
search_response_tb_dto_dict = search_response_tb_dto_instance.to_dict()
# create an instance of SearchResponseTbDto from a dict
search_response_tb_dto_from_dict = SearchResponseTbDto.from_dict(search_response_tb_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
