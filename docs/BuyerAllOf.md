# BuyerAllOf

## Properties

| Name                           | Type                                                          | Description    | Notes      |
| ------------------------------ | ------------------------------------------------------------- | -------------- | ---------- |
| **shared**                     | **bool**                                                      | Default: false | [optional] |
| **progress**                   | [**ProgressDto**](ProgressDto.md)                             |                | [optional] |
| **client**                     | [**ClientReference**](ClientReference.md)                     |                | [optional] |
| **cost_center**                | [**CostCenterReference**](CostCenterReference.md)             |                | [optional] |
| **business_unit**              | [**BusinessUnitReference**](BusinessUnitReference.md)         |                | [optional] |
| **date_due**                   | **datetime**                                                  |                | [optional] |
| **status**                     | **str**                                                       |                | [optional] |
| **purchase_order**             | **str**                                                       |                | [optional] |
| **is_published_on_job_board**  | **bool**                                                      | Default: false | [optional] |
| **note**                       | **str**                                                       |                | [optional] |
| **created_by**                 | [**UserReference**](UserReference.md)                         |                | [optional] |
| **quality_assurance_settings** | **object**                                                    |                | [optional] |
| **workflow_steps**             | [**List[ProjectWorkflowStepDto]**](ProjectWorkflowStepDto.md) |                | [optional] |
| **analyse_settings**           | **object**                                                    |                | [optional] |
| **access_settings**            | **object**                                                    |                | [optional] |
| **financial_settings**         | **object**                                                    |                | [optional] |
| **archived**                   | **bool**                                                      |                | [optional] |
| **vendor_owner**               | [**USER**](USER.md)                                           |                | [optional] |
| **vendor**                     | [**VendorReference**](VendorReference.md)                     |                | [optional] |

## Example

```python
from phrasetms_client.models.buyer_all_of import BuyerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerAllOf from a JSON string
buyer_all_of_instance = BuyerAllOf.from_json(json)
# print the JSON string representation of the object
print BuyerAllOf.to_json()

# convert the object into a dict
buyer_all_of_dict = buyer_all_of_instance.to_dict()
# create an instance of BuyerAllOf from a dict
buyer_all_of_from_dict = BuyerAllOf.from_dict(buyer_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
