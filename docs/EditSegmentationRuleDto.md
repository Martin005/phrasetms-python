# EditSegmentationRuleDto

segmentation rule object for editing

## Properties

| Name        | Type     | Description    | Notes      |
| ----------- | -------- | -------------- | ---------- |
| **name**    | **str**  |                |
| **primary** | **bool** | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.edit_segmentation_rule_dto import EditSegmentationRuleDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditSegmentationRuleDto from a JSON string
edit_segmentation_rule_dto_instance = EditSegmentationRuleDto.from_json(json)
# print the JSON string representation of the object
print EditSegmentationRuleDto.to_json()

# convert the object into a dict
edit_segmentation_rule_dto_dict = edit_segmentation_rule_dto_instance.to_dict()
# create an instance of EditSegmentationRuleDto from a dict
edit_segmentation_rule_dto_from_dict = EditSegmentationRuleDto.from_dict(edit_segmentation_rule_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
