# DiscountSchemeReference

## Properties

| Name             | Type                                  | Description | Notes      |
| ---------------- | ------------------------------------- | ----------- | ---------- |
| **id**           | **str**                               |             | [optional] |
| **uid**          | **str**                               |             | [optional] |
| **name**         | **str**                               |             | [optional] |
| **date_created** | **datetime**                          |             | [optional] |
| **created_by**   | [**UserReference**](UserReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.discount_scheme_reference import DiscountSchemeReference

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountSchemeReference from a JSON string
discount_scheme_reference_instance = DiscountSchemeReference.from_json(json)
# print the JSON string representation of the object
print DiscountSchemeReference.to_json()

# convert the object into a dict
discount_scheme_reference_dict = discount_scheme_reference_instance.to_dict()
# create an instance of DiscountSchemeReference from a dict
discount_scheme_reference_from_dict = DiscountSchemeReference.from_dict(discount_scheme_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
