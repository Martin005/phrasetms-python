# EditLqaConversationDto

## Properties

| Name                | Type                                                | Description | Notes      |
| ------------------- | --------------------------------------------------- | ----------- | ---------- |
| **lqa_description** | **str**                                             |             | [optional] |
| **lqa**             | [**List[LQAReference]**](LQAReference.md)           |             |
| **status**          | **str**                                             |             | [optional] |
| **correlation**     | [**ReferenceCorrelation**](ReferenceCorrelation.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.edit_lqa_conversation_dto import EditLqaConversationDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditLqaConversationDto from a JSON string
edit_lqa_conversation_dto_instance = EditLqaConversationDto.from_json(json)
# print the JSON string representation of the object
print EditLqaConversationDto.to_json()

# convert the object into a dict
edit_lqa_conversation_dto_dict = edit_lqa_conversation_dto_instance.to_dict()
# create an instance of EditLqaConversationDto from a dict
edit_lqa_conversation_dto_from_dict = EditLqaConversationDto.from_dict(edit_lqa_conversation_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
