# QuoteCreateV2Dto

## Properties

| Name                  | Type                                                            | Description | Notes      |
| --------------------- | --------------------------------------------------------------- | ----------- | ---------- |
| **name**              | **str**                                                         |             |
| **project**           | [**UidReference**](UidReference.md)                             |             |
| **analyse**           | [**IdReference**](IdReference.md)                               |             |
| **price_list**        | [**IdReference**](IdReference.md)                               |             |
| **net_rate_scheme**   | [**IdReference**](IdReference.md)                               |             | [optional] |
| **provider**          | [**ProviderReference**](ProviderReference.md)                   |             | [optional] |
| **workflow_settings** | [**List[QuoteWorkflowSettingDto]**](QuoteWorkflowSettingDto.md) |             | [optional] |
| **units**             | [**List[QuoteUnitsDto]**](QuoteUnitsDto.md)                     |             | [optional] |
| **additional_steps**  | **List[str]**                                                   |             | [optional] |

## Example

```python
from phrasetms_client.models.quote_create_v2_dto import QuoteCreateV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteCreateV2Dto from a JSON string
quote_create_v2_dto_instance = QuoteCreateV2Dto.from_json(json)
# print the JSON string representation of the object
print QuoteCreateV2Dto.to_json()

# convert the object into a dict
quote_create_v2_dto_dict = quote_create_v2_dto_instance.to_dict()
# create an instance of QuoteCreateV2Dto from a dict
quote_create_v2_dto_from_dict = QuoteCreateV2Dto.from_dict(quote_create_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
