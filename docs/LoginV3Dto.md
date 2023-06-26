# LoginV3Dto

## Properties

| Name          | Type    | Description                                                 | Notes      |
| ------------- | ------- | ----------------------------------------------------------- | ---------- |
| **user_uid**  | **str** | When not filled, default user of identity will be logged in | [optional] |
| **user_name** | **str** |                                                             |
| **password**  | **str** |                                                             |
| **code**      | **str** | Required only for 2-factor authentication                   | [optional] |

## Example

```python
from phrasetms_client.models.login_v3_dto import LoginV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginV3Dto from a JSON string
login_v3_dto_instance = LoginV3Dto.from_json(json)
# print the JSON string representation of the object
print LoginV3Dto.to_json()

# convert the object into a dict
login_v3_dto_dict = login_v3_dto_instance.to_dict()
# create an instance of LoginV3Dto from a dict
login_v3_dto_from_dict = LoginV3Dto.from_dict(login_v3_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
