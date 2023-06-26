# UpdateCustomFieldInstancesDto

## Properties

| Name                 | Type                                                                                    | Description | Notes      |
| -------------------- | --------------------------------------------------------------------------------------- | ----------- | ---------- |
| **add_instances**    | [**List[CreateCustomFieldInstanceDto]**](CreateCustomFieldInstanceDto.md)               |             | [optional] |
| **remove_instances** | [**List[UidReference]**](UidReference.md)                                               |             | [optional] |
| **update_instances** | [**List[UpdateCustomFieldInstanceWithUidDto]**](UpdateCustomFieldInstanceWithUidDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.update_custom_field_instances_dto import UpdateCustomFieldInstancesDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFieldInstancesDto from a JSON string
update_custom_field_instances_dto_instance = UpdateCustomFieldInstancesDto.from_json(json)
# print the JSON string representation of the object
print UpdateCustomFieldInstancesDto.to_json()

# convert the object into a dict
update_custom_field_instances_dto_dict = update_custom_field_instances_dto_instance.to_dict()
# create an instance of UpdateCustomFieldInstancesDto from a dict
update_custom_field_instances_dto_from_dict = UpdateCustomFieldInstancesDto.from_dict(update_custom_field_instances_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
