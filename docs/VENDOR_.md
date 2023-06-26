# VENDOR

## Properties

| Name                         | Type    | Description | Notes                 |
| ---------------------------- | ------- | ----------- | --------------------- | ---------- |
| **name**                     | **str** |             | [optional] [readonly] |
| **default_project_owner_id** |         | **int**     |                       | [optional] |

## Example

```python
from phrasetms_client.models.vendor_ import VENDOR

# TODO update the JSON string below
json = "{}"
# create an instance of VENDOR from a JSON string
vendor_instance = VENDOR.from_json(json)
# print the JSON string representation of the object
print VENDOR.to_json()

# convert the object into a dict
vendor_dict = vendor_instance.to_dict()
# create an instance of VENDOR from a dict
vendor_from_dict = VENDOR.from_dict(vendor_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
