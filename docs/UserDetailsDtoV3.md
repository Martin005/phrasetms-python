# UserDetailsDtoV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | 
**user_name** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**date_created** | **datetime** |  | [optional] 
**date_deleted** | **datetime** |  | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**role** | **str** | Enum: \&quot;ADMIN\&quot;, \&quot;PROJECT_MANAGER\&quot;, \&quot;LINGUIST\&quot;, \&quot;GUEST\&quot;, \&quot;SUBMITTER\&quot; | 
**timezone** | **str** |  | 
**note** | **str** |  | [optional] 
**receive_newsletter** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**pending_email_change** | **bool** | If user has email change pending (new email not verified) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

