# PlainConversationDto

## Properties

| Name              | Type                                            | Description    | Notes      |
| ----------------- | ----------------------------------------------- | -------------- | ---------- |
| **id**            | **str**                                         |                | [optional] |
| **type**          | **str**                                         | SEGMENT_TARGET | [optional] |
| **date_created**  | **datetime**                                    |                | [optional] |
| **date_modified** | **datetime**                                    |                | [optional] |
| **date_edited**   | **datetime**                                    |                | [optional] |
| **created_by**    | [**MentionableUserDto**](MentionableUserDto.md) |                | [optional] |
| **comments**      | [**List[CommentDto]**](CommentDto.md)           |                | [optional] |
| **status**        | [**StatusDto**](StatusDto.md)                   |                | [optional] |
| **deleted**       | **bool**                                        |                | [optional] |
| **references**    | [**PlainReferences**](PlainReferences.md)       |                | [optional] |

## Example

```python
from phrasetms_client.models.plain_conversation_dto import PlainConversationDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlainConversationDto from a JSON string
plain_conversation_dto_instance = PlainConversationDto.from_json(json)
# print the JSON string representation of the object
print PlainConversationDto.to_json()

# convert the object into a dict
plain_conversation_dto_dict = plain_conversation_dto_instance.to_dict()
# create an instance of PlainConversationDto from a dict
plain_conversation_dto_from_dict = PlainConversationDto.from_dict(plain_conversation_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
