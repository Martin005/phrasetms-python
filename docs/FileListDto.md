# FileListDto

## Properties

| Name                       | Type                            | Description | Notes      |
| -------------------------- | ------------------------------- | ----------- | ---------- |
| **files**                  | [**List[FileDto]**](FileDto.md) |             | [optional] |
| **current_folder**         | **str**                         |             | [optional] |
| **encoded_current_folder** | **str**                         |             | [optional] |
| **root_folder**            | **bool**                        |             | [optional] |
| **last_changed_files**     | [**List[FileDto]**](FileDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.file_list_dto import FileListDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileListDto from a JSON string
file_list_dto_instance = FileListDto.from_json(json)
# print the JSON string representation of the object
print FileListDto.to_json()

# convert the object into a dict
file_list_dto_dict = file_list_dto_instance.to_dict()
# create an instance of FileListDto from a dict
file_list_dto_from_dict = FileListDto.from_dict(file_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
