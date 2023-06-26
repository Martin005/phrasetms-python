# Sftp

## Properties

| Name                | Type    | Description | Notes      |
| ------------------- | ------- | ----------- | ---------- |
| **host**            | **str** |             |
| **port**            | **int** |             |
| **user_name**       | **str** |             |
| **password**        | **str** |             |
| **ssh_key_name**    | **str** |             | [optional] |
| **ssh_key**         | **str** |             | [optional] |
| **ssh_pass_phrase** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.sftp import Sftp

# TODO update the JSON string below
json = "{}"
# create an instance of Sftp from a JSON string
sftp_instance = Sftp.from_json(json)
# print the JSON string representation of the object
print Sftp.to_json()

# convert the object into a dict
sftp_dict = sftp_instance.to_dict()
# create an instance of Sftp from a dict
sftp_from_dict = Sftp.from_dict(sftp_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
