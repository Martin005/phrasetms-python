# BitbucketServerAllOf

## Properties

| Name               | Type    | Description | Notes      |
| ------------------ | ------- | ----------- | ---------- |
| **host**           | **str** |             |
| **commit_message** | **str** |             | [optional] |
| **token**          | **str** |             |

## Example

```python
from phrasetms_client.models.bitbucket_server_all_of import BitbucketServerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketServerAllOf from a JSON string
bitbucket_server_all_of_instance = BitbucketServerAllOf.from_json(json)
# print the JSON string representation of the object
print BitbucketServerAllOf.to_json()

# convert the object into a dict
bitbucket_server_all_of_dict = bitbucket_server_all_of_instance.to_dict()
# create an instance of BitbucketServerAllOf from a dict
bitbucket_server_all_of_from_dict = BitbucketServerAllOf.from_dict(bitbucket_server_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
