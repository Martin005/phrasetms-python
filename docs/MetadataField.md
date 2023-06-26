# MetadataField

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **type** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.metadata_field import MetadataField

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataField from a JSON string
metadata_field_instance = MetadataField.from_json(json)
# print the JSON string representation of the object
print MetadataField.to_json()

# convert the object into a dict
metadata_field_dict = metadata_field_instance.to_dict()
# create an instance of MetadataField from a dict
metadata_field_from_dict = MetadataField.from_dict(metadata_field_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
