# ExportTMDto

## Properties

| Name                    | Type          | Description | Notes      |
| ----------------------- | ------------- | ----------- | ---------- |
| **export_target_langs** | **List[str]** |             | [optional] |
| **callback_url**        | **str**       |             | [optional] |

## Example

```python
from phrasetms_client.models.export_tm_dto import ExportTMDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExportTMDto from a JSON string
export_tm_dto_instance = ExportTMDto.from_json(json)
# print the JSON string representation of the object
print ExportTMDto.to_json()

# convert the object into a dict
export_tm_dto_dict = export_tm_dto_instance.to_dict()
# create an instance of ExportTMDto from a dict
export_tm_dto_from_dict = ExportTMDto.from_dict(export_tm_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
