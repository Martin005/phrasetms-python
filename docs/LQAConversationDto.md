# LQAConversationDto

## Properties

| Name                | Type                                            | Description | Notes      |
| ------------------- | ----------------------------------------------- | ----------- | ---------- |
| **id**              | **str**                                         |             | [optional] |
| **type**            | **str**                                         | LQA         | [optional] |
| **date_created**    | **datetime**                                    |             | [optional] |
| **date_modified**   | **datetime**                                    |             | [optional] |
| **date_edited**     | **datetime**                                    |             | [optional] |
| **created_by**      | [**MentionableUserDto**](MentionableUserDto.md) |             | [optional] |
| **comments**        | [**List[CommentDto]**](CommentDto.md)           |             | [optional] |
| **status**          | [**StatusDto**](StatusDto.md)                   |             | [optional] |
| **deleted**         | **bool**                                        |             | [optional] |
| **references**      | [**LQAReferences**](LQAReferences.md)           |             | [optional] |
| **lqa_description** | **str**                                         |             | [optional] |

## Example

```python
from phrasetms_client.models.lqa_conversation_dto import LQAConversationDto

# TODO update the JSON string below
json = "{}"
# create an instance of LQAConversationDto from a JSON string
lqa_conversation_dto_instance = LQAConversationDto.from_json(json)
# print the JSON string representation of the object
print LQAConversationDto.to_json()

# convert the object into a dict
lqa_conversation_dto_dict = lqa_conversation_dto_instance.to_dict()
# create an instance of LQAConversationDto from a dict
lqa_conversation_dto_from_dict = LQAConversationDto.from_dict(lqa_conversation_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
