# ConceptListResponseDto

## Properties

| Name            | Type                                                          | Description | Notes      |
| --------------- | ------------------------------------------------------------- | ----------- | ---------- |
| **concepts**    | [**List[ConceptWithMetadataDto]**](ConceptWithMetadataDto.md) |             | [optional] |
| **total_count** | **int**                                                       |             | [optional] |

## Example

```python
from phrasetms_client.models.concept_list_response_dto import ConceptListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptListResponseDto from a JSON string
concept_list_response_dto_instance = ConceptListResponseDto.from_json(json)
# print the JSON string representation of the object
print ConceptListResponseDto.to_json()

# convert the object into a dict
concept_list_response_dto_dict = concept_list_response_dto_instance.to_dict()
# create an instance of ConceptListResponseDto from a dict
concept_list_response_dto_from_dict = ConceptListResponseDto.from_dict(concept_list_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
