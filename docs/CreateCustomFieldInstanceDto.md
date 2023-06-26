# CreateCustomFieldInstanceDto

## Properties

| Name                 | Type                                      | Description | Notes      |
| -------------------- | ----------------------------------------- | ----------- | ---------- |
| **custom_field**     | [**UidReference**](UidReference.md)       |             | [optional] |
| **selected_options** | [**List[UidReference]**](UidReference.md) |             | [optional] |
| **value**            | **str**                                   |             | [optional] |

## Example

```python
from phrasetms_client.models.create_custom_field_instance_dto import CreateCustomFieldInstanceDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomFieldInstanceDto from a JSON string
create_custom_field_instance_dto_instance = CreateCustomFieldInstanceDto.from_json(json)
# print the JSON string representation of the object
print CreateCustomFieldInstanceDto.to_json()

# convert the object into a dict
create_custom_field_instance_dto_dict = create_custom_field_instance_dto_instance.to_dict()
# create an instance of CreateCustomFieldInstanceDto from a dict
create_custom_field_instance_dto_from_dict = CreateCustomFieldInstanceDto.from_dict(create_custom_field_instance_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
