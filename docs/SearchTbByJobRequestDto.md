# SearchTbByJobRequestDto

## Properties

| Name        | Type     | Description    | Notes      |
| ----------- | -------- | -------------- | ---------- |
| **query**   | **str**  |                |
| **count**   | **int**  | Default: 15    | [optional] |
| **offset**  | **int**  | Default: 0     | [optional] |
| **reverse** | **bool** | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.search_tb_by_job_request_dto import SearchTbByJobRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTbByJobRequestDto from a JSON string
search_tb_by_job_request_dto_instance = SearchTbByJobRequestDto.from_json(json)
# print the JSON string representation of the object
print SearchTbByJobRequestDto.to_json()

# convert the object into a dict
search_tb_by_job_request_dto_dict = search_tb_by_job_request_dto_instance.to_dict()
# create an instance of SearchTbByJobRequestDto from a dict
search_tb_by_job_request_dto_from_dict = SearchTbByJobRequestDto.from_dict(search_tb_by_job_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
