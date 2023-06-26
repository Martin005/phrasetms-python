# AsyncResponseV2Dto

## Properties

| Name              | Type                                              | Description | Notes      |
| ----------------- | ------------------------------------------------- | ----------- | ---------- |
| **date_created**  | **datetime**                                      |             | [optional] |
| **error_code**    | **str**                                           |             | [optional] |
| **error_desc**    | **str**                                           |             | [optional] |
| **error_details** | [**List[ErrorDetailDtoV2]**](ErrorDetailDtoV2.md) |             | [optional] |
| **warnings**      | [**List[ErrorDetailDtoV2]**](ErrorDetailDtoV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.async_response_v2_dto import AsyncResponseV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncResponseV2Dto from a JSON string
async_response_v2_dto_instance = AsyncResponseV2Dto.from_json(json)
# print the JSON string representation of the object
print AsyncResponseV2Dto.to_json()

# convert the object into a dict
async_response_v2_dto_dict = async_response_v2_dto_instance.to_dict()
# create an instance of AsyncResponseV2Dto from a dict
async_response_v2_dto_from_dict = AsyncResponseV2Dto.from_dict(async_response_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
