# WordpressAllOf

## Properties

| Name                     | Type    | Description            | Notes |
| ------------------------ | ------- | ---------------------- | ----- |
| **basic_auth_user_name** | **str** |                        |
| **basic_auth_password**  | **str** |                        |
| **host**                 | **str** |                        |
| **token**                | **str** | Memsource plugin token |

## Example

```python
from phrasetms_client.models.wordpress_all_of import WordpressAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of WordpressAllOf from a JSON string
wordpress_all_of_instance = WordpressAllOf.from_json(json)
# print the JSON string representation of the object
print WordpressAllOf.to_json()

# convert the object into a dict
wordpress_all_of_dict = wordpress_all_of_instance.to_dict()
# create an instance of WordpressAllOf from a dict
wordpress_all_of_from_dict = WordpressAllOf.from_dict(wordpress_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
