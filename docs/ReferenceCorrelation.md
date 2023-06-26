# ReferenceCorrelation

## Properties

| Name     | Type    | Description | Notes      |
| -------- | ------- | ----------- | ---------- |
| **uid**  | **str** |             | [optional] |
| **role** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.reference_correlation import ReferenceCorrelation

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceCorrelation from a JSON string
reference_correlation_instance = ReferenceCorrelation.from_json(json)
# print the JSON string representation of the object
print ReferenceCorrelation.to_json()

# convert the object into a dict
reference_correlation_dict = reference_correlation_instance.to_dict()
# create an instance of ReferenceCorrelation from a dict
reference_correlation_from_dict = ReferenceCorrelation.from_dict(reference_correlation_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
