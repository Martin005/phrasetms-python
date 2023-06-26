# LINGUISTEDITAllOf

## Properties

| Name                        | Type                                      | Description                             | Notes      |
| --------------------------- | ----------------------------------------- | --------------------------------------- | ---------- |
| **edit_all_terms_in_tb**    | **bool**                                  | Edit all terms in TB. Default: false    | [optional] |
| **edit_translations_in_tm** | **bool**                                  | Edit translations in TM. Default: false | [optional] |
| **enable_mt**               | **bool**                                  | Enable MT. Default: true                | [optional] |
| **may_reject_jobs**         | **bool**                                  | Reject jobs. Default: false             | [optional] |
| **source_locales**          | **List[str]**                             |                                         | [optional] |
| **target_locales**          | **List[str]**                             |                                         | [optional] |
| **workflow_steps**          | [**List[UidReference]**](UidReference.md) |                                         | [optional] |
| **clients**                 | [**List[UidReference]**](UidReference.md) |                                         | [optional] |
| **domains**                 | [**List[UidReference]**](UidReference.md) |                                         | [optional] |
| **sub_domains**             | [**List[UidReference]**](UidReference.md) |                                         | [optional] |
| **net_rate_scheme**         | [**UidReference**](UidReference.md)       |                                         | [optional] |
| **translation_price_list**  | [**UidReference**](UidReference.md)       |                                         | [optional] |

## Example

```python
from phrasetms_client.models.linguistedit_all_of import LINGUISTEDITAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of LINGUISTEDITAllOf from a JSON string
linguistedit_all_of_instance = LINGUISTEDITAllOf.from_json(json)
# print the JSON string representation of the object
print LINGUISTEDITAllOf.to_json()

# convert the object into a dict
linguistedit_all_of_dict = linguistedit_all_of_instance.to_dict()
# create an instance of LINGUISTEDITAllOf from a dict
linguistedit_all_of_from_dict = LINGUISTEDITAllOf.from_dict(linguistedit_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
