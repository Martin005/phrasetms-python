# PageDtoWebHookDtoV2

## Properties

| Name                   | Type                                      | Description | Notes      |
| ---------------------- | ----------------------------------------- | ----------- | ---------- |
| **total_elements**     | **int**                                   |             | [optional] |
| **total_pages**        | **int**                                   |             | [optional] |
| **page_size**          | **int**                                   |             | [optional] |
| **page_number**        | **int**                                   |             | [optional] |
| **number_of_elements** | **int**                                   |             | [optional] |
| **content**            | [**List[WebHookDtoV2]**](WebHookDtoV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.page_dto_web_hook_dto_v2 import PageDtoWebHookDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of PageDtoWebHookDtoV2 from a JSON string
page_dto_web_hook_dto_v2_instance = PageDtoWebHookDtoV2.from_json(json)
# print the JSON string representation of the object
print PageDtoWebHookDtoV2.to_json()

# convert the object into a dict
page_dto_web_hook_dto_v2_dict = page_dto_web_hook_dto_v2_instance.to_dict()
# create an instance of PageDtoWebHookDtoV2 from a dict
page_dto_web_hook_dto_v2_from_dict = PageDtoWebHookDtoV2.from_dict(page_dto_web_hook_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
