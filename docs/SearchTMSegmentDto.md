# SearchTMSegmentDto

## Properties

| Name                 | Type                                                | Description | Notes      |
| -------------------- | --------------------------------------------------- | ----------- | ---------- |
| **id**               | **str**                                             |             | [optional] |
| **text**             | **str**                                             |             | [optional] |
| **lang**             | **str**                                             |             | [optional] |
| **rtl**              | **bool**                                            |             | [optional] |
| **modified_at**      | **int**                                             |             | [optional] |
| **created_at**       | **int**                                             |             | [optional] |
| **modified_by**      | [**UserReference**](UserReference.md)               |             | [optional] |
| **created_by**       | [**UserReference**](UserReference.md)               |             | [optional] |
| **filename**         | **str**                                             |             | [optional] |
| **project**          | [**SearchTMProjectDto**](SearchTMProjectDto.md)     |             | [optional] |
| **client**           | [**SearchTMClientDto**](SearchTMClientDto.md)       |             | [optional] |
| **domain**           | [**SearchTMDomainDto**](SearchTMDomainDto.md)       |             | [optional] |
| **sub_domain**       | [**SearchTMSubDomainDto**](SearchTMSubDomainDto.md) |             | [optional] |
| **tag_metadata**     | [**List[TagMetadata]**](TagMetadata.md)             |             | [optional] |
| **previous_segment** | **str**                                             |             | [optional] |
| **next_segment**     | **str**                                             |             | [optional] |
| **key**              | **str**                                             |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tm_segment_dto import SearchTMSegmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMSegmentDto from a JSON string
search_tm_segment_dto_instance = SearchTMSegmentDto.from_json(json)
# print the JSON string representation of the object
print SearchTMSegmentDto.to_json()

# convert the object into a dict
search_tm_segment_dto_dict = search_tm_segment_dto_instance.to_dict()
# create an instance of SearchTMSegmentDto from a dict
search_tm_segment_dto_from_dict = SearchTMSegmentDto.from_dict(search_tm_segment_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
