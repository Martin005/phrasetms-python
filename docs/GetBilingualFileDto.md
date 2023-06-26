# GetBilingualFileDto

## Properties

| Name     | Type                                      | Description | Notes      |
| -------- | ----------------------------------------- | ----------- | ---------- |
| **jobs** | [**List[UidReference]**](UidReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.get_bilingual_file_dto import GetBilingualFileDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetBilingualFileDto from a JSON string
get_bilingual_file_dto_instance = GetBilingualFileDto.from_json(json)
# print the JSON string representation of the object
print GetBilingualFileDto.to_json()

# convert the object into a dict
get_bilingual_file_dto_dict = get_bilingual_file_dto_instance.to_dict()
# create an instance of GetBilingualFileDto from a dict
get_bilingual_file_dto_from_dict = GetBilingualFileDto.from_dict(get_bilingual_file_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
