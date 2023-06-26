# TagMetadata

## Properties

| Name                 | Type    | Description | Notes      |
| -------------------- | ------- | ----------- | ---------- |
| **id**               | **str** |             | [optional] |
| **type**             | **str** |             | [optional] |
| **content**          | **str** |             | [optional] |
| **trans_attributes** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.tag_metadata import TagMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TagMetadata from a JSON string
tag_metadata_instance = TagMetadata.from_json(json)
# print the JSON string representation of the object
print TagMetadata.to_json()

# convert the object into a dict
tag_metadata_dict = tag_metadata_instance.to_dict()
# create an instance of TagMetadata from a dict
tag_metadata_from_dict = TagMetadata.from_dict(tag_metadata_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
