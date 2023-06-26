# GUESTEDITAllOf

## Properties

| Name                            | Type                                | Description                                                | Notes      |
| ------------------------------- | ----------------------------------- | ---------------------------------------------------------- | ---------- |
| **client**                      | [**UidReference**](UidReference.md) |                                                            |
| **enable_mt**                   | **bool**                            | Enable MT. Default: true                                   | [optional] |
| **project_view_other**          | **bool**                            | View projects created by other users. Default: true        | [optional] |
| **project_view_other_linguist** | **bool**                            | Show provider names. Default: true                         | [optional] |
| **project_view_other_editor**   | **bool**                            | Edit jobs in Memsource Editor. Default: true               | [optional] |
| **trans_memory_view_other**     | **bool**                            | View TMs created by other users. Default: true             | [optional] |
| **trans_memory_edit_other**     | **bool**                            | Modify TMs created by other users. Default: true           | [optional] |
| **trans_memory_export_other**   | **bool**                            | Export TMs created by other users. Default: true           | [optional] |
| **trans_memory_import_other**   | **bool**                            | Import into TMs created by other users. Default: true      | [optional] |
| **term_base_view_other**        | **bool**                            | View TBs created by other users. Default: true             | [optional] |
| **term_base_edit_other**        | **bool**                            | Modify TBs created by other users. Default: true           | [optional] |
| **term_base_export_other**      | **bool**                            | Export TBs created by other users. Default: true           | [optional] |
| **term_base_import_other**      | **bool**                            | Import into TBs created by other users. Default: true      | [optional] |
| **term_base_approve_other**     | **bool**                            | Approve terms in TBs created by other users. Default: true | [optional] |

## Example

```python
from phrasetms_client.models.guestedit_all_of import GUESTEDITAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GUESTEDITAllOf from a JSON string
guestedit_all_of_instance = GUESTEDITAllOf.from_json(json)
# print the JSON string representation of the object
print GUESTEDITAllOf.to_json()

# convert the object into a dict
guestedit_all_of_dict = guestedit_all_of_instance.to_dict()
# create an instance of GUESTEDITAllOf from a dict
guestedit_all_of_from_dict = GUESTEDITAllOf.from_dict(guestedit_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
