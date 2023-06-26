# ExportByQueryDto

## Properties

| Name                    | Type                                | Description | Notes      |
| ----------------------- | ----------------------------------- | ----------- | ---------- |
| **export_target_langs** | **List[str]**                       |             |
| **queries**             | **List[str]**                       |             |
| **query_langs**         | **List[str]**                       |             |
| **created_at_min**      | **datetime**                        |             | [optional] |
| **created_at_max**      | **datetime**                        |             | [optional] |
| **modified_at_min**     | **datetime**                        |             | [optional] |
| **modified_at_max**     | **datetime**                        |             | [optional] |
| **created_by**          | [**IdReference**](IdReference.md)   |             | [optional] |
| **modified_by**         | [**IdReference**](IdReference.md)   |             | [optional] |
| **filename**            | **str**                             |             | [optional] |
| **project**             | [**UidReference**](UidReference.md) |             | [optional] |
| **callback_url**        | **str**                             |             | [optional] |

## Example

```python
from phrasetms_client.models.export_by_query_dto import ExportByQueryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExportByQueryDto from a JSON string
export_by_query_dto_instance = ExportByQueryDto.from_json(json)
# print the JSON string representation of the object
print ExportByQueryDto.to_json()

# convert the object into a dict
export_by_query_dto_dict = export_by_query_dto_instance.to_dict()
# create an instance of ExportByQueryDto from a dict
export_by_query_dto_from_dict = ExportByQueryDto.from_dict(export_by_query_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
