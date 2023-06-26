# WildCardSearchByJobRequestDtoV3

## Properties

| Name        | Type     | Description    | Notes      |
| ----------- | -------- | -------------- | ---------- |
| **query**   | **str**  |                |
| **reverse** | **bool** | Default: false | [optional] |
| **count**   | **int**  |                | [optional] |
| **offset**  | **int**  |                | [optional] |

## Example

```python
from phrasetms_client.models.wild_card_search_by_job_request_dto_v3 import WildCardSearchByJobRequestDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of WildCardSearchByJobRequestDtoV3 from a JSON string
wild_card_search_by_job_request_dto_v3_instance = WildCardSearchByJobRequestDtoV3.from_json(json)
# print the JSON string representation of the object
print WildCardSearchByJobRequestDtoV3.to_json()

# convert the object into a dict
wild_card_search_by_job_request_dto_v3_dict = wild_card_search_by_job_request_dto_v3_instance.to_dict()
# create an instance of WildCardSearchByJobRequestDtoV3 from a dict
wild_card_search_by_job_request_dto_v3_from_dict = WildCardSearchByJobRequestDtoV3.from_dict(wild_card_search_by_job_request_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
