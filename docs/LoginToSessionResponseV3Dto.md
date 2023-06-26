# LoginToSessionResponseV3Dto

## Properties

| Name           | Type                                  | Description | Notes      |
| -------------- | ------------------------------------- | ----------- | ---------- |
| **user**       | [**UserReference**](UserReference.md) |             | [optional] |
| **cookie**     | **str**                               |             | [optional] |
| **csrf_token** | **str**                               |             | [optional] |

## Example

```python
from phrasetms_client.models.login_to_session_response_v3_dto import LoginToSessionResponseV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginToSessionResponseV3Dto from a JSON string
login_to_session_response_v3_dto_instance = LoginToSessionResponseV3Dto.from_json(json)
# print the JSON string representation of the object
print LoginToSessionResponseV3Dto.to_json()

# convert the object into a dict
login_to_session_response_v3_dto_dict = login_to_session_response_v3_dto_instance.to_dict()
# create an instance of LoginToSessionResponseV3Dto from a dict
login_to_session_response_v3_dto_from_dict = LoginToSessionResponseV3Dto.from_dict(login_to_session_response_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
