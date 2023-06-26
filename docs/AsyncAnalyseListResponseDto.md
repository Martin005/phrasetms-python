# AsyncAnalyseListResponseDto

## Properties

| Name         | Type                                                            | Description | Notes      |
| ------------ | --------------------------------------------------------------- | ----------- | ---------- |
| **analyses** | [**List[AsyncAnalyseResponseDto]**](AsyncAnalyseResponseDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.async_analyse_list_response_dto import AsyncAnalyseListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncAnalyseListResponseDto from a JSON string
async_analyse_list_response_dto_instance = AsyncAnalyseListResponseDto.from_json(json)
# print the JSON string representation of the object
print AsyncAnalyseListResponseDto.to_json()

# convert the object into a dict
async_analyse_list_response_dto_dict = async_analyse_list_response_dto_instance.to_dict()
# create an instance of AsyncAnalyseListResponseDto from a dict
async_analyse_list_response_dto_from_dict = AsyncAnalyseListResponseDto.from_dict(async_analyse_list_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
