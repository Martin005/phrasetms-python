# CreateCustomFieldDto

## Properties

| Name                 | Type          | Description | Notes      |
| -------------------- | ------------- | ----------- | ---------- |
| **name**             | **str**       |             |
| **allowed_entities** | **List[str]** |             |
| **options**          | **List[str]** |             | [optional] |
| **type**             | **str**       |             | [optional] |
| **required**         | **bool**      |             | [optional] |
| **description**      | **str**       |             | [optional] |

## Example

```python
from phrasetms_client.models.create_custom_field_dto import CreateCustomFieldDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomFieldDto from a JSON string
create_custom_field_dto_instance = CreateCustomFieldDto.from_json(json)
# print the JSON string representation of the object
print CreateCustomFieldDto.to_json()

# convert the object into a dict
create_custom_field_dto_dict = create_custom_field_dto_instance.to_dict()
# create an instance of CreateCustomFieldDto from a dict
create_custom_field_dto_from_dict = CreateCustomFieldDto.from_dict(create_custom_field_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
