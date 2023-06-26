# CreateVendorDto

## Properties

| Name                | Type                                      | Description | Notes      |
| ------------------- | ----------------------------------------- | ----------- | ---------- |
| **vendor_token**    | **str**                                   |             |
| **net_rate_scheme** | [**UidReference**](UidReference.md)       |             | [optional] |
| **price_list**      | [**UidReference**](UidReference.md)       |             | [optional] |
| **source_locales**  | **List[str]**                             |             | [optional] |
| **target_locales**  | **List[str]**                             |             | [optional] |
| **clients**         | [**List[UidReference]**](UidReference.md) |             | [optional] |
| **domains**         | [**List[UidReference]**](UidReference.md) |             | [optional] |
| **sub_domains**     | [**List[UidReference]**](UidReference.md) |             | [optional] |
| **workflow_steps**  | [**List[UidReference]**](UidReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.create_vendor_dto import CreateVendorDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVendorDto from a JSON string
create_vendor_dto_instance = CreateVendorDto.from_json(json)
# print the JSON string representation of the object
print CreateVendorDto.to_json()

# convert the object into a dict
create_vendor_dto_dict = create_vendor_dto_instance.to_dict()
# create an instance of CreateVendorDto from a dict
create_vendor_dto_from_dict = CreateVendorDto.from_dict(create_vendor_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
