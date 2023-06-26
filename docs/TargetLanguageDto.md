# TargetLanguageDto

## Properties

| Name         | Type    | Description | Notes |
| ------------ | ------- | ----------- | ----- |
| **language** | **str** |             |

## Example

```python
from phrasetms_client.models.target_language_dto import TargetLanguageDto

# TODO update the JSON string below
json = "{}"
# create an instance of TargetLanguageDto from a JSON string
target_language_dto_instance = TargetLanguageDto.from_json(json)
# print the JSON string representation of the object
print TargetLanguageDto.to_json()

# convert the object into a dict
target_language_dto_dict = target_language_dto_instance.to_dict()
# create an instance of TargetLanguageDto from a dict
target_language_dto_from_dict = TargetLanguageDto.from_dict(target_language_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
