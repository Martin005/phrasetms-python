# AnalyseRecalculateRequestDto

## Properties

| Name             | Type                                    | Description | Notes      |
| ---------------- | --------------------------------------- | ----------- | ---------- |
| **analyses**     | [**List[IdReference]**](IdReference.md) |             |
| **callback_url** | **str**                                 |             | [optional] |

## Example

```python
from phrasetms_client.models.analyse_recalculate_request_dto import AnalyseRecalculateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseRecalculateRequestDto from a JSON string
analyse_recalculate_request_dto_instance = AnalyseRecalculateRequestDto.from_json(json)
# print the JSON string representation of the object
print AnalyseRecalculateRequestDto.to_json()

# convert the object into a dict
analyse_recalculate_request_dto_dict = analyse_recalculate_request_dto_instance.to_dict()
# create an instance of AnalyseRecalculateRequestDto from a dict
analyse_recalculate_request_dto_from_dict = AnalyseRecalculateRequestDto.from_dict(analyse_recalculate_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
