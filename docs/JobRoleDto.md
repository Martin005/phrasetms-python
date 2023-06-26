# JobRoleDto

## Properties

| Name                  | Type                                                        | Description                       | Notes      |
| --------------------- | ----------------------------------------------------------- | --------------------------------- | ---------- |
| **type**              | **str**                                                     |                                   |
| **workflow_step**     | [**ProjectWorkflowStepDtoV2**](ProjectWorkflowStepDtoV2.md) |                                   | [optional] |
| **organization_type** | **str**                                                     | not null only for shared projects | [optional] |

## Example

```python
from phrasetms_client.models.job_role_dto import JobRoleDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobRoleDto from a JSON string
job_role_dto_instance = JobRoleDto.from_json(json)
# print the JSON string representation of the object
print JobRoleDto.to_json()

# convert the object into a dict
job_role_dto_dict = job_role_dto_instance.to_dict()
# create an instance of JobRoleDto from a dict
job_role_dto_from_dict = JobRoleDto.from_dict(job_role_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
