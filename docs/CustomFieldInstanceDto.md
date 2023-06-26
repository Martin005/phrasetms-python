# CustomFieldInstanceDto

## Properties

| Name                 | Type                                                      | Description | Notes      |
| -------------------- | --------------------------------------------------------- | ----------- | ---------- |
| **uid**              | **str**                                                   |             | [optional] |
| **custom_field**     | [**CustomFieldDto**](CustomFieldDto.md)                   |             | [optional] |
| **selected_options** | [**List[CustomFieldOptionDto]**](CustomFieldOptionDto.md) |             | [optional] |
| **value**            | **str**                                                   |             | [optional] |
| **created_at**       | **datetime**                                              |             | [optional] |
| **created_by**       | [**UidReference**](UidReference.md)                       |             | [optional] |
| **updated_at**       | **datetime**                                              |             | [optional] |
| **updated_by**       | [**UidReference**](UidReference.md)                       |             | [optional] |

## Example

```python
from phrasetms_client.models.custom_field_instance_dto import CustomFieldInstanceDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldInstanceDto from a JSON string
custom_field_instance_dto_instance = CustomFieldInstanceDto.from_json(json)
# print the JSON string representation of the object
print CustomFieldInstanceDto.to_json()

# convert the object into a dict
custom_field_instance_dto_dict = custom_field_instance_dto_instance.to_dict()
# create an instance of CustomFieldInstanceDto from a dict
custom_field_instance_dto_from_dict = CustomFieldInstanceDto.from_dict(custom_field_instance_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
