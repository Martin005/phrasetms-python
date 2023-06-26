# QuoteWorkflowSettingDto

## Properties

| Name              | Type                                        | Description | Notes      |
| ----------------- | ------------------------------------------- | ----------- | ---------- |
| **workflow_step** | [**IdReference**](IdReference.md)           |             |
| **units**         | [**List[QuoteUnitsDto]**](QuoteUnitsDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.quote_workflow_setting_dto import QuoteWorkflowSettingDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteWorkflowSettingDto from a JSON string
quote_workflow_setting_dto_instance = QuoteWorkflowSettingDto.from_json(json)
# print the JSON string representation of the object
print QuoteWorkflowSettingDto.to_json()

# convert the object into a dict
quote_workflow_setting_dto_dict = quote_workflow_setting_dto_instance.to_dict()
# create an instance of QuoteWorkflowSettingDto from a dict
quote_workflow_setting_dto_from_dict = QuoteWorkflowSettingDto.from_dict(quote_workflow_setting_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
