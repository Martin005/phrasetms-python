# Wordpress

## Properties

| Name                     | Type    | Description            | Notes |
| ------------------------ | ------- | ---------------------- | ----- |
| **basic_auth_user_name** | **str** |                        |
| **basic_auth_password**  | **str** |                        |
| **host**                 | **str** |                        |
| **token**                | **str** | Memsource plugin token |

## Example

```python
from phrasetms_client.models.wordpress import Wordpress

# TODO update the JSON string below
json = "{}"
# create an instance of Wordpress from a JSON string
wordpress_instance = Wordpress.from_json(json)
# print the JSON string representation of the object
print Wordpress.to_json()

# convert the object into a dict
wordpress_dict = wordpress_instance.to_dict()
# create an instance of Wordpress from a dict
wordpress_from_dict = Wordpress.from_dict(wordpress_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
