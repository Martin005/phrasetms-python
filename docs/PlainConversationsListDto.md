# PlainConversationsListDto

## Properties

| Name              | Type                                                      | Description | Notes      |
| ----------------- | --------------------------------------------------------- | ----------- | ---------- |
| **conversations** | [**List[PlainConversationDto]**](PlainConversationDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.plain_conversations_list_dto import PlainConversationsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlainConversationsListDto from a JSON string
plain_conversations_list_dto_instance = PlainConversationsListDto.from_json(json)
# print the JSON string representation of the object
print PlainConversationsListDto.to_json()

# convert the object into a dict
plain_conversations_list_dto_dict = plain_conversations_list_dto_instance.to_dict()
# create an instance of PlainConversationsListDto from a dict
plain_conversations_list_dto_from_dict = PlainConversationsListDto.from_dict(plain_conversations_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
