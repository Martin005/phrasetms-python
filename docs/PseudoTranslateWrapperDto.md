# PseudoTranslateWrapperDto

## Properties

| Name                 | Type                                                            | Description | Notes |
| -------------------- | --------------------------------------------------------------- | ----------- | ----- |
| **job_parts**        | [**JobPartReadyReferences**](JobPartReadyReferences.md)         |             |
| **pseudo_translate** | [**PseudoTranslateActionDtoV2**](PseudoTranslateActionDtoV2.md) |             |

## Example

```python
from phrasetms_client.models.pseudo_translate_wrapper_dto import PseudoTranslateWrapperDto

# TODO update the JSON string below
json = "{}"
# create an instance of PseudoTranslateWrapperDto from a JSON string
pseudo_translate_wrapper_dto_instance = PseudoTranslateWrapperDto.from_json(json)
# print the JSON string representation of the object
print PseudoTranslateWrapperDto.to_json()

# convert the object into a dict
pseudo_translate_wrapper_dto_dict = pseudo_translate_wrapper_dto_instance.to_dict()
# create an instance of PseudoTranslateWrapperDto from a dict
pseudo_translate_wrapper_dto_from_dict = PseudoTranslateWrapperDto.from_dict(pseudo_translate_wrapper_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
