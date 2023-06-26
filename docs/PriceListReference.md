# PriceListReference

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **id**   | **str** |             | [optional] |
| **name** | **str** |             | [optional] |
| **uid**  | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.price_list_reference import PriceListReference

# TODO update the JSON string below
json = "{}"
# create an instance of PriceListReference from a JSON string
price_list_reference_instance = PriceListReference.from_json(json)
# print the JSON string representation of the object
print PriceListReference.to_json()

# convert the object into a dict
price_list_reference_dict = price_list_reference_instance.to_dict()
# create an instance of PriceListReference from a dict
price_list_reference_from_dict = PriceListReference.from_dict(price_list_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
