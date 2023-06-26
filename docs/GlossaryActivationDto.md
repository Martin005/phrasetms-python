# GlossaryActivationDto

## Properties

| Name       | Type     | Description | Notes      |
| ---------- | -------- | ----------- | ---------- |
| **active** | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.glossary_activation_dto import GlossaryActivationDto

# TODO update the JSON string below
json = "{}"
# create an instance of GlossaryActivationDto from a JSON string
glossary_activation_dto_instance = GlossaryActivationDto.from_json(json)
# print the JSON string representation of the object
print GlossaryActivationDto.to_json()

# convert the object into a dict
glossary_activation_dto_dict = glossary_activation_dto_instance.to_dict()
# create an instance of GlossaryActivationDto from a dict
glossary_activation_dto_from_dict = GlossaryActivationDto.from_dict(glossary_activation_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
