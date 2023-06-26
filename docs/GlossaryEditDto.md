# GlossaryEditDto

## Properties

| Name      | Type                              | Description | Notes      |
| --------- | --------------------------------- | ----------- | ---------- |
| **name**  | **str**                           |             |
| **langs** | **List[str]**                     |             |
| **owner** | [**IdReference**](IdReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.glossary_edit_dto import GlossaryEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of GlossaryEditDto from a JSON string
glossary_edit_dto_instance = GlossaryEditDto.from_json(json)
# print the JSON string representation of the object
print GlossaryEditDto.to_json()

# convert the object into a dict
glossary_edit_dto_dict = glossary_edit_dto_instance.to_dict()
# create an instance of GlossaryEditDto from a dict
glossary_edit_dto_from_dict = GlossaryEditDto.from_dict(glossary_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
