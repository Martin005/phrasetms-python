# EditPlainConversationDto

## Properties

| Name            | Type                                                | Description | Notes      |
| --------------- | --------------------------------------------------- | ----------- | ---------- |
| **status**      | **str**                                             |             | [optional] |
| **correlation** | [**ReferenceCorrelation**](ReferenceCorrelation.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.edit_plain_conversation_dto import EditPlainConversationDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditPlainConversationDto from a JSON string
edit_plain_conversation_dto_instance = EditPlainConversationDto.from_json(json)
# print the JSON string representation of the object
print EditPlainConversationDto.to_json()

# convert the object into a dict
edit_plain_conversation_dto_dict = edit_plain_conversation_dto_instance.to_dict()
# create an instance of EditPlainConversationDto from a dict
edit_plain_conversation_dto_from_dict = EditPlainConversationDto.from_dict(edit_plain_conversation_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
