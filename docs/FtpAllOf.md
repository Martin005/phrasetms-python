# FtpAllOf

## Properties

| Name           | Type    | Description              | Notes      |
| -------------- | ------- | ------------------------ | ---------- |
| **user_name**  | **str** |                          |
| **password**   | **str** |                          |
| **host**       | **str** |                          |
| **port**       | **int** |                          |
| **encryption** | **str** | Default TLS_IF_AVAILABLE | [optional] |

## Example

```python
from phrasetms_client.models.ftp_all_of import FtpAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FtpAllOf from a JSON string
ftp_all_of_instance = FtpAllOf.from_json(json)
# print the JSON string representation of the object
print FtpAllOf.to_json()

# convert the object into a dict
ftp_all_of_dict = ftp_all_of_instance.to_dict()
# create an instance of FtpAllOf from a dict
ftp_all_of_from_dict = FtpAllOf.from_dict(ftp_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
