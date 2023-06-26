# QuoteUnitsDto

## Properties

| Name                      | Type                              | Description | Notes      |
| ------------------------- | --------------------------------- | ----------- | ---------- |
| **analyse_language_part** | [**IdReference**](IdReference.md) |             |
| **value**                 | **float**                         |             | [optional] |

## Example

```python
from phrasetms_client.models.quote_units_dto import QuoteUnitsDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteUnitsDto from a JSON string
quote_units_dto_instance = QuoteUnitsDto.from_json(json)
# print the JSON string representation of the object
print QuoteUnitsDto.to_json()

# convert the object into a dict
quote_units_dto_dict = quote_units_dto_instance.to_dict()
# create an instance of QuoteUnitsDto from a dict
quote_units_dto_from_dict = QuoteUnitsDto.from_dict(quote_units_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
