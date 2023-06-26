# RemoteUploadedFileDto

## Properties

| Name     | Type    | Description | Notes                 |
| -------- | ------- | ----------- | --------------------- |
| **uid**  | **str** |             | [optional] [readonly] |
| **name** | **str** |             | [optional] [readonly] |
| **size** | **int** |             | [optional] [readonly] |
| **type** | **str** |             | [optional] [readonly] |
| **url**  | **str** |             | [optional]            |

## Example

```python
from phrasetms_client.models.remote_uploaded_file_dto import RemoteUploadedFileDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteUploadedFileDto from a JSON string
remote_uploaded_file_dto_instance = RemoteUploadedFileDto.from_json(json)
# print the JSON string representation of the object
print RemoteUploadedFileDto.to_json()

# convert the object into a dict
remote_uploaded_file_dto_dict = remote_uploaded_file_dto_instance.to_dict()
# create an instance of RemoteUploadedFileDto from a dict
remote_uploaded_file_dto_from_dict = RemoteUploadedFileDto.from_dict(remote_uploaded_file_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
