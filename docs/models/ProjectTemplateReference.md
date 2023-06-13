# phrasetms_client.model.project_template_reference.ProjectTemplateReference

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                             | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                        | Notes      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **templateName**                | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **sourceLang**                  | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **[targetLangs](#targetLangs)** | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                    | [optional] |
| **id**                          | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **uid**                         | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **owner**                       | [**UserReference**](UserReference.md)                                                                                                       | [**UserReference**](UserReference.md)                                                   |                                                                    | [optional] |
| **domain**                      | [**DomainReference**](DomainReference.md)                                                                                                   | [**DomainReference**](DomainReference.md)                                               |                                                                    | [optional] |
| **subDomain**                   | [**SubDomainReference**](SubDomainReference.md)                                                                                             | [**SubDomainReference**](SubDomainReference.md)                                         |                                                                    | [optional] |
| **costCenter**                  | [**CostCenterReference**](CostCenterReference.md)                                                                                           | [**CostCenterReference**](CostCenterReference.md)                                       |                                                                    | [optional] |
| **businessUnit**                | [**BusinessUnitReference**](BusinessUnitReference.md)                                                                                       | [**BusinessUnitReference**](BusinessUnitReference.md)                                   |                                                                    | [optional] |
| **note**                        | str,                                                                                                                                        | str,                                                                                    |                                                                    | [optional] |
| **client**                      | [**ClientReference**](ClientReference.md)                                                                                                   | [**ClientReference**](ClientReference.md)                                               |                                                                    | [optional] |
| **any_string_name**             | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] |

# targetLangs

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
