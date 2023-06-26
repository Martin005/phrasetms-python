# NetRateSchemeReference

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
from phrasetms_client.models.net_rate_scheme_reference import NetRateSchemeReference

# TODO update the JSON string below
json = "{}"
# create an instance of NetRateSchemeReference from a JSON string
net_rate_scheme_reference_instance = NetRateSchemeReference.from_json(json)
# print the JSON string representation of the object
print NetRateSchemeReference.to_json()

# convert the object into a dict
net_rate_scheme_reference_dict = net_rate_scheme_reference_instance.to_dict()
# create an instance of NetRateSchemeReference from a dict
net_rate_scheme_reference_from_dict = NetRateSchemeReference.from_dict(net_rate_scheme_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
