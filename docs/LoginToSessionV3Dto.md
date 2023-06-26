# LoginToSessionV3Dto

## Properties

| Name                | Type     | Description                                                 | Notes      |
| ------------------- | -------- | ----------------------------------------------------------- | ---------- |
| **user_uid**        | **str**  | When not filled, default user of identity will be logged in | [optional] |
| **user_name**       | **str**  |                                                             |
| **password**        | **str**  |                                                             |
| **remember_me**     | **bool** |                                                             | [optional] |
| **two_factor_code** | **int**  |                                                             | [optional] |
| **captcha_code**    | **str**  |                                                             | [optional] |

## Example

```python
from phrasetms_client.models.login_to_session_v3_dto import LoginToSessionV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginToSessionV3Dto from a JSON string
login_to_session_v3_dto_instance = LoginToSessionV3Dto.from_json(json)
# print the JSON string representation of the object
print LoginToSessionV3Dto.to_json()

# convert the object into a dict
login_to_session_v3_dto_dict = login_to_session_v3_dto_instance.to_dict()
# create an instance of LoginToSessionV3Dto from a dict
login_to_session_v3_dto_from_dict = LoginToSessionV3Dto.from_dict(login_to_session_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
