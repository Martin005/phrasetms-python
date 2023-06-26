# AddCommentDto

## Properties

| Name     | Type    | Description | Notes |
| -------- | ------- | ----------- | ----- |
| **text** | **str** |             |

## Example

```python
from phrasetms_client.models.add_comment_dto import AddCommentDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddCommentDto from a JSON string
add_comment_dto_instance = AddCommentDto.from_json(json)
# print the JSON string representation of the object
print AddCommentDto.to_json()

# convert the object into a dict
add_comment_dto_dict = add_comment_dto_instance.to_dict()
# create an instance of AddCommentDto from a dict
add_comment_dto_from_dict = AddCommentDto.from_dict(add_comment_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
