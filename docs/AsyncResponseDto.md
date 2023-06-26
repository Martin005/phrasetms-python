# AsyncResponseDto

## Properties

| Name                        | Type                                          | Description | Notes      |
| --------------------------- | --------------------------------------------- | ----------- | ---------- |
| **date_created**            | **datetime**                                  |             | [optional] |
| **error_code**              | **str**                                       |             | [optional] |
| **error_desc**              | **str**                                       |             | [optional] |
| **error_details**           | [**List[ErrorDetailDto]**](ErrorDetailDto.md) |             | [optional] |
| **warnings**                | [**List[ErrorDetailDto]**](ErrorDetailDto.md) |             | [optional] |
| **accepted_segments_count** | **int**                                       |             | [optional] |

## Example

```python
from phrasetms_client.models.async_response_dto import AsyncResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncResponseDto from a JSON string
async_response_dto_instance = AsyncResponseDto.from_json(json)
# print the JSON string representation of the object
print AsyncResponseDto.to_json()

# convert the object into a dict
async_response_dto_dict = async_response_dto_instance.to_dict()
# create an instance of AsyncResponseDto from a dict
async_response_dto_from_dict = AsyncResponseDto.from_dict(async_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
