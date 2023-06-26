# LoginOtherDto

## Properties

| Name          | Type    | Description | Notes |
| ------------- | ------- | ----------- | ----- |
| **user_name** | **str** |             |

## Example

```python
from phrasetms_client.models.login_other_dto import LoginOtherDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginOtherDto from a JSON string
login_other_dto_instance = LoginOtherDto.from_json(json)
# print the JSON string representation of the object
print LoginOtherDto.to_json()

# convert the object into a dict
login_other_dto_dict = login_other_dto_instance.to_dict()
# create an instance of LoginOtherDto from a dict
login_other_dto_from_dict = LoginOtherDto.from_dict(login_other_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
