# AddLqaCommentResultDto

## Properties

| Name             | Type                                            | Description           | Notes      |
| ---------------- | ----------------------------------------------- | --------------------- | ---------- |
| **id**           | **str**                                         | ID of created comment | [optional] |
| **conversation** | [**LQAConversationDto**](LQAConversationDto.md) |                       | [optional] |

## Example

```python
from phrasetms_client.models.add_lqa_comment_result_dto import AddLqaCommentResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddLqaCommentResultDto from a JSON string
add_lqa_comment_result_dto_instance = AddLqaCommentResultDto.from_json(json)
# print the JSON string representation of the object
print AddLqaCommentResultDto.to_json()

# convert the object into a dict
add_lqa_comment_result_dto_dict = add_lqa_comment_result_dto_instance.to_dict()
# create an instance of AddLqaCommentResultDto from a dict
add_lqa_comment_result_dto_from_dict = AddLqaCommentResultDto.from_dict(add_lqa_comment_result_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
