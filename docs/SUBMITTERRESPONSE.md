# SUBMITTERRESPONSE

## Properties

| Name                                         | Type                                    | Description | Notes      |
| -------------------------------------------- | --------------------------------------- | ----------- | ---------- |
| **automation_widgets**                       | [**List[IdReference]**](IdReference.md) |             |
| **project_view_created_by_other_submitters** | **bool**                                |             | [optional] |

## Example

```python
from phrasetms_client.models.submitterresponse import SUBMITTERRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of SUBMITTERRESPONSE from a JSON string
submitterresponse_instance = SUBMITTERRESPONSE.from_json(json)
# print the JSON string representation of the object
print SUBMITTERRESPONSE.to_json()

# convert the object into a dict
submitterresponse_dict = submitterresponse_instance.to_dict()
# create an instance of SUBMITTERRESPONSE from a dict
submitterresponse_from_dict = SUBMITTERRESPONSE.from_dict(submitterresponse_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
