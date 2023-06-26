# Providers

## Properties

| Name         | Type                                                | Description | Notes      |
| ------------ | --------------------------------------------------- | ----------- | ---------- |
| **all**      | [**List[ProviderReference]**](ProviderReference.md) |             | [optional] |
| **relevant** | [**List[ProviderReference]**](ProviderReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.providers import Providers

# TODO update the JSON string below
json = "{}"
# create an instance of Providers from a JSON string
providers_instance = Providers.from_json(json)
# print the JSON string representation of the object
print Providers.to_json()

# convert the object into a dict
providers_dict = providers_instance.to_dict()
# create an instance of Providers from a dict
providers_from_dict = Providers.from_dict(providers_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
