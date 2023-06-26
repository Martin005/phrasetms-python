# Ftp

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
from phrasetms_client.models.ftp import Ftp

# TODO update the JSON string below
json = "{}"
# create an instance of Ftp from a JSON string
ftp_instance = Ftp.from_json(json)
# print the JSON string representation of the object
print Ftp.to_json()

# convert the object into a dict
ftp_dict = ftp_instance.to_dict()
# create an instance of Ftp from a dict
ftp_from_dict = Ftp.from_dict(ftp_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
