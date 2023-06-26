# LoginToSessionDto

## Properties

| Name            | Type     | Description | Notes      |
| --------------- | -------- | ----------- | ---------- |
| **user_name**   | **str**  |             |
| **password**    | **str**  |             |
| **remember_me** | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.login_to_session_dto import LoginToSessionDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginToSessionDto from a JSON string
login_to_session_dto_instance = LoginToSessionDto.from_json(json)
# print the JSON string representation of the object
print LoginToSessionDto.to_json()

# convert the object into a dict
login_to_session_dto_dict = login_to_session_dto_instance.to_dict()
# create an instance of LoginToSessionDto from a dict
login_to_session_dto_from_dict = LoginToSessionDto.from_dict(login_to_session_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
