# SearchTMByJobRequestDto

## Properties

| Name                 | Type                                          | Description | Notes      |
| -------------------- | --------------------------------------------- | ----------- | ---------- |
| **segment**          | **str**                                       |             |
| **workflow_level**   | **int**                                       |             | [optional] |
| **score_threshold**  | **float**                                     |             | [optional] |
| **previous_segment** | **str**                                       |             | [optional] |
| **next_segment**     | **str**                                       |             | [optional] |
| **context_key**      | **str**                                       |             | [optional] |
| **max_segments**     | **int**                                       | Default: 5  | [optional] |
| **max_sub_segments** | **int**                                       | Default: 5  | [optional] |
| **tag_metadata**     | [**List[TagMetadataDto]**](TagMetadataDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.search_tmby_job_request_dto import SearchTMByJobRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMByJobRequestDto from a JSON string
search_tmby_job_request_dto_instance = SearchTMByJobRequestDto.from_json(json)
# print the JSON string representation of the object
print SearchTMByJobRequestDto.to_json()

# convert the object into a dict
search_tmby_job_request_dto_dict = search_tmby_job_request_dto_instance.to_dict()
# create an instance of SearchTMByJobRequestDto from a dict
search_tmby_job_request_dto_from_dict = SearchTMByJobRequestDto.from_dict(search_tmby_job_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
