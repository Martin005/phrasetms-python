# BulkEditAnalyseV2Dto

## Properties

| Name                | Type                                          | Description | Notes      |
| ------------------- | --------------------------------------------- | ----------- | ---------- |
| **analyses**        | [**List[IdReference]**](IdReference.md)       |             |
| **name**            | **str**                                       |             | [optional] |
| **provider**        | [**ProviderReference**](ProviderReference.md) |             | [optional] |
| **net_rate_scheme** | [**UidReference**](UidReference.md)           |             | [optional] |

## Example

```python
from phrasetms_client.models.bulk_edit_analyse_v2_dto import BulkEditAnalyseV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkEditAnalyseV2Dto from a JSON string
bulk_edit_analyse_v2_dto_instance = BulkEditAnalyseV2Dto.from_json(json)
# print the JSON string representation of the object
print BulkEditAnalyseV2Dto.to_json()

# convert the object into a dict
bulk_edit_analyse_v2_dto_dict = bulk_edit_analyse_v2_dto_instance.to_dict()
# create an instance of BulkEditAnalyseV2Dto from a dict
bulk_edit_analyse_v2_dto_from_dict = BulkEditAnalyseV2Dto.from_dict(bulk_edit_analyse_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
