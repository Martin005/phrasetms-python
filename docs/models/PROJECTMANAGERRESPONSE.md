# openapi_client.model.projectmanagerresponse.PROJECTMANAGERRESPONSE

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[UserDetailsDtoV3](UserDetailsDtoV3.md) | [**UserDetailsDtoV3**](UserDetailsDtoV3.md) | [**UserDetailsDtoV3**](UserDetailsDtoV3.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[sourceLocales](#sourceLocales)** | list, tuple,  | tuple,  |  | [optional] 
**[targetLocales](#targetLocales)** | list, tuple,  | tuple,  |  | [optional] 
**[workflowSteps](#workflowSteps)** | list, tuple,  | tuple,  |  | [optional] 
**[clients](#clients)** | list, tuple,  | tuple,  |  | [optional] 
**[domains](#domains)** | list, tuple,  | tuple,  |  | [optional] 
**[subDomains](#subDomains)** | list, tuple,  | tuple,  |  | [optional] 
**projectCreate** | bool,  | BoolClass,  |  | [optional] 
**projectViewOther** | bool,  | BoolClass,  |  | [optional] 
**projectEditOther** | bool,  | BoolClass,  |  | [optional] 
**projectDeleteOther** | bool,  | BoolClass,  |  | [optional] 
**[projectClients](#projectClients)** | list, tuple,  | tuple,  |  | [optional] 
**[projectBusinessUnits](#projectBusinessUnits)** | list, tuple,  | tuple,  |  | [optional] 
**projectTemplateCreate** | bool,  | BoolClass,  |  | [optional] 
**projectTemplateViewOther** | bool,  | BoolClass,  |  | [optional] 
**projectTemplateEditOther** | bool,  | BoolClass,  |  | [optional] 
**projectTemplateDeleteOther** | bool,  | BoolClass,  |  | [optional] 
**[projectTemplateClients](#projectTemplateClients)** | list, tuple,  | tuple,  |  | [optional] 
**[projectTemplateBusinessUnits](#projectTemplateBusinessUnits)** | list, tuple,  | tuple,  |  | [optional] 
**transMemoryCreate** | bool,  | BoolClass,  |  | [optional] 
**transMemoryViewOther** | bool,  | BoolClass,  |  | [optional] 
**transMemoryEditOther** | bool,  | BoolClass,  |  | [optional] 
**transMemoryDeleteOther** | bool,  | BoolClass,  |  | [optional] 
**transMemoryExportOther** | bool,  | BoolClass,  |  | [optional] 
**transMemoryImportOther** | bool,  | BoolClass,  |  | [optional] 
**[transMemoryClients](#transMemoryClients)** | list, tuple,  | tuple,  |  | [optional] 
**[transMemoryBusinessUnits](#transMemoryBusinessUnits)** | list, tuple,  | tuple,  |  | [optional] 
**termBaseCreate** | bool,  | BoolClass,  |  | [optional] 
**termBaseViewOther** | bool,  | BoolClass,  |  | [optional] 
**termBaseEditOther** | bool,  | BoolClass,  |  | [optional] 
**termBaseDeleteOther** | bool,  | BoolClass,  |  | [optional] 
**termBaseExportOther** | bool,  | BoolClass,  |  | [optional] 
**termBaseImportOther** | bool,  | BoolClass,  |  | [optional] 
**termBaseApproveOther** | bool,  | BoolClass,  |  | [optional] 
**[termBaseClients](#termBaseClients)** | list, tuple,  | tuple,  |  | [optional] 
**[termBaseBusinessUnits](#termBaseBusinessUnits)** | list, tuple,  | tuple,  |  | [optional] 
**userCreate** | bool,  | BoolClass,  |  | [optional] 
**userViewOther** | bool,  | BoolClass,  |  | [optional] 
**userEditOther** | bool,  | BoolClass,  |  | [optional] 
**userDeleteOther** | bool,  | BoolClass,  |  | [optional] 
**clientDomainSubDomainCreate** | bool,  | BoolClass,  |  | [optional] 
**clientDomainSubDomainViewOther** | bool,  | BoolClass,  |  | [optional] 
**clientDomainSubDomainEditOther** | bool,  | BoolClass,  |  | [optional] 
**clientDomainSubDomainDeleteOther** | bool,  | BoolClass,  |  | [optional] 
**vendorCreate** | bool,  | BoolClass,  |  | [optional] 
**vendorViewOther** | bool,  | BoolClass,  |  | [optional] 
**vendorEditOther** | bool,  | BoolClass,  |  | [optional] 
**vendorDeleteOther** | bool,  | BoolClass,  |  | [optional] 
**dashboardSetting** | str,  | str,  |  | [optional] 
**setupServer** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sourceLocales

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# targetLocales

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# workflowSteps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WorkflowStepReferenceV3**](WorkflowStepReferenceV3.md) | [**WorkflowStepReferenceV3**](WorkflowStepReferenceV3.md) | [**WorkflowStepReferenceV3**](WorkflowStepReferenceV3.md) |  | 

# clients

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) |  | 

# domains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DomainReference**](DomainReference.md) | [**DomainReference**](DomainReference.md) | [**DomainReference**](DomainReference.md) |  | 

# subDomains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SubDomainReference**](SubDomainReference.md) | [**SubDomainReference**](SubDomainReference.md) | [**SubDomainReference**](SubDomainReference.md) |  | 

# projectClients

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) |  | 

# projectBusinessUnits

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BusinessUnitReference**](BusinessUnitReference.md) | [**BusinessUnitReference**](BusinessUnitReference.md) | [**BusinessUnitReference**](BusinessUnitReference.md) |  | 

# projectTemplateClients

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) |  | 

# projectTemplateBusinessUnits

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BusinessUnitReference**](BusinessUnitReference.md) | [**BusinessUnitReference**](BusinessUnitReference.md) | [**BusinessUnitReference**](BusinessUnitReference.md) |  | 

# transMemoryClients

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) |  | 

# transMemoryBusinessUnits

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BusinessUnitReference**](BusinessUnitReference.md) | [**BusinessUnitReference**](BusinessUnitReference.md) | [**BusinessUnitReference**](BusinessUnitReference.md) |  | 

# termBaseClients

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) |  | 

# termBaseBusinessUnits

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BusinessUnitReference**](BusinessUnitReference.md) | [**BusinessUnitReference**](BusinessUnitReference.md) | [**BusinessUnitReference**](BusinessUnitReference.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

