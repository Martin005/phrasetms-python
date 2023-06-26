# BitbucketServer

## Properties

| Name               | Type    | Description | Notes      |
| ------------------ | ------- | ----------- | ---------- |
| **host**           | **str** |             |
| **commit_message** | **str** |             | [optional] |
| **token**          | **str** |             |

## Example

```python
from phrasetms_client.models.bitbucket_server import BitbucketServer

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketServer from a JSON string
bitbucket_server_instance = BitbucketServer.from_json(json)
# print the JSON string representation of the object
print BitbucketServer.to_json()

# convert the object into a dict
bitbucket_server_dict = bitbucket_server_instance.to_dict()
# create an instance of BitbucketServer from a dict
bitbucket_server_from_dict = BitbucketServer.from_dict(bitbucket_server_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
