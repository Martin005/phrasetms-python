# SearchJobsDto

## Properties

| Name     | Type                                                  | Description | Notes      |
| -------- | ----------------------------------------------------- | ----------- | ---------- |
| **jobs** | [**List[JobPartExtendedDto]**](JobPartExtendedDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.search_jobs_dto import SearchJobsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchJobsDto from a JSON string
search_jobs_dto_instance = SearchJobsDto.from_json(json)
# print the JSON string representation of the object
print SearchJobsDto.to_json()

# convert the object into a dict
search_jobs_dto_dict = search_jobs_dto_instance.to_dict()
# create an instance of SearchJobsDto from a dict
search_jobs_dto_from_dict = SearchJobsDto.from_dict(search_jobs_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
