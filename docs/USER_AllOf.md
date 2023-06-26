# USERAllOf

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
from phrasetms_client.models.user__all_of import USERAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of USERAllOf from a JSON string
user__all_of_instance = USERAllOf.from_json(json)
# print the JSON string representation of the object
print USERAllOf.to_json()

# convert the object into a dict
user__all_of_dict = user__all_of_instance.to_dict()
# create an instance of USERAllOf from a dict
user__all_of_from_dict = USERAllOf.from_dict(user__all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
