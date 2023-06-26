# ProjectTranslationMemoryReference

## Properties

| Name              | Type       | Description | Notes      |
| ----------------- | ---------- | ----------- | ---------- |
| **id**            | **str**    |             | [optional] |
| **trans_mem**     | **object** |             | [optional] |
| **name**          | **str**    |             | [optional] |
| **workflow_step** | **object** |             | [optional] |
| **target_lang**   | **str**    |             | [optional] |
| **penalty**       | **float**  |             | [optional] |
| **read_mode**     | **bool**   |             | [optional] |

## Example

```python
from phrasetms_client.models.project_translation_memory_reference import ProjectTranslationMemoryReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTranslationMemoryReference from a JSON string
project_translation_memory_reference_instance = ProjectTranslationMemoryReference.from_json(json)
# print the JSON string representation of the object
print ProjectTranslationMemoryReference.to_json()

# convert the object into a dict
project_translation_memory_reference_dict = project_translation_memory_reference_instance.to_dict()
# create an instance of ProjectTranslationMemoryReference from a dict
project_translation_memory_reference_from_dict = ProjectTranslationMemoryReference.from_dict(project_translation_memory_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
