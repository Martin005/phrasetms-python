# SUBMITTEREDIT

## Properties

| Name                                         | Type                                    | Description                                               | Notes      |
| -------------------------------------------- | --------------------------------------- | --------------------------------------------------------- | ---------- |
| **automation_widgets**                       | [**List[IdReference]**](IdReference.md) |                                                           |
| **project_view_created_by_other_submitters** | **bool**                                | View projects created by other Submitters. Default: false | [optional] |

## Example

```python
from phrasetms_client.models.submitteredit import SUBMITTEREDIT

# TODO update the JSON string below
json = "{}"
# create an instance of SUBMITTEREDIT from a JSON string
submitteredit_instance = SUBMITTEREDIT.from_json(json)
# print the JSON string representation of the object
print SUBMITTEREDIT.to_json()

# convert the object into a dict
submitteredit_dict = submitteredit_instance.to_dict()
# create an instance of SUBMITTEREDIT from a dict
submitteredit_from_dict = SUBMITTEREDIT.from_dict(submitteredit_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
