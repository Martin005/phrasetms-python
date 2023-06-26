# ProjectReference

## Properties

| Name               | Type                                                  | Description | Notes      |
| ------------------ | ----------------------------------------------------- | ----------- | ---------- |
| **uid**            | **str**                                               |             | [optional] |
| **inner_id**       | **int**                                               |             | [optional] |
| **name**           | **str**                                               |             | [optional] |
| **business_unit**  | [**BusinessUnitReference**](BusinessUnitReference.md) |             | [optional] |
| **domain**         | [**DomainReference**](DomainReference.md)             |             | [optional] |
| **sub_domain**     | [**SubDomainReference**](SubDomainReference.md)       |             | [optional] |
| **client**         | [**ClientReference**](ClientReference.md)             |             | [optional] |
| **cost_center**    | [**CostCenterReference**](CostCenterReference.md)     |             | [optional] |
| **due_date**       | **datetime**                                          |             | [optional] |
| **created_date**   | **datetime**                                          |             | [optional] |
| **created_by**     | [**UserReference**](UserReference.md)                 |             | [optional] |
| **owner**          | [**UserReference**](UserReference.md)                 |             | [optional] |
| **vendor**         | [**VendorUserReference**](VendorUserReference.md)     |             | [optional] |
| **purchase_order** | **str**                                               |             | [optional] |
| **source_lang**    | **str**                                               |             | [optional] |
| **target_langs**   | **List[str]**                                         |             | [optional] |
| **status**         | **str**                                               |             | [optional] |
| **progress**       | [**ProgressReference**](ProgressReference.md)         |             | [optional] |
| **metadata**       | [**List[MetadataReference]**](MetadataReference.md)   |             | [optional] |
| **note**           | **str**                                               |             | [optional] |
| **deleted**        | **bool**                                              |             | [optional] |
| **archived**       | **bool**                                              |             | [optional] |

## Example

```python
from phrasetms_client.models.project_reference import ProjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectReference from a JSON string
project_reference_instance = ProjectReference.from_json(json)
# print the JSON string representation of the object
print ProjectReference.to_json()

# convert the object into a dict
project_reference_dict = project_reference_instance.to_dict()
# create an instance of ProjectReference from a dict
project_reference_from_dict = ProjectReference.from_dict(project_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
