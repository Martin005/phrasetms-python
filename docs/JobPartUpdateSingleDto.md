# JobPartUpdateSingleDto

## Properties

| Name          | Type                                                | Description | Notes      |
| ------------- | --------------------------------------------------- | ----------- | ---------- |
| **status**    | **str**                                             |             |
| **date_due**  | **datetime**                                        |             | [optional] |
| **providers** | [**List[ProviderReference]**](ProviderReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_update_single_dto import JobPartUpdateSingleDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartUpdateSingleDto from a JSON string
job_part_update_single_dto_instance = JobPartUpdateSingleDto.from_json(json)
# print the JSON string representation of the object
print JobPartUpdateSingleDto.to_json()

# convert the object into a dict
job_part_update_single_dto_dict = job_part_update_single_dto_instance.to_dict()
# create an instance of JobPartUpdateSingleDto from a dict
job_part_update_single_dto_from_dict = JobPartUpdateSingleDto.from_dict(job_part_update_single_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
