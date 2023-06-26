# MetadataOptionReference

## Properties

| Name      | Type    | Description | Notes      |
| --------- | ------- | ----------- | ---------- |
| **uid**   | **str** |             | [optional] |
| **value** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.metadata_option_reference import MetadataOptionReference

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataOptionReference from a JSON string
metadata_option_reference_instance = MetadataOptionReference.from_json(json)
# print the JSON string representation of the object
print MetadataOptionReference.to_json()

# convert the object into a dict
metadata_option_reference_dict = metadata_option_reference_instance.to_dict()
# create an instance of MetadataOptionReference from a dict
metadata_option_reference_from_dict = MetadataOptionReference.from_dict(metadata_option_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
