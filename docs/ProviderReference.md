# ProviderReference

## Properties

| Name     | Type    | Description | Notes                 |
| -------- | ------- | ----------- | --------------------- |
| **type** | **str** |             |
| **id**   | **str** |             | [optional]            |
| **uid**  | **str** |             | [optional] [readonly] |

## Example

```python
from phrasetms_client.models.provider_reference import ProviderReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderReference from a JSON string
provider_reference_instance = ProviderReference.from_json(json)
# print the JSON string representation of the object
print ProviderReference.to_json()

# convert the object into a dict
provider_reference_dict = provider_reference_instance.to_dict()
# create an instance of ProviderReference from a dict
provider_reference_from_dict = ProviderReference.from_dict(provider_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
