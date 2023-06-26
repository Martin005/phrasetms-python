# JoinTagsWarningDto

## Properties

| Name                       | Type    | Description | Notes      |
| -------------------------- | ------- | ----------- | ---------- |
| **source_tags_count**      | **int** |             | [optional] |
| **translation_tags_count** | **int** |             | [optional] |

## Example

```python
from phrasetms_client.models.join_tags_warning_dto import JoinTagsWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of JoinTagsWarningDto from a JSON string
join_tags_warning_dto_instance = JoinTagsWarningDto.from_json(json)
# print the JSON string representation of the object
print JoinTagsWarningDto.to_json()

# convert the object into a dict
join_tags_warning_dto_dict = join_tags_warning_dto_instance.to_dict()
# create an instance of JoinTagsWarningDto from a dict
join_tags_warning_dto_from_dict = JoinTagsWarningDto.from_dict(join_tags_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
