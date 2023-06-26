# SUBMITTERRESPONSEAllOf

## Properties

| Name                                         | Type                                    | Description | Notes      |
| -------------------------------------------- | --------------------------------------- | ----------- | ---------- |
| **automation_widgets**                       | [**List[IdReference]**](IdReference.md) |             |
| **project_view_created_by_other_submitters** | **bool**                                |             | [optional] |

## Example

```python
from phrasetms_client.models.submitterresponse_all_of import SUBMITTERRESPONSEAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SUBMITTERRESPONSEAllOf from a JSON string
submitterresponse_all_of_instance = SUBMITTERRESPONSEAllOf.from_json(json)
# print the JSON string representation of the object
print SUBMITTERRESPONSEAllOf.to_json()

# convert the object into a dict
submitterresponse_all_of_dict = submitterresponse_all_of_instance.to_dict()
# create an instance of SUBMITTERRESPONSEAllOf from a dict
submitterresponse_all_of_from_dict = SUBMITTERRESPONSEAllOf.from_dict(submitterresponse_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
