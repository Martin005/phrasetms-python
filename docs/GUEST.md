# GUEST

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
from phrasetms_client.models.guest import GUEST

# TODO update the JSON string below
json = "{}"
# create an instance of GUEST from a JSON string
guest_instance = GUEST.from_json(json)
# print the JSON string representation of the object
print GUEST.to_json()

# convert the object into a dict
guest_dict = guest_instance.to_dict()
# create an instance of GUEST from a dict
guest_from_dict = GUEST.from_dict(guest_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
