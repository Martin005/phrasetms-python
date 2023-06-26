# LanguageListDto

envelope for list of languages

## Properties

| Name          | Type                                    | Description | Notes |
| ------------- | --------------------------------------- | ----------- | ----- |
| **languages** | [**List[LanguageDto]**](LanguageDto.md) |             |

## Example

```python
from phrasetms_client.models.language_list_dto import LanguageListDto

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageListDto from a JSON string
language_list_dto_instance = LanguageListDto.from_json(json)
# print the JSON string representation of the object
print LanguageListDto.to_json()

# convert the object into a dict
language_list_dto_dict = language_list_dto_instance.to_dict()
# create an instance of LanguageListDto from a dict
language_list_dto_from_dict = LanguageListDto.from_dict(language_list_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
