# ProvidersPerLanguage

## Properties

| Name               | Type                                                | Description | Notes      |
| ------------------ | --------------------------------------------------- | ----------- | ---------- |
| **target_lang**    | **str**                                             |             | [optional] |
| **providers**      | [**List[ProviderReference]**](ProviderReference.md) |             | [optional] |
| **assigned_users** | [**List[User]**](User.md)                           |             | [optional] |

## Example

```python
from phrasetms_client.models.providers_per_language import ProvidersPerLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidersPerLanguage from a JSON string
providers_per_language_instance = ProvidersPerLanguage.from_json(json)
# print the JSON string representation of the object
print ProvidersPerLanguage.to_json()

# convert the object into a dict
providers_per_language_dict = providers_per_language_instance.to_dict()
# create an instance of ProvidersPerLanguage from a dict
providers_per_language_from_dict = ProvidersPerLanguage.from_dict(providers_per_language_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
