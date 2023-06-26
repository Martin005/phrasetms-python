# MicrosoftAzure

## Properties

| Name                  | Type    | Description                       | Notes |
| --------------------- | ------- | --------------------------------- | ----- |
| **connection_string** | **str** | Microsoft azure connection string |

## Example

```python
from phrasetms_client.models.microsoft_azure import MicrosoftAzure

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftAzure from a JSON string
microsoft_azure_instance = MicrosoftAzure.from_json(json)
# print the JSON string representation of the object
print MicrosoftAzure.to_json()

# convert the object into a dict
microsoft_azure_dict = microsoft_azure_instance.to_dict()
# create an instance of MicrosoftAzure from a dict
microsoft_azure_from_dict = MicrosoftAzure.from_dict(microsoft_azure_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
