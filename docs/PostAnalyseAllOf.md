# PostAnalyseAllOf

## Properties

| Name                               | Type     | Description    | Notes      |
| ---------------------------------- | -------- | -------------- | ---------- |
| **trans_memory_post_editing**      | **bool** | Default: false | [optional] |
| **non_translatable_post_editing**  | **bool** | Default: false | [optional] |
| **machine_translate_post_editing** | **bool** | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.post_analyse_all_of import PostAnalyseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PostAnalyseAllOf from a JSON string
post_analyse_all_of_instance = PostAnalyseAllOf.from_json(json)
# print the JSON string representation of the object
print PostAnalyseAllOf.to_json()

# convert the object into a dict
post_analyse_all_of_dict = post_analyse_all_of_instance.to_dict()
# create an instance of PostAnalyseAllOf from a dict
post_analyse_all_of_from_dict = PostAnalyseAllOf.from_dict(post_analyse_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
