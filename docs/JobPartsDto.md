# JobPartsDto

## Properties

| Name     | Type                                              | Description | Notes      |
| -------- | ------------------------------------------------- | ----------- | ---------- |
| **jobs** | [**List[JobPartReference]**](JobPartReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_parts_dto import JobPartsDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartsDto from a JSON string
job_parts_dto_instance = JobPartsDto.from_json(json)
# print the JSON string representation of the object
print JobPartsDto.to_json()

# convert the object into a dict
job_parts_dto_dict = job_parts_dto_instance.to_dict()
# create an instance of JobPartsDto from a dict
job_parts_dto_from_dict = JobPartsDto.from_dict(job_parts_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
