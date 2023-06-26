# BusinessUnitReference

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **name** | **str** |             | [optional] |
| **id**   | **str** |             | [optional] |
| **uid**  | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.business_unit_reference import BusinessUnitReference

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessUnitReference from a JSON string
business_unit_reference_instance = BusinessUnitReference.from_json(json)
# print the JSON string representation of the object
print BusinessUnitReference.to_json()

# convert the object into a dict
business_unit_reference_dict = business_unit_reference_instance.to_dict()
# create an instance of BusinessUnitReference from a dict
business_unit_reference_from_dict = BusinessUnitReference.from_dict(business_unit_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
