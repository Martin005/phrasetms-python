# SegmentationRuleDto

segmentation rule object

## Properties

| Name             | Type                                  | Description    | Notes                 |
| ---------------- | ------------------------------------- | -------------- | --------------------- |
| **id**           | **str**                               |                | [optional] [readonly] |
| **uid**          | **str**                               |                | [optional] [readonly] |
| **name**         | **str**                               |                |
| **locale**       | **str**                               |                | [optional]            |
| **primary**      | **bool**                              | Default: false | [optional]            |
| **filename**     | **str**                               |                |
| **date_created** | **datetime**                          |                | [optional] [readonly] |
| **created_by**   | [**UserReference**](UserReference.md) |                | [optional]            |

## Example

```python
from phrasetms_client.models.segmentation_rule_dto import SegmentationRuleDto

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentationRuleDto from a JSON string
segmentation_rule_dto_instance = SegmentationRuleDto.from_json(json)
# print the JSON string representation of the object
print SegmentationRuleDto.to_json()

# convert the object into a dict
segmentation_rule_dto_dict = segmentation_rule_dto_instance.to_dict()
# create an instance of SegmentationRuleDto from a dict
segmentation_rule_dto_from_dict = SegmentationRuleDto.from_dict(segmentation_rule_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
