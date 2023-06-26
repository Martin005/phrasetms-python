# CustomFieldInstancesDto

## Properties

| Name                       | Type                                                          | Description | Notes      |
| -------------------------- | ------------------------------------------------------------- | ----------- | ---------- |
| **custom_field_instances** | [**List[CustomFieldInstanceDto]**](CustomFieldInstanceDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.custom_field_instances_dto import CustomFieldInstancesDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldInstancesDto from a JSON string
custom_field_instances_dto_instance = CustomFieldInstancesDto.from_json(json)
# print the JSON string representation of the object
print CustomFieldInstancesDto.to_json()

# convert the object into a dict
custom_field_instances_dto_dict = custom_field_instances_dto_instance.to_dict()
# create an instance of CustomFieldInstancesDto from a dict
custom_field_instances_dto_from_dict = CustomFieldInstancesDto.from_dict(custom_field_instances_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
