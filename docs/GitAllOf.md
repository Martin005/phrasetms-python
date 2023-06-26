# GitAllOf

## Properties

| Name                | Type    | Description | Notes      |
| ------------------- | ------- | ----------- | ---------- |
| **user_name**       | **str** |             |
| **password**        | **str** |             |
| **host**            | **str** |             |
| **commit_message**  | **str** |             | [optional] |
| **ssh_key_name**    | **str** |             | [optional] |
| **ssh_key**         | **str** |             | [optional] |
| **ssh_pass_phrase** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.git_all_of import GitAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GitAllOf from a JSON string
git_all_of_instance = GitAllOf.from_json(json)
# print the JSON string representation of the object
print GitAllOf.to_json()

# convert the object into a dict
git_all_of_dict = git_all_of_instance.to_dict()
# create an instance of GitAllOf from a dict
git_all_of_from_dict = GitAllOf.from_dict(git_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
