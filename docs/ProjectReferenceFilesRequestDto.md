# ProjectReferenceFilesRequestDto

## Properties

| Name                | Type                                    | Description | Notes |
| ------------------- | --------------------------------------- | ----------- | ----- |
| **reference_files** | [**List[IdReference]**](IdReference.md) |             |

## Example

```python
from phrasetms_client.models.project_reference_files_request_dto import ProjectReferenceFilesRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectReferenceFilesRequestDto from a JSON string
project_reference_files_request_dto_instance = ProjectReferenceFilesRequestDto.from_json(json)
# print the JSON string representation of the object
print ProjectReferenceFilesRequestDto.to_json()

# convert the object into a dict
project_reference_files_request_dto_dict = project_reference_files_request_dto_instance.to_dict()
# create an instance of ProjectReferenceFilesRequestDto from a dict
project_reference_files_request_dto_from_dict = ProjectReferenceFilesRequestDto.from_dict(project_reference_files_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
