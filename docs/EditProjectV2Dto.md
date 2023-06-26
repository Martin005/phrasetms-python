# EditProjectV2Dto

## Properties

| Name               | Type                                                                | Description                                       | Notes      |
| ------------------ | ------------------------------------------------------------------- | ------------------------------------------------- | ---------- |
| **name**           | **str**                                                             |                                                   |
| **status**         | **str**                                                             |                                                   | [optional] |
| **client**         | [**IdReference**](IdReference.md)                                   |                                                   | [optional] |
| **business_unit**  | [**IdReference**](IdReference.md)                                   |                                                   | [optional] |
| **domain**         | [**IdReference**](IdReference.md)                                   |                                                   | [optional] |
| **sub_domain**     | [**IdReference**](IdReference.md)                                   |                                                   | [optional] |
| **owner**          | [**IdReference**](IdReference.md)                                   |                                                   | [optional] |
| **purchase_order** | **str**                                                             |                                                   | [optional] |
| **date_due**       | **datetime**                                                        |                                                   | [optional] |
| **note**           | **str**                                                             |                                                   | [optional] |
| **file_handover**  | **bool**                                                            | Default: false                                    | [optional] |
| **lqa_profiles**   | [**List[LqaProfilesForWsV2Dto]**](LqaProfilesForWsV2Dto.md)         | Lqa profiles that will be added to workflow steps | [optional] |
| **archived**       | **bool**                                                            | Default: false                                    | [optional] |
| **custom_fields**  | [**List[CustomFieldInstanceApiDto]**](CustomFieldInstanceApiDto.md) | Custom fields for project                         | [optional] |

## Example

```python
from phrasetms_client.models.edit_project_v2_dto import EditProjectV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of EditProjectV2Dto from a JSON string
edit_project_v2_dto_instance = EditProjectV2Dto.from_json(json)
# print the JSON string representation of the object
print EditProjectV2Dto.to_json()

# convert the object into a dict
edit_project_v2_dto_dict = edit_project_v2_dto_instance.to_dict()
# create an instance of EditProjectV2Dto from a dict
edit_project_v2_dto_from_dict = EditProjectV2Dto.from_dict(edit_project_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
