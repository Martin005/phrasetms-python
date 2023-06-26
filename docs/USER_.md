# USER

## Properties

| Name           | Type     | Description | Notes                 |
| -------------- | -------- | ----------- | --------------------- |
| **user_name**  | **str**  |             | [optional] [readonly] |
| **first_name** | **str**  |             | [optional] [readonly] |
| **last_name**  | **str**  |             | [optional] [readonly] |
| **email**      | **str**  |             | [optional] [readonly] |
| **active**     | **bool** |             | [optional] [readonly] |

## Example

```python
from phrasetms_client.models.user_ import USER

# TODO update the JSON string below
json = "{}"
# create an instance of USER from a JSON string
user_instance = USER.from_json(json)
# print the JSON string representation of the object
print USER.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of USER from a dict
user_from_dict = USER.from_dict(user_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
