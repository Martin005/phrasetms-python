# ProjectTemplateCreateActionDto

## Properties

| Name                  | Type                                | Description | Notes      |
| --------------------- | ----------------------------------- | ----------- | ---------- |
| **project**           | [**UidReference**](UidReference.md) |             |
| **name**              | **str**                             |             |
| **import_settings**   | [**UidReference**](UidReference.md) |             | [optional] |
| **use_dynamic_title** | **bool**                            |             | [optional] |
| **dynamic_title**     | **str**                             |             | [optional] |

## Example

```python
from phrasetms_client.models.project_template_create_action_dto import ProjectTemplateCreateActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateCreateActionDto from a JSON string
project_template_create_action_dto_instance = ProjectTemplateCreateActionDto.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateCreateActionDto.to_json()

# convert the object into a dict
project_template_create_action_dto_dict = project_template_create_action_dto_instance.to_dict()
# create an instance of ProjectTemplateCreateActionDto from a dict
project_template_create_action_dto_from_dict = ProjectTemplateCreateActionDto.from_dict(project_template_create_action_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
