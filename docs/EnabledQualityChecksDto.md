# EnabledQualityChecksDto

## Properties

| Name               | Type          | Description | Notes      |
| ------------------ | ------------- | ----------- | ---------- |
| **enabled_checks** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.enabled_quality_checks_dto import EnabledQualityChecksDto

# TODO update the JSON string below
json = "{}"
# create an instance of EnabledQualityChecksDto from a JSON string
enabled_quality_checks_dto_instance = EnabledQualityChecksDto.from_json(json)
# print the JSON string representation of the object
print EnabledQualityChecksDto.to_json()

# convert the object into a dict
enabled_quality_checks_dto_dict = enabled_quality_checks_dto_instance.to_dict()
# create an instance of EnabledQualityChecksDto from a dict
enabled_quality_checks_dto_from_dict = EnabledQualityChecksDto.from_dict(enabled_quality_checks_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
