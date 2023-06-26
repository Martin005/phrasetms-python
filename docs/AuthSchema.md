# AuthSchema

## Properties

| Name            | Type     | Description | Notes      |
| --------------- | -------- | ----------- | ---------- |
| **type**        | **str**  |             | [optional] |
| **name**        | **str**  |             | [optional] |
| **description** | **str**  |             | [optional] |
| **spec_url**    | **str**  |             | [optional] |
| **primary**     | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.auth_schema import AuthSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSchema from a JSON string
auth_schema_instance = AuthSchema.from_json(json)
# print the JSON string representation of the object
print AuthSchema.to_json()

# convert the object into a dict
auth_schema_dict = auth_schema_instance.to_dict()
# create an instance of AuthSchema from a dict
auth_schema_from_dict = AuthSchema.from_dict(auth_schema_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
