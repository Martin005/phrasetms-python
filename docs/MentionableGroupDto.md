# MentionableGroupDto

## Properties

| Name                | Type                                | Description | Notes      |
| ------------------- | ----------------------------------- | ----------- | ---------- |
| **group_type**      | **str**                             |             | [optional] |
| **group_name**      | **str**                             |             | [optional] |
| **group_reference** | [**UidReference**](UidReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.mentionable_group_dto import MentionableGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of MentionableGroupDto from a JSON string
mentionable_group_dto_instance = MentionableGroupDto.from_json(json)
# print the JSON string representation of the object
print MentionableGroupDto.to_json()

# convert the object into a dict
mentionable_group_dto_dict = mentionable_group_dto_instance.to_dict()
# create an instance of MentionableGroupDto from a dict
mentionable_group_dto_from_dict = MentionableGroupDto.from_dict(mentionable_group_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
