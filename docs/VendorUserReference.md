# VendorUserReference

## Properties

| Name             | Type                                                  | Description | Notes      |
| ---------------- | ----------------------------------------------------- | ----------- | ---------- |
| **uid**          | **str**                                               |             | [optional] |
| **vendor_uid**   | **str**                                               |             | [optional] |
| **username**     | **str**                                               |             | [optional] |
| **first_name**   | **str**                                               |             | [optional] |
| **last_name**    | **str**                                               |             | [optional] |
| **organization** | [**OrganizationReference**](OrganizationReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.vendor_user_reference import VendorUserReference

# TODO update the JSON string below
json = "{}"
# create an instance of VendorUserReference from a JSON string
vendor_user_reference_instance = VendorUserReference.from_json(json)
# print the JSON string representation of the object
print VendorUserReference.to_json()

# convert the object into a dict
vendor_user_reference_dict = vendor_user_reference_instance.to_dict()
# create an instance of VendorUserReference from a dict
vendor_user_reference_from_dict = VendorUserReference.from_dict(vendor_user_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
