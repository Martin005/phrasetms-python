# CostCenterReference

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **name** | **str** |             | [optional] |
| **id**   | **str** |             | [optional] |
| **uid**  | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.cost_center_reference import CostCenterReference

# TODO update the JSON string below
json = "{}"
# create an instance of CostCenterReference from a JSON string
cost_center_reference_instance = CostCenterReference.from_json(json)
# print the JSON string representation of the object
print CostCenterReference.to_json()

# convert the object into a dict
cost_center_reference_dict = cost_center_reference_instance.to_dict()
# create an instance of CostCenterReference from a dict
cost_center_reference_from_dict = CostCenterReference.from_dict(cost_center_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
