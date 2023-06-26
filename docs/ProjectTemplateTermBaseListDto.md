# ProjectTemplateTermBaseListDto

## Properties

| Name           | Type                                                                  | Description | Notes      |
| -------------- | --------------------------------------------------------------------- | ----------- | ---------- |
| **term_bases** | [**List[ProjectTemplateTermBaseDto]**](ProjectTemplateTermBaseDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.project_template_term_base_list_dto import ProjectTemplateTermBaseListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateTermBaseListDto from a JSON string
project_template_term_base_list_dto_instance = ProjectTemplateTermBaseListDto.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateTermBaseListDto.to_json()

# convert the object into a dict
project_template_term_base_list_dto_dict = project_template_term_base_list_dto_instance.to_dict()
# create an instance of ProjectTemplateTermBaseListDto from a dict
project_template_term_base_list_dto_from_dict = ProjectTemplateTermBaseListDto.from_dict(project_template_term_base_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
