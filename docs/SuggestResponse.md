# SuggestResponse

## Properties

| Name            | Type                                  | Description | Notes      |
| --------------- | ------------------------------------- | ----------- | ---------- |
| **word**        | **str**                               |             | [optional] |
| **suggestions** | [**List[Suggestion]**](Suggestion.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.suggest_response import SuggestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestResponse from a JSON string
suggest_response_instance = SuggestResponse.from_json(json)
# print the JSON string representation of the object
print SuggestResponse.to_json()

# convert the object into a dict
suggest_response_dict = suggest_response_instance.to_dict()
# create an instance of SuggestResponse from a dict
suggest_response_from_dict = SuggestResponse.from_dict(suggest_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
