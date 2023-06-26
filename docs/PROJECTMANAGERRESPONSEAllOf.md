# PROJECTMANAGERRESPONSEAllOf

## Properties

| Name                                      | Type                                                            | Description | Notes      |
| ----------------------------------------- | --------------------------------------------------------------- | ----------- | ---------- |
| **source_locales**                        | **List[str]**                                                   |             | [optional] |
| **target_locales**                        | **List[str]**                                                   |             | [optional] |
| **workflow_steps**                        | [**List[WorkflowStepReferenceV3]**](WorkflowStepReferenceV3.md) |             | [optional] |
| **clients**                               | [**List[ClientReference]**](ClientReference.md)                 |             | [optional] |
| **domains**                               | [**List[DomainReference]**](DomainReference.md)                 |             | [optional] |
| **sub_domains**                           | [**List[SubDomainReference]**](SubDomainReference.md)           |             | [optional] |
| **project_create**                        | **bool**                                                        |             | [optional] |
| **project_view_other**                    | **bool**                                                        |             | [optional] |
| **project_edit_other**                    | **bool**                                                        |             | [optional] |
| **project_delete_other**                  | **bool**                                                        |             | [optional] |
| **project_clients**                       | [**List[ClientReference]**](ClientReference.md)                 |             | [optional] |
| **project_business_units**                | [**List[BusinessUnitReference]**](BusinessUnitReference.md)     |             | [optional] |
| **project_template_create**               | **bool**                                                        |             | [optional] |
| **project_template_view_other**           | **bool**                                                        |             | [optional] |
| **project_template_edit_other**           | **bool**                                                        |             | [optional] |
| **project_template_delete_other**         | **bool**                                                        |             | [optional] |
| **project_template_clients**              | [**List[ClientReference]**](ClientReference.md)                 |             | [optional] |
| **project_template_business_units**       | [**List[BusinessUnitReference]**](BusinessUnitReference.md)     |             | [optional] |
| **trans_memory_create**                   | **bool**                                                        |             | [optional] |
| **trans_memory_view_other**               | **bool**                                                        |             | [optional] |
| **trans_memory_edit_other**               | **bool**                                                        |             | [optional] |
| **trans_memory_delete_other**             | **bool**                                                        |             | [optional] |
| **trans_memory_export_other**             | **bool**                                                        |             | [optional] |
| **trans_memory_import_other**             | **bool**                                                        |             | [optional] |
| **trans_memory_clients**                  | [**List[ClientReference]**](ClientReference.md)                 |             | [optional] |
| **trans_memory_business_units**           | [**List[BusinessUnitReference]**](BusinessUnitReference.md)     |             | [optional] |
| **term_base_create**                      | **bool**                                                        |             | [optional] |
| **term_base_view_other**                  | **bool**                                                        |             | [optional] |
| **term_base_edit_other**                  | **bool**                                                        |             | [optional] |
| **term_base_delete_other**                | **bool**                                                        |             | [optional] |
| **term_base_export_other**                | **bool**                                                        |             | [optional] |
| **term_base_import_other**                | **bool**                                                        |             | [optional] |
| **term_base_approve_other**               | **bool**                                                        |             | [optional] |
| **term_base_clients**                     | [**List[ClientReference]**](ClientReference.md)                 |             | [optional] |
| **term_base_business_units**              | [**List[BusinessUnitReference]**](BusinessUnitReference.md)     |             | [optional] |
| **user_create**                           | **bool**                                                        |             | [optional] |
| **user_view_other**                       | **bool**                                                        |             | [optional] |
| **user_edit_other**                       | **bool**                                                        |             | [optional] |
| **user_delete_other**                     | **bool**                                                        |             | [optional] |
| **client_domain_sub_domain_create**       | **bool**                                                        |             | [optional] |
| **client_domain_sub_domain_view_other**   | **bool**                                                        |             | [optional] |
| **client_domain_sub_domain_edit_other**   | **bool**                                                        |             | [optional] |
| **client_domain_sub_domain_delete_other** | **bool**                                                        |             | [optional] |
| **vendor_create**                         | **bool**                                                        |             | [optional] |
| **vendor_view_other**                     | **bool**                                                        |             | [optional] |
| **vendor_edit_other**                     | **bool**                                                        |             | [optional] |
| **vendor_delete_other**                   | **bool**                                                        |             | [optional] |
| **dashboard_setting**                     | **str**                                                         |             | [optional] |
| **setup_server**                          | **bool**                                                        |             | [optional] |

## Example

```python
from phrasetms_client.models.projectmanagerresponse_all_of import PROJECTMANAGERRESPONSEAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PROJECTMANAGERRESPONSEAllOf from a JSON string
projectmanagerresponse_all_of_instance = PROJECTMANAGERRESPONSEAllOf.from_json(json)
# print the JSON string representation of the object
print PROJECTMANAGERRESPONSEAllOf.to_json()

# convert the object into a dict
projectmanagerresponse_all_of_dict = projectmanagerresponse_all_of_instance.to_dict()
# create an instance of PROJECTMANAGERRESPONSEAllOf from a dict
projectmanagerresponse_all_of_from_dict = PROJECTMANAGERRESPONSEAllOf.from_dict(projectmanagerresponse_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
