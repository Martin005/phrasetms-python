# LoginUserDto

## Properties

| Name             | Type                                                  | Description | Notes      |
| ---------------- | ----------------------------------------------------- | ----------- | ---------- |
| **user**         | [**UserReference**](UserReference.md)                 |             | [optional] |
| **csrf_token**   | **str**                                               |             | [optional] |
| **organization** | [**OrganizationReference**](OrganizationReference.md) |             | [optional] |
| **edition**      | [**EditionDto**](EditionDto.md)                       |             | [optional] |
| **features**     | [**FeaturesDto**](FeaturesDto.md)                     |             | [optional] |

## Example

```python
from phrasetms_client.models.login_user_dto import LoginUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginUserDto from a JSON string
login_user_dto_instance = LoginUserDto.from_json(json)
# print the JSON string representation of the object
print LoginUserDto.to_json()

# convert the object into a dict
login_user_dto_dict = login_user_dto_instance.to_dict()
# create an instance of LoginUserDto from a dict
login_user_dto_from_dict = LoginUserDto.from_dict(login_user_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
