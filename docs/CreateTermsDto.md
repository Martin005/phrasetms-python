# CreateTermsDto

## Properties

| Name            | Type                                            | Description | Notes |
| --------------- | ----------------------------------------------- | ----------- | ----- |
| **source_term** | [**TermCreateByJobDto**](TermCreateByJobDto.md) |             |
| **target_term** | [**TermCreateByJobDto**](TermCreateByJobDto.md) |             |

## Example

```python
from phrasetms_client.models.create_terms_dto import CreateTermsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTermsDto from a JSON string
create_terms_dto_instance = CreateTermsDto.from_json(json)
# print the JSON string representation of the object
print CreateTermsDto.to_json()

# convert the object into a dict
create_terms_dto_dict = create_terms_dto_instance.to_dict()
# create an instance of CreateTermsDto from a dict
create_terms_dto_from_dict = CreateTermsDto.from_dict(create_terms_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
