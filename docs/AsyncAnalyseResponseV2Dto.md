# AsyncAnalyseResponseV2Dto

## Properties

| Name              | Type                                          | Description | Notes      |
| ----------------- | --------------------------------------------- | ----------- | ---------- |
| **async_request** | [**AsyncRequestV2Dto**](AsyncRequestV2Dto.md) |             | [optional] |
| **analyse**       | **object**                                    |             | [optional] |

## Example

```python
from phrasetms_client.models.async_analyse_response_v2_dto import AsyncAnalyseResponseV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncAnalyseResponseV2Dto from a JSON string
async_analyse_response_v2_dto_instance = AsyncAnalyseResponseV2Dto.from_json(json)
# print the JSON string representation of the object
print AsyncAnalyseResponseV2Dto.to_json()

# convert the object into a dict
async_analyse_response_v2_dto_dict = async_analyse_response_v2_dto_instance.to_dict()
# create an instance of AsyncAnalyseResponseV2Dto from a dict
async_analyse_response_v2_dto_from_dict = AsyncAnalyseResponseV2Dto.from_dict(async_analyse_response_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
