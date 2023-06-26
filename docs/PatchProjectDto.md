# PatchProjectDto

## Properties

| Name                                     | Type                                                                    | Description | Notes      |
| ---------------------------------------- | ----------------------------------------------------------------------- | ----------- | ---------- |
| **name**                                 | **str**                                                                 |             | [optional] |
| **status**                               | **str**                                                                 |             | [optional] |
| **client**                               | [**IdReference**](IdReference.md)                                       |             | [optional] |
| **business_unit**                        | [**IdReference**](IdReference.md)                                       |             | [optional] |
| **domain**                               | [**IdReference**](IdReference.md)                                       |             | [optional] |
| **sub_domain**                           | [**IdReference**](IdReference.md)                                       |             | [optional] |
| **owner**                                | [**IdReference**](IdReference.md)                                       |             | [optional] |
| **purchase_order**                       | **str**                                                                 |             | [optional] |
| **date_due**                             | **datetime**                                                            |             | [optional] |
| **note**                                 | **str**                                                                 |             | [optional] |
| **machine_translate_settings**           | [**UidReference**](UidReference.md)                                     |             | [optional] |
| **machine_translate_settings_per_langs** | [**List[ProjectMTSettingsPerLangDto]**](ProjectMTSettingsPerLangDto.md) |             | [optional] |
| **archived**                             | **bool**                                                                |             | [optional] |

## Example

```python
from phrasetms_client.models.patch_project_dto import PatchProjectDto

# TODO update the JSON string below
json = "{}"
# create an instance of PatchProjectDto from a JSON string
patch_project_dto_instance = PatchProjectDto.from_json(json)
# print the JSON string representation of the object
print PatchProjectDto.to_json()

# convert the object into a dict
patch_project_dto_dict = patch_project_dto_instance.to_dict()
# create an instance of PatchProjectDto from a dict
patch_project_dto_from_dict = PatchProjectDto.from_dict(patch_project_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
