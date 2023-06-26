# GUESTRESPONSEAllOf

## Properties

| Name                            | Type                                      | Description | Notes      |
| ------------------------------- | ----------------------------------------- | ----------- | ---------- |
| **client**                      | [**ClientReference**](ClientReference.md) |             |
| **enable_mt**                   | **bool**                                  |             | [optional] |
| **project_view_other**          | **bool**                                  |             | [optional] |
| **project_view_other_linguist** | **bool**                                  |             | [optional] |
| **project_view_other_editor**   | **bool**                                  |             | [optional] |
| **trans_memory_view_other**     | **bool**                                  |             | [optional] |
| **trans_memory_edit_other**     | **bool**                                  |             | [optional] |
| **trans_memory_export_other**   | **bool**                                  |             | [optional] |
| **trans_memory_import_other**   | **bool**                                  |             | [optional] |
| **term_base_view_other**        | **bool**                                  |             | [optional] |
| **term_base_edit_other**        | **bool**                                  |             | [optional] |
| **term_base_export_other**      | **bool**                                  |             | [optional] |
| **term_base_import_other**      | **bool**                                  |             | [optional] |
| **term_base_approve_other**     | **bool**                                  |             | [optional] |

## Example

```python
from phrasetms_client.models.guestresponse_all_of import GUESTRESPONSEAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GUESTRESPONSEAllOf from a JSON string
guestresponse_all_of_instance = GUESTRESPONSEAllOf.from_json(json)
# print the JSON string representation of the object
print GUESTRESPONSEAllOf.to_json()

# convert the object into a dict
guestresponse_all_of_dict = guestresponse_all_of_instance.to_dict()
# create an instance of GUESTRESPONSEAllOf from a dict
guestresponse_all_of_from_dict = GUESTRESPONSEAllOf.from_dict(guestresponse_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
