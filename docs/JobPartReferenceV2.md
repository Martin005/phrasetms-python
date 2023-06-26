# JobPartReferenceV2

## Properties

| Name                        | Type                                                                | Description                                                                                                                        | Notes      |
| --------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **uid**                     | **str**                                                             |                                                                                                                                    | [optional] |
| **inner_id**                | **str**                                                             | InnerId is a sequential number of a job in a project. Jobs created from the same file share the same innerId across workflow steps | [optional] |
| **status**                  | **str**                                                             |                                                                                                                                    | [optional] |
| **providers**               | [**List[ProviderReference]**](ProviderReference.md)                 |                                                                                                                                    | [optional] |
| **target_lang**             | **str**                                                             |                                                                                                                                    | [optional] |
| **workflow_step**           | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) |                                                                                                                                    | [optional] |
| **filename**                | **str**                                                             |                                                                                                                                    | [optional] |
| **original_file_directory** | **str**                                                             |                                                                                                                                    | [optional] |
| **date_due**                | **datetime**                                                        |                                                                                                                                    | [optional] |
| **date_created**            | **datetime**                                                        |                                                                                                                                    | [optional] |
| **import_status**           | [**ImportStatusDtoV2**](ImportStatusDtoV2.md)                       |                                                                                                                                    | [optional] |
| **continuous**              | **bool**                                                            |                                                                                                                                    | [optional] |
| **source_file_uid**         | **str**                                                             |                                                                                                                                    | [optional] |
| **split**                   | **bool**                                                            |                                                                                                                                    | [optional] |
| **server_task_id**          | **str**                                                             |                                                                                                                                    | [optional] |
| **owner**                   | [**UserReference**](UserReference.md)                               |                                                                                                                                    | [optional] |
| **imported**                | **bool**                                                            | Default: false                                                                                                                     | [optional] |

## Example

```python
from phrasetms_client.models.job_part_reference_v2 import JobPartReferenceV2

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartReferenceV2 from a JSON string
job_part_reference_v2_instance = JobPartReferenceV2.from_json(json)
# print the JSON string representation of the object
print JobPartReferenceV2.to_json()

# convert the object into a dict
job_part_reference_v2_dict = job_part_reference_v2_instance.to_dict()
# create an instance of JobPartReferenceV2 from a dict
job_part_reference_v2_from_dict = JobPartReferenceV2.from_dict(job_part_reference_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
