# AsyncRequestV2Dto

## Properties

| Name               | Type                                            | Description | Notes      |
| ------------------ | ----------------------------------------------- | ----------- | ---------- |
| **id**             | **str**                                         |             | [optional] |
| **created_by**     | [**UserReference**](UserReference.md)           |             | [optional] |
| **date_created**   | **datetime**                                    |             | [optional] |
| **action**         | **str**                                         |             | [optional] |
| **async_response** | [**AsyncResponseV2Dto**](AsyncResponseV2Dto.md) |             | [optional] |
| **parent**         | [**AsyncRequestV2Dto**](AsyncRequestV2Dto.md)   |             | [optional] |
| **project**        | [**ProjectReference**](ProjectReference.md)     |             | [optional] |

## Example

```python
from phrasetms_client.models.async_request_v2_dto import AsyncRequestV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncRequestV2Dto from a JSON string
async_request_v2_dto_instance = AsyncRequestV2Dto.from_json(json)
# print the JSON string representation of the object
print AsyncRequestV2Dto.to_json()

# convert the object into a dict
async_request_v2_dto_dict = async_request_v2_dto_instance.to_dict()
# create an instance of AsyncRequestV2Dto from a dict
async_request_v2_dto_from_dict = AsyncRequestV2Dto.from_dict(async_request_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
