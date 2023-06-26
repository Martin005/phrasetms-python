# AsyncRequestWrapperV2Dto

## Properties

| Name              | Type                                          | Description | Notes      |
| ----------------- | --------------------------------------------- | ----------- | ---------- |
| **async_request** | [**AsyncRequestV2Dto**](AsyncRequestV2Dto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.async_request_wrapper_v2_dto import AsyncRequestWrapperV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncRequestWrapperV2Dto from a JSON string
async_request_wrapper_v2_dto_instance = AsyncRequestWrapperV2Dto.from_json(json)
# print the JSON string representation of the object
print AsyncRequestWrapperV2Dto.to_json()

# convert the object into a dict
async_request_wrapper_v2_dto_dict = async_request_wrapper_v2_dto_instance.to_dict()
# create an instance of AsyncRequestWrapperV2Dto from a dict
async_request_wrapper_v2_dto_from_dict = AsyncRequestWrapperV2Dto.from_dict(async_request_wrapper_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
