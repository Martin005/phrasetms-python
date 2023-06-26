# EditAnalyseV2Dto

## Properties

| Name                | Type                                          | Description | Notes      |
| ------------------- | --------------------------------------------- | ----------- | ---------- |
| **name**            | **str**                                       |             | [optional] |
| **provider**        | [**ProviderReference**](ProviderReference.md) |             | [optional] |
| **net_rate_scheme** | [**UidReference**](UidReference.md)           |             | [optional] |

## Example

```python
from phrasetms_client.models.edit_analyse_v2_dto import EditAnalyseV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of EditAnalyseV2Dto from a JSON string
edit_analyse_v2_dto_instance = EditAnalyseV2Dto.from_json(json)
# print the JSON string representation of the object
print EditAnalyseV2Dto.to_json()

# convert the object into a dict
edit_analyse_v2_dto_dict = edit_analyse_v2_dto_instance.to_dict()
# create an instance of EditAnalyseV2Dto from a dict
edit_analyse_v2_dto_from_dict = EditAnalyseV2Dto.from_dict(edit_analyse_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
