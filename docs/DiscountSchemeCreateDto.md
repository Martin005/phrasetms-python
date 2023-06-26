# DiscountSchemeCreateDto

## Properties

| Name                          | Type                                                                            | Description | Notes      |
| ----------------------------- | ------------------------------------------------------------------------------- | ----------- | ---------- |
| **name**                      | **str**                                                                         |             |
| **rates**                     | [**DiscountSettingsDto**](DiscountSettingsDto.md)                               |             | [optional] |
| **workflow_step_net_schemes** | [**List[NetRateSchemeWorkflowStepCreate]**](NetRateSchemeWorkflowStepCreate.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.discount_scheme_create_dto import DiscountSchemeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountSchemeCreateDto from a JSON string
discount_scheme_create_dto_instance = DiscountSchemeCreateDto.from_json(json)
# print the JSON string representation of the object
print DiscountSchemeCreateDto.to_json()

# convert the object into a dict
discount_scheme_create_dto_dict = discount_scheme_create_dto_instance.to_dict()
# create an instance of DiscountSchemeCreateDto from a dict
discount_scheme_create_dto_from_dict = DiscountSchemeCreateDto.from_dict(discount_scheme_create_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
