# CommonConversationDto

## Properties

| Name              | Type                                            | Description                                              | Notes      |
| ----------------- | ----------------------------------------------- | -------------------------------------------------------- | ---------- |
| **id**            | **str**                                         |                                                          | [optional] |
| **type**          | **str**                                         | Field references differs based on the Conversation Type. | [optional] |
| **date_created**  | **datetime**                                    |                                                          | [optional] |
| **date_modified** | **datetime**                                    |                                                          | [optional] |
| **date_edited**   | **datetime**                                    |                                                          | [optional] |
| **created_by**    | [**MentionableUserDto**](MentionableUserDto.md) |                                                          | [optional] |
| **comments**      | [**List[CommentDto]**](CommentDto.md)           |                                                          | [optional] |
| **status**        | [**StatusDto**](StatusDto.md)                   |                                                          | [optional] |
| **deleted**       | **bool**                                        |                                                          | [optional] |

## Example

```python
from phrasetms_client.models.common_conversation_dto import CommonConversationDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonConversationDto from a JSON string
common_conversation_dto_instance = CommonConversationDto.from_json(json)
# print the JSON string representation of the object
print CommonConversationDto.to_json()

# convert the object into a dict
common_conversation_dto_dict = common_conversation_dto_instance.to_dict()
# create an instance of CommonConversationDto from a dict
common_conversation_dto_from_dict = CommonConversationDto.from_dict(common_conversation_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
