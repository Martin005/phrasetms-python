# ConceptListReference

## Properties

| Name         | Type                                    | Description | Notes |
| ------------ | --------------------------------------- | ----------- | ----- |
| **concepts** | [**List[IdReference]**](IdReference.md) |             |

## Example

```python
from phrasetms_client.models.concept_list_reference import ConceptListReference

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptListReference from a JSON string
concept_list_reference_instance = ConceptListReference.from_json(json)
# print the JSON string representation of the object
print ConceptListReference.to_json()

# convert the object into a dict
concept_list_reference_dict = concept_list_reference_instance.to_dict()
# create an instance of ConceptListReference from a dict
concept_list_reference_from_dict = ConceptListReference.from_dict(concept_list_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
