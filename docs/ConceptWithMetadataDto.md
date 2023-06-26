# ConceptWithMetadataDto

## Properties

| Name             | Type                                                  | Description | Notes      |
| ---------------- | ----------------------------------------------------- | ----------- | ---------- |
| **id**           | **str**                                               |             | [optional] |
| **domain**       | [**DomainReference**](DomainReference.md)             |             | [optional] |
| **subdomains**   | [**List[SubDomainReference]**](SubDomainReference.md) |             | [optional] |
| **url**          | **str**                                               |             | [optional] |
| **definition**   | **str**                                               |             | [optional] |
| **concept_note** | **str**                                               |             | [optional] |

## Example

```python
from phrasetms_client.models.concept_with_metadata_dto import ConceptWithMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptWithMetadataDto from a JSON string
concept_with_metadata_dto_instance = ConceptWithMetadataDto.from_json(json)
# print the JSON string representation of the object
print ConceptWithMetadataDto.to_json()

# convert the object into a dict
concept_with_metadata_dto_dict = concept_with_metadata_dto_instance.to_dict()
# create an instance of ConceptWithMetadataDto from a dict
concept_with_metadata_dto_from_dict = ConceptWithMetadataDto.from_dict(concept_with_metadata_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
