# AnalyseJobReference

## Properties

| Name         | Type    | Description | Notes      |
| ------------ | ------- | ----------- | ---------- |
| **uid**      | **str** |             | [optional] |
| **filename** | **str** |             | [optional] |
| **inner_id** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.analyse_job_reference import AnalyseJobReference

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseJobReference from a JSON string
analyse_job_reference_instance = AnalyseJobReference.from_json(json)
# print the JSON string representation of the object
print AnalyseJobReference.to_json()

# convert the object into a dict
analyse_job_reference_dict = analyse_job_reference_instance.to_dict()
# create an instance of AnalyseJobReference from a dict
analyse_job_reference_from_dict = AnalyseJobReference.from_dict(analyse_job_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
