# QualityAssuranceDto

## Properties

| Name                       | Type    | Description | Notes      |
| -------------------------- | ------- | ----------- | ---------- |
| **segments_count**         | **int** |             | [optional] |
| **warnings_count**         | **int** |             | [optional] |
| **ignored_warnings_count** | **int** |             | [optional] |

## Example

```python
from phrasetms_client.models.quality_assurance_dto import QualityAssuranceDto

# TODO update the JSON string below
json = "{}"
# create an instance of QualityAssuranceDto from a JSON string
quality_assurance_dto_instance = QualityAssuranceDto.from_json(json)
# print the JSON string representation of the object
print QualityAssuranceDto.to_json()

# convert the object into a dict
quality_assurance_dto_dict = quality_assurance_dto_instance.to_dict()
# create an instance of QualityAssuranceDto from a dict
quality_assurance_dto_from_dict = QualityAssuranceDto.from_dict(quality_assurance_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
