# ConcurrentRequestsDto

## Properties

| Name      | Type    | Description                                                         | Notes      |
| --------- | ------- | ------------------------------------------------------------------- | ---------- |
| **limit** | **int** | Max number of allowed concurrent request, null value means no limit | [optional] |
| **count** | **int** | Current count of running concurrent requests                        | [optional] |

## Example

```python
from phrasetms_client.models.concurrent_requests_dto import ConcurrentRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConcurrentRequestsDto from a JSON string
concurrent_requests_dto_instance = ConcurrentRequestsDto.from_json(json)
# print the JSON string representation of the object
print ConcurrentRequestsDto.to_json()

# convert the object into a dict
concurrent_requests_dto_dict = concurrent_requests_dto_instance.to_dict()
# create an instance of ConcurrentRequestsDto from a dict
concurrent_requests_dto_from_dict = ConcurrentRequestsDto.from_dict(concurrent_requests_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
