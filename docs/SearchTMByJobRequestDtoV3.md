# SearchTMByJobRequestDtoV3

## Properties

| Name                | Type      | Description    | Notes      |
| ------------------- | --------- | -------------- | ---------- |
| **query**           | **str**   |                |
| **reverse**         | **bool**  | Default: false | [optional] |
| **score_threshold** | **float** | Default: 0.0   | [optional] |
| **max_results**     | **int**   | Default: 15    | [optional] |

## Example

```python
from phrasetms_client.models.search_tmby_job_request_dto_v3 import SearchTMByJobRequestDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTMByJobRequestDtoV3 from a JSON string
search_tmby_job_request_dto_v3_instance = SearchTMByJobRequestDtoV3.from_json(json)
# print the JSON string representation of the object
print SearchTMByJobRequestDtoV3.to_json()

# convert the object into a dict
search_tmby_job_request_dto_v3_dict = search_tmby_job_request_dto_v3_instance.to_dict()
# create an instance of SearchTMByJobRequestDtoV3 from a dict
search_tmby_job_request_dto_v3_from_dict = SearchTMByJobRequestDtoV3.from_dict(search_tmby_job_request_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
