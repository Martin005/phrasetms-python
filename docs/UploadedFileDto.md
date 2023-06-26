# UploadedFileDto

## Properties

| Name     | Type    | Description | Notes                 |
| -------- | ------- | ----------- | --------------------- |
| **uid**  | **str** |             | [optional] [readonly] |
| **name** | **str** |             | [optional] [readonly] |
| **size** | **int** |             | [optional] [readonly] |
| **type** | **str** |             | [optional] [readonly] |

## Example

```python
from phrasetms_client.models.uploaded_file_dto import UploadedFileDto

# TODO update the JSON string below
json = "{}"
# create an instance of UploadedFileDto from a JSON string
uploaded_file_dto_instance = UploadedFileDto.from_json(json)
# print the JSON string representation of the object
print UploadedFileDto.to_json()

# convert the object into a dict
uploaded_file_dto_dict = uploaded_file_dto_instance.to_dict()
# create an instance of UploadedFileDto from a dict
uploaded_file_dto_from_dict = UploadedFileDto.from_dict(uploaded_file_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
