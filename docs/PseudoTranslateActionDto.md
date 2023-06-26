# PseudoTranslateActionDto

## Properties

| Name                    | Type                                        | Description | Notes      |
| ----------------------- | ------------------------------------------- | ----------- | ---------- |
| **replacement**         | **str**                                     |             | [optional] |
| **prefix**              | **str**                                     |             | [optional] |
| **suffix**              | **str**                                     |             | [optional] |
| **length**              | **float**                                   |             | [optional] |
| **key_hash_prefix_len** | **int**                                     |             | [optional] |
| **substitution**        | [**List[SubstituteDto]**](SubstituteDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.pseudo_translate_action_dto import PseudoTranslateActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of PseudoTranslateActionDto from a JSON string
pseudo_translate_action_dto_instance = PseudoTranslateActionDto.from_json(json)
# print the JSON string representation of the object
print PseudoTranslateActionDto.to_json()

# convert the object into a dict
pseudo_translate_action_dto_dict = pseudo_translate_action_dto_instance.to_dict()
# create an instance of PseudoTranslateActionDto from a dict
pseudo_translate_action_dto_from_dict = PseudoTranslateActionDto.from_dict(pseudo_translate_action_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
