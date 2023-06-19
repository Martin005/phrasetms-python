# AnalyseV3Dto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**inner_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**provider** | [**ProviderReference**](ProviderReference.md) |  | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**net_rate_scheme** | [**NetRateSchemeReference**](NetRateSchemeReference.md) |  | [optional] 
**can_change_net_rate_scheme** | **bool** |  | [optional] 
**analyse_language_parts** | [**list[AnalyseLanguagePartV3Dto]**](AnalyseLanguagePartV3Dto.md) |  | [optional] 
**settings** | [**AbstractAnalyseSettingsDto**](AbstractAnalyseSettingsDto.md) |  | [optional] 
**outdated** | **bool** |  | [optional] 
**import_status** | [**ImportStatusDto**](ImportStatusDto.md) |  | [optional] 
**pure_warnings** | **list[str]** |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

