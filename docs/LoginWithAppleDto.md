# LoginWithAppleDto

## Properties

| Name                      | Type    | Description | Notes |
| ------------------------- | ------- | ----------- | ----- |
| **code_or_refresh_token** | **str** |             |

## Example

```python
from phrasetms_client.models.login_with_apple_dto import LoginWithAppleDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginWithAppleDto from a JSON string
login_with_apple_dto_instance = LoginWithAppleDto.from_json(json)
# print the JSON string representation of the object
print LoginWithAppleDto.to_json()

# convert the object into a dict
login_with_apple_dto_dict = login_with_apple_dto_instance.to_dict()
# create an instance of LoginWithAppleDto from a dict
login_with_apple_dto_from_dict = LoginWithAppleDto.from_dict(login_with_apple_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
