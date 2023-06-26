# SchemaExtension

## Properties

| Name           | Type     | Description | Notes      |
| -------------- | -------- | ----------- | ---------- |
| **var_schema** | **str**  |             | [optional] |
| **required**   | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.schema_extension import SchemaExtension

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaExtension from a JSON string
schema_extension_instance = SchemaExtension.from_json(json)
# print the JSON string representation of the object
print SchemaExtension.to_json()

# convert the object into a dict
schema_extension_dict = schema_extension_instance.to_dict()
# create an instance of SchemaExtension from a dict
schema_extension_from_dict = SchemaExtension.from_dict(schema_extension_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
