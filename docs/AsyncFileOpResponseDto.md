# AsyncFileOpResponseDto

## Properties

| Name             | Type                                  | Description | Notes      |
| ---------------- | ------------------------------------- | ----------- | ---------- |
| **id**           | **str**                               |             | [optional] |
| **created_by**   | [**UserReference**](UserReference.md) |             | [optional] |
| **date_created** | **datetime**                          |             | [optional] |
| **file_name**    | **str**                               |             | [optional] |
| **action**       | **str**                               |             | [optional] |

## Example

```python
from phrasetms_client.models.async_file_op_response_dto import AsyncFileOpResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncFileOpResponseDto from a JSON string
async_file_op_response_dto_instance = AsyncFileOpResponseDto.from_json(json)
# print the JSON string representation of the object
print AsyncFileOpResponseDto.to_json()

# convert the object into a dict
async_file_op_response_dto_dict = async_file_op_response_dto_instance.to_dict()
# create an instance of AsyncFileOpResponseDto from a dict
async_file_op_response_dto_from_dict = AsyncFileOpResponseDto.from_dict(async_file_op_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
