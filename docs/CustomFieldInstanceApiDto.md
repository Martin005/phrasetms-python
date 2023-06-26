# CustomFieldInstanceApiDto

## Properties

| Name                 | Type                                      | Description | Notes      |
| -------------------- | ----------------------------------------- | ----------- | ---------- |
| **custom_field**     | [**UidReference**](UidReference.md)       |             | [optional] |
| **selected_options** | [**List[UidReference]**](UidReference.md) |             | [optional] |
| **value**            | **str**                                   |             | [optional] |

## Example

```python
from phrasetms_client.models.custom_field_instance_api_dto import CustomFieldInstanceApiDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldInstanceApiDto from a JSON string
custom_field_instance_api_dto_instance = CustomFieldInstanceApiDto.from_json(json)
# print the JSON string representation of the object
print CustomFieldInstanceApiDto.to_json()

# convert the object into a dict
custom_field_instance_api_dto_dict = custom_field_instance_api_dto_instance.to_dict()
# create an instance of CustomFieldInstanceApiDto from a dict
custom_field_instance_api_dto_from_dict = CustomFieldInstanceApiDto.from_dict(custom_field_instance_api_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
