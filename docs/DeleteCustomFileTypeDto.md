# DeleteCustomFileTypeDto

## Properties

| Name                  | Type                                      | Description | Notes |
| --------------------- | ----------------------------------------- | ----------- | ----- |
| **custom_file_types** | [**List[UidReference]**](UidReference.md) |             |

## Example

```python
from phrasetms_client.models.delete_custom_file_type_dto import DeleteCustomFileTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCustomFileTypeDto from a JSON string
delete_custom_file_type_dto_instance = DeleteCustomFileTypeDto.from_json(json)
# print the JSON string representation of the object
print DeleteCustomFileTypeDto.to_json()

# convert the object into a dict
delete_custom_file_type_dto_dict = delete_custom_file_type_dto_instance.to_dict()
# create an instance of DeleteCustomFileTypeDto from a dict
delete_custom_file_type_dto_from_dict = DeleteCustomFileTypeDto.from_dict(delete_custom_file_type_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
