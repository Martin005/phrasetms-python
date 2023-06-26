# MentionDto

## Properties

| Name                   | Type                                                  | Description | Notes      |
| ---------------------- | ----------------------------------------------------- | ----------- | ---------- |
| **mention_type**       | **str**                                               |             |
| **mention_group_type** | **str**                                               |             | [optional] |
| **uid_reference**      | [**UidReference**](UidReference.md)                   |             | [optional] |
| **user_references**    | [**List[MentionableUserDto]**](MentionableUserDto.md) |             | [optional] |
| **mentionable_group**  | [**MentionableGroupDto**](MentionableGroupDto.md)     |             | [optional] |
| **tag**                | **str**                                               |             | [optional] |

## Example

```python
from phrasetms_client.models.mention_dto import MentionDto

# TODO update the JSON string below
json = "{}"
# create an instance of MentionDto from a JSON string
mention_dto_instance = MentionDto.from_json(json)
# print the JSON string representation of the object
print MentionDto.to_json()

# convert the object into a dict
mention_dto_dict = mention_dto_instance.to_dict()
# create an instance of MentionDto from a dict
mention_dto_from_dict = MentionDto.from_dict(mention_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
