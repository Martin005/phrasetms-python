# SuggestResponseDto

## Properties

| Name                | Type                                            | Description | Notes      |
| ------------------- | ----------------------------------------------- | ----------- | ---------- |
| **suggest_results** | [**List[SuggestResponse]**](SuggestResponse.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.suggest_response_dto import SuggestResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestResponseDto from a JSON string
suggest_response_dto_instance = SuggestResponseDto.from_json(json)
# print the JSON string representation of the object
print SuggestResponseDto.to_json()

# convert the object into a dict
suggest_response_dto_dict = suggest_response_dto_instance.to_dict()
# create an instance of SuggestResponseDto from a dict
suggest_response_dto_from_dict = SuggestResponseDto.from_dict(suggest_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
