# ContinuousJobInfoDto

## Properties

| Name             | Type         | Description | Notes      |
| ---------------- | ------------ | ----------- | ---------- |
| **date_updated** | **datetime** |             | [optional] |

## Example

```python
from phrasetms_client.models.continuous_job_info_dto import ContinuousJobInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContinuousJobInfoDto from a JSON string
continuous_job_info_dto_instance = ContinuousJobInfoDto.from_json(json)
# print the JSON string representation of the object
print ContinuousJobInfoDto.to_json()

# convert the object into a dict
continuous_job_info_dto_dict = continuous_job_info_dto_instance.to_dict()
# create an instance of ContinuousJobInfoDto from a dict
continuous_job_info_dto_from_dict = ContinuousJobInfoDto.from_dict(continuous_job_info_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
