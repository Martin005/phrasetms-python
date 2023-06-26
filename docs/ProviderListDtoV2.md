# ProviderListDtoV2

## Properties

| Name          | Type                          | Description | Notes      |
| ------------- | ----------------------------- | ----------- | ---------- |
| **providers** | [**Providers**](Providers.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.provider_list_dto_v2 import ProviderListDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderListDtoV2 from a JSON string
provider_list_dto_v2_instance = ProviderListDtoV2.from_json(json)
# print the JSON string representation of the object
print ProviderListDtoV2.to_json()

# convert the object into a dict
provider_list_dto_v2_dict = provider_list_dto_v2_instance.to_dict()
# create an instance of ProviderListDtoV2 from a dict
provider_list_dto_v2_from_dict = ProviderListDtoV2.from_dict(provider_list_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
