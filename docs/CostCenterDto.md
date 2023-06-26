# CostCenterDto

## Properties

| Name           | Type                                  | Description | Notes      |
| -------------- | ------------------------------------- | ----------- | ---------- |
| **id**         | **str**                               |             | [optional] |
| **uid**        | **str**                               |             | [optional] |
| **name**       | **str**                               |             | [optional] |
| **created_by** | [**UserReference**](UserReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.cost_center_dto import CostCenterDto

# TODO update the JSON string below
json = "{}"
# create an instance of CostCenterDto from a JSON string
cost_center_dto_instance = CostCenterDto.from_json(json)
# print the JSON string representation of the object
print CostCenterDto.to_json()

# convert the object into a dict
cost_center_dto_dict = cost_center_dto_instance.to_dict()
# create an instance of CostCenterDto from a dict
cost_center_dto_from_dict = CostCenterDto.from_dict(cost_center_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
