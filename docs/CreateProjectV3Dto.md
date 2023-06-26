# CreateProjectV3Dto

## Properties

| Name               | Type                                                                | Description                                       | Notes      |
| ------------------ | ------------------------------------------------------------------- | ------------------------------------------------- | ---------- |
| **name**           | **str**                                                             |                                                   |
| **source_lang**    | **str**                                                             |                                                   |
| **target_langs**   | **List[str]**                                                       |                                                   |
| **client**         | [**IdReference**](IdReference.md)                                   |                                                   | [optional] |
| **business_unit**  | [**IdReference**](IdReference.md)                                   |                                                   | [optional] |
| **domain**         | [**IdReference**](IdReference.md)                                   |                                                   | [optional] |
| **sub_domain**     | [**IdReference**](IdReference.md)                                   |                                                   | [optional] |
| **cost_center**    | [**IdReference**](IdReference.md)                                   |                                                   | [optional] |
| **purchase_order** | **str**                                                             |                                                   | [optional] |
| **workflow_steps** | [**List[IdReference]**](IdReference.md)                             |                                                   | [optional] |
| **date_due**       | **datetime**                                                        |                                                   | [optional] |
| **note**           | **str**                                                             |                                                   | [optional] |
| **lqa_profiles**   | [**List[LqaProfilesForWsV2Dto]**](LqaProfilesForWsV2Dto.md)         | Lqa profiles that will be added to workflow steps | [optional] |
| **custom_fields**  | [**List[CustomFieldInstanceApiDto]**](CustomFieldInstanceApiDto.md) | Custom fields for project                         | [optional] |
| **file_handover**  | **bool**                                                            | Default: false                                    | [optional] |

## Example

```python
from phrasetms_client.models.create_project_v3_dto import CreateProjectV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectV3Dto from a JSON string
create_project_v3_dto_instance = CreateProjectV3Dto.from_json(json)
# print the JSON string representation of the object
print CreateProjectV3Dto.to_json()

# convert the object into a dict
create_project_v3_dto_dict = create_project_v3_dto_instance.to_dict()
# create an instance of CreateProjectV3Dto from a dict
create_project_v3_dto_from_dict = CreateProjectV3Dto.from_dict(create_project_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
