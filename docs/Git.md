# Git

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
from phrasetms_client.models.git import Git

# TODO update the JSON string below
json = "{}"
# create an instance of Git from a JSON string
git_instance = Git.from_json(json)
# print the JSON string representation of the object
print Git.to_json()

# convert the object into a dict
git_dict = git_instance.to_dict()
# create an instance of Git from a dict
git_from_dict = Git.from_dict(git_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
