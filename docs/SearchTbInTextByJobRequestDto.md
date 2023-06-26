# SearchTbInTextByJobRequestDto

## Properties

| Name                      | Type     | Description    | Notes      |
| ------------------------- | -------- | -------------- | ---------- |
| **text**                  | **str**  |                |
| **reverse**               | **bool** | Default: false | [optional] |
| **zero_length_separator** | **str**  |                | [optional] |

## Example

```python
from phrasetms_client.models.search_tb_in_text_by_job_request_dto import SearchTbInTextByJobRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTbInTextByJobRequestDto from a JSON string
search_tb_in_text_by_job_request_dto_instance = SearchTbInTextByJobRequestDto.from_json(json)
# print the JSON string representation of the object
print SearchTbInTextByJobRequestDto.to_json()

# convert the object into a dict
search_tb_in_text_by_job_request_dto_dict = search_tb_in_text_by_job_request_dto_instance.to_dict()
# create an instance of SearchTbInTextByJobRequestDto from a dict
search_tb_in_text_by_job_request_dto_from_dict = SearchTbInTextByJobRequestDto.from_dict(search_tb_in_text_by_job_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
