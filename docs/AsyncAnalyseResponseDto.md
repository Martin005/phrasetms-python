# AsyncAnalyseResponseDto

## Properties

| Name              | Type                                      | Description | Notes      |
| ----------------- | ----------------------------------------- | ----------- | ---------- |
| **async_request** | [**AsyncRequestDto**](AsyncRequestDto.md) |             | [optional] |
| **analyse**       | **object**                                |             | [optional] |

## Example

```python
from phrasetms_client.models.async_analyse_response_dto import AsyncAnalyseResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncAnalyseResponseDto from a JSON string
async_analyse_response_dto_instance = AsyncAnalyseResponseDto.from_json(json)
# print the JSON string representation of the object
print AsyncAnalyseResponseDto.to_json()

# convert the object into a dict
async_analyse_response_dto_dict = async_analyse_response_dto_instance.to_dict()
# create an instance of AsyncAnalyseResponseDto from a dict
async_analyse_response_dto_from_dict = AsyncAnalyseResponseDto.from_dict(async_analyse_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
