# AsyncExportTMResponseDto

## Properties

| Name              | Type                                          | Description | Notes      |
| ----------------- | --------------------------------------------- | ----------- | ---------- |
| **async_request** | [**AsyncRequestV2Dto**](AsyncRequestV2Dto.md) |             | [optional] |
| **async_export**  | [**AsyncExportTMDto**](AsyncExportTMDto.md)   |             | [optional] |

## Example

```python
from phrasetms_client.models.async_export_tm_response_dto import AsyncExportTMResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncExportTMResponseDto from a JSON string
async_export_tm_response_dto_instance = AsyncExportTMResponseDto.from_json(json)
# print the JSON string representation of the object
print AsyncExportTMResponseDto.to_json()

# convert the object into a dict
async_export_tm_response_dto_dict = async_export_tm_response_dto_instance.to_dict()
# create an instance of AsyncExportTMResponseDto from a dict
async_export_tm_response_dto_from_dict = AsyncExportTMResponseDto.from_dict(async_export_tm_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
