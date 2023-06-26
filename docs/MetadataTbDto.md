# MetadataTbDto

## Properties

| Name                     | Type               | Description | Notes      |
| ------------------------ | ------------------ | ----------- | ---------- |
| **terms_count**          | **int**            |             | [optional] |
| **metadata_by_language** | **Dict[str, int]** |             | [optional] |

## Example

```python
from phrasetms_client.models.metadata_tb_dto import MetadataTbDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataTbDto from a JSON string
metadata_tb_dto_instance = MetadataTbDto.from_json(json)
# print the JSON string representation of the object
print MetadataTbDto.to_json()

# convert the object into a dict
metadata_tb_dto_dict = metadata_tb_dto_instance.to_dict()
# create an instance of MetadataTbDto from a dict
metadata_tb_dto_from_dict = MetadataTbDto.from_dict(metadata_tb_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
