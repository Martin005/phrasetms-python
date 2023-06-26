# TagMetadataDto

## Properties

| Name                 | Type    | Description | Notes      |
| -------------------- | ------- | ----------- | ---------- |
| **id**               | **str** |             | [optional] |
| **type**             | **str** |             | [optional] |
| **content**          | **str** |             | [optional] |
| **trans_attributes** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.tag_metadata_dto import TagMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of TagMetadataDto from a JSON string
tag_metadata_dto_instance = TagMetadataDto.from_json(json)
# print the JSON string representation of the object
print TagMetadataDto.to_json()

# convert the object into a dict
tag_metadata_dto_dict = tag_metadata_dto_instance.to_dict()
# create an instance of TagMetadataDto from a dict
tag_metadata_dto_from_dict = TagMetadataDto.from_dict(tag_metadata_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
