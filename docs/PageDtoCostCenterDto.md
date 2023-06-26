# PageDtoCostCenterDto

## Properties

| Name                   | Type                                        | Description | Notes      |
| ---------------------- | ------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                     |             | [optional] |
| **total_pages**        | **int**                                     |             | [optional] |
| **page_size**          | **int**                                     |             | [optional] |
| **page_number**        | **int**                                     |             | [optional] |
| **number_of_elements** | **int**                                     |             | [optional] |
| **content**            | [**List[CostCenterDto]**](CostCenterDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_cost_center_dto import PageDtoCostCenterDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoCostCenterDto from a JSON string
page_dto_cost_center_dto_instance = PageDtoCostCenterDto.from_json(json)
# print the JSON string representation of the object
print PageDtoCostCenterDto.to_json()

# convert the object into a dict
page_dto_cost_center_dto_dict = page_dto_cost_center_dto_instance.to_dict()
# create an instance of PageDtoCostCenterDto from a dict
page_dto_cost_center_dto_from_dict = PageDtoCostCenterDto.from_dict(page_dto_cost_center_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
