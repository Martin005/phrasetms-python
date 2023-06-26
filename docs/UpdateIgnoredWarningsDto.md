# UpdateIgnoredWarningsDto

## Properties

| Name          | Type                                                                    | Description | Notes |
| ------------- | ----------------------------------------------------------------------- | ----------- | ----- |
| **job_parts** | [**List[UpdateIgnoredJobPartSegment]**](UpdateIgnoredJobPartSegment.md) |             |

## Example

```python
from phrasetms_client.models.update_ignored_warnings_dto import UpdateIgnoredWarningsDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIgnoredWarningsDto from a JSON string
update_ignored_warnings_dto_instance = UpdateIgnoredWarningsDto.from_json(json)
# print the JSON string representation of the object
print UpdateIgnoredWarningsDto.to_json()

# convert the object into a dict
update_ignored_warnings_dto_dict = update_ignored_warnings_dto_instance.to_dict()
# create an instance of UpdateIgnoredWarningsDto from a dict
update_ignored_warnings_dto_from_dict = UpdateIgnoredWarningsDto.from_dict(update_ignored_warnings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
