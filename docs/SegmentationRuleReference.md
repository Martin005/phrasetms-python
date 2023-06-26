# SegmentationRuleReference

## Properties

| Name             | Type         | Description    | Notes                 |
| ---------------- | ------------ | -------------- | --------------------- |
| **id**           | **str**      |                | [optional] [readonly] |
| **uid**          | **str**      |                | [optional] [readonly] |
| **name**         | **str**      |                |
| **locale**       | **str**      |                | [optional]            |
| **primary**      | **bool**     | Default: false | [optional]            |
| **filename**     | **str**      |                |
| **date_created** | **datetime** |                | [optional] [readonly] |

## Example

```python
from phrasetms_client.models.segmentation_rule_reference import SegmentationRuleReference

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentationRuleReference from a JSON string
segmentation_rule_reference_instance = SegmentationRuleReference.from_json(json)
# print the JSON string representation of the object
print SegmentationRuleReference.to_json()

# convert the object into a dict
segmentation_rule_reference_dict = segmentation_rule_reference_instance.to_dict()
# create an instance of SegmentationRuleReference from a dict
segmentation_rule_reference_from_dict = SegmentationRuleReference.from_dict(segmentation_rule_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
