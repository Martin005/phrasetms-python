# phrasetms_client.model.projectmanager.PROJECTMANAGER

## Model Type Info

| Input Type                                                                                                                                              | Accessed Type                                                                           | Description | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------- | ----- |
| dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |             |

### Composed Schemas (allOf/anyOf/oneOf/not)

#### allOf

| Class Name                                        | Input Type                                            | Accessed Type                                         | Description | Notes |
| ------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------- | ----- |
| [AbstractUserCreateDto](AbstractUserCreateDto.md) | [**AbstractUserCreateDto**](AbstractUserCreateDto.md) | [**AbstractUserCreateDto**](AbstractUserCreateDto.md) |             |
| [all_of_1](#all_of_1)                             | dict, frozendict.frozendict,                          | frozendict.frozendict,                                |             |

# all_of_1

## Model Type Info

| Input Type                   | Accessed Type          | Description | Notes |
| ---------------------------- | ---------------------- | ----------- | ----- |
| dict, frozendict.frozendict, | frozendict.frozendict, |             |

### Dictionary Keys

| Key                                                               | Input Type                                                                                                                                  | Accessed Type                                                                           | Description                                                               | Notes                                                                |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **[sourceLocales](#sourceLocales)**                               | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                           | [optional]                                                           |
| **[targetLocales](#targetLocales)**                               | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                           | [optional]                                                           |
| **[workflowSteps](#workflowSteps)**                               | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                           | [optional]                                                           |
| **[clients](#clients)**                                           | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                           | [optional]                                                           |
| **[domains](#domains)**                                           | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                           | [optional]                                                           |
| **[subDomains](#subDomains)**                                     | list, tuple,                                                                                                                                | tuple,                                                                                  |                                                                           | [optional]                                                           |
| **projectCreate**                                                 | bool,                                                                                                                                       | BoolClass,                                                                              | Enable project creation. Default: true                                    | [optional]                                                           |
| **projectViewOther**                                              | bool,                                                                                                                                       | BoolClass,                                                                              | View projects created by other users. Default: true                       | [optional]                                                           |
| **projectEditOther**                                              | bool,                                                                                                                                       | BoolClass,                                                                              | Modify projects created by other users. Default: true                     | [optional]                                                           |
| **projectDeleteOther**                                            | bool,                                                                                                                                       | BoolClass,                                                                              | Delete projects created by other users. Default: true                     | [optional]                                                           |
| **[projectClients](#projectClients)**                             | list, tuple,                                                                                                                                | tuple,                                                                                  | Access projects of a selected clients only                                | [optional]                                                           |
| **[projectBusinessUnits](#projectBusinessUnits)**                 | list, tuple,                                                                                                                                | tuple,                                                                                  | Access projects of selected business units only                           | [optional]                                                           |
| **projectTemplateCreate**                                         | bool,                                                                                                                                       | BoolClass,                                                                              | Enable project templates creation. Default: true                          | [optional]                                                           |
| **projectTemplateViewOther**                                      | bool,                                                                                                                                       | BoolClass,                                                                              | View project templates created by other users. Default: true              | [optional]                                                           |
| **projectTemplateEditOther**                                      | bool,                                                                                                                                       | BoolClass,                                                                              | Modify project templates created by other users. Default: true            | [optional]                                                           |
| **projectTemplateDeleteOther**                                    | bool,                                                                                                                                       | BoolClass,                                                                              | Delete project templates created by other users. Default: true            | [optional]                                                           |
| **[projectTemplateClients](#projectTemplateClients)**             | list, tuple,                                                                                                                                | tuple,                                                                                  | Access project templates of a selected clients only                       | [optional]                                                           |
| **[projectTemplateBusinessUnits](#projectTemplateBusinessUnits)** | list, tuple,                                                                                                                                | tuple,                                                                                  | Access project templates of selected business units only                  | [optional]                                                           |
| **transMemoryCreate**                                             | bool,                                                                                                                                       | BoolClass,                                                                              | Enable TMs creation. Default: true                                        | [optional]                                                           |
| **transMemoryViewOther**                                          | bool,                                                                                                                                       | BoolClass,                                                                              | View TMs created by other users. Default: true                            | [optional]                                                           |
| **transMemoryEditOther**                                          | bool,                                                                                                                                       | BoolClass,                                                                              | Modify TMs created by other users. Default: true                          | [optional]                                                           |
| **transMemoryDeleteOther**                                        | bool,                                                                                                                                       | BoolClass,                                                                              | Delete TMs created by other users. Default: true                          | [optional]                                                           |
| **transMemoryExportOther**                                        | bool,                                                                                                                                       | BoolClass,                                                                              | Export TMs created by other users. Default: true                          | [optional]                                                           |
| **transMemoryImportOther**                                        | bool,                                                                                                                                       | BoolClass,                                                                              | Import into TMs created by other users. Default: true                     | [optional]                                                           |
| **[transMemoryClients](#transMemoryClients)**                     | list, tuple,                                                                                                                                | tuple,                                                                                  | Access TMs of a selected clients only                                     | [optional]                                                           |
| **[transMemoryBusinessUnits](#transMemoryBusinessUnits)**         | list, tuple,                                                                                                                                | tuple,                                                                                  | Access TMs of selected business units only                                | [optional]                                                           |
| **termBaseCreate**                                                | bool,                                                                                                                                       | BoolClass,                                                                              | Enable TBs creation. Default: true                                        | [optional]                                                           |
| **termBaseViewOther**                                             | bool,                                                                                                                                       | BoolClass,                                                                              | View TBs created by other users. Default: true                            | [optional]                                                           |
| **termBaseEditOther**                                             | bool,                                                                                                                                       | BoolClass,                                                                              | Modify TBs created by other users. Default: true                          | [optional]                                                           |
| **termBaseDeleteOther**                                           | bool,                                                                                                                                       | BoolClass,                                                                              | Delete TBs created by other users. Default: true                          | [optional]                                                           |
| **termBaseExportOther**                                           | bool,                                                                                                                                       | BoolClass,                                                                              | Export TBs created by other users. Default: true                          | [optional]                                                           |
| **termBaseImportOther**                                           | bool,                                                                                                                                       | BoolClass,                                                                              | Import into TBs created by other users. Default: true                     | [optional]                                                           |
| **termBaseApproveOther**                                          | bool,                                                                                                                                       | BoolClass,                                                                              | Approve terms in TBs created by other users. Default: true                | [optional]                                                           |
| **[termBaseClients](#termBaseClients)**                           | list, tuple,                                                                                                                                | tuple,                                                                                  | Access TBs of a selected clients only                                     | [optional]                                                           |
| **[termBaseBusinessUnits](#termBaseBusinessUnits)**               | list, tuple,                                                                                                                                | tuple,                                                                                  | Access TBs of selected business units only                                | [optional]                                                           |
| **userCreate**                                                    | bool,                                                                                                                                       | BoolClass,                                                                              | Enable users creation. Default: true                                      | [optional]                                                           |
| **userViewOther**                                                 | bool,                                                                                                                                       | BoolClass,                                                                              | View users created by other users. Default: true                          | [optional]                                                           |
| **userEditOther**                                                 | bool,                                                                                                                                       | BoolClass,                                                                              | Modify users created by other users. Default: true                        | [optional]                                                           |
| **userDeleteOther**                                               | bool,                                                                                                                                       | BoolClass,                                                                              | Delete users created by other users. Default: true                        | [optional]                                                           |
| **clientDomainSubDomainCreate**                                   | bool,                                                                                                                                       | BoolClass,                                                                              | Enable clients, domains, subdomains creation. Default: true               | [optional]                                                           |
| **clientDomainSubDomainViewOther**                                | bool,                                                                                                                                       | BoolClass,                                                                              | View clients, domains, subdomains created by other users. Default: true   | [optional]                                                           |
| **clientDomainSubDomainEditOther**                                | bool,                                                                                                                                       | BoolClass,                                                                              | Modify clients, domains, subdomains created by other users. Default: true | [optional]                                                           |
| **clientDomainSubDomainDeleteOther**                              | bool,                                                                                                                                       | BoolClass,                                                                              | Delete clients, domains, subdomains created by other users. Default: true | [optional]                                                           |
| **vendorCreate**                                                  | bool,                                                                                                                                       | BoolClass,                                                                              | Enable Vendors creation. Default: true                                    | [optional]                                                           |
| **vendorViewOther**                                               | bool,                                                                                                                                       | BoolClass,                                                                              | View Vendors created by other users. Default: true                        | [optional]                                                           |
| **vendorEditOther**                                               | bool,                                                                                                                                       | BoolClass,                                                                              | Modify Vendors created by other users. Default: true                      | [optional]                                                           |
| **vendorDeleteOther**                                             | bool,                                                                                                                                       | BoolClass,                                                                              | Delete Vendors created by other users. Default: true                      | [optional]                                                           |
| **dashboardSetting**                                              | str,                                                                                                                                        | str,                                                                                    | Home page dashboards. Default: OWN_DATA                                   | [optional] must be one of ["ALL_DATA", "OWN_DATA", "NO_DASHBOARD", ] |
| **setupServer**                                                   | bool,                                                                                                                                       | BoolClass,                                                                              | Modify setup&#x27;s server settings. Default: true                        | [optional]                                                           |
| **any_string_name**                                               | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type        | [optional]                                                           |

# sourceLocales

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# targetLocales

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name | Input Type | Accessed Type | Description | Notes |
| ---------- | ---------- | ------------- | ----------- | ----- |
| items      | str,       | str,          |             |

# workflowSteps

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# clients

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# domains

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# subDomains

## Model Type Info

| Input Type   | Accessed Type | Description | Notes |
| ------------ | ------------- | ----------- | ----- |
| list, tuple, | tuple,        |             |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# projectClients

Access projects of a selected clients only

## Model Type Info

| Input Type   | Accessed Type | Description                                | Notes |
| ------------ | ------------- | ------------------------------------------ | ----- |
| list, tuple, | tuple,        | Access projects of a selected clients only |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# projectBusinessUnits

Access projects of selected business units only

## Model Type Info

| Input Type   | Accessed Type | Description                                     | Notes |
| ------------ | ------------- | ----------------------------------------------- | ----- |
| list, tuple, | tuple,        | Access projects of selected business units only |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# projectTemplateClients

Access project templates of a selected clients only

## Model Type Info

| Input Type   | Accessed Type | Description                                         | Notes |
| ------------ | ------------- | --------------------------------------------------- | ----- |
| list, tuple, | tuple,        | Access project templates of a selected clients only |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# projectTemplateBusinessUnits

Access project templates of selected business units only

## Model Type Info

| Input Type   | Accessed Type | Description                                              | Notes |
| ------------ | ------------- | -------------------------------------------------------- | ----- |
| list, tuple, | tuple,        | Access project templates of selected business units only |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# transMemoryClients

Access TMs of a selected clients only

## Model Type Info

| Input Type   | Accessed Type | Description                           | Notes |
| ------------ | ------------- | ------------------------------------- | ----- |
| list, tuple, | tuple,        | Access TMs of a selected clients only |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# transMemoryBusinessUnits

Access TMs of selected business units only

## Model Type Info

| Input Type   | Accessed Type | Description                                | Notes |
| ------------ | ------------- | ------------------------------------------ | ----- |
| list, tuple, | tuple,        | Access TMs of selected business units only |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# termBaseClients

Access TBs of a selected clients only

## Model Type Info

| Input Type   | Accessed Type | Description                           | Notes |
| ------------ | ------------- | ------------------------------------- | ----- |
| list, tuple, | tuple,        | Access TBs of a selected clients only |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

# termBaseBusinessUnits

Access TBs of selected business units only

## Model Type Info

| Input Type   | Accessed Type | Description                                | Notes |
| ------------ | ------------- | ------------------------------------------ | ----- |
| list, tuple, | tuple,        | Access TBs of selected business units only |

### Tuple Items

| Class Name                          | Input Type                          | Accessed Type                       | Description | Notes |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------- | ----- |
| [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |             |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
