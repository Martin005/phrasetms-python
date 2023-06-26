# SftpAllOf

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
from phrasetms_client.models.sftp_all_of import SftpAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SftpAllOf from a JSON string
sftp_all_of_instance = SftpAllOf.from_json(json)
# print the JSON string representation of the object
print SftpAllOf.to_json()

# convert the object into a dict
sftp_all_of_dict = sftp_all_of_instance.to_dict()
# create an instance of SftpAllOf from a dict
sftp_all_of_from_dict = SftpAllOf.from_dict(sftp_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
