# GitLab

## Properties

| Name               | Type    | Description | Notes      |
| ------------------ | ------- | ----------- | ---------- |
| **commit_message** | **str** |             | [optional] |
| **host**           | **str** |             |
| **token**          | **str** |             |

## Example

```python
from phrasetms_client.models.git_lab import GitLab

# TODO update the JSON string below
json = "{}"
# create an instance of GitLab from a JSON string
git_lab_instance = GitLab.from_json(json)
# print the JSON string representation of the object
print GitLab.to_json()

# convert the object into a dict
git_lab_dict = git_lab_instance.to_dict()
# create an instance of GitLab from a dict
git_lab_from_dict = GitLab.from_dict(git_lab_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
