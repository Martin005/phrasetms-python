# ComparedSegmentsDto

## Properties

| Name         | Type                                                  | Description | Notes      |
| ------------ | ----------------------------------------------------- | ----------- | ---------- |
| **segments** | [**List[ComparedSegmentDto]**](ComparedSegmentDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.compared_segments_dto import ComparedSegmentsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComparedSegmentsDto from a JSON string
compared_segments_dto_instance = ComparedSegmentsDto.from_json(json)
# print the JSON string representation of the object
print ComparedSegmentsDto.to_json()

# convert the object into a dict
compared_segments_dto_dict = compared_segments_dto_instance.to_dict()
# create an instance of ComparedSegmentsDto from a dict
compared_segments_dto_from_dict = ComparedSegmentsDto.from_dict(compared_segments_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
