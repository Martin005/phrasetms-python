# PostAnalyse

## Properties

| Name                               | Type     | Description    | Notes      |
| ---------------------------------- | -------- | -------------- | ---------- |
| **trans_memory_post_editing**      | **bool** | Default: false | [optional] |
| **non_translatable_post_editing**  | **bool** | Default: false | [optional] |
| **machine_translate_post_editing** | **bool** | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.post_analyse import PostAnalyse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAnalyse from a JSON string
post_analyse_instance = PostAnalyse.from_json(json)
# print the JSON string representation of the object
print PostAnalyse.to_json()

# convert the object into a dict
post_analyse_dict = post_analyse_instance.to_dict()
# create an instance of PostAnalyse from a dict
post_analyse_from_dict = PostAnalyse.from_dict(post_analyse_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
