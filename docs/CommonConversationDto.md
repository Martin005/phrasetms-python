# CommonConversationDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** | Field references differs based on the Conversation Type. | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_modified** | **datetime** |  | [optional] 
**date_edited** | **datetime** |  | [optional] 
**created_by** | [**MentionableUserDto**](MentionableUserDto.md) |  | [optional] 
**comments** | [**list[CommentDto]**](CommentDto.md) |  | [optional] 
**status** | [**StatusDto**](StatusDto.md) |  | [optional] 
**deleted** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

