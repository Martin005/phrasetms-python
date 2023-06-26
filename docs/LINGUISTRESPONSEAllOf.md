# LINGUISTRESPONSEAllOf

## Properties

| Name                        | Type                                                            | Description | Notes      |
| --------------------------- | --------------------------------------------------------------- | ----------- | ---------- |
| **edit_all_terms_in_tb**    | **bool**                                                        |             | [optional] |
| **edit_translations_in_tm** | **bool**                                                        |             | [optional] |
| **enable_mt**               | **bool**                                                        |             | [optional] |
| **may_reject_jobs**         | **bool**                                                        |             | [optional] |
| **source_locales**          | **List[str]**                                                   |             | [optional] |
| **target_locales**          | **List[str]**                                                   |             | [optional] |
| **workflow_steps**          | [**List[WorkflowStepReferenceV3]**](WorkflowStepReferenceV3.md) |             | [optional] |
| **clients**                 | [**List[ClientReference]**](ClientReference.md)                 |             | [optional] |
| **domains**                 | [**List[DomainReference]**](DomainReference.md)                 |             | [optional] |
| **sub_domains**             | [**List[SubDomainReference]**](SubDomainReference.md)           |             | [optional] |
| **net_rate_scheme**         | [**DiscountSchemeReference**](DiscountSchemeReference.md)       |             | [optional] |
| **translation_price_list**  | [**PriceListReference**](PriceListReference.md)                 |             | [optional] |

## Example

```python
from phrasetms_client.models.linguistresponse_all_of import LINGUISTRESPONSEAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of LINGUISTRESPONSEAllOf from a JSON string
linguistresponse_all_of_instance = LINGUISTRESPONSEAllOf.from_json(json)
# print the JSON string representation of the object
print LINGUISTRESPONSEAllOf.to_json()

# convert the object into a dict
linguistresponse_all_of_dict = linguistresponse_all_of_instance.to_dict()
# create an instance of LINGUISTRESPONSEAllOf from a dict
linguistresponse_all_of_from_dict = LINGUISTRESPONSEAllOf.from_dict(linguistresponse_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
