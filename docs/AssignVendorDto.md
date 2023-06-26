# AssignVendorDto

## Properties

| Name         | Type                              | Description | Notes      |
| ------------ | --------------------------------- | ----------- | ---------- |
| **vendor**   | [**IdReference**](IdReference.md) |             | [optional] |
| **date_due** | **datetime**                      |             | [optional] |

## Example

```python
from phrasetms_client.models.assign_vendor_dto import AssignVendorDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssignVendorDto from a JSON string
assign_vendor_dto_instance = AssignVendorDto.from_json(json)
# print the JSON string representation of the object
print AssignVendorDto.to_json()

# convert the object into a dict
assign_vendor_dto_dict = assign_vendor_dto_instance.to_dict()
# create an instance of AssignVendorDto from a dict
assign_vendor_dto_from_dict = AssignVendorDto.from_dict(assign_vendor_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
