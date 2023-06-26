# SUBMITTER

## Properties

| Name                                         | Type                                    | Description                                                                                              | Notes      |
| -------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------- |
| **automation_widgets**                       | [**List[IdReference]**](IdReference.md) | If no automation widgets are assigned in request the default automation widgets will be assigned instead | [optional] |
| **project_view_created_by_other_submitters** | **bool**                                | View projects created by other Submitters. Default: false                                                | [optional] |

## Example

```python
from phrasetms_client.models.submitter import SUBMITTER

# TODO update the JSON string below
json = "{}"
# create an instance of SUBMITTER from a JSON string
submitter_instance = SUBMITTER.from_json(json)
# print the JSON string representation of the object
print SUBMITTER.to_json()

# convert the object into a dict
submitter_dict = submitter_instance.to_dict()
# create an instance of SUBMITTER from a dict
submitter_from_dict = SUBMITTER.from_dict(submitter_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
