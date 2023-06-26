# SetTermBaseDto

## Properties

| Name                             | Type                                    | Description | Notes      |
| -------------------------------- | --------------------------------------- | ----------- | ---------- |
| **read_term_bases**              | [**List[IdReference]**](IdReference.md) |             | [optional] |
| **write_term_base**              | [**IdReference**](IdReference.md)       |             | [optional] |
| **quality_assurance_term_bases** | [**List[IdReference]**](IdReference.md) |             | [optional] |
| **target_lang**                  | **str**                                 |             | [optional] |

## Example

```python
from phrasetms_client.models.set_term_base_dto import SetTermBaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetTermBaseDto from a JSON string
set_term_base_dto_instance = SetTermBaseDto.from_json(json)
# print the JSON string representation of the object
print SetTermBaseDto.to_json()

# convert the object into a dict
set_term_base_dto_dict = set_term_base_dto_instance.to_dict()
# create an instance of SetTermBaseDto from a dict
set_term_base_dto_from_dict = SetTermBaseDto.from_dict(set_term_base_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
