# SearchJobsRequestDto

## Properties

| Name     | Type                                      | Description     | Notes |
| -------- | ----------------------------------------- | --------------- | ----- |
| **jobs** | [**List[UidReference]**](UidReference.md) | Max: 50 records |

## Example

```python
from phrasetms_client.models.search_jobs_request_dto import SearchJobsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchJobsRequestDto from a JSON string
search_jobs_request_dto_instance = SearchJobsRequestDto.from_json(json)
# print the JSON string representation of the object
print SearchJobsRequestDto.to_json()

# convert the object into a dict
search_jobs_request_dto_dict = search_jobs_request_dto_instance.to_dict()
# create an instance of SearchJobsRequestDto from a dict
search_jobs_request_dto_from_dict = SearchJobsRequestDto.from_dict(search_jobs_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
