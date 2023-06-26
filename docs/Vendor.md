# Vendor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared** | **bool** | Default: false | [optional] 
**progress** | [**ProgressDto**](ProgressDto.md) |  | [optional] 
**client** | [**ClientReference**](ClientReference.md) |  | [optional] 
**cost_center** | [**CostCenterReference**](CostCenterReference.md) |  | [optional] 
**business_unit** | [**BusinessUnitReference**](BusinessUnitReference.md) |  | [optional] 
**date_due** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**purchase_order** | **str** |  | [optional] 
**is_published_on_job_board** | **bool** | Default: false | [optional] 
**note** | **str** |  | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**quality_assurance_settings** | **object** |  | [optional] 
**workflow_steps** | [**List[ProjectWorkflowStepDto]**](ProjectWorkflowStepDto.md) |  | [optional] 
**analyse_settings** | **object** |  | [optional] 
**access_settings** | **object** |  | [optional] 
**financial_settings** | **object** |  | [optional] 
**archived** | **bool** |  | [optional] 
**buyer_owner** | [**USER**](USER.md) |  | [optional] 
**buyer** | [**BuyerReference**](BuyerReference.md) |  | [optional] 

## Example

```python
from phrasetms_client.models.vendor import Vendor

# TODO update the JSON string below
json = "{}"
# create an instance of Vendor from a JSON string
vendor_instance = Vendor.from_json(json)
# print the JSON string representation of the object
print Vendor.to_json()

# convert the object into a dict
vendor_dict = vendor_instance.to_dict()
# create an instance of Vendor from a dict
vendor_from_dict = Vendor.from_dict(vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


