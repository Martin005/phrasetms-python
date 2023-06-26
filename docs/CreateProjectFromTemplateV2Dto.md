# CreateProjectFromTemplateV2Dto

## Properties

| Name               | Type                                    | Description | Notes      |
| ------------------ | --------------------------------------- | ----------- | ---------- |
| **name**           | **str**                                 |             |
| **source_lang**    | **str**                                 |             | [optional] |
| **target_langs**   | **List[str]**                           |             | [optional] |
| **workflow_steps** | [**List[IdReference]**](IdReference.md) |             | [optional] |
| **date_due**       | **datetime**                            |             | [optional] |
| **note**           | **str**                                 |             | [optional] |
| **client**         | [**IdReference**](IdReference.md)       |             | [optional] |
| **business_unit**  | [**IdReference**](IdReference.md)       |             | [optional] |
| **domain**         | [**IdReference**](IdReference.md)       |             | [optional] |
| **sub_domain**     | [**IdReference**](IdReference.md)       |             | [optional] |
| **cost_center**    | [**IdReference**](IdReference.md)       |             | [optional] |

## Example

```python
from phrasetms_client.models.create_project_from_template_v2_dto import CreateProjectFromTemplateV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectFromTemplateV2Dto from a JSON string
create_project_from_template_v2_dto_instance = CreateProjectFromTemplateV2Dto.from_json(json)
# print the JSON string representation of the object
print CreateProjectFromTemplateV2Dto.to_json()

# convert the object into a dict
create_project_from_template_v2_dto_dict = create_project_from_template_v2_dto_instance.to_dict()
# create an instance of CreateProjectFromTemplateV2Dto from a dict
create_project_from_template_v2_dto_from_dict = CreateProjectFromTemplateV2Dto.from_dict(create_project_from_template_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
