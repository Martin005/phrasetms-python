# TermBaseEditDto

## Properties

| Name              | Type                              | Description | Notes      |
| ----------------- | --------------------------------- | ----------- | ---------- |
| **name**          | **str**                           |             |
| **langs**         | **List[str]**                     |             |
| **client**        | [**IdReference**](IdReference.md) |             | [optional] |
| **domain**        | [**IdReference**](IdReference.md) |             | [optional] |
| **sub_domain**    | [**IdReference**](IdReference.md) |             | [optional] |
| **business_unit** | [**IdReference**](IdReference.md) |             | [optional] |
| **owner**         | [**IdReference**](IdReference.md) |             | [optional] |
| **note**          | **str**                           |             | [optional] |

## Example

```python
from phrasetms_client.models.term_base_edit_dto import TermBaseEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of TermBaseEditDto from a JSON string
term_base_edit_dto_instance = TermBaseEditDto.from_json(json)
# print the JSON string representation of the object
print TermBaseEditDto.to_json()

# convert the object into a dict
term_base_edit_dto_dict = term_base_edit_dto_instance.to_dict()
# create an instance of TermBaseEditDto from a dict
term_base_edit_dto_from_dict = TermBaseEditDto.from_dict(term_base_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
