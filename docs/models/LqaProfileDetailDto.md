# openapi_client.model.lqa_profile_detail_dto.LqaProfileDetailDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**penaltyPoints** | [**PenaltyPointsDto**](PenaltyPointsDto.md) | [**PenaltyPointsDto**](PenaltyPointsDto.md) |  | 
**errorCategories** | [**ErrorCategoriesDto**](ErrorCategoriesDto.md) | [**ErrorCategoriesDto**](ErrorCategoriesDto.md) |  | 
**uid** | str,  | str,  | UID of the profile | 
**isDefault** | bool,  | BoolClass,  | If profile is set as default for organization | 
**dateCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**passFailThreshold** | [**PassFailThresholdDto**](PassFailThresholdDto.md) | [**PassFailThresholdDto**](PassFailThresholdDto.md) |  | 
**createdBy** | [**UserReference**](UserReference.md) | [**UserReference**](UserReference.md) |  | 
**organization** | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | 
**name** | str,  | str,  | Name of the profile | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

