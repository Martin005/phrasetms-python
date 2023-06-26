# QualityAssuranceSegmentsRunDtoV3

## Properties

| Name                      | Type                                                      | Description                                                                                                                                                                                 | Notes      |
| ------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **jobs_and_segments**     | [**List[JobPartSegmentsDtoV3]**](JobPartSegmentsDtoV3.md) |                                                                                                                                                                                             |
| **warning_types**         | **List[str]**                                             | When empty only fast checks run                                                                                                                                                             | [optional] |
| **max_qa_warnings_count** | **int**                                                   | Maximum number of QA warnings in result, default: 100. For efficiency reasons QA warnings are processed with minimum segments chunk size 10, therefore slightly more warnings are returned. | [optional] |

## Example

```python
from phrasetms_client.models.quality_assurance_segments_run_dto_v3 import QualityAssuranceSegmentsRunDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of QualityAssuranceSegmentsRunDtoV3 from a JSON string
quality_assurance_segments_run_dto_v3_instance = QualityAssuranceSegmentsRunDtoV3.from_json(json)
# print the JSON string representation of the object
print QualityAssuranceSegmentsRunDtoV3.to_json()

# convert the object into a dict
quality_assurance_segments_run_dto_v3_dict = quality_assurance_segments_run_dto_v3_instance.to_dict()
# create an instance of QualityAssuranceSegmentsRunDtoV3 from a dict
quality_assurance_segments_run_dto_v3_from_dict = QualityAssuranceSegmentsRunDtoV3.from_dict(quality_assurance_segments_run_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
