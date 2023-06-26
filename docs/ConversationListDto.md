# ConversationListDto

## Properties

| Name              | Type                                                        | Description | Notes      |
| ----------------- | ----------------------------------------------------------- | ----------- | ---------- |
| **conversations** | [**List[CommonConversationDto]**](CommonConversationDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.conversation_list_dto import ConversationListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationListDto from a JSON string
conversation_list_dto_instance = ConversationListDto.from_json(json)
# print the JSON string representation of the object
print ConversationListDto.to_json()

# convert the object into a dict
conversation_list_dto_dict = conversation_list_dto_instance.to_dict()
# create an instance of ConversationListDto from a dict
conversation_list_dto_from_dict = ConversationListDto.from_dict(conversation_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
