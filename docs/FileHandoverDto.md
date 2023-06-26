# FileHandoverDto

## Properties

| Name         | Type    | Description                   | Notes      |
| ------------ | ------- | ----------------------------- | ---------- |
| **file_id**  | **str** | ID of the uploaded file       | [optional] |
| **filename** | **str** | Filename of the uploaded file | [optional] |

## Example

```python
from phrasetms_client.models.file_handover_dto import FileHandoverDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileHandoverDto from a JSON string
file_handover_dto_instance = FileHandoverDto.from_json(json)
# print the JSON string representation of the object
print FileHandoverDto.to_json()

# convert the object into a dict
file_handover_dto_dict = file_handover_dto_instance.to_dict()
# create an instance of FileHandoverDto from a dict
file_handover_dto_from_dict = FileHandoverDto.from_dict(file_handover_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
