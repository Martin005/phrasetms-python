# AsyncRequestStatusDto

## Properties

| Name                    | Type                                                  | Description | Notes      |
| ----------------------- | ----------------------------------------------------- | ----------- | ---------- |
| **concurrent_requests** | [**ConcurrentRequestsDto**](ConcurrentRequestsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.async_request_status_dto import AsyncRequestStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncRequestStatusDto from a JSON string
async_request_status_dto_instance = AsyncRequestStatusDto.from_json(json)
# print the JSON string representation of the object
print AsyncRequestStatusDto.to_json()

# convert the object into a dict
async_request_status_dto_dict = async_request_status_dto_instance.to_dict()
# create an instance of AsyncRequestStatusDto from a dict
async_request_status_dto_from_dict = AsyncRequestStatusDto.from_dict(async_request_status_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
