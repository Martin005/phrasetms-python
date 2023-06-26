# SUBMITTERAllOf

## Properties

| Name                                         | Type                                    | Description                                                                                              | Notes      |
| -------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------- |
| **automation_widgets**                       | [**List[IdReference]**](IdReference.md) | If no automation widgets are assigned in request the default automation widgets will be assigned instead | [optional] |
| **project_view_created_by_other_submitters** | **bool**                                | View projects created by other Submitters. Default: false                                                | [optional] |

## Example

```python
from phrasetms_client.models.submitter_all_of import SUBMITTERAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SUBMITTERAllOf from a JSON string
submitter_all_of_instance = SUBMITTERAllOf.from_json(json)
# print the JSON string representation of the object
print SUBMITTERAllOf.to_json()

# convert the object into a dict
submitter_all_of_dict = submitter_all_of_instance.to_dict()
# create an instance of SUBMITTERAllOf from a dict
submitter_all_of_from_dict = SUBMITTERAllOf.from_dict(submitter_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
