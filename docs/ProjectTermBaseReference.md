# ProjectTermBaseReference

## Properties

| Name              | Type       | Description | Notes      |
| ----------------- | ---------- | ----------- | ---------- |
| **id**            | **str**    |             | [optional] |
| **term_base**     | **object** |             | [optional] |
| **name**          | **str**    |             | [optional] |
| **write_mode**    | **bool**   |             | [optional] |
| **target_lang**   | **str**    |             | [optional] |
| **read_mode**     | **bool**   |             | [optional] |
| **workflow_step** | **object** |             | [optional] |

## Example

```python
from phrasetms_client.models.project_term_base_reference import ProjectTermBaseReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTermBaseReference from a JSON string
project_term_base_reference_instance = ProjectTermBaseReference.from_json(json)
# print the JSON string representation of the object
print ProjectTermBaseReference.to_json()

# convert the object into a dict
project_term_base_reference_dict = project_term_base_reference_instance.to_dict()
# create an instance of ProjectTermBaseReference from a dict
project_term_base_reference_from_dict = ProjectTermBaseReference.from_dict(project_term_base_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
