# ConceptDto

## Properties

| Name         | Type                    | Description | Notes      |
| ------------ | ----------------------- | ----------- | ---------- |
| **id**       | **str**                 |             | [optional] |
| **writable** | **bool**                |             | [optional] |
| **terms**    | **List[List[TermDto]]** |             | [optional] |

## Example

```python
from phrasetms_client.models.concept_dto import ConceptDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptDto from a JSON string
concept_dto_instance = ConceptDto.from_json(json)
# print the JSON string representation of the object
print ConceptDto.to_json()

# convert the object into a dict
concept_dto_dict = concept_dto_instance.to_dict()
# create an instance of ConceptDto from a dict
concept_dto_from_dict = ConceptDto.from_dict(concept_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
