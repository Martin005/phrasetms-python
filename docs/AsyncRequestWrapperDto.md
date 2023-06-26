# AsyncRequestWrapperDto

## Properties

| Name              | Type                                      | Description | Notes      |
| ----------------- | ----------------------------------------- | ----------- | ---------- |
| **async_request** | [**AsyncRequestDto**](AsyncRequestDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.async_request_wrapper_dto import AsyncRequestWrapperDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncRequestWrapperDto from a JSON string
async_request_wrapper_dto_instance = AsyncRequestWrapperDto.from_json(json)
# print the JSON string representation of the object
print AsyncRequestWrapperDto.to_json()

# convert the object into a dict
async_request_wrapper_dto_dict = async_request_wrapper_dto_instance.to_dict()
# create an instance of AsyncRequestWrapperDto from a dict
async_request_wrapper_dto_from_dict = AsyncRequestWrapperDto.from_dict(async_request_wrapper_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
