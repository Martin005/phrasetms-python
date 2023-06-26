# LastLoginDto

## Properties

| Name                | Type                                  | Description | Notes      |
| ------------------- | ------------------------------------- | ----------- | ---------- |
| **user**            | [**UserReference**](UserReference.md) |             | [optional] |
| **last_login_date** | **datetime**                          |             | [optional] |

## Example

```python
from phrasetms_client.models.last_login_dto import LastLoginDto

# TODO update the JSON string below
json = "{}"
# create an instance of LastLoginDto from a JSON string
last_login_dto_instance = LastLoginDto.from_json(json)
# print the JSON string representation of the object
print LastLoginDto.to_json()

# convert the object into a dict
last_login_dto_dict = last_login_dto_instance.to_dict()
# create an instance of LastLoginDto from a dict
last_login_dto_from_dict = LastLoginDto.from_dict(last_login_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
