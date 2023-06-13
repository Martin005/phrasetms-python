# openapi_client.model.project_reference.ProjectReference

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  |  | [optional] 
**innerId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**name** | str,  | str,  |  | [optional] 
**businessUnit** | [**BusinessUnitReference**](BusinessUnitReference.md) | [**BusinessUnitReference**](BusinessUnitReference.md) |  | [optional] 
**domain** | [**DomainReference**](DomainReference.md) | [**DomainReference**](DomainReference.md) |  | [optional] 
**subDomain** | [**SubDomainReference**](SubDomainReference.md) | [**SubDomainReference**](SubDomainReference.md) |  | [optional] 
**client** | [**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) |  | [optional] 
**costCenter** | [**CostCenterReference**](CostCenterReference.md) | [**CostCenterReference**](CostCenterReference.md) |  | [optional] 
**dueDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**createdDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**createdBy** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**owner** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | [optional] 
**vendor** | [**VendorUserReference**](VendorUserReference.md) | [**VendorUserReference**](VendorUserReference.md) |  | [optional] 
**purchaseOrder** | str,  | str,  |  | [optional] 
**sourceLang** | str,  | str,  |  | [optional] 
**[targetLangs](#targetLangs)** | list, tuple,  | tuple,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**progress** | [**ProgressReference**](ProgressReference.md) | [**ProgressReference**](ProgressReference.md) |  | [optional] 
**[metadata](#metadata)** | list, tuple,  | tuple,  |  | [optional] 
**note** | str,  | str,  |  | [optional] 
**deleted** | bool,  | BoolClass,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# targetLangs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MetadataReference**](MetadataReference.md) | [**MetadataReference**](MetadataReference.md) | [**MetadataReference**](MetadataReference.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

