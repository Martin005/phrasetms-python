# ScimResourceTypeSchema

## Properties

| Name                  | Type                                            | Description | Notes      |
| --------------------- | ----------------------------------------------- | ----------- | ---------- |
| **schemas**           | **List[str]**                                   |             | [optional] |
| **id**                | **str**                                         |             | [optional] |
| **name**              | **str**                                         |             | [optional] |
| **endpoint**          | **str**                                         |             | [optional] |
| **description**       | **str**                                         |             | [optional] |
| **var_schema**        | **str**                                         |             | [optional] |
| **schema_extensions** | [**List[SchemaExtension]**](SchemaExtension.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.scim_resource_type_schema import ScimResourceTypeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ScimResourceTypeSchema from a JSON string
scim_resource_type_schema_instance = ScimResourceTypeSchema.from_json(json)
# print the JSON string representation of the object
print ScimResourceTypeSchema.to_json()

# convert the object into a dict
scim_resource_type_schema_dict = scim_resource_type_schema_instance.to_dict()
# create an instance of ScimResourceTypeSchema from a dict
scim_resource_type_schema_from_dict = ScimResourceTypeSchema.from_dict(scim_resource_type_schema_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
