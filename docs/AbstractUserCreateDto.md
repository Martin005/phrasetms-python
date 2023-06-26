# AbstractUserCreateDto

## Properties

| Name                   | Type     | Description                                                                                                                    | Notes      |
| ---------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **user_name**          | **str**  |                                                                                                                                |
| **first_name**         | **str**  |                                                                                                                                |
| **last_name**          | **str**  |                                                                                                                                |
| **email**              | **str**  |                                                                                                                                |
| **password**           | **str**  |                                                                                                                                |
| **role**               | **str**  | Enum: \&quot;ADMIN\&quot;, \&quot;PROJECT_MANAGER\&quot;, \&quot;LINGUIST\&quot;, \&quot;GUEST\&quot;, \&quot;SUBMITTER\&quot; |
| **timezone**           | **str**  |                                                                                                                                |
| **receive_newsletter** | **bool** | Default: true                                                                                                                  | [optional] |
| **note**               | **str**  |                                                                                                                                | [optional] |
| **active**             | **bool** | Default: true                                                                                                                  | [optional] |

## Example

```python
from phrasetms_client.models.abstract_user_create_dto import AbstractUserCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractUserCreateDto from a JSON string
abstract_user_create_dto_instance = AbstractUserCreateDto.from_json(json)
# print the JSON string representation of the object
print AbstractUserCreateDto.to_json()

# convert the object into a dict
abstract_user_create_dto_dict = abstract_user_create_dto_instance.to_dict()
# create an instance of AbstractUserCreateDto from a dict
abstract_user_create_dto_from_dict = AbstractUserCreateDto.from_dict(abstract_user_create_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
