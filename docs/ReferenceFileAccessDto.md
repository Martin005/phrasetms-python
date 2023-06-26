# ReferenceFileAccessDto

## Properties

| Name           | Type     | Description | Notes      |
| -------------- | -------- | ----------- | ---------- |
| **can_create** | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.reference_file_access_dto import ReferenceFileAccessDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceFileAccessDto from a JSON string
reference_file_access_dto_instance = ReferenceFileAccessDto.from_json(json)
# print the JSON string representation of the object
print ReferenceFileAccessDto.to_json()

# convert the object into a dict
reference_file_access_dto_dict = reference_file_access_dto_instance.to_dict()
# create an instance of ReferenceFileAccessDto from a dict
reference_file_access_dto_from_dict = ReferenceFileAccessDto.from_dict(reference_file_access_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
