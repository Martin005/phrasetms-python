# BusinessUnitEditDto

## Properties

| Name     | Type    | Description | Notes |
| -------- | ------- | ----------- | ----- |
| **name** | **str** |             |

## Example

```python
from phrasetms_client.models.business_unit_edit_dto import BusinessUnitEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessUnitEditDto from a JSON string
business_unit_edit_dto_instance = BusinessUnitEditDto.from_json(json)
# print the JSON string representation of the object
print BusinessUnitEditDto.to_json()

# convert the object into a dict
business_unit_edit_dto_dict = business_unit_edit_dto_instance.to_dict()
# create an instance of BusinessUnitEditDto from a dict
business_unit_edit_dto_from_dict = BusinessUnitEditDto.from_dict(business_unit_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
