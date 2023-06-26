# BuyerReference

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **id**   | **str** |             | [optional] |
| **uid**  | **str** |             | [optional] |
| **name** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.buyer_reference import BuyerReference

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerReference from a JSON string
buyer_reference_instance = BuyerReference.from_json(json)
# print the JSON string representation of the object
print BuyerReference.to_json()

# convert the object into a dict
buyer_reference_dict = buyer_reference_instance.to_dict()
# create an instance of BuyerReference from a dict
buyer_reference_from_dict = BuyerReference.from_dict(buyer_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
