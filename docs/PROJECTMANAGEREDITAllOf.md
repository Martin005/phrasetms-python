# PROJECTMANAGEREDITAllOf

## Properties

| Name                                      | Type                                      | Description                                                               | Notes      |
| ----------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------- | ---------- |
| **source_locales**                        | **List[str]**                             |                                                                           | [optional] |
| **target_locales**                        | **List[str]**                             |                                                                           | [optional] |
| **workflow_steps**                        | [**List[UidReference]**](UidReference.md) |                                                                           | [optional] |
| **clients**                               | [**List[UidReference]**](UidReference.md) |                                                                           | [optional] |
| **domains**                               | [**List[UidReference]**](UidReference.md) |                                                                           | [optional] |
| **sub_domains**                           | [**List[UidReference]**](UidReference.md) |                                                                           | [optional] |
| **project_create**                        | **bool**                                  | Enable project creation. Default: true                                    | [optional] |
| **project_view_other**                    | **bool**                                  | View projects created by other users. Default: true                       | [optional] |
| **project_edit_other**                    | **bool**                                  | Modify projects created by other users. Default: true                     | [optional] |
| **project_delete_other**                  | **bool**                                  | Delete projects created by other users. Default: true                     | [optional] |
| **project_clients**                       | [**List[UidReference]**](UidReference.md) | Access projects of a selected clients only                                | [optional] |
| **project_business_units**                | [**List[UidReference]**](UidReference.md) | Access projects of selected business units only                           | [optional] |
| **project_template_create**               | **bool**                                  | Enable project templates creation. Default: true                          | [optional] |
| **project_template_view_other**           | **bool**                                  | View project templates created by other users. Default: true              | [optional] |
| **project_template_edit_other**           | **bool**                                  | Modify project templates created by other users. Default: true            | [optional] |
| **project_template_delete_other**         | **bool**                                  | Delete project templates created by other users. Default: true            | [optional] |
| **project_template_clients**              | [**List[UidReference]**](UidReference.md) | Access project templates of a selected clients only                       | [optional] |
| **project_template_business_units**       | [**List[UidReference]**](UidReference.md) | Access project templates of selected business units only                  | [optional] |
| **trans_memory_create**                   | **bool**                                  | Enable TMs creation. Default: true                                        | [optional] |
| **trans_memory_view_other**               | **bool**                                  | View TMs created by other users. Default: true                            | [optional] |
| **trans_memory_edit_other**               | **bool**                                  | Modify TMs created by other users. Default: true                          | [optional] |
| **trans_memory_delete_other**             | **bool**                                  | Delete TMs created by other users. Default: true                          | [optional] |
| **trans_memory_export_other**             | **bool**                                  | Export TMs created by other users. Default: true                          | [optional] |
| **trans_memory_import_other**             | **bool**                                  | Import into TMs created by other users. Default: true                     | [optional] |
| **trans_memory_clients**                  | [**List[UidReference]**](UidReference.md) | Access TMs of a selected clients only                                     | [optional] |
| **trans_memory_business_units**           | [**List[UidReference]**](UidReference.md) | Access TMs of selected business units only                                | [optional] |
| **term_base_create**                      | **bool**                                  | Enable TBs creation. Default: true                                        | [optional] |
| **term_base_view_other**                  | **bool**                                  | View TBs created by other users. Default: true                            | [optional] |
| **term_base_edit_other**                  | **bool**                                  | Modify TBs created by other users. Default: true                          | [optional] |
| **term_base_delete_other**                | **bool**                                  | Delete TBs created by other users. Default: true                          | [optional] |
| **term_base_export_other**                | **bool**                                  | Export TBs created by other users. Default: true                          | [optional] |
| **term_base_import_other**                | **bool**                                  | Import into TBs created by other users. Default: true                     | [optional] |
| **term_base_approve_other**               | **bool**                                  | Approve terms in TBs created by other users. Default: true                | [optional] |
| **term_base_clients**                     | [**List[UidReference]**](UidReference.md) | Access TBs of a selected clients only                                     | [optional] |
| **term_base_business_units**              | [**List[UidReference]**](UidReference.md) | Access TBs of selected business units only                                | [optional] |
| **user_create**                           | **bool**                                  | Enable users creation. Default: true                                      | [optional] |
| **user_view_other**                       | **bool**                                  | View users created by other users. Default: true                          | [optional] |
| **user_edit_other**                       | **bool**                                  | Modify users created by other users. Default: true                        | [optional] |
| **user_delete_other**                     | **bool**                                  | Delete users created by other users. Default: true                        | [optional] |
| **client_domain_sub_domain_create**       | **bool**                                  | Enable clients, domains, subdomains creation. Default: true               | [optional] |
| **client_domain_sub_domain_view_other**   | **bool**                                  | View clients, domains, subdomains created by other users. Default: true   | [optional] |
| **client_domain_sub_domain_edit_other**   | **bool**                                  | Modify clients, domains, subdomains created by other users. Default: true | [optional] |
| **client_domain_sub_domain_delete_other** | **bool**                                  | Delete clients, domains, subdomains created by other users. Default: true | [optional] |
| **vendor_create**                         | **bool**                                  | Enable Vendors creation. Default: true                                    | [optional] |
| **vendor_view_other**                     | **bool**                                  | View Vendors created by other users. Default: true                        | [optional] |
| **vendor_edit_other**                     | **bool**                                  | Modify Vendors created by other users. Default: true                      | [optional] |
| **vendor_delete_other**                   | **bool**                                  | Delete Vendors created by other users. Default: true                      | [optional] |
| **dashboard_setting**                     | **str**                                   | Home page dashboards. Default: OWN_DATA                                   | [optional] |
| **setup_server**                          | **bool**                                  | Modify setup&#39;s server settings. Default: true                         | [optional] |

## Example

```python
from phrasetms_client.models.projectmanageredit_all_of import PROJECTMANAGEREDITAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PROJECTMANAGEREDITAllOf from a JSON string
projectmanageredit_all_of_instance = PROJECTMANAGEREDITAllOf.from_json(json)
# print the JSON string representation of the object
print PROJECTMANAGEREDITAllOf.to_json()

# convert the object into a dict
projectmanageredit_all_of_dict = projectmanageredit_all_of_instance.to_dict()
# create an instance of PROJECTMANAGEREDITAllOf from a dict
projectmanageredit_all_of_from_dict = PROJECTMANAGEREDITAllOf.from_dict(projectmanageredit_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
