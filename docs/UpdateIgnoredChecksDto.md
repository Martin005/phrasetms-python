# UpdateIgnoredChecksDto

## Properties

| Name              | Type                                        | Description | Notes |
| ----------------- | ------------------------------------------- | ----------- | ----- |
| **segment**       | [**SegmentReference**](SegmentReference.md) |             |
| **warning_types** | **List[str]**                               |             |

## Example

```python
from phrasetms_client.models.update_ignored_checks_dto import UpdateIgnoredChecksDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIgnoredChecksDto from a JSON string
update_ignored_checks_dto_instance = UpdateIgnoredChecksDto.from_json(json)
# print the JSON string representation of the object
print UpdateIgnoredChecksDto.to_json()

# convert the object into a dict
update_ignored_checks_dto_dict = update_ignored_checks_dto_instance.to_dict()
# create an instance of UpdateIgnoredChecksDto from a dict
update_ignored_checks_dto_from_dict = UpdateIgnoredChecksDto.from_dict(update_ignored_checks_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
