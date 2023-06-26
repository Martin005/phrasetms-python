# ConceptDtov2

## Properties

| Name            | Type          | Description | Notes      |
| --------------- | ------------- | ----------- | ---------- |
| **id**          | **str**       |             | [optional] |
| **definition**  | **str**       |             | [optional] |
| **domain**      | **str**       |             | [optional] |
| **sub_domains** | **List[str]** |             | [optional] |
| **url**         | **str**       |             | [optional] |
| **note**        | **str**       |             | [optional] |

## Example

```python
from phrasetms_client.models.concept_dtov2 import ConceptDtov2

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptDtov2 from a JSON string
concept_dtov2_instance = ConceptDtov2.from_json(json)
# print the JSON string representation of the object
print ConceptDtov2.to_json()

# convert the object into a dict
concept_dtov2_dict = concept_dtov2_instance.to_dict()
# create an instance of ConceptDtov2 from a dict
concept_dtov2_from_dict = ConceptDtov2.from_dict(concept_dtov2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
