# BulkDeleteAnalyseDto

## Properties

| Name         | Type                                    | Description    | Notes      |
| ------------ | --------------------------------------- | -------------- | ---------- |
| **analyses** | [**List[IdReference]**](IdReference.md) |                |
| **purge**    | **bool**                                | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.bulk_delete_analyse_dto import BulkDeleteAnalyseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteAnalyseDto from a JSON string
bulk_delete_analyse_dto_instance = BulkDeleteAnalyseDto.from_json(json)
# print the JSON string representation of the object
print BulkDeleteAnalyseDto.to_json()

# convert the object into a dict
bulk_delete_analyse_dto_dict = bulk_delete_analyse_dto_instance.to_dict()
# create an instance of BulkDeleteAnalyseDto from a dict
bulk_delete_analyse_dto_from_dict = BulkDeleteAnalyseDto.from_dict(bulk_delete_analyse_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
