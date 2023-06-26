# PageDtoProviderReference

## Properties

| Name                   | Type                                                | Description | Notes      |
| ---------------------- | --------------------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                             |             | [optional] |
| **total_pages**        | **int**                                             |             | [optional] |
| **page_size**          | **int**                                             |             | [optional] |
| **page_number**        | **int**                                             |             | [optional] |
| **number_of_elements** | **int**                                             |             | [optional] |
| **content**            | [**List[ProviderReference]**](ProviderReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_provider_reference import PageDtoProviderReference

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoProviderReference from a JSON string
page_dto_provider_reference_instance = PageDtoProviderReference.from_json(json)
# print the JSON string representation of the object
print PageDtoProviderReference.to_json()

# convert the object into a dict
page_dto_provider_reference_dict = page_dto_provider_reference_instance.to_dict()
# create an instance of PageDtoProviderReference from a dict
page_dto_provider_reference_from_dict = PageDtoProviderReference.from_dict(page_dto_provider_reference_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
