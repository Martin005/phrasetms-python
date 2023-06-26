# AddPlainCommentResultDto

## Properties

| Name             | Type                                                | Description           | Notes      |
| ---------------- | --------------------------------------------------- | --------------------- | ---------- |
| **id**           | **str**                                             | ID of created comment | [optional] |
| **conversation** | [**PlainConversationDto**](PlainConversationDto.md) |                       | [optional] |

## Example

```python
from phrasetms_client.models.add_plain_comment_result_dto import AddPlainCommentResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddPlainCommentResultDto from a JSON string
add_plain_comment_result_dto_instance = AddPlainCommentResultDto.from_json(json)
# print the JSON string representation of the object
print AddPlainCommentResultDto.to_json()

# convert the object into a dict
add_plain_comment_result_dto_dict = add_plain_comment_result_dto_instance.to_dict()
# create an instance of AddPlainCommentResultDto from a dict
add_plain_comment_result_dto_from_dict = AddPlainCommentResultDto.from_dict(add_plain_comment_result_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
