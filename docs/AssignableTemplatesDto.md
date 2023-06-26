# AssignableTemplatesDto

## Properties

| Name                     | Type                                                  | Description | Notes      |
| ------------------------ | ----------------------------------------------------- | ----------- | ---------- |
| **assignable_templates** | [**List[ProjectTemplateDto]**](ProjectTemplateDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.assignable_templates_dto import AssignableTemplatesDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssignableTemplatesDto from a JSON string
assignable_templates_dto_instance = AssignableTemplatesDto.from_json(json)
# print the JSON string representation of the object
print AssignableTemplatesDto.to_json()

# convert the object into a dict
assignable_templates_dto_dict = assignable_templates_dto_instance.to_dict()
# create an instance of AssignableTemplatesDto from a dict
assignable_templates_dto_from_dict = AssignableTemplatesDto.from_dict(assignable_templates_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
