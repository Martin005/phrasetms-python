# UpdateCustomFieldInstanceDto

## Properties

| Name                 | Type                                      | Description | Notes      |
| -------------------- | ----------------------------------------- | ----------- | ---------- |
| **selected_options** | [**List[UidReference]**](UidReference.md) |             | [optional] |
| **value**            | **str**                                   |             | [optional] |

## Example

```python
from phrasetms_client.models.update_custom_field_instance_dto import UpdateCustomFieldInstanceDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFieldInstanceDto from a JSON string
update_custom_field_instance_dto_instance = UpdateCustomFieldInstanceDto.from_json(json)
# print the JSON string representation of the object
print UpdateCustomFieldInstanceDto.to_json()

# convert the object into a dict
update_custom_field_instance_dto_dict = update_custom_field_instance_dto_instance.to_dict()
# create an instance of UpdateCustomFieldInstanceDto from a dict
update_custom_field_instance_dto_from_dict = UpdateCustomFieldInstanceDto.from_dict(update_custom_field_instance_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
