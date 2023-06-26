# SUBMITTEREDITAllOf

## Properties

| Name                                         | Type                                    | Description                                               | Notes      |
| -------------------------------------------- | --------------------------------------- | --------------------------------------------------------- | ---------- |
| **automation_widgets**                       | [**List[IdReference]**](IdReference.md) |                                                           |
| **project_view_created_by_other_submitters** | **bool**                                | View projects created by other Submitters. Default: false | [optional] |

## Example

```python
from phrasetms_client.models.submitteredit_all_of import SUBMITTEREDITAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SUBMITTEREDITAllOf from a JSON string
submitteredit_all_of_instance = SUBMITTEREDITAllOf.from_json(json)
# print the JSON string representation of the object
print SUBMITTEREDITAllOf.to_json()

# convert the object into a dict
submitteredit_all_of_dict = submitteredit_all_of_instance.to_dict()
# create an instance of SUBMITTEREDITAllOf from a dict
submitteredit_all_of_from_dict = SUBMITTEREDITAllOf.from_dict(submitteredit_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
