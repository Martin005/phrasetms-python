# AdminProjectManagerAllOf

## Properties

| Name                           | Type                                                          | Description    | Notes      |
| ------------------------------ | ------------------------------------------------------------- | -------------- | ---------- |
| **shared**                     | **bool**                                                      | Default: false | [optional] |
| **progress**                   | [**ProgressDto**](ProgressDto.md)                             |                | [optional] |
| **client**                     | [**ClientReference**](ClientReference.md)                     |                | [optional] |
| **cost_center**                | [**CostCenterReference**](CostCenterReference.md)             |                | [optional] |
| **business_unit**              | [**BusinessUnitReference**](BusinessUnitReference.md)         |                | [optional] |
| **date_due**                   | **datetime**                                                  |                | [optional] |
| **status**                     | **str**                                                       |                | [optional] |
| **purchase_order**             | **str**                                                       |                | [optional] |
| **is_published_on_job_board**  | **bool**                                                      | Default: false | [optional] |
| **note**                       | **str**                                                       |                | [optional] |
| **created_by**                 | [**UserReference**](UserReference.md)                         |                | [optional] |
| **quality_assurance_settings** | **object**                                                    |                | [optional] |
| **workflow_steps**             | [**List[ProjectWorkflowStepDto]**](ProjectWorkflowStepDto.md) |                | [optional] |
| **analyse_settings**           | **object**                                                    |                | [optional] |
| **access_settings**            | **object**                                                    |                | [optional] |
| **financial_settings**         | **object**                                                    |                | [optional] |
| **archived**                   | **bool**                                                      |                | [optional] |

## Example

```python
from phrasetms_client.models.admin_project_manager_all_of import AdminProjectManagerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AdminProjectManagerAllOf from a JSON string
admin_project_manager_all_of_instance = AdminProjectManagerAllOf.from_json(json)
# print the JSON string representation of the object
print AdminProjectManagerAllOf.to_json()

# convert the object into a dict
admin_project_manager_all_of_dict = admin_project_manager_all_of_instance.to_dict()
# create an instance of AdminProjectManagerAllOf from a dict
admin_project_manager_all_of_from_dict = AdminProjectManagerAllOf.from_dict(admin_project_manager_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
