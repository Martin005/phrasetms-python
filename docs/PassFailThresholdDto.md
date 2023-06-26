# PassFailThresholdDto

## Properties

| Name                     | Type      | Description                                                                                 | Notes |
| ------------------------ | --------- | ------------------------------------------------------------------------------------------- | ----- |
| **min_score_percentage** | **float** | Minimum allowed LQA score in percentage in line with MQM scoring (1 - penalties/word-count) |

## Example

```python
from phrasetms_client.models.pass_fail_threshold_dto import PassFailThresholdDto

# TODO update the JSON string below
json = "{}"
# create an instance of PassFailThresholdDto from a JSON string
pass_fail_threshold_dto_instance = PassFailThresholdDto.from_json(json)
# print the JSON string representation of the object
print PassFailThresholdDto.to_json()

# convert the object into a dict
pass_fail_threshold_dto_dict = pass_fail_threshold_dto_instance.to_dict()
# create an instance of PassFailThresholdDto from a dict
pass_fail_threshold_dto_from_dict = PassFailThresholdDto.from_dict(pass_fail_threshold_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
