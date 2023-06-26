# PseudoTranslateActionDtoV2

## Properties

| Name                    | Type                                            | Description | Notes      |
| ----------------------- | ----------------------------------------------- | ----------- | ---------- |
| **replacement**         | **str**                                         |             | [optional] |
| **prefix**              | **str**                                         |             | [optional] |
| **suffix**              | **str**                                         |             | [optional] |
| **length**              | **float**                                       |             | [optional] |
| **key_hash_prefix_len** | **int**                                         |             | [optional] |
| **substitution**        | [**List[SubstituteDtoV2]**](SubstituteDtoV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.pseudo_translate_action_dto_v2 import PseudoTranslateActionDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of PseudoTranslateActionDtoV2 from a JSON string
pseudo_translate_action_dto_v2_instance = PseudoTranslateActionDtoV2.from_json(json)
# print the JSON string representation of the object
print PseudoTranslateActionDtoV2.to_json()

# convert the object into a dict
pseudo_translate_action_dto_v2_dict = pseudo_translate_action_dto_v2_instance.to_dict()
# create an instance of PseudoTranslateActionDtoV2 from a dict
pseudo_translate_action_dto_v2_from_dict = PseudoTranslateActionDtoV2.from_dict(pseudo_translate_action_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
