# SuggestRequestDto

## Properties

| Name                | Type          | Description | Notes      |
| ------------------- | ------------- | ----------- | ---------- |
| **lang**            | **str**       |             |
| **words**           | **List[str]** |             |
| **reference_texts** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.suggest_request_dto import SuggestRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestRequestDto from a JSON string
suggest_request_dto_instance = SuggestRequestDto.from_json(json)
# print the JSON string representation of the object
print SuggestRequestDto.to_json()

# convert the object into a dict
suggest_request_dto_dict = suggest_request_dto_instance.to_dict()
# create an instance of SuggestRequestDto from a dict
suggest_request_dto_from_dict = SuggestRequestDto.from_dict(suggest_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
