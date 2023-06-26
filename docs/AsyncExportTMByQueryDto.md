# AsyncExportTMByQueryDto

## Properties

| Name                    | Type                        | Description | Notes      |
| ----------------------- | --------------------------- | ----------- | ---------- |
| **async_request**       | **object**                  |             | [optional] |
| **trans_memory**        | **object**                  |             | [optional] |
| **export_target_langs** | **List[str]**               |             | [optional] |
| **queries**             | [**List[Query]**](Query.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.async_export_tmby_query_dto import AsyncExportTMByQueryDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncExportTMByQueryDto from a JSON string
async_export_tmby_query_dto_instance = AsyncExportTMByQueryDto.from_json(json)
# print the JSON string representation of the object
print AsyncExportTMByQueryDto.to_json()

# convert the object into a dict
async_export_tmby_query_dto_dict = async_export_tmby_query_dto_instance.to_dict()
# create an instance of AsyncExportTMByQueryDto from a dict
async_export_tmby_query_dto_from_dict = AsyncExportTMByQueryDto.from_dict(async_export_tmby_query_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
