# CustomFieldDto

## Properties

| Name                 | Type                                                                    | Description | Notes      |
| -------------------- | ----------------------------------------------------------------------- | ----------- | ---------- |
| **uid**              | **str**                                                                 |             | [optional] |
| **name**             | **str**                                                                 |             | [optional] |
| **type**             | **str**                                                                 |             | [optional] |
| **allowed_entities** | **List[str]**                                                           |             | [optional] |
| **options**          | [**CustomFieldOptionsTruncatedDto**](CustomFieldOptionsTruncatedDto.md) |             | [optional] |
| **created_at**       | **datetime**                                                            |             | [optional] |
| **created_by**       | [**UserReference**](UserReference.md)                                   |             | [optional] |
| **last_modified**    | **datetime**                                                            |             | [optional] |
| **last_modified_by** | [**UserReference**](UserReference.md)                                   |             | [optional] |
| **required_from**    | **datetime**                                                            |             | [optional] |
| **required**         | **bool**                                                                |             | [optional] |
| **description**      | **str**                                                                 |             | [optional] |

## Example

```python
from phrasetms_client.models.custom_field_dto import CustomFieldDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDto from a JSON string
custom_field_dto_instance = CustomFieldDto.from_json(json)
# print the JSON string representation of the object
print CustomFieldDto.to_json()

# convert the object into a dict
custom_field_dto_dict = custom_field_dto_instance.to_dict()
# create an instance of CustomFieldDto from a dict
custom_field_dto_from_dict = CustomFieldDto.from_dict(custom_field_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
