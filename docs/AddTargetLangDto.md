# AddTargetLangDto

## Properties

| Name             | Type          | Description | Notes      |
| ---------------- | ------------- | ----------- | ---------- |
| **target_langs** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.add_target_lang_dto import AddTargetLangDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddTargetLangDto from a JSON string
add_target_lang_dto_instance = AddTargetLangDto.from_json(json)
# print the JSON string representation of the object
print AddTargetLangDto.to_json()

# convert the object into a dict
add_target_lang_dto_dict = add_target_lang_dto_instance.to_dict()
# create an instance of AddTargetLangDto from a dict
add_target_lang_dto_from_dict = AddTargetLangDto.from_dict(add_target_lang_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
