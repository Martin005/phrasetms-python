# AdminProjectManagerV2AllOf

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
from phrasetms_client.models.admin_project_manager_v2_all_of import AdminProjectManagerV2AllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AdminProjectManagerV2AllOf from a JSON string
admin_project_manager_v2_all_of_instance = AdminProjectManagerV2AllOf.from_json(json)
# print the JSON string representation of the object
print AdminProjectManagerV2AllOf.to_json()

# convert the object into a dict
admin_project_manager_v2_all_of_dict = admin_project_manager_v2_all_of_instance.to_dict()
# create an instance of AdminProjectManagerV2AllOf from a dict
admin_project_manager_v2_all_of_from_dict = AdminProjectManagerV2AllOf.from_dict(admin_project_manager_v2_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
