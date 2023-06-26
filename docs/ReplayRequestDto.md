# ReplayRequestDto

## Properties

| Name              | Type                                      | Description | Notes      |
| ----------------- | ----------------------------------------- | ----------- | ---------- |
| **webhook_calls** | [**List[UidReference]**](UidReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.replay_request_dto import ReplayRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayRequestDto from a JSON string
replay_request_dto_instance = ReplayRequestDto.from_json(json)
# print the JSON string representation of the object
print ReplayRequestDto.to_json()

# convert the object into a dict
replay_request_dto_dict = replay_request_dto_instance.to_dict()
# create an instance of ReplayRequestDto from a dict
replay_request_dto_from_dict = ReplayRequestDto.from_dict(replay_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
