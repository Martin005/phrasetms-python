# VENDORAllOf

## Properties

| Name                         | Type    | Description | Notes                 |
| ---------------------------- | ------- | ----------- | --------------------- | ---------- |
| **name**                     | **str** |             | [optional] [readonly] |
| **default_project_owner_id** |         | **int**     |                       | [optional] |

## Example

```python
from phrasetms_client.models.vendor__all_of import VENDORAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of VENDORAllOf from a JSON string
vendor_all_of_instance = VENDORAllOf.from_json(json)
# print the JSON string representation of the object
print VENDORAllOf.to_json()

# convert the object into a dict
vendor_all_of_dict = vendor_all_of_instance.to_dict()
# create an instance of VENDORAllOf from a dict
vendor_all_of_from_dict = VENDORAllOf.from_dict(vendor_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
