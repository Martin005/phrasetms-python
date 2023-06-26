# AsyncRequestDto

## Properties

| Name               | Type                                        | Description | Notes      |
| ------------------ | ------------------------------------------- | ----------- | ---------- |
| **id**             | **str**                                     |             | [optional] |
| **created_by**     | [**UserReference**](UserReference.md)       |             | [optional] |
| **date_created**   | **datetime**                                |             | [optional] |
| **action**         | **str**                                     |             | [optional] |
| **async_response** | [**AsyncResponseDto**](AsyncResponseDto.md) |             | [optional] |
| **parent**         | [**AsyncRequestDto**](AsyncRequestDto.md)   |             | [optional] |
| **project**        | [**ProjectReference**](ProjectReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.async_request_dto import AsyncRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncRequestDto from a JSON string
async_request_dto_instance = AsyncRequestDto.from_json(json)
# print the JSON string representation of the object
print AsyncRequestDto.to_json()

# convert the object into a dict
async_request_dto_dict = async_request_dto_instance.to_dict()
# create an instance of AsyncRequestDto from a dict
async_request_dto_from_dict = AsyncRequestDto.from_dict(async_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
