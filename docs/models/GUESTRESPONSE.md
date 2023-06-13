# openapi_client.model.guestresponse.GUESTRESPONSE

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
**client** | [**ClientReference**](ClientReference.md) | [**ClientReference**](ClientReference.md) |  | 
**enableMT** | bool,  | BoolClass,  |  | [optional] 
**projectViewOther** | bool,  | BoolClass,  |  | [optional] 
**projectViewOtherLinguist** | bool,  | BoolClass,  |  | [optional] 
**projectViewOtherEditor** | bool,  | BoolClass,  |  | [optional] 
**transMemoryViewOther** | bool,  | BoolClass,  |  | [optional] 
**transMemoryEditOther** | bool,  | BoolClass,  |  | [optional] 
**transMemoryExportOther** | bool,  | BoolClass,  |  | [optional] 
**transMemoryImportOther** | bool,  | BoolClass,  |  | [optional] 
**termBaseViewOther** | bool,  | BoolClass,  |  | [optional] 
**termBaseEditOther** | bool,  | BoolClass,  |  | [optional] 
**termBaseExportOther** | bool,  | BoolClass,  |  | [optional] 
**termBaseImportOther** | bool,  | BoolClass,  |  | [optional] 
**termBaseApproveOther** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

