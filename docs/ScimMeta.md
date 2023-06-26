# ScimMeta

## Properties

| Name         | Type         | Description | Notes      |
| ------------ | ------------ | ----------- | ---------- |
| **created**  | **datetime** |             | [optional] |
| **location** | **str**      |             | [optional] |

## Example

```python
from phrasetms_client.models.scim_meta import ScimMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ScimMeta from a JSON string
scim_meta_instance = ScimMeta.from_json(json)
# print the JSON string representation of the object
print ScimMeta.to_json()

# convert the object into a dict
scim_meta_dict = scim_meta_instance.to_dict()
# create an instance of ScimMeta from a dict
scim_meta_from_dict = ScimMeta.from_dict(scim_meta_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
