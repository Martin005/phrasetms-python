# ScimResourceSchema

## Properties

| Name            | Type                                | Description | Notes      |
| --------------- | ----------------------------------- | ----------- | ---------- |
| **id**          | **str**                             |             | [optional] |
| **name**        | **str**                             |             | [optional] |
| **description** | **str**                             |             | [optional] |
| **attributes**  | [**List[Attribute]**](Attribute.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.scim_resource_schema import ScimResourceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ScimResourceSchema from a JSON string
scim_resource_schema_instance = ScimResourceSchema.from_json(json)
# print the JSON string representation of the object
print ScimResourceSchema.to_json()

# convert the object into a dict
scim_resource_schema_dict = scim_resource_schema_instance.to_dict()
# create an instance of ScimResourceSchema from a dict
scim_resource_schema_from_dict = ScimResourceSchema.from_dict(scim_resource_schema_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
