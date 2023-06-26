# FileDto

## Properties

| Name              | Type                        | Description | Notes      |
| ----------------- | --------------------------- | ----------- | ---------- |
| **id**            | **str**                     |             | [optional] |
| **name**          | **str**                     |             | [optional] |
| **encoded_name**  | **str**                     |             | [optional] |
| **content_type**  | **str**                     |             | [optional] |
| **note**          | **str**                     |             | [optional] |
| **size**          | **int**                     |             | [optional] |
| **directory**     | **bool**                    |             | [optional] |
| **last_modified** | **datetime**                |             | [optional] |
| **selected**      | **bool**                    |             | [optional] |
| **error**         | [**ErrorDto**](ErrorDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.file_dto import FileDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileDto from a JSON string
file_dto_instance = FileDto.from_json(json)
# print the JSON string representation of the object
print FileDto.to_json()

# convert the object into a dict
file_dto_dict = file_dto_instance.to_dict()
# create an instance of FileDto from a dict
file_dto_from_dict = FileDto.from_dict(file_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
