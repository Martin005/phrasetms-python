# CreateCustomFieldInstancesDto

## Properties

| Name                       | Type                                                                      | Description | Notes      |
| -------------------------- | ------------------------------------------------------------------------- | ----------- | ---------- |
| **custom_field_instances** | [**List[CreateCustomFieldInstanceDto]**](CreateCustomFieldInstanceDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.create_custom_field_instances_dto import CreateCustomFieldInstancesDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomFieldInstancesDto from a JSON string
create_custom_field_instances_dto_instance = CreateCustomFieldInstancesDto.from_json(json)
# print the JSON string representation of the object
print CreateCustomFieldInstancesDto.to_json()

# convert the object into a dict
create_custom_field_instances_dto_dict = create_custom_field_instances_dto_instance.to_dict()
# create an instance of CreateCustomFieldInstancesDto from a dict
create_custom_field_instances_dto_from_dict = CreateCustomFieldInstancesDto.from_dict(create_custom_field_instances_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
