# MarketoSegmentMappingDto

## Properties

| Name           | Type     | Description | Notes      |
| -------------- | -------- | ----------- | ---------- |
| **segment_id** | **int**  |             | [optional] |
| **locale**     | **str**  |             | [optional] |
| **source**     | **bool** |             | [optional] |

## Example

```python
from phrasetms_client.models.marketo_segment_mapping_dto import MarketoSegmentMappingDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarketoSegmentMappingDto from a JSON string
marketo_segment_mapping_dto_instance = MarketoSegmentMappingDto.from_json(json)
# print the JSON string representation of the object
print MarketoSegmentMappingDto.to_json()

# convert the object into a dict
marketo_segment_mapping_dto_dict = marketo_segment_mapping_dto_instance.to_dict()
# create an instance of MarketoSegmentMappingDto from a dict
marketo_segment_mapping_dto_from_dict = MarketoSegmentMappingDto.from_dict(marketo_segment_mapping_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
