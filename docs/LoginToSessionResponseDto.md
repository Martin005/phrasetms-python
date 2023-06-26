# LoginToSessionResponseDto

## Properties

| Name           | Type                                  | Description | Notes      |
| -------------- | ------------------------------------- | ----------- | ---------- |
| **user**       | [**UserReference**](UserReference.md) |             | [optional] |
| **cookie**     | **str**                               |             | [optional] |
| **csrf_token** | **str**                               |             | [optional] |

## Example

```python
from phrasetms_client.models.login_to_session_response_dto import LoginToSessionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginToSessionResponseDto from a JSON string
login_to_session_response_dto_instance = LoginToSessionResponseDto.from_json(json)
# print the JSON string representation of the object
print LoginToSessionResponseDto.to_json()

# convert the object into a dict
login_to_session_response_dto_dict = login_to_session_response_dto_instance.to_dict()
# create an instance of LoginToSessionResponseDto from a dict
login_to_session_response_dto_from_dict = LoginToSessionResponseDto.from_dict(login_to_session_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
