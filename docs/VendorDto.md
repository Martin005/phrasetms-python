# VendorDto

## Properties

| Name                | Type                                                        | Description | Notes      |
| ------------------- | ----------------------------------------------------------- | ----------- | ---------- |
| **id**              | **str**                                                     |             | [optional] |
| **uid**             | **str**                                                     |             | [optional] |
| **name**            | **str**                                                     |             | [optional] |
| **vendor_token**    | **str**                                                     |             | [optional] |
| **price_list**      | [**PriceListReference**](PriceListReference.md)             |             | [optional] |
| **net_rate_scheme** | [**DiscountSchemeReference**](DiscountSchemeReference.md)   |             | [optional] |
| **source_locales**  | **List[str]**                                               |             | [optional] |
| **target_locales**  | **List[str]**                                               |             | [optional] |
| **clients**         | [**List[ClientReference]**](ClientReference.md)             |             | [optional] |
| **domains**         | [**List[DomainReference]**](DomainReference.md)             |             | [optional] |
| **sub_domains**     | [**List[SubDomainReference]**](SubDomainReference.md)       |             | [optional] |
| **workflow_steps**  | [**List[WorkflowStepReference]**](WorkflowStepReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.vendor_dto import VendorDto

# TODO update the JSON string below
json = "{}"
# create an instance of VendorDto from a JSON string
vendor_dto_instance = VendorDto.from_json(json)
# print the JSON string representation of the object
print VendorDto.to_json()

# convert the object into a dict
vendor_dto_dict = vendor_dto_instance.to_dict()
# create an instance of VendorDto from a dict
vendor_dto_from_dict = VendorDto.from_dict(vendor_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
