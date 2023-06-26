# MentionableUserDto

## Properties

| Name            | Type                                  | Description | Notes      |
| --------------- | ------------------------------------- | ----------- | ---------- |
| **first_name**  | **str**                               |             | [optional] |
| **last_name**   | **str**                               |             | [optional] |
| **user_name**   | **str**                               |             | [optional] |
| **email**       | **str**                               |             | [optional] |
| **role**        | **str**                               |             | [optional] |
| **id**          | **str**                               |             | [optional] |
| **uid**         | **str**                               |             | [optional] |
| **unavailable** | **bool**                              |             | [optional] |
| **job_roles**   | [**List[JobRoleDto]**](JobRoleDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.mentionable_user_dto import MentionableUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of MentionableUserDto from a JSON string
mentionable_user_dto_instance = MentionableUserDto.from_json(json)
# print the JSON string representation of the object
print MentionableUserDto.to_json()

# convert the object into a dict
mentionable_user_dto_dict = mentionable_user_dto_instance.to_dict()
# create an instance of MentionableUserDto from a dict
mentionable_user_dto_from_dict = MentionableUserDto.from_dict(mentionable_user_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
