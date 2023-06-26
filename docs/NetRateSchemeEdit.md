# NetRateSchemeEdit

## Properties

| Name      | Type                                              | Description | Notes      |
| --------- | ------------------------------------------------- | ----------- | ---------- |
| **name**  | **str**                                           |             |
| **rates** | [**DiscountSettingsDto**](DiscountSettingsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.net_rate_scheme_edit import NetRateSchemeEdit

# TODO update the JSON string below
json = "{}"
# create an instance of NetRateSchemeEdit from a JSON string
net_rate_scheme_edit_instance = NetRateSchemeEdit.from_json(json)
# print the JSON string representation of the object
print NetRateSchemeEdit.to_json()

# convert the object into a dict
net_rate_scheme_edit_dict = net_rate_scheme_edit_instance.to_dict()
# create an instance of NetRateSchemeEdit from a dict
net_rate_scheme_edit_from_dict = NetRateSchemeEdit.from_dict(net_rate_scheme_edit_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
