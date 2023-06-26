# ProjectTemplateReference

## Properties

| Name              | Type                                                  | Description | Notes      |
| ----------------- | ----------------------------------------------------- | ----------- | ---------- |
| **template_name** | **str**                                               |             | [optional] |
| **source_lang**   | **str**                                               |             | [optional] |
| **target_langs**  | **List[str]**                                         |             | [optional] |
| **id**            | **str**                                               |             | [optional] |
| **uid**           | **str**                                               |             | [optional] |
| **owner**         | [**UserReference**](UserReference.md)                 |             | [optional] |
| **domain**        | [**DomainReference**](DomainReference.md)             |             | [optional] |
| **sub_domain**    | [**SubDomainReference**](SubDomainReference.md)       |             | [optional] |
| **cost_center**   | [**CostCenterReference**](CostCenterReference.md)     |             | [optional] |
| **business_unit** | [**BusinessUnitReference**](BusinessUnitReference.md) |             | [optional] |
| **note**          | **str**                                               |             | [optional] |
| **client**        | [**ClientReference**](ClientReference.md)             |             | [optional] |

## Example

```python
from phrasetms_client.models.project_template_reference import ProjectTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateReference from a JSON string
project_template_reference_instance = ProjectTemplateReference.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateReference.to_json()

# convert the object into a dict
project_template_reference_dict = project_template_reference_instance.to_dict()
# create an instance of ProjectTemplateReference from a dict
project_template_reference_from_dict = ProjectTemplateReference.from_dict(project_template_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
