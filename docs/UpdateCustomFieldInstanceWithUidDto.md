# UpdateCustomFieldInstanceWithUidDto

## Properties

| Name                      | Type                                      | Description | Notes      |
| ------------------------- | ----------------------------------------- | ----------- | ---------- |
| **custom_field_instance** | [**UidReference**](UidReference.md)       |             | [optional] |
| **custom_field**          | [**UidReference**](UidReference.md)       |             | [optional] |
| **selected_options**      | [**List[UidReference]**](UidReference.md) |             | [optional] |
| **value**                 | **str**                                   |             | [optional] |

## Example

```python
from phrasetms_client.models.update_custom_field_instance_with_uid_dto import UpdateCustomFieldInstanceWithUidDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFieldInstanceWithUidDto from a JSON string
update_custom_field_instance_with_uid_dto_instance = UpdateCustomFieldInstanceWithUidDto.from_json(json)
# print the JSON string representation of the object
print UpdateCustomFieldInstanceWithUidDto.to_json()

# convert the object into a dict
update_custom_field_instance_with_uid_dto_dict = update_custom_field_instance_with_uid_dto_instance.to_dict()
# create an instance of UpdateCustomFieldInstanceWithUidDto from a dict
update_custom_field_instance_with_uid_dto_from_dict = UpdateCustomFieldInstanceWithUidDto.from_dict(update_custom_field_instance_with_uid_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
