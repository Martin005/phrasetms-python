# EditProjectV2Dto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**status** | **str** |  | [optional] 
**client** | [**IdReference**](IdReference.md) |  | [optional] 
**business_unit** | [**IdReference**](IdReference.md) |  | [optional] 
**domain** | [**IdReference**](IdReference.md) |  | [optional] 
**sub_domain** | [**IdReference**](IdReference.md) |  | [optional] 
**owner** | [**IdReference**](IdReference.md) |  | [optional] 
**purchase_order** | **str** |  | [optional] 
**date_due** | **datetime** |  | [optional] 
**note** | **str** |  | [optional] 
**file_handover** | **bool** | Default: false | [optional] 
**lqa_profiles** | [**list[LqaProfilesForWsV2Dto]**](LqaProfilesForWsV2Dto.md) | Lqa profiles that will be added to workflow steps | [optional] 
**archived** | **bool** | Default: false | [optional] 
**custom_fields** | [**list[CustomFieldInstanceApiDto]**](CustomFieldInstanceApiDto.md) | Custom fields for project | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

