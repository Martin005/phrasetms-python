# CostCenterEditDto

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.cost_center_edit_dto import CostCenterEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of CostCenterEditDto from a JSON string
cost_center_edit_dto_instance = CostCenterEditDto.from_json(json)
# print the JSON string representation of the object
print CostCenterEditDto.to_json()

# convert the object into a dict
cost_center_edit_dto_dict = cost_center_edit_dto_instance.to_dict()
# create an instance of CostCenterEditDto from a dict
cost_center_edit_dto_from_dict = CostCenterEditDto.from_dict(cost_center_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
