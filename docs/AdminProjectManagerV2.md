# AdminProjectManagerV2

## Properties

| Name                           | Type                                                              | Description    | Notes      |
| ------------------------------ | ----------------------------------------------------------------- | -------------- | ---------- |
| **shared**                     | **bool**                                                          | Default: false | [optional] |
| **progress**                   | [**ProgressDtoV2**](ProgressDtoV2.md)                             |                | [optional] |
| **client**                     | [**ClientReference**](ClientReference.md)                         |                | [optional] |
| **cost_center**                | [**CostCenterReference**](CostCenterReference.md)                 |                | [optional] |
| **business_unit**              | [**BusinessUnitReference**](BusinessUnitReference.md)             |                | [optional] |
| **date_due**                   | **datetime**                                                      |                | [optional] |
| **status**                     | **str**                                                           |                | [optional] |
| **purchase_order**             | **str**                                                           |                | [optional] |
| **is_published_on_job_board**  | **bool**                                                          | Default: false | [optional] |
| **note**                       | **str**                                                           |                | [optional] |
| **created_by**                 | [**UserReference**](UserReference.md)                             |                | [optional] |
| **quality_assurance_settings** | **object**                                                        |                | [optional] |
| **workflow_steps**             | [**List[ProjectWorkflowStepDtoV2]**](ProjectWorkflowStepDtoV2.md) |                | [optional] |
| **analyse_settings**           | **object**                                                        |                | [optional] |
| **access_settings**            | **object**                                                        |                | [optional] |
| **financial_settings**         | **object**                                                        |                | [optional] |

## Example

```python
from phrasetms_client.models.admin_project_manager_v2 import AdminProjectManagerV2

# TODO update the JSON string below
json = "{}"
# create an instance of AdminProjectManagerV2 from a JSON string
admin_project_manager_v2_instance = AdminProjectManagerV2.from_json(json)
# print the JSON string representation of the object
print AdminProjectManagerV2.to_json()

# convert the object into a dict
admin_project_manager_v2_dict = admin_project_manager_v2_instance.to_dict()
# create an instance of AdminProjectManagerV2 from a dict
admin_project_manager_v2_from_dict = AdminProjectManagerV2.from_dict(admin_project_manager_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
