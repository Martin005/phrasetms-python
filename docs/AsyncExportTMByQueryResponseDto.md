# AsyncExportTMByQueryResponseDto

## Properties

| Name              | Type                                                      | Description | Notes      |
| ----------------- | --------------------------------------------------------- | ----------- | ---------- |
| **async_request** | [**AsyncRequestDto**](AsyncRequestDto.md)                 |             | [optional] |
| **async_export**  | [**AsyncExportTMByQueryDto**](AsyncExportTMByQueryDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.async_export_tmby_query_response_dto import AsyncExportTMByQueryResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncExportTMByQueryResponseDto from a JSON string
async_export_tmby_query_response_dto_instance = AsyncExportTMByQueryResponseDto.from_json(json)
# print the JSON string representation of the object
print AsyncExportTMByQueryResponseDto.to_json()

# convert the object into a dict
async_export_tmby_query_response_dto_dict = async_export_tmby_query_response_dto_instance.to_dict()
# create an instance of AsyncExportTMByQueryResponseDto from a dict
async_export_tmby_query_response_dto_from_dict = AsyncExportTMByQueryResponseDto.from_dict(async_export_tmby_query_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
