# QuoteDto

## Properties

| Name                   | Type                                                        | Description | Notes      |
| ---------------------- | ----------------------------------------------------------- | ----------- | ---------- |
| **id**                 | **int**                                                     |             | [optional] |
| **uid**                | **str**                                                     |             | [optional] |
| **name**               | **str**                                                     |             | [optional] |
| **status**             | **str**                                                     |             | [optional] |
| **currency**           | **str**                                                     |             | [optional] |
| **billing_unit**       | **str**                                                     |             | [optional] |
| **created_by**         | [**UserReference**](UserReference.md)                       |             | [optional] |
| **date_created**       | **datetime**                                                |             | [optional] |
| **total_price**        | **float**                                                   |             | [optional] |
| **net_rate_scheme**    | [**NetRateSchemeReference**](NetRateSchemeReference.md)     |             | [optional] |
| **price_list**         | [**PriceListReference**](PriceListReference.md)             |             | [optional] |
| **workflow_step_list** | [**List[WorkflowStepReference]**](WorkflowStepReference.md) |             | [optional] |
| **provider**           | [**ProviderReference**](ProviderReference.md)               |             | [optional] |
| **customer_email**     | **str**                                                     |             | [optional] |
| **quote_type**         | **str**                                                     |             | [optional] |
| **editable**           | **bool**                                                    |             | [optional] |
| **outdated**           | **bool**                                                    |             | [optional] |

## Example

```python
from phrasetms_client.models.quote_dto import QuoteDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDto from a JSON string
quote_dto_instance = QuoteDto.from_json(json)
# print the JSON string representation of the object
print QuoteDto.to_json()

# convert the object into a dict
quote_dto_dict = quote_dto_instance.to_dict()
# create an instance of QuoteDto from a dict
quote_dto_from_dict = QuoteDto.from_dict(quote_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
