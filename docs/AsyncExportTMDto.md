# AsyncExportTMDto

## Properties

| Name                    | Type          | Description | Notes      |
| ----------------------- | ------------- | ----------- | ---------- |
| **trans_memory**        | **object**    |             | [optional] |
| **export_target_langs** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.async_export_tm_dto import AsyncExportTMDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncExportTMDto from a JSON string
async_export_tm_dto_instance = AsyncExportTMDto.from_json(json)
# print the JSON string representation of the object
print AsyncExportTMDto.to_json()

# convert the object into a dict
async_export_tm_dto_dict = async_export_tm_dto_instance.to_dict()
# create an instance of AsyncExportTMDto from a dict
async_export_tm_dto_from_dict = AsyncExportTMDto.from_dict(async_export_tm_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
