# UserPasswordEditDto

## Properties

| Name         | Type    | Description | Notes |
| ------------ | ------- | ----------- | ----- |
| **password** | **str** |             |

## Example

```python
from phrasetms_client.models.user_password_edit_dto import UserPasswordEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserPasswordEditDto from a JSON string
user_password_edit_dto_instance = UserPasswordEditDto.from_json(json)
# print the JSON string representation of the object
print UserPasswordEditDto.to_json()

# convert the object into a dict
user_password_edit_dto_dict = user_password_edit_dto_instance.to_dict()
# create an instance of UserPasswordEditDto from a dict
user_password_edit_dto_from_dict = UserPasswordEditDto.from_dict(user_password_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
