# openapi_client.model.mention_dto.MentionDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mentionType** | str,  | str,  |  | must be one of ["USER", "GROUP", ] 
**mentionGroupType** | str,  | str,  |  | [optional] must be one of ["JOB", "OWNERS", "PROVIDERS", "GUESTS", "WORKFLOW_STEP", ] 
**uidReference** | [**UidReference**](UidReference.md) | [**UidReference**](UidReference.md) |  | [optional] 
**[userReferences](#userReferences)** | list, tuple,  | tuple,  |  | [optional] 
**mentionableGroup** | [**MentionableGroupDto**](MentionableGroupDto.md) | [**MentionableGroupDto**](MentionableGroupDto.md) |  | [optional] 
**tag** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# userReferences

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MentionableUserDto**](MentionableUserDto.md) | [**MentionableUserDto**](MentionableUserDto.md) | [**MentionableUserDto**](MentionableUserDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
