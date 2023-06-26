# ConceptEditDto

## Properties

| Name             | Type                                      | Description | Notes      |
| ---------------- | ----------------------------------------- | ----------- | ---------- |
| **domain**       | [**UidReference**](UidReference.md)       |             | [optional] |
| **subdomains**   | [**List[UidReference]**](UidReference.md) |             | [optional] |
| **definition**   | **str**                                   |             | [optional] |
| **url**          | **str**                                   |             | [optional] |
| **concept_note** | **str**                                   |             | [optional] |

## Example

```python
from phrasetms_client.models.concept_edit_dto import ConceptEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptEditDto from a JSON string
concept_edit_dto_instance = ConceptEditDto.from_json(json)
# print the JSON string representation of the object
print ConceptEditDto.to_json()

# convert the object into a dict
concept_edit_dto_dict = concept_edit_dto_instance.to_dict()
# create an instance of ConceptEditDto from a dict
concept_edit_dto_from_dict = ConceptEditDto.from_dict(concept_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
