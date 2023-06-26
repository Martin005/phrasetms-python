# UserReference

## Properties

| Name           | Type    | Description | Notes      |
| -------------- | ------- | ----------- | ---------- |
| **first_name** | **str** |             | [optional] |
| **last_name**  | **str** |             | [optional] |
| **user_name**  | **str** |             | [optional] |
| **email**      | **str** |             | [optional] |
| **role**       | **str** |             | [optional] |
| **id**         | **str** |             | [optional] |
| **uid**        | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.user_reference import UserReference

# TODO update the JSON string below
json = "{}"
# create an instance of UserReference from a JSON string
user_reference_instance = UserReference.from_json(json)
# print the JSON string representation of the object
print UserReference.to_json()

# convert the object into a dict
user_reference_dict = user_reference_instance.to_dict()
# create an instance of UserReference from a dict
user_reference_from_dict = UserReference.from_dict(user_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
