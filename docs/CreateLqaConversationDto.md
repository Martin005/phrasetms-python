# CreateLqaConversationDto

## Properties

| Name                | Type                                  | Description | Notes      |
| ------------------- | ------------------------------------- | ----------- | ---------- |
| **lqa_description** | **str**                               |             | [optional] |
| **references**      | [**LQAReferences**](LQAReferences.md) |             |

## Example

```python
from phrasetms_client.models.create_lqa_conversation_dto import CreateLqaConversationDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLqaConversationDto from a JSON string
create_lqa_conversation_dto_instance = CreateLqaConversationDto.from_json(json)
# print the JSON string representation of the object
print CreateLqaConversationDto.to_json()

# convert the object into a dict
create_lqa_conversation_dto_dict = create_lqa_conversation_dto_instance.to_dict()
# create an instance of CreateLqaConversationDto from a dict
create_lqa_conversation_dto_from_dict = CreateLqaConversationDto.from_dict(create_lqa_conversation_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
