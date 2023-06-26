# CreatePlainConversationDto

## Properties

| Name           | Type                                      | Description | Notes      |
| -------------- | ----------------------------------------- | ----------- | ---------- |
| **comment**    | [**AddCommentDto**](AddCommentDto.md)     |             | [optional] |
| **references** | [**PlainReferences**](PlainReferences.md) |             |

## Example

```python
from phrasetms_client.models.create_plain_conversation_dto import CreatePlainConversationDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlainConversationDto from a JSON string
create_plain_conversation_dto_instance = CreatePlainConversationDto.from_json(json)
# print the JSON string representation of the object
print CreatePlainConversationDto.to_json()

# convert the object into a dict
create_plain_conversation_dto_dict = create_plain_conversation_dto_instance.to_dict()
# create an instance of CreatePlainConversationDto from a dict
create_plain_conversation_dto_from_dict = CreatePlainConversationDto.from_dict(create_plain_conversation_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
