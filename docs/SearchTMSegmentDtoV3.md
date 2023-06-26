# SearchTMSegmentDtoV3

## Properties

| Name                 | Type                                                    | Description | Notes      |
| -------------------- | ------------------------------------------------------- | ----------- | ---------- |
| **id**               | **str**                                                 |             | [optional] |
| **text**             | **str**                                                 |             | [optional] |
| **lang**             | **str**                                                 |             | [optional] |
| **rtl**              | **bool**                                                |             | [optional] |
| **modified_at**      | **int**                                                 |             | [optional] |
| **created_at**       | **int**                                                 |             | [optional] |
| **modified_by**      | [**UserReference**](UserReference.md)                   |             | [optional] |
| **created_by**       | [**UserReference**](UserReference.md)                   |             | [optional] |
| **filename**         | **str**                                                 |             | [optional] |
| **project**          | [**SearchTMProjectDtoV3**](SearchTMProjectDtoV3.md)     |             | [optional] |
| **client**           | [**SearchTMClientDtoV3**](SearchTMClientDtoV3.md)       |             | [optional] |
| **domain**           | [**SearchTMDomainDtoV3**](SearchTMDomainDtoV3.md)       |             | [optional] |
| **sub_domain**       | [**SearchTMSubDomainDtoV3**](SearchTMSubDomainDtoV3.md) |             | [optional] |
| **tag_metadata**     | [**List[TagMetadata]**](TagMetadata.md)                 |             | [optional] |
| **previous_segment** | **str**                                                 |             | [optional] |
| **next_segment**     | **str**                                                 |             | [optional] |
| **key**              | **str**                                                 |             | [optional] |
| **target_note**      | **str**                                                 |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tm_segment_dto_v3 import SearchTMSegmentDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMSegmentDtoV3 from a JSON string
search_tm_segment_dto_v3_instance = SearchTMSegmentDtoV3.from_json(json)
# print the JSON string representation of the object
print SearchTMSegmentDtoV3.to_json()

# convert the object into a dict
search_tm_segment_dto_v3_dict = search_tm_segment_dto_v3_instance.to_dict()
# create an instance of SearchTMSegmentDtoV3 from a dict
search_tm_segment_dto_v3_from_dict = SearchTMSegmentDtoV3.from_dict(search_tm_segment_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
