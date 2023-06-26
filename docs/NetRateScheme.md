# NetRateScheme

## Properties

| Name                          | Type                                                                                  | Description | Notes      |
| ----------------------------- | ------------------------------------------------------------------------------------- | ----------- | ---------- |
| **id**                        | **str**                                                                               |             | [optional] |
| **uid**                       | **str**                                                                               |             | [optional] |
| **name**                      | **str**                                                                               |             | [optional] |
| **organization**              | [**OrganizationReference**](OrganizationReference.md)                                 |             | [optional] |
| **date_created**              | **datetime**                                                                          |             | [optional] |
| **created_by**                | [**UserReference**](UserReference.md)                                                 |             | [optional] |
| **workflow_step_net_schemes** | [**List[NetRateSchemeWorkflowStepReference]**](NetRateSchemeWorkflowStepReference.md) |             | [optional] |
| **rates**                     | [**DiscountSettingsDto**](DiscountSettingsDto.md)                                     |             | [optional] |

## Example

```python
from phrasetms_client.models.net_rate_scheme import NetRateScheme

# TODO update the JSON string below
json = "{}"
# create an instance of NetRateScheme from a JSON string
net_rate_scheme_instance = NetRateScheme.from_json(json)
# print the JSON string representation of the object
print NetRateScheme.to_json()

# convert the object into a dict
net_rate_scheme_dict = net_rate_scheme_instance.to_dict()
# create an instance of NetRateScheme from a dict
net_rate_scheme_from_dict = NetRateScheme.from_dict(net_rate_scheme_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
