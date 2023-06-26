# ComparedSegmentDto

## Properties

| Name      | Type    | Description | Notes      |
| --------- | ------- | ----------- | ---------- |
| **uid**   | **str** |             | [optional] |
| **state** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.compared_segment_dto import ComparedSegmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComparedSegmentDto from a JSON string
compared_segment_dto_instance = ComparedSegmentDto.from_json(json)
# print the JSON string representation of the object
print ComparedSegmentDto.to_json()

# convert the object into a dict
compared_segment_dto_dict = compared_segment_dto_instance.to_dict()
# create an instance of ComparedSegmentDto from a dict
compared_segment_dto_from_dict = ComparedSegmentDto.from_dict(compared_segment_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
