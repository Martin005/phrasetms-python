# TermPairDto

## Properties

| Name            | Type                      | Description | Notes |
| --------------- | ------------------------- | ----------- | ----- |
| **source_term** | [**TermDto**](TermDto.md) |             |
| **target_term** | [**TermDto**](TermDto.md) |             |

## Example

```python
from phrasetms_client.models.term_pair_dto import TermPairDto

# TODO update the JSON string below
json = "{}"
# create an instance of TermPairDto from a JSON string
term_pair_dto_instance = TermPairDto.from_json(json)
# print the JSON string representation of the object
print TermPairDto.to_json()

# convert the object into a dict
term_pair_dto_dict = term_pair_dto_instance.to_dict()
# create an instance of TermPairDto from a dict
term_pair_dto_from_dict = TermPairDto.from_dict(term_pair_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
