# NestedTagsWarningDto

## Properties

| Name                     | Type    | Description | Notes      |
| ------------------------ | ------- | ----------- | ---------- |
| **misplaced_target_tag** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.nested_tags_warning_dto import NestedTagsWarningDto

# TODO update the JSON string below
json = "{}"
# create an instance of NestedTagsWarningDto from a JSON string
nested_tags_warning_dto_instance = NestedTagsWarningDto.from_json(json)
# print the JSON string representation of the object
print NestedTagsWarningDto.to_json()

# convert the object into a dict
nested_tags_warning_dto_dict = nested_tags_warning_dto_instance.to_dict()
# create an instance of NestedTagsWarningDto from a dict
nested_tags_warning_dto_from_dict = NestedTagsWarningDto.from_dict(nested_tags_warning_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
