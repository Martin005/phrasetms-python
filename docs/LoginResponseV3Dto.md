# LoginResponseV3Dto

## Properties

| Name                                       | Type                                  | Description | Notes      |
| ------------------------------------------ | ------------------------------------- | ----------- | ---------- |
| **user**                                   | [**UserReference**](UserReference.md) |             | [optional] |
| **token**                                  | **str**                               |             | [optional] |
| **expires**                                | **datetime**                          |             | [optional] |
| **last_invalidate_all_sessions_performed** | **datetime**                          |             | [optional] |

## Example

```python
from phrasetms_client.models.login_response_v3_dto import LoginResponseV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginResponseV3Dto from a JSON string
login_response_v3_dto_instance = LoginResponseV3Dto.from_json(json)
# print the JSON string representation of the object
print LoginResponseV3Dto.to_json()

# convert the object into a dict
login_response_v3_dto_dict = login_response_v3_dto_instance.to_dict()
# create an instance of LoginResponseV3Dto from a dict
login_response_v3_dto_from_dict = LoginResponseV3Dto.from_dict(login_response_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
