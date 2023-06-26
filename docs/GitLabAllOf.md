# GitLabAllOf

## Properties

| Name               | Type    | Description | Notes      |
| ------------------ | ------- | ----------- | ---------- |
| **commit_message** | **str** |             | [optional] |
| **host**           | **str** |             |
| **token**          | **str** |             |

## Example

```python
from phrasetms_client.models.git_lab_all_of import GitLabAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GitLabAllOf from a JSON string
git_lab_all_of_instance = GitLabAllOf.from_json(json)
# print the JSON string representation of the object
print GitLabAllOf.to_json()

# convert the object into a dict
git_lab_all_of_dict = git_lab_all_of_instance.to_dict()
# create an instance of GitLabAllOf from a dict
git_lab_all_of_from_dict = GitLabAllOf.from_dict(git_lab_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
