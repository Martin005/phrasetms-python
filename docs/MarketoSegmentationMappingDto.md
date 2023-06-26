# MarketoSegmentationMappingDto

## Properties

| Name                 | Type                                                              | Description | Notes      |
| -------------------- | ----------------------------------------------------------------- | ----------- | ---------- |
| **segmentation_id**  | **int**                                                           |             | [optional] |
| **segments_mapping** | [**List[MarketoSegmentMappingDto]**](MarketoSegmentMappingDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.marketo_segmentation_mapping_dto import MarketoSegmentationMappingDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarketoSegmentationMappingDto from a JSON string
marketo_segmentation_mapping_dto_instance = MarketoSegmentationMappingDto.from_json(json)
# print the JSON string representation of the object
print MarketoSegmentationMappingDto.to_json()

# convert the object into a dict
marketo_segmentation_mapping_dto_dict = marketo_segmentation_mapping_dto_instance.to_dict()
# create an instance of MarketoSegmentationMappingDto from a dict
marketo_segmentation_mapping_dto_from_dict = MarketoSegmentationMappingDto.from_dict(marketo_segmentation_mapping_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
