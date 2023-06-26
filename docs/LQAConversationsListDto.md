# LQAConversationsListDto

## Properties

| Name              | Type                                                  | Description | Notes      |
| ----------------- | ----------------------------------------------------- | ----------- | ---------- |
| **conversations** | [**List[LQAConversationDto]**](LQAConversationDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.lqa_conversations_list_dto import LQAConversationsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of LQAConversationsListDto from a JSON string
lqa_conversations_list_dto_instance = LQAConversationsListDto.from_json(json)
# print the JSON string representation of the object
print LQAConversationsListDto.to_json()

# convert the object into a dict
lqa_conversations_list_dto_dict = lqa_conversations_list_dto_instance.to_dict()
# create an instance of LQAConversationsListDto from a dict
lqa_conversations_list_dto_from_dict = LQAConversationsListDto.from_dict(lqa_conversations_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
