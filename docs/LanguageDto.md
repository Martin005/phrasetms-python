# LanguageDto

## Properties

| Name            | Type    | Description | Notes      |
| --------------- | ------- | ----------- | ---------- |
| **code**        | **str** |             | [optional] |
| **name**        | **str** |             | [optional] |
| **rfc**         | **str** |             | [optional] |
| **android**     | **str** |             | [optional] |
| **android_bcp** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.language_dto import LanguageDto

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageDto from a JSON string
language_dto_instance = LanguageDto.from_json(json)
# print the JSON string representation of the object
print LanguageDto.to_json()

# convert the object into a dict
language_dto_dict = language_dto_instance.to_dict()
# create an instance of LanguageDto from a dict
language_dto_from_dict = LanguageDto.from_dict(language_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
