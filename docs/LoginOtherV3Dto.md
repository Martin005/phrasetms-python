# LoginOtherV3Dto

## Properties

| Name          | Type    | Description                                                 | Notes      |
| ------------- | ------- | ----------------------------------------------------------- | ---------- |
| **user_uid**  | **str** | When not filled, default user of identity will be logged in | [optional] |
| **user_name** | **str** |                                                             |

## Example

```python
from phrasetms_client.models.login_other_v3_dto import LoginOtherV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginOtherV3Dto from a JSON string
login_other_v3_dto_instance = LoginOtherV3Dto.from_json(json)
# print the JSON string representation of the object
print LoginOtherV3Dto.to_json()

# convert the object into a dict
login_other_v3_dto_dict = login_other_v3_dto_instance.to_dict()
# create an instance of LoginOtherV3Dto from a dict
login_other_v3_dto_from_dict = LoginOtherV3Dto.from_dict(login_other_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
