# VendorSecuritySettingsDto

## Properties

| Name                                       | Type                                      | Description                | Notes      |
| ------------------------------------------ | ----------------------------------------- | -------------------------- | ---------- |
| **can_change_shared_job_due_date_enabled** | **bool**                                  | Default: &#x60;false&#x60; | [optional] |
| **can_change_shared_job_due_date**         | [**List[UidReference]**](UidReference.md) |                            | [optional] |
| **job_vendors_may_upload_references**      | **bool**                                  | Default: &#x60;false&#x60; | [optional] |

## Example

```python
from phrasetms_client.models.vendor_security_settings_dto import VendorSecuritySettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of VendorSecuritySettingsDto from a JSON string
vendor_security_settings_dto_instance = VendorSecuritySettingsDto.from_json(json)
# print the JSON string representation of the object
print VendorSecuritySettingsDto.to_json()

# convert the object into a dict
vendor_security_settings_dto_dict = vendor_security_settings_dto_instance.to_dict()
# create an instance of VendorSecuritySettingsDto from a dict
vendor_security_settings_dto_from_dict = VendorSecuritySettingsDto.from_dict(vendor_security_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
