# JobPartReference

## Properties

| Name                                 | Type                                                  | Description | Notes      |
| ------------------------------------ | ----------------------------------------------------- | ----------- | ---------- |
| **uid**                              | **str**                                               |             | [optional] |
| **status**                           | **str**                                               |             | [optional] |
| **providers**                        | [**List[ProviderReference]**](ProviderReference.md)   |             | [optional] |
| **target_lang**                      | **str**                                               |             | [optional] |
| **workflow_level**                   | **int**                                               |             | [optional] |
| **workflow_step**                    | [**WorkflowStepReference**](WorkflowStepReference.md) |             | [optional] |
| **filename**                         | **str**                                               |             | [optional] |
| **date_due**                         | **datetime**                                          |             | [optional] |
| **date_created**                     | **datetime**                                          |             | [optional] |
| **update_source_date**               | **datetime**                                          |             | [optional] |
| **imported**                         | **bool**                                              |             | [optional] |
| **job_assigned_email_template**      | **object**                                            |             | [optional] |
| **notification_interval_in_minutes** | **int**                                               |             | [optional] |
| **continuous**                       | **bool**                                              |             | [optional] |
| **source_file_uid**                  | **str**                                               |             | [optional] |

## Example

```python
from phrasetms_client.models.job_part_reference import JobPartReference

# TODO update the JSON string below
json = "{}"
# create an instance of JobPartReference from a JSON string
job_part_reference_instance = JobPartReference.from_json(json)
# print the JSON string representation of the object
print JobPartReference.to_json()

# convert the object into a dict
job_part_reference_dict = job_part_reference_instance.to_dict()
# create an instance of JobPartReference from a dict
job_part_reference_from_dict = JobPartReference.from_dict(job_part_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
