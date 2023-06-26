# AbstractUserEditDto

## Properties

| Name                   | Type     | Description                                                                                                                    | Notes      |
| ---------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **user_name**          | **str**  |                                                                                                                                |
| **first_name**         | **str**  |                                                                                                                                |
| **last_name**          | **str**  |                                                                                                                                |
| **email**              | **str**  |                                                                                                                                |
| **role**               | **str**  | Enum: \&quot;ADMIN\&quot;, \&quot;PROJECT_MANAGER\&quot;, \&quot;LINGUIST\&quot;, \&quot;GUEST\&quot;, \&quot;SUBMITTER\&quot; |
| **timezone**           | **str**  |                                                                                                                                |
| **receive_newsletter** | **bool** | Default: true                                                                                                                  | [optional] |
| **note**               | **str**  |                                                                                                                                | [optional] |
| **active**             | **bool** | Default: true                                                                                                                  | [optional] |

## Example

```python
from phrasetms_client.models.abstract_user_edit_dto import AbstractUserEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractUserEditDto from a JSON string
abstract_user_edit_dto_instance = AbstractUserEditDto.from_json(json)
# print the JSON string representation of the object
print AbstractUserEditDto.to_json()

# convert the object into a dict
abstract_user_edit_dto_dict = abstract_user_edit_dto_instance.to_dict()
# create an instance of AbstractUserEditDto from a dict
abstract_user_edit_dto_from_dict = AbstractUserEditDto.from_dict(abstract_user_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
