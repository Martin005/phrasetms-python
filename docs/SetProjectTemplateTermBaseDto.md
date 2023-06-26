# SetProjectTemplateTermBaseDto

## Properties

| Name                             | Type                                    | Description | Notes      |
| -------------------------------- | --------------------------------------- | ----------- | ---------- |
| **read_term_bases**              | [**List[IdReference]**](IdReference.md) |             | [optional] |
| **write_term_base**              | [**IdReference**](IdReference.md)       |             | [optional] |
| **quality_assurance_term_bases** | [**List[IdReference]**](IdReference.md) |             | [optional] |
| **target_lang**                  | **str**                                 |             | [optional] |
| **workflow_step**                | [**IdReference**](IdReference.md)       |             | [optional] |

## Example

```python
from phrasetms_client.models.set_project_template_term_base_dto import SetProjectTemplateTermBaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetProjectTemplateTermBaseDto from a JSON string
set_project_template_term_base_dto_instance = SetProjectTemplateTermBaseDto.from_json(json)
# print the JSON string representation of the object
print SetProjectTemplateTermBaseDto.to_json()

# convert the object into a dict
set_project_template_term_base_dto_dict = set_project_template_term_base_dto_instance.to_dict()
# create an instance of SetProjectTemplateTermBaseDto from a dict
set_project_template_term_base_dto_from_dict = SetProjectTemplateTermBaseDto.from_dict(set_project_template_term_base_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
