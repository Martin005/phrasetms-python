# QualityAssuranceResponseDto

## Properties

| Name                 | Type                                                  | Description | Notes      |
| -------------------- | ----------------------------------------------------- | ----------- | ---------- |
| **segment_warnings** | [**List[SegmentWarningsDto]**](SegmentWarningsDto.md) |             | [optional] |
| **finished**         | **bool**                                              |             | [optional] |

## Example

```python
from phrasetms_client.models.quality_assurance_response_dto import QualityAssuranceResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of QualityAssuranceResponseDto from a JSON string
quality_assurance_response_dto_instance = QualityAssuranceResponseDto.from_json(json)
# print the JSON string representation of the object
print QualityAssuranceResponseDto.to_json()

# convert the object into a dict
quality_assurance_response_dto_dict = quality_assurance_response_dto_instance.to_dict()
# create an instance of QualityAssuranceResponseDto from a dict
quality_assurance_response_dto_from_dict = QualityAssuranceResponseDto.from_dict(quality_assurance_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
